# 06 - Docker en Produccion

## Contenido

1. [Minimizar el tamanio de imagenes](#1-minimizar-el-tamanio-de-imagenes)
2. [Seguridad: usuario no-root](#2-seguridad-usuario-no-root)
3. [Health checks](#3-health-checks)
4. [Logging en produccion](#4-logging-en-produccion)
5. [Docker Registries](#5-docker-registries)
6. [Seguridad y escaneo de vulnerabilidades](#6-seguridad-y-escaneo-de-vulnerabilidades)
7. [CI/CD con Docker](#7-cicd-con-docker)

---

## 1. Minimizar el tamanio de imagenes

El tamanio de la imagen impacta directamente en:
- Velocidad de despliegue (download mas rapido)
- Superficie de ataque (menos paquetes = menos vulnerabilidades)
- Costo de almacenamiento en el registry

### Estrategias de reduccion

```
  IMAGEN SIN OPTIMIZAR              IMAGEN OPTIMIZADA
  ====================              ==================

  FROM node:20                      FROM node:20-alpine AS build
  COPY . .                          WORKDIR /app
  RUN npm install                   COPY package*.json ./
  CMD ["node", "app.js"]            RUN npm ci
                                    COPY . .
  Tamanio: ~1.1 GB                  RUN npm run build

                                    FROM node:20-alpine
                                    WORKDIR /app
                                    COPY --from=build /app/dist ./dist
                                    COPY --from=build /app/package*.json ./
                                    RUN npm ci --omit=dev
                                    CMD ["node", "dist/index.js"]

                                    Tamanio: ~80 MB
```

| Tecnica | Ahorro estimado |
|---------|-----------------|
| Usar Alpine o slim | 70-90% vs imagen completa |
| Multi-stage build | 50-80% (solo lo necesario) |
| Combinar RUN con `&&` | 5-20% (menos capas) |
| Limpiar cache de apt | 10-30% (sin archivos temporales) |
| .dockerignore | Evita copiar archivos innecesarios |
| `npm ci --omit=dev` | Sin devDependencies |

### Comparacion de tamanios base

```
  ┌──────────────────────┬───────────┐
  │ Imagen               │ Tamanio   │
  ├──────────────────────┼───────────┤
  │ node:20              │ ~1.1 GB   │
  │ node:20-slim         │ ~250 MB   │
  │ node:20-alpine       │ ~130 MB   │
  │ python:3.12          │ ~1.0 GB   │
  │ python:3.12-slim     │ ~150 MB   │
  │ python:3.12-alpine   │ ~60 MB    │
  │ nginx                │ ~190 MB   │
  │ nginx:alpine         │ ~40 MB    │
  │ alpine               │ ~5 MB     │
  └──────────────────────┴───────────┘
```

---

## 2. Seguridad: usuario no-root

Por defecto, los procesos en Docker se ejecutan como **root**. Esto es un
riesgo de seguridad: si un atacante escapa del contenedor, tiene acceso root
en el host.

```dockerfile
# Crear un usuario sin privilegios
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

# Cambiar la propiedad de los archivos de la app
RUN chown -R appuser:appgroup /app

# Cambiar al usuario no-root ANTES del CMD
USER appuser

# A partir de aqui, todo se ejecuta como appuser
CMD ["node", "server.js"]
```

```
  COMO ROOT (peligroso):             COMO USUARIO (seguro):

  ┌─────────────────────┐            ┌─────────────────────┐
  │ Contenedor          │            │ Contenedor          │
  │ PID 1: root         │            │ PID 1: appuser      │
  │                     │            │                     │
  │ Si hay escape ──────│──> root    │ Si hay escape ──────│──> appuser
  │ del contenedor      │   en host  │ del contenedor      │   (limitado)
  └─────────────────────┘            └─────────────────────┘
```

---

## 3. Health checks

Los health checks permiten a Docker verificar si la aplicacion dentro del
contenedor esta funcionando correctamente (no solo que el proceso exista).

```dockerfile
HEALTHCHECK --interval=30s --timeout=3s --start-period=10s --retries=3 \
  CMD wget --no-verbose --tries=1 --spider http://localhost:3000/health || exit 1
```

| Parametro | Valor por defecto | Descripcion |
|-----------|-------------------|-------------|
| `--interval` | 30s | Frecuencia de verificacion |
| `--timeout` | 30s | Tiempo maximo de espera |
| `--start-period` | 0s | Periodo de gracia al inicio |
| `--retries` | 3 | Intentos antes de marcar unhealthy |

### Estados del health check

```
  starting ──> healthy ──> unhealthy
      |             |           |
      |        (check OK)  (3 fallos)
      |             |           |
      +── periodo ──+     Docker puede
         de gracia        reiniciar el
                          contenedor
                          (restart: unless-stopped)
```

### Health check en Docker Compose

```yaml
services:
  web:
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:3000/health"]
      interval: 30s
      timeout: 5s
      retries: 3
      start_period: 10s
```

---

## 4. Logging en produccion

### Drivers de logging

Docker soporta multiples drivers de logging:

| Driver | Destino | Uso |
|--------|---------|-----|
| `json-file` | Archivos JSON locales (defecto) | Desarrollo |
| `syslog` | Syslog del sistema | Servidores Linux |
| `fluentd` | Fluentd / Fluent Bit | Centralizacion |
| `awslogs` | CloudWatch (AWS) | Produccion en AWS |
| `gcplogs` | Cloud Logging (GCP) | Produccion en GCP |

```yaml
services:
  web:
    logging:
      driver: json-file
      options:
        max-size: "10m"      # Tamanio maximo por archivo
        max-file: "3"        # Numero maximo de archivos
```

### Buena practica: escribir logs a stdout

Las aplicaciones en contenedores deben escribir sus logs a **stdout/stderr**,
no a archivos. Docker captura automaticamente la salida estandar.

```javascript
// SI: escribir a stdout
console.log(JSON.stringify({ level: 'info', msg: 'Servidor iniciado' }));

// NO: escribir a archivo dentro del contenedor
// fs.writeFileSync('/var/log/app.log', 'Servidor iniciado');
```

---

## 5. Docker Registries

Un registry es un almacen de imagenes Docker. Funciona como npm para paquetes,
pero para imagenes de contenedores.

```
  BUILD                    PUSH                   PULL
  =====                    ====                   ====

  docker build ──> imagen ──> registry ──> servidor de produccion
                               |
                    ┌──────────┼──────────┐
                    |          |          |
               Docker Hub  GitHub    AWS ECR
                            GHCR
```

| Registry | URL | Uso |
|----------|-----|-----|
| **Docker Hub** | hub.docker.com | Imagenes publicas, proyectos personales |
| **GitHub GHCR** | ghcr.io | Integrado con repos de GitHub |
| **AWS ECR** | *.ecr.*.amazonaws.com | Produccion en AWS |
| **Google AR** | *.pkg.dev | Produccion en GCP |
| **Azure ACR** | *.azurecr.io | Produccion en Azure |

### Flujo de push/pull

```bash
# Autenticarse en Docker Hub
docker login

# Etiquetar la imagen con tu usuario
docker tag mi-app:1.0 usuario/mi-app:1.0

# Subir al registry
docker push usuario/mi-app:1.0

# En otro servidor, descargar y ejecutar
docker pull usuario/mi-app:1.0
docker run -d -p 3000:3000 usuario/mi-app:1.0
```

### GitHub Container Registry (GHCR)

```bash
# Autenticarse con token de GitHub
echo $GITHUB_TOKEN | docker login ghcr.io -u USERNAME --password-stdin

# Etiquetar y subir
docker tag mi-app:1.0 ghcr.io/usuario/mi-app:1.0
docker push ghcr.io/usuario/mi-app:1.0
```

---

## 6. Seguridad y escaneo de vulnerabilidades

### Escaneo de imagenes

```bash
# Docker Scout (integrado en Docker Desktop)
docker scout cves mi-app:1.0

# Trivy (herramienta popular de escaneo)
docker run --rm -v /var/run/docker.sock:/var/run/docker.sock \
  aquasec/trivy image mi-app:1.0
```

### Checklist de seguridad

```
  ┌────────────────────────────────────────────────────┐
  │ CHECKLIST DE SEGURIDAD DOCKER                      │
  ├────────────────────────────────────────────────────┤
  │ [ ] Usar imagenes oficiales como base              │
  │ [ ] Fijar versiones de imagen (no :latest)         │
  │ [ ] Ejecutar como usuario no-root (USER)           │
  │ [ ] Escanear vulnerabilidades antes de deploy      │
  │ [ ] No almacenar secretos en la imagen             │
  │ [ ] Usar .dockerignore (excluir .env, .git)        │
  │ [ ] Minimizar paquetes instalados                  │
  │ [ ] Usar multi-stage builds                        │
  │ [ ] Limitar recursos (--memory, --cpus)            │
  │ [ ] Habilitar read-only filesystem donde sea posible│
  └────────────────────────────────────────────────────┘
```

---

## 7. CI/CD con Docker

Docker se integra naturalmente en pipelines de CI/CD:

```
  Pipeline CI/CD con Docker:

  1. Push a main
         |
         v
  2. CI: docker build -t app:$SHA .
         |
         v
  3. CI: docker run app:$SHA npm test
         |
         v
  4. CI: docker push registry/app:$SHA
         |
         v
  5. CD: docker pull registry/app:$SHA
         |
         v
  6. CD: docker compose up -d
         (en servidor de produccion)
```

### Ejemplo con GitHub Actions

```yaml
name: CI/CD
on:
  push:
    branches: [main]

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Login to GHCR
        run: echo ${{ secrets.GITHUB_TOKEN }} | docker login ghcr.io -u ${{ github.actor }} --password-stdin

      - name: Build
        run: docker build -t ghcr.io/${{ github.repository }}:${{ github.sha }} .

      - name: Test
        run: docker run --rm ghcr.io/${{ github.repository }}:${{ github.sha }} npm test

      - name: Push
        run: docker push ghcr.io/${{ github.repository }}:${{ github.sha }}
```

---

## Resumen

En esta seccion aprendiste:

- Usar Alpine y multi-stage builds para reducir el tamanio de imagenes
- Ejecutar procesos como usuario no-root por seguridad
- Configurar health checks para monitorear el estado de la aplicacion
- Escribir logs a stdout para que Docker los capture
- Usar registries (Docker Hub, GHCR) para distribuir imagenes
- Escanear vulnerabilidades con Docker Scout o Trivy
- Integrar Docker en pipelines de CI/CD

Revisa el archivo `Dockerfile.prod` para ver un ejemplo de Dockerfile
optimizado para produccion.

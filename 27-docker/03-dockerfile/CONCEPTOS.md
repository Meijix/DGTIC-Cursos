# 03 - Dockerfile

## Contenido

1. [Que es un Dockerfile?](#1-que-es-un-dockerfile)
2. [Instrucciones principales](#2-instrucciones-principales)
3. [CMD vs ENTRYPOINT](#3-cmd-vs-entrypoint)
4. [Sistema de capas y cache](#4-sistema-de-capas-y-cache)
5. [Multi-stage builds](#5-multi-stage-builds)
6. [.dockerignore](#6-dockerignore)
7. [Buenas practicas](#7-buenas-practicas)

---

## 1. Que es un Dockerfile?

Un Dockerfile es un archivo de texto con instrucciones para construir una imagen
Docker. Cada instruccion crea una **capa** en la imagen. Docker ejecuta las
instrucciones de arriba hacia abajo.

```
  Dockerfile                        Imagen resultante
  ==========                        =================

  FROM node:20-alpine    ──────>    Capa 1: Alpine + Node.js
  WORKDIR /app           ──────>    Capa 2: Crear /app
  COPY package*.json ./  ──────>    Capa 3: Copiar package.json
  RUN npm install        ──────>    Capa 4: Dependencias
  COPY . .               ──────>    Capa 5: Codigo fuente
  CMD ["node", "app.js"] ──────>    Metadata: comando por defecto
```

### Construir una imagen

```bash
# Sintaxis basica
docker build -t mi-app:1.0 .

# -t = tag (nombre:version)
# .  = contexto de build (directorio actual)

# Construir con un Dockerfile diferente
docker build -t mi-app:1.0 -f Dockerfile.prod .
```

---

## 2. Instrucciones principales

### FROM — Imagen base

```dockerfile
FROM node:20-alpine          # Imagen base con Node.js
FROM python:3.12-slim        # Python sobre Debian slim
FROM ubuntu:22.04            # Ubuntu completo
FROM scratch                 # Imagen vacia (para binarios estaticos)
```

### WORKDIR — Directorio de trabajo

```dockerfile
WORKDIR /app                 # Crear y moverse a /app
# Todos los comandos posteriores se ejecutan desde /app
```

### COPY y ADD — Copiar archivos

```dockerfile
COPY package*.json ./        # Copiar archivos al contenedor
COPY src/ ./src/             # Copiar directorio completo
ADD app.tar.gz /app/         # ADD descomprime automaticamente
ADD https://ejemplo.com/f .  # ADD puede descargar URLs (evitar)
```

**Preferir COPY sobre ADD** a menos que necesites descomprimir archivos.

### RUN — Ejecutar comandos durante el build

```dockerfile
RUN npm install              # Instalar dependencias
RUN apt-get update && \
    apt-get install -y curl && \
    rm -rf /var/lib/apt/lists/*   # Combinar para reducir capas
```

### ENV y ARG — Variables

```dockerfile
# ENV: disponible en build Y en el contenedor
ENV NODE_ENV=production
ENV PORT=3000

# ARG: disponible SOLO durante el build
ARG VERSION=1.0
ARG NODE_VERSION=20
```

### EXPOSE — Documentar puertos

```dockerfile
EXPOSE 3000                  # Documenta que la app usa el puerto 3000
# NOTA: NO abre el puerto. Solo es documentacion.
# El puerto se abre con: docker run -p 3000:3000
```

### USER — Usuario no-root

```dockerfile
RUN addgroup -S appgroup && adduser -S appuser -G appgroup
USER appuser                 # Ejecutar como usuario no-root
```

---

## 3. CMD vs ENTRYPOINT

Esta es una de las confusiones mas comunes en Docker:

```
  CMD                                ENTRYPOINT
  ===                                ==========
  Comando por defecto.               Comando FIJO.
  Se puede sobreescribir al          No se sobreescribe facilmente.
  hacer docker run.                  CMD se pasa como argumentos.

  Dockerfile:                        Dockerfile:
  CMD ["node", "app.js"]             ENTRYPOINT ["python"]
                                     CMD ["app.py"]

  docker run mi-app                  docker run mi-app
  -> node app.js                     -> python app.py

  docker run mi-app bash             docker run mi-app test.py
  -> bash (sobreescribe CMD)         -> python test.py (CMD cambia)
```

| Escenario | Usar |
|-----------|------|
| App con comando fijo | `CMD ["node", "server.js"]` |
| Herramienta CLI | `ENTRYPOINT ["python"]` + `CMD ["--help"]` |
| Script de inicio | `ENTRYPOINT ["./entrypoint.sh"]` + `CMD ["start"]` |

---

## 4. Sistema de capas y cache

Docker cachea cada capa del Dockerfile. Si una instruccion no cambio, Docker
reutiliza la capa cacheada. **Si una capa cambia, todas las capas posteriores
se reconstruyen.**

```
  ORDEN INCORRECTO (rebuild lento):

  FROM node:20-alpine
  COPY . .                   <── Cada cambio en el codigo
  RUN npm install            <── invalida esta capa (reinstala todo)

  ORDEN CORRECTO (rebuild rapido):

  FROM node:20-alpine
  COPY package*.json ./      <── Solo cambia si las dependencias cambian
  RUN npm install            <── Se cachea si package.json no cambio
  COPY . .                   <── Solo esta capa se reconstruye al cambiar codigo
```

```
  Build 1 (sin cache):          Build 2 (con cache):
  ┌──────────────────┐           ┌──────────────────┐
  │ FROM node:alpine │ BUILD     │ FROM node:alpine │ CACHE
  ├──────────────────┤           ├──────────────────┤
  │ COPY package*    │ BUILD     │ COPY package*    │ CACHE
  ├──────────────────┤           ├──────────────────┤
  │ RUN npm install  │ BUILD     │ RUN npm install  │ CACHE
  ├──────────────────┤           ├──────────────────┤
  │ COPY . .         │ BUILD     │ COPY . .         │ BUILD (codigo cambio)
  └──────────────────┘           └──────────────────┘
                                 Resultado: mucho mas rapido
```

---

## 5. Multi-stage builds

Los multi-stage builds permiten usar multiples `FROM` en un Dockerfile.
Esto reduce drasticamente el tamanio de la imagen final.

```
  STAGE 1: BUILD                    STAGE 2: PRODUCCION
  ================                  ====================

  FROM node:20 AS build             FROM node:20-alpine
  COPY . .                          COPY --from=build /app/dist ./dist
  RUN npm install                   COPY --from=build /app/node_modules ...
  RUN npm run build                 CMD ["node", "dist/index.js"]

  Contiene:                         Contiene:
  - Codigo fuente                   - Solo los archivos compilados
  - devDependencies                 - Solo dependencias de produccion
  - Herramientas de build           - Imagen Alpine minima
  - ~800 MB                         - ~80 MB
```

```dockerfile
# Ejemplo: aplicacion React
# Stage 1: Build
FROM node:20 AS build
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

# Stage 2: Servir con Nginx
FROM nginx:alpine
COPY --from=build /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

---

## 6. .dockerignore

El archivo `.dockerignore` excluye archivos del contexto de build. Funciona
igual que `.gitignore`.

```
# .dockerignore
node_modules
npm-debug.log
.git
.gitignore
.env
.env.*
Dockerfile
docker-compose*.yml
README.md
.vscode
coverage
dist
```

**Importancia:** Sin `.dockerignore`, el `COPY . .` copiaria `node_modules`
(cientos de MB) al contenedor, haciendo el build lento e innecesario.

---

## 7. Buenas practicas

1. **Usar imagenes Alpine o slim** como base para reducir tamanio
2. **Ordenar instrucciones** de menos a mas cambiante (cache)
3. **Combinar RUN** con `&&` para reducir capas
4. **Copiar package.json antes del codigo** para cachear dependencias
5. **Usar .dockerignore** para excluir archivos innecesarios
6. **No ejecutar como root** en produccion (`USER`)
7. **Usar multi-stage builds** para imagenes de produccion
8. **Fijar versiones** de imagenes base (`node:20.11`, no `node:latest`)

---

## Resumen

En esta seccion aprendiste:

- Un Dockerfile es la receta para construir una imagen
- Cada instruccion crea una capa que Docker puede cachear
- El orden de instrucciones importa para optimizar el cache
- CMD define el comando por defecto; ENTRYPOINT lo fija
- Multi-stage builds reducen el tamanio de la imagen final
- .dockerignore evita copiar archivos innecesarios

Revisa los archivos `Dockerfile` y `Dockerfile.python` para ver ejemplos completos.

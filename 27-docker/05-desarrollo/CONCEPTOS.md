# 05 - Docker para Desarrollo

## Contenido

1. [Docker en el flujo de desarrollo](#1-docker-en-el-flujo-de-desarrollo)
2. [Hot reload con volumenes](#2-hot-reload-con-volumenes)
3. [Debugging en contenedores](#3-debugging-en-contenedores)
4. [Compose para desarrollo vs produccion](#4-compose-para-desarrollo-vs-produccion)
5. [VS Code Dev Containers](#5-vs-code-dev-containers)
6. [Patrones comunes de desarrollo](#6-patrones-comunes-de-desarrollo)

---

## 1. Docker en el flujo de desarrollo

Docker en desarrollo tiene un objetivo simple: que todos los miembros del equipo
trabajen con el **mismo entorno**, sin instalar dependencias en su maquina host.

```
  SIN DOCKER (problemas):              CON DOCKER (solucion):

  Dev 1: Node 18, Postgres 14          Dev 1: docker compose up
  Dev 2: Node 20, Postgres 16          Dev 2: docker compose up
  Dev 3: Node 16, sin Postgres          Dev 3: docker compose up
         "funciona en mi maquina"              Mismo entorno para todos
```

### Flujo tipico de desarrollo con Docker

```
  1. Clonar repo
         |
         v
  2. docker compose up
     (levanta app + DB + cache + todo)
         |
         v
  3. Editar codigo en tu editor favorito
     (los cambios se reflejan al instante via bind mount)
         |
         v
  4. Ver logs: docker compose logs -f web
         |
         v
  5. Detener: docker compose down
```

---

## 2. Hot reload con volumenes

El hot reload permite que los cambios en tu codigo local se reflejen
**instantaneamente** en el contenedor sin necesidad de reconstruir la imagen.

```
  EDITOR (host)                     CONTENEDOR
  =============                     ==========

  src/                              /app/src/
  ├── app.js     ←── bind mount ──→ ├── app.js
  ├── routes/    ←── sincronizado ─→ ├── routes/
  └── utils/     ←── en tiempo real → └── utils/

  Guardas un archivo               nodemon detecta el cambio
  en tu editor                     y reinicia el servidor
```

### Configuracion clave

```yaml
services:
  web:
    build: .
    volumes:
      # Sincronizar codigo fuente
      - ./src:/app/src

      # IMPORTANTE: proteger node_modules del contenedor
      # Sin esto, el bind mount sobreescribiria node_modules
      # con la carpeta local (que puede estar vacia o ser diferente)
      - /app/node_modules

    # Usar nodemon o tsx para auto-reinicio
    command: npx nodemon src/server.js
```

### Por que proteger node_modules?

```
  SIN volume anonimo:               CON volume anonimo:

  Host:                              Host:
  ./node_modules/ (vacio)            ./node_modules/ (vacio)
       |                                  |
  bind mount sobreescribe            bind mount NO afecta
       |                             node_modules del contenedor
       v                                  |
  Contenedor:                        Contenedor:
  /app/node_modules/ (VACIO!)        /app/node_modules/ (completo)
  Error: modulo no encontrado        Funciona correctamente

  Solucion: - /app/node_modules
  (volume anonimo que protege esa carpeta)
```

---

## 3. Debugging en contenedores

### Acceder al contenedor

```bash
# Shell interactivo
docker compose exec web sh

# Ejecutar un comando especifico
docker compose exec web npm test

# Ver logs en tiempo real
docker compose logs -f web

# Ver procesos dentro del contenedor
docker compose top web
```

### Debugging con Node.js (Inspector)

```yaml
services:
  web:
    ports:
      - "3000:3000"
      - "9229:9229"         # Puerto del debugger
    command: node --inspect=0.0.0.0:9229 src/server.js
```

Luego en VS Code: abrir la paleta de comandos > "Attach to Node Process" y
conectar al puerto 9229.

### Debugging con Python (debugpy)

```yaml
services:
  api:
    ports:
      - "8000:8000"
      - "5678:5678"         # Puerto del debugger
    command: python -m debugpy --listen 0.0.0.0:5678 --wait-for-client -m uvicorn main:app
```

---

## 4. Compose para desarrollo vs produccion

Es comun tener archivos Compose separados para cada entorno:

```
  proyecto/
  ├── docker-compose.yml          # Base (servicios comunes)
  ├── docker-compose.dev.yml      # Override para desarrollo
  └── docker-compose.prod.yml     # Override para produccion
```

```
  DESARROLLO                         PRODUCCION
  ===========                        ==========

  ┌─────────────────────┐            ┌─────────────────────┐
  │ Bind mounts (sync)  │            │ COPY (imagen fija)  │
  │ nodemon (hot reload)│            │ node server.js      │
  │ Puerto debugger     │            │ Sin debugger        │
  │ Variables de .env   │            │ Secrets gestionados │
  │ Logs detallados     │            │ Logs estructurados  │
  │ Sin optimizacion    │            │ Multi-stage build   │
  └─────────────────────┘            └─────────────────────┘
```

### Usar multiples archivos Compose

```bash
# Desarrollo: base + override de dev
docker compose -f docker-compose.yml -f docker-compose.dev.yml up

# Produccion: base + override de prod
docker compose -f docker-compose.yml -f docker-compose.prod.yml up -d
```

El segundo archivo **sobreescribe** las propiedades del primero. No necesitas
duplicar toda la configuracion, solo lo que cambia.

---

## 5. VS Code Dev Containers

VS Code Dev Containers permite desarrollar **dentro** de un contenedor Docker.
Tu editor se conecta al contenedor y ejecuta extensiones, terminal y codigo
directamente ahi.

```
  Host (tu maquina)                  Contenedor Docker
  +------------------+               +------------------+
  |  VS Code UI      | ──────────── |  VS Code Server  |
  |  (solo interfaz) |  conexion    |  Extensiones     |
  |                  |  remota      |  Terminal        |
  |                  |              |  Node.js 20     |
  |                  |              |  PostgreSQL CLI  |
  +------------------+               +------------------+
```

### Configuracion

Se define en `.devcontainer/devcontainer.json`:

```json
{
  "name": "Mi Proyecto",
  "dockerComposeFile": "../docker-compose.yml",
  "service": "web",
  "workspaceFolder": "/app",
  "customizations": {
    "vscode": {
      "extensions": [
        "dbaeumer.vscode-eslint",
        "esbenp.prettier-vscode"
      ]
    }
  }
}
```

### Ventajas

- Todos los devs tienen exactamente las mismas extensiones y herramientas
- No necesitas instalar Node, Python, etc. en tu maquina
- El onboarding de nuevos devs es: clonar + abrir en VS Code + "Reopen in Container"

---

## 6. Patrones comunes de desarrollo

### Ejecutar tests

```bash
# Tests en un contenedor temporal
docker compose run --rm web npm test

# Tests con watch mode
docker compose exec web npm test -- --watch
```

### Ejecutar migraciones de base de datos

```bash
# Ejecutar migraciones
docker compose exec web npx prisma migrate dev

# Seed de datos de prueba
docker compose exec web npm run seed
```

### Reinstalar dependencias

```bash
# Si cambias package.json, reconstruir el contenedor
docker compose up --build web

# O eliminar el volume de node_modules y reconstruir
docker compose down
docker volume rm app_node_modules
docker compose up --build
```

---

## Resumen

En esta seccion aprendiste:

- Docker unifica el entorno de desarrollo para todo el equipo
- Los bind mounts permiten hot reload sin reconstruir
- Es clave proteger node_modules con un volume anonimo
- Puedes hacer debugging remoto con puertos del inspector
- Archivos Compose separados para dev y prod (override)
- VS Code Dev Containers permite desarrollar completamente dentro de Docker

Revisa el archivo `docker-compose.dev.yml` para ver un ejemplo de override
para desarrollo.

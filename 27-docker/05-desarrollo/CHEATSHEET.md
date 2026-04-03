# Cheatsheet — 05 Docker para Desarrollo

## Flujo rapido de desarrollo

```bash
docker compose up -d                     # Levantar todo
docker compose logs -f web               # Ver logs de la app
# ... editar codigo (hot reload automatico) ...
docker compose down                      # Detener todo
```

## Hot reload con bind mounts

```yaml
services:
  web:
    volumes:
      - ./src:/app/src            # Sincronizar codigo
      - /app/node_modules         # Proteger node_modules
    command: npx nodemon src/server.js   # Auto-reinicio
```

## Debugging

```bash
# Shell en el contenedor
docker compose exec web sh

# Ejecutar un comando
docker compose exec web npm test

# Logs en tiempo real
docker compose logs -f web

# Procesos del contenedor
docker compose top web
```

## Debugging remoto (Node.js)

```yaml
services:
  web:
    ports:
      - "3000:3000"
      - "9229:9229"               # Puerto inspector
    command: node --inspect=0.0.0.0:9229 src/server.js
```

## Debugging remoto (Python)

```yaml
services:
  api:
    ports:
      - "8000:8000"
      - "5678:5678"               # Puerto debugpy
    command: python -m debugpy --listen 0.0.0.0:5678 -m uvicorn main:app
```

## Multiples archivos Compose (override)

```bash
# Desarrollo
docker compose -f docker-compose.yml -f docker-compose.dev.yml up

# Produccion
docker compose -f docker-compose.yml -f docker-compose.prod.yml up -d
```

## Operaciones comunes

```bash
# Reconstruir despues de cambiar dependencias
docker compose up --build

# Tests en contenedor temporal
docker compose run --rm web npm test

# Migraciones de base de datos
docker compose exec web npx prisma migrate dev

# Reinstalar dependencias (nuclear)
docker compose down
docker volume rm proyecto_node_modules
docker compose up --build
```

## VS Code Dev Containers

```
.devcontainer/
  devcontainer.json       # Configuracion del dev container
```

```json
{
  "name": "Mi Proyecto",
  "dockerComposeFile": "../docker-compose.yml",
  "service": "web",
  "workspaceFolder": "/app"
}
```

## Diferencias dev vs prod

| Aspecto | Desarrollo | Produccion |
|---------|------------|------------|
| Codigo | Bind mount (sync) | COPY en imagen |
| Reinicio | nodemon / hot reload | node server.js |
| Debugger | Puerto expuesto | Sin debugger |
| Build | Sin optimizar | Multi-stage |
| Logs | Detallados | Estructurados |

# Cheatsheet — 06 Docker en Produccion

## Optimizar tamanio de imagen

```dockerfile
# Usar Alpine como base (~5 MB vs ~1 GB)
FROM node:20-alpine

# Multi-stage build: solo copiar lo necesario
FROM node:20 AS build
RUN npm ci && npm run build

FROM node:20-alpine
COPY --from=build /app/dist ./dist
RUN npm ci --omit=dev

# Combinar RUN para reducir capas
RUN apt-get update && \
    apt-get install -y --no-install-recommends curl && \
    rm -rf /var/lib/apt/lists/*
```

## Seguridad: usuario no-root

```dockerfile
RUN addgroup -S appgroup && adduser -S appuser -G appgroup
RUN chown -R appuser:appgroup /app
USER appuser
CMD ["node", "server.js"]
```

## Health checks

```dockerfile
# En Dockerfile
HEALTHCHECK --interval=30s --timeout=3s --retries=3 \
  CMD wget --no-verbose --tries=1 --spider http://localhost:3000/health || exit 1
```

```yaml
# En docker-compose.yml
healthcheck:
  test: ["CMD", "curl", "-f", "http://localhost:3000/health"]
  interval: 30s
  timeout: 5s
  retries: 3
  start_period: 10s
```

## Logging

```yaml
# Limitar tamanio de logs
logging:
  driver: json-file
  options:
    max-size: "10m"
    max-file: "3"
```

Regla: escribir logs a **stdout/stderr**, no a archivos.

## Docker Registries

```bash
# Docker Hub
docker login
docker tag app:1.0 usuario/app:1.0
docker push usuario/app:1.0

# GitHub Container Registry
echo $TOKEN | docker login ghcr.io -u USER --password-stdin
docker tag app:1.0 ghcr.io/usuario/app:1.0
docker push ghcr.io/usuario/app:1.0
```

## Escaneo de vulnerabilidades

```bash
docker scout cves mi-app:1.0                    # Docker Scout
docker run --rm aquasec/trivy image mi-app:1.0   # Trivy
```

## Limitar recursos

```yaml
# docker-compose.yml
services:
  web:
    deploy:
      resources:
        limits:
          cpus: "0.5"       # Maximo 50% de un CPU
          memory: 512M      # Maximo 512 MB de RAM
        reservations:
          cpus: "0.25"
          memory: 256M
```

```bash
# docker run
docker run --memory=512m --cpus=0.5 mi-app
```

## Checklist de produccion

| Verificacion | Comando/Accion |
|--------------|----------------|
| Imagen Alpine/slim | `FROM node:20-alpine` |
| Multi-stage build | Separar build de runtime |
| Usuario no-root | `USER appuser` |
| Health check | `HEALTHCHECK CMD ...` |
| Versiones fijadas | `node:20.11`, no `:latest` |
| .dockerignore | Excluir .env, .git, node_modules |
| Escaneo | `docker scout cves` |
| Logs a stdout | `console.log()`, no archivos |
| Secretos | Variables de entorno, no en imagen |
| Recursos limitados | `--memory`, `--cpus` |

## CI/CD — Pipeline basico

```
push -> build imagen -> test -> push a registry -> pull en servidor -> deploy
```

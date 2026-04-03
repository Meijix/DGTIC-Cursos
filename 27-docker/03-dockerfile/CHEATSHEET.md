# Cheatsheet — 03 Dockerfile

## Construir una imagen

```bash
docker build -t nombre:tag .             # Build desde el directorio actual
docker build -t app:1.0 -f Dockerfile.prod .  # Usar Dockerfile alternativo
docker build --no-cache -t app:1.0 .     # Sin cache (rebuild completo)
docker build --target build -t app:dev . # Solo un stage especifico
```

## Instrucciones Dockerfile

```dockerfile
FROM node:20-alpine              # Imagen base
WORKDIR /app                     # Directorio de trabajo
COPY package*.json ./            # Copiar archivos
COPY src/ ./src/                 # Copiar directorio
ADD archivo.tar.gz /app/         # Copiar + descomprimir
RUN npm install                  # Ejecutar comando en build
ENV NODE_ENV=production          # Variable de entorno (build + runtime)
ARG VERSION=1.0                  # Variable solo para build
EXPOSE 3000                      # Documentar puerto (no lo abre)
CMD ["node", "server.js"]        # Comando por defecto (sobreescribible)
ENTRYPOINT ["python"]            # Comando fijo
USER node                        # Ejecutar como usuario no-root
VOLUME ["/data"]                 # Punto de montaje
HEALTHCHECK CMD curl -f http://localhost:3000/health || exit 1
```

## CMD vs ENTRYPOINT

| Situacion | CMD | ENTRYPOINT |
|-----------|-----|------------|
| App con comando fijo | `CMD ["node", "app.js"]` | - |
| CLI configurable | - | `ENTRYPOINT ["python"]` + `CMD ["app.py"]` |
| `docker run img bash` | Reemplaza CMD | CMD se pasa como argumento |

## Patron de cache optimo

```dockerfile
FROM node:20-alpine
WORKDIR /app

# 1. Copiar SOLO archivos de dependencias (cambian poco)
COPY package*.json ./

# 2. Instalar dependencias (se cachea si package.json no cambio)
RUN npm ci

# 3. Copiar codigo fuente (cambia frecuentemente)
COPY . .

# 4. Comando
CMD ["node", "server.js"]
```

## Multi-stage build

```dockerfile
# Stage 1: Build
FROM node:20 AS build
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

# Stage 2: Produccion (solo lo necesario)
FROM node:20-alpine
WORKDIR /app
COPY --from=build /app/dist ./dist
COPY --from=build /app/package*.json ./
RUN npm ci --omit=dev
CMD ["node", "dist/index.js"]
```

## .dockerignore

```
node_modules
.git
.env
.env.*
Dockerfile
docker-compose*.yml
*.md
.vscode
coverage
dist
```

## Imagenes base recomendadas

| Base | Tamanio | Uso |
|------|---------|-----|
| `alpine` | ~5 MB | Minimalista |
| `node:20-alpine` | ~130 MB | Node.js ligero |
| `python:3.12-slim` | ~150 MB | Python ligero |
| `nginx:alpine` | ~40 MB | Servidor web |
| `scratch` | 0 MB | Binarios estaticos (Go, Rust) |

## Buenas practicas resumen

1. Usar Alpine/slim como base
2. Copiar dependencias antes que codigo (cache)
3. Combinar RUN con `&&` (menos capas)
4. Usar .dockerignore
5. No ejecutar como root (USER)
6. Multi-stage para produccion
7. Fijar versiones de imagen base

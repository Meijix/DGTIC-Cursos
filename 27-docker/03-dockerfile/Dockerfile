# ============================================================================
# DOCKERFILE — Ejemplo: Aplicacion Node.js (Express)
# ============================================================================
# Este Dockerfile construye una imagen para una aplicacion Node.js tipica.
# Sigue las buenas practicas: cache de dependencias, .dockerignore, Alpine.
#
# Construir:  docker build -t mi-node-app:1.0 .
# Ejecutar:   docker run -d -p 3000:3000 mi-node-app:1.0
# ============================================================================

# ── Stage 1: Build ──────────────────────────────────────────────────────────
# Usamos la imagen completa de Node.js para el build
FROM node:20-alpine AS build

# Crear directorio de trabajo
WORKDIR /app

# Copiar SOLO los archivos de dependencias primero
# Esto aprovecha el cache de Docker: si package.json no cambio,
# npm install no se vuelve a ejecutar
COPY package.json package-lock.json ./

# Instalar TODAS las dependencias (incluidas devDependencies para build)
RUN npm ci

# Copiar el resto del codigo fuente
COPY . .

# Si la app necesita compilacion (TypeScript, por ejemplo):
# RUN npm run build

# ── Stage 2: Produccion ────────────────────────────────────────────────────
# Imagen final ligera, solo con lo necesario para ejecutar
FROM node:20-alpine

# Metadata de la imagen
LABEL maintainer="dgtic-cursos"
LABEL description="Aplicacion Node.js de ejemplo"

# Crear directorio de trabajo
WORKDIR /app

# Copiar package.json para instalar solo dependencias de produccion
COPY package.json package-lock.json ./

# Instalar SOLO dependencias de produccion
RUN npm ci --omit=dev

# Copiar el codigo fuente desde el stage de build
COPY --from=build /app/ ./

# Crear usuario no-root por seguridad
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

# Cambiar al usuario no-root
USER appuser

# Documentar el puerto que usa la aplicacion
EXPOSE 3000

# Variable de entorno por defecto
ENV NODE_ENV=production

# Health check: verificar que la app responde
HEALTHCHECK --interval=30s --timeout=3s --retries=3 \
  CMD wget --no-verbose --tries=1 --spider http://localhost:3000/health || exit 1

# Comando para ejecutar la aplicacion
CMD ["node", "server.js"]

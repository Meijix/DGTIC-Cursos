# Cheatsheet — 04 Docker Compose

## Comandos principales

```bash
docker compose up                    # Levantar servicios (primer plano)
docker compose up -d                 # Levantar en segundo plano
docker compose up --build            # Reconstruir imagenes + levantar
docker compose down                  # Detener + eliminar contenedores y redes
docker compose down -v               # Tambien eliminar volumenes
docker compose ps                    # Estado de los servicios
docker compose logs                  # Logs de todos los servicios
docker compose logs -f web           # Seguir logs de un servicio
docker compose exec web bash         # Shell en un servicio activo
docker compose run web npm test      # Ejecutar comando unico en servicio
docker compose build                 # Solo construir imagenes
docker compose pull                  # Descargar imagenes del registry
docker compose restart               # Reiniciar todos los servicios
docker compose stop                  # Detener sin eliminar
docker compose up -d --scale web=3   # Escalar un servicio
```

## Estructura docker-compose.yml

```yaml
services:
  nombre-servicio:
    image: imagen:tag             # Imagen del registry
    build: ./ruta                 # O construir desde Dockerfile
    ports: ["3000:3000"]          # Mapeo de puertos
    volumes:                      # Volumenes
      - ./local:/contenedor       # Bind mount
      - nombre:/contenedor        # Named volume
    environment:                  # Variables de entorno
      VAR: valor
    env_file: [.env]              # Variables desde archivo
    depends_on: [db]              # Dependencias
    command: npm run dev          # Sobreescribir CMD
    restart: unless-stopped       # Politica de reinicio
    networks: [backend]           # Redes

volumes:
  nombre:                         # Declarar named volumes

networks:
  backend:                        # Declarar redes
```

## Opciones de build

```yaml
services:
  web:
    build: .                      # Simple: Dockerfile en directorio actual
    build:                        # Avanzado:
      context: ./backend          #   Directorio de contexto
      dockerfile: Dockerfile.dev  #   Archivo Dockerfile
      args:                       #   Build args
        NODE_ENV: development
```

## Redes — Comunicacion entre servicios

```
Todos los servicios comparten una red por defecto.
Se resuelven por nombre de servicio:

  web -> conecta a "db:5432"    (nombre del servicio como hostname)
  web -> conecta a "redis:6379"
```

## depends_on con health check

```yaml
services:
  web:
    depends_on:
      db:
        condition: service_healthy
  db:
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 5s
      timeout: 5s
      retries: 5
```

## Variables de entorno

```yaml
# Inline
environment:
  NODE_ENV: production
  DB_HOST: postgres

# Desde archivo
env_file:
  - .env
  - .env.local
```

## Patrones comunes

```yaml
# Reinicio automatico
restart: unless-stopped    # Reinicia excepto si se detuvo manualmente

# Volume anonimo para node_modules
volumes:
  - ./src:/app/src         # Sincronizar codigo
  - /app/node_modules      # Proteger node_modules del contenedor

# Puerto solo en localhost (seguridad)
ports:
  - "127.0.0.1:5432:5432"
```

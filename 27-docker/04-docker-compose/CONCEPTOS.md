# 04 - Docker Compose

## Contenido

1. [Que es Docker Compose?](#1-que-es-docker-compose)
2. [Sintaxis de docker-compose.yml](#2-sintaxis-de-docker-composeyml)
3. [Services — Definir servicios](#3-services)
4. [Volumes — Persistencia](#4-volumes)
5. [Networks — Comunicacion entre servicios](#5-networks)
6. [depends_on y orden de arranque](#6-depends_on-y-orden-de-arranque)
7. [Comandos de Docker Compose](#7-comandos-de-docker-compose)

---

## 1. Que es Docker Compose?

Docker Compose es una herramienta para definir y ejecutar aplicaciones
**multi-contenedor**. En lugar de ejecutar multiples `docker run` manualmente,
defines todos los servicios en un archivo YAML y los levantas con un solo comando.

```
  SIN DOCKER COMPOSE:                CON DOCKER COMPOSE:

  docker network create mi-red       docker compose up
  docker run -d                      (un solo comando levanta todo)
    --name postgres
    --network mi-red
    -v pgdata:/var/lib/...
    -e POSTGRES_PASSWORD=...
    postgres:16
  docker run -d
    --name redis
    --network mi-red
    redis:7
  docker run -d
    --name web
    --network mi-red
    -p 3000:3000
    --build .
    mi-app
```

---

## 2. Sintaxis de docker-compose.yml

```yaml
# Estructura basica de docker-compose.yml

services:               # Definicion de contenedores
  web:                  # Nombre del servicio
    build: .            # Construir desde Dockerfile local
    ports:
      - "3000:3000"
    environment:
      NODE_ENV: development

  db:
    image: postgres:16  # Usar imagen del registry
    volumes:
      - pgdata:/var/lib/postgresql/data
    environment:
      POSTGRES_PASSWORD: secret

volumes:                # Declarar volumenes nombrados
  pgdata:

networks:               # Declarar redes (opcional, hay una por defecto)
  mi-red:
```

---

## 3. Services

Cada servicio se convierte en un contenedor. Las opciones mas comunes:

```yaml
services:
  mi-servicio:
    # Origen de la imagen (elegir uno):
    image: nginx:alpine                 # Desde registry
    build: .                            # Desde Dockerfile local
    build:                              # Build con opciones
      context: ./backend
      dockerfile: Dockerfile.dev

    # Puertos
    ports:
      - "3000:3000"                     # host:contenedor
      - "8080:80"

    # Volumenes
    volumes:
      - ./src:/app/src                  # Bind mount
      - node_modules:/app/node_modules  # Named volume

    # Variables de entorno
    environment:
      NODE_ENV: development
      DB_HOST: postgres
    env_file:
      - .env                            # Desde archivo

    # Dependencias
    depends_on:
      - db
      - redis

    # Comando personalizado (sobreescribe CMD del Dockerfile)
    command: npm run dev

    # Reinicio automatico
    restart: unless-stopped

    # Red personalizada
    networks:
      - backend
```

---

## 4. Volumes

Los volumenes en Compose se declaran a nivel de servicio y a nivel global:

```
  docker-compose.yml

  services:
    db:
      volumes:
        - pgdata:/var/lib/postgresql/data    ← Named volume
        - ./init.sql:/docker-entrypoint...   ← Bind mount

  volumes:
    pgdata:          ← Declaracion del named volume
```

```yaml
services:
  web:
    volumes:
      # Bind mount: sincronizar carpeta local (desarrollo)
      - ./src:/app/src

      # Named volume: datos persistentes
      - uploads:/app/uploads

      # Volume anonimo: evitar sobreescribir node_modules del contenedor
      - /app/node_modules

  db:
    volumes:
      # Persistir datos de PostgreSQL
      - pgdata:/var/lib/postgresql/data

      # Script de inicializacion (se ejecuta al crear la BD)
      - ./init.sql:/docker-entrypoint-initdb.d/init.sql

volumes:
  pgdata:
  uploads:
```

---

## 5. Networks

Docker Compose crea una red por defecto para todos los servicios. Los servicios
se comunican usando el **nombre del servicio** como hostname.

```
  Red por defecto de Compose:

  ┌──────────────────────────────────────────────┐
  │  Red: 27-docker_default                      │
  │                                              │
  │  ┌─────┐     ┌──────────┐     ┌───────┐     │
  │  │ web │────>│ postgres │     │ redis │     │
  │  │:3000│     │:5432     │     │:6379  │     │
  │  └─────┘     └──────────┘     └───────┘     │
  │                                              │
  │  web puede conectarse a postgres usando:     │
  │  postgres://postgres:5432/mi_db              │
  │  (nombre del servicio como hostname)         │
  └──────────────────────────────────────────────┘
```

```yaml
# Redes personalizadas para aislar servicios
services:
  web:
    networks:
      - frontend
      - backend
  db:
    networks:
      - backend         # Solo accesible desde backend
  nginx:
    networks:
      - frontend        # Solo accesible desde frontend

networks:
  frontend:
  backend:
```

---

## 6. depends_on y orden de arranque

`depends_on` controla el **orden de inicio** de los servicios, pero NO espera
a que el servicio este "listo" (solo que el contenedor haya iniciado).

```yaml
services:
  web:
    depends_on:
      - db
      - redis
    # web se inicia DESPUES de db y redis

  db:
    image: postgres:16

  redis:
    image: redis:7
```

```
  Orden de arranque:

  1. db (postgres)     ──┐
  2. redis             ──┤──> se inician primero
                         │
  3. web (mi-app)      ──┘──> se inicia despues

  NOTA: "iniciado" != "listo para conexiones"
  Postgres puede tardar unos segundos en aceptar conexiones.
  La app debe manejar reintentos de conexion.
```

### depends_on con condicion (health check)

```yaml
services:
  web:
    depends_on:
      db:
        condition: service_healthy   # Espera a que pase el healthcheck

  db:
    image: postgres:16
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 5s
      timeout: 5s
      retries: 5
```

---

## 7. Comandos de Docker Compose

```bash
# Levantar todos los servicios
docker compose up

# En segundo plano
docker compose up -d

# Reconstruir imagenes antes de levantar
docker compose up --build

# Detener y eliminar contenedores + redes
docker compose down

# Detener, eliminar contenedores + redes + volumenes
docker compose down -v

# Ver estado de los servicios
docker compose ps

# Ver logs de todos los servicios
docker compose logs

# Logs de un servicio especifico
docker compose logs -f web

# Ejecutar comando en un servicio
docker compose exec web bash

# Escalar un servicio (multiples instancias)
docker compose up -d --scale web=3
```

---

## Resumen

En esta seccion aprendiste:

- Docker Compose orquesta multiples contenedores con un archivo YAML
- Cada servicio define su imagen, puertos, volumenes y variables
- Los servicios se comunican por nombre dentro de la red de Compose
- depends_on controla el orden de arranque
- Un solo comando (`docker compose up`) levanta toda la infraestructura

Revisa el archivo `docker-compose.yml` para ver un ejemplo completo con
Express + PostgreSQL + Redis.

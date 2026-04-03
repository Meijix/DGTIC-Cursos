# 02 - Imagenes y Contenedores en Profundidad

## Contenido

1. [Flags de docker run](#1-flags-de-docker-run)
2. [Mapeo de puertos](#2-mapeo-de-puertos)
3. [Variables de entorno](#3-variables-de-entorno)
4. [docker exec — Ejecutar comandos dentro de un contenedor](#4-docker-exec)
5. [docker logs — Monitorear la salida](#5-docker-logs)
6. [Volumenes — Persistencia de datos](#6-volumenes)
7. [Inspeccion de contenedores](#7-inspeccion-de-contenedores)

---

## 1. Flags de docker run

El comando `docker run` tiene decenas de flags. Estos son los mas importantes:

| Flag | Funcion | Ejemplo |
|------|---------|---------|
| `-d` | Detached (segundo plano) | `docker run -d nginx` |
| `-p` | Mapear puertos host:contenedor | `docker run -p 8080:80 nginx` |
| `-v` | Montar volumen | `docker run -v ./data:/app/data img` |
| `--name` | Nombre personalizado | `docker run --name web nginx` |
| `-e` | Variable de entorno | `docker run -e NODE_ENV=dev img` |
| `--rm` | Eliminar al salir | `docker run --rm nginx` |
| `-it` | Interactivo + terminal | `docker run -it ubuntu bash` |
| `--network` | Red personalizada | `docker run --network mi-red img` |
| `--restart` | Politica de reinicio | `docker run --restart unless-stopped img` |
| `-w` | Working directory | `docker run -w /app img` |

```bash
# Ejemplo combinando varios flags
docker run -d \
  --name mi-api \
  -p 3000:3000 \
  -e NODE_ENV=production \
  -v datos:/app/data \
  --restart unless-stopped \
  node:20-alpine node server.js
```

---

## 2. Mapeo de puertos

Los contenedores estan aislados por defecto. Para acceder a ellos desde el host,
necesitas mapear puertos con `-p`:

```
  HOST                              CONTENEDOR
  ====                              ==========

  localhost:8080  ────────────────>  :80 (nginx)
  localhost:3000  ────────────────>  :3000 (node)
  localhost:5432  ────────────────>  :5432 (postgres)

  -p <puerto_host>:<puerto_contenedor>
```

```bash
# Mapear puerto 80 del contenedor al 8080 del host
docker run -d -p 8080:80 nginx
# Acceder en: http://localhost:8080

# Mapear a todas las interfaces
docker run -d -p 0.0.0.0:8080:80 nginx

# Mapear multiples puertos
docker run -d -p 80:80 -p 443:443 nginx

# Puerto aleatorio del host (Docker elige uno libre)
docker run -d -p 80 nginx
docker ps    # Ver que puerto asigno
```

---

## 3. Variables de entorno

Las variables de entorno configuran el comportamiento de la aplicacion sin
modificar el codigo:

```bash
# Una variable
docker run -e DATABASE_URL=postgres://localhost/db mi-app

# Multiples variables
docker run \
  -e NODE_ENV=production \
  -e PORT=3000 \
  -e DB_HOST=postgres \
  mi-app

# Desde un archivo .env
docker run --env-file .env mi-app
```

### Variables comunes en imagenes oficiales

| Imagen     | Variable                  | Funcion                   |
|------------|---------------------------|---------------------------|
| `postgres` | `POSTGRES_PASSWORD`       | Password del superusuario |
| `postgres` | `POSTGRES_DB`             | Nombre de la base de datos |
| `mysql`    | `MYSQL_ROOT_PASSWORD`     | Password de root          |
| `redis`    | `REDIS_PASSWORD`          | Password de acceso        |

---

## 4. docker exec

`docker exec` permite ejecutar comandos dentro de un contenedor que ya esta corriendo:

```bash
# Abrir un shell bash dentro del contenedor
docker exec -it mi-app bash

# Abrir shell sh (si no tiene bash, como en Alpine)
docker exec -it mi-app sh

# Ejecutar un comando sin shell interactivo
docker exec mi-app ls /app

# Ver procesos dentro del contenedor
docker exec mi-app ps aux

# Acceder a la base de datos dentro del contenedor
docker exec -it mi-postgres psql -U postgres
```

```
  HOST                                CONTENEDOR
  +------------------+                +------------------+
  | Terminal          |  docker exec  |   /bin/bash      |
  |                   | ----------->  |   ls /app        |
  | docker exec -it   |               |   ps aux         |
  | mi-app bash       |               |   cat config.yml |
  +------------------+                +------------------+
```

---

## 5. docker logs

Los logs del contenedor capturan la salida estandar (stdout) y errores (stderr)
del proceso principal:

```bash
# Ver todos los logs
docker logs mi-app

# Seguir logs en tiempo real (como tail -f)
docker logs -f mi-app

# Ultimas 50 lineas
docker logs --tail 50 mi-app

# Logs con timestamps
docker logs -t mi-app

# Logs desde hace 5 minutos
docker logs --since 5m mi-app

# Combinar: ultimas 20 lineas + seguir
docker logs --tail 20 -f mi-app
```

---

## 6. Volumenes

Los contenedores son efimeros: cuando se eliminan, sus datos se pierden.
Los volumenes resuelven esto persistiendo datos fuera del contenedor.

### Tipos de volumenes

```
  1. BIND MOUNT                     2. NAMED VOLUME
  ===============                   ===============

  HOST                              DOCKER
  +----------+                      +----------+
  | ./data/  | <── sincronizado ──> | /app/data|
  +----------+     con el host      +----------+
                                    (Docker gestiona la ubicacion)
  -v ./data:/app/data               -v mi-vol:/app/data

  Uso: desarrollo (hot reload)      Uso: produccion (persistencia)
```

| Tipo | Sintaxis | Gestionado por | Uso tipico |
|------|----------|----------------|------------|
| Bind mount | `-v ./local:/contenedor` | El usuario | Desarrollo, hot reload |
| Named volume | `-v nombre:/contenedor` | Docker | Bases de datos, persistencia |
| Anonymous volume | `-v /contenedor` | Docker | Temporal, sin nombre |
| tmpfs | `--tmpfs /ruta` | Memoria RAM | Datos sensibles temporales |

```bash
# Bind mount: carpeta local sincronizada con el contenedor
docker run -v $(pwd)/html:/usr/share/nginx/html nginx

# Named volume: Docker gestiona donde se guarda
docker run -v pgdata:/var/lib/postgresql/data postgres:16

# Listar volumenes
docker volume ls

# Inspeccionar un volumen (ver donde se guarda)
docker volume inspect pgdata

# Eliminar un volumen
docker volume rm pgdata

# Eliminar volumenes huerfanos (sin contenedor asociado)
docker volume prune
```

---

## 7. Inspeccion de contenedores

```bash
# Detalles completos en JSON
docker inspect mi-app

# Solo la IP del contenedor
docker inspect --format '{{.NetworkSettings.IPAddress}}' mi-app

# Ver los puertos mapeados
docker port mi-app

# Estadisticas en tiempo real (CPU, memoria, red, disco)
docker stats

# Estadisticas de un contenedor especifico
docker stats mi-app

# Ver los procesos dentro del contenedor
docker top mi-app

# Ver cambios en el filesystem del contenedor (vs la imagen)
docker diff mi-app
```

```
  docker stats — Ejemplo de salida:
  ┌────────────┬──────┬───────────────┬──────────┬───────────┐
  │ NOMBRE     │ CPU  │ MEMORIA       │ RED I/O  │ DISCO I/O │
  ├────────────┼──────┼───────────────┼──────────┼───────────┤
  │ web        │ 0.5% │ 45MB / 512MB  │ 1.2kB   │ 0B        │
  │ postgres   │ 1.2% │ 120MB / 512MB │ 3.4kB   │ 8.5MB     │
  │ redis      │ 0.1% │ 8MB / 512MB   │ 500B    │ 0B        │
  └────────────┴──────┴───────────────┴──────────┴───────────┘
```

---

## Resumen

En esta seccion aprendiste:

- Los flags esenciales de `docker run` (-d, -p, -v, -e, --name, --rm)
- Mapeo de puertos para acceder a servicios del contenedor
- Variables de entorno para configurar aplicaciones
- `docker exec` para ejecutar comandos dentro de un contenedor en ejecucion
- `docker logs` para monitorear la salida de un contenedor
- Bind mounts vs named volumes para persistencia de datos
- Herramientas de inspeccion: inspect, stats, top, diff

Ahora pasa al archivo `ejemplos.sh` para practicar estos comandos.

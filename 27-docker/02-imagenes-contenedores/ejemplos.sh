#!/bin/bash
# ============================================================================
# 02 - IMAGENES Y CONTENEDORES EN PROFUNDIDAD
# ============================================================================
# Ejemplos practicos de docker run, exec, logs, puertos y volumenes.
# Ejecuta cada bloque por separado.
# ============================================================================

# ────────────────────────────────────────────────────────────────────────────
# 1. MAPEO DE PUERTOS
# ────────────────────────────────────────────────────────────────────────────

# Ejecutar Nginx y mapear el puerto 80 al 8080 del host
docker run -d --name web-puertos -p 8080:80 nginx:alpine
# Abrir en el navegador: http://localhost:8080

# Ver los puertos mapeados
docker port web-puertos

# Limpieza
docker rm -f web-puertos

# ────────────────────────────────────────────────────────────────────────────
# 2. VARIABLES DE ENTORNO
# ────────────────────────────────────────────────────────────────────────────

# Ejecutar PostgreSQL con variables de entorno
docker run -d \
  --name mi-postgres \
  -p 5432:5432 \
  -e POSTGRES_USER=admin \
  -e POSTGRES_PASSWORD=secreto123 \
  -e POSTGRES_DB=mi_base \
  postgres:16-alpine

# Verificar que la base de datos se creo
docker exec -it mi-postgres psql -U admin -d mi_base -c '\l'

# Limpieza
docker rm -f mi-postgres

# ────────────────────────────────────────────────────────────────────────────
# 3. DOCKER EXEC — Ejecutar comandos dentro del contenedor
# ────────────────────────────────────────────────────────────────────────────

# Crear un contenedor de Nginx
docker run -d --name web-exec nginx:alpine

# Abrir shell interactivo dentro del contenedor
docker exec -it web-exec sh

# Dentro del shell puedes ejecutar:
#   ls /usr/share/nginx/html/
#   cat /etc/nginx/nginx.conf
#   exit

# Ejecutar un comando sin abrir shell
docker exec web-exec cat /etc/nginx/nginx.conf

# Ver procesos dentro del contenedor
docker exec web-exec ps aux

# Limpieza
docker rm -f web-exec

# ────────────────────────────────────────────────────────────────────────────
# 4. DOCKER LOGS — Monitorear la salida
# ────────────────────────────────────────────────────────────────────────────

# Crear un contenedor que genera logs
docker run -d --name web-logs -p 8081:80 nginx:alpine

# Generar trafico para producir logs
curl http://localhost:8081
curl http://localhost:8081/pagina-que-no-existe

# Ver todos los logs
docker logs web-logs

# Ver logs con timestamps
docker logs -t web-logs

# Seguir logs en tiempo real (Ctrl+C para salir)
docker logs -f web-logs

# Ultimas 5 lineas + seguir
docker logs --tail 5 -f web-logs

# Limpieza
docker rm -f web-logs

# ────────────────────────────────────────────────────────────────────────────
# 5. BIND MOUNT — Carpeta local sincronizada
# ────────────────────────────────────────────────────────────────────────────

# Crear una carpeta local con contenido HTML
mkdir -p /tmp/docker-demo/html
echo '<h1>Hola Docker!</h1>' > /tmp/docker-demo/html/index.html

# Montar la carpeta local dentro del contenedor de Nginx
docker run -d \
  --name web-bind \
  -p 8082:80 \
  -v /tmp/docker-demo/html:/usr/share/nginx/html:ro \
  nginx:alpine

# Abrir http://localhost:8082 en el navegador
# Cambiar el archivo local y recargar para ver el cambio:
echo '<h1>Contenido actualizado!</h1>' > /tmp/docker-demo/html/index.html

# Limpieza
docker rm -f web-bind
rm -rf /tmp/docker-demo

# ────────────────────────────────────────────────────────────────────────────
# 6. NAMED VOLUME — Persistencia gestionada por Docker
# ────────────────────────────────────────────────────────────────────────────

# Ejecutar PostgreSQL con un named volume
docker run -d \
  --name pg-persistente \
  -e POSTGRES_PASSWORD=secreto \
  -v pgdata:/var/lib/postgresql/data \
  postgres:16-alpine

# Crear una tabla de prueba
docker exec -it pg-persistente psql -U postgres -c \
  "CREATE TABLE prueba (id SERIAL, nombre TEXT);"
docker exec -it pg-persistente psql -U postgres -c \
  "INSERT INTO prueba (nombre) VALUES ('dato persistente');"

# Eliminar el contenedor (los datos se mantienen en el volumen)
docker rm -f pg-persistente

# Crear un nuevo contenedor con el MISMO volumen
docker run -d \
  --name pg-persistente-2 \
  -e POSTGRES_PASSWORD=secreto \
  -v pgdata:/var/lib/postgresql/data \
  postgres:16-alpine

# Verificar que los datos siguen ahi
sleep 3  # Esperar a que PostgreSQL inicie
docker exec -it pg-persistente-2 psql -U postgres -c \
  "SELECT * FROM prueba;"
# Resultado: dato persistente (los datos sobrevivieron)

# Limpieza
docker rm -f pg-persistente-2
docker volume rm pgdata

# ────────────────────────────────────────────────────────────────────────────
# 7. INSPECCION Y ESTADISTICAS
# ────────────────────────────────────────────────────────────────────────────

# Crear un contenedor para inspeccionar
docker run -d --name web-inspeccion -p 8083:80 nginx:alpine

# Obtener la IP interna del contenedor
docker inspect --format '{{.NetworkSettings.IPAddress}}' web-inspeccion

# Ver los puertos mapeados
docker port web-inspeccion

# Ver estadisticas de CPU y memoria en tiempo real (Ctrl+C para salir)
docker stats web-inspeccion

# Ver procesos dentro del contenedor
docker top web-inspeccion

# Ver cambios en el filesystem respecto a la imagen base
docker diff web-inspeccion

# Limpieza
docker rm -f web-inspeccion

# ────────────────────────────────────────────────────────────────────────────
# 8. LISTAR VOLUMENES Y LIMPIEZA
# ────────────────────────────────────────────────────────────────────────────

# Ver todos los volumenes del sistema
docker volume ls

# Eliminar volumenes que no estan asociados a ningun contenedor
docker volume prune

# Limpieza general del sistema Docker
docker system prune

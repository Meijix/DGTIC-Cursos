# Cheatsheet — 02 Imagenes y Contenedores

## docker run — Flags esenciales

```bash
docker run -d <imagen>                   # Detached (segundo plano)
docker run -p 8080:80 <imagen>           # Mapear puerto host:contenedor
docker run -v ./src:/app/src <imagen>    # Bind mount (carpeta local)
docker run -v datos:/app/data <imagen>   # Named volume (persistente)
docker run --name web <imagen>           # Nombre personalizado
docker run -e VAR=valor <imagen>         # Variable de entorno
docker run --env-file .env <imagen>      # Variables desde archivo
docker run --rm <imagen>                 # Eliminar al salir
docker run -it <imagen> bash             # Interactivo con terminal
docker run --network mi-red <imagen>     # Red personalizada
docker run --restart unless-stopped img  # Auto-reinicio
```

## Mapeo de puertos (-p)

```bash
-p 8080:80                # host:8080 -> contenedor:80
-p 3000:3000              # mismo puerto
-p 80:80 -p 443:443       # multiples puertos
-p 80                     # puerto aleatorio del host
-p 127.0.0.1:8080:80      # solo localhost
```

## Variables de entorno (-e)

```bash
docker run -e NODE_ENV=production -e PORT=3000 mi-app
docker run --env-file .env mi-app
```

## docker exec

```bash
docker exec -it <id> bash               # Shell bash
docker exec -it <id> sh                  # Shell sh (Alpine)
docker exec <id> ls /app                 # Comando sin shell
docker exec -it mi-postgres psql -U postgres  # CLI de postgres
```

## docker logs

```bash
docker logs <id>                         # Todos los logs
docker logs -f <id>                      # Seguir en tiempo real
docker logs --tail 50 <id>               # Ultimas 50 lineas
docker logs -t <id>                      # Con timestamps
docker logs --since 5m <id>              # Desde hace 5 minutos
```

## Volumenes

```bash
# Bind mount (desarrollo)
docker run -v $(pwd)/src:/app/src imagen

# Named volume (produccion)
docker run -v mi-vol:/app/data imagen

# Listar, inspeccionar, eliminar
docker volume ls
docker volume inspect mi-vol
docker volume rm mi-vol
docker volume prune                      # Eliminar huerfanos
```

## Inspeccion

```bash
docker inspect <id>                      # JSON completo
docker inspect --format '{{.NetworkSettings.IPAddress}}' <id>
docker port <id>                         # Puertos mapeados
docker stats                             # CPU/memoria en tiempo real
docker top <id>                          # Procesos del contenedor
docker diff <id>                         # Cambios en filesystem
```

## Combinacion tipica

```bash
docker run -d \
  --name mi-api \
  -p 3000:3000 \
  -e NODE_ENV=production \
  -v datos:/app/data \
  --restart unless-stopped \
  node:20-alpine node server.js
```

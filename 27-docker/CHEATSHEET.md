# Cheatsheet — Modulo 27: Docker

## Comandos esenciales de Docker

```bash
docker run <imagen>                     # Crear y ejecutar contenedor
docker run -d -p 3000:3000 <imagen>     # Detached + mapeo de puertos
docker run --name mi-app -e VAR=val img # Con nombre y variable de entorno
docker run --rm <imagen>                # Eliminar automaticamente al salir
docker run -v ./src:/app/src <imagen>   # Bind mount (carpeta local)
docker run -v datos:/app/data <imagen>  # Named volume (persistente)

docker ps                               # Contenedores activos
docker ps -a                            # Todos (incluidos detenidos)
docker stop <id|nombre>                 # Detener contenedor
docker start <id|nombre>                # Reiniciar contenedor detenido
docker rm <id|nombre>                   # Eliminar contenedor
docker rm -f <id|nombre>                # Forzar eliminacion (si esta activo)

docker exec -it <id> bash               # Shell interactivo en contenedor
docker logs <id>                         # Ver logs del contenedor
docker logs -f <id>                      # Seguir logs en tiempo real
docker inspect <id>                      # Detalles JSON del contenedor

docker images                            # Listar imagenes locales
docker pull <imagen>:<tag>               # Descargar imagen del registry
docker rmi <imagen>                      # Eliminar imagen local
docker build -t nombre:tag .             # Construir imagen desde Dockerfile
docker tag img:v1 user/img:v1            # Etiquetar imagen
docker push user/img:v1                  # Subir imagen al registry
```

## Instrucciones Dockerfile

| Instruccion  | Funcion                                    | Ejemplo                          |
|--------------|--------------------------------------------|----------------------------------|
| `FROM`       | Imagen base                                | `FROM node:20-alpine`            |
| `WORKDIR`    | Directorio de trabajo                      | `WORKDIR /app`                   |
| `COPY`       | Copiar archivos al contenedor              | `COPY package*.json ./`          |
| `ADD`        | Copiar + descomprimir + URLs               | `ADD app.tar.gz /app`            |
| `RUN`        | Ejecutar comando durante build             | `RUN npm install`                |
| `ENV`        | Variable de entorno                        | `ENV NODE_ENV=production`        |
| `ARG`        | Variable solo disponible en build          | `ARG VERSION=1.0`               |
| `EXPOSE`     | Documentar puerto (no lo abre)             | `EXPOSE 3000`                    |
| `CMD`        | Comando por defecto al ejecutar            | `CMD ["node", "server.js"]`      |
| `ENTRYPOINT` | Comando fijo (CMD pasa como argumentos)    | `ENTRYPOINT ["python"]`          |
| `VOLUME`     | Punto de montaje para datos persistentes   | `VOLUME ["/data"]`               |
| `USER`       | Usuario para ejecutar el proceso           | `USER node`                      |

**CMD vs ENTRYPOINT:** CMD se puede sobreescribir al hacer `docker run`. ENTRYPOINT es fijo; CMD se concatena como argumentos.

## Docker Compose

```yaml
# docker-compose.yml basico
services:
  web:
    build: .                      # Construir desde Dockerfile local
    ports: ["3000:3000"]          # Mapeo de puertos
    volumes: ["./src:/app/src"]   # Bind mount
    environment:
      NODE_ENV: development
    depends_on: [db]              # Orden de arranque
  db:
    image: postgres:16            # Imagen del registry
    volumes: [pgdata:/var/lib/postgresql/data]
    environment:
      POSTGRES_PASSWORD: secret

volumes:
  pgdata:                         # Volume nombrado
```

```bash
docker compose up                 # Levantar todos los servicios
docker compose up -d              # En segundo plano
docker compose up --build         # Reconstruir imagenes
docker compose down               # Detener y eliminar contenedores
docker compose down -v            # Tambien eliminar volumenes
docker compose ps                 # Ver estado de servicios
docker compose logs -f web        # Logs de un servicio
docker compose exec web bash      # Shell en servicio activo
docker compose build              # Solo construir imagenes
```

## Tipos de volumenes

| Tipo         | Sintaxis                     | Uso tipico                    |
|--------------|------------------------------|-------------------------------|
| Bind mount   | `./local:/contenedor`        | Desarrollo (hot reload)       |
| Named volume | `nombre:/contenedor`         | Persistir datos (bases datos) |
| Tmpfs mount  | `--tmpfs /tmp`               | Datos temporales en memoria   |

## Redes Docker

```bash
docker network ls                          # Listar redes
docker network create mi-red               # Crear red personalizada
docker run --network mi-red <imagen>       # Conectar contenedor a red
docker network inspect mi-red              # Ver detalles de la red
```

| Driver   | Funcion                                            |
|----------|----------------------------------------------------|
| `bridge` | Red aislada por defecto (comunicacion entre contenedores) |
| `host`   | Comparte la red del host (sin aislamiento)         |
| `none`   | Sin red                                            |

En Docker Compose, todos los servicios comparten una red por defecto y se resuelven por nombre de servicio.

## Limpieza

```bash
docker system prune               # Eliminar contenedores, redes e imagenes sin uso
docker system prune -a --volumes  # Limpieza total (incluye imagenes y volumenes)
docker volume prune               # Solo volumenes huerfanos
docker image prune -a             # Solo imagenes sin contenedor asociado
```

## Errores comunes

| Error | Solucion |
|-------|----------|
| Puerto ya en uso | Cambiar el puerto del host: `-p 3001:3000` |
| Permiso denegado | Agregar usuario al grupo docker o usar `sudo` |
| Imagen no encontrada | Verificar nombre y tag: `docker pull imagen:tag` |
| Cambios no reflejados | Reconstruir: `docker compose up --build` |
| Datos perdidos al recrear | Usar named volumes para persistencia |
| COPY falla en build | Verificar que el archivo existe y no esta en `.dockerignore` |

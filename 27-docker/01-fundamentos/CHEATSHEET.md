# Cheatsheet — 01 Fundamentos de Docker

## Verificar instalacion

```bash
docker --version                    # Version instalada
docker info                         # Info del daemon (contenedores, imagenes, etc.)
docker run hello-world              # Test rapido de que todo funciona
```

## Ciclo de vida de contenedores

```bash
docker create --name app nginx      # Crear sin ejecutar
docker start app                    # Iniciar contenedor creado
docker stop app                     # Detener (SIGTERM, espera 10s)
docker kill app                     # Detener inmediatamente (SIGKILL)
docker restart app                  # Reiniciar
docker rm app                       # Eliminar (debe estar detenido)
docker rm -f app                    # Forzar eliminacion
```

## docker run (create + start)

```bash
docker run nginx                    # Primer plano (bloquea terminal)
docker run -d nginx                 # Segundo plano (detached)
docker run --name mi-web nginx      # Con nombre personalizado
docker run --rm nginx               # Eliminar al salir
docker run -it ubuntu bash          # Interactivo con terminal
```

## Listar y ver informacion

```bash
docker ps                           # Contenedores activos
docker ps -a                        # Todos (activos + detenidos)
docker ps -q                        # Solo IDs (util para scripts)
docker images                       # Imagenes locales
docker inspect <id>                 # Detalles JSON del contenedor
```

## Imagenes

```bash
docker pull nginx:alpine            # Descargar imagen
docker pull node:20                 # Descargar version especifica
docker images                       # Listar imagenes locales
docker rmi nginx:alpine             # Eliminar imagen
docker image prune                  # Eliminar imagenes sin uso
```

## Docker Hub — Tags comunes

| Tag           | Significado                  | Tamanio aprox. |
|---------------|------------------------------|----------------|
| `latest`      | Ultima version (evitar en prod) | Varia       |
| `20`          | Version mayor fijada         | Varia          |
| `20-alpine`   | Basada en Alpine Linux       | Pequenio       |
| `20-slim`     | Debian sin extras            | Mediano        |
| `20-bullseye` | Debian Bullseye completo     | Grande         |

## Estados de un contenedor

```
Created  -->  Running  -->  Stopped  -->  Removed
(create)     (start/run)   (stop/kill)   (rm)
```

## Atajos utiles

```bash
# Detener todos los contenedores activos
docker stop $(docker ps -q)

# Eliminar todos los contenedores detenidos
docker rm $(docker ps -aq)

# Eliminar todas las imagenes
docker rmi $(docker images -q)

# Limpieza total (contenedores + imagenes + redes sin uso)
docker system prune -a
```

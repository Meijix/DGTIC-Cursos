# 01 - Fundamentos de Docker

## Contenido

1. [Que es Docker?](#1-que-es-docker)
2. [Instalacion de Docker](#2-instalacion-de-docker)
3. [Ciclo de vida de un contenedor](#3-ciclo-de-vida-de-un-contenedor)
4. [Imagenes vs Contenedores](#4-imagenes-vs-contenedores)
5. [Docker Hub](#5-docker-hub)
6. [Primeros comandos](#6-primeros-comandos)

---

## 1. Que es Docker?

Docker es una plataforma open-source que automatiza el despliegue de aplicaciones
dentro de **contenedores** de software. Un contenedor empaqueta el codigo, las
dependencias, las librerias y la configuracion necesaria para que la aplicacion
funcione de manera identica en cualquier entorno.

### Analogia: el contenedor de carga

```
  ANTES DE LOS CONTENEDORES           CON CONTENEDORES
  (transporte maritimo)                (transporte maritimo)

  +---+ +--+ +------+ +----+          +--------+ +--------+ +--------+
  |   | |  | |      | |    |          |        | |        | |        |
  | ? | |? | |  ?   | | ?  |          | ESTANDAR| | ESTANDAR| | ESTANDAR|
  +---+ +--+ +------+ +----+          +--------+ +--------+ +--------+
  Cada carga necesita trato            Formato estandar, cualquier
  especial, problemas de               barco puede transportarlos
  compatibilidad

  Lo mismo aplica al software:
  - Sin Docker: "funciona en mi maquina" pero no en el servidor
  - Con Docker: funciona igual en todas partes
```

---

## 2. Instalacion de Docker

### Docker Desktop (recomendado para aprender)

| Sistema operativo | Metodo                               |
|-------------------|--------------------------------------|
| **macOS**         | Descargar Docker Desktop desde docker.com |
| **Windows**       | Docker Desktop con WSL2 habilitado   |
| **Linux**         | Docker Engine via apt/dnf o Docker Desktop |

### Verificar la instalacion

```bash
# Version de Docker
docker --version
# Docker version 27.x.x, build xxxxxxx

# Verificar que el daemon esta corriendo
docker info

# Ejecutar el contenedor de prueba
docker run hello-world
```

### Que pasa cuando ejecutas `docker run hello-world`

```
  1. Docker busca la imagen "hello-world" localmente
     (no la encuentra)
             |
             v
  2. Docker descarga (pull) la imagen desde Docker Hub
             |
             v
  3. Docker crea un contenedor a partir de la imagen
             |
             v
  4. Docker ejecuta el proceso definido en la imagen
     (imprime un mensaje de bienvenida)
             |
             v
  5. El proceso termina y el contenedor se detiene
     (queda en estado "exited")
```

---

## 3. Ciclo de vida de un contenedor

Un contenedor pasa por varios estados durante su existencia:

```
                    docker create
  [NO EXISTE] ────────────────────> [CREATED]
                                       |
                                docker start
                                       |
                                       v
                                   [RUNNING] <──── docker restart
                                    /     \              |
                          docker stop  docker kill       |
                                |         |              |
                                v         v              |
                             [STOPPED] ──────────────────+
                                |
                          docker rm
                                |
                                v
                           [REMOVED]
```

### Comandos del ciclo de vida

```bash
# Crear sin ejecutar
docker create --name mi-app nginx

# Iniciar
docker start mi-app

# Detener (envia SIGTERM, espera 10s, luego SIGKILL)
docker stop mi-app

# Matar inmediatamente (SIGKILL)
docker kill mi-app

# Reiniciar
docker restart mi-app

# Eliminar (debe estar detenido)
docker rm mi-app

# Crear + ejecutar en un solo paso (lo mas comun)
docker run --name mi-app nginx

# Crear + ejecutar + eliminar al salir
docker run --rm nginx
```

---

## 4. Imagenes vs Contenedores

Esta es la distincion mas importante al empezar con Docker:

```
  IMAGEN (plantilla)                 CONTENEDOR (instancia)
  ==================                 ======================

  +------------------+               +------------------+
  | Capa 4: app code | (solo lectura)| Capa escritura   | (lectura/escritura)
  +------------------+               +------------------+
  | Capa 3: npm install|             | Capa 4: app code | (solo lectura)
  +------------------+               +------------------+
  | Capa 2: Node.js  |              | Capa 3: npm install|
  +------------------+               +------------------+
  | Capa 1: Alpine   |              | Capa 2: Node.js  |
  +------------------+               +------------------+
                                     | Capa 1: Alpine   |
  Una imagen puede generar           +------------------+
  MUCHOS contenedores:
                                     Cada contenedor tiene
  imagen ──> contenedor-1            su propia capa de escritura
  imagen ──> contenedor-2
  imagen ──> contenedor-3
```

| Concepto     | Imagen                     | Contenedor                   |
|--------------|----------------------------|------------------------------|
| Analogia     | Clase (blueprint)          | Objeto (instancia)           |
| Mutabilidad  | Solo lectura               | Lectura y escritura          |
| Persistencia | Permanente                 | Efimero (se puede eliminar)  |
| Creacion     | `docker build` o `docker pull` | `docker run`             |
| Almacenamiento | En disco como capas     | En memoria + capa de escritura |

---

## 5. Docker Hub

Docker Hub es el **registro publico** de imagenes Docker. Es como el npm de los
contenedores. Cualquiera puede subir y descargar imagenes.

### Imagenes oficiales populares

| Imagen        | Descripcion               | Ejemplo de uso            |
|---------------|---------------------------|---------------------------|
| `nginx`       | Servidor web              | `docker run -p 80:80 nginx` |
| `node`        | Runtime de Node.js        | `docker run node:20-alpine` |
| `python`      | Runtime de Python         | `docker run python:3.12`  |
| `postgres`    | Base de datos PostgreSQL  | `docker run postgres:16`  |
| `redis`       | Cache y mensaje broker    | `docker run redis:7`      |
| `mysql`       | Base de datos MySQL       | `docker run mysql:8`      |
| `alpine`      | Linux minimalista (5 MB)  | Base para imagenes ligeras |

### Tags (etiquetas)

Las tags permiten especificar la version de la imagen:

```bash
docker pull node           # Tag "latest" (no recomendado para produccion)
docker pull node:20        # Version mayor
docker pull node:20.11     # Version menor
docker pull node:20-alpine # Variante Alpine (mas ligera)
docker pull node:20-slim   # Variante Debian slim
```

---

## 6. Primeros comandos

```bash
# Descargar una imagen
docker pull nginx:alpine

# Ejecutar un contenedor en primer plano
docker run nginx:alpine

# Ejecutar en segundo plano (detached)
docker run -d nginx:alpine

# Ver contenedores activos
docker ps

# Ver todos los contenedores (incluidos los detenidos)
docker ps -a

# Ver imagenes descargadas
docker images

# Eliminar un contenedor detenido
docker rm <id-o-nombre>

# Eliminar una imagen
docker rmi nginx:alpine
```

---

## Resumen

En esta seccion aprendiste:

- Docker empaqueta aplicaciones en contenedores reproducibles
- Los contenedores comparten el kernel del host (a diferencia de las VMs)
- Las imagenes son plantillas de solo lectura; los contenedores son instancias
- Docker Hub es el registro publico para descargar imagenes
- El ciclo de vida: create > start > stop > rm
- `docker run` combina create + start en un solo paso

Ahora pasa al archivo `ejemplos.sh` para ver los comandos en accion.

# Modulo 27: Docker — Contenedores para Desarrollo y Produccion

## Indice de contenidos

1. [Que es Docker?](#1-que-es-docker)
2. [Contenedores vs Maquinas Virtuales](#2-contenedores-vs-maquinas-virtuales)
3. [Arquitectura de Docker](#3-arquitectura-de-docker)
4. [Conceptos fundamentales](#4-conceptos-fundamentales)
5. [Por que importan los contenedores](#5-por-que-importan-los-contenedores)
6. [Ecosistema Docker](#6-ecosistema-docker)
7. [Mapa del modulo](#7-mapa-del-modulo)

---

## 1. Que es Docker?

Docker es una plataforma de **contenedorizacion** que permite empaquetar una
aplicacion junto con todas sus dependencias en una unidad estandarizada llamada
**contenedor**. Esto garantiza que la aplicacion funcione de manera identica en
cualquier entorno: desarrollo, testing o produccion.

```
Docker = Aplicacion + Dependencias + Configuracion = Contenedor reproducible
```

**Problema que resuelve:** "Funciona en mi maquina" deja de ser una excusa. Docker
asegura que el entorno de ejecucion sea identico en todos lados.

---

## 2. Contenedores vs Maquinas Virtuales

```
  MAQUINA VIRTUAL                          CONTENEDOR
  ================                         ==========

  +--------+ +--------+ +--------+         +------+ +------+ +------+
  |  App A | |  App B | |  App C |         |App A | |App B | |App C |
  +--------+ +--------+ +--------+         +------+ +------+ +------+
  |Guest OS| |Guest OS| |Guest OS|         | Bins | | Bins | | Bins |
  +--------+ +--------+ +--------+         +------+ +------+ +------+
  +----------------------------------+     +----------------------------------+
  |          HYPERVISOR              |     |         DOCKER ENGINE            |
  +----------------------------------+     +----------------------------------+
  +----------------------------------+     +----------------------------------+
  |          HOST OS                 |     |          HOST OS                 |
  +----------------------------------+     +----------------------------------+
  |          HARDWARE                |     |          HARDWARE                |
  +----------------------------------+     +----------------------------------+

  - Cada VM tiene su propio SO               - Comparten el kernel del host
  - Arranque en minutos                      - Arranque en segundos
  - Gigabytes de tamanio                     - Megabytes de tamanio
  - Aislamiento completo                     - Aislamiento a nivel de proceso
```

| Caracteristica    | Maquina Virtual      | Contenedor          |
|-------------------|----------------------|---------------------|
| Arranque          | Minutos              | Segundos            |
| Tamanio           | GBs                  | MBs                 |
| SO invitado       | Completo             | Comparte kernel     |
| Rendimiento       | Overhead alto        | Casi nativo         |
| Aislamiento       | Completo (hardware)  | Proceso (namespace) |
| Portabilidad      | Limitada             | Excelente           |
| Densidad          | Pocas por host       | Muchos por host     |

---

## 3. Arquitectura de Docker

Docker usa una arquitectura **cliente-servidor** con tres componentes principales:

```
  +------------------+          REST API           +-------------------+
  |  DOCKER CLIENT   | =========================> |  DOCKER DAEMON    |
  |  (docker CLI)    |                             |  (dockerd)        |
  +------------------+                             +-------------------+
                                                    |       |       |
  Comandos:                                         v       v       v
  docker build                              +-------+ +-----+ +--------+
  docker run                                |Imagenes| |Conte-| |Redes / |
  docker pull                               |        | |nedores| |Volumenes|
  docker push                               +-------+ +-------+ +--------+
                                                    |
                                                    v
                                            +-------------------+
                                            |  DOCKER REGISTRY  |
                                            |  (Docker Hub,     |
                                            |   GitHub GHCR,    |
                                            |   AWS ECR)        |
                                            +-------------------+
```

### Componentes clave

| Componente       | Funcion                                          |
|------------------|--------------------------------------------------|
| **Docker Client** | CLI que envia comandos al daemon                |
| **Docker Daemon** | Servicio que gestiona imagenes, contenedores, redes y volumenes |
| **Docker Registry** | Almacen de imagenes (Docker Hub es el publico por defecto) |
| **Docker Desktop** | Aplicacion GUI para macOS/Windows que incluye el daemon |

---

## 4. Conceptos fundamentales

### Imagen

Una imagen es una **plantilla de solo lectura** con instrucciones para crear un
contenedor. Se construye a partir de un Dockerfile y se compone de capas.

### Contenedor

Un contenedor es una **instancia en ejecucion de una imagen**. Es efimero por
naturaleza: cuando se elimina, sus datos internos se pierden (a menos que uses volumenes).

### Volumen

Un volumen es un mecanismo para **persistir datos** fuera del contenedor.
Sobrevive al ciclo de vida del contenedor.

### Red (Network)

Docker crea redes virtuales para que los contenedores se **comuniquen entre si**
de forma aislada.

```
  IMAGEN ──build──> IMAGEN ──run──> CONTENEDOR
  (Dockerfile)      (capas r/o)     (capa r/w + proceso)
                                         |
                                    +----+----+
                                    |         |
                                 VOLUMEN     RED
                                 (datos)   (comunicacion)
```

---

## 5. Por que importan los contenedores

1. **Consistencia** — Mismo entorno en dev, staging y produccion
2. **Aislamiento** — Cada servicio en su propio contenedor sin conflictos
3. **Portabilidad** — Funciona en cualquier maquina con Docker instalado
4. **Escalabilidad** — Facil de replicar contenedores horizontalmente
5. **Velocidad** — Arranque en segundos, builds incrementales por capas
6. **Microservicios** — Arquitectura natural para descomponer aplicaciones
7. **CI/CD** — Builds reproducibles en cualquier pipeline

---

## 6. Ecosistema Docker

| Herramienta        | Funcion                                      |
|--------------------|----------------------------------------------|
| **Docker Engine**  | Motor de contenedores (daemon + CLI)         |
| **Docker Compose** | Orquestar multiples contenedores con YAML    |
| **Docker Hub**     | Registro publico de imagenes                 |
| **Docker Desktop** | GUI para macOS y Windows                     |
| **Dockerfile**     | Archivo de instrucciones para construir imagenes |
| **Docker Swarm**   | Orquestacion nativa (alternativa ligera a K8s) |
| **Kubernetes**     | Orquestacion avanzada de contenedores        |

---

## 7. Mapa del modulo

```
27-docker/
├── CONCEPTOS.md          <-- Este archivo
├── CHEATSHEET.md         <-- Referencia rapida general
├── index.html            <-- Pagina de navegacion
├── 01-fundamentos/       <-- Que es Docker, instalacion, ciclo de vida
├── 02-imagenes-contenedores/ <-- docker run, exec, logs, volumenes
├── 03-dockerfile/        <-- Sintaxis Dockerfile, multi-stage, cache
├── 04-docker-compose/    <-- Orquestacion multi-contenedor
├── 05-desarrollo/        <-- Flujos de trabajo para desarrollo local
└── 06-produccion/        <-- Mejores practicas para produccion
```

| Seccion | Temas principales |
|---------|-------------------|
| 01-fundamentos | Que es Docker, instalacion, ciclo de vida, Docker Hub |
| 02-imagenes-contenedores | docker run, exec, logs, puertos, variables, volumenes |
| 03-dockerfile | FROM, RUN, COPY, CMD, ENTRYPOINT, multi-stage, cache |
| 04-docker-compose | services, ports, volumes, depends_on, redes, multi-contenedor |
| 05-desarrollo | Hot reload, dev containers, compose dev vs prod |
| 06-produccion | Optimizacion de imagenes, seguridad, registries, CI/CD |

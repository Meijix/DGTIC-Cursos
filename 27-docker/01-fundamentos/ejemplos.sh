#!/bin/bash
# ============================================================================
# 01 - FUNDAMENTOS DE DOCKER
# ============================================================================
# Ejemplos practicos de los primeros comandos de Docker.
# Ejecuta cada bloque por separado, no todo el script de una vez.
# ============================================================================

# ────────────────────────────────────────────────────────────────────────────
# 1. VERIFICAR INSTALACION
# ────────────────────────────────────────────────────────────────────────────

# Version de Docker
docker --version

# Informacion completa del sistema Docker
docker info

# Contenedor de prueba (descarga la imagen si no existe)
docker run hello-world

# ────────────────────────────────────────────────────────────────────────────
# 2. DESCARGAR IMAGENES DESDE DOCKER HUB
# ────────────────────────────────────────────────────────────────────────────

# Descargar la imagen de Nginx (servidor web) en su variante Alpine
docker pull nginx:alpine

# Descargar Node.js version 20
docker pull node:20-alpine

# Ver todas las imagenes descargadas
docker images

# ────────────────────────────────────────────────────────────────────────────
# 3. EJECUTAR CONTENEDORES
# ────────────────────────────────────────────────────────────────────────────

# Ejecutar Nginx en primer plano (Ctrl+C para salir)
docker run nginx:alpine

# Ejecutar Nginx en segundo plano (detached)
# Docker devuelve el ID del contenedor
docker run -d nginx:alpine

# Ejecutar con un nombre personalizado
docker run -d --name mi-web nginx:alpine

# Ejecutar Ubuntu con terminal interactiva
# -i = mantener STDIN abierto
# -t = asignar pseudo-terminal
docker run -it ubuntu:22.04 bash

# Ejecutar y eliminar automaticamente al salir
docker run --rm alpine echo "Hola desde Alpine!"

# ────────────────────────────────────────────────────────────────────────────
# 4. LISTAR CONTENEDORES
# ────────────────────────────────────────────────────────────────────────────

# Ver contenedores en ejecucion
docker ps

# Ver todos los contenedores (incluidos los detenidos)
docker ps -a

# Ver solo los IDs (util para scripts)
docker ps -q

# ────────────────────────────────────────────────────────────────────────────
# 5. CICLO DE VIDA COMPLETO
# ────────────────────────────────────────────────────────────────────────────

# Paso 1: Crear un contenedor sin ejecutarlo
docker create --name ciclo-demo nginx:alpine

# Paso 2: Verificar que esta en estado "created"
docker ps -a --filter name=ciclo-demo

# Paso 3: Iniciar el contenedor
docker start ciclo-demo

# Paso 4: Verificar que esta en estado "running"
docker ps --filter name=ciclo-demo

# Paso 5: Detener el contenedor
docker stop ciclo-demo

# Paso 6: Reiniciar el contenedor
docker restart ciclo-demo

# Paso 7: Detener y eliminar
docker stop ciclo-demo
docker rm ciclo-demo

# Alternativa: forzar eliminacion aunque este activo
# docker rm -f ciclo-demo

# ────────────────────────────────────────────────────────────────────────────
# 6. INSPECCIONAR CONTENEDORES
# ────────────────────────────────────────────────────────────────────────────

# Crear un contenedor para inspeccion
docker run -d --name inspeccion nginx:alpine

# Ver detalles completos en JSON
docker inspect inspeccion

# Ver solo la IP del contenedor
docker inspect --format '{{.NetworkSettings.IPAddress}}' inspeccion

# Limpieza
docker rm -f inspeccion

# ────────────────────────────────────────────────────────────────────────────
# 7. LIMPIEZA
# ────────────────────────────────────────────────────────────────────────────

# Detener todos los contenedores activos
docker stop $(docker ps -q)

# Eliminar todos los contenedores detenidos
docker rm $(docker ps -aq)

# Eliminar imagenes que no estan en uso
docker image prune

# Limpieza total del sistema Docker
# (contenedores detenidos, redes sin uso, imagenes sin contenedor)
docker system prune

# Limpieza total incluyendo imagenes con tag
# docker system prune -a

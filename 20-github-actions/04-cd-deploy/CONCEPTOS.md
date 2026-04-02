# 04 - Despliegue Continuo (CD)

## Contenido

1. [Que es CD?](#1-que-es-cd)
2. [Estrategias de despliegue](#2-estrategias-de-despliegue)
3. [Destinos de despliegue](#3-destinos-de-despliegue)
4. [GitHub Pages](#4-github-pages)
5. [Despliegue a plataformas cloud](#5-despliegue-a-plataformas-cloud)
6. [Docker build y push](#6-docker-build-y-push)
7. [Versionado semantico y releases](#7-versionado-semantico-y-releases)
8. [Entornos y protecciones](#8-entornos-y-protecciones)
9. [Patrones de despliegue](#9-patrones-de-despliegue)
10. [Errores comunes](#10-errores-comunes)

---

## 1. Que es CD?

CD puede referirse a dos conceptos relacionados pero distintos:

### Continuous Delivery (Entrega Continua)

El codigo esta **siempre listo para desplegarse**. Despues de pasar todas las
pruebas, se empaqueta y se prepara para el despliegue. El paso final a produccion
requiere una **aprobacion manual** (un clic).

### Continuous Deployment (Despliegue Continuo)

Cada cambio que pasa las pruebas se despliega **automaticamente** a produccion
sin intervencion humana.

```
  DELIVERY vs DEPLOYMENT:

  Delivery (entrega):
  +-------+    +-------+    +-------+    +--------+    +-----------+
  | Code  |--->| Build |--->| Test  |--->| Stage  |--->| APROBACION|---> Produccion
  +-------+    +-------+    +-------+    +--------+    | manual    |
                                                       +-----------+

  Deployment (despliegue):
  +-------+    +-------+    +-------+    +--------+    +-----------+
  | Code  |--->| Build |--->| Test  |--->| Stage  |--->| Produccion|  (automatico)
  +-------+    +-------+    +-------+    +--------+    +-----------+
```

### Cual elegir?

| Criterio | Delivery | Deployment |
|----------|----------|------------|
| Control | Alto (aprobacion manual) | Bajo (todo automatico) |
| Velocidad | Moderada | Maxima |
| Riesgo | Menor (humano revisa) | Mayor (confia en tests) |
| Ideal para | Apps criticas, finanzas, salud | Apps web, SaaS, startups |
| Requisito | CI + buenos tests | CI + tests excelentes + monitoreo |

---

## 2. Estrategias de despliegue

### Despliegue directo (Big Bang)

La forma mas simple: reemplazar la version anterior por la nueva.

```
  Version 1   --->  Version 2
  (se apaga)        (se enciende)

  Downtime: Si (breve)
  Rollback: Manual (redesplegar v1)
```

### Blue-Green Deployment

Mantener dos entornos identicos. Uno esta activo (Blue), el otro inactivo (Green).
Desplegar en el inactivo y cambiar el trafico.

```
  ANTES:                          DESPUES:
  +--------+                      +--------+
  | Blue   | <--- trafico         | Blue   |
  | (v1)   |                      | (v1)   |
  +--------+                      +--------+
  +--------+                      +--------+
  | Green  |                      | Green  | <--- trafico
  | (vacio)|                      | (v2)   |
  +--------+                      +--------+

  Downtime: No
  Rollback: Instantaneo (cambiar trafico de vuelta a Blue)
```

### Canary Deployment

Desplegar la nueva version a un pequeno porcentaje de usuarios primero.
Si todo va bien, incrementar gradualmente.

```
  Fase 1: 5% trafico a v2
  +--------+  95%
  | v1     | <======
  +--------+
  +--------+  5%
  | v2     | <==
  +--------+

  Fase 2: 50% trafico a v2
  +--------+  50%
  | v1     | <====
  +--------+
  +--------+  50%
  | v2     | <====
  +--------+

  Fase 3: 100% trafico a v2
  +--------+
  | v1     | (apagar)
  +--------+
  +--------+  100%
  | v2     | <========
  +--------+
```

### Rolling Update

Actualizar las instancias una por una. En cada momento, algunas corren v1
y otras v2.

```
  Inicio:     [v1] [v1] [v1] [v1]
  Paso 1:     [v2] [v1] [v1] [v1]
  Paso 2:     [v2] [v2] [v1] [v1]
  Paso 3:     [v2] [v2] [v2] [v1]
  Final:      [v2] [v2] [v2] [v2]
```

### Comparativa de estrategias

| Estrategia | Downtime | Rollback | Complejidad | Costo |
|------------|----------|----------|-------------|-------|
| Directo | Si | Lento | Baja | Bajo |
| Blue-Green | No | Instantaneo | Media | Alto (2x recursos) |
| Canary | No | Rapido | Alta | Medio |
| Rolling | Minimo | Medio | Media | Bajo |

---

## 3. Destinos de despliegue

### Donde puedes desplegar con GitHub Actions

| Destino | Tipo | Costo | Ideal para |
|---------|------|-------|------------|
| **GitHub Pages** | Sitio estatico | Gratis | Docs, portfolios, blogs |
| **Vercel** | Serverless | Free tier | Apps Next.js, React, Vue |
| **Netlify** | Sitio estatico / Serverless | Free tier | JAMstack, SPA |
| **AWS S3 + CloudFront** | Sitio estatico | Pago por uso | Apps en AWS |
| **AWS ECS / EKS** | Contenedores | Pago por uso | Apps en contenedores |
| **Google Cloud Run** | Contenedores | Free tier | APIs, microservicios |
| **Azure App Service** | PaaS | Free tier | Apps .NET, Node, Python |
| **DigitalOcean** | VPS / App Platform | Desde $5/mes | Apps generales |
| **Heroku** | PaaS | Free tier limitado | Prototipos |
| **Docker Hub** | Registro de imagenes | Gratis | Distribuir contenedores |
| **npm / PyPI** | Registro de paquetes | Gratis | Publicar librerias |

---

## 4. GitHub Pages

GitHub Pages es un servicio gratuito de hosting de sitios estaticos integrado
en GitHub. Es perfecto para documentacion, portfolios, blogs y demos.

### Flujo de despliegue a GitHub Pages

```
  1. Generar sitio estatico (build)
       |
       v
  2. Subir artefacto con los archivos HTML/CSS/JS
       |
       v
  3. GitHub Pages despliega los archivos
       |
       v
  4. Sitio disponible en https://usuario.github.io/repo/
```

### Configuracion previa

1. Ve a Settings > Pages
2. Source: selecciona "GitHub Actions"
3. El workflow se encargara del resto

### Tipos de contenido para Pages

| Tipo | Herramienta | Comando de build |
|------|-------------|-----------------|
| HTML/CSS/JS puro | Ninguna | Copiar archivos |
| React | Create React App / Vite | `npm run build` |
| Vue | Vue CLI / Vite | `npm run build` |
| Next.js | Next.js (static export) | `next build && next export` |
| Hugo | Hugo | `hugo` |
| Jekyll | Jekyll (nativo en GitHub) | Automatico |
| MkDocs | MkDocs | `mkdocs build` |
| Sphinx | Sphinx | `make html` |

---

## 5. Despliegue a plataformas cloud

### Vercel

Vercel tiene integracion nativa con GitHub, pero tambien puedes usar
GitHub Actions para mas control:

```yaml
# Patrón general:
# 1. Instalar Vercel CLI
# 2. Ejecutar vercel pull (obtener configuracion)
# 3. Ejecutar vercel build
# 4. Ejecutar vercel deploy --prebuilt
```

### AWS S3

```yaml
# Patron general:
# 1. Configurar credenciales de AWS
# 2. Ejecutar el build
# 3. Sincronizar archivos a S3
# 4. Invalidar cache de CloudFront (opcional)
```

### Netlify

```yaml
# Patron general:
# 1. Ejecutar el build
# 2. Usar netlify-cli o la action de Netlify para desplegar
```

---

## 6. Docker build y push

Docker permite empaquetar tu aplicacion con todas sus dependencias en un
contenedor portable. El flujo tipico es:

```
  1. Build de imagen Docker
       |
       v
  2. Tag de la imagen (ej: v1.2.3, latest)
       |
       v
  3. Push a un registro (Docker Hub, GitHub Container Registry, AWS ECR)
       |
       v
  4. Desplegar el contenedor (Kubernetes, ECS, Cloud Run, etc.)
```

### Registros de contenedores

| Registro | URL | Gratis |
|----------|-----|--------|
| Docker Hub | `docker.io` | Si (1 repo privado) |
| GitHub Container Registry | `ghcr.io` | Si (repos publicos) |
| AWS ECR | `*.dkr.ecr.*.amazonaws.com` | Pago por uso |
| Google Artifact Registry | `*-docker.pkg.dev` | Free tier |
| Azure Container Registry | `*.azurecr.io` | Pago |

### Buenas practicas para Docker en CI

- Usa multi-stage builds para imagenes mas pequenas
- Cachea las capas de Docker para builds mas rapidos
- Etiqueta las imagenes con la version y el SHA del commit
- Escanea las imagenes en busca de vulnerabilidades
- No incluyas secretos en la imagen

---

## 7. Versionado semantico y releases

### Versionado Semantico (SemVer)

```
  MAJOR.MINOR.PATCH
    |     |     |
    |     |     +-- Correccion de bugs (compatible)
    |     +-------- Nueva funcionalidad (compatible)
    +-------------- Cambio incompatible (breaking change)

  Ejemplos:
    1.0.0 -> 1.0.1  (patch: corregir un bug)
    1.0.1 -> 1.1.0  (minor: nueva feature)
    1.1.0 -> 2.0.0  (major: cambio incompatible)
```

### Flujo de releases con GitHub

```
  1. Desarrollar en rama feature/*
       |
       v
  2. Merge a main via PR (con CI)
       |
       v
  3. Crear tag: git tag v1.2.0
       |
       v
  4. Push tag: git push origin v1.2.0
       |
       v
  5. GitHub Actions detecta el tag y activa el workflow de release
       |
       v
  6. Workflow: build + test + crear release en GitHub + deploy
```

### Automatizar releases

Herramientas que crean releases automaticamente basandose en los commits:

| Herramienta | Como funciona |
|-------------|---------------|
| `semantic-release` | Analiza commits (Conventional Commits) y crea releases |
| `release-please` | Crea PRs con changelog y crea releases al hacer merge |
| `changesets` | Maneja versiones en monorepos |

---

## 8. Entornos y protecciones

### Environments en GitHub

Los environments permiten configurar reglas de proteccion para despliegues:

```
  Settings > Environments > New environment

  +-------------------+
  | Environment:      |
  | "production"      |
  +-------------------+
  |                   |
  | Protecciones:     |
  | [x] Requiere     |
  |     aprobacion    |
  |     (reviewer)    |
  |                   |
  | [x] Timer de     |
  |     espera:       |
  |     30 minutos    |
  |                   |
  | [ ] Ramas        |
  |     permitidas:   |
  |     main, release |
  |                   |
  | Secretos:         |
  | PROD_API_KEY=***  |
  | PROD_DB_URL=***   |
  +-------------------+
```

### Reglas de proteccion

| Regla | Que hace |
|-------|----------|
| Required reviewers | Un humano debe aprobar antes de desplegar |
| Wait timer | Esperar N minutos antes de desplegar |
| Deployment branches | Solo ciertas ramas pueden desplegar |
| Environment secrets | Secretos solo disponibles en este environment |
| Environment variables | Variables solo para este environment |

### Ejemplo de uso en un workflow

```yaml
jobs:
  deploy-staging:
    environment: staging        # Usa el environment "staging"
    runs-on: ubuntu-latest

  deploy-production:
    environment:
      name: production          # Usa el environment "production"
      url: https://mi-app.com  # URL que aparece en GitHub
    needs: deploy-staging       # Requiere que staging pase
    runs-on: ubuntu-latest
```

---

## 9. Patrones de despliegue

### Patron: CI/CD completo

```
  push a main --> CI (test + lint) --> Deploy a staging --> Aprobar --> Deploy a produccion
```

### Patron: Tag-based release

```
  push tag v* --> CI (test) --> Build --> Crear release --> Deploy a produccion
```

### Patron: PR preview

```
  Abrir PR --> CI --> Deploy preview --> Reviewer ve la preview --> Merge --> Deploy produccion
```

### Patron: Staging automatico, produccion manual

```yaml
# Este es el patron mas comun y seguro para equipos medianos:
on:
  push:
    branches: [main]     # Deploy automatico a staging
  workflow_dispatch:      # Deploy manual a produccion
```

---

## 10. Errores comunes

### 1. No tener rollback

Siempre ten un plan para volver a la version anterior. Guarda las versiones
desplegadas anteriormente y ten un mecanismo rapido de rollback.

### 2. Deployer sin tests

Nunca hagas CD sin CI. Si no tienes tests automatizados, un deploy automatico
puede llevar bugs directamente a produccion.

### 3. Secretos hardcodeados

Nunca pongas URLs de produccion, tokens o credenciales directamente en el
workflow. Usa secretos y environments.

### 4. No notificar al equipo

Configura notificaciones (Slack, email, etc.) para que el equipo sepa cuando
se despliega algo, especialmente a produccion.

### 5. Deploy los fines de semana

Evita deploys en viernes por la tarde o fines de semana. Si algo falla,
no habra nadie para arreglarlo.

---

## Archivos de ejemplo

| Archivo | Que demuestra |
|---------|---------------|
| `deploy_pages.yml` | Despliegue de sitio estatico a GitHub Pages |
| `deploy_vercel.yml` | Despliegue a Vercel con preview en PRs |
| `docker_build.yml` | Build y push de imagen Docker a GHCR |
| `release_tag.yml` | Release automatico basado en tags |

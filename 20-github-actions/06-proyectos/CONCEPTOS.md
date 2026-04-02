# 06 - Proyectos Integradores

## Contenido

1. [Sobre esta seccion](#1-sobre-esta-seccion)
2. [Proyecto Fullstack (Node.js)](#2-proyecto-fullstack-nodejs)
3. [Proyecto Python Package](#3-proyecto-python-package)
4. [Proyecto Monorepo](#4-proyecto-monorepo)
5. [Automatizacion de Pull Requests](#5-automatizacion-de-pull-requests)
6. [Como adaptar estos proyectos](#6-como-adaptar-estos-proyectos)

---

## 1. Sobre esta seccion

Esta seccion integra todos los conceptos de las secciones 01-05 en workflows
completos y realistas. Cada proyecto demuestra como combinar multiples
funcionalidades de GitHub Actions en un escenario practico.

### Mapa de conceptos por proyecto

```
  PROYECTO                    CONCEPTOS QUE INTEGRA
  ========                    =====================

  proyecto_fullstack.yml      - Triggers (push, PR)           [01]
                              - Jobs con dependencias (needs)  [02]
                              - Matrix strategy (Node.js)      [03]
                              - Artifacts (upload/download)     [02, 04]
                              - Deploy a GitHub Pages           [04]
                              - Concurrencia                    [05]

  proyecto_python_package.yml - Trigger por tags (push tags)   [01, 02]
                              - Matrix (Python versions)        [03]
                              - Build y empaquetado              [04]
                              - Publicacion a PyPI               [04]
                              - OIDC / Trusted Publishing        [05]

  proyecto_monorepo.yml       - Path filters (paths:)           [01]
                              - Jobs condicionales               [02]
                              - CI multi-proyecto                [03]
                              - Concurrencia por proyecto        [05]

  auto_review.yml             - Trigger pull_request             [01]
                              - github-script (API de GitHub)    [05]
                              - Etiquetado automatico            [02]
                              - Notificaciones                   [04]
```

---

## 2. Proyecto Fullstack (Node.js)

**Archivo:** `proyecto_fullstack.yml`

Un pipeline CI/CD completo para una aplicacion web Node.js con 4 jobs
encadenados:

```
  Lint -----> Test (matrix) -----> Build -----> Deploy
                                      |            ^
                                      |            |
                                      +-- artifact-+
                                      (archivos de build)
```

### Que demuestra

- **Job dependencies (`needs`):** cada job espera al anterior
- **Matrix strategy:** ejecutar tests en Node.js 18, 20 y 22
- **Artifacts:** el job de Build sube los archivos compilados; el job de
  Deploy los descarga para desplegarlos
- **Deploy condicional:** solo despliega en push a main (no en PRs)
- **Concurrencia:** un solo deploy a la vez

### Conceptos de secciones anteriores

| Concepto | Seccion de origen |
|----------|-------------------|
| Triggers push/PR | 01-introduccion |
| needs, jobs, steps | 02-workflows-basicos |
| Matrix, testing | 03-ci-testing |
| GitHub Pages, artifacts | 04-cd-deploy |
| Concurrencia, permisos | 05-actions-avanzadas |

---

## 3. Proyecto Python Package

**Archivo:** `proyecto_python_package.yml`

Pipeline para un paquete Python publicado en PyPI:

```
  Tag push (v*) -----> Test (matrix 3.9/3.10/3.11) -----> Build wheel -----> Publish PyPI
                                                                                  |
                                                                          (Trusted Publishing)
```

### Que demuestra

- **Trigger por tags:** el workflow se activa al hacer push de un tag `v*`
- **Matrix multi-version:** tests en Python 3.9, 3.10 y 3.11
- **Build de paquete:** crear wheel y sdist con `build`
- **Trusted Publishing:** publicar en PyPI usando OIDC sin necesidad de
  tokens manuales
- **Test PyPI:** probar la publicacion antes de ir a produccion

### Trusted Publishing (OIDC)

PyPI soporta "Trusted Publishing", que usa OIDC para autenticar workflows
de GitHub Actions sin necesidad de crear tokens API manualmente. Es mas
seguro porque:

1. No hay tokens permanentes que puedan filtrarse
2. Los permisos son especificos al repositorio y workflow
3. La configuracion se hace en PyPI, no en GitHub Secrets

---

## 4. Proyecto Monorepo

**Archivo:** `proyecto_monorepo.yml`

Workflow para un repositorio que contiene multiples proyectos:

```
  Monorepo/
  |-- frontend/     (React)
  |-- backend/      (Python/FastAPI)
  +-- docs/         (MkDocs)

  Push que modifica frontend/ -----> Solo corre job de frontend
  Push que modifica backend/  -----> Solo corre job de backend
  Push que modifica ambos     -----> Corren ambos jobs
```

### Que demuestra

- **Path filters (`paths:`):** solo ejecutar cuando cambian archivos
  relevantes
- **Jobs condicionales:** cada job verifica que directorio cambio
- **Concurrencia por proyecto:** cada sub-proyecto tiene su propio grupo
  de concurrencia
- **Eficiencia:** no desperdiciar minutos de CI en codigo que no cambio

### Estrategias de monorepo

| Estrategia | Ventajas | Desventajas |
|------------|----------|-------------|
| Path filters | Simple, nativo | No detecta dependencias cruzadas |
| Changed files action | Mas flexible | Requiere accion adicional |
| Nx/Turborepo affected | Detecta dependencias | Requiere herramienta externa |

---

## 5. Automatizacion de Pull Requests

**Archivo:** `auto_review.yml`

Workflow que automatiza tareas comunes al trabajar con PRs:

```
  PR abierto/actualizado
       |
       +---> Etiquetar segun archivos cambiados
       +---> Ejecutar checks (lint, test)
       +---> Comentar con resultados
       +---> Notificar en Slack si falla (opcional)
```

### Que demuestra

- **`actions/github-script`:** interactuar con la API de GitHub desde
  un step (crear labels, comentar en PRs)
- **Etiquetado automatico:** asignar labels como `frontend`, `backend`,
  `docs` segun que archivos se modificaron
- **Comentarios automaticos:** postear un resumen de los checks en el PR
- **Notificaciones:** enviar mensaje a Slack si el CI falla

### La API de GitHub en Actions

`actions/github-script` te da acceso a `octokit` (el SDK de GitHub) directamente
en un step. Puedes:

- Crear/editar issues y PRs
- Agregar labels y reviewers
- Postear comentarios
- Crear releases
- Y cualquier cosa que la API de GitHub soporte

---

## 6. Como adaptar estos proyectos

Estos workflows son plantillas educativas con comandos simulados (`echo`).
Para usarlos en un proyecto real:

### Pasos para adaptar

1. **Copia el workflow** a `.github/workflows/` de tu proyecto
2. **Reemplaza los comandos simulados** (`echo "npm test (simulado)"`)
   con los comandos reales de tu proyecto
3. **Ajusta las versiones** (Node.js, Python, etc.) a las que usa tu proyecto
4. **Configura los secretos** necesarios en Settings > Secrets and variables
5. **Activa las protecciones** de rama en Settings > Branches
6. **Prueba con un PR** antes de activar en main

### Orden recomendado de implementacion

```
  1. Empieza con CI basico (lint + test)
  2. Agrega matrix para multi-version
  3. Implementa build y artifacts
  4. Configura deploy a staging
  5. Agrega protecciones y aprobaciones
  6. Implementa deploy a produccion
  7. Agrega automatizaciones (labels, notificaciones)
```

---

## Archivos de ejemplo

| Archivo | Que demuestra |
|---------|---------------|
| `proyecto_fullstack.yml` | CI/CD completo para Node.js con jobs encadenados |
| `proyecto_python_package.yml` | Pipeline de paquete Python con publicacion a PyPI |
| `proyecto_monorepo.yml` | CI con path filters para multiples proyectos |
| `auto_review.yml` | Automatizacion de PRs con labels y comentarios |

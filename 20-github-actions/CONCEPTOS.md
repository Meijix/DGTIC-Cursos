# Modulo 20: GitHub Actions - CI/CD

## Indice de contenidos

1. [Que es CI/CD?](#1-que-es-cicd)
2. [Arquitectura de GitHub Actions](#2-arquitectura-de-github-actions)
3. [Sintaxis YAML para workflows](#3-sintaxis-yaml-para-workflows)
4. [Eventos y triggers](#4-eventos-y-triggers)
5. [Variables, secretos y expresiones](#5-variables-secretos-y-expresiones)
6. [Estrategia de matrices](#6-estrategia-de-matrices)
7. [Integracion Continua (CI)](#7-integracion-continua-ci)
8. [Despliegue Continuo (CD)](#8-despliegue-continuo-cd)
9. [Actions avanzadas y seguridad](#9-actions-avanzadas-y-seguridad)
10. [Mapa del modulo](#10-mapa-del-modulo)

---

## 1. Que es CI/CD?

CI/CD automatiza el ciclo de vida del software: desde que un desarrollador hace push hasta que el codigo llega a produccion.

```
  CI (Integracion Continua)          CD (Despliegue Continuo)
  =========================          ========================
  - Integrar codigo frecuente        - Empaquetar y desplegar
  - Ejecutar pruebas automaticas     - Delivery: con aprobacion manual
  - Detectar bugs temprano           - Deployment: automatico a produccion
```

### El pipeline completo

```
  DESARROLLADOR              REPOSITORIO              PIPELINE                PRODUCCION
  +----------+  git push    +---------+  trigger    +----------+  deploy   +----------+
  |  Escribe |------------->| GitHub  |------------>| 1. Build |---------->| Servidor |
  |  codigo  |              | Repo    |             | 2. Test  |           | o Cloud  |
  +----------+              +---------+             | 3. Lint  |           +----------+
                                                    | 4. Deploy|
                                                    +----------+
```

---

## 2. Arquitectura de GitHub Actions

GitHub Actions se organiza en una jerarquia clara de componentes:

```
WORKFLOW (.github/workflows/ci.yml)
|
|-- on: (EVENTO que lo activa)
|     push, pull_request, schedule, workflow_dispatch
|
+-- jobs:
      |
      +-- job-1 (se ejecuta en un RUNNER)
      |     |-- runs-on: ubuntu-latest
      |     +-- steps:
      |           |-- uses: actions/checkout@v4     <-- ACTION (reutilizable)
      |           |-- run: npm install              <-- Comando shell
      |           +-- run: npm test
      |
      +-- job-2 (puede ser paralelo o depender de job-1)
            +-- needs: [job-1]
```

### Componentes clave

| Componente | Que es | Analogia |
|------------|--------|----------|
| **Workflow** | Archivo YAML con el proceso automatizado | La receta completa |
| **Event** | Lo que dispara el workflow | El timbre para empezar |
| **Job** | Conjunto de steps en un mismo runner | Un plato de la receta |
| **Step** | Tarea individual (`run:` o `uses:`) | Un paso de la preparacion |
| **Action** | Unidad reutilizable del Marketplace | Un electrodomestico |
| **Runner** | Maquina virtual que ejecuta los jobs | La cocina |
| **Secret** | Variable cifrada (tokens, API keys) | La receta secreta |
| **Artifact** | Archivo generado (binarios, reportes) | El plato terminado |

### Flujo de ejecucion de jobs

```
  PARALELO (defecto):             CON DEPENDENCIAS (needs):

  +-----+  +-----+  +-----+     +-------+     +------+     +--------+
  |Job A|  |Job B|  |Job C|     | Build |---->| Test |---->| Deploy |
  +-----+  +-----+  +-----+     +-------+     +------+     +--------+

  EN FORMA DE ARBOL:
       +-------+
       | Build |
       +-------+
        /     \
       v       v
  +------+  +------+
  | Test |  | Lint |     (paralelos)
  +------+  +------+
       \      /
        v    v
      +--------+
      | Deploy |         (espera a ambos)
      +--------+
```

---

## 3. Sintaxis YAML para workflows

Los workflows se definen en archivos YAML dentro de `.github/workflows/`. Las reglas fundamentales de YAML son:

- Indentacion con **espacios** (nunca tabs), 2 espacios por nivel
- Pares clave-valor: `nombre: "valor"`
- Listas con guion: `- elemento`
- Cadenas multilinea con `|` (preserva saltos) o `>` (une en una linea)

```yaml
name: CI Pipeline              # Nombre del workflow
on: [push, pull_request]       # Eventos que lo activan
jobs:
  test:
    runs-on: ubuntu-latest     # Runner
    steps:
      - uses: actions/checkout@v4
      - run: npm ci
      - run: npm test
```

---

## 4. Eventos y triggers

Los eventos determinan **cuando** se ejecuta un workflow.

| Evento | Se activa cuando... | Ejemplo de uso |
|--------|---------------------|----------------|
| `push` | Se hace push a una rama | CI en cada commit |
| `pull_request` | Se abre/actualiza un PR | Validar antes de merge |
| `schedule` | Cron programado | Tests nocturnos |
| `workflow_dispatch` | Clic manual en GitHub | Deploy a produccion |
| `release` | Se publica un release | Publicar paquete |
| `workflow_call` | Otro workflow lo invoca | Workflows reutilizables |

### Filtros de ramas y rutas

```yaml
on:
  push:
    branches: [main, 'feature/**']    # Solo estas ramas
    paths: ['src/**', 'package.json']  # Solo si cambian estos archivos
    paths-ignore: ['*.md', 'docs/**']  # Ignorar cambios cosmeticos
```

---

## 5. Variables, secretos y expresiones

### Tres niveles de variables de entorno

```
env:
  GLOBAL: "todo el workflow"          ← Nivel 1: Workflow
jobs:
  mi-job:
    env:
      JOB_VAR: "todo el job"          ← Nivel 2: Job
    steps:
      - env:
          STEP_VAR: "solo este step"   ← Nivel 3: Step
```

### Secretos y expresiones

```yaml
steps:
  - env:
      TOKEN: ${{ secrets.MI_SECRETO }}    # Secreto cifrado
    if: github.ref == 'refs/heads/main'   # Condicional
    run: echo "Rama: ${{ github.ref }}"   # Contexto de GitHub
```

Los secretos se enmascaran automaticamente en los logs (`***`).

---

## 6. Estrategia de matrices

Las matrices ejecutan un job con multiples combinaciones de variables:

```yaml
strategy:
  matrix:
    os: [ubuntu-latest, windows-latest]
    node: [18, 20, 22]
    # Genera 2 x 3 = 6 jobs en paralelo
```

```
  +------------------+--------+
  | OS               | Node   |
  +------------------+--------+
  | ubuntu-latest    |   18   |
  | ubuntu-latest    |   20   |
  | ubuntu-latest    |   22   |
  | windows-latest   |   18   |
  | windows-latest   |   20   |
  | windows-latest   |   22   |
  +------------------+--------+
```

Se pueden excluir combinaciones con `exclude:`, agregar extras con `include:`, y controlar fallos con `fail-fast: false`.

---

## 7. Integracion Continua (CI)

La CI verifica automaticamente cada cambio de codigo. Un pipeline tipico incluye:

```
  push/PR ──> Build ──> Lint ──> Tests ──> Cobertura
                                    |
                              +-----+-----+
                              |           |
                           EXITO       FALLO
                              |           |
                         Puede merge  Bloquear merge
```

### Piramide de testing

```
                   /\
                  / E2E \         Pocas, lentas, costosas
                 /--------\
                /Integracion\     Algunas, moderadas
               /--------------\
              / Tests Unitarios \  Muchas, rapidas, baratas
             /--------------------\
```

### Herramientas por lenguaje

| Lenguaje | Tests | Linter | Cobertura |
|----------|-------|--------|-----------|
| Python | pytest | flake8, ruff | coverage.py |
| Node.js | Jest, Vitest | ESLint | Istanbul |
| PHP | PHPUnit | PHPStan | Xdebug |

---

## 8. Despliegue Continuo (CD)

### Estrategias de despliegue

```
  Blue-Green:                    Canary:
  +------+ trafico               +------+ 95%
  | v1   | <====                 | v1   | <====
  +------+                       +------+
  +------+                       +------+ 5%
  | v2   | (espera)              | v2   | <==      (incrementar gradualmente)
  +------+                       +------+
```

| Estrategia | Downtime | Rollback | Complejidad |
|------------|----------|----------|-------------|
| Directo | Si | Lento | Baja |
| Blue-Green | No | Instantaneo | Media |
| Canary | No | Rapido | Alta |
| Rolling | Minimo | Medio | Media |

### Deploy a GitHub Pages

```
  push a main ──> Build sitio ──> Upload artifact ──> GitHub Pages
                  (npm run build)                     (https://user.github.io/repo/)
```

Se configura en Settings > Pages > Source: "GitHub Actions".

---

## 9. Actions avanzadas y seguridad

### Acciones personalizadas

| Tipo | Lenguaje | Velocidad | Uso |
|------|----------|-----------|-----|
| Composite | YAML | Rapida | Agrupar steps comunes |
| JavaScript | JS/TS | Rapida | Logica compleja con API |
| Docker | Cualquiera | Lenta | Entorno especifico |

### Workflows reutilizables

```
  Workflow A ──> uses: ./.github/workflows/deploy.yml   (workflow_call)
  Workflow B ──> uses: ./.github/workflows/deploy.yml   (misma logica)
```

### Seguridad

- **Fijar versiones** de actions con SHA: `uses: actions/checkout@b4ffde65...`
- **Minimo privilegio**: `permissions: { contents: read }`
- **OIDC** para credenciales temporales con AWS/Azure/GCP (sin tokens permanentes)
- **Concurrencia**: evitar deploys simultaneos con `concurrency: { group: deploy }`

---

## 10. Mapa del modulo

| Seccion | Temas principales |
|---------|-------------------|
| 01-introduccion | CI/CD, terminologia, YAML, arquitectura de GitHub Actions |
| 02-workflows-basicos | Eventos, jobs, steps, matrices, cache, artefactos, secretos |
| 03-ci-testing | Pipelines CI para Python/Node/PHP, linting, cobertura, badges |
| 04-cd-deploy | Estrategias de deploy, GitHub Pages, Docker, releases, environments |
| 05-actions-avanzadas | Acciones personalizadas, workflows reutilizables, OIDC, seguridad |
| 06-proyectos | Proyecto fullstack, paquete Python, monorepo, automatizacion de PRs |

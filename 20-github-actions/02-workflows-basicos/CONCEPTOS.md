# 02 - Workflows Basicos

## Contenido

1. [Eventos en profundidad](#1-eventos-en-profundidad)
2. [Jobs y Steps](#2-jobs-y-steps)
3. [Variables de entorno y secretos](#3-variables-de-entorno-y-secretos)
4. [Expresiones y contextos](#4-expresiones-y-contextos)
5. [Ejecucion condicional](#5-ejecucion-condicional)
6. [Estrategia de matrices](#6-estrategia-de-matrices)
7. [Cache de dependencias](#7-cache-de-dependencias)
8. [Artefactos](#8-artefactos)
9. [Buenas practicas](#9-buenas-practicas)

---

## 1. Eventos en profundidad

Los eventos son el mecanismo que activa (dispara) los workflows. GitHub Actions
soporta mas de 35 tipos de eventos diferentes.

### Eventos mas comunes

```
  ACTIVIDAD DEL DESARROLLADOR                  EVENTO EN GITHUB ACTIONS
  ============================                  ========================

  git push                          ------>     push
  Crear/actualizar un PR            ------>     pull_request
  Crear un release/tag              ------>     release / push (tags)
  Abrir un issue                    ------>     issues
  Comentar en un issue              ------>     issue_comment
  Hacer merge a main                ------>     push (a main)
  Clic en boton "Run workflow"      ------>     workflow_dispatch
  Cron/horario programado           ------>     schedule
  Otro workflow termina             ------>     workflow_run
  Llamada API externa               ------>     repository_dispatch
```

### Evento: push

Se activa cuando se hace push de commits a una rama o tag.

```yaml
on:
  push:
    # Filtrar por ramas
    branches:
      - main
      - 'feature/**'       # Glob: feature/login, feature/api, etc.
      - '!feature/experimental'  # Excluir esta rama especifica

    # Filtrar por rutas de archivos modificados
    paths:
      - 'src/**'
      - 'package.json'

    # Filtrar por tags
    tags:
      - 'v*'               # v1.0, v2.3.1, etc.
      - '!v*-beta'         # Excluir tags beta
```

**Nota sobre filtros:** Cuando usas `branches` y `paths` juntos, AMBOS deben
cumplirse (operacion AND). El push debe ser a una rama listada Y modificar
archivos en las rutas listadas.

### Evento: pull_request

Se activa con actividad en Pull Requests. Por defecto reacciona a `opened`,
`synchronize` y `reopened`.

```yaml
on:
  pull_request:
    branches:
      - main                # Solo PRs dirigidos a main
    types:
      - opened              # Se abrio el PR
      - synchronize         # Se agregaron commits
      - reopened            # Se reabrio
      - closed              # Se cerro (merged o no)
      - labeled             # Se agrego una etiqueta
      - review_requested    # Se pidio revision
```

**Diferencia clave con push:** En un evento `pull_request`, el workflow se
ejecuta en el contexto de la rama del PR (merge simulado), no en la rama destino.
Esto permite probar el codigo antes de hacer merge.

### Evento: schedule

Ejecuta el workflow en un horario programado usando expresiones cron.

```yaml
on:
  schedule:
    - cron: '30 5 * * 1-5'   # Lunes a viernes a las 5:30 UTC
```

**Formato cron:**

```
  *    *    *    *    *
  |    |    |    |    |
  |    |    |    |    +-- Dia de la semana (0-6, 0=domingo)
  |    |    |    +------- Mes (1-12)
  |    |    +------------ Dia del mes (1-31)
  |    +----------------- Hora (0-23) en UTC
  +---------------------- Minuto (0-59)
```

**Ejemplos practicos:**

| Expresion | Significado |
|-----------|-------------|
| `0 0 * * *` | Todos los dias a medianoche UTC |
| `0 6 * * 1` | Cada lunes a las 6:00 UTC |
| `*/15 * * * *` | Cada 15 minutos |
| `0 12 1 * *` | Primer dia de cada mes a las 12:00 UTC |
| `0 8 * * 1-5` | Lunes a viernes a las 8:00 UTC |

**Advertencias del schedule:**
- Solo funciona en la rama por defecto (main/master)
- No es preciso al minuto (puede haber retrasos de varios minutos)
- El minimo intervalo recomendado es cada 5 minutos
- Si el repositorio no tiene actividad en 60 dias, los schedules se desactivan

### Evento: workflow_dispatch

Permite ejecutar el workflow manualmente desde la interfaz de GitHub o la API.

```yaml
on:
  workflow_dispatch:
    inputs:
      entorno:
        description: 'Entorno de despliegue'
        required: true
        type: choice
        options: [staging, production]
      version:
        description: 'Version a desplegar'
        required: false
        type: string
        default: 'latest'
      dry-run:
        description: 'Simular sin ejecutar'
        type: boolean
        default: false
```

Los inputs se acceden con `${{ github.event.inputs.entorno }}` o
`${{ inputs.entorno }}`.

### Evento: release

Se activa cuando se crea, edita o publica un release en GitHub.

```yaml
on:
  release:
    types:
      - published     # Cuando se publica un release
      - created       # Cuando se crea
      - prereleased   # Cuando se crea un pre-release
```

---

## 2. Jobs y Steps

### Jobs

Los jobs son las unidades de ejecucion principales. Cada job:

- Se ejecuta en un runner independiente (maquina virtual aislada)
- Por defecto, se ejecutan en **paralelo** (todos al mismo tiempo)
- No comparten sistema de archivos (cada uno empieza limpio)
- Pueden depender de otros jobs usando `needs`

```
  SIN DEPENDENCIAS (paralelo):          CON DEPENDENCIAS (secuencial):

  +--------+  +--------+  +--------+   +-------+   +-------+   +--------+
  | Job A  |  | Job B  |  | Job C  |   | Job A |-->| Job B |-->| Job C  |
  +--------+  +--------+  +--------+   +-------+   +-------+   +--------+
  (todos empiezan al mismo tiempo)      (B espera a A, C espera a B)


  DEPENDENCIAS EN FORMA DE ARBOL:

       +-------+
       | Build |
       +-------+
        /     \
       v       v
  +------+  +------+
  | Test |  | Lint |    (Test y Lint son paralelos)
  +------+  +------+
       \      /
        v    v
      +--------+
      | Deploy |           (Deploy espera a Test Y Lint)
      +--------+
```

### Propiedades de un Job

```yaml
jobs:
  mi-job:
    name: "Nombre legible"           # Aparece en la UI de GitHub
    runs-on: ubuntu-latest           # Runner
    needs: [otro-job]                # Dependencias
    if: github.ref == 'refs/heads/main'  # Condicion
    timeout-minutes: 30              # Timeout (defecto: 360 min)
    continue-on-error: false         # Si falla, marca el workflow como fallido
    environment: production          # Environment de GitHub
    env:                             # Variables de entorno del job
      MI_VAR: "valor"
    outputs:                         # Outputs para otros jobs
      resultado: ${{ steps.paso1.outputs.valor }}
    services:                        # Contenedores de servicio (ej: base de datos)
      postgres:
        image: postgres:15
        ports: ['5432:5432']
    container:                       # Ejecutar el job dentro de un contenedor
      image: node:20
    steps:                           # Lista de pasos
      - run: echo "hola"
```

### Steps

Los steps son las tareas individuales dentro de un job. Se ejecutan en
**secuencia** (nunca en paralelo).

Hay dos tipos de steps:

#### Step con `run` (comando shell)

```yaml
steps:
  # Comando simple
  - name: Saludo
    run: echo "Hola"

  # Multiples comandos (con pipe |)
  - name: Multiples comandos
    run: |
      echo "Linea 1"
      echo "Linea 2"
      ls -la

  # Especificar shell
  - name: Comando en Python
    shell: python
    run: |
      import os
      print(f"Home: {os.environ['HOME']}")

  # Directorio de trabajo
  - name: En un subdirectorio
    working-directory: ./src
    run: ls -la
```

#### Step con `uses` (action reutilizable)

```yaml
steps:
  # Action del Marketplace
  - name: Checkout
    uses: actions/checkout@v4

  # Action con parametros
  - name: Instalar Node.js
    uses: actions/setup-node@v4
    with:
      node-version: '20'
      cache: 'npm'

  # Action de otro repositorio
  - name: Action de tercero
    uses: usuario/repositorio@v1
    with:
      parametro: 'valor'

  # Action local (del mismo repositorio)
  - name: Action local
    uses: ./.github/actions/mi-action
```

---

## 3. Variables de entorno y secretos

### Variables de entorno

Las variables de entorno se pueden definir en tres niveles:

```yaml
# NIVEL 1: Todo el workflow
env:
  GLOBAL_VAR: "disponible en todos los jobs y steps"

jobs:
  mi-job:
    # NIVEL 2: Todo el job
    env:
      JOB_VAR: "disponible en todos los steps de este job"
    steps:
      # NIVEL 3: Un solo step
      - name: Mi paso
        env:
          STEP_VAR: "solo disponible en este step"
        run: |
          echo $GLOBAL_VAR
          echo $JOB_VAR
          echo $STEP_VAR
```

**Precedencia:** Step > Job > Workflow (el nivel mas especifico gana).

### Variables predefinidas por GitHub

GitHub proporciona automaticamente muchas variables. Las mas utiles:

| Variable | Descripcion | Ejemplo |
|----------|-------------|---------|
| `GITHUB_REPOSITORY` | Owner/nombre del repo | `usuario/mi-repo` |
| `GITHUB_REF` | Ref completa del evento | `refs/heads/main` |
| `GITHUB_SHA` | SHA del commit | `abc123def456...` |
| `GITHUB_ACTOR` | Usuario que activo el evento | `mejbau` |
| `GITHUB_WORKSPACE` | Directorio de trabajo | `/home/runner/work/repo/repo` |
| `GITHUB_RUN_ID` | ID unico de la ejecucion | `1234567890` |
| `GITHUB_RUN_NUMBER` | Numero incremental | `42` |
| `RUNNER_OS` | SO del runner | `Linux` |

### Secretos

Los secretos son variables cifradas almacenadas en GitHub. Se usan para API keys,
tokens, contrasenas, etc.

**Como crear un secreto:**
1. Ve a Settings > Secrets and variables > Actions
2. Clic en "New repository secret"
3. Nombre: `MI_SECRETO` (mayusculas y guiones bajos por convencion)
4. Valor: el valor secreto

```yaml
steps:
  - name: Usar secreto
    env:
      # Asi se accede a un secreto en un workflow
      TOKEN: ${{ secrets.MI_SECRETO }}
    run: |
      # El valor se enmascara automaticamente en los logs
      # Si intentas imprimirlo, aparece como ***
      echo "Token: $TOKEN"    # Muestra: Token: ***
```

**Reglas de los secretos:**
- Nunca aparecen en los logs (se enmascaran con `***`)
- No se pueden leer despues de crearlos (solo reemplazar)
- No estan disponibles en workflows de forks (por seguridad)
- No se pasan automaticamente a acciones de terceros

### GITHUB_TOKEN

GitHub genera automaticamente un token temporal (`GITHUB_TOKEN`) para cada
ejecucion del workflow. Este token permite interactuar con la API de GitHub.

```yaml
steps:
  - name: Usar GITHUB_TOKEN
    env:
      # Forma 1: a traves de secrets
      GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
    run: |
      # Crear un comentario en un issue
      gh issue comment 1 --body "Comentario automatico"

  - name: Forma alternativa
    env:
      # Forma 2: a traves del contexto github
      GH_TOKEN: ${{ github.token }}
    run: |
      gh pr list
```

---

## 4. Expresiones y contextos

Las expresiones de GitHub Actions se escriben con `${{ ... }}` y permiten
acceder a informacion del contexto, evaluar condiciones y manipular datos.

### Contextos disponibles

| Contexto | Que contiene | Ejemplo |
|----------|-------------|---------|
| `github` | Info del evento y repositorio | `${{ github.actor }}` |
| `env` | Variables de entorno | `${{ env.MI_VAR }}` |
| `secrets` | Secretos del repositorio | `${{ secrets.API_KEY }}` |
| `job` | Info del job actual | `${{ job.status }}` |
| `steps` | Outputs de steps anteriores | `${{ steps.mi-step.outputs.valor }}` |
| `runner` | Info del runner | `${{ runner.os }}` |
| `needs` | Outputs de jobs dependientes | `${{ needs.build.outputs.version }}` |
| `matrix` | Variables de la matrix actual | `${{ matrix.node-version }}` |
| `inputs` | Inputs de workflow_dispatch | `${{ inputs.entorno }}` |
| `vars` | Variables del repositorio | `${{ vars.MI_VARIABLE }}` |

### Funciones disponibles

```yaml
# Funciones de estado
if: success()              # El paso anterior fue exitoso
if: failure()              # El paso anterior fallo
if: always()               # Siempre se ejecuta
if: cancelled()            # El workflow fue cancelado

# Funciones de string
${{ contains('Hola Mundo', 'Mundo') }}           # true
${{ startsWith('Hola', 'Ho') }}                  # true
${{ endsWith('archivo.yml', '.yml') }}           # true
${{ format('Hola {0}, tienes {1}', 'Ana', 25) }} # "Hola Ana, tienes 25"

# Funciones de conversion
${{ toJSON(github.event) }}     # Convierte a JSON
${{ fromJSON(steps.data.outputs.json) }}  # Parsea JSON

# Operadores
${{ github.ref == 'refs/heads/main' }}        # Igualdad
${{ github.event_name != 'pull_request' }}    # Desigualdad
${{ github.run_number > 10 }}                 # Mayor que
${{ true && false }}                          # AND logico
${{ true || false }}                          # OR logico
${{ !true }}                                  # NOT logico
```

---

## 5. Ejecucion condicional

### Condicionales en Jobs

```yaml
jobs:
  deploy:
    # Solo ejecutar en la rama main
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    steps:
      - run: echo "Desplegando..."

  notify:
    # Solo ejecutar cuando falla el job anterior
    needs: deploy
    if: failure()
    runs-on: ubuntu-latest
    steps:
      - run: echo "El deploy fallo!"
```

### Condicionales en Steps

```yaml
steps:
  - name: Solo en push
    if: github.event_name == 'push'
    run: echo "Esto fue un push"

  - name: Solo en PR a main
    if: github.event_name == 'pull_request' && github.base_ref == 'main'
    run: echo "PR hacia main"

  - name: Solo en tags
    if: startsWith(github.ref, 'refs/tags/')
    run: echo "Esto es un tag"

  - name: Limpiar (siempre, aunque falle algo)
    if: always()
    run: echo "Limpieza..."

  - name: Solo si fallo el paso anterior
    if: failure()
    run: echo "Algo fallo, notificando..."
```

### Patrones comunes de condicionales

```yaml
# Solo en la rama main
if: github.ref == 'refs/heads/main'

# Solo en ramas que no sean main
if: github.ref != 'refs/heads/main'

# Solo si es un tag de version
if: startsWith(github.ref, 'refs/tags/v')

# Solo si NO es un fork
if: github.event.pull_request.head.repo.full_name == github.repository

# Solo si el commit message contiene "[deploy]"
if: contains(github.event.head_commit.message, '[deploy]')

# Solo los lunes (en schedules)
if: github.event.schedule == '0 6 * * 1'

# Solo si un input manual tiene cierto valor
if: github.event.inputs.entorno == 'production'
```

---

## 6. Estrategia de matrices

Las matrices permiten ejecutar un job multiples veces con diferentes
combinaciones de variables. Es ideal para probar en multiples versiones,
sistemas operativos, etc.

### Ejemplo basico

```yaml
jobs:
  test:
    strategy:
      matrix:
        version: [18, 20, 22]
    runs-on: ubuntu-latest
    steps:
      - name: Usar version ${{ matrix.version }}
        run: echo "Probando con version ${{ matrix.version }}"
```

Esto genera **3 jobs** que se ejecutan en paralelo.

### Matrix multi-dimensional

```yaml
strategy:
  matrix:
    os: [ubuntu-latest, windows-latest, macos-latest]
    node: [18, 20]
    # Genera 3 x 2 = 6 combinaciones
```

```
  Combinaciones generadas:
  +------------------+------+
  | OS               | Node |
  +------------------+------+
  | ubuntu-latest    |   18 |
  | ubuntu-latest    |   20 |
  | windows-latest   |   18 |
  | windows-latest   |   20 |
  | macos-latest     |   18 |
  | macos-latest     |   20 |
  +------------------+------+
```

### Excluir e incluir combinaciones

```yaml
strategy:
  matrix:
    os: [ubuntu-latest, windows-latest]
    node: [18, 20, 22]

    # Eliminar combinaciones que no necesitas
    exclude:
      - os: windows-latest
        node: 18

    # Agregar combinaciones extra con variables adicionales
    include:
      - os: ubuntu-latest
        node: 22
        experimental: true    # Variable extra solo para esta combinacion
```

### fail-fast

```yaml
strategy:
  # false = si un job de la matrix falla, los demas siguen ejecutandose
  # true (defecto) = si uno falla, se cancelan todos los demas
  fail-fast: false
  matrix:
    node: [18, 20, 22]
```

### max-parallel

```yaml
strategy:
  max-parallel: 2    # Maximo 2 jobs de la matrix al mismo tiempo
  matrix:
    node: [18, 20, 22]
  # Sin max-parallel, los 3 correran a la vez.
  # Con max-parallel: 2, primero corren 2, y al terminar uno empieza el 3ro.
```

---

## 7. Cache de dependencias

Instalar dependencias (npm install, pip install, composer install) puede tomar
minutos. El cache permite reusar las dependencias descargadas entre ejecuciones.

### Diagrama del cache

```
  PRIMERA EJECUCION:                    EJECUCIONES SIGUIENTES:

  +----------+    No hay cache          +----------+    Cache encontrado!
  |  Runner  |                          |  Runner  |
  +----------+                          +----------+
       |                                     |
       v                                     v
  +-----------+                         +----------+
  | npm install|  (descarga todo)       | Restaurar|  (restaura del cache)
  | 2 minutos  |                        |  cache   |  (5 segundos)
  +-----------+                         +----------+
       |                                     |
       v                                     v
  +----------+                          +----------+
  |  Guardar |                          | npm install| (casi nada que instalar)
  |  cache   |                          | 10 segundos|
  +----------+                          +----------+
```

### Usando actions/cache

```yaml
steps:
  - name: Cache de dependencias npm
    uses: actions/cache@v4
    with:
      # Ruta de los archivos a cachear
      path: ~/.npm
      # Clave del cache - si cambia package-lock.json, se regenera
      key: ${{ runner.os }}-npm-${{ hashFiles('**/package-lock.json') }}
      # Claves alternativas si no se encuentra la clave exacta
      restore-keys: |
        ${{ runner.os }}-npm-

  - name: Instalar dependencias
    run: npm ci
```

### Cache integrado en setup actions

Muchas acciones de setup tienen cache integrado, lo cual es mas simple:

```yaml
# Node.js con cache integrado
- uses: actions/setup-node@v4
  with:
    node-version: '20'
    cache: 'npm'       # Cachea automaticamente node_modules

# Python con cache integrado
- uses: actions/setup-python@v5
  with:
    python-version: '3.12'
    cache: 'pip'       # Cachea automaticamente los paquetes pip

# No necesitas un step separado de actions/cache!
```

### Rutas comunes de cache

| Gestor de paquetes | Ruta a cachear | Hash file |
|---------------------|----------------|-----------|
| npm | `~/.npm` | `package-lock.json` |
| yarn | `~/.cache/yarn` | `yarn.lock` |
| pip | `~/.cache/pip` | `requirements.txt` |
| composer | `~/.cache/composer` | `composer.lock` |
| maven | `~/.m2/repository` | `pom.xml` |
| gradle | `~/.gradle/caches` | `*.gradle` |

### Limites del cache

- Tamanio maximo por cache: 10 GB
- Tamanio total de caches por repositorio: 10 GB
- Los caches que no se usan en 7 dias se eliminan automaticamente
- Los caches mas antiguos se eliminan cuando se alcanza el limite de 10 GB

---

## 8. Artefactos

Los artefactos son archivos generados durante la ejecucion de un workflow
que quieres conservar. Ejemplos: binarios compilados, reportes de pruebas,
capturas de pantalla, logs.

### Subir artefactos

```yaml
steps:
  - name: Generar reporte
    run: |
      mkdir -p reportes
      echo "Resultado: OK" > reportes/resultado.txt

  - name: Subir artefacto
    uses: actions/upload-artifact@v4
    with:
      name: mi-reporte                # Nombre del artefacto
      path: reportes/resultado.txt    # Ruta del archivo/carpeta
      retention-days: 5               # Dias de retencion (defecto: 90)
```

### Descargar artefactos (entre jobs)

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - run: echo "binario compilado" > app.bin
      - uses: actions/upload-artifact@v4
        with:
          name: build-output
          path: app.bin

  deploy:
    needs: build
    runs-on: ubuntu-latest
    steps:
      - uses: actions/download-artifact@v4
        with:
          name: build-output
          path: ./descargado/
      - run: cat descargado/app.bin
```

### Subir multiples archivos

```yaml
- uses: actions/upload-artifact@v4
  with:
    name: reportes-de-test
    path: |
      coverage/
      test-results/
      screenshots/*.png
    # Excluir archivos
    # path: |
    #   build/
    #   !build/temp/
```

---

## 9. Buenas practicas

### Nombrado

- Nombres de workflows: descriptivos (`CI - Tests`, `CD - Deploy to Production`)
- Nombres de jobs: kebab-case (`build-and-test`, `deploy-staging`)
- Nombres de steps: descriptivos y concisos (`Instalar dependencias`, `Ejecutar tests`)

### Seguridad

- Siempre usa secretos para tokens y credenciales
- Fija las versiones de las actions con el SHA completo en produccion
- Limita los permisos del `GITHUB_TOKEN` al minimo necesario
- Nunca confies en datos de PRs de forks

### Rendimiento

- Usa cache para dependencias
- Usa `fail-fast: true` en matrices si un fallo invalida todo
- Ejecuta jobs en paralelo cuando sea posible
- Usa runners Linux (mas baratos y rapidos)
- Usa `paths` para evitar ejecutar workflows innecesariamente

### Mantenibilidad

- Un workflow por archivo (no mezclar CI y CD)
- Comenta las decisiones no obvias
- Usa variables de entorno para valores repetidos
- Agrupa logica compleja en acciones reutilizables

---

## Archivos de ejemplo

| Archivo | Que demuestra |
|---------|---------------|
| `evento_push.yml` | Workflow activado por push con filtros de rama y ruta |
| `evento_pr.yml` | Workflow activado por pull requests |
| `evento_schedule.yml` | Workflow programado con cron |
| `manual_dispatch.yml` | Workflow con ejecucion manual y parametros |
| `variables_secretos.yml` | Uso de variables de entorno, secretos y contextos |
| `matriz_estrategia.yml` | Matrices para pruebas multi-version y multi-OS |
| `cache_dependencias.yml` | Cache de dependencias para npm, pip y composer |

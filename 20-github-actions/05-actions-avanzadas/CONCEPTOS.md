# 05 - GitHub Actions Avanzadas

## Contenido

1. [Acciones personalizadas](#1-acciones-personalizadas)
2. [Acciones compuestas](#2-acciones-compuestas-composite)
3. [Acciones JavaScript](#3-acciones-javascript)
4. [Acciones Docker](#4-acciones-docker)
5. [Workflows reutilizables](#5-workflows-reutilizables)
6. [Self-hosted runners](#6-self-hosted-runners)
7. [Seguridad](#7-seguridad)
8. [OpenID Connect (OIDC)](#8-openid-connect-oidc)
9. [Control de concurrencia](#9-control-de-concurrencia)
10. [Debugging de workflows](#10-debugging-de-workflows)

---

## 1. Acciones personalizadas

Cuando la logica se repite en multiples workflows, puedes encapsularla
en una **accion personalizada** (custom action).

### Tipos de acciones personalizadas

| Tipo | Lenguaje | Donde se ejecuta | Velocidad | Complejidad |
|------|----------|-------------------|-----------|-------------|
| **Composite** | YAML (steps) | En el runner directamente | Rapida | Baja |
| **JavaScript** | JavaScript/TypeScript | Node.js en el runner | Rapida | Media |
| **Docker** | Cualquiera | Contenedor Docker | Lenta (build) | Alta |

### Cuando crear una accion personalizada

```
  ANTES (repeticion en multiples workflows):

  workflow-1.yml:           workflow-2.yml:           workflow-3.yml:
  steps:                    steps:                    steps:
    - run: paso A             - run: paso A             - run: paso A
    - run: paso B             - run: paso B             - run: paso B
    - run: paso C             - run: paso C             - run: paso C

  DESPUES (accion reutilizable):

  workflow-1.yml:           workflow-2.yml:           workflow-3.yml:
  steps:                    steps:                    steps:
    - uses: mi-accion        - uses: mi-accion         - uses: mi-accion

  mi-accion/action.yml:
    runs:
      steps:
        - run: paso A
        - run: paso B
        - run: paso C
```

---

## 2. Acciones compuestas (Composite)

Las acciones compuestas son las mas simples de crear. Son basicamente una
lista de steps empaquetados en un archivo `action.yml`.

### Estructura de una accion compuesta

```
mi-accion/
|-- action.yml      <-- Definicion de la accion (obligatorio)
+-- scripts/        <-- Scripts auxiliares (opcional)
    +-- setup.sh
```

### Anatomia del action.yml

```yaml
# mi-accion/action.yml
name: 'Mi Accion Compuesta'
description: 'Descripcion de lo que hace'
author: 'Tu Nombre'

# Inputs que recibe la accion
inputs:
  version:
    description: 'Version del lenguaje'
    required: true
    default: '3.12'
  entorno:
    description: 'Entorno de despliegue'
    required: false
    default: 'staging'

# Outputs que produce la accion
outputs:
  resultado:
    description: 'Resultado de la ejecucion'
    value: ${{ steps.ejecutar.outputs.resultado }}

# Tipo: composite
runs:
  using: 'composite'
  steps:
    - name: Paso 1
      shell: bash          # OBLIGATORIO en composite actions
      run: echo "Version: ${{ inputs.version }}"

    - name: Paso 2
      id: ejecutar
      shell: bash
      run: |
        echo "resultado=exito" >> $GITHUB_OUTPUT
```

### Como usar una accion compuesta

```yaml
# En tu workflow:
steps:
  # Accion local (del mismo repositorio)
  - uses: ./.github/actions/mi-accion
    with:
      version: '3.12'

  # Accion de otro repositorio
  - uses: usuario/repo/.github/actions/mi-accion@v1
    with:
      version: '3.12'
```

**Nota importante:** En composite actions, el `shell` es OBLIGATORIO en cada
step de tipo `run`. Esto es diferente de los workflows normales donde es opcional.

---

## 3. Acciones JavaScript

Las acciones JavaScript son mas poderosas. Pueden usar la API de GitHub,
manejar inputs/outputs de forma programatica y usar paquetes npm.

### Estructura

```
mi-accion-js/
|-- action.yml
|-- index.js         <-- Punto de entrada
|-- package.json
+-- node_modules/    <-- Dependencias (se deben commitear o usar ncc)
```

### action.yml para JavaScript

```yaml
name: 'Mi Accion JavaScript'
description: 'Accion escrita en JavaScript'
inputs:
  token:
    description: 'GitHub token'
    required: true
outputs:
  resultado:
    description: 'Resultado'
runs:
  using: 'node20'       # Version de Node.js
  main: 'index.js'      # Archivo de entrada
```

### index.js basico

```javascript
const core = require('@actions/core');
const github = require('@actions/github');

async function run() {
  try {
    // Leer inputs
    const token = core.getInput('token', { required: true });

    // Acceder al contexto de GitHub
    const context = github.context;
    console.log(`Repo: ${context.repo.owner}/${context.repo.repo}`);

    // Usar la API de GitHub
    const octokit = github.getOctokit(token);
    const { data: issues } = await octokit.rest.issues.list({
      owner: context.repo.owner,
      repo: context.repo.repo,
    });

    // Definir outputs
    core.setOutput('resultado', `Encontrados ${issues.length} issues`);
  } catch (error) {
    core.setFailed(`Error: ${error.message}`);
  }
}

run();
```

---

## 4. Acciones Docker

Las acciones Docker ejecutan tu codigo dentro de un contenedor Docker.
Son utiles cuando necesitas un entorno especifico o un lenguaje no soportado
nativamente por los runners.

### Estructura

```
mi-accion-docker/
|-- action.yml
|-- Dockerfile
+-- entrypoint.sh
```

### action.yml para Docker

```yaml
name: 'Mi Accion Docker'
description: 'Accion que corre en Docker'
inputs:
  parametro:
    description: 'Un parametro'
    required: true
runs:
  using: 'docker'
  image: 'Dockerfile'
  args:
    - ${{ inputs.parametro }}
```

### Limitaciones

- Solo funcionan en runners Linux
- Mas lentas (necesitan construir la imagen)
- El Dockerfile y dependencias se descargan cada vez

---

## 5. Workflows reutilizables

Los workflows reutilizables (reusable workflows) permiten definir un
workflow completo que otros workflows pueden invocar, similar a una funcion.

### Diferencia con acciones

```
  ACCION:                           WORKFLOW REUTILIZABLE:
  ======                            =====================
  - Se usa en un STEP               - Se usa como un JOB completo
  - uses: en un step                - uses: en un job
  - Definida en action.yml          - Definida en un .yml normal
  - Puede ser composite/JS/Docker   - Es un workflow YAML completo
  - Mas granular (un paso)          - Mas amplio (multiples jobs/steps)
```

### Definir un workflow reutilizable

```yaml
# .github/workflows/workflow_reutilizable.yml
name: Workflow Reutilizable

# El trigger DEBE ser workflow_call
on:
  workflow_call:
    # Inputs que recibe
    inputs:
      entorno:
        description: 'Entorno de despliegue'
        required: true
        type: string
      node-version:
        description: 'Version de Node.js'
        required: false
        type: string
        default: '20'
    # Secretos que recibe
    secrets:
      deploy-token:
        description: 'Token de despliegue'
        required: true
    # Outputs que devuelve
    outputs:
      url:
        description: 'URL del despliegue'
        value: ${{ jobs.deploy.outputs.url }}

jobs:
  deploy:
    runs-on: ubuntu-latest
    outputs:
      url: ${{ steps.deploy.outputs.url }}
    steps:
      - uses: actions/checkout@v4
      - run: echo "Desplegando a ${{ inputs.entorno }}"
      - id: deploy
        run: echo "url=https://ejemplo.com" >> $GITHUB_OUTPUT
```

### Invocar un workflow reutilizable

```yaml
# Otro workflow que LLAMA al reutilizable:
jobs:
  deploy-staging:
    uses: ./.github/workflows/workflow_reutilizable.yml
    with:
      entorno: staging
      node-version: '20'
    secrets:
      deploy-token: ${{ secrets.DEPLOY_TOKEN }}
      # O para pasar TODOS los secretos:
      # secrets: inherit
```

### Limitaciones

- Un workflow puede llamar maximo 20 workflows reutilizables
- No se pueden anidar mas de 4 niveles de profundidad
- Las variables de entorno del caller no se heredan

---

## 6. Self-hosted runners

Los self-hosted runners son maquinas que tu administras y que ejecutan
los workflows de GitHub Actions.

### Cuando usar self-hosted runners

| Usar cuando... | No usar cuando... |
|----------------|-------------------|
| Necesitas hardware especifico (GPU, ARM) | Los runners de GitHub son suficientes |
| Tienes requisitos de compliance | Es un proyecto open source |
| El build necesita acceso a red interna | No quieres mantener infraestructura |
| Quieres evitar limites de minutos | El proyecto es pequeno |
| Necesitas persistencia entre jobs | Quieres simplicidad |

### Arquitectura

```
  GITHUB                          TU INFRAESTRUCTURA
  ======                          ==================

  +----------+                    +------------------+
  | Workflow  |   Poll/HTTPS      | Self-hosted      |
  | (cola de |<------------------>| Runner           |
  |  jobs)   |                    | (tu servidor)    |
  +----------+                    +------------------+
                                  |  - Escucha jobs  |
                                  |  - Los ejecuta   |
                                  |  - Reporta result|
                                  +------------------+
```

### Como configurar

1. Settings > Actions > Runners > New self-hosted runner
2. Seguir instrucciones para descargar e instalar el runner
3. El runner se conecta a GitHub via HTTPS (no necesitas abrir puertos)
4. Usar en workflows con:

```yaml
runs-on: self-hosted
# O con labels personalizados:
runs-on: [self-hosted, linux, x64, gpu]
```

### Consideraciones de seguridad

- NUNCA uses self-hosted runners en repos publicos
  (cualquiera podria ejecutar codigo malicioso en tu servidor)
- Ejecuta el runner como un usuario sin privilegios
- Usa contenedores para aislar las ejecuciones
- Limpia el workspace despues de cada job

---

## 7. Seguridad

### Fijar versiones de acciones (version pinning)

```yaml
# RIESGOSO: la tag "v4" puede cambiar si el mantenedor la mueve
- uses: actions/checkout@v4

# SEGURO: el SHA del commit es inmutable
- uses: actions/checkout@b4ffde65f46336ab88eb53be808477a3936bae11 # v4.1.1
```

**Por que importa:** Un atacante podria comprometer una accion popular y mover
el tag a un commit malicioso. Con el SHA, siempre usas exactamente el mismo
codigo.

### Principio de minimo privilegio

```yaml
# MALO: permisos amplios
permissions: write-all

# BUENO: solo lo necesario
permissions:
  contents: read
  pull-requests: write
```

### CODEOWNERS

El archivo `CODEOWNERS` define quien debe aprobar cambios en archivos criticos:

```
# .github/CODEOWNERS

# Los cambios a workflows requieren aprobacion del equipo DevOps
.github/workflows/ @equipo/devops

# Los cambios a configuracion de seguridad requieren aprobacion de Security
.github/CODEOWNERS @equipo/security
```

### Proteger secretos

```yaml
# NUNCA hagas esto:
run: echo ${{ secrets.TOKEN }}      # El secreto se enmascara, pero es riesgoso

# NUNCA exportes secretos a archivos:
run: echo ${{ secrets.TOKEN }} > config.txt   # Queda en disco!

# CORRECTO: usar como variable de entorno
env:
  TOKEN: ${{ secrets.TOKEN }}
run: curl -H "Authorization: Bearer $TOKEN" https://api.example.com
```

### Secret scanning

GitHub escanea automaticamente tu repositorio buscando secretos expuestos
(tokens de AWS, claves de API, etc.). Si encuentra uno:

1. Te notifica
2. Puede revocar automaticamente el secreto (si el proveedor lo soporta)
3. Bloquea el push si tienes "push protection" activado

Para activar: Settings > Code security > Secret scanning

---

## 8. OpenID Connect (OIDC)

OIDC permite a tus workflows autenticarse con proveedores cloud (AWS, Azure, GCP)
sin necesidad de almacenar credenciales de larga duracion como secretos.

### Como funciona

```
  SIN OIDC:                             CON OIDC:

  1. Crear credenciales de AWS          1. Configurar trust policy en AWS
  2. Guardar como secreto en GitHub     2. El workflow solicita un token OIDC
  3. Workflow usa las credenciales      3. AWS valida el token con GitHub
  4. Si se filtran, acceso permanente   4. AWS emite credenciales temporales
                                        5. Credenciales expiran automaticamente

  Riesgo: alto (credenciales permanentes)   Riesgo: bajo (credenciales temporales)
```

### Ejemplo con AWS

```yaml
permissions:
  id-token: write     # Necesario para solicitar el token OIDC
  contents: read

steps:
  - name: Configurar credenciales AWS (OIDC)
    uses: aws-actions/configure-aws-credentials@v4
    with:
      role-to-assume: arn:aws:iam::123456789:role/mi-rol-github
      aws-region: us-east-1
      # No necesitas access-key-id ni secret-access-key!
```

### Proveedores soportados

| Proveedor | Action oficial |
|-----------|---------------|
| AWS | `aws-actions/configure-aws-credentials@v4` |
| Azure | `azure/login@v2` |
| GCP | `google-github-actions/auth@v2` |
| HashiCorp Vault | `hashicorp/vault-action@v3` |

---

## 9. Control de concurrencia

La concurrencia controla cuantas ejecuciones del mismo workflow pueden
correr simultaneamente.

### Grupos de concurrencia

```yaml
# Todas las ejecuciones con el mismo "group" se agrupan.
# Solo una ejecucion por grupo puede estar activa.
concurrency:
  group: deploy-production
  cancel-in-progress: false    # Esperar (no cancelar la que esta corriendo)
```

### Patrones comunes

```yaml
# Patron 1: Una ejecucion por rama (cancelar anteriores)
# Ideal para CI en PRs: solo importa el ultimo commit
concurrency:
  group: ci-${{ github.ref }}
  cancel-in-progress: true

# Patron 2: Una ejecucion por PR
concurrency:
  group: pr-${{ github.event.pull_request.number }}
  cancel-in-progress: true

# Patron 3: Un deploy a la vez (NO cancelar)
# Importante para deploys: no quieres interrumpir uno a la mitad
concurrency:
  group: deploy-${{ inputs.entorno }}
  cancel-in-progress: false

# Patron 4: Un deploy por entorno
concurrency:
  group: deploy-${{ github.event.inputs.entorno || 'staging' }}
  cancel-in-progress: false
```

### Ejemplo visual

```
  Sin concurrencia:           Con concurrencia (cancel-in-progress: true):

  Push 1: ===========         Push 1: =====X (cancelado)
  Push 2:   =========         Push 2:      =====X (cancelado)
  Push 3:     =======         Push 3:           ============
                              (solo el ultimo se completa)
```

---

## 10. Debugging de workflows

### Activar logs de debug

Para activar logs detallados, define este secreto en tu repositorio:

| Secreto | Valor | Efecto |
|---------|-------|--------|
| `ACTIONS_STEP_DEBUG` | `true` | Logs detallados de cada step |
| `ACTIONS_RUNNER_DEBUG` | `true` | Logs detallados del runner |

### Debugging en el workflow

```yaml
steps:
  # Imprimir todo el contexto del evento
  - name: Debug - contexto del evento
    run: echo '${{ toJSON(github.event) }}'

  # Imprimir todas las variables de entorno
  - name: Debug - variables de entorno
    run: env | sort

  # Step condicional de debug
  - name: Debug info
    if: runner.debug == '1'
    run: |
      echo "Debug mode activado"
      echo "Contexto completo:"
      echo '${{ toJSON(github) }}'
```

### Herramientas de debugging

| Herramienta | Uso |
|-------------|-----|
| `act` | Ejecutar workflows localmente (sin push a GitHub) |
| `gh run view` | Ver logs de una ejecucion desde la CLI |
| `gh run rerun` | Re-ejecutar un workflow fallido |
| `gh run watch` | Ver la ejecucion en tiempo real |

### Comando `act` (ejecucion local)

```bash
# Instalar act
brew install act           # macOS
# o
curl -s https://raw.githubusercontent.com/nektos/act/master/install.sh | sudo bash

# Ejecutar un workflow localmente
act push                    # Simular un push
act pull_request            # Simular un PR
act -j mi-job               # Ejecutar solo un job
act --list                  # Listar todos los workflows
act -s MY_SECRET=value      # Pasar un secreto
```

---

## Archivos de ejemplo

| Archivo | Que demuestra |
|---------|---------------|
| `accion_compuesta.yml` | Crear y usar una accion compuesta |
| `workflow_reutilizable.yml` | Workflows reutilizables con workflow_call |
| `concurrencia.yml` | Patrones de control de concurrencia |
| `seguridad.yml` | Mejores practicas de seguridad |

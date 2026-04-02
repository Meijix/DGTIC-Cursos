# 01 - Introduccion a GitHub Actions y CI/CD

## Contenido

1. [Que es CI/CD?](#1-que-es-cicd)
2. [El pipeline de CI/CD](#2-el-pipeline-de-cicd)
3. [Que son GitHub Actions?](#3-que-son-github-actions)
4. [Terminologia clave](#4-terminologia-clave)
5. [Sintaxis basica de YAML](#5-sintaxis-basica-de-yaml)
6. [Comparativa con otras herramientas](#6-comparativa-con-otras-herramientas)
7. [Convencion de directorios](#7-convencion-de-directorios)
8. [Limites y facturacion](#8-limites-del-plan-gratuito-y-facturacion)
9. [Errores comunes de principiante](#9-errores-comunes-de-principiante)

---

## 1. Que es CI/CD?

CI/CD son las siglas de **Continuous Integration** (Integracion Continua) y
**Continuous Delivery/Deployment** (Entrega/Despliegue Continuo). Es una practica
de desarrollo de software que busca automatizar las tareas repetitivas del ciclo
de vida del software.

### Integracion Continua (CI)

La CI consiste en integrar los cambios de codigo de multiples desarrolladores en
un repositorio compartido de forma frecuente (idealmente, varias veces al dia).
Cada integracion se verifica mediante:

- Compilacion automatica del codigo
- Ejecucion de pruebas automatizadas
- Analisis de calidad de codigo (linting)
- Verificacion de que no se rompio nada existente

**Problema que resuelve:** Sin CI, los equipos integran codigo una vez a la semana
o al final del sprint. Esto genera conflictos masivos, bugs dificiles de rastrear,
y el temido "funciona en mi maquina".

### Entrega Continua (CD - Delivery)

La entrega continua extiende la CI asegurando que el codigo esta **siempre en un
estado desplegable**. Despues de pasar todas las pruebas, el codigo se empaqueta
y se prepara para su despliegue. El despliegue final se hace con un clic manual.

### Despliegue Continuo (CD - Deployment)

El despliegue continuo va un paso mas alla: cada cambio que pasa las pruebas se
despliega **automaticamente** a produccion sin intervencion humana.

```
Delivery:   codigo --> pruebas --> empaquetado --> [boton manual] --> produccion
Deployment: codigo --> pruebas --> empaquetado --> produccion (automatico)
```

---

## 2. El pipeline de CI/CD

Un pipeline es la secuencia completa de pasos automatizados que recorre el codigo
desde el commit del desarrollador hasta su despliegue.

```
  DESARROLLADOR          REPOSITORIO           CI/CD PIPELINE              PRODUCCION
  =============          ===========           ==============              ==========

  +----------+           +---------+           +---------------+           +----------+
  |  Escribe |  git push |         |  trigger  |   1. Build    |           |          |
  |  codigo  |---------->| GitHub  |---------->|   2. Test     |           | Servidor |
  |  local   |           | Repo    |           |   3. Lint     |---------->| o Cloud  |
  +----------+           +---------+           |   4. Package  |  deploy   |          |
       ^                      |                |   5. Deploy   |           +----------+
       |                      |                +---------------+
       |                      |                       |
       |                      v                       v
       |                 +---------+           +-------------+
       +<----------------|  Merge  |           | Notifica al |
        feedback         | o block |           | equipo      |
                         +---------+           +-------------+
```

### Flujo tipico paso a paso

```
1. El desarrollador hace push de su rama
            |
            v
2. GitHub detecta el evento (push/PR)
            |
            v
3. Se activa el workflow definido en .github/workflows/
            |
            v
4. GitHub asigna un runner (maquina virtual)
            |
            v
5. Se ejecutan los jobs definidos:
   a) Instalar dependencias
   b) Compilar (si aplica)
   c) Ejecutar pruebas
   d) Ejecutar linters
   e) Generar artefactos
            |
            v
6. Resultado: EXITO o FALLO
   - Si EXITO: se puede hacer merge / deploy
   - Si FALLO: se bloquea el merge, se notifica al dev
```

---

## 3. Que son GitHub Actions?

GitHub Actions es la plataforma de CI/CD **integrada directamente en GitHub**.
No necesitas configurar un servidor externo ni crear cuentas adicionales. Los
workflows se definen como archivos YAML dentro de tu repositorio.

### Caracteristicas principales

- **Integrado en GitHub**: no necesitas salir de la plataforma
- **Basado en eventos**: se activan con push, PR, issues, cron, etc.
- **Marketplace**: miles de acciones reutilizables creadas por la comunidad
- **Multi-plataforma**: runners con Linux, macOS y Windows
- **Gratis**: para repositorios publicos (con limites en repos privados)
- **Infraestructura como codigo**: los pipelines viven en el repositorio

### Como funciona internamente

```
  TU REPOSITORIO                    GITHUB
  ================                  ======

  .github/
    workflows/
      ci.yml  ----+
      cd.yml  ----|----> GitHub lee estos archivos
                   |     y registra los triggers
                   |
  (evento: push)   |
        |          |
        +--------->+
                   |
                   v
            +-------------+
            |  GitHub crea |
            |  un runner   |
            |  (maq.virtual)|
            +-------------+
                   |
                   v
            +-------------+
            | Ejecuta los  |
            | steps del    |
            | workflow     |
            +-------------+
                   |
                   v
            +-------------+
            | Reporta      |
            | resultado en |
            | la pestana   |
            | "Actions"    |
            +-------------+
```

---

## 4. Terminologia clave

Es fundamental dominar estos conceptos antes de escribir tu primer workflow:

### Tabla de terminologia

| Termino | Que es | Analogia |
|---------|--------|----------|
| **Workflow** | Archivo YAML que define el proceso automatizado completo | La receta de cocina completa |
| **Event** | Lo que dispara (activa) el workflow | El timbre que suena para empezar a cocinar |
| **Job** | Conjunto de pasos que se ejecutan en un mismo runner | Un plato de la receta |
| **Step** | Una tarea individual dentro de un job | Un paso de la preparacion del plato |
| **Action** | Unidad reutilizable de codigo (propia o del Marketplace) | Un electrodomestico que ya hace algo especifico |
| **Runner** | Maquina virtual donde se ejecutan los jobs | La cocina donde se prepara todo |
| **Artifact** | Archivo generado durante el workflow (binarios, reportes) | El plato terminado |
| **Secret** | Variable cifrada almacenada en GitHub | La receta secreta que no compartes |

### Relacion jerarquica

```
WORKFLOW (archivo .yml)
|
|-- on: (EVENTO que lo activa)
|     |-- push
|     |-- pull_request
|     +-- schedule
|
+-- jobs:
      |
      +-- job-1: (JOB: se ejecuta en un RUNNER)
      |     |-- runs-on: ubuntu-latest
      |     +-- steps:
      |           |-- step 1: uses: actions/checkout@v4   <-- ACTION
      |           |-- step 2: run: npm install            <-- Comando shell
      |           +-- step 3: run: npm test               <-- Comando shell
      |
      +-- job-2: (otro JOB, puede ser paralelo o dependiente)
            |-- runs-on: windows-latest
            +-- steps:
                  |-- step 1: ...
                  +-- step 2: ...
```

### Workflow

Un workflow es un proceso automatizado configurable definido en un archivo YAML.
Se almacena en `.github/workflows/` y puede contener uno o mas jobs.

**Ejemplo:** un workflow que ejecuta pruebas cada vez que alguien hace push.

### Event (Evento)

Un evento es una actividad especifica en el repositorio que activa un workflow.
Puede ser:

- **Actividad del repositorio:** push, pull_request, issues, release
- **Programado:** cron schedule (cada dia a las 3am, por ejemplo)
- **Manual:** workflow_dispatch (boton en la interfaz de GitHub)
- **Externo:** repository_dispatch (llamada desde API externa)

### Job (Trabajo)

Un job es un conjunto de steps que se ejecutan en el mismo runner. Por defecto,
los jobs se ejecutan en **paralelo**. Para ejecutarlos en secuencia, se usa `needs`.

### Step (Paso)

Un step es una tarea individual dentro de un job. Puede ser:
- Un comando shell (`run:`)
- Una action reutilizable (`uses:`)

Los steps se ejecutan siempre en **secuencia** (uno despues de otro).

### Action (Accion)

Una action es una aplicacion reutilizable para la plataforma de GitHub Actions.
Puedes usar acciones del Marketplace o crear las tuyas propias.

Ejemplos populares:
- `actions/checkout@v4` - Descarga el codigo del repositorio
- `actions/setup-node@v4` - Instala Node.js
- `actions/setup-python@v5` - Instala Python
- `actions/cache@v4` - Cachea dependencias

### Runner

Un runner es una maquina virtual que ejecuta los jobs. GitHub ofrece runners
hospedados (gratuitos) con estos sistemas operativos:

| Runner | Sistema operativo | Etiqueta |
|--------|-------------------|----------|
| Ubuntu | Linux | `ubuntu-latest`, `ubuntu-22.04`, `ubuntu-24.04` |
| macOS | macOS | `macos-latest`, `macos-14` |
| Windows | Windows | `windows-latest`, `windows-2022` |

Tambien puedes usar **self-hosted runners** (tu propio servidor).

### Artifact (Artefacto)

Un artefacto es un archivo producido durante la ejecucion de un workflow.
Ejemplos: binarios compilados, reportes de cobertura, logs. Se pueden compartir
entre jobs o descargar desde la interfaz de GitHub.

---

## 5. Sintaxis basica de YAML

YAML (YAML Ain't Markup Language) es el formato usado para definir los workflows.
Si vienes de JSON o XML, YAML es mucho mas legible.

### Reglas fundamentales

```yaml
# 1. Los comentarios empiezan con #

# 2. La indentacion es con ESPACIOS (nunca tabs)
#    Se recomiendan 2 espacios por nivel

# 3. Pares clave-valor
nombre: "Juan"
edad: 30
activo: true

# 4. Listas (con guion y espacio)
frutas:
  - manzana
  - naranja
  - platano

# 5. Objetos anidados (mas indentacion)
persona:
  nombre: "Ana"
  direccion:
    calle: "Av. Universidad"
    numero: 3000

# 6. Cadenas multilinea
descripcion: |
  Esta es una cadena
  que ocupa multiples lineas.
  Cada salto de linea se preserva.

descripcion_sin_saltos: >
  Esta cadena larga se
  une en una sola linea
  al procesarse.

# 7. Listas de objetos
empleados:
  - nombre: "Carlos"
    puesto: "Developer"
  - nombre: "Maria"
    puesto: "Designer"
```

### YAML en el contexto de GitHub Actions

```yaml
# Ejemplo minimo de un workflow
name: Mi Workflow          # Nombre descriptivo

on: push                   # Evento que lo activa

jobs:                      # Definicion de trabajos
  mi-job:                  # Identificador del job (sin espacios)
    runs-on: ubuntu-latest # Runner donde se ejecuta
    steps:                 # Lista de pasos
      - name: Saludo       # Nombre descriptivo del paso
        run: echo "Hola"   # Comando a ejecutar
```

### Errores comunes en YAML

| Error | Problema | Solucion |
|-------|----------|----------|
| Usar tabs en lugar de espacios | YAML no acepta tabs | Configurar editor para usar espacios |
| Indentacion inconsistente | Mezclar 2 y 4 espacios | Usar siempre 2 espacios |
| Olvidar las comillas en strings especiales | `on: true` se interpreta como booleano | Usar `on: "true"` o evitar palabras reservadas |
| No escapar caracteres especiales | `: ` dentro de strings | Poner la cadena entre comillas |
| Espacio faltante despues de `-` | `-item` en vez de `- item` | Siempre poner espacio despues del guion |

---

## 6. Comparativa con otras herramientas

| Caracteristica | GitHub Actions | Jenkins | GitLab CI | CircleCI |
|----------------|---------------|---------|-----------|----------|
| **Hospedaje** | SaaS (GitHub) | Self-hosted | SaaS / Self-hosted | SaaS |
| **Configuracion** | YAML en repo | Jenkinsfile / UI | `.gitlab-ci.yml` | `.circleci/config.yml` |
| **Runners gratuitos** | Si (repos publicos) | No (tu servidor) | Si (limitados) | Si (limitados) |
| **Marketplace** | 20,000+ acciones | 1,800+ plugins | Templates | Orbs |
| **Integracion con GitHub** | Nativa | Plugin | Limitada | Plugin |
| **Curva de aprendizaje** | Baja | Alta | Media | Media |
| **Multi-plataforma** | Linux, macOS, Windows | Depende del server | Linux (nativo) | Linux, macOS |
| **Precio (privado)** | 2,000 min/mes gratis | Gratis (tu infra) | 400 min/mes gratis | 6,000 min/mes gratis |
| **Escalabilidad** | Automatica | Manual | Automatica | Automatica |
| **Secretos** | Integrado | Plugin | Integrado | Integrado |
| **Self-hosted runners** | Si | Es el modelo base | Si | Si |
| **Cache** | Integrado | Plugin | Integrado | Integrado |

### Cuando elegir GitHub Actions

- Tu codigo ya esta en GitHub
- Quieres simplicidad y rapidez de configuracion
- No quieres mantener infraestructura de CI/CD
- Necesitas integracion profunda con PRs, issues, releases

### Cuando NO elegir GitHub Actions

- Tu codigo esta en otro proveedor (GitLab, Bitbucket)
- Necesitas pipelines extremadamente complejos con muchas dependencias
- Tienes requisitos de compliance que exigen CI/CD on-premise
- Necesitas mas de 2,000 minutos/mes en repos privados (sin pagar)

---

## 7. Convencion de directorios

GitHub Actions busca los workflows en una ruta especifica dentro del repositorio:

```
mi-repositorio/
|
+-- .github/
|     |
|     +-- workflows/          <-- AQUI van los workflows activos
|     |     |-- ci.yml
|     |     |-- cd.yml
|     |     +-- lint.yml
|     |
|     +-- ISSUE_TEMPLATE/     <-- Templates de issues (no relacionado)
|     +-- PULL_REQUEST_TEMPLATE.md
|     +-- CODEOWNERS           <-- Quien revisa que archivos
|     +-- dependabot.yml       <-- Configuracion de Dependabot
|
+-- src/
+-- tests/
+-- package.json
+-- README.md
```

### Reglas importantes

1. **Ruta obligatoria:** `.github/workflows/` (exactamente asi, con el punto)
2. **Extension:** `.yml` o `.yaml` (ambas son validas)
3. **Cantidad:** puedes tener multiples archivos de workflow
4. **Nombre del archivo:** cualquier nombre descriptivo (ej: `ci.yml`, `deploy.yml`)
5. **Rama:** el workflow se lee de la rama donde ocurre el evento

### Nota sobre este curso

Los archivos `.yml` de este curso estan en subcarpetas de aprendizaje (como
`01-introduccion/`), NO en `.github/workflows/`. Por lo tanto, **no se ejecutan
automaticamente**. Para probarlos, copialos a `.github/workflows/`.

---

## 8. Limites del plan gratuito y facturacion

### Repositorios publicos

| Recurso | Limite |
|---------|--------|
| Minutos de ejecucion | **Ilimitados** |
| Almacenamiento de artefactos | 500 MB |
| Jobs concurrentes | 20 |
| Runners disponibles | Linux, macOS, Windows |

### Repositorios privados (plan Free)

| Recurso | Limite |
|---------|--------|
| Minutos de ejecucion | **2,000 min/mes** |
| Almacenamiento de artefactos | 500 MB |
| Jobs concurrentes | 20 |

### Multiplicadores por sistema operativo

No todos los minutos cuestan igual en repos privados:

| Runner | Multiplicador | Ejemplo: job de 10 min |
|--------|---------------|------------------------|
| Linux | 1x | Gasta 10 minutos |
| Windows | 2x | Gasta 20 minutos |
| macOS | 10x | Gasta 100 minutos |

**Consejo:** Usa Linux siempre que sea posible para maximizar tus minutos gratuitos.

### Limites de ejecucion

| Limite | Valor |
|--------|-------|
| Duracion maxima de un workflow | 35 dias |
| Duracion maxima de un job | 6 horas |
| Jobs en cola maximos (por repo) | 500 |
| Tamanio maximo de un log | 64 KB por step |
| Tamanio maximo de artefactos | 500 MB (Free) |
| Retencion de artefactos | 90 dias |
| Retencion de logs | 400 dias |

---

## 9. Errores comunes de principiante

### 1. Poner el workflow en la ruta incorrecta

```
MAL:   github/workflows/ci.yml       (falta el punto)
MAL:   .github/workflow/ci.yml        (workflow sin s)
MAL:   .github/ci.yml                 (falta workflows/)
BIEN:  .github/workflows/ci.yml
```

### 2. Indentacion incorrecta en YAML

```yaml
# MAL - el step no esta indentado correctamente
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - name: Checkout          # Deberia tener mas indentacion
    run: echo "hola"          # Esto no es un atributo del step

# BIEN
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        run: echo "hola"
```

### 3. Olvidar actions/checkout

```yaml
# MAL - intentar acceder al codigo sin checkout
steps:
  - name: Ejecutar tests
    run: npm test    # FALLA: el codigo no esta en el runner

# BIEN - primero hacer checkout
steps:
  - name: Checkout del codigo
    uses: actions/checkout@v4
  - name: Ejecutar tests
    run: npm test    # Ahora si tiene acceso al codigo
```

### 4. No especificar la version de la action

```yaml
# RIESGOSO - usar la rama principal (puede cambiar)
uses: actions/checkout@main

# MEJOR - usar un tag de version
uses: actions/checkout@v4

# OPTIMO - usar el hash del commit (inmutable)
uses: actions/checkout@b4ffde65f46336ab88eb53be808477a3936bae11
```

### 5. Poner secretos en el archivo YAML

```yaml
# NUNCA hagas esto - el secreto queda en el historial de git
env:
  API_KEY: "sk-abc123secreto456"

# CORRECTO - usar secretos de GitHub
env:
  API_KEY: ${{ secrets.API_KEY }}
```

---

## Resumen

En esta seccion aprendiste:

- CI/CD automatiza la integracion, pruebas y despliegue de codigo
- GitHub Actions es la plataforma de CI/CD nativa de GitHub
- Los workflows se definen en archivos YAML dentro de `.github/workflows/`
- La jerarquia es: Workflow > Job > Step > Action
- YAML usa indentacion con espacios (nunca tabs)
- GitHub Actions es gratuito e ilimitado para repositorios publicos
- Los runners Linux son los mas economicos en repos privados

Ahora pasa a los archivos de ejemplo:
- `mi_primer_workflow.yml` - Tu primer workflow funcional
- `anatomia_workflow.yml` - Anatomia detallada de un workflow

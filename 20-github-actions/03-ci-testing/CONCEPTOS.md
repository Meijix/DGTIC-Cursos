# 03 - Integracion Continua y Testing

## Contenido

1. [Que es la Integracion Continua?](#1-que-es-la-integracion-continua)
2. [Testing en CI](#2-testing-en-ci)
3. [CI para Python](#3-ci-para-python)
4. [CI para JavaScript/Node.js](#4-ci-para-javascriptnodejs)
5. [CI para PHP](#5-ci-para-php)
6. [Linting y formateo](#6-linting-y-formateo)
7. [Matrices multi-version](#7-matrices-multi-version)
8. [Cobertura de codigo](#8-cobertura-de-codigo)
9. [Status badges](#9-status-badges)
10. [Branch protection rules](#10-branch-protection-rules)
11. [Patrones y buenas practicas](#11-patrones-y-buenas-practicas)

---

## 1. Que es la Integracion Continua?

La Integracion Continua (CI) es la practica de integrar cambios de codigo
frecuentemente y verificarlos automaticamente. El objetivo es detectar problemas
lo antes posible, cuando son mas faciles y baratos de arreglar.

### El costo de encontrar bugs tarde

```
  COSTO DE CORREGIR UN BUG vs CUANDO SE DETECTA

  Costo
    ^
    |                                                    $$$$$$
    |                                              $$$$$$
    |                                        $$$$$
    |                                  $$$$
    |                            $$$
    |                      $$
    |                 $
    |            $
    |       $
    |   $
    +--$-------+--------+--------+--------+--------+-----> Tiempo
       |       |        |        |        |        |
    Mientras  En code   En CI    En QA    En       En
    escribes  review              manual staging  produccion
    el codigo

  La CI detecta bugs aqui:   ^
  Sin CI, se detectan aqui:               ^    ^    ^
```

### Flujo de trabajo con CI

```
  +-------------+     +-----------+     +-------------+
  | Desarrollar |---->| git push  |---->|   CI activa  |
  |  (local)    |     | (remoto)  |     |  workflow    |
  +-------------+     +-----------+     +-------------+
                                              |
                                    +---------+---------+
                                    |         |         |
                                    v         v         v
                               +-------+ +-------+ +--------+
                               | Build | | Tests | |  Lint  |
                               +-------+ +-------+ +--------+
                                    |         |         |
                                    +---------+---------+
                                              |
                                     +--------+--------+
                                     |                 |
                                     v                 v
                              +-----------+     +-----------+
                              |  EXITO    |     |  FALLO    |
                              |  (verde)  |     |  (rojo)   |
                              +-----------+     +-----------+
                                     |                 |
                                     v                 v
                              +-----------+     +-----------+
                              | Se puede  |     | Bloquear  |
                              | hacer     |     | merge y   |
                              | merge     |     | notificar |
                              +-----------+     +-----------+
```

### Que debe hacer un pipeline de CI?

| Paso | Que hace | Herramientas |
|------|----------|-------------|
| **Build** | Compilar/construir el proyecto | npm run build, pip install, composer install |
| **Lint** | Verificar estilo y calidad del codigo | ESLint, Flake8, PHPStan, Prettier |
| **Test unitarios** | Probar funciones individuales | Jest, pytest, PHPUnit |
| **Test integracion** | Probar componentes juntos | Supertest, pytest, Cypress |
| **Cobertura** | Medir cuanto codigo se prueba | Istanbul/nyc, coverage.py, Xdebug |
| **Seguridad** | Buscar vulnerabilidades | npm audit, pip-audit, Snyk |

---

## 2. Testing en CI

### Tipos de pruebas en CI

```
                    PIRAMIDE DE TESTING

                         /\
                        /  \
                       / E2E\        Pocas, lentas, costosas
                      / Tests\       (Cypress, Playwright)
                     /--------\
                    /Integracion\    Algunas, moderadas
                   /   Tests     \   (Supertest, Testcontainers)
                  /--------------\
                 /  Tests Unitarios\  Muchas, rapidas, baratas
                /                   \ (Jest, pytest, PHPUnit)
               /---------------------\
```

### Estrategia de testing en CI

| Evento | Tests a ejecutar | Razon |
|--------|-----------------|-------|
| Push a feature branch | Unitarios + Lint | Feedback rapido al desarrollador |
| Pull Request a main | Unitarios + Integracion + Lint | Verificacion completa antes de merge |
| Push a main | Todos (incluido E2E) | Maxima confianza antes de deploy |
| Schedule (nightly) | Todos + lentos + performance | Tests que tardan demasiado para CI |

---

## 3. CI para Python

### Estructura tipica de un proyecto Python con CI

```
mi-proyecto-python/
|-- src/
|   |-- __init__.py
|   +-- calculadora.py
|-- tests/
|   |-- __init__.py
|   +-- test_calculadora.py
|-- requirements.txt
|-- requirements-dev.txt
|-- setup.py o pyproject.toml
|-- .flake8 o setup.cfg
+-- .github/
    +-- workflows/
        +-- ci_python.yml
```

### Herramientas clave

| Herramienta | Proposito | Comando |
|-------------|-----------|---------|
| pytest | Framework de testing | `pytest` |
| coverage.py | Cobertura de codigo | `pytest --cov=src` |
| flake8 | Linter (estilo PEP 8) | `flake8 src/` |
| black | Formateador automatico | `black --check src/` |
| mypy | Verificador de tipos | `mypy src/` |
| isort | Ordenar imports | `isort --check src/` |
| pip-audit | Auditar vulnerabilidades | `pip-audit` |

---

## 4. CI para JavaScript/Node.js

### Estructura tipica

```
mi-proyecto-node/
|-- src/
|   +-- index.js
|-- tests/
|   +-- index.test.js
|-- package.json
|-- package-lock.json
|-- .eslintrc.json
|-- jest.config.js
+-- .github/
    +-- workflows/
        +-- ci_node.yml
```

### Herramientas clave

| Herramienta | Proposito | Comando |
|-------------|-----------|---------|
| Jest | Framework de testing | `npx jest` |
| Vitest | Testing (Vite projects) | `npx vitest run` |
| ESLint | Linter | `npx eslint src/` |
| Prettier | Formateador | `npx prettier --check .` |
| npm audit | Auditar vulnerabilidades | `npm audit` |
| TypeScript | Verificar tipos | `npx tsc --noEmit` |

### npm ci vs npm install

| Comando | Uso en CI | Comportamiento |
|---------|-----------|----------------|
| `npm ci` | Recomendado | Borra node_modules, instala desde package-lock.json (determinista) |
| `npm install` | No recomendado | Puede actualizar package-lock.json (no determinista) |

---

## 5. CI para PHP

### Estructura tipica

```
mi-proyecto-php/
|-- src/
|   +-- Calculadora.php
|-- tests/
|   +-- CalculadoraTest.php
|-- composer.json
|-- composer.lock
|-- phpunit.xml
|-- phpstan.neon
+-- .github/
    +-- workflows/
        +-- ci_php.yml
```

### Herramientas clave

| Herramienta | Proposito | Comando |
|-------------|-----------|---------|
| PHPUnit | Framework de testing | `vendor/bin/phpunit` |
| PHPStan | Analisis estatico | `vendor/bin/phpstan analyse` |
| PHP_CodeSniffer | Linter (estilo PSR-12) | `vendor/bin/phpcs` |
| Psalm | Analisis estatico | `vendor/bin/psalm` |

---

## 6. Linting y formateo

### Por que incluir linting en CI?

El linting en CI garantiza que **todo el codigo** sigue las mismas reglas de
estilo, sin importar la configuracion del editor de cada desarrollador.

```
  SIN LINTING EN CI:                     CON LINTING EN CI:

  Dev A: usa tabs                        Dev A: configura como quiera
  Dev B: usa espacios                    Dev B: configura como quiera
  Dev C: otro estilo                     Dev C: configura como quiera
                                              |
  Resultado: codigo inconsistente        CI: "Fallo: estilo incorrecto"
                                              |
                                         Resultado: codigo consistente
```

### Linters comunes por lenguaje

| Lenguaje | Linter | Formateador | Config |
|----------|--------|-------------|--------|
| Python | flake8, pylint, ruff | black, autopep8 | `.flake8`, `pyproject.toml` |
| JavaScript | ESLint | Prettier | `.eslintrc.json`, `.prettierrc` |
| TypeScript | ESLint + @typescript-eslint | Prettier | `.eslintrc.json` |
| PHP | PHP_CodeSniffer, PHPStan | PHP-CS-Fixer | `phpcs.xml`, `phpstan.neon` |
| Go | golangci-lint | gofmt | `.golangci.yml` |

---

## 7. Matrices multi-version

### Cuando usar matrices

Las matrices son esenciales cuando tu codigo debe funcionar en multiples
versiones de un lenguaje o en multiples sistemas operativos.

```
  MATRIX DE PYTHON:

  +----------+----------+----------+
  |  Python  |  Python  |  Python  |
  |   3.10   |   3.11   |   3.12   |
  +----------+----------+----------+
  |  pytest  |  pytest  |  pytest  |
  | PASS     | PASS     | PASS     |
  +----------+----------+----------+

  MATRIX DE NODE:

  +----------+----------+----------+
  |  Node 18 |  Node 20 |  Node 22 |
  +----------+----------+----------+
  |  jest    |  jest    |  jest    |
  | PASS     | PASS     | FAIL!   |  <-- Detecta incompatibilidad
  +----------+----------+----------+
```

### Consideraciones de rendimiento

| Combinaciones | Jobs | Tiempo aprox (serial) | Costo (minutos) |
|---------------|------|-----------------------|-----------------|
| 3 versiones | 3 | 3 x 2 min = 6 min | 6 minutos |
| 3 versiones x 2 OS | 6 | Paralelo: ~2 min | 6 minutos |
| 3 versiones x 3 OS | 9 | Paralelo: ~2 min | 9 minutos |
| 5 versiones x 3 OS x 2 BD | 30 | Paralelo: ~2 min | 30 minutos |

En repos privados, cada minuto cuenta contra tu cuota. Usa matrices con
prudencia y aprovecha `exclude` para eliminar combinaciones innecesarias.

---

## 8. Cobertura de codigo

### Que es la cobertura?

La cobertura de codigo mide que porcentaje de tu codigo se ejecuta durante
las pruebas. No garantiza que las pruebas sean buenas, pero si indica que
partes del codigo NO estan siendo probadas.

```
  EJEMPLO:

  def dividir(a, b):           # Linea ejecutada en tests?
      if b == 0:               # Si (test con b=0)
          raise ValueError()   # Si (test con b=0)
      return a / b             # Si (test con b=2)

  Cobertura: 4/4 = 100%

  def multiplicar(a, b):       # No probada
      return a * b             # No probada

  Cobertura total: 4/6 = 66.7%
```

### Umbrales comunes

| Nivel | Cobertura | Recomendacion |
|-------|-----------|---------------|
| Bajo | < 50% | Necesita mejora urgente |
| Aceptable | 50-70% | Minimo para proyectos establecidos |
| Bueno | 70-85% | Objetivo razonable |
| Excelente | 85-95% | Proyectos criticos |
| Perfecto | 100% | Rara vez practico ni necesario |

---

## 9. Status badges

Los status badges son imagenes que muestran el estado actual del workflow
en tu README. Ejemplo:

```
![CI](https://github.com/USUARIO/REPO/actions/workflows/ci.yml/badge.svg)
```

### Formato de la URL

```
https://github.com/{OWNER}/{REPO}/actions/workflows/{WORKFLOW_FILE}/badge.svg
```

### Parametros opcionales

| Parametro | Descripcion | Ejemplo |
|-----------|-------------|---------|
| `branch` | Estado de una rama especifica | `?branch=develop` |
| `event` | Estado de un evento especifico | `?event=push` |

### Como obtener el badge

1. Ve a la pestana "Actions"
2. Selecciona el workflow
3. Clic en los tres puntos (...) > "Create status badge"
4. Copia el Markdown generado
5. Pegalo en tu README.md

---

## 10. Branch protection rules

Las branch protection rules permiten exigir que ciertos checks pasen antes
de permitir un merge a ramas protegidas.

### Como configurar

1. Ve a Settings > Branches > Add branch protection rule
2. Branch name pattern: `main`
3. Marca "Require status checks to pass before merging"
4. Busca y selecciona los checks (nombres de tus jobs)
5. Opcionalmente: "Require branches to be up to date before merging"

### Configuracion recomendada para main

| Opcion | Recomendacion | Motivo |
|--------|---------------|--------|
| Require status checks | Si | No se puede hacer merge si CI falla |
| Require branches to be up to date | Si | Asegura que el PR esta actualizado |
| Require pull request reviews | Si (1+) | Al menos una persona revisa |
| Require conversation resolution | Si | Todos los comentarios deben resolverse |
| Restrict who can push | Si | Solo merge via PR |
| Include administrators | Depende | Si = reglas aplican a todos |

```
  SIN PROTECCION:                      CON PROTECCION:

  feature --merge--> main              feature --> PR --> CI --> Review --> main
  (cualquiera,                         (obligatorio pasar CI y revision
   sin verificar)                       antes de merge)
```

---

## 11. Patrones y buenas practicas

### Patron: CI rapido en push, completo en PR

```yaml
# En push a feature branches: solo lint y tests rapidos
on:
  push:
    branches-ignore: [main]

# En PR a main: CI completo
on:
  pull_request:
    branches: [main]
```

### Patron: Cancela ejecuciones anteriores

```yaml
concurrency:
  group: ci-${{ github.ref }}
  cancel-in-progress: true
```

Si haces 3 pushes rapidos, solo se ejecuta el ultimo (los otros se cancelan).

### Patron: Fallar rapido

Ejecuta el job mas rapido primero. Si falla, no pierdas tiempo con el resto.

```yaml
jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - run: npx eslint src/    # 10 segundos

  test:
    needs: lint                  # Solo si lint pasa
    runs-on: ubuntu-latest
    steps:
      - run: npm test            # 2 minutos
```

### Patron: No ejecutar CI en cambios cosmeticos

```yaml
on:
  push:
    paths-ignore:
      - '*.md'
      - 'docs/**'
      - 'LICENSE'
      - '.gitignore'
```

---

## Archivos de ejemplo

| Archivo | Que demuestra |
|---------|---------------|
| `ci_python.yml` | Pipeline completo para Python con pytest y cobertura |
| `ci_node.yml` | Pipeline completo para Node.js con Jest |
| `ci_php.yml` | Pipeline completo para PHP con PHPUnit |
| `ci_lint.yml` | Linting multi-lenguaje (flake8 + ESLint) |
| `ci_matrix.yml` | Matrices multi-version y multi-OS |
| `badge_ejemplo.md` | Ejemplo de como usar status badges |

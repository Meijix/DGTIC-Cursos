# Cheatsheet — Modulo 20: GitHub Actions

## Estructura de un workflow

```yaml
name: CI Pipeline                        # Nombre
on:                                      # Trigger
  push:
    branches: [main]
  pull_request:
    branches: [main]
jobs:                                    # Trabajos
  build:
    runs-on: ubuntu-latest               # Runner
    steps:
      - uses: actions/checkout@v4        # Action
      - run: npm ci                      # Comando shell
      - run: npm test
```

**Ruta:** `.github/workflows/nombre.yml` (con punto, con s en workflows)

## Triggers (on:)

| Trigger | Cuando |
|---------|--------|
| `push: branches: [main]` | Push a main |
| `pull_request: branches: [main]` | PR hacia main |
| `schedule: - cron: '0 6 * * 1'` | Lunes 6:00 UTC |
| `workflow_dispatch:` | Boton manual en GitHub |
| `release: types: [published]` | Publicar release |

Filtros: `paths: ['src/**']` `paths-ignore: ['*.md']` `tags: ['v*']`

Cron: `minuto hora dia-mes mes dia-semana` (UTC). Ej: `0 0 * * *` = diario medianoche.

## Actions comunes

| Action | Uso |
|--------|-----|
| `actions/checkout@v4` | Descargar codigo (obligatorio) |
| `actions/setup-node@v4` | Instalar Node (`with: node-version: '20', cache: 'npm'`) |
| `actions/setup-python@v5` | Instalar Python (`with: python-version: '3.12', cache: 'pip'`) |
| `actions/cache@v4` | Cachear dependencias |
| `actions/upload-artifact@v4` | Subir artefactos |

## Matrix strategy

```yaml
strategy:
  fail-fast: false
  matrix:
    os: [ubuntu-latest, windows-latest]
    node: [18, 20, 22]                  # 2x3 = 6 jobs paralelos
    exclude:
      - os: windows-latest
        node: 18
runs-on: ${{ matrix.os }}
```

## Secretos y variables

```yaml
env:
  GLOBAL: "valor"                        # Nivel workflow/job/step
steps:
  - env:
      TOKEN: ${{ secrets.MI_SECRETO }}   # Secreto (Settings > Secrets > Actions)
    run: curl -H "Authorization: $TOKEN" https://api.example.com
```

Contextos utiles: `github.actor` `github.ref` `github.sha` `github.event_name` `matrix.node` `secrets.X`

## Condicionales (if:)

```yaml
if: github.ref == 'refs/heads/main'           # Solo en main
if: github.event_name == 'push'               # Solo en push
if: startsWith(github.ref, 'refs/tags/v')     # Solo en tags v*
if: always()                                   # Siempre
if: failure()                                  # Solo si fallo
```

## Dependencias entre jobs

```yaml
jobs:
  lint:
    runs-on: ubuntu-latest
    steps: [...]
  test:
    needs: lint                                # Espera a lint
    steps: [...]
  deploy:
    needs: [lint, test]                        # Espera a ambos
    if: github.ref == 'refs/heads/main'
```

## Patrones comunes

```yaml
# Cancelar ejecuciones anteriores (solo importa el ultimo push)
concurrency:
  group: ci-${{ github.ref }}
  cancel-in-progress: true

# CI basico Node.js
name: CI
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: '20', cache: 'npm' }
      - run: npm ci
      - run: npm test

# Status badge en README
# ![CI](https://github.com/USER/REPO/actions/workflows/ci.yml/badge.svg)
```

## Errores comunes

| Error | Solucion |
|-------|----------|
| Workflow no se ejecuta | Ruta debe ser `.github/workflows/` (punto + s) |
| YAML parse error | Usar 2 espacios, nunca tabs |
| Codigo no encontrado | Agregar `actions/checkout@v4` como primer step |
| Secreto en YAML | Usar `${{ secrets.NOMBRE }}` |
| Action se rompe | Fijar con tag (`@v4`) o SHA, no `@main` |
| Matrix gasta muchos min | Usar `exclude`, preferir Linux (1x costo) |
| Schedule no se activa | Solo rama default + requiere actividad en 60 dias |
| Jobs desordenados | Agregar `needs: [job-anterior]` |

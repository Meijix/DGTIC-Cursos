# Ejemplo de Status Badges

Los status badges muestran el estado actual de tus workflows directamente
en el README de tu repositorio.

## Formato de la URL

```
https://github.com/{OWNER}/{REPO}/actions/workflows/{ARCHIVO}/badge.svg
```

## Ejemplos de Markdown

```markdown
<!-- Badge basico -->
![CI](https://github.com/USUARIO/REPO/actions/workflows/ci.yml/badge.svg)

<!-- Badge para una rama especifica -->
![CI - main](https://github.com/USUARIO/REPO/actions/workflows/ci.yml/badge.svg?branch=main)

<!-- Badge para un evento especifico -->
![CI - Push](https://github.com/USUARIO/REPO/actions/workflows/ci.yml/badge.svg?event=push)

<!-- Multiples badges en una linea -->
![CI](https://github.com/USUARIO/REPO/actions/workflows/ci.yml/badge.svg)
![CD](https://github.com/USUARIO/REPO/actions/workflows/cd.yml/badge.svg)
![Lint](https://github.com/USUARIO/REPO/actions/workflows/lint.yml/badge.svg)
```

## Como obtener el badge automaticamente

1. Ve a la pestana **Actions** de tu repositorio
2. Selecciona un workflow en la barra lateral izquierda
3. Haz clic en el boton de tres puntos **...** (arriba a la derecha)
4. Selecciona **Create status badge**
5. Copia el Markdown generado
6. Pegalo en tu `README.md`

## Ejemplo visual en un README

```markdown
# Mi Proyecto

![CI Python](https://github.com/usuario/mi-proyecto/actions/workflows/ci_python.yml/badge.svg)
![CI Node](https://github.com/usuario/mi-proyecto/actions/workflows/ci_node.yml/badge.svg)
![Deploy](https://github.com/usuario/mi-proyecto/actions/workflows/deploy.yml/badge.svg)

## Descripcion
Mi proyecto es una aplicacion web que hace cosas increibles...
```

## Otros badges utiles (no de GitHub Actions)

```markdown
<!-- Badge de cobertura (Codecov) -->
![Coverage](https://codecov.io/gh/USUARIO/REPO/branch/main/graph/badge.svg)

<!-- Badge de version npm -->
![npm version](https://img.shields.io/npm/v/mi-paquete)

<!-- Badge de licencia -->
![License](https://img.shields.io/github/license/USUARIO/REPO)

<!-- Badge personalizado (shields.io) -->
![Custom](https://img.shields.io/badge/estado-estable-green)
```

## Referencia

- [Documentacion oficial: Adding a workflow status badge](https://docs.github.com/es/actions/monitoring-and-troubleshooting-workflows/monitoring-workflows/adding-a-workflow-status-badge)
- [Shields.io - Badges personalizados](https://shields.io/)

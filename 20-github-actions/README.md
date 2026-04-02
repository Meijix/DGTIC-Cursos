# Curso Completo de GitHub Actions

Curso progresivo y practico de **GitHub Actions**: desde los conceptos fundamentales
de CI/CD hasta la creacion de pipelines avanzados con despliegue automatizado,
acciones personalizadas y proyectos integradores.

---

## Requisitos previos

| Requisito | Descripcion |
|-----------|-------------|
| Git basico | Saber hacer commits, branches, push, pull, merge |
| Cuenta de GitHub | Cuenta gratuita es suficiente para todo el curso |
| Algun lenguaje de programacion | Python, JavaScript o PHP (modulos 11-19) |
| Editor de texto | VS Code recomendado (con extension YAML) |
| Terminal / linea de comandos | Bash, Zsh o PowerShell |

---

## Estructura del curso

| # | Seccion | Temas principales | Dificultad | Archivos clave |
|---|---------|-------------------|------------|----------------|
| 01 | Introduccion | CI/CD, terminologia, YAML, comparativa | Principiante | `mi_primer_workflow.yml`, `anatomia_workflow.yml` |
| 02 | Workflows basicos | Eventos, jobs, variables, secretos, cache, matrices | Principiante-Intermedio | `evento_push.yml`, `matriz_estrategia.yml`, `cache_dependencias.yml` |
| 03 | CI y Testing | Pruebas automaticas, linting, cobertura, matrices multi-version | Intermedio | `ci_python.yml`, `ci_node.yml`, `ci_matrix.yml` |
| 04 | CD y Deploy | GitHub Pages, Vercel, Docker, releases, entornos | Intermedio-Avanzado | `deploy_pages.yml`, `docker_build.yml`, `release_tag.yml` |
| 05 | Acciones avanzadas | Acciones custom, workflows reutilizables, seguridad, OIDC | Avanzado | `accion_compuesta.yml`, `workflow_reutilizable.yml`, `seguridad.yml` |
| 06 | Proyectos integradores | Fullstack, paquete Python, monorepo, auto-review | Avanzado | `proyecto_fullstack.yml`, `proyecto_monorepo.yml` |

---

## Mapa de progresion

```
  PRINCIPIANTE                INTERMEDIO                    AVANZADO
  ============                ==========                    ========

  01-introduccion             03-ci-testing                 05-actions-avanzadas
  Que es CI/CD?               Pruebas automaticas           Acciones custom
  Terminologia                Linting y cobertura           Workflows reutilizables
  YAML basico                 Matrices multi-version        Seguridad y OIDC
       |                           |                             |
       v                           v                             v
  02-workflows-basicos        04-cd-deploy                  06-proyectos
  Eventos y triggers          GitHub Pages                  Fullstack pipeline
  Jobs y steps                Docker + registros            Monorepo CI/CD
  Variables y secretos        Releases y tags               Auto-review PRs
  Cache y artefactos          Entornos protegidos           Publicar paquetes

  +-----------+    +------------+    +---------+    +--------+    +----------+    +----------+
  |    01     |--->|     02     |--->|   03    |--->|   04   |--->|    05    |--->|    06    |
  | Conceptos |    | Workflows  |    |  CI /   |    |  CD /  |    | Avanzado |    | Proyectos|
  |  basicos  |    |  basicos   |    | Testing |    | Deploy |    |          |    |          |
  +-----------+    +------------+    +---------+    +--------+    +----------+    +----------+
```

---

## Como usar este curso

### 1. Configuracion inicial

```bash
# Forkea este repositorio en tu cuenta de GitHub
# Luego clonalo localmente:
git clone https://github.com/TU_USUARIO/DGTIC-Cursos.git
cd DGTIC-Cursos/20-github-actions/

# Habilita GitHub Actions en tu fork:
# Ve a Settings > Actions > General > Allow all actions
```

### 2. Estudiar cada seccion

1. Lee el archivo `CONCEPTOS.md` de cada carpeta
2. Examina los archivos `.yml` de ejemplo (estan densamente comentados)
3. Copia un `.yml` a `.github/workflows/` de tu repositorio para probarlo
4. Modifica, experimenta, rompe cosas y aprende

### 3. Probar los workflows

```bash
# Para activar un workflow de ejemplo, copialo a la carpeta correcta:
mkdir -p .github/workflows/
cp 20-github-actions/01-introduccion/mi_primer_workflow.yml .github/workflows/

# Haz commit y push para que GitHub lo ejecute:
git add .github/workflows/mi_primer_workflow.yml
git commit -m "Probar mi primer workflow"
git push
```

---

## Nota importante sobre los archivos .yml

Los archivos `.yml` dentro de cada subcarpeta (`01-introduccion/`, `02-workflows-basicos/`, etc.)
son **ejemplos educativos**. GitHub Actions solo ejecuta workflows que esten en la ruta
`.github/workflows/` de la raiz del repositorio.

Para probar un workflow:
1. Copia el archivo `.yml` deseado a `.github/workflows/`
2. Haz commit y push
3. Ve a la pestana "Actions" de tu repositorio en GitHub

---

## Recursos adicionales

- [Documentacion oficial de GitHub Actions](https://docs.github.com/es/actions)
- [GitHub Actions Marketplace](https://github.com/marketplace?type=actions)
- [Sintaxis de workflows](https://docs.github.com/es/actions/using-workflows/workflow-syntax-for-github-actions)
- [Eventos que activan workflows](https://docs.github.com/es/actions/using-workflows/events-that-trigger-workflows)
- [Variables de entorno predefinidas](https://docs.github.com/es/actions/learn-github-actions/variables)

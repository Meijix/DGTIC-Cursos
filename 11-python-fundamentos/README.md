# Python Fundamentos - Curso Completo

Curso integral de Python desde los fundamentos hasta temas avanzados,
diseñado para estudiantes con conocimientos previos de programación
(ver módulo `00-ejercicios-programacion`).

---

## Mapa de Progresión

```
  NIVEL BÁSICO                NIVEL INTERMEDIO              NIVEL AVANZADO
  ─────────────               ────────────────              ──────────────
  ┌────────────┐   ┌───────────────────┐   ┌──────────────────────────┐
  │ 01-basicos │──▶│ 02-estructuras    │──▶│ 03-funciones-avanzadas   │
  └────────────┘   │    -datos         │   └────────────┬─────────────┘
                   └───────────────────┘                │
                                                        ▼
                   ┌───────────────────┐   ┌──────────────────────────┐
                   │ 05-modulos        │◀──│ 04-poo                   │
                   │    -paquetes      │   └──────────────────────────┘
                   └────────┬──────────┘
                            │
                            ▼
  ┌────────────────────────────────────────────────────────────────────┐
  │                    06-archivos-io                                  │
  └────────────────────────────┬───────────────────────────────────────┘
                               │
                ┌──────────────┴──────────────┐
                ▼                             ▼
  ┌──────────────────────────┐  ┌──────────────────────────┐
  │ 07-decoradores           │  │ 08-manejo-errores        │
  │    -generadores          │  └────────────┬─────────────┘
  └────────────┬─────────────┘               │
               │         ┌───────────────────┘
               ▼         ▼
        ┌─────────────────────┐
        │    09-testing       │
        └─────────┬───────────┘
                  │
                  ▼
        ┌─────────────────────┐
        │   10-proyectos      │
        └─────────────────────┘
```

---

## Contenido del Curso

| # | Sección | Temas principales | Nivel | Archivos clave |
|---|---------|-------------------|-------|----------------|
| 01 | Básicos | Variables, tipos, operadores, strings, condicionales, ciclos | Básico | `tipos_datos.py`, `operadores.py`, `strings.py`, `condicionales.py`, `ciclos.py` |
| 02 | Estructuras de Datos | Listas, tuplas, diccionarios, sets, comprehensions | Básico-Intermedio | `listas.py`, `tuplas.py`, `diccionarios.py`, `sets.py`, `comprehensions.py` |
| 03 | Funciones Avanzadas | Closures, lambdas, map/filter/reduce, *args/**kwargs, type hints | Intermedio | `funciones_orden_superior.py`, `lambdas.py`, `args_kwargs.py`, `type_hints.py` |
| 04 | POO | Clases, herencia, polimorfismo, magic methods, dataclasses | Intermedio | `clases_basicas.py`, `herencia.py`, `polimorfismo.py`, `magic_methods.py`, `dataclasses_ejemplo.py` |
| 05 | Módulos y Paquetes | import, __init__.py, pip, venv, bibliotecas populares | Intermedio | `mi_modulo.py`, `uso_modulos.py`, `ejemplo_paquete/` |
| 06 | Archivos e I/O | open(), read/write, context managers, CSV, JSON, pathlib | Intermedio | `lectura_escritura.py`, `csv_ejemplo.py`, `json_ejemplo.py`, `pathlib_ejemplo.py` |
| 07 | Decoradores y Generadores | Decorators, @wraps, generators, yield, iteradores | Avanzado | `decoradores.py`, `generadores.py`, `iteradores.py`, `decoradores_practicos.py` |
| 08 | Manejo de Errores | Excepciones, custom exceptions, logging, context managers | Avanzado | `excepciones.py`, `excepciones_custom.py`, `logging_ejemplo.py`, `context_managers.py` |
| 09 | Testing | unittest, pytest, mocking, coverage, TDD | Avanzado | `test_basico.py`, `test_pytest.py`, `test_fixtures.py`, `test_mocking.py`, `calculadora.py` |
| 10 | Proyectos Integradores | Gestor de tareas, analizador de texto, cliente API | Integración | `gestor_tareas.py`, `analizador_texto.py`, `api_clima.py` |

---

## Prerrequisitos

- Haber completado el módulo `00-ejercicios-programacion` (lógica de programación)
- Conocimientos básicos de terminal / línea de comandos
- Ganas de practicar: **la programación se aprende programando**

---

## Configuración del Entorno

### 1. Instalar Python 3

```bash
# macOS (con Homebrew)
brew install python3

# Ubuntu / Debian
sudo apt update && sudo apt install python3 python3-pip python3-venv

# Verificar instalación
python3 --version   # Debe ser 3.10 o superior
```

### 2. Crear un entorno virtual

```bash
# Crear el entorno
python3 -m venv .venv

# Activar (macOS / Linux)
source .venv/bin/activate

# Activar (Windows)
.venv\Scripts\activate

# Verificar que estás dentro del entorno
which python   # Debe apuntar a .venv/bin/python
```

### 3. Instalar dependencias (para secciones avanzadas)

```bash
pip install pytest pytest-cov requests
```

### 4. Ejecutar los ejemplos

```bash
# Ejecutar cualquier archivo de ejemplo
python 01-basicos/tipos_datos.py

# Ejecutar tests (sección 09)
pytest 09-testing/ -v
```

---

## Convenciones de los Archivos

- **CONCEPTOS.md** — Teoría, diagramas ASCII, tablas y ejercicios propuestos
- **archivos .py** — Ejemplos ejecutables con comentarios educativos extensos
- Cada archivo `.py` se puede ejecutar de forma independiente
- Los comentarios explican el *por qué*, no solo el *qué*

---

## Licencia

Material educativo de uso libre para fines académicos.
DGTIC — UNAM.

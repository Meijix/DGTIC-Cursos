# 05 — Módulos y Paquetes

## Índice

1. [Módulos](#módulos)
2. [Importaciones](#importaciones)
3. [Paquetes](#paquetes)
4. [El Sistema de Import](#el-sistema-de-import)
5. [Entornos Virtuales](#entornos-virtuales)
6. [pip y Gestión de Dependencias](#pip-y-gestión-de-dependencias)
7. [Bibliotecas Populares](#bibliotecas-populares)
8. [Errores Comunes](#errores-comunes)
9. [Ejercicios](#ejercicios)

---

## Módulos

Un **módulo** es simplemente un archivo `.py`. Permite organizar y reutilizar código.

```
  mi_proyecto/
  ├── main.py            ← Punto de entrada
  ├── utils.py           ← Módulo de utilidades
  └── config.py          ← Módulo de configuración
```

### Anatomía de un módulo

```python
# utils.py

"""Módulo de utilidades — docstring del módulo."""

# Variables del módulo
VERSION = "1.0"

# Funciones
def limpiar_texto(texto):
    return texto.strip().lower()

# Clases
class Formateador:
    pass

# Código que solo se ejecuta si el archivo se ejecuta directamente
if __name__ == "__main__":
    print("Ejecutando utils.py directamente")
    print(limpiar_texto("  HOLA  "))
```

### `__name__` y `__main__`

| Situación | `__name__` vale |
|-----------|-----------------|
| `python utils.py` (ejecución directa) | `"__main__"` |
| `import utils` (importado) | `"utils"` |

Este patrón permite que un archivo sirva como módulo importable
Y como script ejecutable.

---

## Importaciones

### Formas de importar

```python
# 1. Importar el módulo completo
import math
math.sqrt(16)

# 2. Importar con alias
import numpy as np
np.array([1, 2, 3])

# 3. Importar nombres específicos
from math import sqrt, pi
sqrt(16)

# 4. Importar con alias específico
from collections import OrderedDict as OD

# 5. Importar todo (NO recomendado)
from math import *
```

### Importaciones relativas (dentro de paquetes)

```python
# Dentro de un paquete:
from . import modulo_hermano          # Mismo nivel
from .modulo_hermano import funcion   # Nombre específico
from .. import modulo_padre           # Nivel superior
from ..otro_paquete import algo       # Otro paquete del padre
```

---

## Paquetes

Un **paquete** es un directorio con un archivo `__init__.py`.

```
  mi_paquete/
  ├── __init__.py         ← Hace del directorio un paquete
  ├── modulo_a.py
  ├── modulo_b.py
  └── subpaquete/
      ├── __init__.py
      └── modulo_c.py
```

### `__init__.py`

Se ejecuta cuando se importa el paquete. Puede:
- Estar vacío (solo marca el directorio como paquete)
- Definir `__all__` para controlar `from paquete import *`
- Re-exportar nombres para una API más limpia

```python
# mi_paquete/__init__.py
from .modulo_a import funcion_principal
from .modulo_b import ClaseImportante

__all__ = ["funcion_principal", "ClaseImportante"]
```

---

## El Sistema de Import

### Búsqueda de módulos (`sys.path`)

Python busca módulos en este orden:
1. Directorio del script que se ejecuta
2. `PYTHONPATH` (variable de entorno)
3. Directorios de instalación (site-packages)

```python
import sys
for ruta in sys.path:
    print(ruta)
```

### Cache de módulos

- Python cachea módulos importados en `sys.modules`
- Un módulo se ejecuta solo la primera vez que se importa
- Importaciones subsecuentes usan la versión cacheada

---

## Entornos Virtuales

Un entorno virtual es una copia aislada de Python con sus propias
dependencias. Evita conflictos entre proyectos.

```
  Sistema
  ├── Python 3.12
  │
  ├── Proyecto A/
  │   └── .venv/           ← requests 2.31
  │       ├── bin/python
  │       └── lib/
  │
  └── Proyecto B/
      └── .venv/           ← requests 2.28 (otra versión)
          ├── bin/python
          └── lib/
```

### Comandos esenciales

```bash
# Crear entorno virtual
python3 -m venv .venv

# Activar
source .venv/bin/activate      # macOS/Linux
.venv\Scripts\activate         # Windows

# Verificar
which python                   # .venv/bin/python
pip list                       # Solo paquetes del entorno

# Desactivar
deactivate
```

---

## pip y Gestión de Dependencias

```bash
# Instalar paquete
pip install requests

# Instalar versión específica
pip install requests==2.31.0

# Instalar desde requirements.txt
pip install -r requirements.txt

# Generar requirements.txt
pip freeze > requirements.txt

# Buscar paquete
pip search nombre      # (puede no estar disponible)

# Información de un paquete
pip show requests

# Actualizar
pip install --upgrade requests

# Desinstalar
pip uninstall requests
```

### requirements.txt

```
requests==2.31.0
pytest>=7.0
flask~=3.0          # Compatible con 3.x
python-dotenv       # Última versión
```

---

## Bibliotecas Populares

| Biblioteca | Uso | Instalación |
|------------|-----|-------------|
| `requests` | HTTP / APIs | `pip install requests` |
| `flask` | Web (micro) | `pip install flask` |
| `django` | Web (full) | `pip install django` |
| `pytest` | Testing | `pip install pytest` |
| `numpy` | Cálculo numérico | `pip install numpy` |
| `pandas` | Análisis de datos | `pip install pandas` |
| `matplotlib` | Gráficas | `pip install matplotlib` |
| `sqlalchemy` | Base de datos | `pip install sqlalchemy` |
| `pydantic` | Validación | `pip install pydantic` |
| `click` | CLI | `pip install click` |

---

## Errores Comunes

| Error | Causa | Solución |
|-------|-------|----------|
| `ModuleNotFoundError` | Módulo no instalado o no en sys.path | `pip install` o verificar sys.path |
| `ImportError` | Nombre no existe en el módulo | Verificar nombre exacto |
| Importación circular | A importa B y B importa A | Reestructurar, importar dentro de función |
| `from x import *` | Contamina namespace | Importar nombres específicos |
| No activar venv | Instalar en Python global | `source .venv/bin/activate` |

---

## Ejercicios

### Nivel 1
1. Crea un módulo `matematicas.py` con funciones para factorial, fibonacci y es_primo. Impórtalo desde otro archivo.
2. Agrega `if __name__ == "__main__"` a tu módulo para que ejecute tests cuando se corra directamente.

### Nivel 2
3. Crea un paquete `utilidades/` con módulos `texto.py`, `numeros.py` y un `__init__.py` que re-exporte las funciones principales.
4. Crea un `requirements.txt` para un proyecto que use requests, pytest y python-dotenv.

### Nivel 3
5. Implementa un sistema de plugins donde cada plugin es un módulo que se importa dinámicamente con `importlib`.
6. Crea un paquete con importaciones relativas entre módulos hermanos.

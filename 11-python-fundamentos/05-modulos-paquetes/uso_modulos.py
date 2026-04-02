"""
Uso de Módulos en Python
==========================
Demuestra las diferentes formas de importar y usar módulos,
tanto de la biblioteca estándar como módulos propios.

Ejecuta este archivo:
    python uso_modulos.py
"""

# ============================================================
# 1. IMPORTAR MÓDULOS DE LA BIBLIOTECA ESTÁNDAR
# ============================================================

print("=== MÓDULOS DE LA BIBLIOTECA ESTÁNDAR ===\n")

# --- Forma 1: import módulo ---
import math
print(f"math.sqrt(16) = {math.sqrt(16)}")
print(f"math.pi = {math.pi:.10f}")

# --- Forma 2: from módulo import nombre ---
from datetime import datetime, timedelta
ahora = datetime.now()
print(f"\nAhora: {ahora.strftime('%Y-%m-%d %H:%M')}")
manana = ahora + timedelta(days=1)
print(f"Mañana: {manana.strftime('%Y-%m-%d %H:%M')}")

# --- Forma 3: import módulo as alias ---
import json as j
datos = {"nombre": "Ana", "edad": 25}
print(f"\nJSON: {j.dumps(datos, ensure_ascii=False)}")

# --- Forma 4: from módulo import nombre as alias ---
from collections import Counter as Contador
palabras = "el gato y el perro y el pájaro".split()
freq = Contador(palabras)
print(f"Frecuencias: {dict(freq)}")

# ============================================================
# 2. MÓDULOS ESTÁNDAR ÚTILES
# ============================================================

print("\n=== MÓDULOS ESTÁNDAR ÚTILES ===\n")

# --- os: sistema operativo ---
import os
print(f"Directorio actual: {os.getcwd()}")
print(f"Variables de entorno HOME: {os.environ.get('HOME', 'No definida')}")

# --- sys: sistema Python ---
import sys
print(f"\nVersión de Python: {sys.version}")
print(f"Plataforma: {sys.platform}")
print(f"Rutas de búsqueda (primeras 3): {sys.path[:3]}")

# --- random ---
import random
random.seed(42)
print(f"\nRandom int: {random.randint(1, 100)}")
print(f"Random choice: {random.choice(['rojo', 'azul', 'verde'])}")
print(f"Random sample: {random.sample(range(1, 50), 5)}")

# --- itertools ---
from itertools import chain, product, islice
print(f"\nchain: {list(chain([1,2], [3,4], [5,6]))}")
print(f"product: {list(product('AB', '12'))}")

# --- functools ---
from functools import reduce, partial
suma = reduce(lambda a, b: a + b, [1, 2, 3, 4, 5])
print(f"\nreduce(+): {suma}")

doble = partial(pow, 2)  # pow(2, x)
print(f"partial(pow, 2)(10): {doble(10)}")

# --- collections ---
from collections import defaultdict, namedtuple, deque
dd = defaultdict(list)
dd["frutas"].append("manzana")
dd["frutas"].append("pera")
print(f"\ndefaultdict: {dict(dd)}")

Punto = namedtuple("Punto", ["x", "y"])
p = Punto(3, 4)
print(f"namedtuple: {p}, x={p.x}")

# ============================================================
# 3. IMPORTAR NUESTRO MÓDULO PROPIO
# ============================================================

print("\n=== MÓDULO PROPIO (mi_modulo) ===\n")

# Importar funciones de nuestro módulo
# NOTA: Esto funciona si ejecutas desde el directorio 05-modulos-paquetes/
# o si ese directorio está en sys.path
try:
    from mi_modulo import factorial, fibonacci, es_primo, Estadisticas

    print(f"5! = {factorial(5)}")
    print(f"Fibonacci(8): {fibonacci(8)}")
    print(f"¿17 es primo? {es_primo(17)}")

    stats = Estadisticas([10, 20, 30, 40, 50])
    print(f"Estadísticas: {stats.resumen()}")

except ImportError:
    print("No se pudo importar mi_modulo.")
    print("Ejecuta desde el directorio 05-modulos-paquetes/")

# ============================================================
# 4. IMPORTACIÓN DINÁMICA
# ============================================================

print("\n=== IMPORTACIÓN DINÁMICA ===\n")

import importlib

# Importar un módulo por nombre (string)
mod = importlib.import_module("math")
print(f"Import dinámico de math: sqrt(25) = {mod.sqrt(25)}")

# Útil para sistemas de plugins
modulos_a_cargar = ["json", "os.path", "collections"]
for nombre in modulos_a_cargar:
    m = importlib.import_module(nombre)
    print(f"  Cargado: {nombre} — {type(m)}")

# ============================================================
# 5. INSPECCIONAR MÓDULOS
# ============================================================

print("\n=== INSPECCIÓN DE MÓDULOS ===\n")

# dir() — lista todos los nombres de un módulo
print("Nombres en math (primeros 10):")
for nombre in dir(math)[:10]:
    print(f"  {nombre}")

# help() — documentación (descomenta para ver)
# help(math.sqrt)

# __doc__ — docstring del módulo
print(f"\nDocstring de json: {j.__doc__[:80]}...")

# __file__ — ubicación del archivo
print(f"Archivo de json: {j.__file__}")

# __name__ — nombre del módulo
print(f"Nombre de este módulo: {__name__}")  # __main__ (porque se ejecuta directamente)

# ============================================================
# 6. sys.modules — CACHÉ DE MÓDULOS
# ============================================================

print("\n=== CACHÉ DE MÓDULOS ===\n")

# Python cachea todos los módulos importados
modulos_cargados = list(sys.modules.keys())
print(f"Módulos cargados: {len(modulos_cargados)}")
print(f"Primeros 10: {modulos_cargados[:10]}")

# Verificar si un módulo ya está cargado
print(f"\n'math' cargado: {'math' in sys.modules}")
print(f"'numpy' cargado: {'numpy' in sys.modules}")

# ============================================================
# 7. EJEMPLO INTEGRADOR
# ============================================================

print("\n=== EJEMPLO: HERRAMIENTA DE ANÁLISIS ===\n")

from collections import Counter
from datetime import datetime
import os

def analizar_directorio(ruta="."):
    """Analiza los archivos en un directorio."""
    archivos = os.listdir(ruta)

    # Contar por extensión
    extensiones = Counter()
    for archivo in archivos:
        _, ext = os.path.splitext(archivo)
        extensiones[ext or "(sin ext)"] += 1

    print(f"Directorio: {os.path.abspath(ruta)}")
    print(f"Total archivos/carpetas: {len(archivos)}")
    print(f"\nPor extensión:")
    for ext, count in extensiones.most_common():
        print(f"  {ext:12s}: {count}")

    # Archivos Python
    py_files = [f for f in archivos if f.endswith(".py")]
    if py_files:
        print(f"\nArchivos Python ({len(py_files)}):")
        for f in sorted(py_files):
            ruta_completa = os.path.join(ruta, f)
            tamano = os.path.getsize(ruta_completa)
            print(f"  {f:30s} ({tamano:,} bytes)")


analizar_directorio()

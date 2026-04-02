"""
Context Managers en Python — La Sentencia 'with'
===================================================
Los context managers garantizan que los recursos se adquieran
y liberen correctamente, incluso si ocurre un error. Son la forma
pythonica de manejar setup/teardown de recursos.

Ejecuta este archivo:
    python context_managers.py
"""

import os
import tempfile
import time

# ============================================================
# 1. EL PROBLEMA QUE RESUELVEN
# ============================================================

print("=== El problema ===\n")

# SIN context manager — error-prone:
# Si ocurre un error ANTES de close(), el archivo queda abierto.
ruta_temp = os.path.join(tempfile.gettempdir(), "cm_ejemplo.txt")

archivo = open(ruta_temp, "w")
try:
    archivo.write("datos importantes\n")
finally:
    archivo.close()    # Debemos recordar cerrar SIEMPRE
    print("Archivo cerrado manualmente con try/finally")

# CON context manager — limpio y seguro:
with open(ruta_temp, "w") as archivo:
    archivo.write("datos importantes\n")
    # El archivo se cierra AUTOMATICAMENTE al salir del with,
    # incluso si ocurre una excepcion dentro del bloque.
print("Archivo cerrado automaticamente con 'with'\n")

# ============================================================
# 2. PROTOCOLO: __enter__ y __exit__
# ============================================================

# Un context manager es cualquier objeto que implemente:
#   __enter__() — se ejecuta al entrar al 'with' (setup)
#   __exit__()  — se ejecuta al salir del 'with' (teardown)

class MiContextManager:
    """
    Context manager basico que demuestra el protocolo.
    """

    def __init__(self, nombre):
        self.nombre = nombre
        print(f"  __init__: creando '{nombre}'")

    def __enter__(self):
        """Se ejecuta al inicio del 'with'. Lo que retorna se asigna con 'as'."""
        print(f"  __enter__: abriendo recurso '{self.nombre}'")
        return self   # Este objeto se asigna a la variable 'as'

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Se ejecuta SIEMPRE al salir del 'with'.

        Parametros (info sobre la excepcion, si hubo):
            exc_type: tipo de excepcion (o None)
            exc_val:  valor de la excepcion (o None)
            exc_tb:   traceback (o None)

        Retorna:
            True  -> suprime la excepcion (no se propaga)
            False -> deja que la excepcion se propague
        """
        if exc_type is not None:
            print(f"  __exit__: hubo error — {exc_type.__name__}: {exc_val}")
        else:
            print(f"  __exit__: sin errores")
        print(f"  __exit__: cerrando recurso '{self.nombre}'")
        return False   # No suprimir excepciones

print("=== Protocolo __enter__ / __exit__ ===\n")

# Caso sin error
with MiContextManager("recurso_A") as cm:
    print(f"  Dentro del with: usando '{cm.nombre}'")

print()

# Caso con error
try:
    with MiContextManager("recurso_B") as cm:
        print(f"  Dentro del with: usando '{cm.nombre}'")
        raise ValueError("Algo salio mal")
except ValueError:
    print("  Excepcion capturada fuera del with")

# ============================================================
# 3. EJEMPLO PRACTICO: CRONOMETRO
# ============================================================

class Cronometro:
    """Context manager que mide el tiempo de ejecucion."""

    def __init__(self, etiqueta="Bloque"):
        self.etiqueta = etiqueta
        self.duracion = 0

    def __enter__(self):
        self.inicio = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.duracion = time.perf_counter() - self.inicio
        print(f"  [{self.etiqueta}] Duracion: {self.duracion:.6f} segundos")
        return False

print("\n=== Cronometro con context manager ===\n")

with Cronometro("Suma de cuadrados") as t:
    resultado = sum(x ** 2 for x in range(1_000_000))

print(f"  Resultado: {resultado}")
print(f"  Duracion accesible despues del with: {t.duracion:.6f}s")

# ============================================================
# 4. EJEMPLO PRACTICO: DIRECTORIO TEMPORAL
# ============================================================

class DirectorioTemporal:
    """
    Crea un directorio temporal que se elimina automaticamente
    al salir del bloque 'with'.
    """

    def __init__(self, prefijo="tmp_"):
        self.prefijo = prefijo
        self.ruta = None

    def __enter__(self):
        self.ruta = tempfile.mkdtemp(prefix=self.prefijo)
        print(f"  Creado directorio temporal: {self.ruta}")
        return self.ruta

    def __exit__(self, exc_type, exc_val, exc_tb):
        import shutil
        if self.ruta and os.path.exists(self.ruta):
            shutil.rmtree(self.ruta)
            print(f"  Eliminado directorio temporal: {self.ruta}")
        return False

print("\n=== Directorio temporal ===\n")

with DirectorioTemporal("python_demo_") as ruta:
    # Crear un archivo dentro del directorio temporal
    archivo = os.path.join(ruta, "datos.txt")
    with open(archivo, "w") as f:
        f.write("Datos temporales")
    print(f"  Archivo creado: {archivo}")
    print(f"  Existe: {os.path.exists(archivo)}")

# El directorio y su contenido ya no existen
print(f"  Despues del with, directorio existe: {os.path.exists(ruta)}")

# ============================================================
# 5. contextlib.contextmanager — FORMA RAPIDA CON GENERADOR
# ============================================================

from contextlib import contextmanager

@contextmanager
def abrir_y_cerrar(nombre):
    """
    Context manager usando un generador.
    Todo ANTES de yield es __enter__.
    Todo DESPUES de yield es __exit__.
    Lo que se hace yield es lo que se asigna con 'as'.
    """
    print(f"  Abriendo {nombre}")
    recurso = {"nombre": nombre, "datos": []}
    try:
        yield recurso        # <-- aqui se ejecuta el bloque 'with'
    finally:
        print(f"  Cerrando {nombre} (tenia {len(recurso['datos'])} datos)")

print("\n=== contextlib.contextmanager ===\n")

with abrir_y_cerrar("base_datos") as db:
    db["datos"].append("registro 1")
    db["datos"].append("registro 2")
    print(f"  Trabajando con: {db}")

# ============================================================
# 6. SUPRIMIR EXCEPCIONES
# ============================================================

from contextlib import suppress

print("\n=== suppress (ignorar excepciones especificas) ===\n")

# En vez de:
#   try:
#       os.remove("archivo.txt")
#   except FileNotFoundError:
#       pass

# Puedes usar:
with suppress(FileNotFoundError):
    os.remove("/tmp/archivo_que_no_existe.txt")
    print("  Esto no se ejecuta si el archivo no existe")

print("  El programa continua sin error")

# ============================================================
# 7. MULTIPLES CONTEXT MANAGERS
# ============================================================

print("\n=== Multiples context managers ===\n")

ruta_a = os.path.join(tempfile.gettempdir(), "cm_a.txt")
ruta_b = os.path.join(tempfile.gettempdir(), "cm_b.txt")

# Se pueden combinar multiples 'with' en una linea:
with open(ruta_a, "w") as fa, open(ruta_b, "w") as fb:
    fa.write("Datos en archivo A")
    fb.write("Datos en archivo B")
    print("  Ambos archivos abiertos simultaneamente")

print("  Ambos archivos cerrados automaticamente")

# Limpiar
os.remove(ruta_a)
os.remove(ruta_b)

# ============================================================
# RESUMEN
# ============================================================

print("""
=== RESUMEN DE CONTEXT MANAGERS ===

1. 'with' garantiza setup/teardown incluso si hay errores.
2. Protocolo: __enter__() y __exit__(exc_type, exc_val, exc_tb).
3. __exit__ retorna True para suprimir excepciones, False para propagarlas.
4. @contextmanager simplifica la creacion usando generadores.
5. Usos comunes: archivos, locks, conexiones, temporizadores.
6. contextlib.suppress() ignora excepciones especificas.

Regla: si un recurso necesita cerrarse/liberarse, usa 'with'.
""")

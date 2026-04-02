"""
Lectura y Escritura de Archivos en Python
============================================
Operaciones fundamentales de I/O con archivos de texto
usando open(), context managers y buenas prácticas.

Ejecuta este archivo:
    python lectura_escritura.py
"""

import os
import tempfile

# Usamos un directorio temporal para no dejar archivos basura
TEMP_DIR = tempfile.mkdtemp(prefix="python_io_")
print(f"Directorio temporal: {TEMP_DIR}\n")

# ============================================================
# 1. ESCRITURA BÁSICA
# ============================================================

print("=== ESCRITURA ===\n")

ruta = os.path.join(TEMP_DIR, "ejemplo.txt")

# Modo "w" — crea o SOBRESCRIBE
with open(ruta, "w", encoding="utf-8") as f:
    f.write("Primera línea\n")
    f.write("Segunda línea\n")
    f.write("Tercera línea con acentos: café, niño, señor\n")
    # write() NO agrega \n automáticamente

print(f"Archivo escrito: {ruta}")

# Modo "a" — agrega al final (no sobrescribe)
with open(ruta, "a", encoding="utf-8") as f:
    f.write("Cuarta línea (agregada con 'a')\n")
    f.write("Quinta línea\n")

# Modo "x" — creación exclusiva (error si ya existe)
ruta_nuevo = os.path.join(TEMP_DIR, "nuevo.txt")
try:
    with open(ruta_nuevo, "x", encoding="utf-8") as f:
        f.write("Archivo creado exclusivamente\n")
    print(f"Creado con modo 'x': {ruta_nuevo}")
except FileExistsError:
    print("El archivo ya existía")

# writelines() — escribe una lista de strings
ruta_lineas = os.path.join(TEMP_DIR, "lineas.txt")
lineas = ["Línea A\n", "Línea B\n", "Línea C\n"]
with open(ruta_lineas, "w", encoding="utf-8") as f:
    f.writelines(lineas)
    # NOTA: writelines NO agrega \n entre elementos

# print() con file= — alternativa cómoda
ruta_print = os.path.join(TEMP_DIR, "con_print.txt")
with open(ruta_print, "w", encoding="utf-8") as f:
    print("Hola desde print", file=f)
    print("Otra línea", file=f)
    print(f"Números: {1 + 2 + 3}", file=f)

# ============================================================
# 2. LECTURA BÁSICA
# ============================================================

print("\n=== LECTURA ===\n")

# --- read() — todo el contenido de una vez ---
with open(ruta, "r", encoding="utf-8") as f:
    contenido = f.read()
print("read() completo:")
print(contenido)

# --- readline() — una línea a la vez ---
print("readline():")
with open(ruta, "r", encoding="utf-8") as f:
    primera = f.readline()
    segunda = f.readline()
    print(f"  Línea 1: {primera.strip()!r}")
    print(f"  Línea 2: {segunda.strip()!r}")

# --- readlines() — lista de todas las líneas ---
with open(ruta, "r", encoding="utf-8") as f:
    todas = f.readlines()
print(f"\nreadlines(): {len(todas)} líneas")
for i, linea in enumerate(todas):
    print(f"  [{i}] {linea.strip()!r}")

# --- Iterar directamente (más eficiente en memoria) ---
print("\nIteración directa (más eficiente):")
with open(ruta, "r", encoding="utf-8") as f:
    for num, linea in enumerate(f, start=1):
        print(f"  {num:3d} | {linea.rstrip()}")

# ============================================================
# 3. LECTURA PARCIAL
# ============================================================

print("\n=== LECTURA PARCIAL ===\n")

with open(ruta, "r", encoding="utf-8") as f:
    # Leer solo N caracteres
    primeros_20 = f.read(20)
    print(f"Primeros 20 chars: {primeros_20!r}")

    # tell() — posición actual del cursor
    print(f"Posición actual: {f.tell()}")

    # seek() — mover el cursor
    f.seek(0)  # Volver al inicio
    print(f"Después de seek(0): {f.read(10)!r}")

# ============================================================
# 4. ARCHIVOS BINARIOS
# ============================================================

print("\n=== ARCHIVOS BINARIOS ===\n")

ruta_bin = os.path.join(TEMP_DIR, "datos.bin")

# Escribir bytes
with open(ruta_bin, "wb") as f:
    f.write(b"\x00\x01\x02\x03\x04")
    f.write(bytes([255, 128, 64, 32, 16]))
    f.write("Texto como bytes".encode("utf-8"))

# Leer bytes
with open(ruta_bin, "rb") as f:
    datos = f.read()
    print(f"Bytes leídos: {datos}")
    print(f"Longitud: {len(datos)} bytes")
    print(f"Primeros 5 como lista: {list(datos[:5])}")

# ============================================================
# 5. MANEJO DE ERRORES
# ============================================================

print("\n=== MANEJO DE ERRORES ===\n")

# Archivo que no existe
try:
    with open("no_existe.txt", "r") as f:
        f.read()
except FileNotFoundError as e:
    print(f"FileNotFoundError: {e}")

# Verificar antes de abrir
ruta_test = os.path.join(TEMP_DIR, "quizas.txt")
if os.path.exists(ruta_test):
    print("El archivo existe")
else:
    print(f"El archivo no existe: {ruta_test}")

# Encoding incorrecto
ruta_utf8 = os.path.join(TEMP_DIR, "utf8.txt")
with open(ruta_utf8, "w", encoding="utf-8") as f:
    f.write("Café, niño, señor")

try:
    with open(ruta_utf8, "r", encoding="ascii") as f:
        f.read()
except UnicodeDecodeError as e:
    print(f"UnicodeDecodeError: {e}")

# ============================================================
# 6. EJEMPLO INTEGRADOR: PROCESADOR DE TEXTO
# ============================================================

print("\n=== EJEMPLO: PROCESADOR DE TEXTO ===\n")

# Crear un archivo de ejemplo
ruta_texto = os.path.join(TEMP_DIR, "texto_ejemplo.txt")
with open(ruta_texto, "w", encoding="utf-8") as f:
    f.write("""Python es un lenguaje de programación interpretado.
Es multiparadigma y de tipado dinámico.
Python fue creado por Guido van Rossum.
El nombre Python viene de Monty Python.
Python es uno de los lenguajes más populares del mundo.
""")


def analizar_archivo(ruta):
    """Analiza un archivo de texto y muestra estadísticas."""
    with open(ruta, "r", encoding="utf-8") as f:
        lineas = f.readlines()

    total_lineas = len(lineas)
    lineas_no_vacias = sum(1 for l in lineas if l.strip())
    palabras = []
    caracteres = 0

    for linea in lineas:
        limpia = linea.strip()
        if limpia:
            palabras.extend(limpia.split())
            caracteres += len(limpia)

    # Frecuencia de palabras
    from collections import Counter
    frecuencia = Counter(p.lower().strip(".,;:!?") for p in palabras)

    print(f"Archivo: {os.path.basename(ruta)}")
    print(f"  Líneas totales:     {total_lineas}")
    print(f"  Líneas no vacías:   {lineas_no_vacias}")
    print(f"  Palabras:           {len(palabras)}")
    print(f"  Caracteres:         {caracteres}")
    print(f"  Promedio palabras/línea: {len(palabras)/lineas_no_vacias:.1f}")
    print(f"  Palabras únicas:    {len(frecuencia)}")
    print(f"  Top 5 palabras:")
    for palabra, cuenta in frecuencia.most_common(5):
        print(f"    '{palabra}': {cuenta}")


analizar_archivo(ruta_texto)

# ============================================================
# 7. LIMPIEZA
# ============================================================

print(f"\nArchivos creados en: {TEMP_DIR}")
print("(Se eliminarán automáticamente al reiniciar el sistema)")

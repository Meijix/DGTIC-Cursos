"""
Strings (Cadenas de Texto) en Python
=====================================
Las cadenas son secuencias INMUTABLES de caracteres Unicode.
Son uno de los tipos más usados en cualquier programa.

Ejecuta este archivo:
    python strings.py
"""

# ============================================================
# 1. CREACIÓN DE STRINGS
# ============================================================

print("=== CREACIÓN DE STRINGS ===\n")

# Cuatro formas de crear strings:
simple = 'comillas simples'
doble = "comillas dobles"
triple_simple = '''triple
simple'''
triple_doble = """triple
doble — ideal para docstrings"""

# Raw strings — las barras invertidas NO se interpretan como escapes
normal = "línea1\nlínea2"      # \n se convierte en salto de línea
raw = r"línea1\nlínea2"         # \n se queda como texto literal
print(f"Normal: {normal}")
print(f"Raw:    {raw}")

# Byte strings — para datos binarios
bytes_str = b"solo ASCII"
print(f"\nByte string: {bytes_str}, tipo: {type(bytes_str)}")

# ============================================================
# 2. INDEXACIÓN Y SLICING
# ============================================================

print("\n=== INDEXACIÓN Y SLICING ===\n")

texto = "Python"

# Visualización de índices:
# Carácter:   P    y    t    h    o    n
# Positivo:   0    1    2    3    4    5
# Negativo:  -6   -5   -4   -3   -2   -1

print(f"texto = '{texto}'")
print(f"texto[0]  = '{texto[0]}'")     # P — primer carácter
print(f"texto[-1] = '{texto[-1]}'")    # n — último carácter
print(f"texto[2]  = '{texto[2]}'")     # t

# Slicing: texto[inicio:fin:paso]
# El índice 'fin' NO se incluye
print(f"\ntexto[0:3]  = '{texto[0:3]}'")   # Pyt
print(f"texto[2:5]  = '{texto[2:5]}'")     # tho
print(f"texto[:3]   = '{texto[:3]}'")      # Pyt (desde el inicio)
print(f"texto[3:]   = '{texto[3:]}'")      # hon (hasta el final)
print(f"texto[::2]  = '{texto[::2]}'")     # Pto (cada 2 caracteres)
print(f"texto[::-1] = '{texto[::-1]}'")    # nohtyP (invertida)
print(f"texto[-3:]  = '{texto[-3:]}'")     # hon (últimos 3)

# ============================================================
# 3. INMUTABILIDAD
# ============================================================

print("\n=== INMUTABILIDAD ===\n")

# Los strings NO se pueden modificar en su lugar
texto = "Hola"
# texto[0] = "h"  # TypeError: 'str' object does not support item assignment

# Para "modificar", creas un string NUEVO:
texto_nuevo = "h" + texto[1:]
print(f"Original: '{texto}' → Nuevo: '{texto_nuevo}'")

# ============================================================
# 4. MÉTODOS DE STRING
# ============================================================

print("\n=== MÉTODOS DE STRING ===\n")

s = "  Hola Mundo Python  "

# --- Transformación de caso ---
print(f"'{s.strip()}'.upper()    = '{s.strip().upper()}'")
print(f"'{s.strip()}'.lower()    = '{s.strip().lower()}'")
print(f"'{s.strip()}'.title()    = '{s.strip().title()}'")
print(f"'{s.strip()}'.capitalize()= '{s.strip().capitalize()}'")
print(f"'{s.strip()}'.swapcase() = '{s.strip().swapcase()}'")

# --- Limpieza de espacios ---
print(f"\n'{s}'.strip()  = '{s.strip()}'")    # Ambos lados
print(f"'{s}'.lstrip() = '{s.lstrip()}'")     # Solo izquierda
print(f"'{s}'.rstrip() = '{s.rstrip()}'")     # Solo derecha

# strip también acepta caracteres específicos
url = "///ruta/al/recurso///"
print(f"'{url}'.strip('/') = '{url.strip('/')}'")

# --- Búsqueda ---
frase = "La programación es el arte de pensar en abstracto"
print(f"\n'{frase}'")
print(f".find('arte')     = {frase.find('arte')}")      # 28 (posición)
print(f".find('xyz')      = {frase.find('xyz')}")       # -1 (no encontrado)
print(f".index('arte')    = {frase.index('arte')}")     # 28
# .index() lanza ValueError si no encuentra, .find() devuelve -1
print(f".count('a')       = {frase.count('a')}")        # 4
print(f".startswith('La') = {frase.startswith('La')}")   # True
print(f".endswith('acto')  = {frase.endswith('acto')}")  # False

# --- Separar y unir ---
csv_line = "Ana,25,Ingeniera,CDMX"
partes = csv_line.split(",")
print(f"\n'{csv_line}'.split(',') = {partes}")

# join es el inverso de split
reunido = " | ".join(partes)
print(f"' | '.join(partes)   = '{reunido}'")

# splitlines — divide por saltos de línea
multi = "línea1\nlínea2\nlínea3"
print(f"splitlines: {multi.splitlines()}")

# --- Reemplazo ---
original = "Hola Mundo"
modificado = original.replace("Mundo", "Python")
print(f"\n'{original}'.replace('Mundo', 'Python') = '{modificado}'")

# Reemplazar solo las primeras N ocurrencias
texto_r = "aaa bbb aaa bbb aaa"
print(f"replace('aaa', 'xxx', 1) = '{texto_r.replace('aaa', 'xxx', 1)}'")

# --- Verificación ---
print(f"\n'123'.isdigit()   = {'123'.isdigit()}")       # True
print(f"'abc'.isalpha()   = {'abc'.isalpha()}")         # True
print(f"'abc123'.isalnum()= {'abc123'.isalnum()}")      # True
print(f"'   '.isspace()   = {'   '.isspace()}")         # True
print(f"'Hola'.islower()  = {'Hola'.islower()}")        # False
print(f"'HOLA'.isupper()  = {'HOLA'.isupper()}")        # True

# --- Alineación y relleno ---
print(f"\n'42'.zfill(5)       = {'42'.zfill(5)}")         # '00042'
print(f"'hola'.center(20, '-') = {'hola'.center(20, '-')}")
print(f"'hola'.ljust(20, '.')  = {'hola'.ljust(20, '.')}")
print(f"'hola'.rjust(20, '.')  = {'hola'.rjust(20, '.')}")

# ============================================================
# 5. FORMATEO DE STRINGS
# ============================================================

print("\n=== FORMATEO DE STRINGS ===\n")

nombre = "Ana"
edad = 25
pi = 3.14159265

# --- f-strings (Python 3.6+) — RECOMENDADO ---
print(f"Hola, {nombre}. Tienes {edad} años.")

# Expresiones dentro de llaves
print(f"En 10 años tendrás {edad + 10} años.")
print(f"{nombre.upper() = }")  # Debug: muestra la expresión Y el resultado

# Formateo numérico
print(f"Pi con 2 decimales: {pi:.2f}")
print(f"Millón con comas:   {1000000:,}")
print(f"Millón con guiones: {1000000:_}")
print(f"Porcentaje:         {0.856:.1%}")     # 85.6%
print(f"Binario:            {42:b}")           # 101010
print(f"Hexadecimal:        {255:x}")          # ff
print(f"Octal:              {8:o}")            # 10

# Alineación con f-strings
print(f"\n{'Izquierda':<20} |")
print(f"{'Centro':^20} |")
print(f"{'Derecha':>20} |")
print(f"{'Relleno':*^20} |")

# --- .format() ---
print("\n{0} tiene {1} años.".format(nombre, edad))
print("{nombre} tiene {edad} años.".format(nombre=nombre, edad=edad))

# --- % (estilo C — antiguo, no recomendado) ---
print("Hola, %s. Tienes %d años. Pi es %.2f." % (nombre, edad, pi))

# ============================================================
# 6. STRINGS MULTILÍNEA Y ESCAPES
# ============================================================

print("\n=== ESCAPES Y MULTILÍNEA ===\n")

# Secuencias de escape comunes:
print("Salto de línea:     línea1\\n línea2")
print("Tabulación:         col1\tcol2\tcol3")
print("Comilla simple:     it\\'s")
print("Comilla doble:      she said \\\"hi\\\"")
print("Barra invertida:    C:\\\\Users")
print(f"Unicode:            \\u00e9 = {chr(0x00e9)}")

# Multilínea sin triple comillas (con \)
texto_largo = "Esta es una línea muy larga que " \
              "se puede dividir usando barra " \
              "invertida al final."
print(f"\n{texto_largo}")

# Con triple comillas (preserva saltos de línea)
poema = """
    Caminante, no hay camino,
    se hace camino al andar.
    — Antonio Machado
"""
print(poema)

# Quitar indentación con textwrap.dedent
import textwrap
poema_limpio = textwrap.dedent(poema).strip()
print(f"Limpio:\n{poema_limpio}")

# ============================================================
# 7. OPERACIONES CON STRINGS
# ============================================================

print("\n=== OPERACIONES ===\n")

# Concatenación
saludo = "Hola" + " " + "Mundo"
print(f"Concatenación: {saludo}")

# Repetición
linea = "-" * 40
print(f"Repetición: {linea}")

# Pertenencia
print(f"'Hola' in 'Hola Mundo': {'Hola' in 'Hola Mundo'}")

# Longitud
print(f"len('Python'): {len('Python')}")

# Iterar sobre un string
print("Iterando: ", end="")
for char in "Hola":
    print(f"[{char}]", end=" ")
print()

# ============================================================
# 8. CODIFICACIÓN (ENCODING)
# ============================================================

print("\n=== CODIFICACIÓN ===\n")

# Python 3 usa Unicode (UTF-8) por defecto
texto_unicode = "café ñoño 日本語 🐍"
print(f"Texto Unicode: {texto_unicode}")

# Convertir a bytes (encode) y de vuelta (decode)
como_bytes = texto_unicode.encode("utf-8")
print(f"Como bytes: {como_bytes}")

de_vuelta = como_bytes.decode("utf-8")
print(f"De vuelta: {de_vuelta}")

# Caracteres especiales
print(f"\nCarácter U+00F1: {chr(0x00F1)}")      # ñ
print(f"Código de 'ñ': {ord('ñ')}")             # 241
print(f"Emoji serpiente: {chr(0x1F40D)}")

# ============================================================
# 9. TRUCOS Y PATRONES COMUNES
# ============================================================

print("\n=== TRUCOS Y PATRONES ===\n")

# Invertir un string
original = "abcdef"
invertido = original[::-1]
print(f"Invertir '{original}' → '{invertido}'")

# Verificar palíndromo
palabra = "reconocer"
es_palindromo = palabra == palabra[::-1]
print(f"¿'{palabra}' es palíndromo? {es_palindromo}")

# Contar palabras
frase = "El rápido zorro marrón salta sobre el perro perezoso"
num_palabras = len(frase.split())
print(f"Palabras en la frase: {num_palabras}")

# Eliminar vocales
sin_vocales = "".join(c for c in frase if c.lower() not in "aeiouáéíóú")
print(f"Sin vocales: '{sin_vocales}'")

# Capitalizar cada palabra manualmente
titulo = " ".join(p.capitalize() for p in "hola mundo python".split())
print(f"Título: '{titulo}'")

# Repetir patrón
patron = ("=-" * 20) + "="
print(f"Patrón: {patron}")

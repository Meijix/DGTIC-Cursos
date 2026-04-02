"""
Tipos de Datos en Python
========================
Python es un lenguaje de tipado dinámico: no declaramos el tipo de una
variable, el intérprete lo infiere del valor asignado.

Ejecuta este archivo:
    python tipos_datos.py
"""

# ============================================================
# 1. TIPOS NUMÉRICOS
# ============================================================

# --- Enteros (int) ---
# Python maneja enteros de precisión arbitraria: no hay límite de tamaño.
entero = 42
entero_negativo = -17
entero_grande = 10 ** 100  # Un googol — Python lo maneja sin problema

# Representaciones alternativas
binario = 0b1010       # 10 en binario
octal = 0o17           # 15 en octal
hexadecimal = 0xFF     # 255 en hexadecimal

# Separador visual para números grandes (Python 3.6+)
millon = 1_000_000     # Es exactamente igual a 1000000
print(f"Un millón: {millon}")
print(f"Binario 0b1010 = {binario}")
print(f"Hex 0xFF = {hexadecimal}")

# --- Flotantes (float) ---
# Implementación IEEE 754 de 64 bits (doble precisión).
flotante = 3.14159
notacion_cientifica = 1.5e-3   # 0.0015
infinito = float("inf")
no_es_numero = float("nan")

# CUIDADO: imprecisión de punto flotante
print(f"\n0.1 + 0.2 = {0.1 + 0.2}")  # 0.30000000000000004
print(f"¿0.1 + 0.2 == 0.3? {0.1 + 0.2 == 0.3}")  # False

# Solución: usar math.isclose o el módulo decimal
import math
print(f"¿Cercanos? {math.isclose(0.1 + 0.2, 0.3)}")  # True

# --- Complejos (complex) ---
complejo = 3 + 4j
print(f"\nComplejo: {complejo}")
print(f"Parte real: {complejo.real}, imaginaria: {complejo.imag}")

# ============================================================
# 2. TIPO BOOLEANO (bool)
# ============================================================

# bool es una SUBCLASE de int: True == 1, False == 0
verdadero = True
falso = False

print(f"\nTrue + True = {True + True}")   # 2
print(f"True * 10 = {True * 10}")         # 10
print(f"isinstance(True, int) = {isinstance(True, int)}")  # True

# --- Valores "falsy" (se evalúan como False) ---
# Regla: cero, vacío y None son falsy. Todo lo demás es truthy.
valores_falsy = [0, 0.0, 0j, "", [], {}, set(), None, False]
print("\nValores falsy:")
for valor in valores_falsy:
    print(f"  bool({valor!r:12s}) = {bool(valor)}")

# ============================================================
# 3. CADENAS DE TEXTO (str)
# ============================================================

# Las cadenas son secuencias INMUTABLES de caracteres Unicode.
cadena_simple = 'comillas simples'
cadena_doble = "comillas dobles"
cadena_triple = """Cadena
multilínea con
tres comillas"""

# Raw strings — ignoran secuencias de escape
ruta_windows = r"C:\Users\nueva\carpeta"  # Sin raw, \n sería salto de línea
print(f"\nRaw string: {ruta_windows}")

# ============================================================
# 4. NONE
# ============================================================

# None es el valor "nulo" de Python. Es un singleton.
valor_nulo = None
print(f"\nNone es: {valor_nulo}")
print(f"type(None): {type(None)}")

# Siempre comparar con 'is', no con '=='
if valor_nulo is None:
    print("La variable es None (comparada con 'is')")

# ============================================================
# 5. FUNCIONES DE INSPECCIÓN DE TIPOS
# ============================================================

print("\n--- Inspección de tipos ---")
datos = [42, 3.14, True, "hola", None, [1, 2], {"a": 1}]

for dato in datos:
    # type() devuelve la clase exacta
    # isinstance() verifica si es instancia de una clase (o tupla de clases)
    print(f"  {str(dato):12s} → type: {type(dato).__name__:8s} "
          f"| isinstance(int): {isinstance(dato, int)}")

# isinstance es preferible a type() == porque respeta herencia
print(f"\ntype(True) == int: {type(True) == int}")          # False
print(f"isinstance(True, int): {isinstance(True, int)}")    # True

# ============================================================
# 6. CONVERSIONES (CASTING)
# ============================================================

print("\n--- Conversiones ---")

# str → int
print(f"int('42') = {int('42')}")
print(f"int('0xFF', 16) = {int('0xFF', 16)}")  # Base 16

# str → float
print(f"float('3.14') = {float('3.14')}")

# número → str
print(f"str(100) = {str(100)!r}")

# Truthy/Falsy → bool
print(f"bool('') = {bool('')}")       # False
print(f"bool('x') = {bool('x')}")     # True
print(f"bool(0) = {bool(0)}")         # False
print(f"bool(42) = {bool(42)}")       # True

# ============================================================
# 7. IDENTIDAD vs IGUALDAD
# ============================================================

print("\n--- Identidad (is) vs Igualdad (==) ---")

a = [1, 2, 3]
b = [1, 2, 3]
c = a  # c apunta al mismo objeto que a

print(f"a == b: {a == b}")   # True — mismo contenido
print(f"a is b: {a is b}")   # False — objetos distintos en memoria
print(f"a is c: {a is c}")   # True — misma referencia

# Nota: Python cachea enteros pequeños (-5 a 256) y strings cortos
x = 256
y = 256
print(f"\n256 is 256: {x is y}")   # True (entero cacheado)

# ============================================================
# 8. ASIGNACIÓN MÚLTIPLE Y DESEMPAQUETADO
# ============================================================

print("\n--- Asignación múltiple ---")

# Asignar varios valores a la vez
nombre, edad, activo = "Ana", 25, True
print(f"nombre={nombre}, edad={edad}, activo={activo}")

# Intercambiar variables sin variable temporal
a, b = 10, 20
a, b = b, a
print(f"Después del swap: a={a}, b={b}")

# Asignación en cadena
x = y = z = 0
print(f"x={x}, y={y}, z={z}")

# ============================================================
# 9. CONSTANTES (por convención)
# ============================================================

# Python NO tiene constantes reales. Usamos MAYÚSCULAS por convención.
PI = 3.14159265358979
GRAVEDAD = 9.81
MAX_INTENTOS = 3

# Nada impide reasignarlas, pero NO DEBERÍAS hacerlo.
# PI = 0  # Mala práctica — rompe la convención

print(f"\nConstantes: PI={PI}, GRAVEDAD={GRAVEDAD}")

# ============================================================
# 10. TIPADO DINÁMICO EN ACCIÓN
# ============================================================

print("\n--- Tipado dinámico ---")

variable = 42
print(f"variable = {variable}, tipo: {type(variable).__name__}")

variable = "ahora soy un string"
print(f"variable = {variable}, tipo: {type(variable).__name__}")

variable = [1, 2, 3]
print(f"variable = {variable}, tipo: {type(variable).__name__}")

# Esto es legal en Python pero puede causar confusión.
# En proyectos grandes, usa TYPE HINTS (ver sección 03).

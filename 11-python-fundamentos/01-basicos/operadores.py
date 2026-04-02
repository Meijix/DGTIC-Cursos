"""
Operadores en Python
====================
Todos los operadores de Python organizados por categoría,
con ejemplos prácticos y notas sobre comportamiento inesperado.

Ejecuta este archivo:
    python operadores.py
"""

# ============================================================
# 1. OPERADORES ARITMÉTICOS
# ============================================================

print("=== OPERADORES ARITMÉTICOS ===\n")

a, b = 17, 5

print(f"{a} + {b}  = {a + b}")       # 22 — Suma
print(f"{a} - {b}  = {a - b}")       # 12 — Resta
print(f"{a} * {b}  = {a * b}")       # 85 — Multiplicación
print(f"{a} / {b}  = {a / b}")       # 3.4 — División real (siempre float)
print(f"{a} // {b} = {a // b}")      # 3 — División entera (floor)
print(f"{a} % {b}  = {a % b}")       # 2 — Módulo (residuo)
print(f"{a} ** {b} = {a ** b}")      # 1419857 — Potencia

# --- División entera con negativos ---
# Python redondea hacia -infinito (floor), NO hacia cero.
print(f"\n-17 // 5  = {-17 // 5}")    # -4 (no -3)
print(f"-17 % 5   = {-17 % 5}")      # 3 (no -2)
# Esto garantiza que: a == (a // b) * b + (a % b)
# -17 == (-4) * 5 + 3  →  -17 == -20 + 3  →  -17 == -17 ✓

# --- divmod() — división y módulo en una sola operación ---
cociente, residuo = divmod(17, 5)
print(f"\ndivmod(17, 5) = ({cociente}, {residuo})")

# ============================================================
# 2. OPERADORES DE COMPARACIÓN
# ============================================================

print("\n=== OPERADORES DE COMPARACIÓN ===\n")

x, y = 10, 20

print(f"{x} == {y}: {x == y}")    # False — Igualdad de valor
print(f"{x} != {y}: {x != y}")    # True  — Desigualdad
print(f"{x} < {y}:  {x < y}")     # True  — Menor que
print(f"{x} > {y}:  {x > y}")     # False — Mayor que
print(f"{x} <= {y}: {x <= y}")    # True  — Menor o igual
print(f"{x} >= {y}: {x >= y}")    # False — Mayor o igual

# --- Comparaciones encadenadas (característica única de Python) ---
edad = 25
# En vez de: edad >= 18 and edad <= 65
print(f"\n18 <= {edad} <= 65: {18 <= edad <= 65}")   # True
print(f"1 < 2 < 3: {1 < 2 < 3}")                     # True
print(f"1 < 2 > 0: {1 < 2 > 0}")                     # True

# ============================================================
# 3. OPERADORES DE IDENTIDAD: is / is not
# ============================================================

print("\n=== OPERADORES DE IDENTIDAD ===\n")

# 'is' compara si dos variables apuntan al MISMO objeto en memoria
# '==' compara si dos variables tienen el MISMO valor

lista_a = [1, 2, 3]
lista_b = [1, 2, 3]
lista_c = lista_a      # c es un alias de a

print(f"lista_a == lista_b: {lista_a == lista_b}")   # True (mismo valor)
print(f"lista_a is lista_b: {lista_a is lista_b}")   # False (distinto objeto)
print(f"lista_a is lista_c: {lista_a is lista_c}")   # True (mismo objeto)

# Uso correcto: SIEMPRE usar 'is' para comparar con None
valor = None
print(f"\nvalor is None: {valor is None}")       # Correcto
# print(f"valor == None: {valor == None}")       # Funciona pero NO recomendado

# ============================================================
# 4. OPERADORES LÓGICOS
# ============================================================

print("\n=== OPERADORES LÓGICOS ===\n")

# and, or, not — trabajan con valores truthy/falsy

print(f"True and True:   {True and True}")     # True
print(f"True and False:  {True and False}")    # False
print(f"False or True:   {False or True}")     # True
print(f"not True:        {not True}")          # False

# --- Cortocircuito (short-circuit) ---
# 'and' devuelve el primer valor falsy, o el último si todos son truthy
# 'or' devuelve el primer valor truthy, o el último si todos son falsy
print(f"\n0 and 'hola':     {0 and 'hola'!r}")      # 0 (primer falsy)
print(f"'hola' and 42:    {'hola' and 42}")          # 42 (último truthy)
print(f"'' or 'default':  {'' or 'default'!r}")      # 'default' (primer truthy)
print(f"None or 0 or []:  {None or 0 or []}")        # [] (último — todos falsy)

# --- Uso práctico del cortocircuito ---
nombre = ""
# Si nombre es vacío (falsy), usa "Anónimo"
nombre_final = nombre or "Anónimo"
print(f"\nnombre_final: {nombre_final!r}")

# ============================================================
# 5. OPERADORES DE PERTENENCIA: in / not in
# ============================================================

print("\n=== OPERADORES DE PERTENENCIA ===\n")

frutas = ["manzana", "pera", "uva"]
print(f"'pera' in frutas: {'pera' in frutas}")          # True
print(f"'kiwi' not in frutas: {'kiwi' not in frutas}")  # True

# Funciona con strings también
print(f"'Py' in 'Python': {'Py' in 'Python'}")          # True

# Y con diccionarios (busca en las llaves)
datos = {"nombre": "Ana", "edad": 25}
print(f"'nombre' in datos: {'nombre' in datos}")        # True
print(f"'Ana' in datos: {'Ana' in datos}")               # False (no busca valores)

# ============================================================
# 6. OPERADORES A NIVEL DE BITS (BITWISE)
# ============================================================

print("\n=== OPERADORES BITWISE ===\n")

# Trabajan con la representación binaria de los enteros
a, b = 0b1100, 0b1010   # 12 y 10

print(f"a     = {a:04b} ({a})")
print(f"b     = {b:04b} ({b})")
print(f"a & b = {a & b:04b} ({a & b})")    # AND: 1000 (8)
print(f"a | b = {a | b:04b} ({a | b})")    # OR:  1110 (14)
print(f"a ^ b = {a ^ b:04b} ({a ^ b})")    # XOR: 0110 (6)
print(f"~a    = {~a} (complemento)")         # NOT: -13
print(f"a << 2 = {a << 2:08b} ({a << 2})") # Shift izq: 110000 (48)
print(f"a >> 1 = {a >> 1:04b} ({a >> 1})") # Shift der: 0110 (6)

# Uso práctico: flags y permisos (estilo Unix)
READ    = 0b100   # 4
WRITE   = 0b010   # 2
EXECUTE = 0b001   # 1

permisos = READ | WRITE   # Combinar permisos: 110 (6)
print(f"\nPermisos: {permisos:03b}")
print(f"¿Tiene lectura? {bool(permisos & READ)}")     # True
print(f"¿Tiene ejecución? {bool(permisos & EXECUTE)}") # False

# ============================================================
# 7. ASIGNACIÓN AUMENTADA
# ============================================================

print("\n=== ASIGNACIÓN AUMENTADA ===\n")

x = 10
print(f"x inicial: {x}")

x += 5    # x = x + 5
print(f"x += 5  → {x}")     # 15

x -= 3    # x = x - 3
print(f"x -= 3  → {x}")     # 12

x *= 2    # x = x * 2
print(f"x *= 2  → {x}")     # 24

x //= 5   # x = x // 5
print(f"x //= 5 → {x}")    # 4

x **= 3   # x = x ** 3
print(f"x **= 3 → {x}")    # 64

x %= 10   # x = x % 10
print(f"x %%= 10 → {x}")   # 4

# También existen: &=, |=, ^=, <<=, >>=

# ============================================================
# 8. PRECEDENCIA DE OPERADORES
# ============================================================

print("\n=== PRECEDENCIA (de mayor a menor) ===\n")

# Tabla simplificada (de mayor a menor prioridad):
precedencia = """
  1. ()              — Paréntesis
  2. **              — Potencia
  3. +x, -x, ~x     — Unarios
  4. *, /, //, %     — Multiplicativos
  5. +, -            — Suma/Resta
  6. <<, >>          — Shift
  7. &               — AND bitwise
  8. ^               — XOR bitwise
  9. |               — OR bitwise
 10. ==, !=, <, >, <=, >=, is, in  — Comparación
 11. not             — NOT lógico
 12. and             — AND lógico
 13. or              — OR lógico
"""
print(precedencia)

# Ejemplo donde la precedencia importa:
resultado = 2 + 3 * 4 ** 2
# Se evalúa como: 2 + 3 * (4 ** 2) = 2 + 3 * 16 = 2 + 48 = 50
print(f"2 + 3 * 4 ** 2 = {resultado}")

# Consejo: en caso de duda, usa paréntesis para claridad
resultado_claro = 2 + (3 * (4 ** 2))
print(f"Con paréntesis explícitos: {resultado_claro}")

# ============================================================
# 9. WALRUS OPERATOR (:=) — Python 3.8+
# ============================================================

print("\n=== WALRUS OPERATOR (:=) ===\n")

# Asigna un valor Y lo devuelve en la misma expresión.
# Útil para evitar cálculos repetidos.

# Ejemplo 1: Filtrar y usar el resultado
datos = [1, 5, 3, 8, 2, 9, 4]
# Queremos los cuadrados, pero solo de los números > 5
grandes = [(cuadrado := x**2) for x in datos if x > 5]
print(f"Cuadrados de números > 5: {grandes}")

# Ejemplo 2: Leer hasta encontrar un valor (patrón común)
import random
random.seed(42)
intentos = 0
# Simular: generar números aleatorios hasta obtener un 7
while (numero := random.randint(1, 10)) != 7:
    intentos += 1
print(f"Se necesitaron {intentos} intentos para obtener un 7")

# Ejemplo 3: Verificar y usar longitud
texto = "Python es genial"
if (n := len(texto)) > 10:
    print(f"El texto tiene {n} caracteres (largo)")

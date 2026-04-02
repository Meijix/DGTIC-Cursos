"""
Funciones Lambda en Python
============================
Funciones anónimas de una sola expresión. Son útiles como
argumentos rápidos para funciones de orden superior.

Ejecuta este archivo:
    python lambdas.py
"""

# ============================================================
# 1. SINTAXIS BÁSICA
# ============================================================

print("=== SINTAXIS BÁSICA ===\n")

# Sintaxis: lambda parámetros: expresión
# La lambda evalúa UNA sola expresión y retorna su resultado.

# Equivalencias:
# lambda x: x ** 2   ↔   def f(x): return x ** 2

cuadrado = lambda x: x ** 2
suma = lambda a, b: a + b
identidad = lambda x: x
constante = lambda: 42

print(f"cuadrado(5) = {cuadrado(5)}")
print(f"suma(3, 4)  = {suma(3, 4)}")
print(f"identidad('hola') = {identidad('hola')}")
print(f"constante() = {constante()}")

# Lambda con valores por defecto
saludar = lambda nombre, saludo="Hola": f"{saludo}, {nombre}!"
print(f"saludar('Ana') = {saludar('Ana')}")
print(f"saludar('Ana', 'Buenos días') = {saludar('Ana', 'Buenos días')}")

# ============================================================
# 2. LAMBDA COMO ARGUMENTO
# ============================================================

print("\n=== LAMBDA COMO ARGUMENTO ===\n")

# Este es el uso principal y recomendado de lambdas:
# como argumentos de funciones de orden superior.

# --- sorted con key ---
palabras = ["Python", "es", "un", "lenguaje", "genial"]
por_longitud = sorted(palabras, key=lambda p: len(p))
print(f"Por longitud: {por_longitud}")

# Ordenar tuplas por segundo elemento
pares = [(3, "c"), (1, "a"), (2, "b")]
ordenados = sorted(pares, key=lambda x: x[1])
print(f"Por segundo elem: {ordenados}")

# --- max/min con key ---
personas = [
    {"nombre": "Ana", "edad": 25},
    {"nombre": "Luis", "edad": 30},
    {"nombre": "Eva", "edad": 22},
]
mayor = max(personas, key=lambda p: p["edad"])
print(f"Mayor: {mayor['nombre']} ({mayor['edad']})")

# --- map ---
numeros = [1, 2, 3, 4, 5]
dobles = list(map(lambda x: x * 2, numeros))
print(f"Dobles: {dobles}")

# --- filter ---
pares = list(filter(lambda x: x % 2 == 0, range(20)))
print(f"Pares: {pares}")

# ============================================================
# 3. LAMBDA vs DEF — CUÁNDO USAR CADA UNO
# ============================================================

print("\n=== LAMBDA vs DEF ===\n")

# REGLA: Si le vas a poner nombre, usa def.
# Las lambdas están diseñadas para ser anónimas y efímeras.

# MAL — lambda con nombre (antipatrón PEP 8)
# area_circulo = lambda r: 3.14159 * r ** 2

# BIEN — usar def si necesitas un nombre
import math
def area_circulo(r):
    """Calcula el área de un círculo dado su radio."""
    return math.pi * r ** 2

print(f"Área (r=5): {area_circulo(5):.2f}")

# BIEN — lambda anónima como argumento
resultado = sorted([3, -1, 4, -1, 5], key=lambda x: abs(x))
print(f"Ordenar por valor absoluto: {resultado}")

# ============================================================
# 4. LIMITACIONES DE LAMBDA
# ============================================================

print("\n=== LIMITACIONES ===\n")

# 1. Solo UNA expresión (no sentencias como if/for/while/=)
# MAL: lambda x: x = x + 1  # SyntaxError

# 2. No pueden contener asignaciones
# MAL: lambda x: y = x + 1  # SyntaxError

# 3. Sin docstring
# Las lambdas no tienen __doc__

# 4. Difícil de depurar (aparecen como <lambda> en tracebacks)

# Truco: operador ternario SÍ funciona (es una expresión)
clasificar = lambda x: "positivo" if x > 0 else "negativo" if x < 0 else "cero"
print(f"clasificar(5):  {clasificar(5)}")
print(f"clasificar(-3): {clasificar(-3)}")
print(f"clasificar(0):  {clasificar(0)}")

# ============================================================
# 5. LAMBDAS EN DICCIONARIOS (patrón strategy)
# ============================================================

print("\n=== PATRÓN STRATEGY ===\n")

# Usar diccionario de lambdas como alternativa a if/elif
operaciones = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b if b != 0 else "Error: div/0",
    "**": lambda a, b: a ** b,
    "%": lambda a, b: a % b,
}

def calcular(a, op, b):
    """Calculadora usando diccionario de lambdas."""
    if op not in operaciones:
        return f"Operador '{op}' no soportado"
    return operaciones[op](a, b)

ejemplos = [(10, "+", 3), (10, "-", 3), (10, "*", 3),
            (10, "/", 3), (10, "**", 3), (10, "/", 0)]

for a, op, b in ejemplos:
    print(f"  {a} {op} {b} = {calcular(a, op, b)}")

# ============================================================
# 6. LAMBDA Y CLOSURES
# ============================================================

print("\n=== LAMBDA Y CLOSURES ===\n")

# Las lambdas capturan variables del scope exterior (como cualquier closure)

def crear_funciones():
    """Ejemplo del problema clásico de late binding."""
    funciones = []
    for i in range(5):
        funciones.append(lambda: i)  # Todas capturan la MISMA variable i
    return funciones

# Problema: todas las funciones retornan 4 (el último valor de i)
fs = crear_funciones()
print("Late binding (problema):")
print(f"  Resultados: {[f() for f in fs]}")  # [4, 4, 4, 4, 4]

def crear_funciones_bien():
    """Solución: capturar el valor actual con argumento default."""
    funciones = []
    for i in range(5):
        funciones.append(lambda x=i: x)  # x=i captura el VALOR actual
    return funciones

fs = crear_funciones_bien()
print("Con default arg (solución):")
print(f"  Resultados: {[f() for f in fs]}")  # [0, 1, 2, 3, 4]

# ============================================================
# 7. EJEMPLOS PRÁCTICOS
# ============================================================

print("\n=== EJEMPLOS PRÁCTICOS ===\n")

# --- Ordenar diccionarios por valor ---
inventario = {"manzana": 5, "pera": 12, "uva": 3, "kiwi": 8}
por_cantidad = dict(sorted(inventario.items(), key=lambda item: item[1]))
print(f"Por cantidad: {por_cantidad}")

# --- Agrupar y transformar ---
datos = ["Ana:25", "Luis:30", "Eva:22", "Carlos:28"]
personas = list(map(lambda s: {"nombre": s.split(":")[0],
                                "edad": int(s.split(":")[1])}, datos))
print(f"Parseados: {personas}")

# --- Encadenar transformaciones ---
numeros = range(1, 21)
# Filtrar pares, elevar al cuadrado, y sumar
resultado = sum(map(lambda x: x**2, filter(lambda x: x % 2 == 0, numeros)))
print(f"Suma de cuadrados de pares (1-20): {resultado}")

# Lo mismo con comprehension (más legible):
resultado2 = sum(x**2 for x in range(1, 21) if x % 2 == 0)
print(f"Mismo resultado con comprehension: {resultado2}")

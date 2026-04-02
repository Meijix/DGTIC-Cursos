"""
Ciclos (Loops) en Python
=========================
Estructuras de repetición: while, for, y herramientas asociadas
como range(), enumerate(), zip(), break, continue, else.

Ejecuta este archivo:
    python ciclos.py
"""

# ============================================================
# 1. CICLO WHILE
# ============================================================

print("=== CICLO WHILE ===\n")

# El while se ejecuta mientras la condición sea True.
contador = 1
while contador <= 5:
    print(f"  Iteración {contador}")
    contador += 1

# --- While con centinela ---
# Patrón: repetir hasta que el usuario quiera salir.
# (No ejecutamos input aquí para que el script sea no interactivo)
print("\nSimulación de menú con centinela:")
opciones = ["ver", "agregar", "borrar", "salir"]
for opcion in opciones:
    if opcion == "salir":
        print(f"  Opción '{opcion}' → Saliendo...")
        break
    print(f"  Procesando opción: '{opcion}'")

# --- While con walrus operator (Python 3.8+) ---
import random
random.seed(42)

print("\nBuscando un 6 con dados (walrus):")
intentos = 0
while (dado := random.randint(1, 6)) != 6:
    intentos += 1
    print(f"  Intento {intentos}: salió {dado}")
print(f"  ¡Salió 6 después de {intentos} intentos!")

# ============================================================
# 2. CICLO FOR
# ============================================================

print("\n=== CICLO FOR ===\n")

# En Python, for itera sobre CUALQUIER iterable (no solo números).

# Iterar sobre string
print("Iterando sobre string:")
for char in "Hola":
    print(f"  '{char}'", end="")
print()

# Iterar sobre lista
print("\nIterando sobre lista:")
frutas = ["manzana", "pera", "uva", "kiwi"]
for fruta in frutas:
    print(f"  → {fruta}")

# Iterar sobre diccionario
print("\nIterando sobre diccionario:")
persona = {"nombre": "Ana", "edad": 25, "ciudad": "CDMX"}
for clave, valor in persona.items():
    print(f"  {clave}: {valor}")

# ============================================================
# 3. RANGE()
# ============================================================

print("\n=== RANGE() ===\n")

# range(fin)           → 0, 1, 2, ..., fin-1
# range(inicio, fin)   → inicio, inicio+1, ..., fin-1
# range(inicio, fin, paso) → con incremento personalizado

print("range(5):", list(range(5)))           # [0, 1, 2, 3, 4]
print("range(2, 8):", list(range(2, 8)))     # [2, 3, 4, 5, 6, 7]
print("range(0, 10, 2):", list(range(0, 10, 2)))  # [0, 2, 4, 6, 8]
print("range(10, 0, -2):", list(range(10, 0, -2)))  # [10, 8, 6, 4, 2]

# range() es LAZY: no crea la lista en memoria
# Esto ocupa la misma memoria que range(5):
rango_enorme = range(1_000_000_000)
print(f"\n¿500_000 está en el rango? {500_000 in rango_enorme}")  # True (O(1))
print(f"Longitud del rango: {len(rango_enorme):,}")

# ============================================================
# 4. ENUMERATE()
# ============================================================

print("\n=== ENUMERATE() ===\n")

# enumerate() devuelve pares (índice, valor).
# Evita el antipatrón de: for i in range(len(lista))

lenguajes = ["Python", "JavaScript", "Rust", "Go"]

# MAL (antipatrón):
# for i in range(len(lenguajes)):
#     print(f"{i}: {lenguajes[i]}")

# BIEN (pythónico):
print("Lenguajes populares:")
for i, lenguaje in enumerate(lenguajes, start=1):  # start=1 para contar desde 1
    print(f"  {i}. {lenguaje}")

# ============================================================
# 5. ZIP()
# ============================================================

print("\n=== ZIP() ===\n")

# zip() combina múltiples iterables en paralelo.
nombres = ["Ana", "Luis", "Eva"]
edades = [25, 30, 22]
ciudades = ["CDMX", "GDL", "MTY"]

print("Datos combinados:")
for nombre, edad, ciudad in zip(nombres, edades, ciudades):
    print(f"  {nombre} tiene {edad} años y vive en {ciudad}")

# zip se detiene en el iterable más corto
corta = [1, 2]
larga = [10, 20, 30, 40]
print(f"\nzip con longitudes distintas: {list(zip(corta, larga))}")

# Para NO perder datos, usar itertools.zip_longest
from itertools import zip_longest
print(f"zip_longest: {list(zip_longest(corta, larga, fillvalue=0))}")

# Truco: desempaquetar con zip (transponer)
pares = [(1, "a"), (2, "b"), (3, "c")]
numeros, letras = zip(*pares)
print(f"\nTransponer: números={numeros}, letras={letras}")

# ============================================================
# 6. BREAK, CONTINUE Y ELSE
# ============================================================

print("\n=== BREAK, CONTINUE, ELSE ===\n")

# --- break: salir del ciclo inmediatamente ---
print("Buscando el primer número par:")
numeros = [1, 3, 7, 4, 9, 2]
for num in numeros:
    if num % 2 == 0:
        print(f"  Encontrado: {num}")
        break
    print(f"  {num} no es par, sigo buscando...")

# --- continue: saltar a la siguiente iteración ---
print("\nSolo números impares:")
for i in range(10):
    if i % 2 == 0:
        continue  # Salta los pares
    print(f"  {i}", end="")
print()

# --- else en ciclos (poco conocido pero útil) ---
# El bloque else se ejecuta si el ciclo terminó SIN break.

print("\n¿Hay algún negativo?")
datos = [5, 3, 8, 1, 9]
for dato in datos:
    if dato < 0:
        print(f"  ¡Encontré un negativo: {dato}!")
        break
else:
    # Este bloque se ejecuta porque NO hubo break
    print("  No se encontraron números negativos.")

# Comparar cuando SÍ hay un negativo:
datos_con_negativo = [5, 3, -2, 1, 9]
for dato in datos_con_negativo:
    if dato < 0:
        print(f"  ¡Encontré un negativo: {dato}!")
        break
else:
    print("  No se encontraron números negativos.")

# ============================================================
# 7. CICLOS ANIDADOS
# ============================================================

print("\n=== CICLOS ANIDADOS ===\n")

# Tabla de multiplicar del 1 al 5
print("Tabla de multiplicar (1-5):")
print("     ", end="")
for j in range(1, 6):
    print(f"{j:4d}", end="")
print("\n    " + "-" * 20)

for i in range(1, 6):
    print(f"{i:2d} |", end="")
    for j in range(1, 6):
        print(f"{i*j:4d}", end="")
    print()

# --- Patrón de triángulo ---
print("\nTriángulo de asteriscos:")
n = 5
for i in range(1, n + 1):
    print("  " + " " * (n - i) + "*" * (2 * i - 1))

# ============================================================
# 8. PATRONES AVANZADOS
# ============================================================

print("\n=== PATRONES AVANZADOS ===\n")

# --- Iterar con índice y condición ---
print("Elementos en posiciones pares:")
colores = ["rojo", "azul", "verde", "amarillo", "morado"]
for i, color in enumerate(colores):
    if i % 2 == 0:
        print(f"  [{i}] {color}")

# --- Iterar en reversa ---
print("\nCuenta regresiva:")
for i in reversed(range(1, 6)):
    print(f"  {i}...", end="")
print(" ¡Despegue!")

# También: for i in range(5, 0, -1)

# --- Iterar sobre múltiples listas con índice ---
print("\nComparación de listas:")
esperado = [10, 20, 30, 40, 50]
obtenido = [10, 22, 30, 38, 50]
for i, (exp, obt) in enumerate(zip(esperado, obtenido)):
    estado = "✓ OK" if exp == obt else f"✗ DIFF (esperado {exp})"
    print(f"  [{i}] obtenido={obt} → {estado}")

# ============================================================
# 9. ANTIPATRONES (qué NO hacer)
# ============================================================

print("\n=== ANTIPATRONES ===\n")

# ❌ MAL: Modificar una lista mientras se itera
# numeros = [1, 2, 3, 4, 5]
# for n in numeros:
#     if n % 2 == 0:
#         numeros.remove(n)  # Puede saltar elementos

# ✓ BIEN: Crear una nueva lista
numeros = [1, 2, 3, 4, 5]
impares = [n for n in numeros if n % 2 != 0]
print(f"Solo impares (con comprehension): {impares}")

# ❌ MAL: for i in range(len(lista)) para acceder a elementos
# ✓ BIEN: usar enumerate si necesitas el índice, o for item in lista si no

# ❌ MAL: while True sin condición de salida clara
# ✓ BIEN: while con condición explícita, o while True con break controlado

# ============================================================
# 10. EJEMPLO INTEGRADOR: NÚMEROS PRIMOS
# ============================================================

print("\n=== EJEMPLO: NÚMEROS PRIMOS ===\n")


def es_primo(n):
    """Verifica si un número es primo."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    # Solo verificar impares hasta la raíz cuadrada
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


# Encontrar primos menores a 50
limite = 50
primos = [n for n in range(2, limite) if es_primo(n)]
print(f"Primos menores a {limite}: {primos}")
print(f"Cantidad: {len(primos)}")

# ============================================================
# 11. EJEMPLO INTEGRADOR: FIZZBUZZ
# ============================================================

print("\n=== EJEMPLO: FIZZBUZZ ===\n")

# Reglas: múltiplo de 3 → Fizz, de 5 → Buzz, de ambos → FizzBuzz
for i in range(1, 31):
    if i % 15 == 0:       # Múltiplo de 3 Y 5 (verificar primero)
        print("FizzBuzz", end=" ")
    elif i % 3 == 0:
        print("Fizz", end=" ")
    elif i % 5 == 0:
        print("Buzz", end=" ")
    else:
        print(i, end=" ")
print()

# Versión elegante con concatenación:
print("\nVersión alternativa:")
for i in range(1, 31):
    resultado = ""
    if i % 3 == 0:
        resultado += "Fizz"
    if i % 5 == 0:
        resultado += "Buzz"
    print(resultado or i, end=" ")
print()

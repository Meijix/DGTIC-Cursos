"""
Generadores en Python
======================
Los generadores son funciones que producen valores uno a la vez
usando 'yield'. Permiten evaluacion perezosa (lazy evaluation):
los valores se calculan bajo demanda, sin cargar todo en memoria.

Ejecuta este archivo:
    python generadores.py
"""

import sys

# ============================================================
# 1. YIELD — LA BASE DE LOS GENERADORES
# ============================================================

# Una funcion normal usa 'return' y termina.
# Un generador usa 'yield': PAUSA y devuelve un valor,
# luego REANUDA donde se quedo en la siguiente llamada.

def contar_hasta(n):
    """Genera numeros del 1 al n."""
    print(f"  (Generador: iniciando)")
    i = 1
    while i <= n:
        print(f"  (Generador: produciendo {i})")
        yield i       # Pausa aqui y devuelve i
        i += 1        # Reanuda aqui cuando se pide el siguiente
    print(f"  (Generador: terminado)")

print("=== yield basico ===")
gen = contar_hasta(3)

# El generador NO se ejecuta al crearlo
print(f"Tipo: {type(gen)}")  # <class 'generator'>

# Se ejecuta paso a paso con next()
print(f"\nPrimer next():  {next(gen)}")
print(f"Segundo next(): {next(gen)}")
print(f"Tercer next():  {next(gen)}")

# El cuarto next() lanza StopIteration
try:
    next(gen)
except StopIteration:
    print("StopIteration: el generador se agoto")

# ============================================================
# 2. GENERADOR EN UN FOR (uso normal)
# ============================================================

# El for maneja automaticamente StopIteration.
print("\n=== Generador en un for ===")
for numero in contar_hasta(3):
    print(f"  Recibido: {numero}")

# ============================================================
# 3. GENERADOR VS FUNCION NORMAL
# ============================================================

def lista_cuadrados(n):
    """Retorna una LISTA con todos los cuadrados (todo en memoria)."""
    resultado = []
    for i in range(n):
        resultado.append(i ** 2)
    return resultado

def gen_cuadrados(n):
    """GENERA cuadrados uno a uno (memoria constante)."""
    for i in range(n):
        yield i ** 2

print("\n=== Comparacion de memoria ===")
n = 100_000

lista = lista_cuadrados(n)
generador = gen_cuadrados(n)

print(f"Lista de {n} elementos: {sys.getsizeof(lista):,} bytes")
print(f"Generador de {n} elementos: {sys.getsizeof(generador)} bytes")
# El generador usa memoria CONSTANTE sin importar n

# ============================================================
# 4. FIBONACCI — EJEMPLO CLASICO DE GENERADOR INFINITO
# ============================================================

def fibonacci():
    """Genera la secuencia de Fibonacci infinitamente."""
    a, b = 0, 1
    while True:      # Nunca termina — produce valores para siempre
        yield a
        a, b = b, a + b

print("\n=== Fibonacci infinito (primeros 15) ===")
fib = fibonacci()
primeros_15 = [next(fib) for _ in range(15)]
print(f"Fibonacci: {primeros_15}")

# ============================================================
# 5. LECTURA DE ARCHIVOS GRANDES (LAZY)
# ============================================================

import tempfile
import os

def leer_lineas(ruta):
    """
    Lee un archivo linea por linea sin cargarlo completo en memoria.
    Ideal para archivos de gigabytes.
    """
    with open(ruta, "r", encoding="utf-8") as f:
        for numero, linea in enumerate(f, start=1):
            yield numero, linea.rstrip()

# Crear un archivo de ejemplo
temp = tempfile.NamedTemporaryFile(mode="w", suffix=".txt",
                                   delete=False, encoding="utf-8")
for i in range(10):
    temp.write(f"Linea {i + 1}: datos de ejemplo\n")
temp.close()

print("\n=== Lectura lazy de archivo ===")
for num, linea in leer_lineas(temp.name):
    if num <= 5:  # Solo mostramos las primeras 5
        print(f"  {num:3d} | {linea}")
    elif num == 6:
        print("  ... (continuaria sin cargar todo en memoria)")
        break

os.unlink(temp.name)

# ============================================================
# 6. EXPRESIONES GENERADORAS vs LIST COMPREHENSIONS
# ============================================================

print("\n=== Expresiones generadoras ===")

# List comprehension — crea la lista completa en memoria
lista = [x ** 2 for x in range(10)]
print(f"Lista:     {lista}")
print(f"  Tipo: {type(lista)}, Tamanio: {sys.getsizeof(lista)} bytes")

# Expresion generadora — calcula bajo demanda (parentesis en vez de corchetes)
gen_expr = (x ** 2 for x in range(10))
print(f"Generador: {gen_expr}")
print(f"  Tipo: {type(gen_expr)}, Tamanio: {sys.getsizeof(gen_expr)} bytes")

# Se puede usar directamente en funciones como argumento
# (no necesitas doble parentesis)
total = sum(x ** 2 for x in range(10))
mayor = max(x ** 2 for x in range(10))
print(f"\nsum(x**2 for x in range(10)) = {total}")
print(f"max(x**2 for x in range(10)) = {mayor}")

# ============================================================
# 7. next() CON VALOR POR DEFECTO
# ============================================================

print("\n=== next() con default ===")

gen = (x for x in [10, 20, 30])
print(f"next(gen):           {next(gen)}")        # 10
print(f"next(gen):           {next(gen)}")        # 20
print(f"next(gen):           {next(gen)}")        # 30
print(f"next(gen, 'Fin'):    {next(gen, 'Fin')}")  # Fin (en vez de StopIteration)

# ============================================================
# 8. yield from — DELEGAR A OTRO GENERADOR
# ============================================================

def gen_a():
    yield 1
    yield 2

def gen_b():
    yield 3
    yield 4

def combinado():
    """Combina dos generadores usando yield from."""
    yield from gen_a()   # Delega al generador A
    yield from gen_b()   # Luego al generador B
    yield 5              # Y agrega su propio valor

print("\n=== yield from ===")
print(f"Combinado: {list(combinado())}")

# Util para aplanar estructuras anidadas
def aplanar(estructura):
    """Aplana listas anidadas de cualquier profundidad."""
    for elemento in estructura:
        if isinstance(elemento, (list, tuple)):
            yield from aplanar(elemento)  # Recursion con yield from
        else:
            yield elemento

anidada = [1, [2, 3], [4, [5, 6]], [[7, 8], 9]]
print(f"Anidada:  {anidada}")
print(f"Aplanada: {list(aplanar(anidada))}")

# ============================================================
# 9. send() — ENVIAR VALORES AL GENERADOR (COROUTINE BASICA)
# ============================================================

def acumulador():
    """
    Generador que acumula valores enviados con send().
    send() envia un valor que se convierte en el resultado de yield.
    """
    total = 0
    while True:
        valor = yield total    # yield devuelve total, recibe valor
        if valor is None:
            break
        total += valor

print("\n=== send() — coroutine basica ===")
acc = acumulador()
next(acc)                      # Inicializar (avanza hasta el primer yield)
print(f"send(10): {acc.send(10)}")   # total = 10
print(f"send(20): {acc.send(20)}")   # total = 30
print(f"send(5):  {acc.send(5)}")    # total = 35

# ============================================================
# 10. GENERADOR COMO PIPELINE (PATRON COMUN)
# ============================================================

def numeros(n):
    """Genera numeros del 0 al n-1."""
    for i in range(n):
        yield i

def filtrar_pares(iterable):
    """Filtra solo los pares."""
    for x in iterable:
        if x % 2 == 0:
            yield x

def al_cuadrado(iterable):
    """Eleva cada elemento al cuadrado."""
    for x in iterable:
        yield x ** 2

def tomar(iterable, n):
    """Toma los primeros n elementos."""
    for i, x in enumerate(iterable):
        if i >= n:
            break
        yield x

# Pipeline: numeros -> pares -> cuadrado -> tomar 5
print("\n=== Pipeline de generadores ===")
pipeline = tomar(al_cuadrado(filtrar_pares(numeros(100))), 5)
print(f"Pipeline resultado: {list(pipeline)}")
# Equivale a: [0, 4, 16, 36, 64] (cuadrados de 0, 2, 4, 6, 8)
# NADA se calcula hasta que iteramos — todo es lazy

# ============================================================
# RESUMEN
# ============================================================

print("""
=== RESUMEN DE GENERADORES ===

1. yield PAUSA la funcion y devuelve un valor.
2. Los generadores son LAZY: calculan bajo demanda.
3. Memoria O(1) vs O(n) de las listas.
4. Expresion generadora: (x for x in iterable) — como comprehension lazy.
5. next(gen) avanza un paso; next(gen, default) evita StopIteration.
6. yield from delega a otro generador.
7. send() permite enviar valores al generador (uso avanzado).
8. Los generadores se pueden encadenar como pipelines.
""")

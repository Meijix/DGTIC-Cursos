"""
Iteradores en Python — El Protocolo de Iteracion
===================================================
Un iterador es un objeto que implementa __iter__() y __next__().
Entender iteradores es clave para entender for loops, generadores,
comprehensions y gran parte de Python.

Ejecuta este archivo:
    python iteradores.py
"""

import sys

# ============================================================
# 1. ITERABLE vs ITERATOR
# ============================================================

# ITERABLE: objeto que tiene __iter__() -> retorna un iterator
# ITERATOR: objeto que tiene __iter__() y __next__() -> produce valores

print("=== Iterable vs Iterator ===\n")

mi_lista = [10, 20, 30]                     # Iterable
iterador = iter(mi_lista)                    # Iterator (creado con iter())

print(f"Lista tiene __iter__: {hasattr(mi_lista, '__iter__')}")     # True
print(f"Lista tiene __next__: {hasattr(mi_lista, '__next__')}")     # False
print(f"Iterador tiene __iter__: {hasattr(iterador, '__iter__')}")  # True
print(f"Iterador tiene __next__: {hasattr(iterador, '__next__')}")  # True

# Recorrer manualmente
print(f"\nnext(iterador): {next(iterador)}")  # 10
print(f"next(iterador): {next(iterador)}")    # 20
print(f"next(iterador): {next(iterador)}")    # 30

try:
    next(iterador)
except StopIteration:
    print("StopIteration: iterador agotado")

# Un for loop hace EXACTAMENTE esto internamente:
# 1. Llama iter(objeto) para obtener un iterador
# 2. Llama next(iterador) repetidamente
# 3. Captura StopIteration para terminar

# ============================================================
# 2. CREAR UN ITERADOR PERSONALIZADO (CLASE)
# ============================================================

class CuentaRegresiva:
    """
    Iterador que cuenta hacia atras desde un numero dado.
    Implementa el protocolo de iteracion: __iter__ y __next__.
    """

    def __init__(self, inicio):
        self.actual = inicio

    def __iter__(self):
        # Un iterador se retorna a si mismo
        return self

    def __next__(self):
        if self.actual <= 0:
            raise StopIteration     # Senial de que se termino
        valor = self.actual
        self.actual -= 1
        return valor

print("\n=== Iterador personalizado: CuentaRegresiva ===")
cuenta = CuentaRegresiva(5)

# Funciona en un for porque implementa el protocolo
for numero in cuenta:
    print(f"  {numero}...")
print("  Despegue!")

# ============================================================
# 3. ITERABLE vs ITERATOR — DIFERENCIA CLAVE
# ============================================================

# Un ITERABLE puede recorrerse multiples veces (crea nuevo iterator cada vez).
# Un ITERATOR solo se recorre UNA vez.

class Rango:
    """
    Iterable personalizado (como range).
    __iter__ retorna un NUEVO iterador cada vez.
    """

    def __init__(self, fin):
        self.fin = fin

    def __iter__(self):
        # Retorna un nuevo iterador cada vez
        return _RangoIterator(self.fin)

class _RangoIterator:
    """Iterador interno para Rango."""

    def __init__(self, fin):
        self.actual = 0
        self.fin = fin

    def __iter__(self):
        return self

    def __next__(self):
        if self.actual >= self.fin:
            raise StopIteration
        valor = self.actual
        self.actual += 1
        return valor

print("\n=== Iterable reutilizable ===")
mi_rango = Rango(4)

print("Primera iteracion:", list(mi_rango))   # [0, 1, 2, 3]
print("Segunda iteracion:", list(mi_rango))   # [0, 1, 2, 3] — funciona!

# Compara con un iterador simple que se agota:
iterador_simple = CuentaRegresiva(3)
print("\nIterador primera vez:", list(iterador_simple))   # [3, 2, 1]
print("Iterador segunda vez:", list(iterador_simple))     # [] — agotado!

# ============================================================
# 4. POR QUE LOS ITERADORES SON EFICIENTES EN MEMORIA
# ============================================================

print("\n=== Eficiencia de memoria ===")

# range() es un iterable, NO crea la lista en memoria
rango_grande = range(1_000_000)
lista_grande = list(range(1_000_000))

print(f"range(1_000_000): {sys.getsizeof(rango_grande)} bytes")
print(f"list(range(1_000_000)): {sys.getsizeof(lista_grande):,} bytes")
# El range usa bytes constantes sin importar el tamanio

# ============================================================
# 5. itertools — HERRAMIENTAS PARA ITERADORES
# ============================================================

import itertools

print("\n=== itertools ===\n")

# --- chain: concatenar iterables ---
letras = "abc"
numeros = [1, 2, 3]
combinado = list(itertools.chain(letras, numeros))
print(f"chain('abc', [1,2,3]): {combinado}")
# ['a', 'b', 'c', 1, 2, 3]

# --- islice: tomar una rebanada de un iterador ---
# Util con iteradores infinitos o cuando no puedes usar [:]
infinito = itertools.count(10)  # 10, 11, 12, 13, ...
primeros_5 = list(itertools.islice(infinito, 5))
print(f"islice(count(10), 5): {primeros_5}")
# [10, 11, 12, 13, 14]

# --- zip_longest: zip sin truncar ---
nombres = ["Ana", "Luis", "Pedro"]
edades = [25, 30]
# zip normal trunca al mas corto
print(f"\nzip normal: {list(zip(nombres, edades))}")
# zip_longest rellena con un valor por defecto
resultado = list(itertools.zip_longest(nombres, edades, fillvalue="??"))
print(f"zip_longest: {resultado}")

# --- product: producto cartesiano ---
colores = ["rojo", "azul"]
tallas = ["S", "M", "L"]
combos = list(itertools.product(colores, tallas))
print(f"\nproduct(colores, tallas):")
for combo in combos:
    print(f"  {combo}")

# --- combinations: combinaciones ---
items = ["A", "B", "C", "D"]
combos_2 = list(itertools.combinations(items, 2))
print(f"\ncombinations(['A','B','C','D'], 2): {combos_2}")

# --- permutations: permutaciones ---
perms = list(itertools.permutations(["X", "Y", "Z"], 2))
print(f"permutations(['X','Y','Z'], 2): {perms}")

# --- groupby: agrupar elementos consecutivos ---
datos = [("fruta", "manzana"), ("fruta", "pera"),
         ("verdura", "zanahoria"), ("verdura", "brocoli"),
         ("fruta", "uva")]

# IMPORTANTE: groupby agrupa elementos CONSECUTIVOS, por lo que
# los datos deben estar ordenados por la clave.
datos_ordenados = sorted(datos, key=lambda x: x[0])
print(f"\ngroupby (agrupados por categoria):")
for clave, grupo in itertools.groupby(datos_ordenados, key=lambda x: x[0]):
    items = [item[1] for item in grupo]
    print(f"  {clave}: {items}")

# --- accumulate: sumas acumuladas ---
numeros = [1, 2, 3, 4, 5]
acumulado = list(itertools.accumulate(numeros))
print(f"\naccumulate([1,2,3,4,5]): {acumulado}")
# [1, 3, 6, 10, 15]

# --- takewhile / dropwhile ---
datos = [2, 4, 6, 7, 8, 10]
tomados = list(itertools.takewhile(lambda x: x % 2 == 0, datos))
saltados = list(itertools.dropwhile(lambda x: x % 2 == 0, datos))
print(f"\ntakewhile(par, [2,4,6,7,8,10]): {tomados}")   # [2, 4, 6]
print(f"dropwhile(par, [2,4,6,7,8,10]): {saltados}")     # [7, 8, 10]

# --- cycle: repetir infinitamente ---
ciclo = itertools.cycle(["A", "B", "C"])
primeros_7 = [next(ciclo) for _ in range(7)]
print(f"\ncycle(['A','B','C']) x7: {primeros_7}")

# ============================================================
# 6. EJEMPLO PRACTICO: PROCESAR DATOS CON ITERTOOLS
# ============================================================

print("\n=== Ejemplo: procesamiento de datos ===")

# Simular datos de sensores (lectura cada segundo)
def sensor_temperatura():
    """Genera lecturas de temperatura simuladas."""
    import random
    random.seed(42)
    while True:
        yield round(random.gauss(22.0, 2.0), 1)

# Tomar las primeras 20 lecturas
lecturas = list(itertools.islice(sensor_temperatura(), 20))
print(f"Lecturas: {lecturas}")

# Promedio movil (ventanas de 5)
def ventanas(iterable, tamanio):
    """Genera ventanas deslizantes de tamanio dado."""
    it = iter(iterable)
    ventana = list(itertools.islice(it, tamanio))
    if len(ventana) == tamanio:
        yield tuple(ventana)
    for elemento in it:
        ventana = ventana[1:] + [elemento]
        yield tuple(ventana)

promedios = [round(sum(v) / len(v), 1) for v in ventanas(lecturas, 5)]
print(f"Promedios (ventana 5): {promedios}")

# ============================================================
# RESUMEN
# ============================================================

print("""
=== RESUMEN DE ITERADORES ===

1. Iterable: tiene __iter__() — puede crear un iterador.
2. Iterator: tiene __iter__() y __next__() — produce valores.
3. for loop usa iter() + next() + captura StopIteration.
4. Un iterador se agota despues de una iteracion.
5. Un iterable puede crear multiples iteradores.
6. itertools ofrece herramientas eficientes para iteracion:
   - chain, islice, cycle, count, repeat
   - product, combinations, permutations
   - groupby, accumulate, zip_longest
   - takewhile, dropwhile, filterfalse
""")

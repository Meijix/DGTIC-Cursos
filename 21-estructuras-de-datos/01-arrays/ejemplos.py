"""
Arrays (Arreglos) en Python
============================
Un array es una estructura de datos que almacena elementos en posiciones
contiguas de memoria, permitiendo acceso directo por indice en O(1).
En Python, la 'list' es la implementacion mas comun, aunque el modulo
'array' ofrece arreglos tipados mas eficientes en memoria.
"""

from array import array
from collections import deque
import time

# =============================================================================
# 1. Operaciones basicas con listas
# =============================================================================
print("=" * 60)
print("1. OPERACIONES BASICAS CON LISTAS")
print("=" * 60)

# Crear una lista
frutas = ["manzana", "banana", "cereza", "durazno", "uva"]
print(f"Lista original: {frutas}")

# Acceso por indice
print(f"Elemento en indice 0: {frutas[0]}")
print(f"Elemento en indice -1 (ultimo): {frutas[-1]}")

# Append: agregar al final O(1)
frutas.append("kiwi")
print(f"Despues de append('kiwi'): {frutas}")

# Insert: agregar en posicion especifica O(n)
frutas.insert(2, "naranja")
print(f"Despues de insert(2, 'naranja'): {frutas}")

# Delete: eliminar por valor
frutas.remove("banana")
print(f"Despues de remove('banana'): {frutas}")

# Delete: eliminar por indice
eliminado = frutas.pop(3)
print(f"Despues de pop(3), eliminado='{eliminado}': {frutas}")

# Slicing (rebanado)
print(f"Slice [1:4]: {frutas[1:4]}")
print(f"Slice [::2] (cada 2): {frutas[::2]}")
print(f"Slice [::-1] (reversa): {frutas[::-1]}")

# Busqueda
print(f"'cereza' esta en la lista: {'cereza' in frutas}")
print(f"Indice de 'cereza': {frutas.index('cereza')}")

# =============================================================================
# 2. Modulo array: arreglos tipados
# =============================================================================
print("\n" + "=" * 60)
print("2. MODULO ARRAY: ARREGLOS TIPADOS")
print("=" * 60)

# 'i' = enteros con signo, 'f' = flotantes, 'd' = dobles
numeros = array('i', [10, 20, 30, 40, 50])
print(f"Array de enteros: {numeros}")
print(f"Tipo de dato: '{numeros.typecode}' (entero con signo)")

numeros.append(60)
print(f"Despues de append(60): {numeros}")

numeros.insert(0, 5)
print(f"Despues de insert(0, 5): {numeros}")

numeros.pop(3)
print(f"Despues de pop(3): {numeros}")

# Convertir a lista normal
lista_normal = numeros.tolist()
print(f"Convertido a lista: {lista_normal}")

# Arrays de punto flotante
temperaturas = array('f', [36.5, 37.0, 38.2, 36.8])
print(f"Array de flotantes: {temperaturas}")

# =============================================================================
# 3. Comparacion de rendimiento: list vs deque
# =============================================================================
print("\n" + "=" * 60)
print("3. RENDIMIENTO: list.insert(0) vs deque.appendleft()")
print("=" * 60)

n = 50_000

# Insercion al inicio con lista - O(n) por operacion
inicio = time.perf_counter()
lista = []
for i in range(n):
    lista.insert(0, i)
tiempo_lista = time.perf_counter() - inicio

# Insercion al inicio con deque - O(1) por operacion
inicio = time.perf_counter()
cola = deque()
for i in range(n):
    cola.appendleft(i)
tiempo_deque = time.perf_counter() - inicio

print(f"Insertando {n:,} elementos al inicio:")
print(f"  list.insert(0, x):    {tiempo_lista:.4f} segundos")
print(f"  deque.appendleft(x):  {tiempo_deque:.4f} segundos")
print(f"  deque fue {tiempo_lista / tiempo_deque:.1f}x mas rapido")

# =============================================================================
# 4. Operaciones utiles adicionales
# =============================================================================
print("\n" + "=" * 60)
print("4. OPERACIONES UTILES ADICIONALES")
print("=" * 60)

nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
print(f"Lista original: {nums}")
print(f"Ordenada: {sorted(nums)}")
print(f"Sin duplicados (set): {sorted(set(nums))}")
print(f"Suma: {sum(nums)}, Min: {min(nums)}, Max: {max(nums)}")

# List comprehension
cuadrados = [x**2 for x in range(1, 11)]
print(f"Cuadrados del 1 al 10: {cuadrados}")

# Matrices (array 2D)
matriz = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
print(f"Matriz 3x3:")
for fila in matriz:
    print(f"  {fila}")
print(f"Elemento [1][2] = {matriz[1][2]}")

# Complejidad de operaciones
print("\n" + "=" * 60)
print("RESUMEN DE COMPLEJIDAD")
print("=" * 60)
print("  Acceso por indice:   O(1)")
print("  Busqueda:            O(n)")
print("  Insercion al final:  O(1) amortizado")
print("  Insercion al inicio: O(n)")
print("  Eliminacion al final: O(1)")
print("  Eliminacion al inicio: O(n)")

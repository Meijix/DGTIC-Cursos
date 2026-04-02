"""
Listas en Python
=================
Las listas son la estructura de datos más versátil de Python:
secuencias mutables y ordenadas que pueden contener cualquier tipo.

Ejecuta este archivo:
    python listas.py
"""

# ============================================================
# 1. CREACIÓN DE LISTAS
# ============================================================

print("=== CREACIÓN DE LISTAS ===\n")

# Literal
numeros = [1, 2, 3, 4, 5]
mixta = [1, "hola", 3.14, True, None, [5, 6]]
vacia = []

# Constructor list()
desde_string = list("Python")     # ['P', 'y', 't', 'h', 'o', 'n']
desde_range = list(range(5))       # [0, 1, 2, 3, 4]
desde_tupla = list((1, 2, 3))     # [1, 2, 3]

print(f"Desde string: {desde_string}")
print(f"Desde range:  {desde_range}")
print(f"Mixta:        {mixta}")

# Repetición
ceros = [0] * 5                    # [0, 0, 0, 0, 0]
print(f"Repetición:   {ceros}")

# CUIDADO con la repetición de mutables:
# Cada "fila" es la MISMA lista en memoria
mal = [[0]] * 3    # [[0], [0], [0]] — las 3 sublistas son el MISMO objeto
mal[0].append(1)
print(f"\nRepetición de mutables (MAL): {mal}")  # [[0, 1], [0, 1], [0, 1]]

# Forma correcta:
bien = [[0] for _ in range(3)]  # Cada sublista es un objeto distinto
bien[0].append(1)
print(f"Con comprehension (BIEN):     {bien}")  # [[0, 1], [0], [0]]

# ============================================================
# 2. ACCESO Y SLICING
# ============================================================

print("\n=== ACCESO Y SLICING ===\n")

letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

print(f"letras = {letras}")
print(f"letras[0]    = '{letras[0]}'")      # 'a'
print(f"letras[-1]   = '{letras[-1]}'")     # 'g'
print(f"letras[2:5]  = {letras[2:5]}")      # ['c', 'd', 'e']
print(f"letras[::2]  = {letras[::2]}")      # ['a', 'c', 'e', 'g']
print(f"letras[::-1] = {letras[::-1]}")     # ['g', 'f', 'e', 'd', 'c', 'b', 'a']

# Slicing CREA una nueva lista (copia superficial)
sublista = letras[1:4]
sublista[0] = 'X'
print(f"\nsublista modificada: {sublista}")
print(f"original intacta:   {letras}")

# ============================================================
# 3. MODIFICACIÓN (MUTABILIDAD)
# ============================================================

print("\n=== MODIFICACIÓN ===\n")

frutas = ["manzana", "pera", "uva"]
print(f"Original: {frutas}")

# Asignación por índice
frutas[1] = "naranja"
print(f"Cambiar [1]: {frutas}")

# Asignación por slice (puede cambiar el tamaño)
frutas[1:2] = ["kiwi", "mango", "fresa"]
print(f"Slice [1:2] = 3 elems: {frutas}")

# Eliminar por slice
frutas[2:4] = []
print(f"Eliminar [2:4]: {frutas}")

# ============================================================
# 4. MÉTODOS DE LISTA
# ============================================================

print("\n=== MÉTODOS ===\n")

nums = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"Original: {nums}")

# --- Agregar elementos ---
nums.append(7)             # Agrega al final
print(f"append(7):    {nums}")

nums.insert(0, 0)         # Inserta en posición 0
print(f"insert(0, 0): {nums}")

nums.extend([8, 10])      # Agrega cada elemento del iterable
print(f"extend([8,10]): {nums}")

# --- Eliminar elementos ---
nums.remove(1)             # Elimina la PRIMERA ocurrencia de 1
print(f"remove(1):    {nums}")

ultimo = nums.pop()       # Elimina y devuelve el último
print(f"pop():        {nums} (eliminó {ultimo})")

segundo = nums.pop(1)     # Elimina y devuelve el de posición 1
print(f"pop(1):       {nums} (eliminó {segundo})")

# --- Información ---
print(f"\ncount(5):    {nums.count(5)}")
print(f"index(9):    {nums.index(9)}")    # Posición de la primera ocurrencia
print(f"len(nums):   {len(nums)}")

# --- Ordenamiento ---
nums_copia = nums.copy()
nums_copia.sort()
print(f"\nsort():      {nums_copia}")

nums_copia.sort(reverse=True)
print(f"sort(rev):   {nums_copia}")

# sorted() — devuelve nueva lista, NO modifica la original
nombres = ["Carlos", "ana", "Beto", "diana"]
ordenados = sorted(nombres, key=str.lower)
print(f"\nsorted(key=str.lower): {ordenados}")

# Ordenar por longitud
por_longitud = sorted(nombres, key=len)
print(f"sorted(key=len):       {por_longitud}")

# --- Invertir ---
datos = [1, 2, 3, 4, 5]
datos.reverse()            # In-place
print(f"\nreverse(): {datos}")

# reversed() — devuelve iterador, no modifica
original = [1, 2, 3]
print(f"reversed(): {list(reversed(original))}")
print(f"original:   {original}")  # Sin cambios

# ============================================================
# 5. COPIA DE LISTAS
# ============================================================

print("\n=== COPIAS ===\n")

import copy

original = [[1, 2], [3, 4], [5, 6]]

# Asignación — NO es copia (son el mismo objeto)
alias = original
alias[0][0] = 99
print(f"Alias modifica original: {original}")
original[0][0] = 1  # Restaurar

# Copia superficial (shallow) — copia la lista exterior pero comparte los internos
shallow = original.copy()       # Equivalente a: original[:] o list(original)
shallow[0][0] = 99
print(f"Shallow modifica sub-listas: {original}")
original[0][0] = 1  # Restaurar

# Copia profunda (deep) — copia TODO recursivamente
deep = copy.deepcopy(original)
deep[0][0] = 99
print(f"Deep NO modifica original:  {original}")

# ============================================================
# 6. LISTAS COMO PILAS Y COLAS
# ============================================================

print("\n=== PILAS Y COLAS ===\n")

# --- Pila (LIFO: Last In, First Out) ---
pila = []
pila.append("primero")
pila.append("segundo")
pila.append("tercero")
print(f"Pila: {pila}")
print(f"pop(): {pila.pop()}")  # "tercero"
print(f"Pila después: {pila}")

# --- Cola (FIFO: First In, First Out) ---
# Usar collections.deque es más eficiente que list para colas
from collections import deque
cola = deque(["primero", "segundo", "tercero"])
print(f"\nCola: {list(cola)}")
cola.append("cuarto")          # Agregar al final
print(f"Enqueue: {list(cola)}")
primero = cola.popleft()       # Eliminar del inicio — O(1)
print(f"Dequeue: {list(cola)} (salió '{primero}')")

# ============================================================
# 7. FUNCIONES ÚTILES CON LISTAS
# ============================================================

print("\n=== FUNCIONES ÚTILES ===\n")

nums = [3, 7, 2, 9, 1, 5, 8]

print(f"nums = {nums}")
print(f"min(nums)  = {min(nums)}")
print(f"max(nums)  = {max(nums)}")
print(f"sum(nums)  = {sum(nums)}")
print(f"len(nums)  = {len(nums)}")
print(f"any([0, '', True]) = {any([0, '', True])}")    # True si al menos 1 truthy
print(f"all([1, 'a', True]) = {all([1, 'a', True])}")  # True si todos truthy
print(f"all([1, '', True])  = {all([1, '', True])}")    # False ('') es falsy

# ============================================================
# 8. EJEMPLO INTEGRADOR: PROCESAMIENTO DE DATOS
# ============================================================

print("\n=== EJEMPLO: PROCESAMIENTO DE CALIFICACIONES ===\n")

# Lista de tuplas: (nombre, [calificaciones])
alumnos = [
    ("Ana", [95, 88, 92, 78, 90]),
    ("Luis", [72, 68, 80, 75, 65]),
    ("Eva", [100, 98, 95, 99, 97]),
    ("Carlos", [60, 55, 70, 65, 58]),
]

print(f"{'Alumno':<10} {'Promedio':>8} {'Máx':>5} {'Mín':>5} {'Estado':<12}")
print("-" * 45)

aprobados = []
for nombre, califs in alumnos:
    promedio = sum(califs) / len(califs)
    maximo = max(califs)
    minimo = min(califs)
    estado = "Aprobado" if promedio >= 70 else "Reprobado"

    if promedio >= 70:
        aprobados.append(nombre)

    print(f"{nombre:<10} {promedio:>8.1f} {maximo:>5} {minimo:>5} {estado:<12}")

print(f"\nAprobados: {', '.join(aprobados)}")
print(f"Tasa de aprobación: {len(aprobados)/len(alumnos):.0%}")

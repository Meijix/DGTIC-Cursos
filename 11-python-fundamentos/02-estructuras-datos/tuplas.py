"""
Tuplas en Python
=================
Las tuplas son secuencias INMUTABLES y ordenadas.
Son ideales para datos que no deben cambiar: coordenadas,
registros, claves compuestas de diccionario.

Ejecuta este archivo:
    python tuplas.py
"""

# ============================================================
# 1. CREACIÓN DE TUPLAS
# ============================================================

print("=== CREACIÓN DE TUPLAS ===\n")

# Con paréntesis (forma habitual)
coordenada = (10.5, 20.3)
rgb = (255, 128, 0)
mixta = (1, "hola", 3.14, True)
vacia = ()

# Sin paréntesis (tuple packing)
otra = 1, 2, 3
print(f"Sin paréntesis: {otra}, tipo: {type(otra)}")

# CUIDADO: tupla de UN solo elemento necesita coma
singleton = (42,)     # Esto SÍ es una tupla
no_tupla = (42)       # Esto es solo el int 42 entre paréntesis
print(f"singleton = {singleton}, tipo: {type(singleton)}")
print(f"no_tupla  = {no_tupla}, tipo: {type(no_tupla)}")

# Constructor tuple()
desde_lista = tuple([1, 2, 3])
desde_string = tuple("Python")
desde_range = tuple(range(5))
print(f"\nDesde lista:   {desde_lista}")
print(f"Desde string:  {desde_string}")
print(f"Desde range:   {desde_range}")

# ============================================================
# 2. ACCESO Y SLICING
# ============================================================

print("\n=== ACCESO Y SLICING ===\n")

meses = ("Ene", "Feb", "Mar", "Abr", "May", "Jun",
         "Jul", "Ago", "Sep", "Oct", "Nov", "Dic")

print(f"meses[0]   = {meses[0]}")       # Ene
print(f"meses[-1]  = {meses[-1]}")      # Dic
print(f"meses[3:6] = {meses[3:6]}")     # ('Abr', 'May', 'Jun')
print(f"meses[::3] = {meses[::3]}")     # ('Ene', 'Abr', 'Jul', 'Oct')

# ============================================================
# 3. INMUTABILIDAD
# ============================================================

print("\n=== INMUTABILIDAD ===\n")

punto = (3, 4)
# punto[0] = 5  # TypeError: 'tuple' object does not support item assignment
print(f"Las tuplas no se pueden modificar: {punto}")

# PERO: si una tupla contiene un objeto mutable, ESE objeto sí puede cambiar
tupla_con_lista = (1, [2, 3], 4)
tupla_con_lista[1].append(5)   # Modificamos la LISTA interna
print(f"Tupla con lista mutable: {tupla_con_lista}")
# La tupla sigue siendo la misma (las referencias no cambiaron)

# ============================================================
# 4. DESEMPAQUETADO (UNPACKING)
# ============================================================

print("\n=== DESEMPAQUETADO ===\n")

# Desempaquetado básico — número de variables = número de elementos
x, y = (10, 20)
print(f"x={x}, y={y}")

# Intercambio de valores (usa tuplas internamente)
a, b = 1, 2
a, b = b, a
print(f"Swap: a={a}, b={b}")

# Desempaquetado extendido con * (star unpacking)
primero, *medio, ultimo = (1, 2, 3, 4, 5, 6)
print(f"primero={primero}, medio={medio}, ultimo={ultimo}")
# primero=1, medio=[2, 3, 4, 5], ultimo=6

# Ignorar valores con _
nombre, _, _, ciudad = ("Ana", 25, "F", "CDMX")
print(f"nombre={nombre}, ciudad={ciudad}")

# Desempaquetado en for
puntos = [(1, 2), (3, 4), (5, 6)]
for x, y in puntos:
    print(f"  Punto({x}, {y})")

# ============================================================
# 5. MÉTODOS DE TUPLA
# ============================================================

print("\n=== MÉTODOS ===\n")

# Las tuplas solo tienen 2 métodos (por ser inmutables):
datos = (1, 3, 5, 3, 7, 3, 9)

print(f"datos = {datos}")
print(f"datos.count(3) = {datos.count(3)}")    # 3 (tres ocurrencias)
print(f"datos.index(5) = {datos.index(5)}")    # 2 (primera posición)

# Funciones built-in que funcionan con tuplas:
print(f"len(datos) = {len(datos)}")
print(f"min(datos) = {min(datos)}")
print(f"max(datos) = {max(datos)}")
print(f"sum(datos) = {sum(datos)}")
print(f"sorted(datos) = {sorted(datos)}")  # Devuelve una LISTA

# ============================================================
# 6. TUPLAS COMO CLAVES DE DICCIONARIO
# ============================================================

print("\n=== TUPLAS COMO CLAVES ===\n")

# Las tuplas son hashable (si sus elementos lo son) → pueden ser claves
distancias = {
    ("CDMX", "GDL"): 540,
    ("CDMX", "MTY"): 900,
    ("GDL", "MTY"): 760,
}

for (origen, destino), km in distancias.items():
    print(f"  {origen} → {destino}: {km} km")

# Buscar la distancia entre dos ciudades
ruta = ("CDMX", "GDL")
print(f"\nDistancia {ruta[0]}→{ruta[1]}: {distancias[ruta]} km")

# ============================================================
# 7. NAMED TUPLES
# ============================================================

print("\n=== NAMED TUPLES ===\n")

from collections import namedtuple

# Crear un tipo de tupla con nombres para cada campo
Punto = namedtuple("Punto", ["x", "y"])
Color = namedtuple("Color", "rojo verde azul")  # También acepta string

# Crear instancias
p1 = Punto(3, 4)
p2 = Punto(x=1, y=7)
rojo = Color(255, 0, 0)

# Acceso por nombre O por índice
print(f"p1.x = {p1.x}, p1.y = {p1.y}")
print(f"p1[0] = {p1[0]}, p1[1] = {p1[1]}")
print(f"Color rojo: R={rojo.rojo}, G={rojo.verde}, B={rojo.azul}")

# Distancia entre puntos
import math
distancia = math.sqrt((p2.x - p1.x)**2 + (p2.y - p1.y)**2)
print(f"\nDistancia entre {p1} y {p2}: {distancia:.2f}")

# Convertir a diccionario
print(f"Como dict: {p1._asdict()}")

# Crear una nueva instancia con un campo modificado
p3 = p1._replace(x=10)
print(f"p1._replace(x=10) = {p3}")
print(f"p1 original = {p1}")  # No se modificó

# ============================================================
# 8. TUPLAS vs LISTAS — RENDIMIENTO
# ============================================================

print("\n=== RENDIMIENTO ===\n")

import sys

# Las tuplas son más eficientes en memoria
lista = [1, 2, 3, 4, 5]
tupla = (1, 2, 3, 4, 5)

print(f"Tamaño lista [1..5]: {sys.getsizeof(lista)} bytes")
print(f"Tamaño tupla (1..5): {sys.getsizeof(tupla)} bytes")

# Las tuplas de constantes se crean una sola vez (constant folding)
# y se reutilizan en memoria

# ============================================================
# 9. EJEMPLO INTEGRADOR: REGISTRO DE ESTUDIANTES
# ============================================================

print("\n=== EJEMPLO: REGISTRO DE ESTUDIANTES ===\n")

Estudiante = namedtuple("Estudiante", ["nombre", "matricula", "carrera", "promedio"])

estudiantes = [
    Estudiante("Ana García", "A001", "Computación", 9.2),
    Estudiante("Luis Pérez", "A002", "Matemáticas", 8.5),
    Estudiante("Eva Ruiz", "A003", "Computación", 9.8),
    Estudiante("Carlos López", "A004", "Física", 7.3),
    Estudiante("Diana Soto", "A005", "Computación", 8.9),
]

# Filtrar por carrera
carrera = "Computación"
de_compu = [e for e in estudiantes if e.carrera == carrera]
print(f"Estudiantes de {carrera}:")
for e in de_compu:
    print(f"  {e.matricula} - {e.nombre} (promedio: {e.promedio})")

# Mejor promedio
mejor = max(estudiantes, key=lambda e: e.promedio)
print(f"\nMejor promedio: {mejor.nombre} ({mejor.promedio})")

# Promedio general
promedio_general = sum(e.promedio for e in estudiantes) / len(estudiantes)
print(f"Promedio general: {promedio_general:.2f}")

# Ordenar por promedio descendente
por_promedio = sorted(estudiantes, key=lambda e: e.promedio, reverse=True)
print("\nRanking:")
for i, e in enumerate(por_promedio, 1):
    print(f"  {i}. {e.nombre:<15s} {e.promedio:.1f}")

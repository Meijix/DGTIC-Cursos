"""
Sets (Conjuntos) en Python
============================
Colecciones mutables, no ordenadas y sin duplicados.
Ideales para eliminar duplicados, verificar pertenencia
y operaciones matemáticas de conjuntos.

Ejecuta este archivo:
    python sets.py
"""

# ============================================================
# 1. CREACIÓN DE SETS
# ============================================================

print("=== CREACIÓN ===\n")

# Literal con llaves
vocales = {"a", "e", "i", "o", "u"}
print(f"Vocales: {vocales}")

# Los duplicados se eliminan automáticamente
con_duplicados = {1, 2, 3, 2, 1, 4, 3}
print(f"Con duplicados: {con_duplicados}")  # {1, 2, 3, 4}

# CUIDADO: {} crea un diccionario VACÍO, no un set
vacio_dict = {}         # dict
vacio_set = set()       # set
print(f"\ntype({{}}):    {type(vacio_dict)}")
print(f"type(set()): {type(vacio_set)}")

# Constructor set()
desde_lista = set([1, 2, 3, 2, 1])
desde_string = set("mississippi")    # Letras únicas
desde_range = set(range(5))
print(f"\nDesde lista:  {desde_lista}")
print(f"Desde string: {desde_string}")
print(f"Desde range:  {desde_range}")

# ============================================================
# 2. OPERACIONES BÁSICAS
# ============================================================

print("\n=== OPERACIONES BÁSICAS ===\n")

colores = {"rojo", "verde", "azul"}
print(f"colores = {colores}")

# Agregar un elemento
colores.add("amarillo")
print(f"add('amarillo'): {colores}")

# Agregar un elemento que ya existe — NO error, NO duplica
colores.add("rojo")
print(f"add('rojo'):     {colores}")

# Eliminar un elemento
colores.discard("verde")  # No lanza error si no existe
print(f"discard('verde'): {colores}")

colores.remove("azul")    # Lanza KeyError si no existe
print(f"remove('azul'):   {colores}")

# colores.remove("xyz")   # KeyError

# pop() — elimina y devuelve un elemento ARBITRARIO
eliminado = colores.pop()
print(f"pop():            {colores} (eliminó '{eliminado}')")

# Agregar múltiples elementos
colores.update(["negro", "blanco", "gris"])
print(f"update([...]):    {colores}")

# Verificar pertenencia — O(1), muy rápido
print(f"\n'negro' in colores: {'negro' in colores}")

# Longitud
print(f"len(colores): {len(colores)}")

# ============================================================
# 3. OPERACIONES DE CONJUNTOS
# ============================================================

print("\n=== OPERACIONES DE CONJUNTOS ===\n")

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print(f"A = {A}")
print(f"B = {B}")

# --- Unión: todos los elementos de ambos ---
print(f"\nA | B (unión):              {A | B}")
print(f"A.union(B):                 {A.union(B)}")

# --- Intersección: solo los comunes ---
print(f"\nA & B (intersección):       {A & B}")
print(f"A.intersection(B):          {A.intersection(B)}")

# --- Diferencia: en A pero no en B ---
print(f"\nA - B (diferencia):         {A - B}")
print(f"A.difference(B):            {A.difference(B)}")
print(f"B - A:                      {B - A}")

# --- Diferencia simétrica: en uno u otro pero no en ambos ---
print(f"\nA ^ B (dif. simétrica):     {A ^ B}")
print(f"A.symmetric_difference(B):  {A.symmetric_difference(B)}")

# ============================================================
# 4. COMPARACIÓN DE CONJUNTOS
# ============================================================

print("\n=== COMPARACIÓN ===\n")

X = {1, 2, 3}
Y = {1, 2, 3, 4, 5}
Z = {1, 2, 3}

# Subconjunto
print(f"X = {X}")
print(f"Y = {Y}")
print(f"Z = {Z}")
print(f"\nX <= Y (subconjunto):     {X <= Y}")     # True
print(f"X.issubset(Y):            {X.issubset(Y)}")

# Superconjunto
print(f"Y >= X (superconjunto):   {Y >= X}")       # True
print(f"Y.issuperset(X):         {Y.issuperset(X)}")

# Igualdad (orden no importa)
print(f"X == Z:                   {X == Z}")        # True

# Subconjunto propio (< estricto)
print(f"X < Y (subconjunto propio): {X < Y}")       # True
print(f"X < Z (subconjunto propio): {X < Z}")       # False (son iguales)

# Disjuntos (sin elementos en común)
P = {1, 2}
Q = {3, 4}
print(f"\n{P}.isdisjoint({Q}): {P.isdisjoint(Q)}")  # True

# ============================================================
# 5. OPERACIONES IN-PLACE
# ============================================================

print("\n=== OPERACIONES IN-PLACE ===\n")

s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
print(f"s1 = {s1}, s2 = {s2}")

# intersection_update — conserva solo los comunes
s1_copia = s1.copy()
s1_copia.intersection_update(s2)  # Equivale a: s1_copia &= s2
print(f"s1 &= s2: {s1_copia}")

# difference_update — elimina los que están en s2
s1_copia = s1.copy()
s1_copia.difference_update(s2)    # Equivale a: s1_copia -= s2
print(f"s1 -= s2: {s1_copia}")

# symmetric_difference_update
s1_copia = s1.copy()
s1_copia.symmetric_difference_update(s2)  # Equivale a: s1_copia ^= s2
print(f"s1 ^= s2: {s1_copia}")

# ============================================================
# 6. FROZENSET — SET INMUTABLE
# ============================================================

print("\n=== FROZENSET ===\n")

# frozenset es un set inmutable — puede ser clave de dict o elemento de otro set
inmutable = frozenset([1, 2, 3, 4])
print(f"frozenset: {inmutable}")

# inmutable.add(5)  # AttributeError — no se puede modificar

# Uso como clave de diccionario
permisos = {
    frozenset({"leer", "escribir"}): "Editor",
    frozenset({"leer"}): "Lector",
    frozenset({"leer", "escribir", "admin"}): "Administrador",
}

mis_permisos = frozenset({"leer", "escribir"})
print(f"Mi rol: {permisos[mis_permisos]}")

# Uso como elemento de un set de sets
conjuntos = {frozenset({1, 2}), frozenset({3, 4}), frozenset({1, 2})}
print(f"Set de frozensets: {conjuntos}")  # Solo 2 (el duplicado se elimina)

# ============================================================
# 7. PATRONES COMUNES
# ============================================================

print("\n=== PATRONES COMUNES ===\n")

# --- Eliminar duplicados de una lista (preservando orden) ---
lista = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

# Método simple (pierde orden en Python < 3.7)
sin_dup_set = list(set(lista))
print(f"set() simple: {sin_dup_set}")

# Preservando orden (funciona en todas las versiones)
vistos = set()
sin_dup_orden = []
for x in lista:
    if x not in vistos:
        vistos.add(x)
        sin_dup_orden.append(x)
print(f"Preservando orden: {sin_dup_orden}")

# Con dict.fromkeys (truco elegante, Python 3.7+)
sin_dup_dict = list(dict.fromkeys(lista))
print(f"dict.fromkeys: {sin_dup_dict}")

# --- Verificar si una lista tiene duplicados ---
tiene_dup = len(lista) != len(set(lista))
print(f"\n¿Lista tiene duplicados? {tiene_dup}")

# --- Encontrar elementos comunes entre listas ---
lista_a = [1, 2, 3, 4, 5, 6]
lista_b = [4, 5, 6, 7, 8, 9]
comunes = set(lista_a) & set(lista_b)
print(f"Elementos comunes: {comunes}")

# --- Anagramas ---
def son_anagramas(s1, s2):
    """Verifica si dos strings son anagramas."""
    return sorted(s1.lower().replace(" ", "")) == sorted(s2.lower().replace(" ", ""))

print(f"\n¿'listen' y 'silent' son anagramas? {son_anagramas('listen', 'silent')}")
print(f"¿'hola' y 'algo' son anagramas? {son_anagramas('hola', 'algo')}")

# ============================================================
# 8. SET COMPREHENSION
# ============================================================

print("\n=== SET COMPREHENSION ===\n")

# Letras únicas en una frase
frase = "el murcielago tiene todas las vocales"
letras_unicas = {c for c in frase if c.isalpha()}
print(f"Letras únicas: {sorted(letras_unicas)}")

vocales_encontradas = {c for c in frase.lower() if c in "aeiou"}
print(f"Vocales encontradas: {vocales_encontradas}")

# Números con alguna propiedad
multiplos_3_o_5 = {x for x in range(1, 31) if x % 3 == 0 or x % 5 == 0}
print(f"Múltiplos de 3 o 5 (1-30): {sorted(multiplos_3_o_5)}")

# ============================================================
# 9. EJEMPLO INTEGRADOR: ANÁLISIS DE TEXTO
# ============================================================

print("\n=== EJEMPLO: ANÁLISIS DE TEXTO ===\n")

texto_a = "python es un lenguaje de programación interpretado"
texto_b = "javascript es un lenguaje de programación web"

palabras_a = set(texto_a.split())
palabras_b = set(texto_b.split())

print(f"Texto A: \"{texto_a}\"")
print(f"Texto B: \"{texto_b}\"")

print(f"\nPalabras en común:         {palabras_a & palabras_b}")
print(f"Solo en A:                 {palabras_a - palabras_b}")
print(f"Solo en B:                 {palabras_b - palabras_a}")
print(f"En uno u otro (no ambos): {palabras_a ^ palabras_b}")
print(f"Todas las palabras:        {palabras_a | palabras_b}")

similitud = len(palabras_a & palabras_b) / len(palabras_a | palabras_b)
print(f"\nSimilitud (Jaccard): {similitud:.2%}")

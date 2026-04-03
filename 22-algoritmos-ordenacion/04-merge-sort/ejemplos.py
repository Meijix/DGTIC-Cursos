"""
Merge Sort (Ordenamiento por Mezcla)

Algoritmo de tipo divide y venceras. Divide el arreglo en dos
mitades, ordena cada mitad recursivamente y luego mezcla las
dos mitades ordenadas. Es estable y garantiza O(n log n).

Complejidad:
  - Peor caso:    O(n log n)
  - Mejor caso:   O(n log n)
  - Caso promedio: O(n log n)
  - Espacio:      O(n)
"""

import time
import random


# --- Funcion de mezcla (merge) ---

def mezclar(izquierda, derecha):
    """Mezcla dos listas ordenadas en una sola lista ordenada."""
    resultado = []
    i = j = 0

    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] <= derecha[j]:  # <= para mantener estabilidad
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1

    # Agregar los elementos restantes
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado


# --- Merge sort recursivo ---

def merge_sort(arreglo):
    """Merge sort recursivo clasico."""
    if len(arreglo) <= 1:
        return arreglo

    medio = len(arreglo) // 2
    izquierda = merge_sort(arreglo[:medio])
    derecha = merge_sort(arreglo[medio:])

    return mezclar(izquierda, derecha)


# --- Merge sort con impresion de pasos ---

def merge_sort_verbose(arreglo, nivel=0):
    """Merge sort que imprime los pasos de division y mezcla."""
    sangria = "    " * nivel

    if len(arreglo) <= 1:
        return arreglo

    medio = len(arreglo) // 2
    print(f"{sangria}Dividir: {arreglo} -> {arreglo[:medio]} | {arreglo[medio:]}")

    izquierda = merge_sort_verbose(arreglo[:medio], nivel + 1)
    derecha = merge_sort_verbose(arreglo[medio:], nivel + 1)

    resultado = mezclar(izquierda, derecha)
    print(f"{sangria}Mezclar: {izquierda} + {derecha} -> {resultado}")

    return resultado


# --- Demostracion de estabilidad ---

def merge_sort_estable(arreglo_tuplas):
    """Merge sort para tuplas (valor, indice_original).
    Demuestra estabilidad: elementos con el mismo valor mantienen
    su orden relativo original."""
    if len(arreglo_tuplas) <= 1:
        return arreglo_tuplas

    medio = len(arreglo_tuplas) // 2
    izq = merge_sort_estable(arreglo_tuplas[:medio])
    der = merge_sort_estable(arreglo_tuplas[medio:])

    resultado = []
    i = j = 0
    while i < len(izq) and j < len(der):
        # Comparar solo por el primer elemento (valor)
        if izq[i][0] <= der[j][0]:
            resultado.append(izq[i])
            i += 1
        else:
            resultado.append(der[j])
            j += 1
    resultado.extend(izq[i:])
    resultado.extend(der[j:])
    return resultado


# --- Merge sort iterativo (bottom-up) ---

def merge_sort_iterativo(arreglo):
    """Version iterativa (bottom-up) de merge sort.
    Comienza mezclando pares de 1, luego de 2, 4, 8, etc."""
    arr = arreglo.copy()
    n = len(arr)
    tamano = 1  # Tamano de los subarreglos a mezclar

    while tamano < n:
        for inicio in range(0, n, tamano * 2):
            medio = min(inicio + tamano, n)
            fin = min(inicio + tamano * 2, n)
            # Mezclar arr[inicio:medio] con arr[medio:fin]
            izq = arr[inicio:medio]
            der = arr[medio:fin]
            arr[inicio:fin] = mezclar(izq, der)
        tamano *= 2

    return arr


# ============================================================
# Ejecucion principal
# ============================================================

if __name__ == "__main__":
    print("=" * 60)
    print("  MERGE SORT - Ordenamiento por Mezcla")
    print("=" * 60)

    # 1. Paso a paso con arreglo pequeno
    print("\n--- Division y mezcla paso a paso ---")
    datos = [38, 27, 43, 3, 9, 82, 10]
    print(f"  Arreglo original: {datos}\n")
    resultado = merge_sort_verbose(datos)
    print(f"\n  Resultado: {resultado}")

    # 2. Demostracion de estabilidad
    print("\n--- Demostracion de estabilidad ---")
    # Alumnos con la misma calificacion deben mantener su orden original
    alumnos = [("Ana", 85), ("Luis", 90), ("Maria", 85),
               ("Carlos", 70), ("Sofia", 90), ("Pedro", 85)]
    print(f"  Alumnos originales:")
    for i, (nombre, cal) in enumerate(alumnos):
        print(f"    [{i}] {nombre}: {cal}")

    # Crear tuplas (calificacion, indice_original, nombre)
    tuplas = [(cal, i, nombre) for i, (nombre, cal) in enumerate(alumnos)]
    ordenado = merge_sort_estable(tuplas)

    print(f"\n  Ordenados por calificacion (estable):")
    for cal, idx_orig, nombre in ordenado:
        print(f"    {nombre}: {cal}  (posicion original: {idx_orig})")
    print("  Nota: Ana, Maria y Pedro (85) mantienen su orden relativo")

    # 3. Version iterativa
    print("\n--- Version iterativa (bottom-up) ---")
    datos_it = [5, 2, 8, 1, 9, 3, 7, 4, 6]
    resultado_it = merge_sort_iterativo(datos_it)
    print(f"  Entrada:  {datos_it}")
    print(f"  Resultado: {resultado_it}")

    # Verificar que ambas versiones dan el mismo resultado
    datos_ver = [random.randint(1, 100) for _ in range(15)]
    r_rec = merge_sort(datos_ver)
    r_it = merge_sort_iterativo(datos_ver)
    print(f"\n  Verificacion recursivo == iterativo: {r_rec == r_it}")

    # 4. Comparacion de rendimiento
    print("\n--- Comparacion de rendimiento ---")
    tamanos = [5000, 20000, 50000]
    for n in tamanos:
        datos_rand = [random.randint(0, n) for _ in range(n)]

        inicio = time.time()
        merge_sort(datos_rand)
        t_rec = time.time() - inicio

        inicio = time.time()
        merge_sort_iterativo(datos_rand)
        t_it = time.time() - inicio

        inicio = time.time()
        sorted(datos_rand)
        t_builtin = time.time() - inicio

        print(f"  n={n:>6}: recursivo={t_rec:.4f}s | "
              f"iterativo={t_it:.4f}s | "
              f"sorted()={t_builtin:.6f}s")

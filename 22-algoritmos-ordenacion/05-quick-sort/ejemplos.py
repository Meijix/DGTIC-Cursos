"""
Quick Sort (Ordenamiento Rapido)

Algoritmo de tipo divide y venceras. Selecciona un elemento como
pivote y particiona el arreglo de modo que los elementos menores
queden a la izquierda y los mayores a la derecha. Luego ordena
recursivamente cada particion.

Complejidad:
  - Peor caso:    O(n^2)  (pivote siempre es el minimo o maximo)
  - Mejor caso:   O(n log n)
  - Caso promedio: O(n log n)
  - Espacio:      O(log n) promedio (por la pila de recursion)
"""

import time
import random


# --- Particion de Lomuto (pivote al final) ---

def particion_lomuto(arr, bajo, alto):
    """Esquema de Lomuto: pivote es el ultimo elemento."""
    pivote = arr[alto]
    i = bajo - 1  # Indice del ultimo elemento menor que el pivote

    for j in range(bajo, alto):
        if arr[j] <= pivote:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[alto] = arr[alto], arr[i + 1]
    return i + 1


def quick_sort_lomuto(arr, bajo=None, alto=None):
    """Quick sort usando particion de Lomuto."""
    if bajo is None:
        arr = arr.copy()
        bajo, alto = 0, len(arr) - 1
        quick_sort_lomuto(arr, bajo, alto)
        return arr

    if bajo < alto:
        pi = particion_lomuto(arr, bajo, alto)
        quick_sort_lomuto(arr, bajo, pi - 1)
        quick_sort_lomuto(arr, pi + 1, alto)


# --- Particion de Hoare (pivote al inicio) ---

def particion_hoare(arr, bajo, alto):
    """Esquema de Hoare: pivote es el primer elemento.
    Dos punteros se mueven hacia el centro."""
    pivote = arr[bajo]
    i = bajo - 1
    j = alto + 1

    while True:
        i += 1
        while arr[i] < pivote:
            i += 1
        j -= 1
        while arr[j] > pivote:
            j -= 1
        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]


def quick_sort_hoare(arr, bajo=None, alto=None):
    """Quick sort usando particion de Hoare."""
    if bajo is None:
        arr = arr.copy()
        bajo, alto = 0, len(arr) - 1
        quick_sort_hoare(arr, bajo, alto)
        return arr

    if bajo < alto:
        pi = particion_hoare(arr, bajo, alto)
        quick_sort_hoare(arr, bajo, pi)
        quick_sort_hoare(arr, pi + 1, alto)


# --- Seleccion de pivote: mediana de tres ---

def mediana_de_tres(arr, bajo, alto):
    """Selecciona la mediana entre el primero, medio y ultimo
    y la coloca al final para usar con Lomuto."""
    medio = (bajo + alto) // 2
    # Ordenar los tres: arr[bajo], arr[medio], arr[alto]
    if arr[bajo] > arr[medio]:
        arr[bajo], arr[medio] = arr[medio], arr[bajo]
    if arr[bajo] > arr[alto]:
        arr[bajo], arr[alto] = arr[alto], arr[bajo]
    if arr[medio] > arr[alto]:
        arr[medio], arr[alto] = arr[alto], arr[medio]
    # La mediana esta en arr[medio], moverla al final
    arr[medio], arr[alto] = arr[alto], arr[medio]
    return arr[alto]


# --- Quick sort aleatorizado ---

def quick_sort_aleatorio(arr, bajo=None, alto=None):
    """Quick sort con pivote aleatorio (evita peor caso)."""
    if bajo is None:
        arr = arr.copy()
        bajo, alto = 0, len(arr) - 1
        quick_sort_aleatorio(arr, bajo, alto)
        return arr

    if bajo < alto:
        # Elegir pivote aleatorio y moverlo al final
        rand_idx = random.randint(bajo, alto)
        arr[rand_idx], arr[alto] = arr[alto], arr[rand_idx]
        pi = particion_lomuto(arr, bajo, alto)
        quick_sort_aleatorio(arr, bajo, pi - 1)
        quick_sort_aleatorio(arr, pi + 1, alto)


# --- Demostracion paso a paso de la particion ---

def particion_verbose(arreglo):
    """Muestra paso a paso como funciona la particion de Lomuto."""
    arr = arreglo.copy()
    alto = len(arr) - 1
    pivote = arr[alto]
    print(f"  Arreglo: {arr}")
    print(f"  Pivote (ultimo elemento): {pivote}")
    print()

    i = -1
    for j in range(alto):
        comp = "<=" if arr[j] <= pivote else ">"
        if arr[j] <= pivote:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            print(f"    j={j}: arr[{j}]={arreglo[j]} {comp} {pivote} "
                  f"-> intercambiar arr[{i}] y arr[{j}] -> {arr}")
        else:
            print(f"    j={j}: arr[{j}]={arreglo[j]} {comp} {pivote} "
                  f"-> no mover -> {arr}")

    arr[i + 1], arr[alto] = arr[alto], arr[i + 1]
    print(f"\n  Colocar pivote en posicion {i + 1}: {arr}")
    print(f"  Menores: {arr[:i+1]} | Pivote: [{arr[i+1]}] | Mayores: {arr[i+2:]}")
    return arr


# ============================================================
# Ejecucion principal
# ============================================================

if __name__ == "__main__":
    print("=" * 60)
    print("  QUICK SORT - Ordenamiento Rapido")
    print("=" * 60)

    # 1. Paso a paso de la particion
    print("\n--- Particion de Lomuto paso a paso ---")
    particion_verbose([10, 80, 30, 90, 40, 50, 70])

    # 2. Comparacion Lomuto vs Hoare
    print("\n--- Lomuto vs Hoare ---")
    datos = [random.randint(1, 100) for _ in range(12)]
    res_lomuto = quick_sort_lomuto(datos)
    res_hoare = quick_sort_hoare(datos)
    print(f"  Entrada:  {datos}")
    print(f"  Lomuto:   {res_lomuto}")
    print(f"  Hoare:    {res_hoare}")
    print(f"  Iguales:  {res_lomuto == res_hoare}")

    # 3. Estrategias de seleccion de pivote
    print("\n--- Estrategias de seleccion de pivote ---")
    muestra = [8, 3, 7, 1, 5, 9, 2, 6, 4]
    print(f"  Arreglo: {muestra}")
    print(f"  Pivote = primero:          {muestra[0]}")
    print(f"  Pivote = ultimo:           {muestra[-1]}")
    m = muestra.copy()
    med = mediana_de_tres(m, 0, len(m) - 1)
    print(f"  Pivote = mediana de tres:  {med}  "
          f"(entre {muestra[0]}, {muestra[len(muestra)//2]}, {muestra[-1]})")

    # 4. Quicksort aleatorizado
    print("\n--- Quick sort aleatorizado ---")
    # Caso que seria O(n^2) con pivote fijo: arreglo ya ordenado
    ordenado = list(range(20))
    resultado = quick_sort_aleatorio(ordenado)
    print(f"  Entrada (ya ordenada): {ordenado}")
    print(f"  Resultado: {resultado}")

    # 5. Comparacion de rendimiento
    print("\n--- Comparacion de rendimiento ---")
    tamanos = [5000, 20000, 50000]
    for n in tamanos:
        datos_rand = [random.randint(0, n) for _ in range(n)]

        inicio = time.time()
        quick_sort_lomuto(datos_rand)
        t_lom = time.time() - inicio

        inicio = time.time()
        quick_sort_hoare(datos_rand)
        t_hoa = time.time() - inicio

        inicio = time.time()
        quick_sort_aleatorio(datos_rand)
        t_rand = time.time() - inicio

        print(f"  n={n:>6}: Lomuto={t_lom:.4f}s | "
              f"Hoare={t_hoa:.4f}s | "
              f"Aleatorio={t_rand:.4f}s")

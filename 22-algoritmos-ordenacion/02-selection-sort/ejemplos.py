"""
Selection Sort (Ordenamiento por Seleccion)

Algoritmo que divide el arreglo en dos partes: la parte ordenada
(al inicio) y la parte sin ordenar. En cada iteracion, busca el
elemento minimo de la parte sin ordenar y lo coloca al final de
la parte ordenada.

Complejidad:
  - Peor caso:    O(n^2)
  - Mejor caso:   O(n^2)  (siempre recorre todo)
  - Caso promedio: O(n^2)
  - Espacio:      O(1)
"""

import time
import random


# --- Implementacion con contador de comparaciones ---

def selection_sort(arreglo):
    """Selection sort que cuenta comparaciones e intercambios."""
    arr = arreglo.copy()
    n = len(arr)
    comparaciones = 0
    intercambios = 0

    for i in range(n - 1):
        # Buscar el indice del minimo en la parte sin ordenar
        indice_min = i
        for j in range(i + 1, n):
            comparaciones += 1
            if arr[j] < arr[indice_min]:
                indice_min = j

        # Intercambiar solo si el minimo no esta ya en su posicion
        if indice_min != i:
            arr[i], arr[indice_min] = arr[indice_min], arr[i]
            intercambios += 1

    return arr, comparaciones, intercambios


# --- Demostracion paso a paso ---

def selection_sort_paso_a_paso(arreglo):
    """Muestra cada paso: busqueda del minimo e intercambio."""
    arr = arreglo.copy()
    n = len(arr)

    print(f"  Arreglo inicial: {arr}")
    print()

    for i in range(n - 1):
        indice_min = i
        # Mostrar la parte ordenada y la parte sin ordenar
        parte_ordenada = arr[:i]
        parte_sin_ordenar = arr[i:]
        print(f"  Pasada {i + 1}:")
        print(f"    Ordenado: {parte_ordenada}  |  Sin ordenar: {parte_sin_ordenar}")

        # Buscar el minimo
        for j in range(i + 1, n):
            if arr[j] < arr[indice_min]:
                indice_min = j

        minimo = arr[indice_min]
        print(f"    Minimo encontrado: {minimo} (posicion {indice_min})")

        if indice_min != i:
            print(f"    Intercambio: {arr[i]} <-> {arr[indice_min]}")
            arr[i], arr[indice_min] = arr[indice_min], arr[i]
        else:
            print(f"    {arr[i]} ya esta en su posicion correcta")

        print(f"    Estado: {arr}")
        print()

    print(f"  Resultado final: {arr}")
    return arr


# --- Visualizacion con barras ---

def selection_sort_visual(arreglo):
    """Muestra cada pasada con una representacion visual de barras."""
    arr = arreglo.copy()
    n = len(arr)

    print(f"  Valores: {arr}")
    for i in range(n - 1):
        indice_min = i
        for j in range(i + 1, n):
            if arr[j] < arr[indice_min]:
                indice_min = j
        if indice_min != i:
            arr[i], arr[indice_min] = arr[indice_min], arr[i]
        # Representacion con barras
        barras = "  "
        for k, val in enumerate(arr):
            marca = "*" if k < i + 1 else " "
            barras += f"[{val:>2}]{marca} "
        print(f"  Pasada {i + 1}: {barras}  (* = posicion final)")
    print()


# ============================================================
# Ejecucion principal
# ============================================================

if __name__ == "__main__":
    print("=" * 60)
    print("  SELECTION SORT - Ordenamiento por Seleccion")
    print("=" * 60)

    # 1. Paso a paso detallado
    print("\n--- Paso a paso detallado ---")
    datos = [29, 10, 14, 37, 13]
    selection_sort_paso_a_paso(datos)

    # 2. Visualizacion con barras
    print("\n--- Visualizacion de pasadas ---")
    datos_vis = [5, 3, 8, 1, 9, 2, 7]
    selection_sort_visual(datos_vis)

    # 3. Conteo de comparaciones
    print("--- Conteo de operaciones ---")
    tamanos_demo = [10, 50, 100]
    for n in tamanos_demo:
        datos_aleatorios = [random.randint(1, 1000) for _ in range(n)]
        _, comps, inters = selection_sort(datos_aleatorios)
        # Para selection sort, comparaciones siempre = n*(n-1)/2
        teorico = n * (n - 1) // 2
        print(f"  n={n:>3}: comparaciones={comps:>5} "
              f"(teorico={teorico:>5}), intercambios={inters}")

    # 4. Selection sort siempre hace las mismas comparaciones
    print("\n--- Mismo numero de comparaciones sin importar el orden ---")
    n = 20
    casos = {
        "Aleatorio": [random.randint(1, 100) for _ in range(n)],
        "Ordenado":  list(range(n)),
        "Invertido": list(range(n, 0, -1)),
    }
    for nombre, datos in casos.items():
        _, comps, inters = selection_sort(datos)
        print(f"  {nombre:>10}: comparaciones={comps}, intercambios={inters}")

    # 5. Comparacion de rendimiento
    print("\n--- Comparacion de rendimiento ---")
    tamanos = [1000, 3000, 5000]
    for n in tamanos:
        datos_rand = [random.randint(0, n) for _ in range(n)]
        inicio = time.time()
        selection_sort(datos_rand)
        t = time.time() - inicio
        print(f"  n={n:>5}: {t:.4f}s")

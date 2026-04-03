"""
Bubble Sort (Ordenamiento Burbuja)

Algoritmo de ordenamiento que recorre repetidamente la lista,
compara elementos adyacentes y los intercambia si estan en el
orden incorrecto. El proceso se repite hasta que no se necesitan
mas intercambios.

Complejidad:
  - Peor caso:    O(n^2)
  - Mejor caso:   O(n)   (version optimizada, arreglo ya ordenado)
  - Caso promedio: O(n^2)
  - Espacio:      O(1)
"""

import time
import random


# --- Implementacion basica con contador de intercambios ---

def bubble_sort_basico(arreglo):
    """Bubble sort basico: siempre hace n-1 pasadas."""
    arr = arreglo.copy()
    n = len(arr)
    intercambios = 0

    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                intercambios += 1

    return arr, intercambios


# --- Version optimizada con terminacion temprana ---

def bubble_sort_optimizado(arreglo):
    """Bubble sort con bandera: se detiene si no hubo intercambios."""
    arr = arreglo.copy()
    n = len(arr)
    intercambios = 0
    pasadas = 0

    for i in range(n - 1):
        hubo_intercambio = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                intercambios += 1
                hubo_intercambio = True
        pasadas += 1
        # Si no hubo intercambios, el arreglo ya esta ordenado
        if not hubo_intercambio:
            break

    return arr, intercambios, pasadas


# --- Demostracion paso a paso ---

def bubble_sort_paso_a_paso(arreglo):
    """Muestra cada paso del algoritmo."""
    arr = arreglo.copy()
    n = len(arr)

    print(f"  Arreglo inicial: {arr}")
    for i in range(n - 1):
        hubo_intercambio = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                hubo_intercambio = True
        # Mostrar el estado despues de cada pasada
        # Los ultimos i+1 elementos ya estan en su posicion final
        fijos = arr[n - 1 - i:]
        por_ordenar = arr[:n - 1 - i]
        print(f"  Pasada {i + 1}: {por_ordenar} | {fijos}  (| separa los ya ordenados)")
        if not hubo_intercambio:
            print("  -> Sin intercambios, terminacion temprana!")
            break

    print(f"  Resultado: {arr}")
    return arr


# ============================================================
# Ejecucion principal
# ============================================================

if __name__ == "__main__":
    print("=" * 60)
    print("  BUBBLE SORT - Ordenamiento Burbuja")
    print("=" * 60)

    # 1. Paso a paso con arreglo pequeno
    print("\n--- Paso a paso ---")
    datos = [64, 34, 25, 12, 22, 11, 90]
    bubble_sort_paso_a_paso(datos)

    # 2. Comparacion basico vs optimizado con arreglo ya ordenado
    print("\n--- Basico vs Optimizado (arreglo ya ordenado) ---")
    ordenado = list(range(1, 11))
    _, intercambios_basico = bubble_sort_basico(ordenado)
    _, intercambios_opt, pasadas_opt = bubble_sort_optimizado(ordenado)
    print(f"  Arreglo: {ordenado}")
    print(f"  Basico:     {intercambios_basico} intercambios")
    print(f"  Optimizado: {intercambios_opt} intercambios, {pasadas_opt} pasada(s)")

    # 3. Con arreglo aleatorio
    print("\n--- Basico vs Optimizado (arreglo aleatorio) ---")
    aleatorio = [random.randint(1, 100) for _ in range(10)]
    res_basico, inter_basico = bubble_sort_basico(aleatorio)
    res_opt, inter_opt, pasadas = bubble_sort_optimizado(aleatorio)
    print(f"  Arreglo:    {aleatorio}")
    print(f"  Basico:     {inter_basico} intercambios")
    print(f"  Optimizado: {inter_opt} intercambios, {pasadas} pasada(s)")
    print(f"  Resultado:  {res_opt}")

    # 4. Comparacion de rendimiento
    print("\n--- Comparacion de rendimiento ---")
    tamanos = [1000, 3000, 5000]
    for n in tamanos:
        datos_rand = [random.randint(0, n) for _ in range(n)]
        datos_ord = list(range(n))

        # Medir con arreglo aleatorio
        inicio = time.time()
        bubble_sort_basico(datos_rand)
        t_basico = time.time() - inicio

        inicio = time.time()
        bubble_sort_optimizado(datos_rand)
        t_opt_rand = time.time() - inicio

        # Medir con arreglo ya ordenado
        inicio = time.time()
        bubble_sort_optimizado(datos_ord)
        t_opt_ord = time.time() - inicio

        print(f"  n={n:>5}: basico={t_basico:.4f}s | "
              f"optimizado(aleatorio)={t_opt_rand:.4f}s | "
              f"optimizado(ordenado)={t_opt_ord:.6f}s")

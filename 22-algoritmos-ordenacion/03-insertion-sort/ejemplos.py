"""
Insertion Sort (Ordenamiento por Insercion)

Algoritmo que construye la lista ordenada de izquierda a derecha.
Para cada elemento, lo inserta en la posicion correcta dentro de
la parte ya ordenada, desplazando los elementos mayores a la derecha.

Es especialmente eficiente para arreglos casi ordenados.

Complejidad:
  - Peor caso:    O(n^2)  (arreglo invertido)
  - Mejor caso:   O(n)    (arreglo ya ordenado)
  - Caso promedio: O(n^2)
  - Espacio:      O(1)
"""

import time
import random
from bisect import insort_left


# --- Implementacion clasica ---

def insertion_sort(arreglo):
    """Insertion sort clasico con conteo de desplazamientos."""
    arr = arreglo.copy()
    n = len(arr)
    desplazamientos = 0

    for i in range(1, n):
        clave = arr[i]
        j = i - 1
        # Desplazar elementos mayores que la clave hacia la derecha
        while j >= 0 and arr[j] > clave:
            arr[j + 1] = arr[j]
            j -= 1
            desplazamientos += 1
        arr[j + 1] = clave

    return arr, desplazamientos


# --- Paso a paso ---

def insertion_sort_paso_a_paso(arreglo):
    """Muestra el proceso de insercion en cada paso."""
    arr = arreglo.copy()
    n = len(arr)

    print(f"  Arreglo inicial: {arr}")
    print()

    for i in range(1, n):
        clave = arr[i]
        j = i - 1
        posiciones_desplazadas = []

        while j >= 0 and arr[j] > clave:
            arr[j + 1] = arr[j]
            posiciones_desplazadas.append(arr[j + 1])
            j -= 1

        arr[j + 1] = clave

        print(f"  Paso {i}: insertar {clave}")
        if posiciones_desplazadas:
            print(f"    Desplazados a la derecha: {posiciones_desplazadas}")
        else:
            print(f"    Sin desplazamientos (ya esta en posicion)")
        print(f"    Resultado: {arr}")
        # Marcar la parte ordenada
        parte_ord = arr[:i + 1]
        parte_rest = arr[i + 1:]
        print(f"    Ordenado hasta ahora: {parte_ord}  |  Resto: {parte_rest}")
        print()

    return arr


# --- Insertion sort binario ---

def binary_insertion_sort(arreglo):
    """Usa busqueda binaria para encontrar la posicion de insercion.
    Reduce comparaciones a O(n log n), pero desplazamientos siguen O(n^2)."""
    arr = arreglo.copy()
    n = len(arr)
    comparaciones = 0

    for i in range(1, n):
        clave = arr[i]
        # Busqueda binaria en arr[0..i-1]
        izq, der = 0, i - 1
        while izq <= der:
            medio = (izq + der) // 2
            comparaciones += 1
            if arr[medio] > clave:
                der = medio - 1
            else:
                izq = medio + 1

        # Desplazar elementos para hacer espacio
        for j in range(i, izq, -1):
            arr[j] = arr[j - 1]
        arr[izq] = clave

    return arr, comparaciones


# ============================================================
# Ejecucion principal
# ============================================================

if __name__ == "__main__":
    print("=" * 60)
    print("  INSERTION SORT - Ordenamiento por Insercion")
    print("=" * 60)

    # 1. Paso a paso
    print("\n--- Paso a paso ---")
    datos = [12, 11, 13, 5, 6]
    insertion_sort_paso_a_paso(datos)

    # 2. Eficiencia con arreglos casi ordenados
    print("--- Eficiencia con arreglos casi ordenados ---")
    n = 20
    casi_ordenado = list(range(n))
    # Intercambiar solo 2 pares
    casi_ordenado[3], casi_ordenado[4] = casi_ordenado[4], casi_ordenado[3]
    casi_ordenado[15], casi_ordenado[16] = casi_ordenado[16], casi_ordenado[15]

    aleatorio = [random.randint(0, 100) for _ in range(n)]
    invertido = list(range(n, 0, -1))

    for nombre, datos in [("Casi ordenado", casi_ordenado),
                          ("Aleatorio", aleatorio),
                          ("Invertido", invertido)]:
        _, despl = insertion_sort(datos)
        print(f"  {nombre:>15}: {despl} desplazamientos")

    # 3. Comparacion: clasico vs binario
    print("\n--- Clasico vs Binario (comparaciones) ---")
    datos_comp = [random.randint(1, 100) for _ in range(15)]
    print(f"  Datos: {datos_comp}")
    res_clasico, despl_clasico = insertion_sort(datos_comp)
    res_binario, comps_binario = binary_insertion_sort(datos_comp)
    print(f"  Clasico:  {despl_clasico} desplazamientos")
    print(f"  Binario:  {comps_binario} comparaciones (busqueda binaria)")
    print(f"  Resultado clasico:  {res_clasico}")
    print(f"  Resultado binario:  {res_binario}")
    print(f"  Ambos iguales: {res_clasico == res_binario}")

    # 4. Rendimiento comparativo
    print("\n--- Comparacion de rendimiento ---")
    tamanos = [1000, 3000, 5000]
    for n in tamanos:
        datos_rand = [random.randint(0, n) for _ in range(n)]
        datos_casi = list(range(n))
        # Perturbar ligeramente
        for _ in range(5):
            a, b = random.sample(range(n), 2)
            datos_casi[a], datos_casi[b] = datos_casi[b], datos_casi[a]

        inicio = time.time()
        insertion_sort(datos_rand)
        t_rand = time.time() - inicio

        inicio = time.time()
        insertion_sort(datos_casi)
        t_casi = time.time() - inicio

        inicio = time.time()
        binary_insertion_sort(datos_rand)
        t_bin = time.time() - inicio

        print(f"  n={n:>5}: clasico(aleatorio)={t_rand:.4f}s | "
              f"clasico(casi ordenado)={t_casi:.6f}s | "
              f"binario(aleatorio)={t_bin:.4f}s")

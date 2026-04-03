"""
Counting Sort (Ordenamiento por Conteo)

Algoritmo de ordenamiento no comparativo. Cuenta las ocurrencias
de cada valor y usa esas cuentas para colocar los elementos en
su posicion correcta. Funciona en O(n + k) donde k es el rango
de los valores.

Complejidad:
  - Tiempo:  O(n + k)  donde k = max - min + 1
  - Espacio: O(n + k)

Requisitos:
  - Los valores deben ser enteros (o mapeables a enteros)
  - Es mas eficiente cuando k no es mucho mayor que n
"""

import time
import random


# --- Counting sort basico ---

def counting_sort(arreglo):
    """Counting sort para enteros no negativos."""
    if not arreglo:
        return []

    maximo = max(arreglo)
    # Crear arreglo de conteo
    conteo = [0] * (maximo + 1)

    # Contar ocurrencias
    for valor in arreglo:
        conteo[valor] += 1

    # Reconstruir el arreglo ordenado
    resultado = []
    for valor, cantidad in enumerate(conteo):
        resultado.extend([valor] * cantidad)

    return resultado


# --- Counting sort con numeros negativos ---

def counting_sort_negativos(arreglo):
    """Counting sort que soporta numeros negativos."""
    if not arreglo:
        return []

    minimo = min(arreglo)
    maximo = max(arreglo)
    rango = maximo - minimo + 1

    # Desplazar todos los valores para que el minimo sea indice 0
    conteo = [0] * rango
    for valor in arreglo:
        conteo[valor - minimo] += 1

    resultado = []
    for i in range(rango):
        resultado.extend([i + minimo] * conteo[i])

    return resultado


# --- Counting sort estable ---

def counting_sort_estable(arreglo, obtener_clave=None):
    """Version estable de counting sort.
    Mantiene el orden relativo de elementos con la misma clave."""
    if not arreglo:
        return []

    if obtener_clave is None:
        obtener_clave = lambda x: x

    # Encontrar rango
    claves = [obtener_clave(elem) for elem in arreglo]
    minimo = min(claves)
    maximo = max(claves)
    rango = maximo - minimo + 1

    # Contar ocurrencias
    conteo = [0] * rango
    for c in claves:
        conteo[c - minimo] += 1

    # Acumular: conteo[i] indica la posicion final del ultimo elemento con clave i
    for i in range(1, rango):
        conteo[i] += conteo[i - 1]

    # Construir resultado recorriendo de derecha a izquierda (estabilidad)
    resultado = [None] * len(arreglo)
    for i in range(len(arreglo) - 1, -1, -1):
        c = obtener_clave(arreglo[i]) - minimo
        conteo[c] -= 1
        resultado[conteo[c]] = arreglo[i]

    return resultado


# --- Visualizacion del arreglo de conteo ---

def counting_sort_visual(arreglo):
    """Muestra el arreglo de conteo como histograma."""
    print(f"  Arreglo: {arreglo}")

    maximo = max(arreglo)
    conteo = [0] * (maximo + 1)
    for v in arreglo:
        conteo[v] += 1

    print(f"\n  Arreglo de conteo (valor: cantidad):")
    for valor, cantidad in enumerate(conteo):
        if cantidad > 0:
            barra = "#" * cantidad
            print(f"    {valor:>3}: {barra} ({cantidad})")

    # Mostrar acumulado
    acumulado = conteo.copy()
    for i in range(1, len(acumulado)):
        acumulado[i] += acumulado[i - 1]

    print(f"\n  Conteo acumulado (posiciones finales):")
    for valor, pos in enumerate(acumulado):
        if conteo[valor] > 0:
            print(f"    Valor {valor}: posicion final -> {pos - 1}")

    resultado = counting_sort(arreglo)
    print(f"\n  Resultado: {resultado}")
    return resultado


# ============================================================
# Ejecucion principal
# ============================================================

if __name__ == "__main__":
    print("=" * 60)
    print("  COUNTING SORT - Ordenamiento por Conteo")
    print("=" * 60)

    # 1. Visualizacion del arreglo de conteo
    print("\n--- Visualizacion del arreglo de conteo ---")
    datos = [4, 2, 2, 8, 3, 3, 1, 7, 4, 2]
    counting_sort_visual(datos)

    # 2. Con numeros negativos
    print("\n--- Soporte para numeros negativos ---")
    negativos = [3, -1, 0, -5, 2, -3, 1, -2, 4, 0]
    resultado_neg = counting_sort_negativos(negativos)
    print(f"  Entrada:   {negativos}")
    print(f"  Resultado: {resultado_neg}")

    # 3. Ejemplo practico: ordenar alumnos por calificacion
    print("\n--- Ejemplo: Ordenar alumnos por calificacion (0-100) ---")
    alumnos = [
        ("Ana", 85), ("Luis", 92), ("Maria", 78),
        ("Carlos", 85), ("Sofia", 92), ("Pedro", 60),
        ("Laura", 78), ("Diego", 95), ("Elena", 85),
    ]
    print("  Alumnos originales:")
    for nombre, cal in alumnos:
        print(f"    {nombre}: {cal}")

    # Ordenar de forma estable por calificacion
    ordenados = counting_sort_estable(alumnos, obtener_clave=lambda x: x[1])
    print("\n  Ordenados por calificacion (estable):")
    for nombre, cal in ordenados:
        print(f"    {nombre}: {cal}")
    print("  Nota: Ana, Carlos, Elena (85) mantienen su orden original")

    # 4. Demostracion de estabilidad
    print("\n--- Demostracion de estabilidad ---")
    # Elementos con mismo valor pero diferente identidad
    elementos = [(3, "A"), (1, "B"), (3, "C"), (2, "D"), (1, "E"), (2, "F")]
    print(f"  Entrada: {elementos}")
    estable = counting_sort_estable(elementos, obtener_clave=lambda x: x[0])
    print(f"  Estable: {estable}")
    print("  Los pares con valor 1 son (B, E), con 3 son (A, C): orden preservado")

    # 5. Comparacion de rendimiento
    print("\n--- Comparacion de rendimiento ---")
    tamanos = [10000, 50000, 100000]
    for n in tamanos:
        k = 100  # Rango de valores [0, k)
        datos_rand = [random.randint(0, k - 1) for _ in range(n)]

        inicio = time.time()
        counting_sort(datos_rand)
        t_counting = time.time() - inicio

        inicio = time.time()
        sorted(datos_rand)
        t_builtin = time.time() - inicio

        print(f"  n={n:>6}, k={k}: counting={t_counting:.5f}s | "
              f"sorted()={t_builtin:.5f}s")

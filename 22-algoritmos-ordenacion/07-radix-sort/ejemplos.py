"""
Radix Sort (Ordenamiento por Raices / Digitos)

Algoritmo no comparativo que ordena numeros procesando cada digito
de forma individual, del menos significativo al mas significativo
(LSD - Least Significant Digit). Usa counting sort como subrutina
para ordenar por cada digito.

Complejidad:
  - Tiempo:  O(d * (n + k))  donde d = num. digitos, k = base (10)
  - Espacio: O(n + k)
"""

import time
import random


# --- Counting sort por digito (subrutina) ---

def counting_sort_por_digito(arreglo, exp):
    """Counting sort estable que ordena por el digito en la posicion 'exp'.
    exp=1 ordena por unidades, exp=10 por decenas, etc."""
    n = len(arreglo)
    resultado = [0] * n
    conteo = [0] * 10  # Digitos del 0 al 9

    # Contar ocurrencias del digito
    for num in arreglo:
        digito = (num // exp) % 10
        conteo[digito] += 1

    # Acumular
    for i in range(1, 10):
        conteo[i] += conteo[i - 1]

    # Construir resultado de derecha a izquierda (estabilidad)
    for i in range(n - 1, -1, -1):
        digito = (arreglo[i] // exp) % 10
        conteo[digito] -= 1
        resultado[conteo[digito]] = arreglo[i]

    return resultado


# --- Radix sort LSD ---

def radix_sort(arreglo):
    """Radix sort LSD (del digito menos significativo al mas significativo)."""
    if not arreglo:
        return []

    arr = arreglo.copy()
    maximo = max(arr)

    # Procesar cada digito: unidades, decenas, centenas, ...
    exp = 1
    while maximo // exp > 0:
        arr = counting_sort_por_digito(arr, exp)
        exp *= 10

    return arr


# --- Radix sort con impresion de pasos ---

def radix_sort_verbose(arreglo):
    """Radix sort que muestra el estado despues de ordenar cada digito."""
    if not arreglo:
        return []

    arr = arreglo.copy()
    maximo = max(arr)
    num_digitos = len(str(maximo))

    print(f"  Arreglo original: {arr}")
    print(f"  Maximo: {maximo} ({num_digitos} digito(s))")
    print()

    exp = 1
    paso = 1
    while maximo // exp > 0:
        # Mostrar los digitos que se estan comparando
        nombres = {1: "unidades", 10: "decenas", 100: "centenas",
                   1000: "millares", 10000: "decenas de millar"}
        nombre_digito = nombres.get(exp, f"posicion {paso}")

        digitos_actuales = [(num, (num // exp) % 10) for num in arr]
        print(f"  Paso {paso} - Ordenar por {nombre_digito}:")
        representacion = [f"{num}(d={d})" for num, d in digitos_actuales]
        print(f"    Digitos: {representacion}")

        arr = counting_sort_por_digito(arr, exp)
        print(f"    Resultado: {arr}")
        print()

        exp *= 10
        paso += 1

    return arr


# --- Radix sort para numeros negativos ---

def radix_sort_con_negativos(arreglo):
    """Radix sort que soporta numeros negativos.
    Separa positivos y negativos, ordena cada grupo, y combina."""
    negativos = [-x for x in arreglo if x < 0]
    positivos = [x for x in arreglo if x >= 0]

    # Ordenar ambos grupos
    neg_ordenados = radix_sort(negativos) if negativos else []
    pos_ordenados = radix_sort(positivos) if positivos else []

    # Los negativos van al reves (y se les restaura el signo)
    return [-x for x in reversed(neg_ordenados)] + pos_ordenados


# --- Ejemplo practico: ordenar fechas ---

def ordenar_fechas(fechas):
    """Ordena fechas en formato (dia, mes, anio) usando radix sort.
    Ordena primero por dia, luego por mes, luego por anio (LSD)."""
    resultado = fechas.copy()

    # Paso 1: ordenar por dia (posicion 0 de la tupla)
    resultado = counting_sort_estable(resultado, clave_idx=0, rango=32)
    print(f"    Tras ordenar por dia:  {formato_fechas(resultado)}")

    # Paso 2: ordenar por mes (posicion 1)
    resultado = counting_sort_estable(resultado, clave_idx=1, rango=13)
    print(f"    Tras ordenar por mes:  {formato_fechas(resultado)}")

    # Paso 3: ordenar por anio (posicion 2)
    anio_min = min(f[2] for f in resultado)
    anio_max = max(f[2] for f in resultado)
    resultado = counting_sort_estable(
        resultado, clave_idx=2, rango=anio_max - anio_min + 1, offset=anio_min)
    print(f"    Tras ordenar por anio: {formato_fechas(resultado)}")

    return resultado


def counting_sort_estable(arreglo, clave_idx, rango, offset=0):
    """Counting sort estable para tuplas, ordena por clave en clave_idx."""
    n = len(arreglo)
    conteo = [0] * rango
    resultado = [None] * n

    for elem in arreglo:
        conteo[elem[clave_idx] - offset] += 1

    for i in range(1, rango):
        conteo[i] += conteo[i - 1]

    for i in range(n - 1, -1, -1):
        c = arreglo[i][clave_idx] - offset
        conteo[c] -= 1
        resultado[conteo[c]] = arreglo[i]

    return resultado


def formato_fechas(fechas):
    """Formatea lista de tuplas (dia, mes, anio) para imprimir."""
    return [f"{d:02d}/{m:02d}/{a}" for d, m, a in fechas]


# ============================================================
# Ejecucion principal
# ============================================================

if __name__ == "__main__":
    print("=" * 60)
    print("  RADIX SORT - Ordenamiento por Raices/Digitos")
    print("=" * 60)

    # 1. Paso a paso digito por digito
    print("\n--- Paso a paso digito por digito ---")
    datos = [170, 45, 75, 90, 802, 24, 2, 66]
    resultado = radix_sort_verbose(datos)
    print(f"  Resultado final: {resultado}")

    # 2. Con numeros de diferente cantidad de digitos
    print("--- Numeros variados ---")
    variados = [3, 521, 78, 1, 4329, 100, 56, 9999, 42]
    res = radix_sort(variados)
    print(f"  Entrada:   {variados}")
    print(f"  Resultado: {res}")

    # 3. Con numeros negativos
    print("\n--- Soporte para negativos ---")
    negativos = [5, -3, 10, -1, 0, -8, 7, -2, 3]
    res_neg = radix_sort_con_negativos(negativos)
    print(f"  Entrada:   {negativos}")
    print(f"  Resultado: {res_neg}")

    # 4. Ejemplo practico: ordenar fechas
    print("\n--- Ejemplo: Ordenar fechas (dia, mes, anio) ---")
    fechas = [
        (15, 3, 2024), (10, 1, 2023), (25, 12, 2023),
        (5, 3, 2024), (10, 6, 2023), (1, 1, 2024),
        (20, 12, 2022), (15, 6, 2023),
    ]
    print(f"  Fechas originales: {formato_fechas(fechas)}")
    print()
    fechas_ord = ordenar_fechas(fechas)
    print(f"\n  Fechas ordenadas:  {formato_fechas(fechas_ord)}")

    # 5. Comparacion de rendimiento
    print("\n--- Comparacion de rendimiento ---")
    tamanos = [10000, 50000, 100000]
    for n in tamanos:
        datos_rand = [random.randint(0, 999999) for _ in range(n)]

        inicio = time.time()
        radix_sort(datos_rand)
        t_radix = time.time() - inicio

        inicio = time.time()
        sorted(datos_rand)
        t_builtin = time.time() - inicio

        print(f"  n={n:>6}: radix_sort={t_radix:.4f}s | "
              f"sorted()={t_builtin:.5f}s")

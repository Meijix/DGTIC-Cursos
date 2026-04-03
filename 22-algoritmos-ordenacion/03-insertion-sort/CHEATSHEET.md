# Cheatsheet — Insertion Sort

## En una frase

Toma cada elemento y lo inserta en su posicion correcta dentro de la parte ya ordenada, como cuando ordenas cartas en la mano.

## Diagrama rapido

```
Analogia: ordenar cartas en la mano

Mano:      []              Mesa: [5, 3, 8, 1]

Paso 1:    [5]             toma 5, mano vacia → colocar
Paso 2:    [5] ← 3        3 < 5, desplaza 5 → [3, 5]
Paso 3:    [3, 5] ← 8     8 > 5, ya esta bien → [3, 5, 8]
Paso 4:    [3, 5, 8] ← 1  1 < 3, desplaza 3,5,8 → [1, 3, 5, 8]

Detalle del paso 4:
  [3, 5, 8, |1]    clave = 1
  [3, 5, 8, _]     8 > 1 → desplaza   [3, 5, _, 8]
                    5 > 1 → desplaza   [3, _, 5, 8]
                    3 > 1 → desplaza   [_, 3, 5, 8]
                    inserta clave →    [1, 3, 5, 8]
```

## Complejidad

| Caso     | Tiempo | Espacio |
|----------|--------|---------|
| Mejor    | O(n)   | O(1)    |
| Promedio | O(n²)  | O(1)    |
| Peor     | O(n²)  | O(1)    |

**Estable:** Si — **In-place:** Si

> Mejor caso O(n) cuando la lista ya esta ordenada (0 desplazamientos).

## Python en 8 lineas

```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        clave = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > clave:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = clave
    return arr
```

### Variante: Binary Insertion Sort

```python
from bisect import insort
def binary_insertion_sort(arr):
    resultado = []
    for x in arr:
        insort(resultado, x)    # busqueda binaria para posicion, O(log n)
    return resultado             # comparaciones O(n log n), pero movimientos siguen O(n²)
```

## Cuando SI usar

- Datos casi ordenados — rinde cercano a O(n)
- Conjuntos pequenos (n < 50) — menos overhead que algoritmos recursivos
- Ordenamiento online/streaming — puede ordenar a medida que llegan datos
- Como subrutina en algoritmos hibridos (Timsort usa Insertion Sort para runs cortos)

## Cuando NO usar

- Conjuntos grandes desordenados — O(n²) comparaciones y movimientos
- Datos en orden inverso — peor caso garantizado

## Tip clave

Insertion Sort es el algoritmo cuadratico mas rapido en la practica para datos casi ordenados. Por eso Timsort (el sort de Python) lo usa internamente para ordenar subsequencias cortas antes de mezclarlas con Merge Sort.

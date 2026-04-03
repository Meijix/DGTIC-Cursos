# Cheatsheet — Bubble Sort

## En una frase

Compara pares adyacentes y "burbujea" el elemento mayor hacia el final en cada pasada.

## Diagrama rapido

```
Pasada 1:  [5, 3, 8, 1]
            ^--^           5 > 3 → swap → [3, 5, 8, 1]
               ^--^        5 < 8 → ok
                  ^--^     8 > 1 → swap → [3, 5, 1, 8]  ← 8 ya en su lugar

Pasada 2:  [3, 5, 1, 8]
            ^--^           3 < 5 → ok
               ^--^        5 > 1 → swap → [3, 1, 5, 8]  ← 5 ya en su lugar

Pasada 3:  [3, 1, 5, 8]
            ^--^           3 > 1 → swap → [1, 3, 5, 8]  ← 3 ya en su lugar

Resultado: [1, 3, 5, 8]   ✓ Ordenado en 3 pasadas
```

## Complejidad

| Caso     | Tiempo | Espacio |
|----------|--------|---------|
| Mejor    | O(n)   | O(1)    |
| Promedio | O(n²)  | O(1)    |
| Peor     | O(n²)  | O(1)    |

**Estable:** Si — **In-place:** Si

> El mejor caso O(n) solo se alcanza con la version optimizada (bandera de intercambio).

## Python en 10 lineas

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        hubo_swap = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                hubo_swap = True
        if not hubo_swap:       # optimizacion: si no hubo swaps, ya esta ordenado
            break
    return arr
```

**La bandera `hubo_swap`** convierte el mejor caso de O(n²) a O(n) cuando la lista ya esta ordenada.

## Cuando SI usar

- Datos casi ordenados (la bandera lo detecta y termina rapido)
- Conjuntos muy pequenos (n < 20)
- Propositos educativos — es el algoritmo mas intuitivo
- Cuando necesitas estabilidad y simplicidad

## Cuando NO usar

- Conjuntos grandes (n > 100) — O(n²) es inaceptable
- Datos en orden inverso — peor caso garantizado
- Aplicaciones de rendimiento critico

## Tip clave

Bubble Sort sin la bandera de optimizacion siempre ejecuta n² comparaciones. Con la bandera, es el unico algoritmo O(n²) que detecta una lista ya ordenada en una sola pasada.

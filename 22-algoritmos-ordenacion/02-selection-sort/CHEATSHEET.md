# Cheatsheet — Selection Sort

## En una frase

Encuentra el minimo del subarreglo no ordenado y lo coloca en su posicion final con un unico swap por pasada.

## Diagrama rapido

```
Pasada 1:  [5, 3, 8, 1]
            ↑        ↑     busca min en [0..3] → min=1 en pos 3
           swap(0,3) →    [1, 3, 8, 5]   ← pos 0 definitiva

Pasada 2:  [1, |3, 8, 5]
                ↑          busca min en [1..3] → min=3 en pos 1
               ya esta →  [1, 3, 8, 5]   ← pos 1 definitiva

Pasada 3:  [1, 3, |8, 5]
                   ↑  ↑   busca min en [2..3] → min=5 en pos 3
              swap(2,3) → [1, 3, 5, 8]   ← pos 2 y 3 definitivas

Resultado: [1, 3, 5, 8]   Solo 2 swaps reales (minimo posible)
```

## Complejidad

| Caso     | Tiempo | Espacio |
|----------|--------|---------|
| Mejor    | O(n²)  | O(1)    |
| Promedio | O(n²)  | O(1)    |
| Peor     | O(n²)  | O(1)    |

**Estable:** No — **In-place:** Si

> Siempre O(n²) comparaciones, pero maximo n-1 intercambios.

### Por que NO es estable

```
Entrada:  [3a, 3b, 1]      (3a y 3b son ambos "3")
Pasada 1: min=1, swap(0,2) → [1, 3b, 3a]
Resultado: 3b quedo antes de 3a — se invirtio el orden relativo
```

## Python en 8 lineas

```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        idx_min = i
        for j in range(i + 1, n):
            if arr[j] < arr[idx_min]:
                idx_min = j
        arr[i], arr[idx_min] = arr[idx_min], arr[i]
    return arr
```

## Cuando SI usar

- Minimizar el numero de intercambios (escrituras) — util en memoria flash/EEPROM
- Conjuntos pequenos (n < 50)
- Cuando los swaps son costosos pero las comparaciones son baratas

## Cuando NO usar

- Conjuntos grandes — siempre O(n²), sin atajos
- Cuando necesitas estabilidad (Selection Sort no la garantiza)
- Datos casi ordenados (no aprovecha el orden previo)

## Tip clave

Selection Sort siempre hace exactamente n-1 swaps sin importar la entrada. Si tu cuello de botella es el costo de escritura (no de lectura), Selection Sort minimiza escrituras entre los algoritmos cuadraticos.

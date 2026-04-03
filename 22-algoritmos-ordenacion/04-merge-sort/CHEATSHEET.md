# Cheatsheet — Merge Sort

## En una frase

Divide el arreglo a la mitad recursivamente hasta tener elementos individuales, luego mezcla las mitades ordenadas de vuelta.

## Diagrama rapido

```
              [5, 3, 8, 1, 7, 2]
             /                   \            DIVIDIR
        [5, 3, 8]            [1, 7, 2]
        /       \            /       \
    [5, 3]     [8]      [1, 7]     [2]
    /    \                /    \
  [5]   [3]           [1]    [7]
    \    /                \    /
    [3, 5]     [8]      [1, 7]     [2]       MEZCLAR
        \       /            \       /
        [3, 5, 8]            [1, 2, 7]
             \                   /
              [1, 2, 3, 5, 7, 8]

Detalle de mezcla [3,5,8] + [1,2,7]:
  i→[3, 5, 8]   j→[1, 2, 7]   resultado = []
  1 < 3 → toma 1              resultado = [1]
  2 < 3 → toma 2              resultado = [1, 2]
  3 < 7 → toma 3              resultado = [1, 2, 3]
  5 < 7 → toma 5              resultado = [1, 2, 3, 5]
  7 < 8 → toma 7              resultado = [1, 2, 3, 5, 7]
  queda 8                      resultado = [1, 2, 3, 5, 7, 8]
```

## Complejidad

| Caso     | Tiempo     | Espacio |
|----------|------------|---------|
| Mejor    | O(n log n) | O(n)    |
| Promedio | O(n log n) | O(n)    |
| Peor     | O(n log n) | O(n)    |

**Estable:** Si — **In-place:** No (requiere O(n) memoria auxiliar)

> Siempre O(n log n) — rendimiento garantizado sin importar la entrada.

## Python en 15 lineas

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    izq = merge_sort(arr[:mid])
    der = merge_sort(arr[mid:])
    return merge(izq, der)

def merge(izq, der):
    resultado = []
    i = j = 0
    while i < len(izq) and j < len(der):
        if izq[i] <= der[j]:       # <= garantiza estabilidad
            resultado.append(izq[i])
            i += 1
        else:
            resultado.append(der[j])
            j += 1
    resultado.extend(izq[i:])
    resultado.extend(der[j:])
    return resultado
```

> El `<=` en la comparacion (en lugar de `<`) es lo que garantiza la estabilidad.

## Cuando SI usar

- Necesitas O(n log n) garantizado — no hay peor caso degradado
- Necesitas estabilidad (mantener orden relativo de elementos iguales)
- Ordenar listas enlazadas — no necesita acceso aleatorio, y se puede hacer in-place
- Ordenamiento externo (archivos en disco) — patron secuencial de lectura/escritura
- Datos muy grandes que no caben en memoria (external merge sort)

## Cuando NO usar

- Memoria limitada — necesita O(n) espacio adicional para arreglos
- Conjuntos pequenos (n < 50) — el overhead recursivo no vale la pena; usa Insertion Sort
- Cuando Quick Sort es suficiente y la memoria importa

## Tip clave

Merge Sort es el unico algoritmo basado en comparaciones que garantiza O(n log n) en todos los casos Y es estable. Esa combinacion lo hace la base de Timsort (Python, Java) y la primera opcion para ordenar datos enlazados o en disco.

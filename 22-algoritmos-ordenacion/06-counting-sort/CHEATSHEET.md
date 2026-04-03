# Cheatsheet — Counting Sort

## En una frase
Cuenta las ocurrencias de cada valor en un arreglo auxiliar y reconstruye el arreglo ordenado sin hacer comparaciones.

## Diagrama rapido
```
Arreglo:  [4, 2, 2, 8, 3, 3, 1]    rango: 0..8 (k=9)

Paso 1 — Contar ocurrencias:
  indice:  0  1  2  3  4  5  6  7  8
  count:  [0, 1, 2, 2, 1, 0, 0, 0, 1]
               ^  ^  ^  ^           ^
               1  2  2  4           8

Paso 2 — Acumular (prefijos):
  count:  [0, 1, 3, 5, 6, 6, 6, 6, 7]
           cada valor indica la posicion final

Paso 3 — Colocar elementos (de derecha a izquierda):
  salida: [_, _, _, _, _, _, _]
  arr[6]=1 -> salida[0]=1  ->  [1, _, _, _, _, _, _]
  arr[5]=3 -> salida[4]=3  ->  [1, _, _, _, 3, _, _]
  arr[4]=3 -> salida[3]=3  ->  [1, _, _, 3, 3, _, _]
  ...
  Resultado: [1, 2, 2, 3, 3, 4, 8]
```

## Complejidad
| Caso    | Tiempo  | Espacio |
|---------|---------|---------|
| Mejor   | O(n+k)  | O(n+k)  |
| Promedio | O(n+k) | O(n+k)  |
| Peor    | O(n+k)  | O(n+k)  |

> **k** = rango de valores (max - min + 1)

**Estable:** Si — **In-place:** No

## Requisitos
- Las claves deben ser **enteros** (o mapeables a enteros)
- El rango **k** debe ser conocido y razonablemente pequeno
- Funciona mejor cuando k = O(n)

## Python en 10 lineas
```python
def counting_sort(arr):
    if not arr:
        return arr
    min_val, max_val = min(arr), max(arr)
    k = max_val - min_val + 1
    count = [0] * k
    output = [0] * len(arr)
    for x in arr:
        count[x - min_val] += 1
    for i in range(1, k):
        count[i] += count[i - 1]
    for x in reversed(arr):           # reversed = estable
        output[count[x - min_val] - 1] = x
        count[x - min_val] -= 1
    return output
```

## Cuando SI / Cuando NO
**Usar cuando:**
- Los datos son enteros con rango pequeno (edades, calificaciones 0-100, digitos)
- Se necesita ordenamiento estable como subrutina (ej. dentro de Radix Sort)
- Se quiere romper la barrera O(n log n) de los algoritmos por comparacion

**NO usar cuando:**
- El rango k es mucho mayor que n (desperdicio de memoria)
- Los datos son de punto flotante o cadenas arbitrarias
- El rango de valores es desconocido o cambia dinamicamente
- La memoria es limitada (necesita O(n+k) espacio extra)

## Tip clave
Counting Sort no es un algoritmo de comparacion: no compara elementos entre si. Por eso puede ser mas rapido que O(n log n), pero a cambio solo funciona con enteros de rango acotado.

# Cheatsheet — Quick Sort

## En una frase
Divide el arreglo eligiendo un pivote, coloca los menores a la izquierda y los mayores a la derecha, y repite recursivamente.

## Diagrama rapido
```
Arreglo:  [8, 3, 1, 7, 0, 5, 2, 4]
                            pivote = 4

Particion (Lomuto):
  i
  [8, 3, 1, 7, 0, 5, 2,|4]   comparar cada elemento con pivote
  [3, 1, 0, 2,|4,|8, 7, 5]   resultado de particion
   \_________/  ^  \______/
    menores   pivote mayores

Recursion:
  quick_sort([3,1,0,2])  +  [4]  +  quick_sort([8,7,5])
  quick_sort([0,1,2,3])  +  [4]  +  quick_sort([5,7,8])

Resultado: [0, 1, 2, 3, 4, 5, 7, 8]
```

## Complejidad
| Caso    | Tiempo     | Espacio  |
|---------|------------|----------|
| Mejor   | O(n log n) | O(log n) |
| Promedio | O(n log n) | O(log n) |
| Peor    | O(n²)     | O(n)     |

**Estable:** No — **In-place:** Si

## Estrategias de pivote
| Estrategia       | Descripcion                        | Riesgo peor caso |
|------------------|------------------------------------|-------------------|
| Primer elemento  | `pivot = arr[lo]`                  | Alto (datos ordenados) |
| Ultimo elemento  | `pivot = arr[hi]`                  | Alto (datos ordenados) |
| Aleatorio        | `pivot = arr[random(lo, hi)]`      | Bajo              |
| Mediana de tres  | mediana de `arr[lo], arr[mid], arr[hi]` | Muy bajo     |

## Python en 10 lineas
```python
def quick_sort(arr, lo=0, hi=None):
    if hi is None:
        hi = len(arr) - 1
    if lo < hi:
        pi = partition(arr, lo, hi)
        quick_sort(arr, lo, pi - 1)
        quick_sort(arr, pi + 1, hi)

def partition(arr, lo, hi):
    pivot = arr[hi]          # Lomuto: pivote al final
    i = lo - 1
    for j in range(lo, hi):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[hi] = arr[hi], arr[i + 1]
    return i + 1
```

## Cuando SI / Cuando NO
**Usar cuando:**
- Se necesita un algoritmo de proposito general rapido en la practica
- Se requiere ordenamiento in-place (poca memoria extra)
- Se busca buen rendimiento con cache (acceso secuencial a memoria)
- Los datos no estan casi ordenados

**NO usar cuando:**
- Se necesita garantia de O(n log n) en el peor caso (usar Merge Sort)
- Se requiere estabilidad (elementos iguales mantienen orden original)
- Los datos ya estan casi ordenados y se elige mal el pivote
- Se trabaja con listas enlazadas (Merge Sort es mejor opcion)

## Tip clave
Quick Sort es mas rapido que Merge Sort en la practica gracias a su mejor localidad de cache, aunque su peor caso es O(n²). Usar pivote aleatorio o mediana de tres elimina el peor caso en la practica.

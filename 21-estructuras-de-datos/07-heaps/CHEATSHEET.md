# Cheatsheet — Heaps (Monticulos)

## Diagrama rapido

```
MIN-HEAP: el padre siempre es <= que sus hijos

        [1]                 MAX-HEAP: el padre siempre es >= que sus hijos
       /   \
     [3]   [2]                     [9]
    /   \                         /   \
  [7]   [5]                    [7]   [8]
                              /   \
                            [3]   [5]

REPRESENTACION EN ARRAY (min-heap):

  Indice:  0   1   2   3   4
  Array: [ 1 , 3 , 2 , 7 , 5 ]

  Arbol:       [1]           FORMULAS DE INDICES (base 0):
              /   \
           [3]    [2]         padre(i)    = (i - 1) // 2
          /   \               hijo_izq(i) = 2 * i + 1
        [7]   [5]             hijo_der(i) = 2 * i + 2

HEAPIFY UP (al insertar):         HEAPIFY DOWN (al extraer min/max):
  Insertas al final del array.      Mueves el ultimo elemento a la raiz.
  Sube comparando con su padre.     Baja comparando con sus hijos.

  Insertar 0:                       Extraer min (1):
  [ 1, 3, 2, 7, 5, 0 ]             [ 5, 3, 2, 7 ]
  0 < 2? si → swap                  5 > 2? si → swap con hijo menor
  0 < 1? si → swap                  [ 2, 3, 5, 7 ] ← heap restaurado
  [ 0, 3, 1, 7, 5, 2 ] ← listo
```

## Operaciones — O(?)

```
┌──────────────────────┬──────────────┐
│ Operacion            │ Complejidad  │
├──────────────────────┼──────────────┤
│ Obtener min/max      │    O(1)      │
│ Insertar (push)      │  O(log n)    │
│ Extraer min/max (pop)│  O(log n)    │
│ Heapify (construir)  │    O(n)      │
│ Buscar un elemento   │    O(n)      │
│ nlargest / nsmallest │  O(n log k)  │
└──────────────────────┴──────────────┘
Espacio: O(n)
```

## Python en 30 segundos

```python
import heapq

# --- Operaciones basicas (MIN-HEAP) ---
h = []
heapq.heappush(h, 5);  heapq.heappush(h, 2);  heapq.heappush(h, 8)
print(h[0])                    # ver minimo sin extraer → 2
minimo = heapq.heappop(h)     # extraer minimo → 2

# Convertir lista en heap in-place O(n)
datos = [7, 3, 9, 1, 5]
heapq.heapify(datos)           # → [1, 3, 9, 7, 5]

# Top-K elementos
heapq.nlargest(3, datos)       # los 3 mas grandes
heapq.nsmallest(2, datos)      # los 2 mas pequenos

# TRUCO MAX-HEAP: negar valores
heapq.heappush(h, -10);  heapq.heappush(h, -20)
maximo = -heapq.heappop(h)    # → 20

# Cola de prioridad con tuplas (prioridad, dato)
tareas = []
heapq.heappush(tareas, (1, "urgente"))
heapq.heappush(tareas, (3, "baja"))
prioridad, tarea = heapq.heappop(tareas)  # → (1, "urgente")
```

## Cuando usar / Cuando NO usar

- **Usar** para colas de prioridad (procesamiento por urgencia).
- **Usar** para obtener los K elementos mas grandes/pequenos eficientemente.
- **Usar** para algoritmos como Dijkstra, Huffman, merge de K listas ordenadas.
- **NO usar** si necesitas buscar un elemento especifico (es O(n), no O(log n)).
- **NO usar** si necesitas todos los datos ordenados — mejor ordena la lista directamente.
- **NO usar** si necesitas acceso aleatorio por indice con significado logico.

## Errores clasicos

- **Creer que `heapq` soporta max-heap**: solo es min-heap. Usa `heappush(h, -val)` para simular max-heap.
- **Pensar que el heap esta ordenado**: `[1, 3, 9, 7, 5]` es un heap valido pero NO esta sorted. Solo se garantiza que `h[0]` es el minimo.
- **Usar `h[0]` despues de `heappop` sin verificar**: si el heap queda vacio, `h[0]` lanza `IndexError`.
- **Olvidar que `heapify` es in-place**: modifica la lista original, no retorna una nueva.
- **No usar tuplas para desempatar**: si dos elementos tienen la misma prioridad y no son comparables, Python lanza error. Usa `(prioridad, contador, dato)`.

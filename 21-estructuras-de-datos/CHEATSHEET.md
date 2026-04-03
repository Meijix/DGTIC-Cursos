# Cheatsheet — Estructuras de Datos

## Tabla comparativa general

```
┌─────────────────────┬───────────┬───────────┬───────────┬───────────┬─────────────┐
│ Estructura          │  Acceso   │ Busqueda  │ Insercion │Eliminacion│   Espacio   │
├─────────────────────┼───────────┼───────────┼───────────┼───────────┼─────────────┤
│ Array / Lista       │   O(1)    │   O(n)    │   O(n)    │   O(n)    │    O(n)     │
│ Lista enlazada      │   O(n)    │   O(n)    │   O(1)*   │   O(1)*   │    O(n)     │
│ Pila (Stack)        │   O(n)    │   O(n)    │   O(1)    │   O(1)    │    O(n)     │
│ Cola (Queue)        │   O(n)    │   O(n)    │   O(1)    │   O(1)    │    O(n)     │
│ Tabla hash          │    —      │   O(1)†   │   O(1)†   │   O(1)†   │    O(n)     │
│ Arbol BST           │ O(log n)‡ │ O(log n)‡ │ O(log n)‡ │ O(log n)‡ │    O(n)     │
│ Heap                │   O(1)§   │   O(n)    │ O(log n)  │ O(log n)  │    O(n)     │
│ Grafo (lista adj.)  │    —      │   O(V+E)  │   O(1)    │   O(E)    │   O(V+E)    │
└─────────────────────┴───────────┴───────────┴───────────┴───────────┴─────────────┘

*  Con referencia al nodo. Sin ella, buscar el nodo es O(n).
†  Caso promedio. Peor caso O(n) con muchas colisiones.
‡  Arbol balanceado. Peor caso O(n) si esta degenerado.
§  Solo el minimo (min-heap) o maximo (max-heap).
```

---

## Diagrama visual rapido

```
ARRAY:
  ┌───┬───┬───┬───┬───┐
  │ 0 │ 1 │ 2 │ 3 │ 4 │   Memoria contigua, acceso por indice
  └───┴───┴───┴───┴───┘

LISTA ENLAZADA:
  [A] ──► [B] ──► [C] ──► None    Nodos con punteros

PILA (LIFO):                COLA (FIFO):
  ┌───┐  ← top               salida ← [A][B][C][D] ← entrada
  │ C │
  │ B │
  │ A │
  └───┘

TABLA HASH:
  clave ──► hash() ──► indice ──► valor
  "gato"   ──► 3421  ──► [2]  ──► "felino"

ARBOL BST:
        8
       / \
      3   10
     / \    \
    1   6    14

HEAP (min):
        1
       / \
      3   2
     / \
    7   5

GRAFO:
  A ─── B
  |   / |
  |  /  |
  C ─── D
```

---

## Cuando usar cada estructura

```
┌──────────────────────────────┬──────────────────────────────────────────┐
│ Necesitas...                 │ Usa                                      │
├──────────────────────────────┼──────────────────────────────────────────┤
│ Acceso por indice rapido     │ Array / Lista                            │
│ Insertar/eliminar frecuente  │ Lista enlazada                           │
│ LIFO (deshacer, recursion)   │ Pila                                     │
│ FIFO (turnos, BFS)           │ Cola                                     │
│ Buscar por clave en O(1)     │ Tabla hash (dict/set)                    │
│ Datos ordenados + busqueda   │ Arbol BST / Arbol balanceado             │
│ Minimo/maximo rapido         │ Heap                                     │
│ Modelar relaciones           │ Grafo                                    │
│ Cola con prioridad           │ Heap                                     │
│ Cache LRU                    │ Tabla hash + lista doble enlazada        │
│ Autocompletado / prefijos    │ Trie (arbol de prefijos)                 │
└──────────────────────────────┴──────────────────────────────────────────┘
```

---

## Equivalencias en Python

| Estructura | Python |
|-----------|--------|
| Array / Lista | `list`, `array.array` |
| Lista enlazada | Implementacion manual (no hay built-in) |
| Pila | `list` (append/pop) o `collections.deque` |
| Cola | `collections.deque` o `queue.Queue` |
| Tabla hash | `dict`, `set`, `collections.defaultdict` |
| Arbol | Implementacion manual o `sortedcontainers.SortedList` |
| Heap | `heapq` (min-heap sobre lista) |
| Grafo | `dict` de listas/sets, o `networkx` |
| Cola de prioridad | `heapq` o `queue.PriorityQueue` |

---

## Arbol de decision

```
¿Necesitas acceso por posicion (indice)?
├── SI ──► Array / Lista
└── NO
    ¿Necesitas acceso por clave?
    ├── SI ──► Tabla hash (dict)
    └── NO
        ¿Los datos tienen jerarquia?
        ├── SI ──► Arbol
        └── NO
            ¿Los datos tienen relaciones multiples?
            ├── SI ──► Grafo
            └── NO
                ¿El orden de procesamiento importa?
                ├── LIFO ──► Pila
                ├── FIFO ──► Cola
                ├── Por prioridad ──► Heap
                └── NO ──► Lista o Set
```

---

## Errores frecuentes

| Error | Correccion |
|-------|-----------|
| Usar lista para busquedas frecuentes | Usa `set` o `dict` → O(1) en vez de O(n) |
| Insertar al inicio de una lista grande | Usa `deque` → O(1) en vez de O(n) |
| BST sin balancear con datos ordenados | Degenera a lista enlazada → usa arbol balanceado |
| Olvidar que `heapq` es min-heap | Para max-heap, niega los valores: `heappush(h, -val)` |
| Confundir pila y cola | LIFO = Pila (platos), FIFO = Cola (fila del banco) |
| Usar lista de adyacencia para grafo denso | Mejor matriz de adyacencia si E ≈ V² |

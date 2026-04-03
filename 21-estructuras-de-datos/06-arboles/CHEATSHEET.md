# Cheatsheet — Arboles (BST)

## Diagrama rapido

```
TERMINOLOGIA:
                 [8]  ← raiz (root), profundidad=0
                /   \
             [3]     [10]  ← nodos internos, profundidad=1
            /   \       \
          [1]   [6]     [14]  ← profundidad=2
                / \     /
              [4] [7] [13]  ← hojas (sin hijos), profundidad=3

  Altura del arbol = 3 (camino mas largo desde raiz a hoja)
  Profundidad de un nodo = distancia desde la raiz

PROPIEDAD BST:
  Para cada nodo: izquierda < nodo < derecha

BALANCEADO vs DEGENERADO:
      [5]              [1]
     /   \               \
   [3]   [7]              [2]
   / \   / \                \
  [1][4][6][8]               [3]    ← Esto es basicamente una lista enlazada
  Altura: O(log n)            \     ← Todas las operaciones caen a O(n)
                               [4]
```

## Operaciones — O(?)

```
┌───────────────────┬──────────────────┬──────────────┐
│ Operacion         │ Balanceado       │ Degenerado   │
├───────────────────┼──────────────────┼──────────────┤
│ Buscar            │   O(log n)       │    O(n)      │
│ Insertar          │   O(log n)       │    O(n)      │
│ Eliminar          │   O(log n)       │    O(n)      │
│ Minimo / Maximo   │   O(log n)       │    O(n)      │
│ Recorrido completo│   O(n)           │    O(n)      │
└───────────────────┴──────────────────┴──────────────┘
Espacio: O(n)
```

## Recorridos — Cuando usar cada uno

```
        [8]
       /   \
     [3]   [10]
     / \
   [1] [6]

Inorder   (izq, raiz, der):  1, 3, 6, 8, 10  ← ORDENADO! Usar para obtener datos sorted
Preorder  (raiz, izq, der):  8, 3, 1, 6, 10   ← Usar para copiar/serializar el arbol
Postorder (izq, der, raiz):  1, 6, 3, 10, 8   ← Usar para eliminar/liberar el arbol
Level-order (por niveles):   8, 3, 10, 1, 6   ← BFS, usar para imprimir por niveles
```

## Python en 30 segundos

```python
class Nodo:
    def __init__(self, val):
        self.val, self.izq, self.der = val, None, None

def insertar(raiz, val):
    if raiz is None: return Nodo(val)
    if val < raiz.val:   raiz.izq = insertar(raiz.izq, val)
    elif val > raiz.val: raiz.der = insertar(raiz.der, val)
    return raiz  # IMPORTANTE: siempre retornar la raiz

def buscar(raiz, val):
    if raiz is None or raiz.val == val: return raiz
    return buscar(raiz.izq if val < raiz.val else raiz.der, val)

def inorder(raiz):  # Imprime en orden ascendente
    if raiz:
        inorder(raiz.izq); print(raiz.val, end=" "); inorder(raiz.der)
```

## Cuando usar / Cuando NO usar

- **Usar** cuando necesitas datos ordenados con insercion/busqueda eficiente.
- **Usar** para rangos de busqueda ("todos los valores entre X e Y").
- **NO usar** si los datos llegan ya ordenados (el BST degenera) — usa arbol balanceado (AVL, Red-Black).
- **NO usar** si solo necesitas busqueda por clave sin orden — una tabla hash es mas rapida.

## Errores clasicos

- **Olvidar el caso `None`**: siempre verifica `if raiz is None` antes de acceder a `.val`.
- **Eliminar nodo con 2 hijos mal**: debes reemplazar con el sucesor inorder (minimo del subarbol derecho) o predecesor inorder (maximo del izquierdo), no solo borrar.
- **No retornar la raiz en funciones recursivas**: `raiz.izq = insertar(raiz.izq, val)` — sin la asignacion, el nodo nuevo se pierde.
- **Insertar datos ordenados en BST sin balanceo**: obtienes una lista enlazada con O(n) en todo.
- **Confundir profundidad con altura**: profundidad = desde la raiz hacia abajo; altura = desde el nodo hacia la hoja mas lejana.

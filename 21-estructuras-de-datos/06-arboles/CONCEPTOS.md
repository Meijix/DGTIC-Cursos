# Arboles (Trees)

## Que es

Un **arbol** es una estructura de datos jerarquica no lineal compuesta por nodos conectados por aristas. Tiene un **nodo raiz** del cual descienden todos los demas nodos. Cada nodo puede tener cero o mas hijos. Los arboles de busqueda binaria (BST) y los arboles AVL son variantes fundamentales que permiten busquedas eficientes.

## Diagrama

### Terminologia basica

```
             [8]          ← raiz (root), profundidad 0
            /   \
         [4]     [12]     ← nodos internos, profundidad 1
        /   \    /   \
      [2]  [6] [10] [14]  ← profundidad 2
      / \
    [1] [3]                ← hojas (leaves), profundidad 3

    Altura del arbol: 3
    Nodo [4]: padre=[8], hijos=[2,6], subarbol izquierdo de [8]
```

### Propiedad del BST (Arbol de Busqueda Binaria)

```
Para cada nodo:
  - Todo el subarbol izquierdo < nodo
  - Todo el subarbol derecho  > nodo

         [8]
        /   \
      [4]   [12]
       ↑      ↑
    < 8     > 8

Buscar 6:  8 → izquierda → 4 → derecha → 6  ✓ (3 pasos)
```

### BST balanceado vs desbalanceado

```
Balanceado (h = log n):     Desbalanceado (h = n):

       [4]                  [1]
      /   \                    \
    [2]   [6]                  [2]
    / \   / \                     \
  [1] [3][5] [7]                  [3]
                                     \
  Busqueda: O(log n)                 [4]
                                        \
                                        [5]

                              Busqueda: O(n) ← degenera a lista!
```

## Operaciones principales

| Operacion     | BST promedio | BST peor caso | AVL        |
|---------------|-------------|---------------|------------|
| Busqueda      | O(log n)    | O(n)          | O(log n)   |
| Insercion     | O(log n)    | O(n)          | O(log n)   |
| Eliminacion   | O(log n)    | O(n)          | O(log n)   |
| Minimo/Maximo | O(log n)    | O(n)          | O(log n)   |
| Recorrido     | O(n)        | O(n)          | O(n)       |

El arbol AVL se **autobalancea** con rotaciones, garantizando O(log n).

## Como funciona

### Recorridos (traversals)

```
           [8]
          /   \
        [4]   [12]
        / \
      [2] [6]

Inorden (izq, raiz, der):    2, 4, 6, 8, 12   ← ordenado!
Preorden (raiz, izq, der):   8, 4, 2, 6, 12   ← copia del arbol
Postorden (izq, der, raiz):  2, 6, 4, 12, 8   ← eliminar arbol
Por niveles (BFS):           8, 4, 12, 2, 6    ← nivel por nivel
```

### Insercion en BST

```
Insertar 5 en el BST:

       [8]          5 < 8 → izquierda
      /   \
    [4]   [12]      5 > 4 → derecha
    / \
  [2] [6]           5 < 6 → izquierda
      /
    [5]  ← nuevo nodo (siempre se inserta como hoja)
```

### Rotaciones en AVL

```
Rotacion simple a la derecha (cuando esta desbalanceado a la izquierda):

      [30]                [20]
      /          →       /    \
    [20]               [10]   [30]
    /
  [10]

Rotacion doble izquierda-derecha:

    [30]        [30]         [25]
    /      →    /       →   /    \
  [20]        [25]        [20]   [30]
     \        /
    [25]    [20]
```

## Cuando usarla

**Usar BST cuando:**
- Necesitas datos ordenados con busqueda eficiente
- Requieres operaciones de rango (elementos entre X y Y)
- Necesitas minimo/maximo rapido
- Los datos se insertan en orden relativamente aleatorio

**Usar AVL / arbol balanceado cuando:**
- Los datos pueden insertarse en orden (lo que desbalancea un BST simple)
- Necesitas garantia de O(log n) en todas las operaciones
- La aplicacion es critica en rendimiento

**NO usar arboles cuando:**
- Solo necesitas busqueda por clave sin orden (usar tabla hash, O(1))
- Los datos son pocos (un array con busqueda lineal es suficiente)
- No necesitas mantener orden

## Casos de uso en el mundo real

- **Bases de datos**: indices B-Tree y B+Tree para busqueda en disco
- **Sistemas de archivos**: estructura de directorios
- **Compiladores**: arboles de sintaxis abstracta (AST)
- **Autocompletado**: arboles Trie para prefijos
- **Balanceo de carga**: arboles de intervalos
- **Compresion**: arbol de Huffman

## Errores comunes

1. **No manejar el caso de eliminacion con dos hijos**: se debe reemplazar con el sucesor inorden (menor del subarbol derecho) o el predecesor inorden.
2. **Asumir que un BST esta balanceado**: insertar datos ordenados produce un arbol degenerado. Usar AVL o Red-Black Tree.
3. **Confundir profundidad con altura**: la profundidad se mide desde la raiz hacia abajo, la altura desde las hojas hacia arriba.
4. **Olvidar actualizar el padre**: al eliminar o rotar nodos, hay que actualizar las referencias del nodo padre.
5. **Recursion sin caso base**: los recorridos recursivos necesitan verificar si el nodo es `None` antes de continuar.

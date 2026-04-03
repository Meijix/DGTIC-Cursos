# Heaps (Monticulos)

## Que es

Un **heap** (monticulo) es un arbol binario completo que cumple la **propiedad de heap**: en un max-heap, cada padre es mayor o igual que sus hijos; en un min-heap, cada padre es menor o igual que sus hijos. Se usa principalmente para implementar **colas de prioridad** y es la base del algoritmo heapsort.

## Diagrama

### Min-Heap vs Max-Heap

```
Min-Heap (raiz = minimo):       Max-Heap (raiz = maximo):

         [1]                             [9]
        /   \                           /   \
      [3]   [2]                       [7]   [8]
     /   \  /                        /   \  /
   [7]  [6][5]                     [3]  [6][5]

Propiedad: padre <= hijos         Propiedad: padre >= hijos
```

### Representacion como array

Un heap se almacena eficientemente en un **array**, sin necesidad de punteros:

```
Min-Heap:
         [1]
        /   \
      [3]   [2]
     /   \  /
   [7]  [6][5]

Array: [1, 3, 2, 7, 6, 5]
Indice: 0  1  2  3  4  5

Relaciones (indice base 0):
  Padre de i:      (i - 1) // 2
  Hijo izquierdo:  2 * i + 1
  Hijo derecho:    2 * i + 2

Ejemplo: nodo en indice 1 (valor 3)
  Padre: (1-1)//2 = 0 → valor 1  ✓ (1 <= 3)
  Hijo izq: 2*1+1 = 3 → valor 7
  Hijo der: 2*1+2 = 4 → valor 6
```

## Operaciones principales

| Operacion       | Complejidad | Descripcion                              |
|-----------------|-------------|------------------------------------------|
| peek/find-min   | O(1)        | Ver el minimo (raiz) sin removerlo       |
| insert (push)   | O(log n)    | Insertar y subir (heapify-up)            |
| extract-min(pop)| O(log n)    | Extraer raiz y reordenar (heapify-down)  |
| heapify (array) | O(n)        | Construir heap desde un array            |
| merge           | O(n)        | Combinar dos heaps                       |

## Como funciona

### Insercion (heapify-up / sift-up)

```
Insertar 0 en el min-heap:

Paso 1: Agregar al final         Paso 2: Subir (0 < 2)
         [1]                              [1]
        /   \                            /   \
      [3]   [2]                        [3]   [0] ←
     /   \  / \                       /   \  / \
   [7]  [6][5] [0] ←               [7]  [6][5] [2]

Paso 3: Subir (0 < 1)
         [0] ←
        /   \
      [3]   [1]
     /   \  / \
   [7]  [6][5] [2]

Se detiene cuando el padre es menor o llega a la raiz.
```

### Extraccion del minimo (heapify-down / sift-down)

```
Extraer minimo (raiz = 1):

Paso 1: Mover ultimo a raiz     Paso 2: Bajar (6 > 2, ir a der)
         [1]  → extraer              [6]
        /   \                        /   \
      [3]   [2]      →            [3]   [2] ←menor hijo
     /   \  /                    /   \
   [7]  [6][5]→mover           [7]  [5]

Paso 3: Resultado               Paso 4: Bajar (6 > 5, ir a izq)
         [2]                             [2]
        /   \                           /   \
      [3]   [6]                       [3]   [5]
     /   \           →               /   \
   [7]  [5]←menor hijo            [7]  [6]

Retorna: 1
```

### Construir heap desde array - heapify O(n)

```
Array desordenado: [5, 3, 8, 1, 2, 7]

Aplicar sift-down desde el ultimo padre hasta la raiz:

  [5]        [5]        [5]        [1]
 /   \      /   \      /   \      /   \
[3]  [8] → [1]  [8] → [1]  [7] → [2]  [7]
/ \  /    / \   /    / \   /    / \   /
[1][2][7]  [3][2] [7]  [3][2] [8]  [3][5] [8]

Es O(n), NO O(n log n), porque los nodos inferiores hacen menos trabajo.
```

## Cuando usarla

**Usar heaps cuando:**
- Necesitas acceso rapido al minimo o maximo (O(1))
- Implementas una cola de prioridad
- Necesitas los K elementos mas grandes/pequenos de un conjunto
- Implementas algoritmos como Dijkstra, Prim o A*
- Necesitas ordenamiento eficiente (heapsort, O(n log n) in-place)

**NO usar heaps cuando:**
- Necesitas buscar un elemento arbitrario (O(n) en heap, O(log n) en BST)
- Necesitas todos los elementos ordenados constantemente (usar BST/AVL)
- Necesitas acceso por clave (usar tabla hash)

### En Python

```
import heapq  # Implementa min-heap

nums = [5, 3, 8, 1, 2]
heapq.heapify(nums)          # Convertir lista a heap O(n)
heapq.heappush(nums, 0)      # Insertar O(log n)
minimo = heapq.heappop(nums) # Extraer minimo O(log n)

# Para max-heap: negar los valores
heapq.heappush(heap, -valor)
maximo = -heapq.heappop(heap)
```

## Casos de uso en el mundo real

- **Planificador de procesos**: el proceso con mayor prioridad se ejecuta primero
- **Mediana en streaming**: un max-heap y un min-heap combinados
- **Algoritmo de Dijkstra**: encontrar caminos mas cortos en grafos
- **Merge de K listas ordenadas**: extraer el minimo de K cabezas
- **Compresion Huffman**: construir el arbol desde las frecuencias menores

## Errores comunes

1. **Confundir heap con BST**: en un heap, solo se garantiza la relacion padre-hijo, NO que el hijo izquierdo sea menor que el derecho.
2. **Asumir que el heap esta completamente ordenado**: el heap solo garantiza que la raiz es el min/max. Los demas niveles no estan ordenados.
3. **Olvidar que `heapq` de Python es min-heap**: no existe max-heap nativo. Negar valores o usar una clase wrapper.
4. **Modificar elementos sin re-heapificar**: si cambias un valor en el array, debes llamar a heapify o las operaciones sift correspondientes.
5. **Confundir heap (estructura) con heap (memoria)**: el heap de memoria (donde se almacenan objetos dinamicos) no tiene relacion con la estructura de datos heap.

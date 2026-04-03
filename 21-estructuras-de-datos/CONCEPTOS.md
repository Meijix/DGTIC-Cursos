# Modulo 21: Estructuras de Datos

## Indice de contenidos

1. [Que son las estructuras de datos?](#1-que-son-las-estructuras-de-datos)
2. [Panorama general](#2-panorama-general)
3. [Estructuras lineales](#3-estructuras-lineales)
4. [Estructuras asociativas](#4-estructuras-asociativas)
5. [Estructuras jerarquicas](#5-estructuras-jerarquicas)
6. [Estructuras de relacion](#6-estructuras-de-relacion)
7. [Tabla comparativa](#7-tabla-comparativa)
8. [Arbol de decision](#8-arbol-de-decision)
9. [Mapa del modulo](#9-mapa-del-modulo)

---

## 1. Que son las estructuras de datos?

Una estructura de datos es una forma de **organizar, almacenar y acceder** a datos de manera eficiente. Elegir la estructura correcta es tan importante como elegir el algoritmo correcto: la misma operacion puede ser O(1) con una estructura y O(n) con otra.

### La progresion del modulo

```
  LINEALES             ASOCIATIVAS       JERARQUICAS         RELACION
  ========             ===========       ============        ========

  Arrays               Tablas Hash       Arboles (BST/AVL)   Grafos
  Listas enlazadas                       Heaps
  Pilas (LIFO)
  Colas (FIFO)

  Mas simples ─────────────────────────────────────────> Mas complejas
  Datos secuenciales ──────────────────────> Relaciones complejas
```

---

## 2. Panorama general

Las 8 estructuras del modulo cubren las necesidades fundamentales de la programacion:

```
  +-----------+    +------------------+    +--------+    +--------+
  |  Arrays   |    | Listas enlazadas |    | Pilas  |    | Colas  |
  | Acceso    |    | Insercion/elim.  |    | LIFO   |    | FIFO   |
  | por indice|    | eficiente        |    | Undo   |    | Turnos |
  | O(1)      |    | O(1) en extremos |    | DFS    |    | BFS    |
  +-----------+    +------------------+    +--------+    +--------+

  +-------------+    +---------+    +--------+    +---------+
  | Tablas Hash |    | Arboles |    | Heaps  |    | Grafos  |
  | Clave-valor |    | BST/AVL |    | Cola de|    | Redes   |
  | Busqueda    |    | Datos   |    | priori-|    | Caminos |
  | O(1) prom.  |    | ordenados|   | dad    |    | BFS/DFS |
  +-------------+    +---------+    +--------+    +---------+
```

---

## 3. Estructuras lineales

Las estructuras lineales almacenan datos en secuencia, una despues de otra.

### Arrays

Elementos contiguos en memoria con acceso directo por indice.

```
Indice:  0     1     2     3     4
       +-----+-----+-----+-----+-----+
       | 10  | 20  | 30  | 40  | 50  |
       +-----+-----+-----+-----+-----+
       Acceso O(1)    Insercion en medio O(n)
```

### Listas enlazadas

Nodos dispersos en memoria, conectados por punteros.

```
Simple:   [10|->] --> [20|->] --> [30|None]
Doble:    [<-|10|->] <-> [<-|20|->] <-> [<-|30|->]
Circular: [10|->] --> [20|->] --> [30|->] --+
           ^------------------------------------+
```

### Pilas (LIFO: Last In, First Out)

Solo se opera por el tope. Como una pila de platos.

```
  push(40)        pop() -> 40
     |               |
     v               v
  +------+       +------+
  |  40  | tope  |  30  | nuevo tope
  +------+       +------+
  |  30  |       |  20  |
  +------+       +------+
  |  20  |       |  10  |
  +------+       +------+
```

Usos: call stack, Undo/Redo, parentesis balanceados, DFS.

### Colas (FIFO: First In, First Out)

Entra por un extremo, sale por el otro. Como una fila de personas.

```
  enqueue(60)                          dequeue() -> 10
     |                                      |
     v                                      v
   +----+----+----+----+----+
   | 60 | 50 | 40 | 30 | 10 | -->  sale 10
   +----+----+----+----+----+
   rear                front
```

Variantes: cola circular, cola de prioridad (heap), deque (doble extremo).

---

## 4. Estructuras asociativas

### Tablas Hash

Mapean claves a valores usando una funcion hash. Acceso O(1) promedio.

```
  Clave          Funcion Hash       Tabla
  "ana"  ----->  hash("ana")=2  --> [2] "ana":"Ingeniera"
  "bob"  ----->  hash("bob")=5  --> [5] "bob":"Doctor"

  Colision (misma posicion):
  [2] --> ["ana":"Ing."] --> ["dan":"Chef"] --> None
           (encadenamiento)
```

En Python: `dict` (clave-valor) y `set` (solo claves) son tablas hash.

---

## 5. Estructuras jerarquicas

### Arboles (BST y AVL)

Estructura jerarquica donde cada nodo tiene un padre y cero o mas hijos. En un BST, el subarbol izquierdo es menor y el derecho es mayor.

```
  BST balanceado:              BST desbalanceado (degenerado):

         [8]                   [1]
        /   \                     \
      [4]   [12]                  [2]
      / \   / \                      \
    [2] [6][10][14]                  [3]    <-- opera como lista O(n)
                                        \
  Busqueda: O(log n)                    [4]
```

Los arboles AVL se autobalancean con rotaciones, garantizando O(log n).

### Heaps (Monticulos)

Arbol binario completo con propiedad de heap. Se almacena como array.

```
  Min-Heap:                    Como array:
       [1]                     [1, 3, 2, 7, 6, 5]
      /   \
    [3]   [2]                  Padre de i:     (i-1) // 2
   /   \  /                    Hijo izquierdo: 2*i + 1
 [7]  [6][5]                   Hijo derecho:   2*i + 2
```

Uso principal: colas de prioridad, algoritmo de Dijkstra, heapsort.

---

## 6. Estructuras de relacion

### Grafos

La estructura mas general: modela relaciones entre objetos.

```
  No dirigido:        Dirigido:          Ponderado:
  [A]---[B]           [A]-->[B]          [A]--5--[B]
   |  \  |             |  \  |            |  \    |
   |   \ |             v   v v            2   3   7
  [D]---[C]           [D]<--[C]          [D]--1--[C]
```

Se representan como **lista de adyacencia** (grafos dispersos) o **matriz de adyacencia** (grafos densos). Los algoritmos fundamentales son BFS (usa cola) y DFS (usa pila).

---

## 7. Tabla comparativa

| Estructura | Acceso | Busqueda | Insercion | Eliminacion | Espacio |
|------------|--------|----------|-----------|-------------|---------|
| **Array** | O(1) | O(n) | O(n)* | O(n)* | O(n) |
| **Lista enlazada** | O(n) | O(n) | O(1)** | O(1)** | O(n) |
| **Pila** | O(1) tope | O(n) | O(1) push | O(1) pop | O(n) |
| **Cola** | O(1) frente | O(n) | O(1) enqueue | O(1) dequeue | O(n) |
| **Tabla hash** | -- | O(1) prom. | O(1) prom. | O(1) prom. | O(n) |
| **BST (balanc.)** | -- | O(log n) | O(log n) | O(log n) | O(n) |
| **Heap** | O(1) min/max | O(n) | O(log n) | O(log n) | O(n) |
| **Grafo (lista adj.)** | -- | O(V+E) | O(1) | O(E) | O(V+E) |

*Insercion/eliminacion al final es O(1). En medio es O(n).
**Asumiendo que se tiene referencia al nodo.

---

## 8. Arbol de decision

```
  Necesitas almacenar datos...

  Necesitas acceso por indice?
  |
  +-- Si --> ARRAY
  |
  +-- No --> Necesitas busqueda rapida por clave?
             |
             +-- Si --> TABLA HASH
             |
             +-- No --> Los datos deben estar ordenados?
                        |
                        +-- Si --> Necesitas min/max rapido?
                        |          |
                        |          +-- Si --> HEAP
                        |          +-- No --> ARBOL BST/AVL
                        |
                        +-- No --> El orden de procesamiento importa?
                                   |
                                   +-- LIFO (ultimo en entrar) --> PILA
                                   +-- FIFO (primero en entrar) --> COLA
                                   +-- Muchas inserciones/eliminaciones --> LISTA ENLAZADA
                                   +-- Relaciones entre objetos --> GRAFO
```

### Reglas rapidas

- **Acceso por posicion**: Array
- **Insercion/eliminacion frecuente en extremos**: Lista enlazada o Deque
- **Revertir, deshacer, DFS**: Pila
- **Turnos, BFS, buffers**: Cola
- **Busqueda por clave O(1)**: Tabla hash
- **Datos ordenados con busqueda O(log n)**: Arbol BST/AVL
- **Acceso al minimo/maximo O(1)**: Heap
- **Relaciones complejas, redes, caminos**: Grafo

---

## 9. Mapa del modulo

| Seccion | Estructura | Concepto clave | Complejidad destacada |
|---------|------------|----------------|----------------------|
| 01-arrays | Arrays | Memoria contigua, acceso directo | Acceso O(1) |
| 02-listas-enlazadas | Listas enlazadas | Nodos con punteros, simple/doble/circular | Insercion O(1) |
| 03-pilas | Pilas | LIFO, push/pop | Todas las ops O(1) |
| 04-colas | Colas | FIFO, enqueue/dequeue, prioridad | Todas las ops O(1) |
| 05-tablas-hash | Tablas hash | Funcion hash, colisiones, factor de carga | Busqueda O(1) prom. |
| 06-arboles | Arboles BST/AVL | Jerarquia, recorridos, rotaciones | Busqueda O(log n) |
| 07-heaps | Heaps | Propiedad de heap, heapify, cola de prioridad | Min/max O(1) |
| 08-grafos | Grafos | Vertices/aristas, BFS, DFS, Dijkstra | BFS/DFS O(V+E) |

# Cheatsheet — Listas Enlazadas

## Diagrama rapido

```
Simple (singly linked):
 head
  |
  v
 [10|*]--> [20|*]--> [30|*]--> None

Doble (doubly linked):
 head                                    tail
  |                                       |
  v                                       v
 None <--[*|10|*]<-->[*|20|*]<-->[*|30|*]--> None

Circular:
       +-->[10|*]--> [20|*]--> [30|*]--+
       |                               |
       +-------------------------------+
```

```python
# Nodo basico
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None     # .prev para doble
```

## Operaciones — O(?)

| Operacion               | Simple | Doble | list Python |
|--------------------------|:------:|:-----:|:-----------:|
| Acceso por indice        | O(n)   | O(n)  | O(1)        |
| Busqueda                 | O(n)   | O(n)  | O(n)        |
| Prepend (inicio)         | O(1)   | O(1)  | O(n)        |
| Append (final, con tail) | O(1)   | O(1)  | O(1)*       |
| Insert despues de nodo   | O(1)   | O(1)  | O(n)        |
| Delete nodo conocido     | O(n)   | O(1)  | O(n)        |
| Reverse                  | O(n)   | O(n)  | O(n)        |

## Python en 30 segundos

```python
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, val):
        self.head = Node(val, self.head)

    def append(self, val):
        if not self.head:
            self.head = Node(val)
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = Node(val)

    def delete(self, val):
        if self.head and self.head.val == val:
            self.head = self.head.next
            return
        cur = self.head
        while cur and cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
                return
            cur = cur.next

    def reverse(self):
        prev, cur = None, self.head
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        self.head = prev
```

```python
# Alternativa practica: collections.deque (doble enlazada en C)
from collections import deque
d = deque([1, 2, 3])
d.appendleft(0)   # O(1) al inicio
d.append(4)        # O(1) al final
d.popleft()        # O(1) desde inicio
```

## Cuando usar / Cuando NO usar

- **Usar** cuando necesitas inserciones/eliminaciones O(1) al inicio o en medio (nodo conocido).
- **Usar** cuando el tamano varia mucho y no quieres redimensionamiento.
- **Usar** `deque` en Python en vez de implementar tu propia lista (es mas rapido y probado).
- **NO usar** si necesitas acceso aleatorio por indice -> usar array/list.
- **NO usar** si la localidad de cache importa (nodos dispersos en memoria).

## Errores clasicos

- **Perder la referencia a head:** si mueves `head` sin guardar referencia, pierdes toda la lista.
- **Olvidar el caso vacio:** siempre verificar `if not self.head` antes de operar.
- **Ciclos infinitos:** al recorrer una circular, necesitas condicion de paro (nodo == head).
- **Memory leak (otros lenguajes):** en C/C++ olvidar liberar nodos al eliminar.
- **Confundir doble con simple:** en doble debes actualizar AMBOS punteros (next y prev).

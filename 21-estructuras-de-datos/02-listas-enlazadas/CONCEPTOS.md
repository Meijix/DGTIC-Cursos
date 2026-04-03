# Listas Enlazadas

## Que es

Una **lista enlazada** es una estructura de datos lineal donde cada elemento (nodo) contiene un valor y una referencia (puntero) al siguiente nodo. A diferencia de los arrays, los elementos **no estan contiguos en memoria**, lo que permite inserciones y eliminaciones eficientes sin desplazar elementos.

## Diagrama

### Lista simplemente enlazada

```
Lista simple:
┌───────────┐    ┌───────────┐    ┌───────────┐
│ dato: 10  │    │ dato: 20  │    │ dato: 30  │
│ next: ─────┼──►│ next: ─────┼──►│ next: None│
└───────────┘    └───────────┘    └───────────┘
     head                              tail
```

### Lista doblemente enlazada

```
Lista doble:
         ┌────────────┐      ┌────────────┐      ┌────────────┐
None ◄───┤ prev       │  ┌──►│ prev       │  ┌──►│ prev       │
         │ dato: 10   │  │   │ dato: 20   │  │   │ dato: 30   │
         │ next: ──────┼──┘   │ next: ──────┼──┘   │ next: None │
         └────────────┘      └────────────┘      └────────────┘
              head                                     tail
```

### Lista circular

```
Lista circular:
┌───────────┐    ┌───────────┐    ┌───────────┐
│ dato: 10  │    │ dato: 20  │    │ dato: 30  │
│ next: ─────┼──►│ next: ─────┼──►│ next: ─────┼──┐
└───────────┘    └───────────┘    └───────────┘  │
     ▲                                            │
     └────────────────────────────────────────────┘
```

## Operaciones principales

| Operacion               | Simple  | Doble   | Descripcion                           |
|-------------------------|---------|---------|---------------------------------------|
| Acceso por indice       | O(n)    | O(n)    | Recorrer desde head hasta posicion    |
| Insercion al inicio     | O(1)    | O(1)    | Crear nodo y apuntar a head           |
| Insercion al final      | O(n)*   | O(1)**  | Recorrer hasta tail e insertar        |
| Insercion en medio      | O(n)    | O(n)    | Buscar posicion + enlazar (enlace O(1))|
| Eliminacion al inicio   | O(1)    | O(1)    | Mover head al siguiente               |
| Eliminacion al final    | O(n)    | O(1)    | Necesita el penultimo nodo            |
| Busqueda                | O(n)    | O(n)    | Recorrer nodo por nodo                |

*O(1) si se mantiene referencia al tail.
**La lista doble siempre mantiene referencia a tail.

## Como funciona

### Insercion al inicio

```
Antes:
head ──► [10] ──► [20] ──► [30] ──► None

Insertar 5 al inicio:
1. Crear nodo [5]
2. nodo.next = head
3. head = nodo

Despues:
head ──► [5] ──► [10] ──► [20] ──► [30] ──► None
```

### Eliminacion de un nodo

```
Eliminar nodo con valor 20:

Antes:
[10] ──► [20] ──► [30] ──► None

1. Encontrar nodo anterior (10)
2. anterior.next = nodo_a_eliminar.next

Despues:
[10] ──────────► [30] ──► None
         [20] (se libera)
```

### Estructura del nodo en Python

```
class Nodo:              class NodoDoble:
    dato = valor             dato = valor
    next = siguiente         next = siguiente
                             prev = anterior
```

## Cuando usarla

**Usar lista enlazada cuando:**
- Hay muchas inserciones/eliminaciones al inicio o en medio
- No se conoce el tamaño de antemano
- No necesitas acceso aleatorio por indice
- Implementas pilas, colas o listas de adyacencia para grafos

**NO usar lista enlazada cuando:**
- Necesitas acceso rapido por indice (usar array)
- La memoria es limitada (cada nodo tiene overhead de punteros)
- Necesitas buena localidad de cache (los nodos estan dispersos en memoria)

### Comparacion de tipos

```
                    Simple      Doble       Circular
Memoria por nodo    dato+1ptr   dato+2ptr   dato+1ptr
Recorrido reverso   No          Si          No (sin prev)
Insercion inicio    O(1)        O(1)        O(1)
Eliminacion tail    O(n)        O(1)        O(n)
Uso tipico          Pilas       Caches LRU  Round-robin
```

## Casos de uso en el mundo real

- **Historial del navegador**: lista doble (adelante/atras)
- **Reproductor de musica**: lista circular (repetir playlist)
- **Gestion de memoria**: listas de bloques libres en sistemas operativos
- **Cache LRU**: lista doble + tabla hash para acceso O(1)
- **Polinomios**: representar terminos con coeficiente y exponente

## Errores comunes

1. **Perder la referencia al head**: si sobreescribes head sin guardar referencia, pierdes toda la lista.
2. **No manejar el caso vacio**: siempre verificar si `head is None` antes de operar.
3. **Ciclos infinitos**: en listas circulares, olvidar la condicion de parada al recorrer.
4. **Fugas de memoria**: no desenlazar nodos correctamente al eliminar (en lenguajes sin garbage collector).
5. **Olvidar actualizar tail**: al insertar/eliminar al final, actualizar la referencia a tail.

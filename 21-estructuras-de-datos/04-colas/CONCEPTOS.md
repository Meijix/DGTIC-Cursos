# Colas (Queues)

## Que es

Una **cola** (queue) es una estructura de datos lineal que sigue el principio **FIFO** (First In, First Out): el primer elemento en entrar es el primero en salir. Funciona como una fila de personas esperando: el primero que llega es el primero en ser atendido.

## Diagrama

### Cola basica (FIFO)

```
  enqueue                                    dequeue
  (entrada)                                  (salida)
     │                                          │
     ▼                                          ▼
   ┌──────┬──────┬──────┬──────┬──────┐
   │  50  │  40  │  30  │  20  │  10  │ ──►  sale 10
   └──────┴──────┴──────┴──────┴──────┘
   rear/                           front/
   final                           frente
```

### Operacion enqueue (encolar)

```
enqueue(60):
Antes:  frente → [10, 20, 30, 40, 50] ← final
Despues: frente → [10, 20, 30, 40, 50, 60] ← final
```

### Operacion dequeue (desencolar)

```
dequeue() → retorna 10:
Antes:   frente → [10, 20, 30, 40, 50] ← final
Despues: frente → [20, 30, 40, 50] ← final
```

## Operaciones principales

| Operacion   | Complejidad | Descripcion                                |
|-------------|-------------|--------------------------------------------|
| enqueue(x)  | O(1)        | Agregar elemento al final                  |
| dequeue()   | O(1)        | Remover y retornar el elemento del frente  |
| peek/front()| O(1)        | Ver el elemento del frente sin removerlo   |
| is_empty()  | O(1)        | Verificar si la cola esta vacia            |
| size()      | O(1)        | Obtener el numero de elementos             |

## Como funciona

### Cola circular (eficiente en memoria)

Evita desperdiciar espacio al reutilizar posiciones liberadas:

```
Capacidad: 5     front=2, rear=4

  0     1     2     3     4
┌─────┬─────┬─────┬─────┬─────┐
│     │     │  30 │  40 │  50 │
└─────┴─────┴─────┴─────┴─────┘
              front        rear

Despues de enqueue(60) y enqueue(70):  rear vuelve al inicio

  0     1     2     3     4
┌─────┬─────┬─────┬─────┬─────┐
│  70 │     │  30 │  40 │  50 │
└─────┴─────┴─────┴─────┴─────┘
  rear        front

rear = (rear + 1) % capacidad
```

### Cola de prioridad

Los elementos salen segun su prioridad, no su orden de llegada:

```
Encolar tareas con prioridad (menor = mas urgente):

  enqueue("email", prioridad=3)
  enqueue("bug critico", prioridad=1)
  enqueue("reunion", prioridad=2)

Cola interna (organizada por prioridad):
┌─────────────────┬───────────────┬──────────────────┐
│ bug critico (1) │ reunion (2)   │ email (3)        │
└─────────────────┴───────────────┴──────────────────┘
  ▲ sale primero                     sale ultimo
```

### Deque (cola de doble extremo)

Permite insertar y remover por ambos extremos:

```
        ┌──────┬──────┬──────┬──────┐
◄──── │  10  │  20  │  30  │  40  │ ────►
──►── │      │      │      │      │ ◄────
        └──────┴──────┴──────┴──────┘
   push/pop                      push/pop
   izquierda                     derecha
```

## Cuando usarla

**Usar colas cuando:**
- Necesitas procesamiento en orden de llegada (FIFO)
- Implementas BFS (recorrido por niveles en grafos/arboles)
- Manejas tareas asincronas o buffers de datos
- Necesitas un sistema de turnos justo

**Usar cola de prioridad cuando:**
- Los elementos tienen diferentes urgencias
- Implementas algoritmos como Dijkstra o A*
- Necesitas un planificador de tareas

**Usar deque cuando:**
- Necesitas insertar/remover por ambos extremos eficientemente
- Implementas una ventana deslizante
- Necesitas funcionalidad de pila y cola simultaneamente

### En Python

```
from collections import deque      # Cola y Deque eficientes
import heapq                       # Cola de prioridad (ver Heaps)
from queue import Queue            # Cola thread-safe
```

## Casos de uso en el mundo real

- **Cola de impresion**: los documentos se imprimen en orden de envio
- **Servidores web**: cola de peticiones HTTP entrantes
- **BFS**: explorar grafos nivel por nivel
- **Buffer de teclado**: las teclas se procesan en orden de presion
- **Sistemas de mensajeria**: RabbitMQ, Kafka (colas de mensajes)
- **CPU scheduling**: Round Robin usa cola circular

## Errores comunes

1. **Usar lista como cola**: `list.pop(0)` en Python es O(n). Usar `collections.deque` con `popleft()` que es O(1).
2. **Dequeue en cola vacia**: siempre verificar `is_empty()` antes de hacer `dequeue()`.
3. **Confundir FIFO con LIFO**: si necesitas revertir orden, usa una pila.
4. **Cola circular llena**: no verificar si `(rear + 1) % capacidad == front` antes de encolar.
5. **Ignorar la cola de prioridad**: cuando el orden de procesamiento depende de la urgencia, una cola FIFO simple no es suficiente.

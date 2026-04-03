# Cheatsheet — Colas (Queues)

## Diagrama rapido

```
FIFO — First In, First Out

  enqueue(x)                          dequeue() -> sale primero
      |                                    |
      v                                    v
  +------+------+------+------+------+
  |  50  |  40  |  30  |  20  |  10  |
  +------+------+------+------+------+
  ^  REAR (final)          FRONT (frente)  ^

Cola circular (array fijo):
      front           rear
        |               |
        v               v
  +-----+-----+-----+-----+-----+
  |     |  A  |  B  |  C  |     |
  +-----+-----+-----+-----+-----+
    4     0     1     2     3
        (los indices se envuelven con % n)

Cola de prioridad (min-heap):
          1
         / \
        3   2       -> dequeue siempre retorna el minimo
       / \
      5   4
```

## Operaciones — O(?)

| Operacion   | deque  | Queue  | PriorityQueue | list (NO usar) |
|-------------|:------:|:------:|:-------------:|:--------------:|
| enqueue     | O(1)   | O(1)   | O(log n)      | O(1) append    |
| dequeue     | O(1)   | O(1)   | O(log n)      | O(n) pop(0)    |
| peek/front  | O(1)   | —      | —             | O(1)           |
| is_empty    | O(1)   | O(1)   | O(1)          | O(1)           |
| size        | O(1)   | O(1)   | O(1)          | O(1)           |

## Python en 30 segundos

```python
# --- Opcion 1: deque (la mas comun y rapida) ---
from collections import deque
q = deque()
q.append(10)         # enqueue (por la derecha)
q.append(20)
q.append(30)
x = q.popleft()      # dequeue -> 10 (por la izquierda)
front = q[0]          # peek -> 20

# --- Opcion 2: queue.Queue (thread-safe con bloqueo) ---
from queue import Queue
q = Queue(maxsize=100)   # 0 = sin limite
q.put(10)                # enqueue (bloquea si llena)
q.get()                  # dequeue (bloquea si vacia)
q.empty()                # True/False

# --- Opcion 3: PriorityQueue (menor valor sale primero) ---
from queue import PriorityQueue
pq = PriorityQueue()
pq.put(3)
pq.put(1)
pq.put(2)
pq.get()              # 1 (el menor)

# --- Opcion 4: heapq (heap sobre lista, mas eficiente) ---
import heapq
h = []
heapq.heappush(h, 3)
heapq.heappush(h, 1)
heapq.heappush(h, 2)
heapq.heappop(h)      # 1
# Para max-heap: insertar con signo negado

# --- Deque como cola circular con tamano fijo ---
buffer = deque(maxlen=5)
for i in range(10):
    buffer.append(i)   # descarta los mas viejos automaticamente
# buffer = deque([5, 6, 7, 8, 9], maxlen=5)
```

## Aplicaciones clasicas

- **BFS (busqueda en anchura):** explorar grafo nivel por nivel usando cola.
- **Scheduler / planificador:** procesos en espera atienden en orden de llegada.
- **Buffer de datos:** productor-consumidor, streaming, impresion de documentos.
- **Cache LRU:** deque para rastrear uso reciente (o `OrderedDict`).
- **Cola de mensajes:** sistemas distribuidos, tareas asincronas.

## Cuando usar / Cuando NO usar

- **Usar** cuando necesitas orden FIFO (primero en llegar, primero en salir).
- **Usar** `deque` para colas simples de alto rendimiento.
- **Usar** `PriorityQueue`/`heapq` cuando los elementos tienen prioridad.
- **Usar** `Queue` cuando multiples hilos producen/consumen.
- **NO usar** `list.pop(0)` como cola: es O(n) porque desplaza todos los elementos.
- **NO usar** cola si necesitas acceso aleatorio o LIFO -> usar lista o pila.

## Errores clasicos

- **`list.pop(0)` para dequeue:** es O(n). Usar `deque.popleft()` que es O(1).
- **Deadlock con Queue:** `q.get()` bloquea si la cola esta vacia; usar `q.get(timeout=5)` o `q.get_nowait()`.
- **Prioridad invertida:** `PriorityQueue` es min-heap; para max-heap negar los valores: `pq.put(-valor)`.
- **Olvidar maxlen en buffer:** sin `maxlen`, un `deque` crece sin limite y puede agotar memoria.
- **Comparar objetos en PriorityQueue:** si dos elementos tienen igual prioridad, Python intenta comparar el objeto. Usar tuplas `(prioridad, id_unico, objeto)`.

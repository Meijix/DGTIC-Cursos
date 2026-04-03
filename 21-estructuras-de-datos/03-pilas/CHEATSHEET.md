# Cheatsheet — Pilas (Stacks)

## Diagrama rapido

```
LIFO — Last In, First Out

         push(40)              pop() -> 40
            |                     ^
            v                     |
         +------+              +------+
  TOP -> |  40  |       TOP -> |  30  |
         +------+              +------+
         |  30  |              |  20  |
         +------+              +------+
         |  20  |              |  10  |
         +------+              +------+
         |  10  |
         +------+

  peek() -> retorna el TOP sin eliminarlo
```

## Operaciones — O(?)

| Operacion   | Complejidad | Descripcion                     |
|-------------|:-----------:|---------------------------------|
| push(x)     | O(1)        | Agrega elemento al tope         |
| pop()       | O(1)        | Elimina y retorna el tope       |
| peek/top()  | O(1)        | Retorna el tope sin eliminar    |
| is_empty()  | O(1)        | Verifica si la pila esta vacia  |
| size()      | O(1)        | Numero de elementos             |
| search(x)   | O(n)        | Buscar un elemento              |

## Python en 30 segundos

```python
# --- Opcion 1: list (lo mas comun) ---
stack = []
stack.append(10)       # push
stack.append(20)
stack.append(30)
top = stack.pop()      # 30
top = stack[-1]        # peek -> 20
empty = len(stack) == 0

# --- Opcion 2: deque (mas eficiente y thread-safe para append/pop) ---
from collections import deque
stack = deque()
stack.append(10)       # push
stack.pop()            # pop

# --- Opcion 3: LifoQueue (thread-safe con bloqueo) ---
from queue import LifoQueue
stack = LifoQueue()
stack.put(10)
stack.get()            # 10 (bloquea si vacia)
```

## Aplicaciones clasicas

```python
# 1. Validar parentesis balanceados
def parentesis_validos(s):
    pila = []
    pares = {')': '(', ']': '[', '}': '{'}
    for c in s:
        if c in '([{':
            pila.append(c)
        elif c in ')]}':
            if not pila or pila[-1] != pares[c]:
                return False
            pila.pop()
    return len(pila) == 0

# 2. Evaluar expresion postfija (notacion polaca inversa)
def eval_postfija(tokens):
    pila = []
    ops = {'+': lambda a,b: a+b, '-': lambda a,b: a-b,
           '*': lambda a,b: a*b, '/': lambda a,b: int(a/b)}
    for t in tokens:
        if t in ops:
            b, a = pila.pop(), pila.pop()
            pila.append(ops[t](a, b))
        else:
            pila.append(int(t))
    return pila[0]

# 3. Deshacer (Undo) — cada accion se apila, Ctrl+Z hace pop
# 4. Call stack — cada llamada a funcion se apila, al retornar hace pop
```

## Cuando usar / Cuando NO usar

- **Usar** para problemas de ultimo en entrar, primero en salir (LIFO).
- **Usar** para DFS (busqueda en profundidad), backtracking, parseo de expresiones.
- **Usar** para invertir secuencias o rastrear estado previo (undo, historial).
- **NO usar** si necesitas acceso a elementos intermedios -> usar lista o deque.
- **NO usar** si necesitas FIFO (primero en entrar, primero en salir) -> usar cola.

## Errores clasicos

- **Pop en pila vacia:** siempre verificar `if stack:` antes de `stack.pop()`.
- **Usar `stack[0]` como peek:** el tope es `stack[-1]`, no `stack[0]`.
- **Usar list como cola:** `list.pop(0)` es O(n); para FIFO usar `deque`.
- **Recursion infinita:** la pila de llamadas tiene limite (`sys.getrecursionlimit()`).
- **Confundir orden de operandos:** en postfija, `a` se apila antes que `b`, asi que `pop` da `b` primero.

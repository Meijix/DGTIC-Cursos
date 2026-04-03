# Cheatsheet — Arrays / Listas

## Diagrama rapido

```
Memoria contigua (array):
 Indice:   0     1     2     3     4
         +-----+-----+-----+-----+-----+
 Valor:  | 10  | 20  | 30  | 40  | 50  |
         +-----+-----+-----+-----+-----+
 Addr:   0x00  0x08  0x10  0x18  0x20    <- acceso directo por indice
```

## Operaciones — O(?)

| Operacion          | list (Python) | array.array | numpy.ndarray |
|--------------------|:-------------:|:-----------:|:-------------:|
| Acceso `a[i]`      | O(1)          | O(1)        | O(1)          |
| Busqueda `x in a`  | O(n)          | O(n)        | O(n)          |
| Append             | O(1)*         | O(1)*       | O(n)          |
| Insert en pos `i`  | O(n)          | O(n)        | O(n)          |
| Delete en pos `i`  | O(n)          | O(n)        | O(n)          |
| Slicing `a[i:j]`   | O(j-i)        | O(j-i)      | O(1) vista    |
| Sort               | O(n log n)    | O(n log n)  | O(n log n)    |

\* Amortizado. La lista se redimensiona al doble cuando se llena.

## Python en 30 segundos

```python
# --- Creacion ---
a = [1, 2, 3, 4, 5]
b = list(range(10))            # [0, 1, ..., 9]
c = [0] * 5                    # [0, 0, 0, 0, 0]

# --- Acceso y slicing ---
a[0]          # 1
a[-1]         # 5
a[1:4]        # [2, 3, 4]
a[::2]        # [1, 3, 5]  (paso de 2)
a[::-1]       # [5, 4, 3, 2, 1]  (invertir)

# --- Modificacion ---
a.append(6)           # agrega al final
a.insert(0, 0)        # inserta en posicion 0
a.pop()               # elimina y retorna el ultimo
a.remove(3)           # elimina la primera ocurrencia de 3
del a[1]              # elimina por indice

# --- Busqueda ---
3 in a                # True/False  — O(n)
a.index(3)            # indice de la primera ocurrencia

# --- Comprehensions ---
pares = [x for x in range(20) if x % 2 == 0]
matriz = [[0]*3 for _ in range(3)]   # 3x3 correcto

# --- array.array (tipo fijo, menos memoria) ---
from array import array
arr = array('i', [1, 2, 3])   # 'i' = enteros con signo

# --- numpy (operaciones vectorizadas) ---
import numpy as np
v = np.array([1, 2, 3])
v * 2                          # array([2, 4, 6])
```

## Cuando usar / Cuando NO usar

- **Usar** cuando necesitas acceso aleatorio rapido por indice.
- **Usar** cuando el tamano es conocido o crece principalmente al final.
- **Usar** `numpy` para calculo numerico masivo (vectorizado en C).
- **NO usar** si necesitas inserciones/eliminaciones frecuentes en medio -> lista enlazada.
- **NO usar** `list` para millones de numeros del mismo tipo -> `array.array` o `numpy`.

## Errores clasicos

- **Copia superficial:** `b = a` NO copia, ambos apuntan al mismo objeto. Usar `b = a[:]` o `b = a.copy()`.
- **Matriz con multiplicacion:** `[[0]*3]*3` crea 3 referencias a la MISMA fila. Usar comprehension.
- **IndexError:** acceder a `a[len(a)]` falla; el ultimo indice valido es `len(a)-1`.
- **Mutar mientras iteras:** `for x in a: a.remove(x)` salta elementos. Iterar sobre una copia.
- **`append` vs `extend`:** `a.append([4,5])` agrega UNA lista; `a.extend([4,5])` agrega DOS elementos.

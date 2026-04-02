# 02 — Estructuras de Datos en Python

## Índice

1. [Listas](#listas)
2. [Tuplas](#tuplas)
3. [Diccionarios](#diccionarios)
4. [Sets (Conjuntos)](#sets-conjuntos)
5. [Comprehensions](#comprehensions)
6. [Mutabilidad vs Inmutabilidad](#mutabilidad-vs-inmutabilidad)
7. [Unpacking y Desempaquetado](#unpacking-y-desempaquetado)
8. [Comparativa General](#comparativa-general)
9. [Errores Comunes](#errores-comunes)
10. [Ejercicios](#ejercicios)

---

## Listas

Las listas son **secuencias mutables y ordenadas** que pueden contener
elementos de cualquier tipo.

```python
mi_lista = [1, "hola", 3.14, True, [5, 6]]
```

### Anatomía de una lista

```
  Índice:    0       1       2      3      4
           ┌───────┬───────┬──────┬──────┬────────┐
           │   1   │"hola" │ 3.14 │ True │ [5, 6] │
           └───────┴───────┴──────┴──────┴────────┘
  Negativo: -5      -4      -3     -2     -1
```

### Métodos principales

| Método | Qué hace | Retorna | Modifica original |
|--------|----------|---------|-------------------|
| `.append(x)` | Agrega al final | `None` | Sí |
| `.extend(iter)` | Agrega cada elemento del iterable | `None` | Sí |
| `.insert(i, x)` | Inserta en posición i | `None` | Sí |
| `.remove(x)` | Elimina primera ocurrencia | `None` | Sí |
| `.pop(i)` | Elimina y devuelve el de posición i | Elemento | Sí |
| `.clear()` | Vacía la lista | `None` | Sí |
| `.index(x)` | Posición de primera ocurrencia | int | No |
| `.count(x)` | Cuenta ocurrencias | int | No |
| `.sort()` | Ordena in-place | `None` | Sí |
| `.reverse()` | Invierte in-place | `None` | Sí |
| `.copy()` | Copia superficial | list | No |

### Diferencia entre append y extend

```python
a = [1, 2]
a.append([3, 4])   # [1, 2, [3, 4]]  — agrega el OBJETO

b = [1, 2]
b.extend([3, 4])   # [1, 2, 3, 4]    — agrega cada ELEMENTO
```

### Slicing (misma sintaxis que strings)

```python
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
nums[2:5]     # [2, 3, 4]
nums[::2]     # [0, 2, 4, 6, 8]
nums[::-1]    # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
nums[3:7] = [30, 40]  # Reemplazo por slicing (modifica la lista)
```

---

## Tuplas

Las tuplas son **secuencias inmutables y ordenadas**. Se usan para datos
que no deben cambiar.

```python
coordenada = (10.5, 20.3)
rgb = (255, 128, 0)
singleton = (42,)    # ← la coma es NECESARIA para tuplas de un elemento
no_tupla = (42)      # Esto es solo el int 42 entre paréntesis
```

### Cuándo usar tuplas vs listas

| Criterio | Lista | Tupla |
|----------|-------|-------|
| Mutabilidad | Mutable | Inmutable |
| Uso típico | Colección de iguales | Registro de campos |
| Ejemplo | `[1, 2, 3, 4]` | `("Ana", 25, "CDMX")` |
| Como clave de dict | No | Sí |
| Rendimiento | Ligeramente más lenta | Ligeramente más rápida |

### Named tuples

```python
from collections import namedtuple
Punto = namedtuple("Punto", ["x", "y"])
p = Punto(3, 4)
print(p.x, p.y)  # 3 4 — acceso por nombre
```

---

## Diccionarios

Los diccionarios son **mapeos mutables** de claves a valores. Desde Python 3.7+,
preservan el orden de inserción.

```python
persona = {
    "nombre": "Ana",
    "edad": 25,
    "activo": True
}
```

### Representación conceptual

```
  Diccionario persona:
  ┌──────────────┬─────────┐
  │    Clave     │  Valor  │
  ├──────────────┼─────────┤
  │ "nombre"     │ "Ana"   │
  │ "edad"       │  25     │
  │ "activo"     │  True   │
  └──────────────┴─────────┘
```

### Métodos principales

| Método | Qué hace |
|--------|----------|
| `d[k]` | Accede al valor (KeyError si no existe) |
| `d.get(k, default)` | Accede al valor (devuelve default si no existe) |
| `d[k] = v` | Asigna o modifica |
| `d.pop(k)` | Elimina y devuelve el valor |
| `d.keys()` | Vista de claves |
| `d.values()` | Vista de valores |
| `d.items()` | Vista de pares (clave, valor) |
| `d.update(otro)` | Fusiona otro diccionario |
| `d.setdefault(k, v)` | Devuelve valor existente o inserta default |
| `d | otro` | Fusión (Python 3.9+, crea nuevo dict) |

### Requisitos para las claves

Las claves deben ser **hashable** (inmutables): `int`, `str`, `float`, `tuple`, `frozenset`.
Las listas, diccionarios y sets NO pueden ser claves.

---

## Sets (Conjuntos)

Los sets son **colecciones mutables, no ordenadas y sin duplicados**.

```python
vocales = {"a", "e", "i", "o", "u"}
numeros = {1, 2, 3, 2, 1}  # → {1, 2, 3} — sin duplicados
```

### Operaciones de conjuntos

```
  A = {1, 2, 3, 4}        B = {3, 4, 5, 6}

  Unión (A | B):           {1, 2, 3, 4, 5, 6}
  Intersección (A & B):    {3, 4}
  Diferencia (A - B):      {1, 2}
  Dif. simétrica (A ^ B):  {1, 2, 5, 6}
```

### Diagrama de Venn

```
       A                 B
  ┌─────────┐      ┌─────────┐
  │  1  2   │      │   5  6  │
  │      ┌──┼──────┼──┐      │
  │      │ 3│  4   │  │      │
  │      └──┼──────┼──┘      │
  └─────────┘      └─────────┘
        A & B = {3, 4}
```

### frozenset — versión inmutable

```python
inmutable = frozenset({1, 2, 3})
# inmutable.add(4)  # Error — no se puede modificar
# Puede ser clave de diccionario o elemento de otro set
```

---

## Comprehensions

Sintaxis concisa para crear listas, diccionarios y sets a partir de iterables.

### List comprehension

```python
# [expresion for variable in iterable if condicion]
cuadrados = [x**2 for x in range(10)]
pares = [x for x in range(20) if x % 2 == 0]
```

### Dict comprehension

```python
# {clave: valor for variable in iterable if condicion}
cuadrados = {x: x**2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

### Set comprehension

```python
# {expresion for variable in iterable if condicion}
vocales_en = {c for c in "murcielago" if c in "aeiou"}
# {'a', 'e', 'i', 'o', 'u'}
```

### Comprehensions anidadas

```python
# Aplanar lista de listas
matriz = [[1, 2], [3, 4], [5, 6]]
plana = [elem for fila in matriz for elem in fila]
# [1, 2, 3, 4, 5, 6]
```

### Cuándo NO usar comprehensions

- Si la lógica es compleja (más de 2 condiciones o ciclos anidados)
- Si necesitas efectos secundarios (print, append externo)
- Si la legibilidad se sacrifica

---

## Mutabilidad vs Inmutabilidad

```
  INMUTABLE                    MUTABLE
  ─────────                    ───────
  int, float, bool             list
  str                          dict
  tuple                        set
  frozenset                    bytearray
  bytes
```

### Por qué importa

```python
# Las variables apuntan a objetos. La asignación NO copia.
a = [1, 2, 3]
b = a         # b apunta al MISMO objeto que a
b.append(4)
print(a)      # [1, 2, 3, 4] — a también cambió

# Para copiar:
c = a.copy()          # Copia superficial (shallow copy)
d = a[:]              # También copia superficial
import copy
e = copy.deepcopy(a)  # Copia profunda (para listas anidadas)
```

### Copia superficial vs profunda

```
  Shallow copy:
  a = [[1, 2], [3, 4]]
  b = a.copy()
  b[0].append(99)
  print(a)  # [[1, 2, 99], [3, 4]] — ¡la sub-lista es compartida!

  Deep copy:
  c = copy.deepcopy(a)
  c[0].append(88)
  print(a)  # [[1, 2, 99], [3, 4]] — NO se afecta
```

---

## Unpacking y Desempaquetado

```python
# Desempaquetado básico
a, b, c = [1, 2, 3]

# Con asterisco (star unpacking)
primero, *medio, ultimo = [1, 2, 3, 4, 5]
# primero=1, medio=[2, 3, 4], ultimo=5

# Intercambio de valores
a, b = b, a

# En funciones con *args
def suma(*numeros):
    return sum(numeros)
suma(1, 2, 3)  # 6

# Desempaquetar al llamar
datos = [1, 2, 3]
suma(*datos)    # equivale a suma(1, 2, 3)
```

---

## Comparativa General

| Operación | list | tuple | dict | set |
|-----------|------|-------|------|-----|
| Acceso por índice | O(1) | O(1) | — | — |
| Acceso por clave | — | — | O(1) | — |
| Búsqueda `in` | O(n) | O(n) | O(1) | O(1) |
| Agregar al final | O(1)* | — | O(1)* | O(1)* |
| Insertar al inicio | O(n) | — | — | — |
| Eliminar | O(n) | — | O(1) | O(1) |
| Ordenado | Sí | Sí | Inserción (3.7+) | No |
| Duplicados | Sí | Sí | Claves no | No |

\* Amortizado

---

## Errores Comunes

| Error | Causa | Solución |
|-------|-------|----------|
| `IndexError` | Índice fuera de rango | Verificar `len()` |
| `KeyError` | Clave no existe en dict | Usar `.get()` |
| Mutación inesperada | Asignar lista sin copiar | Usar `.copy()` o `[:]` |
| `TypeError: unhashable` | Usar lista como clave de dict | Convertir a tupla |
| Tupla de un elemento | `(42)` no es tupla | Usar `(42,)` |
| `sort()` retorna None | `.sort()` modifica in-place | Usar `sorted()` si necesitas nueva lista |

---

## Ejercicios

### Nivel 1 — Listas y tuplas
1. Crea una lista con los números del 1 al 20 y extrae los múltiplos de 3.
2. Dada una lista de nombres, ordénalos alfabéticamente sin modificar la original.
3. Rota una lista N posiciones a la derecha (ej: `[1,2,3,4,5]` rotada 2 → `[4,5,1,2,3]`).

### Nivel 2 — Diccionarios
4. Cuenta la frecuencia de cada palabra en un texto.
5. Dado un diccionario de alumnos y calificaciones, encuentra al alumno con mejor promedio.
6. Fusiona dos diccionarios, sumando los valores de claves comunes.

### Nivel 3 — Sets
7. Dadas dos listas, encuentra los elementos comunes sin duplicados.
8. Verifica si una lista tiene todos los elementos únicos (sin duplicados).
9. Implementa una función que determine si dos strings son anagramas.

### Nivel 4 — Comprehensions
10. Crea un diccionario que mapee cada letra del alfabeto a su posición (a→1, b→2...).
11. Genera una lista con los primeros 20 números de Fibonacci usando un ciclo (no comprehension) y luego filtra los pares con comprehension.
12. Aplana una matriz 3x3 a una lista simple con comprehension anidada.

### Nivel 5 — Integración
13. Implementa un sistema de inventario usando diccionarios: agregar, eliminar, buscar y listar productos.
14. Dado un texto largo, genera un reporte con: total de palabras, palabras únicas, las 5 más frecuentes.

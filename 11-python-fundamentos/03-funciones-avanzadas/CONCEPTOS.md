# 03 — Funciones Avanzadas

## Índice

1. [Funciones como Objetos de Primera Clase](#funciones-como-objetos-de-primera-clase)
2. [Closures (Clausuras)](#closures-clausuras)
3. [Lambdas](#lambdas)
4. [Funciones de Orden Superior](#funciones-de-orden-superior)
5. [*args y **kwargs](#args-y-kwargs)
6. [Type Hints (Anotaciones de Tipo)](#type-hints-anotaciones-de-tipo)
7. [functools](#functools)
8. [Errores Comunes](#errores-comunes)
9. [Ejercicios](#ejercicios)

---

## Funciones como Objetos de Primera Clase

En Python, las funciones son **objetos de primera clase** (first-class objects):

- Se pueden asignar a variables
- Se pueden pasar como argumentos
- Se pueden retornar desde otras funciones
- Se pueden almacenar en estructuras de datos

```python
def saludar(nombre):
    return f"Hola, {nombre}"

# Asignar a variable
mi_funcion = saludar
mi_funcion("Ana")  # "Hola, Ana"

# Almacenar en una lista
funciones = [len, str.upper, abs]
```

### Diagrama mental

```
  En Python, una función es un OBJETO como cualquier otro:

  ┌──────────────────────────┐
  │  Función "saludar"       │
  │  ────────────────        │
  │  tipo: function          │
  │  nombre: "saludar"       │
  │  código: ...             │
  │  __doc__: "..."          │
  └──────────────────────────┘
       ▲            ▲
       │            │
   saludar     mi_funcion    ← Dos variables apuntando al mismo objeto
```

---

## Closures (Clausuras)

Un closure es una función interna que **recuerda** las variables del scope
donde fue creada, incluso después de que ese scope haya terminado.

```
  Scope exterior
  ┌────────────────────────────┐
  │  variable_libre = valor    │
  │                            │
  │  ┌──────────────────────┐  │
  │  │  Función interior    │  │
  │  │  Usa variable_libre  │──┼── El closure "captura" esta variable
  │  └──────────────────────┘  │
  └────────────────────────────┘
```

### Patrón clásico: fábrica de funciones

```python
def crear_multiplicador(factor):
    def multiplicar(x):
        return x * factor  # 'factor' viene del scope exterior
    return multiplicar

doble = crear_multiplicador(2)
triple = crear_multiplicador(3)
doble(5)   # 10
triple(5)  # 15
```

### Reglas del closure

1. Debe existir una función anidada (función dentro de función)
2. La función interna debe referenciar variables del scope externo
3. La función externa debe retornar la función interna

---

## Lambdas

Funciones anónimas de una sola expresión.

```python
# Sintaxis: lambda parámetros: expresión
cuadrado = lambda x: x ** 2
suma = lambda a, b: a + b
```

### Cuándo usarlas

| Usar lambda | Usar def |
|-------------|----------|
| Funciones triviales de una línea | Lógica compleja |
| Argumentos de sort/map/filter | Funciones reutilizables |
| Callbacks simples | Necesitas docstring |

### Regla: si le pones nombre, usa def

```python
# MAL — lambda con nombre es un antipatrón
cuadrado = lambda x: x ** 2

# BIEN — usa def si necesitas un nombre
def cuadrado(x):
    return x ** 2
```

---

## Funciones de Orden Superior

Funciones que **reciben funciones** como argumento o **retornan funciones**.

### map(funcion, iterable)

Aplica una función a cada elemento.

```python
nums = [1, 2, 3, 4]
cuadrados = list(map(lambda x: x**2, nums))  # [1, 4, 9, 16]
# Equivalente: [x**2 for x in nums]
```

### filter(funcion, iterable)

Filtra elementos según una condición.

```python
nums = [1, 2, 3, 4, 5, 6]
pares = list(filter(lambda x: x % 2 == 0, nums))  # [2, 4, 6]
# Equivalente: [x for x in nums if x % 2 == 0]
```

### reduce(funcion, iterable)

Reduce un iterable a un solo valor, acumulando.

```python
from functools import reduce
producto = reduce(lambda acc, x: acc * x, [1, 2, 3, 4])  # 24
```

```
  reduce(f, [a, b, c, d])

  Paso 1: f(a, b)     → r1
  Paso 2: f(r1, c)    → r2
  Paso 3: f(r2, d)    → resultado final
```

### Comprehensions vs map/filter

En general, las comprehensions son más legibles en Python:

```python
# map + lambda → comprehension
list(map(lambda x: x*2, nums))   →   [x*2 for x in nums]

# filter + lambda → comprehension
list(filter(lambda x: x>3, nums))  →  [x for x in nums if x > 3]
```

---

## *args y **kwargs

### *args — argumentos posicionales variables

```python
def sumar(*numeros):
    return sum(numeros)

sumar(1, 2, 3)      # 6
sumar(1, 2, 3, 4, 5)  # 15
```

### **kwargs — argumentos con nombre variables

```python
def crear_perfil(**datos):
    return datos

crear_perfil(nombre="Ana", edad=25)
# {"nombre": "Ana", "edad": 25}
```

### Orden de parámetros

```python
def funcion(pos, /, pos_o_kw, *, solo_kw):
    pass
```

```
  Orden obligatorio de parámetros:
  ┌────────┬───────────┬──────────┬──────────┬──────────┐
  │ normal │ *args     │ keyword  │ **kwargs │          │
  │        │           │ -only    │          │          │
  └────────┴───────────┴──────────┴──────────┴──────────┘

  def f(a, b, *args, clave=True, **kwargs):
        ─┬──  ──┬──  ───┬────  ────┬──────
         │      │       │          │
    positional  │   keyword-only   │
              variable          catch-all
              positional        keyword
```

### Desempaquetado al llamar

```python
def sumar(a, b, c):
    return a + b + c

args = [1, 2, 3]
sumar(*args)        # Desempaqueta lista

kwargs = {"a": 1, "b": 2, "c": 3}
sumar(**kwargs)     # Desempaqueta diccionario
```

---

## Type Hints (Anotaciones de Tipo)

Python 3.5+ permite anotar tipos. Son **opcionales** y **no se verifican
en tiempo de ejecución** (son solo documentación y para herramientas como mypy).

```python
def saludar(nombre: str) -> str:
    return f"Hola, {nombre}"

edad: int = 25
nombres: list[str] = ["Ana", "Luis"]
```

### Tipos comunes

| Anotación | Significado |
|-----------|-------------|
| `int`, `str`, `float`, `bool` | Tipos primitivos |
| `list[int]` | Lista de enteros |
| `dict[str, int]` | Diccionario str→int |
| `tuple[int, str]` | Tupla de 2 elementos |
| `set[str]` | Set de strings |
| `int \| None` | Int o None (Python 3.10+) |
| `Optional[int]` | Int o None (antes de 3.10) |
| `Union[int, str]` | Int o str |
| `Callable[[int], str]` | Función int→str |
| `Any` | Cualquier tipo |

---

## functools

Módulo con herramientas para funciones de orden superior.

| Función | Qué hace |
|---------|----------|
| `reduce(f, iterable)` | Reduce a un solo valor |
| `partial(f, *args)` | Fija algunos argumentos |
| `lru_cache(maxsize)` | Memoización automática |
| `wraps(f)` | Preserva metadata en decoradores |
| `total_ordering` | Genera operadores de comparación |
| `cache` | Cache ilimitado (Python 3.9+) |

---

## Errores Comunes

| Error | Causa | Solución |
|-------|-------|----------|
| Lambda multilínea | Intentar lógica compleja en lambda | Usar def |
| Mutable default | `def f(lista=[])` | `def f(lista=None)` |
| Late binding closures | Closure en loop captura variable | Usar default arg `lambda x=x:` |
| `reduce` sin import | `reduce` no es builtin | `from functools import reduce` |
| Type hints incorrectos | Usar `List` en vez de `list` | `list[int]` (Python 3.9+) |

---

## Ejercicios

### Nivel 1
1. Crea una función `aplicar` que reciba una función y una lista, y retorne una nueva lista con la función aplicada a cada elemento.
2. Implementa una función `componer(f, g)` que retorne una nueva función que sea la composición f(g(x)).

### Nivel 2
3. Crea una fábrica de funciones `potencia(n)` que retorne una función que eleve a la n-ésima potencia.
4. Implementa tu propia versión de `map` y `filter` usando generadores.
5. Usa `reduce` para implementar `factorial(n)`.

### Nivel 3
6. Crea una función con type hints completos que reciba un diccionario de estudiantes y calificaciones y retorne estadísticas.
7. Implementa un sistema de pipeline donde puedas encadenar funciones: `pipeline(dato, [f1, f2, f3])`.
8. Usa `partial` para crear versiones especializadas de una función genérica de formato de números.

### Nivel 4
9. Implementa un sistema de memoización manual usando closures (sin `lru_cache`).
10. Crea un decorator factory que acepte parámetros (anticipo de sección 07).

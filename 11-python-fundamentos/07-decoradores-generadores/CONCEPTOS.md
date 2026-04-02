# 07 — Decoradores y Generadores

## Índice

1. [Decoradores — De Closure a Decorator](#decoradores)
2. [Decoradores con Argumentos](#decoradores-con-argumentos)
3. [functools.wraps](#functoolswraps)
4. [Decoradores Prácticos](#decoradores-prácticos)
5. [Generadores](#generadores)
6. [yield y Lazy Evaluation](#yield-y-lazy-evaluation)
7. [Expresiones Generadoras](#expresiones-generadoras)
8. [Protocolo de Iteradores](#protocolo-de-iteradores)
9. [itertools](#itertools)
10. [Errores Comunes](#errores-comunes)
11. [Ejercicios](#ejercicios)

---

## Decoradores

Un decorador es una función que **modifica el comportamiento** de otra función
sin cambiar su código. Es azúcar sintáctica para envolver funciones.

### Progresión: Closure → Wrapper → Decorator

```
  Paso 1: Función normal
  ─────────────────────────
  def saludar():
      return "Hola"

  Paso 2: Wrapper manual (closure)
  ─────────────────────────────────
  def wrapper():
      print("[LOG] Llamando función")
      resultado = saludar()
      print("[LOG] Función terminó")
      return resultado

  Paso 3: Wrapper genérico (decorador)
  ──────────────────────────────────────
  def logger(func):
      def wrapper(*args, **kwargs):
          print(f"[LOG] Llamando {func.__name__}")
          resultado = func(*args, **kwargs)
          print(f"[LOG] {func.__name__} terminó")
          return resultado
      return wrapper

  Paso 4: Sintaxis @decorador
  ────────────────────────────
  @logger
  def saludar():
      return "Hola"

  # Es equivalente a: saludar = logger(saludar)
```

### Diagrama visual

```
  @logger
  def saludar():
      return "Hola"

  Equivale a:
  ┌────────────┐
  │   logger   │ ← recibe 'saludar' original
  │ ┌────────┐ │
  │ │wrapper │ │ ← nueva función que envuelve a 'saludar'
  │ │ [LOG]  │ │
  │ │saludar()│ │
  │ │ [LOG]  │ │
  │ └────────┘ │
  └────────────┘
  saludar ──▶ ahora apunta a 'wrapper'
```

---

## Decoradores con Argumentos

Cuando el decorador necesita parámetros, se agrega un nivel
adicional de anidamiento (decorator factory).

```python
def repetir(veces):           # Nivel 1: factory (recibe argumentos)
    def decorador(func):       # Nivel 2: decorador (recibe función)
        def wrapper(*args, **kwargs):  # Nivel 3: wrapper
            for _ in range(veces):
                resultado = func(*args, **kwargs)
            return resultado
        return wrapper
    return decorador

@repetir(3)
def saludar():
    print("Hola")
```

---

## functools.wraps

Sin `@wraps`, el wrapper reemplaza los metadatos de la función original.

```python
from functools import wraps

def mi_decorador(func):
    @wraps(func)  # Preserva __name__, __doc__, __annotations__
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
```

---

## Decoradores Prácticos

| Decorador | Uso |
|-----------|-----|
| Timer | Medir tiempo de ejecución |
| Cache/Memoize | Cachear resultados |
| Retry | Reintentar en caso de error |
| Validate | Validar argumentos |
| Rate limit | Limitar frecuencia |
| `@property` | Getter/setter pythónico |
| `@staticmethod` | Método sin self |
| `@classmethod` | Método con cls |
| `@functools.lru_cache` | Cache LRU built-in |

---

## Generadores

Un generador es una función que usa `yield` en vez de `return`.
Produce valores **uno a la vez** (lazy evaluation), sin cargar
todo en memoria.

```python
def contar(n):
    i = 0
    while i < n:
        yield i    # Pausa aquí y devuelve i
        i += 1     # Continúa desde aquí en la siguiente llamada

gen = contar(3)
next(gen)  # 0
next(gen)  # 1
next(gen)  # 2
next(gen)  # StopIteration
```

### Generador vs Lista

```
  Lista: [0, 1, 2, ..., 999999]
  ───────────────────────────────
  Crea TODOS los valores en memoria
  Memoria: O(n)

  Generador: genera bajo demanda
  ───────────────────────────────
  Crea UN valor a la vez
  Memoria: O(1)
```

---

## yield y Lazy Evaluation

```
  Función normal:           Generador:
  ┌────────────────┐       ┌────────────────┐
  │ def f():       │       │ def g():       │
  │   return [1,2] │       │   yield 1      │
  │                │       │   yield 2      │
  └────────┬───────┘       └────────┬───────┘
           │                        │
      Calcula TODO             Pausa y resume
      de una vez               bajo demanda
```

### yield from — delegar a otro generador

```python
def subgenerador():
    yield 1
    yield 2

def generador():
    yield from subgenerador()  # Delega al subgenerador
    yield 3
```

---

## Expresiones Generadoras

Como list comprehensions pero con paréntesis. Son lazy.

```python
# List comprehension — crea toda la lista
cuadrados_lista = [x**2 for x in range(1000000)]

# Generator expression — calcula bajo demanda
cuadrados_gen = (x**2 for x in range(1000000))

# Uso directo en funciones
sum(x**2 for x in range(1000000))
```

---

## Protocolo de Iteradores

```
  Iterable                Iterator
  ────────                ────────
  Tiene __iter__()        Tiene __iter__() y __next__()

  list, str, dict...      Generadores, archivos abiertos...
  │                       │
  └── __iter__() ──▶      │ (retorna un iterator)
                          │
                          ├── __next__() → valor
                          ├── __next__() → valor
                          └── __next__() → StopIteration
```

---

## itertools

Módulo de la biblioteca estándar con herramientas para iteradores eficientes.

| Función | Qué hace |
|---------|----------|
| `chain(a, b)` | Concatena iterables |
| `islice(it, n)` | Toma n elementos |
| `count(start)` | Cuenta infinitamente |
| `cycle(it)` | Repite infinitamente |
| `repeat(v, n)` | Repite un valor |
| `product(a, b)` | Producto cartesiano |
| `permutations(it)` | Permutaciones |
| `combinations(it, n)` | Combinaciones |
| `groupby(it, key)` | Agrupar |
| `accumulate(it)` | Acumular |
| `zip_longest(a, b)` | Zip sin truncar |
| `filterfalse(f, it)` | Inverso de filter |
| `takewhile(f, it)` | Tomar mientras True |
| `dropwhile(f, it)` | Saltar mientras True |
| `starmap(f, it)` | map con unpacking |
| `tee(it, n)` | Duplicar iterador |

---

## Errores Comunes

| Error | Causa | Solución |
|-------|-------|----------|
| Pérdida de metadata | No usar `@wraps` | Agregar `@functools.wraps(func)` |
| Generador agotado | Iterar dos veces | Crear nuevo generador o convertir a lista |
| `return` en generador | return con valor (OK en 3.3+) | Usar `return` sin valor o `yield` |
| Decorador sin paréntesis | `@decorador` vs `@decorador()` | Consistencia según si acepta args |
| `StopIteration` | Llamar `next()` en gen agotado | Usar `next(gen, default)` |

---

## Ejercicios

### Nivel 1
1. Crea un decorador `@timer` que imprima el tiempo de ejecución.
2. Escribe un generador que produzca números de Fibonacci infinitamente.
3. Crea un generador que lea un archivo línea por línea (lazy).

### Nivel 2
4. Implementa un decorador `@retry(intentos=3)` con argumentos.
5. Crea un decorador `@cache` que memorice resultados (sin lru_cache).
6. Escribe un generador que aplane listas anidadas de cualquier profundidad.

### Nivel 3
7. Implementa un decorador `@validate_types` que verifique type hints en runtime.
8. Usa `itertools` para generar todas las combinaciones de un candado de 3 dígitos.
9. Crea una función generadora que simule la lectura paginada de una API.

### Nivel 4
10. Implementa tu propia versión de `itertools.chain`, `islice` y `groupby`.

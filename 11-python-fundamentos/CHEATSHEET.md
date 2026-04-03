# Cheatsheet — Fundamentos de Python (Modulo 11)

## Tipos de datos

| Tipo       | Ejemplo                | Mutable | Notas                     |
|------------|------------------------|---------|---------------------------|
| `int`      | `42`, `-7`, `0b1010`   | No      | Precision arbitraria      |
| `float`    | `3.14`, `1e-3`         | No      | IEEE 754 (64 bits)        |
| `bool`     | `True`, `False`        | No      | Subclase de `int`         |
| `str`      | `"hola"`, `'mundo'`    | No      | Unicode, inmutable        |
| `list`     | `[1, 2, 3]`           | Si      | Secuencia ordenada        |
| `tuple`    | `(1, 2, 3)`           | No      | Inmutable, puede ser clave de dict |
| `dict`     | `{"k": "v"}`          | Si      | Pares clave-valor, O(1) acceso |
| `set`      | `{1, 2, 3}`           | Si      | Sin duplicados, sin orden |
| `NoneType` | `None`                | No      | Valor nulo unico          |

```
Falsy: 0, 0.0, "", [], {}, set(), None, False
Truthy: todo lo demas
```

## Operadores

```
Aritmeticos:   +  -  *  /  //  %  **
               suma resta mult div div_entera modulo potencia

Comparacion:   ==  !=  <  >  <=  >=  is  is not
               (==: valor)    (is: misma identidad en memoria)

Logicos:       and  or  not    (con cortocircuito)

Walrus:        if (n := len(datos)) > 3:    # asigna y evalua
```

## Strings

```
Indexacion:   P  y  t  h  o  n
              0  1  2  3  4  5
             -6 -5 -4 -3 -2 -1

Slicing:  s[1:4] -> "yth"   s[::-1] -> invertida   s[::2] -> cada 2
```

| Metodo          | Ejemplo                          | Resultado       |
|-----------------|----------------------------------|-----------------|
| `.upper()`      | `"hola".upper()`                 | `"HOLA"`        |
| `.lower()`      | `"HOLA".lower()`                 | `"hola"`        |
| `.strip()`      | `" hi ".strip()`                 | `"hi"`          |
| `.split(sep)`   | `"a,b".split(",")`               | `["a","b"]`     |
| `.join(iter)`   | `",".join(["a","b"])`            | `"a,b"`         |
| `.replace(a,b)` | `"foo".replace("o","0")`         | `"f00"`         |
| `.find(sub)`    | `"hola".find("ol")`              | `1`             |

```python
# f-strings (recomendado)
f"Hola, {nombre}. Tienes {edad} anos."
f"{3.14159:.2f}"     # "3.14"
f"{'Python':>10}"    # Alineado a la derecha, ancho 10
```

## Estructuras de datos

### Listas

```python
lista = [1, 2, 3]
lista.append(4)         # [1, 2, 3, 4]       Agrega objeto
lista.extend([5, 6])    # [1, 2, 3, 4, 5, 6] Agrega elementos
lista.pop()             # 6 (elimina y retorna ultimo)
lista.sort()            # Ordena in-place, retorna None
sorted(lista)           # Retorna nueva lista ordenada
```

### Diccionarios

```python
d = {"nombre": "Ana", "edad": 25}
d["nombre"]             # "Ana" (KeyError si no existe)
d.get("tel", "N/A")     # "N/A" (default si no existe)
d.keys()                # Vista de claves
d.values()              # Vista de valores
d.items()               # Vista de pares (clave, valor)
d | otro                # Fusion (Python 3.9+)
```

### Sets

```
A = {1, 2, 3, 4}     B = {3, 4, 5, 6}

Union:          A | B  = {1, 2, 3, 4, 5, 6}
Interseccion:   A & B  = {3, 4}
Diferencia:     A - B  = {1, 2}
Dif. simetrica: A ^ B  = {1, 2, 5, 6}
```

### Complejidad

| Operacion         | list | dict | set  |
|-------------------|------|------|------|
| Acceso indice/key | O(1) | O(1) | --   |
| Busqueda `in`     | O(n) | O(1) | O(1) |
| Agregar           | O(1) | O(1) | O(1) |
| Eliminar          | O(n) | O(1) | O(1) |

## Comprehensions

```python
[x**2 for x in range(10)]                  # List comprehension
[x for x in range(20) if x % 2 == 0]       # Con filtro
{x: x**2 for x in range(5)}                # Dict comprehension
{c for c in "murcielago" if c in "aeiou"}  # Set comprehension
(x**2 for x in range(1000))                # Generator expression (lazy)
```

## Funciones

```python
def funcion(pos, /, pos_o_kw, *, solo_kw, **kwargs):
    pass
```

```
Orden obligatorio de parametros:
  normal -> *args -> keyword-only -> **kwargs

  def f(a, b, *args, clave=True, **kwargs):
```

```python
# *args: posicionales variables (tupla)
def sumar(*nums):       return sum(nums)

# **kwargs: keyword variables (dict)
def perfil(**datos):    return datos

# Desempaquetar al llamar
sumar(*[1, 2, 3])          # sumar(1, 2, 3)
funcion(**{"a": 1, "b": 2})  # funcion(a=1, b=2)

# Lambda (funciones anonimas de una expresion)
cuadrado = lambda x: x ** 2
# Regla: si le pones nombre, mejor usa def
```

### Funciones de orden superior

```python
list(map(lambda x: x**2, nums))        # -> [x**2 for x in nums]
list(filter(lambda x: x > 3, nums))    # -> [x for x in nums if x > 3]
from functools import reduce
reduce(lambda acc, x: acc * x, [1,2,3,4])  # 24
```

## Clases (POO)

```python
class Animal:
    total = 0                    # Atributo de clase (compartido)

    def __init__(self, nombre):  # Constructor
        self.nombre = nombre     # Atributo de instancia
        Animal.total += 1

    def hablar(self):            # Metodo de instancia
        raise NotImplementedError

    @classmethod
    def info(cls):               # Metodo de clase
        return f"Total: {cls.total}"

    @staticmethod
    def es_animal():             # Metodo estatico
        return True
```

### Herencia

```python
class Perro(Animal):
    def hablar(self):
        return "Guau!"

    def __init__(self, nombre, raza):
        super().__init__(nombre)   # Llamar al padre
        self.raza = raza
```

### Encapsulamiento

| Prefijo | Significado        | Acceso                  |
|---------|--------------------|-------------------------|
| (nada)  | Publico            | `self.nombre`           |
| `_`     | Protegido (conv.)  | `self._edad`            |
| `__`    | Privado (mangling) | `obj._Clase__saldo`     |

### @property

```python
class Cuenta:
    def __init__(self, saldo):
        self._saldo = saldo

    @property
    def saldo(self):           return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if valor < 0: raise ValueError("Negativo")
        self._saldo = valor
```

### Magic methods principales

| Metodo          | Se llama con         | Uso                |
|-----------------|----------------------|--------------------|
| `__init__`      | `Clase()`            | Constructor        |
| `__str__`       | `str(obj)` / `print` | Legible            |
| `__repr__`      | `repr(obj)` / REPL   | Tecnico            |
| `__eq__`        | `obj1 == obj2`       | Igualdad           |
| `__len__`       | `len(obj)`           | Longitud           |
| `__getitem__`   | `obj[key]`           | Acceso por indice  |
| `__iter__`      | `for x in obj`       | Iteracion          |
| `__call__`      | `obj()`              | Llamar como func   |

## Decoradores

```python
def mi_decorador(func):
    @wraps(func)               # Preserva metadata
    def wrapper(*args, **kwargs):
        print("antes")
        resultado = func(*args, **kwargs)
        print("despues")
        return resultado
    return wrapper

@mi_decorador                  # Equivale a: saludar = mi_decorador(saludar)
def saludar():
    return "Hola"

# Decorador con argumentos (factory)
def repetir(veces):
    def decorador(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(veces):
                resultado = func(*args, **kwargs)
            return resultado
        return wrapper
    return decorador

@repetir(3)
def saludar(): print("Hola")
```

## Generadores

```python
def contar(n):
    i = 0
    while i < n:
        yield i       # Pausa y devuelve valor
        i += 1        # Continua en la siguiente llamada

gen = contar(3)
next(gen)  # 0
next(gen)  # 1
```

```
Lista:      [0, 1, ..., 999999]  Memoria: O(n) - TODO en memoria
Generador:  genera bajo demanda   Memoria: O(1) - UN valor a la vez
```

## try / except / else / finally

```python
try:
    resultado = operacion()
except ValueError as e:            # Excepcion especifica
    print(f"Error: {e}")
except (TypeError, KeyError):      # Multiples tipos
    pass
else:                              # Solo si NO hubo error
    print("Exito")
finally:                           # SIEMPRE se ejecuta
    print("Limpieza")
```

```
Reglas:
  - except sin tipo captura TODO (mala practica)
  - except mas especifico PRIMERO
  - Usar `raise` (sin args) para re-lanzar preservando traceback
  - EAFP > LBYL en Python (pedir perdon > mirar antes de saltar)
```

### Context managers

```python
with open("archivo.txt") as f:    # Cierra automaticamente
    contenido = f.read()

# Crear uno propio con contextlib
from contextlib import contextmanager
@contextmanager
def mi_recurso():
    print("Abriendo")
    yield recurso
    print("Cerrando")
```

## Testing (pytest)

```python
# test_ejemplo.py
def test_suma():
    assert 1 + 1 == 2

def test_excepcion():
    with pytest.raises(ZeroDivisionError):
        1 / 0

# Patron AAA: Arrange -> Act -> Assert

# Ejecutar: pytest -v
# Un test:  pytest test_ejemplo.py::test_suma
# Parar 1er fallo: pytest -x
```

```python
# Fixtures
@pytest.fixture
def calculadora():
    return Calculadora()

def test_suma(calculadora):       # Inyectada automaticamente
    assert calculadora.sumar(3, 5) == 8

# Parametrize
@pytest.mark.parametrize("entrada, esperado", [
    (1, 1), (2, 4), (3, 9), (-2, 4),
])
def test_cuadrado(entrada, esperado):
    assert entrada ** 2 == esperado
```

## Errores comunes

| Error                          | Solucion                                 |
|--------------------------------|------------------------------------------|
| `=` en vez de `==`             | `if x == 5:` (comparar, no asignar)     |
| Mezclar tabs y espacios        | Usar siempre 4 espacios                  |
| `"str" + int`                  | Convertir: `str(42)` o f-string          |
| `(42)` no es tupla             | Usar `(42,)` con la coma                |
| `lista.sort()` retorna None   | Usar `sorted(lista)` si necesitas nueva  |
| `d["clave"]` KeyError          | Usar `d.get("clave", default)`           |
| `def f(lista=[])` mutable     | `def f(lista=None)` + if None dentro     |
| Olvidar `self` en metodos      | `def metodo(self, ...)`                  |
| `except:` sin tipo             | Siempre especificar el tipo de excepcion |
| `except: pass` silenciando     | Al menos loggear el error                |
| Closure en loop (late binding) | Usar default arg `lambda x=x:`           |
| Generador agotado              | Crear nuevo generador o convertir a lista|
| Decorador pierde metadata      | Usar `@functools.wraps(func)`            |

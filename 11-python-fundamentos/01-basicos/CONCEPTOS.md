# 01 — Básicos de Python

## Índice

1. [Variables y Tipos de Datos](#variables-y-tipos-de-datos)
2. [Operadores](#operadores)
3. [Strings (Cadenas de Texto)](#strings-cadenas-de-texto)
4. [Entrada y Salida (I/O)](#entrada-y-salida-io)
5. [Condicionales](#condicionales)
6. [Ciclos](#ciclos)
7. [Errores Comunes](#errores-comunes)
8. [Ejercicios](#ejercicios)

---

## Variables y Tipos de Datos

En Python, **no se declara el tipo** de una variable; el intérprete lo infiere
del valor asignado. Esto se llama **tipado dinámico**.

```
  Variable          Objeto en memoria
  ─────────         ──────────────────
  nombre ──────────▶ "Ana"  (str)
  edad   ──────────▶ 25     (int)
  pi     ──────────▶ 3.14   (float)
```

### Tipos primitivos principales

| Tipo | Ejemplo | Mutable | Notas |
|------|---------|---------|-------|
| `int` | `42`, `-7`, `0b1010` | No | Precisión arbitraria |
| `float` | `3.14`, `1e-3` | No | IEEE 754 (64 bits) |
| `bool` | `True`, `False` | No | Subclase de `int` |
| `str` | `"hola"`, `'mundo'` | No | Unicode por defecto |
| `NoneType` | `None` | No | Valor nulo único |
| `complex` | `3+4j` | No | Parte real e imaginaria |

### Funciones de inspección

```python
type(42)             # <class 'int'>
isinstance(42, int)  # True
isinstance(True, int)  # True — bool hereda de int
id(x)               # Dirección de memoria del objeto
```

### Conversiones (casting)

```python
int("42")       # 42
float("3.14")   # 3.14
str(100)        # "100"
bool(0)         # False
bool("")        # False
bool("hola")    # True
```

### Regla de truthiness

```
Falsy: 0, 0.0, "", [], {}, set(), None, False
Truthy: todo lo demás
```

---

## Operadores

### Aritméticos

| Operador | Nombre | Ejemplo | Resultado |
|----------|--------|---------|-----------|
| `+` | Suma | `3 + 2` | `5` |
| `-` | Resta | `3 - 2` | `1` |
| `*` | Multiplicación | `3 * 2` | `6` |
| `/` | División real | `7 / 2` | `3.5` |
| `//` | División entera | `7 // 2` | `3` |
| `%` | Módulo | `7 % 2` | `1` |
| `**` | Potencia | `2 ** 10` | `1024` |

### Comparación

| Operador | Significado |
|----------|-------------|
| `==` | Igual en valor |
| `!=` | Diferente en valor |
| `is` | Mismo objeto en memoria |
| `is not` | Distinto objeto |
| `<`, `>`, `<=`, `>=` | Orden |

**Cuidado:** `==` compara valores, `is` compara identidad (dirección de memoria).

```
  a = [1, 2]
  b = [1, 2]
  c = a

  a == b  → True   (mismo contenido)
  a is b  → False  (objetos distintos)
  a is c  → True   (misma referencia)
```

### Lógicos

| Operador | Descripción | Cortocircuito |
|----------|-------------|---------------|
| `and` | Verdadero si ambos lo son | Si el primero es falsy, no evalúa el segundo |
| `or` | Verdadero si al menos uno lo es | Si el primero es truthy, no evalúa el segundo |
| `not` | Negación | — |

### Asignación aumentada

```python
x += 1    # x = x + 1
x -= 2    # x = x - 2
x *= 3    # x = x * 3
x //= 4   # x = x // 4
x **= 2   # x = x ** 2
```

### Walrus operator (`:=`) — Python 3.8+

Asigna un valor y lo devuelve en la misma expresión.

```python
# Sin walrus — se calcula len() dos veces o se usa variable auxiliar
datos = [1, 2, 3, 4, 5]
n = len(datos)
if n > 3:
    print(f"Muchos datos: {n}")

# Con walrus — asignación inline
if (n := len(datos)) > 3:
    print(f"Muchos datos: {n}")
```

---

## Strings (Cadenas de Texto)

Las cadenas son **secuencias inmutables** de caracteres Unicode.

### Creación

```python
simple = 'comillas simples'
doble  = "comillas dobles"
triple = """cadena
multilínea"""
raw    = r"sin \n escape"   # raw string
```

### Indexación y slicing

```
  Cadena:    P  y  t  h  o  n
  Índice:    0  1  2  3  4  5
  Negativo: -6 -5 -4 -3 -2 -1
```

```python
s = "Python"
s[0]      # 'P'
s[-1]     # 'n'
s[1:4]    # 'yth'   — desde 1 hasta 3 (no incluye 4)
s[:3]     # 'Pyt'   — desde el inicio hasta 2
s[3:]     # 'hon'   — desde 3 hasta el final
s[::2]    # 'Pto'   — cada 2 caracteres
s[::-1]   # 'nohtyP' — invertida
```

### Métodos más usados

| Método | Qué hace | Ejemplo |
|--------|----------|---------|
| `.upper()` | Mayúsculas | `"hola".upper()` → `"HOLA"` |
| `.lower()` | Minúsculas | `"HOLA".lower()` → `"hola"` |
| `.strip()` | Quita espacios extremos | `" hi ".strip()` → `"hi"` |
| `.split(sep)` | Divide en lista | `"a,b,c".split(",")` → `["a","b","c"]` |
| `.join(iter)` | Une iterable | `",".join(["a","b"])` → `"a,b"` |
| `.replace(a,b)` | Reemplaza | `"foo".replace("o","0")` → `"f00"` |
| `.startswith()` | Verifica inicio | `"hola".startswith("ho")` → `True` |
| `.endswith()` | Verifica final | `"hola".endswith("la")` → `True` |
| `.find(sub)` | Posición de sub (-1 si no) | `"hola".find("ol")` → `1` |
| `.count(sub)` | Cuenta ocurrencias | `"banana".count("a")` → `3` |
| `.isdigit()` | Solo dígitos | `"123".isdigit()` → `True` |
| `.isalpha()` | Solo letras | `"abc".isalpha()` → `True` |

### Formateo de strings

```python
nombre = "Ana"
edad = 25

# f-strings (recomendado, Python 3.6+)
f"Hola, {nombre}. Tienes {edad} años."

# Expresiones dentro de f-strings
f"En 10 años tendrás {edad + 10} años."
f"{'Python':>10}"   # Alineación derecha, ancho 10
f"{3.14159:.2f}"     # "3.14" — 2 decimales

# .format()
"Hola, {}. Tienes {} años.".format(nombre, edad)

# % (estilo antiguo, no recomendado)
"Hola, %s. Tienes %d años." % (nombre, edad)
```

---

## Entrada y Salida (I/O)

```python
# Salida
print("Hola")
print("a", "b", "c", sep=", ", end="!\n")  # a, b, c!

# Entrada — siempre devuelve str
nombre = input("Tu nombre: ")
edad = int(input("Tu edad: "))  # Convertir manualmente
```

---

## Condicionales

### Estructura básica

```python
if condicion:
    # bloque si True
elif otra_condicion:
    # bloque alternativo
else:
    # si ninguna se cumplió
```

### Diagrama de flujo

```
          ┌──────────────┐
          │  condicion?   │
          └──────┬───────┘
           True  │  False
          ┌──────┘  └──────────┐
          ▼                    ▼
   ┌────────────┐     ┌──────────────┐
   │ bloque if  │     │ elif/else?   │
   └────────────┘     └──────────────┘
```

### Operador ternario

```python
resultado = "par" if x % 2 == 0 else "impar"
```

### Match-case (Python 3.10+)

```python
match comando:
    case "salir":
        print("Adiós")
    case "ayuda":
        print("Mostrando ayuda...")
    case _:
        print("Comando desconocido")
```

---

## Ciclos

### while

```python
contador = 0
while contador < 5:
    print(contador)
    contador += 1
```

### for

```python
# Iterar sobre una secuencia
for letra in "Python":
    print(letra)

# Iterar con range
for i in range(5):        # 0, 1, 2, 3, 4
    print(i)

for i in range(2, 10, 3): # 2, 5, 8
    print(i)
```

### Flujo de control en ciclos

```
  ┌──────────────────────────────────────────┐
  │  for elemento in iterable:               │
  │      if condicion_a:                     │
  │          continue   ──▶ salta al inicio  │
  │      if condicion_b:                     │
  │          break      ──▶ sale del ciclo   │
  │      # código normal                     │
  │  else:                                   │
  │      # se ejecuta si NO hubo break       │
  └──────────────────────────────────────────┘
```

### enumerate y zip

```python
nombres = ["Ana", "Luis", "Eva"]

# enumerate — índice + valor
for i, nombre in enumerate(nombres):
    print(f"{i}: {nombre}")

# zip — iterar en paralelo
edades = [25, 30, 22]
for nombre, edad in zip(nombres, edades):
    print(f"{nombre} tiene {edad} años")
```

---

## Errores Comunes

| Error | Causa | Solución |
|-------|-------|----------|
| `SyntaxError` | Olvidar `:` después de `if/for/while` | Revisar sintaxis |
| `IndentationError` | Mezclar tabs y espacios | Usar siempre 4 espacios |
| `TypeError: 'str' + int` | Concatenar str con int | Convertir: `str(42)` |
| `NameError` | Variable no definida | Verificar nombre y scope |
| Comparar con `=` | Usar `=` en vez de `==` | `if x == 5:` |
| Mutabilidad inesperada | Pasar lista como default | Usar `None` como default |

---

## Ejercicios

### Nivel 1 — Variables y tipos
1. Crea variables de cada tipo primitivo y muestra su tipo con `type()`.
2. Investiga qué pasa con `int("hola")`. ¿Qué error da?
3. ¿Cuál es la diferencia entre `10 / 3` y `10 // 3`?

### Nivel 2 — Strings
4. Dada la cadena `"Hola Mundo"`, obtén `"Mundo"` usando slicing.
5. Cuenta cuántas vocales tiene una cadena ingresada por el usuario.
6. Invierte una cadena sin usar funciones externas (solo slicing).

### Nivel 3 — Condicionales
7. Programa que determine si un año es bisiesto.
8. Calculadora básica: lee dos números y un operador (+, -, *, /), imprime el resultado.
9. Programa que clasifique una calificación (0-10) en: Reprobado, Suficiente, Bien, Notable, Sobresaliente.

### Nivel 4 — Ciclos
10. Imprime la tabla de multiplicar de un número dado.
11. Programa que encuentre todos los números primos menores a N.
12. Implementa el juego de "adivina el número" (el programa elige un número aleatorio y el usuario lo adivina).
13. FizzBuzz: imprime del 1 al 100, pero si es múltiplo de 3 imprime "Fizz", de 5 "Buzz", de ambos "FizzBuzz".

### Nivel 5 — Walrus operator
14. Usa el walrus operator para leer líneas del usuario hasta que escriba "salir", procesando cada línea en el mismo `while`.

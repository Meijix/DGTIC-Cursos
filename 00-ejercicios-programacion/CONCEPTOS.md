# Conceptos Fundamentales de Python - Modulo 11

Guia de referencia rapida para los conceptos de Python utilizados en los 15 ejercicios de este modulo.

---

## Tabla de Contenidos

1. [Variables y Tipos de Datos](#1-variables-y-tipos-de-datos)
2. [Operadores](#2-operadores)
3. [Entrada y Salida](#3-entrada-y-salida-inputoutput)
4. [Control de Flujo: Condicionales](#4-control-de-flujo-condicionales)
5. [Control de Flujo: Ciclos](#5-control-de-flujo-ciclos)
6. [Funciones](#6-funciones)
7. [Manejo de Errores: try/except](#7-manejo-de-errores-tryexcept)
8. [Modulos e Importaciones](#8-modulos-e-importaciones)
9. [Listas](#9-listas)
10. [Patrones de Validacion](#10-patrones-de-validacion-de-datos)
11. [Diagrama de Decision: for vs while](#11-diagrama-de-decision-for-vs-while)
12. [Tabla Completa de Operadores](#12-tabla-completa-de-operadores-de-python)
13. [Errores Comunes de Principiantes](#13-errores-comunes-de-principiantes-gotchas)
14. [Mapa de Progresion de Ejercicios](#14-mapa-de-progresion-de-ejercicios)
15. [Ejercicios de Practica Adicionales](#15-ejercicios-de-practica-adicionales)

---

## 1. Variables y Tipos de Datos

### Que es una variable?

Una variable es un **nombre** que se le asigna a un valor almacenado en memoria. En Python, no necesitas declarar el tipo de la variable; se determina automaticamente.

```python
# Asignacion simple
nombre = "Ana"        # str (cadena de texto)
edad = 25             # int (entero)
estatura = 1.65       # float (decimal)
es_estudiante = True  # bool (booleano)
```

### Tipos de datos basicos

| Tipo    | Descripcion              | Ejemplo            | Usado en Ejercicio |
|---------|--------------------------|--------------------|--------------------|
| `int`   | Numero entero            | `42`, `-7`, `0`    | 01, 02, 08, 14     |
| `float` | Numero con decimales     | `3.14`, `-0.5`     | 03, 04, 05, 06     |
| `str`   | Cadena de texto          | `"Hola"`, `'mundo'`| Todos              |
| `bool`  | Verdadero o Falso        | `True`, `False`    | 09, 10, 12         |
| `list`  | Lista ordenada           | `[1, 2, 3]`        | 11, 12             |
| `None`  | Ausencia de valor        | `None`             | 08                 |

### Conversion de tipos (casting)

```python
int("42")        # str -> int: 42
float("3.14")    # str -> float: 3.14
str(42)          # int -> str: "42"
int(3.99)        # float -> int: 3 (trunca, NO redondea)
float(42)        # int -> float: 42.0
bool(0)          # int -> bool: False
bool(1)          # int -> bool: True
bool("")         # str -> bool: False (cadena vacia)
bool("hola")     # str -> bool: True (cadena no vacia)
```

### Reglas para nombres de variables

```python
# VALIDOS
mi_variable = 1       # snake_case (recomendado en Python)
_privada = 2           # empieza con guion bajo
nombre2 = 3            # puede tener numeros (no al inicio)
CONSTANTE = 3.14       # MAYUSCULAS para constantes (convencion)

# INVALIDOS
2nombre = 1            # NO puede empezar con numero
mi-variable = 2        # NO puede tener guiones
mi variable = 3        # NO puede tener espacios
class = 4              # NO puede ser una palabra reservada
```

---

## 2. Operadores

### Operadores aritmeticos

```python
10 + 3    # Suma: 13
10 - 3    # Resta: 7
10 * 3    # Multiplicacion: 30
10 / 3    # Division: 3.3333... (siempre devuelve float)
10 // 3   # Division entera: 3 (descarta decimales)
10 % 3    # Modulo (residuo): 1
10 ** 3   # Potencia: 1000
```

### Operadores de comparacion

```python
5 == 5    # Igual a: True
5 != 3    # Diferente de: True
5 > 3     # Mayor que: True
5 < 3     # Menor que: False
5 >= 5    # Mayor o igual: True
5 <= 3    # Menor o igual: False
```

### Operadores logicos

```python
True and True    # True  (ambos deben ser True)
True and False   # False
True or False    # True  (al menos uno debe ser True)
False or False   # False
not True         # False (invierte el valor)
not False        # True
```

### Operadores de asignacion compuesta

```python
x = 10
x += 5    # x = x + 5  -> 15
x -= 3    # x = x - 3  -> 12
x *= 2    # x = x * 2  -> 24
x /= 4    # x = x / 4  -> 6.0
x //= 2   # x = x // 2 -> 3.0
x %= 2    # x = x % 2  -> 1.0
x **= 3   # x = x ** 3 -> 1.0
```

---

## 3. Entrada y Salida (Input/Output)

### input() - Leer datos del usuario

```python
# input() SIEMPRE devuelve un string
nombre = input("Como te llamas? ")           # tipo: str
edad = int(input("Cuantos años tienes? "))   # tipo: int
peso = float(input("Cuanto pesas? "))        # tipo: float
```

**Peligro:** Si el usuario escribe texto cuando esperas un numero:
```python
edad = int(input("Edad: "))  # Si escribe "abc" -> ValueError!
```

### print() - Mostrar informacion

```python
# Formas de usar print()
print("Hola mundo")                        # Texto simple
print("Edad:", 25)                         # Multiples argumentos (separados por espacio)
print("Hola", "mundo", sep="-")            # Separador personalizado: "Hola-mundo"
print("Sin salto", end="")                 # Sin salto de linea al final

# f-strings (la forma moderna y recomendada)
nombre = "Ana"
edad = 25
print(f"Hola {nombre}, tienes {edad} años")        # Variables
print(f"En 5 años tendras {edad + 5} años")        # Expresiones
print(f"Precio: ${100.5:.2f}")                      # Formato: "Precio: $100.50"
print(f"{'Centrado':^20}")                          # Alineacion

# Otras formas de formatear (menos recomendadas)
print("Hola " + nombre + ", tienes " + str(edad))   # Concatenacion
print("Hola {}, tienes {}".format(nombre, edad))     # .format()
print("Hola %s, tienes %d" % (nombre, edad))         # Estilo antiguo
```

---

## 4. Control de Flujo: Condicionales

### if / elif / else

```python
nota = 85

if nota >= 90:
    print("Excelente")      # Se ejecuta si nota >= 90
elif nota >= 80:
    print("Muy bien")       # Se ejecuta si 80 <= nota < 90
elif nota >= 70:
    print("Bien")           # Se ejecuta si 70 <= nota < 80
else:
    print("Necesita mejorar")  # Se ejecuta si nota < 70
```

### Reglas importantes

1. **Solo se ejecuta UN bloque** de toda la cadena if/elif/else
2. Las condiciones se evaluan **de arriba hacia abajo**
3. `elif` y `else` son **opcionales**
4. Puedes tener **multiples elif** pero solo **un else**
5. El orden importa: coloca las condiciones **mas especificas primero**

### Comparaciones encadenadas (exclusivo de Python)

```python
# En vez de:
if x >= 1 and x <= 10:

# Python permite:
if 1 <= x <= 10:    # Mucho mas legible!
```

### Operador ternario (condicional en una linea)

```python
edad = 20
mensaje = "Mayor" if edad >= 18 else "Menor"
# Equivalente a:
# if edad >= 18:
#     mensaje = "Mayor"
# else:
#     mensaje = "Menor"
```

### match/case (Python 3.10+)

```python
opcion = 2
match opcion:
    case 1:
        print("Opcion uno")
    case 2:
        print("Opcion dos")
    case 3:
        print("Opcion tres")
    case _:                     # _ es el "comodin" (equivale a else)
        print("Opcion invalida")
```

---

## 5. Control de Flujo: Ciclos

### Ciclo for (cuando sabes cuantas iteraciones)

```python
# Recorrer un rango de numeros
for i in range(5):            # 0, 1, 2, 3, 4
    print(i)

for i in range(2, 8):         # 2, 3, 4, 5, 6, 7
    print(i)

for i in range(0, 20, 3):     # 0, 3, 6, 9, 12, 15, 18
    print(i)

# Recorrer una lista
frutas = ["manzana", "pera", "uva"]
for fruta in frutas:
    print(fruta)

# Recorrer con indice
for i, fruta in enumerate(frutas):
    print(f"{i}: {fruta}")
```

### Ciclo while (cuando NO sabes cuantas iteraciones)

```python
# Repetir hasta que se cumpla una condicion
contador = 0
while contador < 5:
    print(contador)
    contador += 1    # IMPORTANTE: sin esto, ciclo infinito!

# Ciclo infinito controlado
while True:
    respuesta = input("Continuar? (s/n): ")
    if respuesta == "n":
        break        # Sale del ciclo
```

### break, continue y pass

```python
# break: Sale del ciclo inmediatamente
for i in range(10):
    if i == 5:
        break       # Sale cuando i es 5
    print(i)        # Imprime: 0, 1, 2, 3, 4

# continue: Salta a la siguiente iteracion
for i in range(10):
    if i % 2 == 0:
        continue    # Salta los pares
    print(i)        # Imprime: 1, 3, 5, 7, 9

# pass: No hace nada (placeholder)
for i in range(10):
    pass            # Aun no se que poner aqui
```

### Clausula else en ciclos (caracteristica unica de Python)

```python
# El else se ejecuta SOLO si el ciclo termino SIN break
for i in range(10):
    if i == 15:      # Nunca se cumple
        break
else:
    print("El ciclo termino sin break")  # SI se ejecuta

for i in range(10):
    if i == 5:       # Se cumple cuando i=5
        break
else:
    print("El ciclo termino sin break")  # NO se ejecuta
```

---

## 6. Funciones

### Definicion basica

```python
def saludar(nombre):
    """Funcion que saluda a una persona."""  # Docstring (documentacion)
    return f"Hola, {nombre}!"

# Llamada a la funcion
mensaje = saludar("Ana")
print(mensaje)  # "Hola, Ana!"
```

### Tipos de funciones

```python
# 1. Funcion con return (calcula y devuelve)
def sumar(a, b):
    return a + b

# 2. Funcion sin return (realiza una accion)
def mostrar_tabla(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

# 3. Funcion sin parametros
def menu():
    print("1. Opcion A")
    print("2. Opcion B")
    return int(input("Elige: "))

# 4. Funcion con valores por defecto
def potencia(base, exponente=2):
    return base ** exponente

potencia(5)       # 25 (usa exponente=2 por defecto)
potencia(5, 3)    # 125 (usa exponente=3)

# 5. Funcion con anotaciones de tipo (Python 3.5+)
def es_par(numero: int) -> bool:
    return numero % 2 == 0
```

### Alcance (scope) de variables

```python
x = "global"           # Variable GLOBAL

def mi_funcion():
    y = "local"         # Variable LOCAL (solo existe dentro de la funcion)
    print(x)            # Puede LEER variables globales
    print(y)            # Puede usar sus variables locales

mi_funcion()
print(x)               # "global" (accesible)
# print(y)             # ERROR! 'y' no existe fuera de la funcion
```

### Argumentos posicionales vs nombrados

```python
def crear_perfil(nombre, edad, ciudad):
    print(f"{nombre}, {edad} años, de {ciudad}")

# Posicionales: el orden IMPORTA
crear_perfil("Ana", 25, "CDMX")

# Nombrados (keyword): el orden NO importa
crear_perfil(ciudad="CDMX", nombre="Ana", edad=25)

# Mixtos: posicionales PRIMERO, luego nombrados
crear_perfil("Ana", ciudad="CDMX", edad=25)
```

---

## 7. Manejo de Errores: try/except

### Sintaxis basica

```python
try:
    numero = int(input("Ingresa un numero: "))
    resultado = 10 / numero
    print(f"Resultado: {resultado}")
except ValueError:
    print("Eso no es un numero!")
except ZeroDivisionError:
    print("No puedes dividir entre cero!")
except Exception as e:
    print(f"Error inesperado: {e}")
finally:
    print("Esto se ejecuta SIEMPRE")
```

### Excepciones comunes

| Excepcion            | Cuando ocurre                              | Ejemplo                    |
|----------------------|--------------------------------------------|----------------------------|
| `ValueError`         | Conversion de tipo invalida                | `int("abc")`               |
| `TypeError`          | Operacion con tipo incorrecto              | `"texto" + 5`              |
| `ZeroDivisionError`  | Division entre cero                        | `10 / 0`                   |
| `IndexError`         | Indice fuera de rango en lista             | `[1,2,3][10]`              |
| `KeyError`           | Clave inexistente en diccionario           | `{"a": 1}["b"]`            |
| `FileNotFoundError`  | Archivo no encontrado                      | `open("no_existe.txt")`    |
| `NameError`          | Variable no definida                       | `print(variable_no_existe)`|
| `AttributeError`     | Atributo/metodo no existe                  | `"hola".no_existe()`       |

### Patron robusto de validacion (Ejercicio 15)

```python
def pedir_entero(mensaje, minimo, maximo):
    """Pide un entero al usuario con validacion completa."""
    while True:
        try:
            valor = int(input(mensaje))
            if minimo <= valor <= maximo:
                return valor
            else:
                print(f"Debe estar entre {minimo} y {maximo}")
        except ValueError:
            print("Debe ingresar un numero entero")
```

---

## 8. Modulos e Importaciones

### Que es un modulo?

Un modulo es un archivo `.py` que contiene funciones, clases y variables que puedes reutilizar.

### Formas de importar

```python
# Importar el modulo completo
import random
numero = random.randint(1, 100)    # Necesitas el prefijo 'random.'

# Importar funciones especificas
from random import randint, choice
numero = randint(1, 100)           # Sin prefijo

# Importar con alias
import random as rnd
numero = rnd.randint(1, 100)

# Importar todo (NO recomendado)
from random import *               # Contamina el espacio de nombres
```

### Modulos utiles de la biblioteca estandar

```python
# random - Numeros aleatorios
import random
random.randint(1, 10)       # Entero aleatorio entre 1 y 10 (inclusivo)
random.random()             # Float entre 0.0 y 1.0
random.choice([1, 2, 3])   # Elige un elemento aleatorio de la lista
random.shuffle(lista)       # Mezcla la lista (modifica la original)

# math - Funciones matematicas
import math
math.sqrt(16)               # Raiz cuadrada: 4.0
math.pi                     # 3.141592653589793
math.ceil(3.2)              # Redondear hacia arriba: 4
math.floor(3.8)             # Redondear hacia abajo: 3

# time - Funciones de tiempo
import time
time.sleep(2)               # Pausa 2 segundos
time.time()                 # Timestamp actual en segundos

# datetime - Fechas y horas
from datetime import date
hoy = date.today()          # Fecha de hoy
```

---

## 9. Listas

### Operaciones basicas

```python
# Crear una lista
frutas = ["manzana", "pera", "uva", "naranja"]
numeros = [1, 2, 3, 4, 5]
mixta = [1, "hola", 3.14, True]     # Puede mezclar tipos
vacia = []                          # Lista vacia

# Acceso por indice (empieza en 0!)
frutas[0]     # "manzana" (primer elemento)
frutas[1]     # "pera" (segundo elemento)
frutas[-1]    # "naranja" (ultimo elemento)
frutas[-2]    # "uva" (penultimo)

# Longitud
len(frutas)   # 4

# Verificar si un elemento existe
"pera" in frutas        # True
"kiwi" in frutas        # False
"kiwi" not in frutas    # True

# Modificar
frutas[0] = "fresa"     # Cambiar primer elemento
frutas.append("kiwi")   # Agregar al final
frutas.insert(1, "mango")  # Insertar en posicion 1
frutas.remove("pera")   # Eliminar por valor
del frutas[0]           # Eliminar por indice
ultimo = frutas.pop()   # Eliminar y devolver el ultimo

# Slicing (rebanado)
frutas[1:3]   # Elementos del indice 1 al 2
frutas[:2]    # Primeros 2 elementos
frutas[2:]    # Desde el indice 2 hasta el final
frutas[::2]   # Cada 2 elementos
```

### Lista como tabla de busqueda (Ejercicio 11)

```python
# En vez de 12 condicionales if/elif:
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
         "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

numero_mes = 3
print(meses[numero_mes])  # "Abril" (indice 3 = cuarto elemento)
```

---

## 10. Patrones de Validacion de Datos

### Patron 1: while simple (Ejercicios 02-06)

```python
# Pedir dato y repetir si no es valido
numero = int(input("Numero entre 1 y 50: "))
while numero < 1 or numero > 50:
    print("Numero invalido")
    numero = int(input("Numero entre 1 y 50: "))
```

**Limitacion:** Si el usuario escribe "abc", el programa se detiene con error.

### Patron 2: while True + break (mas limpio)

```python
while True:
    numero = int(input("Numero entre 1 y 50: "))
    if 1 <= numero <= 50:
        break
    print("Numero invalido")
```

### Patron 3: while True + try/except (robusto) (Ejercicio 15)

```python
while True:
    try:
        numero = int(input("Numero entre 1 y 50: "))
        if 1 <= numero <= 50:
            break
        print("Debe estar entre 1 y 50")
    except ValueError:
        print("Debe ser un numero entero")
```

### Patron 4: Funcion reutilizable (mejor practica)

```python
def pedir_numero(mensaje, minimo, maximo):
    while True:
        try:
            valor = int(input(mensaje))
            if minimo <= valor <= maximo:
                return valor
            print(f"Debe estar entre {minimo} y {maximo}")
        except ValueError:
            print("Debe ser un numero entero")

# Uso
edad = pedir_numero("Tu edad: ", 1, 120)
mes = pedir_numero("Mes (1-12): ", 1, 12)
```

---

## 11. Diagrama de Decision: for vs while

```
Necesito repetir codigo?
|
+-- SI
|   |
|   +-- Se cuantas veces repetir?
|   |   |
|   |   +-- SI --> Usa FOR
|   |   |         Ejemplos:
|   |   |         - Imprimir numeros del 1 al 100
|   |   |         - Recorrer una lista
|   |   |         - Repetir algo exactamente N veces
|   |   |
|   |   +-- NO --> Usa WHILE
|   |             Ejemplos:
|   |             - Pedir datos hasta que sean validos
|   |             - Juego hasta que alguien gane
|   |             - Leer datos hasta encontrar un valor especifico
|   |
|   +-- Necesito salir antes de terminar?
|       |
|       +-- SI --> Usa BREAK dentro del ciclo
|       +-- NO --> El ciclo termina naturalmente
|
+-- NO --> No necesitas un ciclo
```

### Resumen rapido

| Situacion                                  | Usa        | Ejemplo en Ejercicio |
|--------------------------------------------|------------|----------------------|
| Recorrer numeros en un rango               | `for`      | 01, 02, 08, 13      |
| Pedir entrada hasta que sea valida         | `while`    | 02, 03, 04, 05, 06  |
| Numero fijo de rondas/intentos             | `while`    | 14, 15               |
| Recorrer elementos de una lista            | `for`      | 11                   |
| Repetir hasta que el usuario quiera salir  | `while True` + `break` | 15       |

---

## 12. Tabla Completa de Operadores de Python

### Operadores aritmeticos

| Operador | Nombre             | Ejemplo     | Resultado |
|----------|--------------------|-------------|-----------|
| `+`      | Suma               | `5 + 3`     | `8`       |
| `-`      | Resta              | `5 - 3`     | `2`       |
| `*`      | Multiplicacion     | `5 * 3`     | `15`      |
| `/`      | Division           | `5 / 3`     | `1.6667`  |
| `//`     | Division entera    | `5 // 3`    | `1`       |
| `%`      | Modulo (residuo)   | `5 % 3`     | `2`       |
| `**`     | Potencia           | `5 ** 3`    | `125`     |

### Operadores de comparacion

| Operador | Nombre             | Ejemplo     | Resultado |
|----------|--------------------|-------------|-----------|
| `==`     | Igual a            | `5 == 5`    | `True`    |
| `!=`     | Diferente de       | `5 != 3`    | `True`    |
| `>`      | Mayor que          | `5 > 3`     | `True`    |
| `<`      | Menor que          | `5 < 3`     | `False`   |
| `>=`     | Mayor o igual      | `5 >= 5`    | `True`    |
| `<=`     | Menor o igual      | `5 <= 3`    | `False`   |

### Operadores logicos

| Operador | Descripcion                    | Ejemplo              | Resultado |
|----------|--------------------------------|----------------------|-----------|
| `and`    | True si AMBOS son True         | `True and False`     | `False`   |
| `or`     | True si AL MENOS UNO es True   | `True or False`      | `True`    |
| `not`    | Invierte el valor              | `not True`           | `False`   |

### Operadores de pertenencia

| Operador  | Descripcion                         | Ejemplo               | Resultado |
|-----------|-------------------------------------|-----------------------|-----------|
| `in`      | True si esta en la coleccion        | `3 in [1,2,3]`        | `True`    |
| `not in`  | True si NO esta en la coleccion     | `4 not in [1,2,3]`    | `True`    |

### Operadores de identidad

| Operador  | Descripcion                           | Ejemplo          | Resultado |
|-----------|---------------------------------------|------------------|-----------|
| `is`      | True si son el MISMO objeto           | `x is None`      | Depende   |
| `is not`  | True si NO son el mismo objeto        | `x is not None`  | Depende   |

### Precedencia de operadores (de mayor a menor)

| Prioridad | Operadores                        |
|-----------|-----------------------------------|
| 1 (mayor) | `**`                              |
| 2         | `+x`, `-x`, `~x` (unarios)       |
| 3         | `*`, `/`, `//`, `%`              |
| 4         | `+`, `-`                          |
| 5         | `==`, `!=`, `>`, `<`, `>=`, `<=` |
| 6         | `not`                             |
| 7         | `and`                             |
| 8 (menor) | `or`                              |

**Consejo:** En caso de duda, usa parentesis `()` para hacer explicita la prioridad.

---

## 13. Errores Comunes de Principiantes (Gotchas)

### 1. Olvidar convertir input()

```python
# MAL - input() devuelve string
edad = input("Edad: ")
print(edad + 5)            # TypeError: no se puede sumar str + int

# BIEN
edad = int(input("Edad: "))
print(edad + 5)            # Funciona correctamente
```

### 2. Confundir = con ==

```python
# = es ASIGNACION
x = 5              # Guarda 5 en x

# == es COMPARACION
if x == 5:         # Pregunta: "x es igual a 5?"
    print("Si")
```

### 3. Indentacion incorrecta

```python
# MAL (IndentationError)
if True:
print("Hola")     # Falta la indentacion!

# BIEN
if True:
    print("Hola")  # 4 espacios de indentacion
```

### 4. range() no incluye el ultimo numero

```python
# Si quieres del 1 al 10:
for i in range(1, 10):     # Solo llega hasta 9!
    print(i)

for i in range(1, 11):     # CORRECTO: llega hasta 10
    print(i)
```

### 5. Modificar una lista mientras la recorres

```python
# MAL - Resultados impredecibles
numeros = [1, 2, 3, 4, 5]
for n in numeros:
    if n % 2 == 0:
        numeros.remove(n)  # Modifica la lista durante el recorrido!

# BIEN - Crear lista nueva
numeros = [1, 2, 3, 4, 5]
impares = [n for n in numeros if n % 2 != 0]
```

### 6. Variables locales vs globales

```python
x = 10

def cambiar():
    x = 20         # Crea una variable LOCAL nueva, NO modifica la global
    print(x)       # 20 (la local)

cambiar()
print(x)           # 10 (la global no cambio)
```

### 7. Comparar con == True/False (redundante)

```python
# REDUNDANTE
if es_valido == True:
    ...

# PYTHONICO (preferido)
if es_valido:
    ...

# REDUNDANTE
if es_valido == False:
    ...

# PYTHONICO (preferido)
if not es_valido:
    ...
```

### 8. Division entera inesperada

```python
# En Python 3, / siempre devuelve float
10 / 3      # 3.3333... (float)
10 / 2      # 5.0 (float, NO int!)

# Si necesitas un entero, usa //
10 // 3     # 3 (int)
10 // 2     # 5 (int)
```

### 9. Precision de flotantes

```python
0.1 + 0.2           # 0.30000000000000004 (NO exactamente 0.3!)
0.1 + 0.2 == 0.3    # False!

# Solucion: usar round() o comparar con tolerancia
round(0.1 + 0.2, 1) == 0.3    # True
abs((0.1 + 0.2) - 0.3) < 0.0001  # True
```

### 10. Ciclo while infinito

```python
# MAL - Olvidar actualizar la condicion
i = 0
while i < 5:
    print(i)
    # Falta: i += 1  -> El programa nunca termina!

# BIEN
i = 0
while i < 5:
    print(i)
    i += 1         # Actualizar la variable de control
```

---

## 14. Mapa de Progresion de Ejercicios

```
Ejercicio 01: for + modulo (%)
     |
     v
Ejercicio 02: Funciones + while (validacion) + input/int
     |
     v
Ejercicio 03: float + multiples parametros
     |
     +---> Ejercicio 04: Triangulo equilatero (1 parametro)
     |          |
     |          v
     |     Ejercicio 05: Triangulo isosceles (2 parametros)
     |          |
     |          v
     |     Ejercicio 06: Triangulo escaleno (3 parametros)
     |          |
     |          v
     |     Ejercicio 07: Unificacion (menus + if/elif)
     |
     v
Ejercicio 08: Funciones sin return + f-strings con expresiones
     |
     v
Ejercicio 09: Funciones booleanas + and
     |
     v
Ejercicio 10: Logica compleja (and/or) + type hints ----+
     |                                                    |
     v                                                    |
Ejercicio 11: Listas + comparaciones encadenadas --------+
     |                                                    |
     v                                                    v
Ejercicio 12: Combina Ej.10 + Ej.11 (reutilizar funciones)
     |
     v
Ejercicio 13: Ping Pong (orden de condiciones)
     |
     v
Ejercicio 14: import random + break + while/else
     |
     v
Ejercicio 15: try/except + time + estado del juego (CULMINACION)
```

---

## 15. Ejercicios de Practica Adicionales

### Nivel Basico (despues de Ej. 01-03)

1. **Numeros impares:** Modifica el Ejercicio 01 para imprimir solo los numeros impares del 1 al 99.

2. **Factorial:** Escribe una funcion que calcule el factorial de un numero (ej: 5! = 5 x 4 x 3 x 2 x 1 = 120).

3. **Temperatura:** Crea un convertidor de Celsius a Fahrenheit y viceversa. Formula: F = C * 9/5 + 32.

### Nivel Intermedio (despues de Ej. 04-09)

4. **Area de triangulo:** Extiende los ejercicios de triangulos para calcular tambien el area usando la formula de Heron.

5. **Clasificador de triangulos:** Dada las longitudes de 3 lados, determina si el triangulo es equilatero, isosceles o escaleno, Y si es acutangulo, rectangulo u obtusangulo.

6. **Tabla de multiplicar completa:** Imprime una tabla de multiplicar del 1 al 10 en formato de cuadricula alineada.

### Nivel Avanzado (despues de Ej. 10-15)

7. **Calendario:** Dado un mes y año, determina cuantos dias tiene y en que dia de la semana empieza.

8. **Piedra, papel o tijera:** Implementa el juego contra la computadora con sistema de puntos (mejor de 5).

9. **Ahorcado:** Implementa el juego del ahorcado donde la computadora elige una palabra y el usuario intenta adivinarla letra por letra.

10. **Cajero automatico:** Simula un cajero que permite depositar, retirar y consultar saldo, con validaciones completas y manejo de errores.

---

## Glosario Rapido

| Termino           | Significado                                                |
|--------------------|------------------------------------------------------------|
| **Variable**       | Nombre que almacena un valor en memoria                    |
| **Funcion**        | Bloque de codigo reutilizable con nombre                   |
| **Parametro**      | Variable que recibe una funcion en su definicion           |
| **Argumento**      | Valor que se pasa al llamar una funcion                    |
| **Return**         | Devuelve un valor desde una funcion                        |
| **Modulo**         | Archivo .py con funciones reutilizables                    |
| **Iterar**         | Recorrer elementos uno por uno (en un ciclo)               |
| **Acumulador**     | Variable que acumula valores (suma, contador)              |
| **Bandera (flag)** | Variable booleana que indica un estado                     |
| **Excepcion**      | Error que ocurre durante la ejecucion                      |
| **Indentacion**    | Espacios al inicio de linea que definen bloques de codigo  |
| **Scope (alcance)**| Zona del codigo donde una variable es accesible            |
| **Casting**        | Convertir un valor de un tipo a otro                       |
| **Pythonic**       | Forma idiomatica y elegante de escribir codigo Python      |
| **Game loop**      | Ciclo principal que controla la ejecucion de un juego      |
| **Booleano**       | Tipo de dato que solo puede ser True o False               |
| **Snake_case**     | Convencion de nombres: palabras_separadas_por_guion_bajo   |

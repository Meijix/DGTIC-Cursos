# Cheatsheet — Python Fundamentals (Modulo 00)

## Tipos de datos y conversion

| Tipo    | Ejemplo           | Conversion desde str     |
|---------|--------------------|--------------------------|
| `int`   | `42`, `-7`, `0`    | `int("42")`              |
| `float` | `3.14`, `-0.5`     | `float("3.14")`          |
| `str`   | `"Hola"`, `'mundo'`| ya es str                |
| `bool`  | `True`, `False`    | `bool("texto")` -> True  |

**Recuerda:** `int(3.99)` da `3` (trunca, NO redondea).

---

## Condicionales: if / elif / else

```python
if condicion:
    ...             # solo se ejecuta UN bloque
elif otra:
    ...
else:
    ...
```

Comparaciones encadenadas (exclusivo de Python):
```python
if 1 <= x <= 10:       # equivale a: x >= 1 and x <= 10
```

Operador ternario:
```python
msg = "Mayor" if edad >= 18 else "Menor"
```

---

## Ciclos: for vs while

```
Necesito repetir codigo?
|
+-- Se cuantas veces? ---> for i in range(n):
|
+-- NO se cuantas? ------> while condicion:
|
+-- Hasta que el usuario
    quiera salir? -------> while True: ... break
```

### range() -- cuidado, NO incluye el final

```python
range(5)          # 0, 1, 2, 3, 4
range(2, 8)       # 2, 3, 4, 5, 6, 7
range(0, 20, 3)   # 0, 3, 6, 9, 12, 15, 18
range(1, 11)      # 1 al 10 (usa n+1 para incluir n)
```

### break / continue

```python
for i in range(10):
    if i == 5: break       # sale del ciclo
    if i % 2 == 0: continue  # salta al siguiente
```

---

## Funciones

```python
def nombre_funcion(param1, param2=valor_default):
    """Docstring: describe la funcion."""
    # cuerpo
    return resultado
```

| Tipo                  | Ejemplo                          |
|-----------------------|----------------------------------|
| Con return            | `def sumar(a, b): return a + b`  |
| Sin return (accion)   | `def mostrar(x): print(x)`      |
| Valor por defecto     | `def f(x, y=2): return x ** y`  |

**Scope:** variables dentro de una funcion son locales; no modifican las globales.

---

## Entrada y salida

```python
nombre = input("Tu nombre: ")             # siempre devuelve str
edad   = int(input("Tu edad: "))           # convertir a int
peso   = float(input("Tu peso: "))         # convertir a float

print(f"Hola {nombre}, tienes {edad} anios")  # f-string (recomendado)
print(f"Precio: ${100.5:.2f}")                 # formato: $100.50
```

---

## Patron de validacion robusto

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
```

---

## Operadores: referencia rapida

| Operador  | Nombre           | Ejemplo          | Resultado |
|-----------|------------------|------------------|-----------|
| `+`       | Suma             | `5 + 3`          | `8`       |
| `-`       | Resta            | `5 - 3`          | `2`       |
| `*`       | Multiplicacion   | `5 * 3`          | `15`      |
| `/`       | Division (float) | `5 / 3`          | `1.667`   |
| `//`      | Division entera  | `5 // 3`         | `1`       |
| `%`       | Modulo           | `5 % 3`          | `2`       |
| `**`      | Potencia         | `5 ** 3`         | `125`     |
| `==`      | Igual a          | `5 == 5`         | `True`    |
| `!=`      | Diferente        | `5 != 3`         | `True`    |
| `and`     | Y logico         | `True and False` | `False`   |
| `or`      | O logico         | `True or False`  | `True`    |
| `not`     | Negacion         | `not True`       | `False`   |

---

## Errores comunes

| Error                                  | Problema                              | Solucion                                  |
|----------------------------------------|---------------------------------------|-------------------------------------------|
| `input()` sin convertir               | `"5" + 3` -> TypeError               | `int(input(...))`                         |
| `=` en vez de `==`                     | Asigna en lugar de comparar          | `if x == 5:` (doble igual)               |
| Indentacion incorrecta                 | IndentationError                      | Usar 4 espacios consistentemente          |
| `range(1, 10)` para llegar a 10       | Solo llega hasta 9                    | `range(1, 11)`                            |
| Ciclo `while` sin actualizar variable  | Ciclo infinito                        | No olvidar `i += 1` o usar `break`       |
| `0.1 + 0.2 == 0.3` es False           | Precision de flotantes                | `round(0.1 + 0.2, 1) == 0.3`             |
| Comparar con `== True`                 | Redundante                            | Usar `if es_valido:` directamente         |

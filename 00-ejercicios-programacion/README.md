# Ejercicios de Programacion con Python

Coleccion de 15 ejercicios practicos del curso introductorio de programacion de la **DGTIC-UNAM**. Los ejercicios estan disenados para recorrer de forma progresiva los fundamentos de Python: desde ciclos y funciones basicas hasta juegos interactivos con manejo de excepciones.

> **Nota:** Este material proviene originalmente de la carpeta `11-python-programacion` y fue reorganizado dentro de la estructura modular del repositorio.

---

## Tabla de ejercicios

| # | Nombre | Tema | Conceptos clave | Dificultad |
|:---:|--------|------|-----------------|:----------:|
| 01 | Numeros pares | Numeros pares del 0 al 100 | `for`, `range()`, modulo (`%`), f-strings | Basico |
| 02 | Suma consecutivos | Suma de consecutivos | Funciones, `while`, validacion de entrada | Basico |
| 03 | Dolares a pesos | Conversion de divisas | Funciones con multiples parametros, `float` | Basico |
| 04 | Equilatero | Perimetro triangulo equilatero | Funciones, formulas geometricas | Basico |
| 05 | Isosceles | Perimetro triangulo isosceles | Funciones con 2 params, validacion repetida | Basico |
| 06 | Escaleno | Perimetro triangulo escaleno | Funciones con 3 params, refactoring | Basico |
| 07 | Perimetro triangulo | Menu de triangulos | `if/elif/else`, menus, funciones que llaman funciones | Intermedio |
| 08 | Tablas de multiplicar | Tablas de multiplicar | Funciones sin `return`, expresiones en f-strings | Intermedio |
| 09 | Desigualdad del triangulo | Desigualdad del triangulo | Return booleano, `and`, cortocircuito | Intermedio |
| 10 | Es bisiesto | Ano bisiesto | Condicionales complejas (`and`/`or`), precedencia | Intermedio |
| 11 | Meses | Nombre del mes | Listas, indexacion desde 0, lookup tables | Intermedio |
| 12 | Fecha real | Validacion de fecha completa | Reutilizacion de funciones, `in`, flags | Intermedio |
| 13 | Ping Pong | Ping Pong (FizzBuzz) | Orden de condiciones, encapsulamiento | Intermedio |
| 14 | Adivina el numero | Adivina el numero | `import random`, `break`, `while/else` | Avanzado |
| 15 | Volados | Juego de volados con apuestas | `try/except`, gestion de estado, `time.sleep` | Avanzado |

---

## Mapa de progresion

Los ejercicios estan ordenados para construir conocimiento de forma acumulativa:

```
Basico (01-06)
  Ciclos y operadores ──> Funciones simples ──> Funciones con parametros
  01 Numeros pares        02 Suma consecutivos   03 Dolares a pesos
                          04 Equilatero           05 Isosceles
                                                  06 Escaleno
        |
        v
Intermedio (07-13)
  Composicion de funciones ──> Logica booleana ──> Estructuras de datos
  07 Menu de triangulos        09 Desigualdad      11 Meses
  08 Tablas de multiplicar     10 Bisiesto          12 Fecha real
                               13 Ping Pong

        |
        v
Avanzado (14-15)
  Modulos y control de flujo avanzado
  14 Adivina el numero (random, break, while/else)
  15 Volados (try/except, estado, time.sleep)
```

**Relaciones clave entre ejercicios:**

- **04 -> 05 -> 06 -> 07**: La serie de triangulos evoluciona de una funcion simple a un menu que integra las tres funciones anteriores.
- **10 -> 12**: El ejercicio de ano bisiesto se reutiliza dentro de la validacion completa de fechas.
- **09 -> 07**: La desigualdad del triangulo complementa el calculo de perimetros con validacion geometrica.
- **13**: Aplica el patron de condiciones multiples (similar a 07 y 10) en un contexto ludico.
- **14 -> 15**: Ambos son juegos interactivos; el ejercicio 15 suma manejo de excepciones y estado persistente.

---

## Como ejecutar los ejercicios

Cada ejercicio se encuentra en su propia carpeta (`Ejercicio-01_Numeros_pares`, `Ejercicio-02_Suma_consecutivos`, etc.) y contiene:

- **`ejercicioNN.py`** -- el codigo fuente ejecutable.
- **`ejercicioNN.md`** -- la descripcion del problema y notas del ejercicio.

### Requisitos

- Python 3.8 o superior.
- No se requieren dependencias externas.

### Ejecucion

```bash
# Ejemplo: ejecutar el ejercicio 01
cd Ejercicio-01_Numeros_pares
python3 ejercicio01.py

# Ejemplo: ejecutar el ejercicio 15
cd Ejercicio-15_Volados
python3 ejercicio15.py
```

Tambien puede consultarse el archivo [CONCEPTOS.md](CONCEPTOS.md) para una referencia rapida de los conceptos de Python que se cubren a lo largo de los ejercicios.

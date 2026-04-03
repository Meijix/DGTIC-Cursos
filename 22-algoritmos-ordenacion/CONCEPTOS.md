# Modulo 22: Algoritmos de Ordenacion

## Indice de contenidos

1. [Que es un algoritmo de ordenacion?](#1-que-es-un-algoritmo-de-ordenacion)
2. [Panorama general](#2-panorama-general)
3. [Algoritmos cuadraticos O(n^2)](#3-algoritmos-cuadraticos-on2)
4. [Algoritmos logaritmicos O(n log n)](#4-algoritmos-logaritmicos-on-log-n)
5. [Algoritmos lineales O(n)](#5-algoritmos-lineales-on)
6. [Estabilidad en la ordenacion](#6-estabilidad-en-la-ordenacion)
7. [Tabla comparativa](#7-tabla-comparativa)
8. [Arbol de decision](#8-arbol-de-decision)
9. [Mapa del modulo](#9-mapa-del-modulo)

---

## 1. Que es un algoritmo de ordenacion?

Un algoritmo de ordenacion reorganiza los elementos de una coleccion segun un criterio (numerico, alfabetico, por prioridad). Es una de las operaciones mas fundamentales en informatica: la busqueda binaria, la eliminacion de duplicados y muchos otros algoritmos requieren datos ordenados.

### La barrera O(n log n)

Se ha demostrado matematicamente que ningun algoritmo **basado en comparaciones** puede ordenar n elementos en menos de O(n log n) en el caso general. Los algoritmos no comparativos (Counting Sort, Radix Sort) logran O(n) al usar propiedades especificas de los datos.

---

## 2. Panorama general

Los 7 algoritmos del modulo progresan de simples e ineficientes a sofisticados y rapidos:

```
  CUADRATICOS O(n^2)         LOGARITMICOS O(n log n)      LINEALES O(n)
  ==================         =======================      =============

  Bubble Sort                Merge Sort                   Counting Sort
  Selection Sort             Quick Sort                   Radix Sort
  Insertion Sort

  Simples, educativos        Eficientes, uso general      Especializados
  Buenos para n pequeno      Dominan en la practica       Requieren restricciones
```

### Visualizacion de la progresion

```
  Tiempo
    ^
    |  *
    |  * *
    |  *   *    O(n^2): Bubble, Selection, Insertion
    |  *     *
    |  *       *  *  *  *  *  *  *  *  *
    |  *
    |  * *
    |  *  * *       O(n log n): Merge, Quick
    |  *    * * *
    |  *        * * * * * *
    |  * * * * * * * * * * * * *     O(n): Counting, Radix
    +-----------------------------------------> n
         10   100   1,000   10,000
```

---

## 3. Algoritmos cuadraticos O(n^2)

Estos tres algoritmos comparan e intercambian elementos. Son ineficientes para datos grandes pero utiles para arreglos pequenos y con fines educativos.

### Bubble Sort

Compara pares adyacentes e intercambia si estan desordenados. Los mayores "burbujean" al final.

```
  [5, 3, 8, 1, 2]
   ^  ^
   intercambio --> [3, 5, 8, 1, 2] --> ... --> [3, 5, 1, 2, | 8]
                                                              ordenado
  Cada pasada coloca un elemento mas en su posicion final.
```

### Selection Sort

Busca el minimo en la zona sin ordenar y lo coloca al inicio.

```
  | 29  10  14  37  13 |    Buscar minimo (10), intercambiar con arr[0]
  | 10 | 29  14  37  13 |   Buscar minimo (13), intercambiar con arr[1]
  | 10  13 | 29  14  37 |   ...y asi sucesivamente
```

### Insertion Sort

Toma cada elemento y lo desliza a su posicion correcta en la zona ordenada, como ordenar cartas en la mano.

```
  Mano:     Carta nueva:    Accion:
  [7]          4         <- deslizar antes de 7
  [4, 7]       5         <- deslizar entre 4 y 7
  [4, 5, 7]    2         <- deslizar al inicio
  [2, 4, 5, 7] 1         <- deslizar al inicio
  [1, 2, 4, 5, 7]        <- terminado
```

### Comparacion de los cuadraticos

| Caracteristica | Bubble | Selection | Insertion |
|----------------|--------|-----------|-----------|
| Mejor caso | O(n) | O(n^2) | O(n) |
| Intercambios | Muchos | Pocos O(n) | Desplazamientos |
| Estable | Si | No | Si |
| Casi ordenado | Bueno | Igual | Excelente |
| Uso practico | Educativo | Escrituras costosas | Arreglos pequenos |

---

## 4. Algoritmos logaritmicos O(n log n)

Los algoritmos eficientes de proposito general, basados en la estrategia "divide y venceras".

### Merge Sort

Divide el arreglo por la mitad recursivamente, luego mezcla las mitades ordenadas.

```
  DIVISION:                    MEZCLA:
  [38, 27, 43, 3]             [27, 38]  [3, 43]
     /        \                   \       /
  [38, 27]  [43, 3]          [3, 27, 38, 43]
   /   \     /   \
 [38] [27] [43] [3]

  log n niveles de division  x  n comparaciones por nivel = O(n log n)
```

### Quick Sort

Elige un pivote, particiona en menores/mayores, y ordena recursivamente cada parte.

```
  [6, 3, 8, 2, 7, 1, 5]    pivote = 5
                     ^
  Particion: [3, 2, 1]  5  [8, 7, 6]
              <menores>      <mayores>

  Ordenar recursivamente cada particion.
```

### Comparacion Merge vs Quick

| Caracteristica | Merge Sort | Quick Sort |
|----------------|------------|------------|
| Peor caso | O(n log n) | O(n^2) |
| Espacio extra | O(n) | O(log n) |
| Estable | Si | No |
| In-place | No | Si |
| Practica | Listas enlazadas | Arrays en memoria |
| Garantia | Siempre O(n log n) | Depende del pivote |

---

## 5. Algoritmos lineales O(n)

Rompen la barrera O(n log n) al **no comparar** elementos entre si. Usan propiedades de los datos (enteros, rango limitado).

### Counting Sort

Cuenta las ocurrencias de cada valor y usa sumas acumuladas para posicionar.

```
  Entrada: [4, 2, 2, 8, 3, 3, 1]    Rango: 0-8

  Conteo:    [0, 1, 2, 2, 1, 0, 0, 0, 1]
  Acumulado: [0, 1, 3, 5, 6, 6, 6, 6, 7]
                  ^     ^  ^              ^
                 1 elem  5 elem           7 elem
                  <= 1    <= 3            <= 8

  Salida:  [1, 2, 2, 3, 3, 4, 8]
```

Complejidad: O(n + k) donde k es el rango de valores. Ideal cuando k es pequeno.

### Radix Sort

Ordena digito por digito (unidades, decenas, centenas...) usando Counting Sort como subrutina estable.

```
  [170, 45, 75, 90, 802, 24, 2, 66]

  Por unidades: [170, 90, 802, 2, 24, 45, 75, 66]
  Por decenas:  [802, 2, 24, 45, 66, 170, 75, 90]
  Por centenas: [2, 24, 45, 66, 75, 90, 170, 802]
```

Complejidad: O(d * (n + k)) donde d es el numero de digitos y k es la base. Para enteros de 32 bits con base 256: O(4 * (n + 256)) que es efectivamente O(n).

---

## 6. Estabilidad en la ordenacion

Un algoritmo es **estable** si mantiene el orden relativo de los elementos con la misma clave.

```
  Entrada:  [(Ana, 85), (Bob, 90), (Carlos, 85)]
                   ^                    ^
                 misma nota           misma nota

  Estable:   [(Ana, 85), (Carlos, 85), (Bob, 90)]   Ana antes de Carlos (orden original)
  Inestable: [(Carlos, 85), (Ana, 85), (Bob, 90)]   Orden original no se preserva
```

### Por que importa

- Permite ordenar por multiples criterios encadenados (primero por apellido, luego por nota)
- Es esencial para Radix Sort (la subrutina debe ser estable)
- Bases de datos y UI esperan orden predecible para registros iguales

---

## 7. Tabla comparativa

| Algoritmo | Mejor | Promedio | Peor | Espacio | Estable | Tipo |
|-----------|-------|----------|------|---------|---------|------|
| **Bubble Sort** | O(n) | O(n^2) | O(n^2) | O(1) | Si | Comparativo |
| **Selection Sort** | O(n^2) | O(n^2) | O(n^2) | O(1) | No | Comparativo |
| **Insertion Sort** | O(n) | O(n^2) | O(n^2) | O(1) | Si | Comparativo |
| **Merge Sort** | O(n log n) | O(n log n) | O(n log n) | O(n) | Si | Comparativo |
| **Quick Sort** | O(n log n) | O(n log n) | O(n^2) | O(log n) | No | Comparativo |
| **Counting Sort** | O(n+k) | O(n+k) | O(n+k) | O(n+k) | Si | No comparativo |
| **Radix Sort** | O(d(n+k)) | O(d(n+k)) | O(d(n+k)) | O(n+k) | Si | No comparativo |

---

## 8. Arbol de decision

```
  Necesitas ordenar datos...

  Son enteros en un rango pequeno conocido?
  |
  +-- Si --> El rango k << n? --> COUNTING SORT
  |          Muchos digitos?  --> RADIX SORT
  |
  +-- No --> Son datos generales (comparables)?
             |
             +-- Pocos elementos (n < 50)?
             |   |
             |   +-- Casi ordenados? --> INSERTION SORT
             |   +-- No --> INSERTION SORT (aun eficiente para n pequeno)
             |
             +-- Muchos elementos (n >= 50)?
                 |
                 +-- Necesitas garantia O(n log n)? --> MERGE SORT
                 +-- Necesitas estabilidad?         --> MERGE SORT
                 +-- Necesitas minimo espacio?       --> QUICK SORT
                 +-- Caso general en memoria?        --> QUICK SORT
```

### Reglas rapidas

- **Arreglo pequeno o casi ordenado**: Insertion Sort
- **Caso general en memoria**: Quick Sort (con mediana de tres)
- **Garantia de rendimiento o estabilidad**: Merge Sort
- **Enteros en rango limitado**: Counting Sort
- **Numeros con muchos digitos pero rango de digitos fijo**: Radix Sort
- **Listas enlazadas**: Merge Sort (no necesita espacio extra)
- **Subparticiones dentro de Quick/Merge Sort**: Insertion Sort (< 15 elementos)

---

## 9. Mapa del modulo

| Seccion | Algoritmo | Familia | Complejidad promedio | Estable |
|---------|-----------|---------|---------------------|---------|
| 01-bubble-sort | Bubble Sort | Cuadratico | O(n^2) | Si |
| 02-selection-sort | Selection Sort | Cuadratico | O(n^2) | No |
| 03-insertion-sort | Insertion Sort | Cuadratico | O(n^2) | Si |
| 04-merge-sort | Merge Sort | Divide y venceras | O(n log n) | Si |
| 05-quick-sort | Quick Sort | Divide y venceras | O(n log n) | No |
| 06-counting-sort | Counting Sort | No comparativo | O(n + k) | Si |
| 07-radix-sort | Radix Sort | No comparativo | O(d(n + k)) | Si |

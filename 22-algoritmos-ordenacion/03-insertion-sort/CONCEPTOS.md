# Insertion Sort (Ordenamiento por Insercion)

## Que es

Insertion Sort funciona de la misma forma en que la mayoria de las personas
ordenan cartas en su mano: se toma una carta nueva y se desliza hacia la
izquierda hasta encontrar su posicion correcta entre las cartas ya ordenadas.
Es eficiente para arreglos pequenos o casi ordenados.

## Diagrama paso a paso

Arreglo inicial: `[7, 4, 5, 2, 1]`

```
Estado inicial:
  [7 | 4, 5, 2, 1]
   ok  sin ordenar

Paso 1: insertar 4 en la zona ordenada [7]
  clave = 4
  [7, _, 5, 2, 1]   ← 7 > 4, desplazar 7 a la derecha
  [_, 7, 5, 2, 1]   ← insertar 4 en la posicion vacia
  [4, 7 | 5, 2, 1]

Paso 2: insertar 5 en la zona ordenada [4, 7]
  clave = 5
  [4, 7, _, 2, 1]   ← 7 > 5, desplazar 7
  [4, _, 7, 2, 1]   ← 4 < 5, detener. Insertar 5 aqui
  [4, 5, 7 | 2, 1]

Paso 3: insertar 2 en la zona ordenada [4, 5, 7]
  clave = 2
  [4, 5, 7, _, 1]   ← 7 > 2, desplazar
  [4, 5, _, 7, 1]   ← 5 > 2, desplazar
  [4, _, 5, 7, 1]   ← 4 > 2, desplazar
  [_, 4, 5, 7, 1]   ← inicio del arreglo, insertar 2
  [2, 4, 5, 7 | 1]

Paso 4: insertar 1 en la zona ordenada [2, 4, 5, 7]
  clave = 1
  [2, 4, 5, 7, _]   ← 7 > 1, desplazar
  [2, 4, 5, _, 7]   ← 5 > 1, desplazar
  [2, 4, _, 5, 7]   ← 4 > 1, desplazar
  [2, _, 4, 5, 7]   ← 2 > 1, desplazar
  [_, 2, 4, 5, 7]   ← inicio, insertar 1
  [1, 2, 4, 5, 7]

Resultado final: [1, 2, 4, 5, 7]
```

Analogia con cartas en la mano:

```
  Mano:     Carta nueva:    Accion:
  [7]          4         ← deslizar 4 antes de 7
  [4, 7]       5         ← deslizar 5 entre 4 y 7
  [4, 5, 7]    2         ← deslizar 2 al inicio
  [2,4,5,7]    1         ← deslizar 1 al inicio
  [1,2,4,5,7]             ← terminado
```

## Complejidad

| Caso | Tiempo | Espacio |
|------|--------|---------|
| Mejor | O(n) | O(1) |
| Promedio | O(n^2) | O(1) |
| Peor | O(n^2) | O(1) |

**Estable:** Si

El mejor caso O(n) ocurre cuando el arreglo ya esta ordenado: cada elemento
se compara solo una vez con su antecesor y no se desplaza nada.

## Como funciona

1. Comenzar desde el segundo elemento (indice 1). El primer elemento por si
   solo ya esta "ordenado".
2. Guardar el elemento actual como `clave`.
3. Comparar la clave con los elementos a su izquierda, de derecha a izquierda.
4. Desplazar hacia la derecha cada elemento que sea mayor que la clave.
5. Insertar la clave en la posicion correcta (donde se detuvo el desplazamiento).
6. Avanzar al siguiente elemento y repetir hasta recorrer todo el arreglo.

## Cuando usarlo

- **Ideal para:** arreglos pequenos (< 50 elementos) o arreglos casi ordenados.
  Muchas implementaciones de Merge Sort y Quick Sort cambian a Insertion Sort
  cuando la subparticion es pequena (tipicamente < 10-15 elementos).
- **Ventaja sobre Bubble Sort:** generalmente hace menos comparaciones y
  es mas rapido en la practica para datos parcialmente ordenados.
- **Ventaja sobre Selection Sort:** es estable y se beneficia del orden
  existente. Caso mejor es O(n) vs O(n^2).
- **Desventaja frente a Merge/Quick Sort:** para arreglos grandes es O(n^2),
  mucho mas lento que O(n log n).
- **Caso especial:** es excelente para flujos de datos en tiempo real donde
  los elementos llegan uno por uno y se deben mantener ordenados.

## Errores comunes

1. **Empezar desde el indice 0:** el bucle externo debe iniciar en el indice 1,
   ya que el primer elemento no necesita insertarse.
2. **Olvidar guardar la clave:** al desplazar elementos hacia la derecha se
   sobreescribe la posicion original del elemento a insertar. Si no se guardo
   la clave en una variable temporal, se pierde.
3. **Usar intercambios en lugar de desplazamientos:** funciona pero es mas lento.
   Lo correcto es desplazar y luego insertar una sola vez.
4. **No manejar el caso de insercion al inicio:** el bucle interno debe
   permitir llegar hasta el indice 0.

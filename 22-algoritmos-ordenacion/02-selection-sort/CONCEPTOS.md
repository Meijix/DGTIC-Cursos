# Selection Sort (Ordenamiento por Seleccion)

## Que es

Selection Sort divide el arreglo en dos partes: una zona ordenada (al inicio) y
una zona sin ordenar (el resto). En cada iteracion, busca el elemento minimo en
la zona sin ordenar y lo coloca al final de la zona ordenada. Es como buscar la
carta mas baja de tu mano y colocarla al frente, luego la siguiente mas baja,
y asi sucesivamente.

## Diagrama paso a paso

Arreglo inicial: `[29, 10, 14, 37, 13]`

```
Paso 1: buscar el minimo en [29, 10, 14, 37, 13]
        minimo = 10 (posicion 1)
        intercambiar arr[0] con arr[1]
  [ 29, 10, 14, 37, 13 ]
    ^    ^
    └────┘  intercambio
  [ 10 | 29, 14, 37, 13 ]
    ok    sin ordenar

Paso 2: buscar el minimo en [29, 14, 37, 13]
        minimo = 13 (posicion 4)
        intercambiar arr[1] con arr[4]
  [ 10, 29, 14, 37, 13 ]
         ^           ^
         └───────────┘  intercambio
  [ 10, 13 | 29, 14, 37 ]
    ordenado  sin ordenar

Paso 3: buscar el minimo en [29, 14, 37]
        minimo = 14 (posicion 3)
        intercambiar arr[2] con arr[3]
  [ 10, 13, 29, 14, 37 ]
             ^   ^
             └───┘  intercambio
  [ 10, 13, 14 | 29, 37 ]
     ordenado    sin ordenar

Paso 4: buscar el minimo en [29, 37]
        minimo = 29 (posicion 3)
        ya esta en su lugar, no hay intercambio
  [ 10, 13, 14, 29 | 37 ]
       ordenado      sin ordenar

Resultado final: [10, 13, 14, 29, 37]
```

Resumen visual del progreso:

```
Inicio:  | 29  10  14  37  13 |    ordenados: 0
Paso 1:  | 10 | 29  14  37  13 |   ordenados: 1
Paso 2:  | 10  13 | 29  14  37 |   ordenados: 2
Paso 3:  | 10  13  14 | 29  37 |   ordenados: 3
Paso 4:  | 10  13  14  29 | 37 |   ordenados: 4
Final:   | 10  13  14  29  37  |   ordenados: 5
```

## Complejidad

| Caso | Tiempo | Espacio |
|------|--------|---------|
| Mejor | O(n^2) | O(1) |
| Promedio | O(n^2) | O(1) |
| Peor | O(n^2) | O(1) |

**Estable:** No

Selection Sort siempre tiene complejidad O(n^2) porque necesita recorrer toda
la zona no ordenada para encontrar el minimo, sin importar el estado del arreglo.

Es **inestable** porque el intercambio puede mover un elemento por encima de
otro igual. Ejemplo: `[3a, 2, 3b]` → al intercambiar `3a` con `2` se obtiene
`[2, 3b, 3a]`, alterando el orden relativo de los dos 3.

## Como funciona

1. Establecer la posicion actual como el inicio de la zona sin ordenar (i = 0).
2. Recorrer toda la zona sin ordenar para encontrar el elemento minimo.
3. Intercambiar el minimo encontrado con el elemento en la posicion actual.
4. Avanzar la frontera de la zona ordenada (i = i + 1).
5. Repetir hasta que la zona sin ordenar tenga un solo elemento.

## Cuando usarlo

- **Ideal para:** situaciones donde el numero de intercambios (escrituras) debe
  ser minimo, ya que realiza exactamente O(n) intercambios. Util en hardware
  donde las escrituras son costosas (como memoria flash).
- **Ventaja sobre Bubble Sort:** siempre hace menos intercambios (maximo n-1).
- **Desventaja frente a Insertion Sort:** no se beneficia de datos parcialmente
  ordenados; siempre es O(n^2).
- **Nunca usar para:** datos grandes o cuando se necesita estabilidad.
  Prefiere Merge Sort o Insertion Sort respectivamente.

## Errores comunes

1. **Asumir que es estable:** Selection Sort NO es estable. Si necesitas
   estabilidad, usa Insertion Sort.
2. **No guardar el indice del minimo:** algunos intentan guardar el valor en
   vez del indice, complicando el intercambio posterior.
3. **Intercambiar incluso cuando el minimo ya esta en su posicion:** no es un
   error funcional, pero es una optimizacion sencilla que se suele olvidar.
4. **Confundir con Insertion Sort:** Selection Sort busca el minimo y lo pone
   en su lugar; Insertion Sort toma el siguiente elemento y lo inserta en la
   zona ordenada.

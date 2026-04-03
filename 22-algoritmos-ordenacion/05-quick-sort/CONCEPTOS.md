# Quick Sort (Ordenamiento Rapido)

## Que es

Quick Sort es un algoritmo de tipo "divide y venceras" que selecciona un
elemento como pivote y particiona el arreglo en dos grupos: elementos menores
que el pivote y elementos mayores. Luego ordena recursivamente cada grupo.
En la practica, es uno de los algoritmos mas rapidos para ordenamiento general.

## Diagrama paso a paso

Arreglo inicial: `[6, 3, 8, 2, 7, 1, 5]`
Estrategia de pivote: ultimo elemento.

```
Paso 1: pivote = 5
  [6, 3, 8, 2, 7, 1, 5]
                       ^pivote

  Particion — recorrer y colocar menores a la izquierda:
  i=-1, j=0: 6 > 5 → no mover
  i=-1, j=1: 3 < 5 → i=0, intercambiar arr[0] con arr[1]
    [3, 6, 8, 2, 7, 1, 5]
  i=0, j=2:  8 > 5 → no mover
  i=0, j=3:  2 < 5 → i=1, intercambiar arr[1] con arr[3]
    [3, 2, 8, 6, 7, 1, 5]
  i=1, j=4:  7 > 5 → no mover
  i=1, j=5:  1 < 5 → i=2, intercambiar arr[2] con arr[5]
    [3, 2, 1, 6, 7, 8, 5]

  Colocar pivote en su posicion (i+1=3):
    intercambiar arr[3] con arr[6]
    [3, 2, 1, 5, 7, 8, 6]
               ^
         pivote en posicion final

  Resultado: [3, 2, 1] 5 [7, 8, 6]
              <menores>   <mayores>
```

```
Paso 2a: ordenar [3, 2, 1], pivote = 1
  [3, 2, 1]
         ^pivote
  Particion → [1, 2, 3]
              [] 1 [2, 3]

Paso 2b: ordenar [7, 8, 6], pivote = 6
  [7, 8, 6]
         ^pivote
  Particion → [6, 8, 7]
              [] 6 [8, 7]
```

```
Paso 3: ordenar subproblemas restantes [2, 3] y [8, 7]
  [2, 3] → pivote 3 → [2] 3 [] → ya ordenado
  [8, 7] → pivote 7 → [] 7 [8] → ya ordenado
```

```
Arbol completo de recursion:

          [6, 3, 8, 2, 7, 1, 5]
           /        |5|        \
     [3, 2, 1]             [7, 8, 6]
      /  |1|  \              /  |6|  \
    []       [2, 3]        []       [8, 7]
              / |3| \                / |7| \
            [2]     []             []      [8]

  Resultado: [1, 2, 3, 5, 6, 7, 8]
```

## Complejidad

| Caso     | Tiempo      | Espacio    |
|----------|-------------|------------|
| Mejor    | O(n log n)  | O(log n)  |
| Promedio | O(n log n)  | O(log n)  |
| Peor     | O(n^2)      | O(n)      |

**Estable:** No

El peor caso O(n^2) ocurre cuando el pivote siempre es el menor o mayor
elemento (arreglo ya ordenado con pivote al final). Se mitiga con:
- Seleccion aleatoria del pivote.
- Mediana de tres (primer, medio, ultimo elemento).

## Como funciona

1. Elegir un elemento como pivote.
2. Particionar: reorganizar el arreglo para que todos los elementos menores
   que el pivote queden a su izquierda y los mayores a su derecha.
3. El pivote queda en su posicion final definitiva.
4. Aplicar Quick Sort recursivamente a la particion izquierda.
5. Aplicar Quick Sort recursivamente a la particion derecha.
6. Caso base: si la particion tiene 0 o 1 elementos, ya esta ordenada.

## Cuando usarlo

- **Ideal para:** ordenamiento general de arreglos en memoria. Es el
  algoritmo de ordenamiento mas usado en la practica (base de `qsort` en C
  y `Arrays.sort` en Java para tipos primitivos).
- **Ventaja sobre Merge Sort:** ordena in-place, usa solo O(log n) espacio
  de pila. Merge Sort necesita O(n) espacio adicional.
- **Desventaja frente a Merge Sort:** peor caso O(n^2) y no es estable.
- **No recomendado cuando:** se necesita estabilidad o rendimiento garantizado
  en el peor caso. Merge Sort es mejor en esos escenarios.
- **Optimizacion comun:** cambiar a Insertion Sort para particiones pequenas
  (< 10-15 elementos).

## Errores comunes

1. **Mala eleccion de pivote:** usar siempre el primer o ultimo elemento
   resulta en O(n^2) para arreglos ya ordenados. Usar mediana de tres o
   pivote aleatorio.
2. **Recursion infinita:** no excluir el pivote de las llamadas recursivas.
   El pivote ya esta en su posicion final y no debe incluirse.
3. **No manejar elementos iguales al pivote:** puede causar particiones
   desbalanceadas. La particion de tres vias (Dutch National Flag) resuelve
   esto para arreglos con muchos duplicados.
4. **Desbordamiento de pila:** para arreglos grandes con mala particion, la
   recursion puede ser muy profunda. Usar recursion de cola o convertir a
   iterativo.

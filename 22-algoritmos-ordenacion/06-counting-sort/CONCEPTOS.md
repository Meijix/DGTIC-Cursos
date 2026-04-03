# Counting Sort (Ordenamiento por Conteo)

## Que es

Counting Sort es un algoritmo de ordenamiento no comparativo. En lugar de
comparar elementos entre si, cuenta cuantas veces aparece cada valor y usa
esa informacion para colocar cada elemento en su posicion final. Funciona
unicamente con claves enteras dentro de un rango conocido y limitado.

## Diagrama paso a paso

Arreglo inicial: `[4, 2, 2, 8, 3, 3, 1]`
Rango de valores: 0 a 8 (k = 9)

```
Paso 1: Construir arreglo de conteo
  Recorrer el arreglo y contar cada valor:

  Valor:   0   1   2   3   4   5   6   7   8
  Conteo: [0,  1,  2,  2,  1,  0,  0,  0,  1]
                ^   ^   ^   ^               ^
                1   2   2   1               1
              vez veces veces vez          vez

Paso 2: Acumular conteos (suma de prefijos)
  Cada posicion indica cuantos elementos son <= a ese valor.

  Valor:       0   1   2   3   4   5   6   7   8
  Acumulado:  [0,  1,  3,  5,  6,  6,  6,  6,  7]
                   |       |       |               |
                 1 elem  3 elem  6 elem          7 elem
                  <= 1    <= 2    <= 4            <= 8

Paso 3: Construir arreglo de salida (recorrer entrada de derecha a izquierda)
  Entrada: [4, 2, 2, 8, 3, 3, 1]

  Procesando de derecha a izquierda para estabilidad:

  Elemento 1: acum[1]=1 → posicion 0, acum[1]=0
    salida: [_, _, _, _, _, _, _]
             1
    salida: [1, _, _, _, _, _, _]

  Elemento 3: acum[3]=5 → posicion 4, acum[3]=4
    salida: [1, _, _, _, 3, _, _]

  Elemento 3: acum[3]=4 → posicion 3, acum[3]=3
    salida: [1, _, _, 3, 3, _, _]

  Elemento 8: acum[8]=7 → posicion 6, acum[8]=6
    salida: [1, _, _, 3, 3, _, 8]

  Elemento 2: acum[2]=3 → posicion 2, acum[2]=2
    salida: [1, _, 2, 3, 3, _, 8]

  Elemento 2: acum[2]=2 → posicion 1, acum[2]=1
    salida: [1, 2, 2, 3, 3, _, 8]

  Elemento 4: acum[4]=6 → posicion 5, acum[4]=5
    salida: [1, 2, 2, 3, 3, 4, 8]

Resultado final: [1, 2, 2, 3, 3, 4, 8]
```

## Complejidad

| Caso     | Tiempo    | Espacio   |
|----------|-----------|-----------|
| Mejor    | O(n + k)  | O(n + k) |
| Promedio | O(n + k)  | O(n + k) |
| Peor     | O(n + k)  | O(n + k) |

Donde `n` es el numero de elementos y `k` es el rango de valores posibles.

**Estable:** Si (si se implementa correctamente recorriendo de derecha a izquierda)

## Como funciona

1. Determinar el valor maximo (k) en el arreglo de entrada.
2. Crear un arreglo de conteo de tamano k+1, inicializado en ceros.
3. Recorrer la entrada y contar las ocurrencias de cada valor.
4. Transformar el arreglo de conteo en sumas acumuladas: cada posicion
   indica cuantos elementos son menores o iguales a ese valor.
5. Recorrer el arreglo de entrada de derecha a izquierda:
   a. Para cada elemento, usar su conteo acumulado como posicion de salida.
   b. Decrementar el conteo acumulado.
6. Copiar el arreglo de salida al arreglo original.

## Cuando usarlo

- **Ideal para:** datos con claves enteras en un rango pequeno y conocido.
  Ejemplos: edades (0-150), calificaciones (0-100), caracteres ASCII (0-127).
- **Ventaja sobre algoritmos comparativos:** su complejidad O(n + k) rompe
  la barrera inferior de O(n log n) de los algoritmos basados en comparacion.
- **No recomendado cuando:** el rango k es mucho mayor que n (desperdicia
  memoria), las claves son numeros de punto flotante, o las claves son cadenas.
- **Uso como subrutina:** es la base de Radix Sort, que lo usa para ordenar
  digito por digito.

## Errores comunes

1. **Olvidar la suma acumulada:** sin la fase de acumulacion, no se puede
   determinar la posicion correcta de cada elemento.
2. **Recorrer de izquierda a derecha en el paso 5:** esto invierte el
   orden relativo de los elementos iguales, haciendo el algoritmo inestable.
3. **No contemplar el rango completo:** si hay valores negativos, se debe
   ajustar desplazando los indices.
4. **Usar Counting Sort con un rango enorme:** si k >> n, el arreglo de
   conteo desperdicia mucha memoria. Ejemplo: ordenar 100 numeros en el
   rango 0 a 1,000,000 usa 1 MB solo para el arreglo de conteo.
5. **Confundir con un histograma simple:** Counting Sort necesita la fase
   de acumulacion y la construccion del arreglo de salida, no basta con
   contar frecuencias y escribir los valores en orden.

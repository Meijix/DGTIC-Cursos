# Bubble Sort (Ordenamiento Burbuja)

## Que es

Bubble Sort es el algoritmo de ordenamiento mas sencillo. Funciona recorriendo
repetidamente la lista, comparando elementos adyacentes e intercambiandolos si
estan en el orden incorrecto. Los elementos mas grandes "burbujean" hacia el
final del arreglo en cada pasada, de ahi su nombre.

## Diagrama paso a paso

Arreglo inicial: `[5, 3, 8, 1, 2]`

```
Paso 1 (primera pasada):
  [5, 3, 8, 1, 2]
   ^  ^
   5 > 3 → intercambio
  [3, 5, 8, 1, 2]
      ^  ^
      5 < 8 → no intercambio
  [3, 5, 8, 1, 2]
         ^  ^
         8 > 1 → intercambio
  [3, 5, 1, 8, 2]
            ^  ^
            8 > 2 → intercambio
  [3, 5, 1, 2, 8]  ← el 8 ya esta en su lugar final

Paso 2 (segunda pasada):
  [3, 5, 1, 2, 8]
   ^  ^
   3 < 5 → no intercambio
  [3, 5, 1, 2, 8]
      ^  ^
      5 > 1 → intercambio
  [3, 1, 5, 2, 8]
         ^  ^
         5 > 2 → intercambio
  [3, 1, 2, 5, 8]  ← el 5 ya esta en su lugar final

Paso 3 (tercera pasada):
  [3, 1, 2, 5, 8]
   ^  ^
   3 > 1 → intercambio
  [1, 3, 2, 5, 8]
      ^  ^
      3 > 2 → intercambio
  [1, 2, 3, 5, 8]  ← el 3 ya esta en su lugar final

Paso 4 (cuarta pasada):
  [1, 2, 3, 5, 8]
   ^  ^
   1 < 2 → no intercambio
  [1, 2, 3, 5, 8]  ← sin intercambios, arreglo ordenado!

Resultado final: [1, 2, 3, 5, 8]
```

Visualizacion del progreso de cada pasada:

```
Pasada 1: [3, 5, 1, 2, | 8 ]    zona ordenada: 1 elemento
Pasada 2: [3, 1, 2, | 5,  8 ]    zona ordenada: 2 elementos
Pasada 3: [1, 2, | 3,  5,  8 ]    zona ordenada: 3 elementos
Pasada 4: [1, | 2,  3,  5,  8 ]    zona ordenada: 4 elementos
                  |← ordenado →|
```

## Complejidad

| Caso | Tiempo | Espacio |
|------|--------|---------|
| Mejor | O(n) | O(1) |
| Promedio | O(n^2) | O(1) |
| Peor | O(n^2) | O(1) |

**Estable:** Si

El mejor caso O(n) se logra cuando el arreglo ya esta ordenado y se usa la
optimizacion de detectar si no hubo intercambios en una pasada completa.

## Como funciona

1. Recorrer el arreglo desde el inicio hasta el penultimo elemento no ordenado.
2. Comparar cada par de elementos adyacentes (posicion `i` e `i+1`).
3. Si el elemento en la posicion `i` es mayor que el de `i+1`, intercambiarlos.
4. Al terminar una pasada completa, el elemento mas grande queda al final.
5. Repetir el proceso, reduciendo en uno la zona a comparar cada vez.
6. Optimizacion: si en una pasada no hubo ningun intercambio, el arreglo ya
   esta ordenado y se puede terminar antes.

## Cuando usarlo

- **Ideal para:** arreglos muy pequenos (< 20 elementos) o arreglos casi
  ordenados donde la optimizacion de deteccion temprana es efectiva.
- **Ventaja sobre Selection Sort:** puede terminar antes si detecta que ya
  esta ordenado.
- **Desventaja frente a Insertion Sort:** generalmente hace mas intercambios
  para arreglos parcialmente ordenados.
- **Nunca usar para:** conjuntos de datos grandes. Su complejidad O(n^2) lo
  hace impractico. Prefiere Merge Sort o Quick Sort para esos casos.
- Es util principalmente con fines educativos por su simplicidad.

## Errores comunes

1. **Olvidar reducir el limite superior:** en cada pasada, el ultimo elemento
   ya esta ordenado. No reducir el rango provoca comparaciones innecesarias.
2. **No implementar la deteccion temprana:** sin verificar si hubo intercambios,
   se pierde el caso optimo O(n).
3. **Confundir indices:** comparar `arr[i]` con `arr[i+1]` pero iterar hasta
   `n` en lugar de `n-1`, causando acceso fuera de limites.
4. **Asumir que una pasada sin intercambios en la primera mitad significa que
   todo esta ordenado:** la bandera debe cubrir la pasada completa.

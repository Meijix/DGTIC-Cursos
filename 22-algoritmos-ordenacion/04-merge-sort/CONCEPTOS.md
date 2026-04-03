# Merge Sort (Ordenamiento por Mezcla)

## Que es

Merge Sort es un algoritmo de tipo "divide y venceras". Divide el arreglo por
la mitad recursivamente hasta tener subarreglos de un solo elemento, y luego
los combina (mezcla) de forma ordenada. Garantiza O(n log n) en todos los
casos, lo que lo hace muy confiable para datos grandes.

## Diagrama paso a paso

Arreglo inicial: `[38, 27, 43, 3, 9, 82, 10]`

### Fase de division

```
                [38, 27, 43, 3, 9, 82, 10]
                       /              \
            [38, 27, 43, 3]      [9, 82, 10]
              /        \           /       \
          [38, 27]  [43, 3]    [9, 82]   [10]
           /   \     /   \      /   \      |
         [38] [27] [43]  [3]  [9] [82]  [10]
```

### Fase de mezcla (merge)

```
         [38] [27] [43]  [3]  [9] [82]  [10]
           \   /     \   /      \   /      |
        [27, 38]  [3, 43]    [9, 82]    [10]
            \       /            \        /
       [3, 27, 38, 43]       [9, 10, 82]
               \                  /
        [3, 9, 10, 27, 38, 43, 82]
```

### Detalle de una operacion de mezcla

Mezclar `[3, 27, 38, 43]` con `[9, 10, 82]`:

```
  izq: [3, 27, 38, 43]    der: [9, 10, 82]    resultado: []
        ^                        ^
        3 < 9 → tomar 3

  izq: [3, 27, 38, 43]    der: [9, 10, 82]    resultado: [3]
           ^                     ^
           27 > 9 → tomar 9

  izq: [3, 27, 38, 43]    der: [9, 10, 82]    resultado: [3, 9]
           ^                        ^
           27 > 10 → tomar 10

  izq: [3, 27, 38, 43]    der: [9, 10, 82]    resultado: [3, 9, 10]
           ^                            ^
           27 < 82 → tomar 27

  izq: [3, 27, 38, 43]    der: [9, 10, 82]    resultado: [3, 9, 10, 27]
               ^                        ^
               38 < 82 → tomar 38

  izq: [3, 27, 38, 43]    der: [9, 10, 82]    resultado: [3, 9, 10, 27, 38]
                   ^                    ^
                   43 < 82 → tomar 43

  izq agotado → copiar resto de der
  resultado: [3, 9, 10, 27, 38, 43, 82]
```

## Complejidad

| Caso     | Tiempo      | Espacio |
|----------|-------------|---------|
| Mejor    | O(n log n)  | O(n)   |
| Promedio | O(n log n)  | O(n)   |
| Peor     | O(n log n)  | O(n)   |

**Estable:** Si

La complejidad de tiempo es siempre O(n log n) porque:
- Se realizan log n niveles de division.
- En cada nivel se recorren los n elementos durante la mezcla.
El costo es el espacio adicional O(n) para los arreglos temporales de mezcla.

## Como funciona

1. Si el arreglo tiene 0 o 1 elementos, ya esta ordenado (caso base).
2. Dividir el arreglo en dos mitades.
3. Ordenar recursivamente cada mitad con Merge Sort.
4. Mezclar las dos mitades ordenadas:
   a. Usar dos punteros, uno para cada mitad.
   b. Comparar los elementos apuntados y copiar el menor al resultado.
   c. Avanzar el puntero correspondiente.
   d. Cuando una mitad se agote, copiar el resto de la otra.

## Cuando usarlo

- **Ideal para:** datos grandes donde se necesita rendimiento garantizado
  O(n log n). Es la mejor opcion cuando no puedes tolerar el peor caso de
  Quick Sort.
- **Ventaja sobre Quick Sort:** peor caso garantizado O(n log n) y es estable.
- **Desventaja frente a Quick Sort:** usa O(n) espacio adicional. Quick Sort
  ordena in-place con O(log n) de pila.
- **Uso clasico:** ordenar listas enlazadas (donde no tiene costo extra de
  espacio) y ordenamiento externo de archivos grandes.
- **Desventaja frente a Insertion Sort:** para arreglos pequenos, la
  sobrecarga de la recursion hace que sea mas lento.

## Errores comunes

1. **Calcular mal el punto medio:** usar `(izq + der) / 2` puede causar
   desbordamiento en algunos lenguajes. Mejor usar `izq + (der - izq) / 2`.
2. **No copiar los elementos restantes:** al terminar el bucle de mezcla,
   olvidar copiar lo que queda de la mitad no agotada.
3. **Crear arreglos nuevos en cada llamada recursiva:** es mas eficiente
   crear un arreglo auxiliar una sola vez y reutilizarlo.
4. **Confundir los indices de mezcla:** manejar mal los limites de las dos
   mitades al mezclar, provocando elementos duplicados o perdidos.

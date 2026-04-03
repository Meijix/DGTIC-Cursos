# Radix Sort (Ordenamiento por Raiz)

## Que es

Radix Sort ordena numeros procesando digito por digito, desde el menos
significativo (LSD - Least Significant Digit) hasta el mas significativo,
o viceversa (MSD - Most Significant Digit). Usa un algoritmo estable como
Counting Sort para ordenar por cada digito. No compara elementos directamente,
sino que los distribuye en cubetas segun el digito que se esta procesando.

## Diagrama paso a paso

Arreglo inicial: `[170, 45, 75, 90, 802, 24, 2, 66]`
Metodo: LSD (digito menos significativo primero).

```
Paso 1: Ordenar por el digito de las UNIDADES

  Numero → digito unidades:
  170 → 0    45 → 5    75 → 5    90 → 0
  802 → 2    24 → 4     2 → 2    66 → 6

  Cubetas (0-9):
  [0]: 170, 90
  [1]:
  [2]: 802, 2
  [3]:
  [4]: 24
  [5]: 45, 75
  [6]: 66
  [7]:
  [8]:
  [9]:

  Recolectar en orden:
  [170, 90, 802, 2, 24, 45, 75, 66]

Paso 2: Ordenar por el digito de las DECENAS

  Numero → digito decenas:
  170 → 7    90 → 9    802 → 0     2 → 0
   24 → 2    45 → 4     75 → 7    66 → 6

  Cubetas (0-9):
  [0]: 802, 2
  [1]:
  [2]: 24
  [3]:
  [4]: 45
  [5]:
  [6]: 66
  [7]: 170, 75
  [8]:
  [9]: 90

  Recolectar en orden:
  [802, 2, 24, 45, 66, 170, 75, 90]

Paso 3: Ordenar por el digito de las CENTENAS

  Numero → digito centenas:
  802 → 8     2 → 0    24 → 0    45 → 0
   66 → 0   170 → 1    75 → 0    90 → 0

  Cubetas (0-9):
  [0]: 2, 24, 45, 66, 75, 90
  [1]: 170
  [2]:
  [3]:
  [4]:
  [5]:
  [6]:
  [7]:
  [8]: 802
  [9]:

  Recolectar en orden:
  [2, 24, 45, 66, 75, 90, 170, 802]

Resultado final: [2, 24, 45, 66, 75, 90, 170, 802]
```

## LSD vs MSD

```
LSD (Least Significant Digit):          MSD (Most Significant Digit):
  - Procesa del digito menos              - Procesa del digito mas
    significativo al mas                    significativo al menos
    significativo                           significativo
  - Funciona con un solo pase             - Trabaja recursivamente
    por digito sobre todo                   dentro de cada cubeta
    el arreglo                            - Puede terminar antes
  - Mas sencillo de implementar             si las cubetas son pequenas
  - Necesita algoritmo estable            - Natural para cadenas
    como subrutina                          (orden lexicografico)

  Ejemplo con 3 digitos:                 Ejemplo con 3 digitos:
  Orden de proceso:                      Orden de proceso:
    1ro → unidades                         1ro → centenas
    2do → decenas                          2do → decenas (por cubeta)
    3ro → centenas                         3ro → unidades (por cubeta)
```

## Complejidad

| Caso     | Tiempo    | Espacio   |
|----------|-----------|-----------|
| Mejor    | O(d * (n + k))  | O(n + k) |
| Promedio | O(d * (n + k))  | O(n + k) |
| Peor     | O(d * (n + k))  | O(n + k) |

Donde:
- `n` = numero de elementos
- `d` = numero de digitos del valor maximo
- `k` = base (10 para decimal, 256 para bytes, etc.)

**Estable:** Si (cuando se usa un algoritmo estable como subrutina)

Para numeros enteros de 32 bits con base 256: d=4, k=256, dando O(4*(n+256))
que es efectivamente O(n) para n grande.

## Como funciona

1. Determinar el numero maximo de digitos (d) en el arreglo.
2. Para cada posicion de digito, del menos significativo al mas significativo:
   a. Extraer el digito correspondiente de cada elemento.
   b. Usar Counting Sort (u otro algoritmo estable) para ordenar los
      elementos segun ese digito.
3. Despues de procesar todos los digitos, el arreglo esta ordenado.

La clave es que **la estabilidad del algoritmo de subrutina preserva el orden
de los digitos anteriores.** Cuando se ordena por las decenas, los elementos
con la misma decena mantienen su orden por unidades (que se ordeno antes).

## Cuando usarlo

- **Ideal para:** grandes cantidades de numeros enteros o cadenas de longitud
  fija. Ejemplo: ordenar millones de numeros telefonicos, codigos postales,
  o direcciones IP.
- **Ventaja sobre algoritmos comparativos:** puede ser O(n) cuando d y k son
  constantes, superando el limite O(n log n).
- **No recomendado cuando:** los numeros tienen muchos digitos (d grande),
  los valores son de punto flotante, o n es pequeno (la constante oculta
  hace que Quick Sort sea mas rapido).
- **LSD es preferible para:** enteros y cadenas de longitud fija.
- **MSD es preferible para:** cadenas de longitud variable con orden
  lexicografico.

## Errores comunes

1. **Usar un algoritmo inestable como subrutina:** si la subrutina de
   ordenamiento por digito no es estable, el resultado final sera incorrecto.
   Es esencial que Counting Sort o un equivalente estable sea la subrutina.
2. **No manejar numeros con diferente cantidad de digitos:** se deben rellenar
   con ceros a la izquierda conceptualmente (o manejar el caso de que el
   digito no exista como cero).
3. **Elegir una base inadecuada:** base 10 es intuitiva pero base 256 es
   mucho mas eficiente para enteros de 32/64 bits (solo 4/8 pasadas).
4. **Aplicar Radix Sort a datos no adecuados:** no funciona directamente con
   numeros negativos (se necesita un ajuste) ni con punto flotante.
5. **Confundir LSD con MSD:** LSD procesa todo el arreglo junto en cada
   pasada; MSD requiere recursion dentro de cada cubeta.

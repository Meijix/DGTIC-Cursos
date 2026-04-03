# Cheatsheet — Algoritmos de Ordenacion

## Tabla comparativa general

```
┌──────────────────┬────────────┬────────────┬────────────┬──────────┬─────────┬──────────┐
│ Algoritmo        │  Mejor     │  Promedio  │   Peor     │ Espacio  │ Estable │ In-place │
├──────────────────┼────────────┼────────────┼────────────┼──────────┼─────────┼──────────┤
│ Bubble Sort      │   O(n)     │   O(n²)    │   O(n²)    │  O(1)    │   Si    │   Si     │
│ Selection Sort   │   O(n²)    │   O(n²)    │   O(n²)    │  O(1)    │   No    │   Si     │
│ Insertion Sort   │   O(n)     │   O(n²)    │   O(n²)    │  O(1)    │   Si    │   Si     │
│ Merge Sort       │ O(n log n) │ O(n log n) │ O(n log n) │  O(n)    │   Si    │   No     │
│ Quick Sort       │ O(n log n) │ O(n log n) │   O(n²)    │ O(log n) │   No    │   Si     │
│ Counting Sort    │  O(n + k)  │  O(n + k)  │  O(n + k)  │ O(n + k) │   Si    │   No     │
│ Radix Sort       │  O(d·n)    │  O(d·n)    │  O(d·n)    │ O(n + k) │   Si    │   No     │
└──────────────────┴────────────┴────────────┴────────────┴──────────┴─────────┴──────────┘

n = numero de elementos
k = rango de valores (counting/radix)
d = numero de digitos (radix)
```

---

## Visualizacion rapida de cada algoritmo

```
BUBBLE SORT — Burbujea el mayor al final
  [5, 3, 8, 1] → compara pares adyacentes, intercambia si estan desordenados
   ^  ^          3 < 5 → swap → [3, 5, 8, 1]
      ^  ^       5 < 8 → ok
         ^  ^    1 < 8 → swap → [3, 5, 1, 8]  ← 8 ya en su lugar

SELECTION SORT — Selecciona el minimo
  [5, 3, 8, 1] → busca min en todo el arreglo → 1 (pos 3)
   ↕        ↕    swap con pos 0 → [1, 3, 8, 5]
             ↑   ahora busca min desde pos 1...

INSERTION SORT — Inserta en la posicion correcta
  [5, |3, 8, 1] → toma 3, inserta en la parte ordenada
  [3, 5, |8, 1] → toma 8, ya esta en su lugar
  [3, 5, 8, |1] → toma 1, desplaza 3,5,8 → [1, 3, 5, 8]

MERGE SORT — Divide, ordena, mezcla
  [5, 3, 8, 1] → [5, 3] [8, 1] → [5] [3] [8] [1]
                   merge: [3, 5]  [1, 8]
                   merge: [1, 3, 5, 8]

QUICK SORT — Pivote + particion
  [5, 3, 8, 1, 7]  pivote = 5
  [3, 1] [5] [8, 7]   ← menores | pivote | mayores
  ordena cada lado recursivamente

COUNTING SORT — Cuenta ocurrencias
  [3, 1, 4, 1, 3] → cuenta: [0, 2, 0, 2, 1] (indices 0-4)
                   → reconstruye: [1, 1, 3, 3, 4]

RADIX SORT — Ordena digito por digito
  [170, 45, 75, 90, 802]
  por unidades:  [170, 90, 802, 45, 75]
  por decenas:   [802, 45, 170, 75, 90]
  por centenas:  [45, 75, 90, 170, 802]
```

---

## Cuando usar cada algoritmo

```
┌──────────────────────────────────────┬────────────────────────────────────────┐
│ Situacion                            │ Mejor algoritmo                        │
├──────────────────────────────────────┼────────────────────────────────────────┤
│ Datos casi ordenados                 │ Insertion Sort — O(n) en mejor caso    │
│ Pocos elementos (n < 50)            │ Insertion Sort — overhead minimo        │
│ Necesitas estabilidad garantizada    │ Merge Sort                             │
│ Caso general, buen rendimiento       │ Quick Sort — mas rapido en practica    │
│ Memoria limitada (in-place)          │ Quick Sort o Heap Sort                 │
│ Garantia de O(n log n) siempre       │ Merge Sort                             │
│ Enteros en rango conocido [0, k]     │ Counting Sort — O(n + k)              │
│ Numeros grandes, muchos digitos      │ Radix Sort — O(d * n)                 │
│ Ordenar datos enlazados (linked)     │ Merge Sort — no necesita acceso random │
│ Datos enormes en disco               │ Merge Sort — buen patron de I/O       │
│ Proposito educativo / entrevistas    │ Todos — conocer trade-offs             │
└──────────────────────────────────────┴────────────────────────────────────────┘
```

---

## Estabilidad explicada

```
Estable = elementos iguales mantienen su orden relativo original

  Entrada:  [(Ana, 85), (Bob, 90), (Eva, 85)]
                  ↑                    ↑
            ambas tienen 85

  Ordenar por nota:

  ESTABLE:    [(Ana, 85), (Eva, 85), (Bob, 90)]   ← Ana antes que Eva (orden original)
  NO ESTABLE: [(Eva, 85), (Ana, 85), (Bob, 90)]   ← podria invertir Ana y Eva

  Estables:     Bubble, Insertion, Merge, Counting, Radix
  No estables:  Selection, Quick (implementacion clasica)
```

---

## Arbol de decision

```
¿Cuantos elementos?
├── Pocos (n < 50) ──► Insertion Sort
└── Muchos (n >= 50)
    ¿Son enteros en rango acotado?
    ├── SI ──► Counting Sort o Radix Sort
    └── NO
        ¿Necesitas estabilidad?
        ├── SI ──► Merge Sort
        └── NO
            ¿Puedes tolerar O(n²) en peor caso?
            ├── SI ──► Quick Sort (mas rapido en promedio)
            └── NO ──► Merge Sort (siempre O(n log n))
```

---

## Python: sorted() y list.sort()

```python
# Python usa Timsort: hibrido de Merge Sort + Insertion Sort
# - Estable
# - O(n log n) peor caso
# - O(n) para datos parcialmente ordenados
# - Usado por sorted() y list.sort()

# Ordenar lista (modifica in-place)
numeros = [5, 3, 8, 1]
numeros.sort()                    # [1, 3, 5, 8]

# Crear nueva lista ordenada
ordenados = sorted([5, 3, 8, 1])  # [1, 3, 5, 8]

# Ordenar por clave personalizada
alumnos = [("Ana", 85), ("Bob", 90), ("Eva", 78)]
sorted(alumnos, key=lambda x: x[1])           # por nota
sorted(alumnos, key=lambda x: x[1], reverse=True)  # descendente

# Ordenar objetos
from operator import attrgetter
sorted(personas, key=attrgetter('edad'))
```

---

## Errores frecuentes

| Error | Correccion |
|-------|-----------|
| Implementar sort desde cero en produccion | Usa `sorted()` / `.sort()` — Timsort es casi imbatible |
| Quick Sort con pivote fijo en datos ordenados | Usa mediana de tres o pivote aleatorio |
| Olvidar que Merge Sort necesita O(n) extra | Si la memoria importa, usa Quick Sort |
| Usar Bubble Sort para n grande | Solo es aceptable para n muy pequeno o datos casi ordenados |
| Counting Sort con rango enorme (ej. floats) | Solo funciona con enteros en rango acotado |
| No considerar estabilidad al ordenar objetos | Si el orden relativo importa, necesitas algoritmo estable |

# Arrays (Arreglos)

## Que es

Un **array** (arreglo) es una estructura de datos que almacena elementos del mismo tipo en posiciones **contiguas de memoria**. Cada elemento se identifica por un indice numerico que comienza en 0. Es la estructura mas fundamental en programacion y la base sobre la que se construyen muchas otras.

## Diagrama

### Disposicion en memoria

```
Indice:   0     1     2     3     4
        ┌─────┬─────┬─────┬─────┬─────┐
Valor:  │  10 │  20 │  30 │  40 │  50 │
        └─────┴─────┴─────┴─────┴─────┘
Memoria: 0x00  0x04  0x08  0x0C  0x10   (contiguos)
```

La direccion de cualquier elemento se calcula como:
```
direccion(i) = direccion_base + (i * tamaño_elemento)
```

### Insercion en medio (costosa)

```
Insertar 25 en indice 2:

Antes:  [10, 20, 30, 40, 50]
                  ↓   ↓   ↓      Desplazar a la derecha
Despues:[10, 20, 25, 30, 40, 50]
```

### Eliminacion en medio (costosa)

```
Eliminar indice 1 (valor 20):

Antes:  [10, 20, 30, 40, 50]
              ↑   ↑   ↑          Desplazar a la izquierda
Despues:[10, 30, 40, 50]
```

## Operaciones principales

| Operacion           | Complejidad | Descripcion                                      |
|---------------------|-------------|--------------------------------------------------|
| Acceso por indice   | O(1)        | Acceso directo por calculo de direccion           |
| Busqueda (sin orden)| O(n)        | Recorrer elemento por elemento                    |
| Busqueda (ordenado) | O(log n)    | Busqueda binaria                                  |
| Insercion al final  | O(1)*       | Amortizado en arrays dinamicos                    |
| Insercion en medio  | O(n)        | Requiere desplazar elementos                      |
| Eliminacion al final| O(1)        | Solo reducir el tamaño                            |
| Eliminacion en medio| O(n)        | Requiere desplazar elementos                      |

*O(1) amortizado: ocasionalmente O(n) cuando se necesita redimensionar.

## Como funciona

### Arrays estaticos vs dinamicos

```
Array estatico (tamaño fijo):
┌─────┬─────┬─────┬─────┐
│  10 │  20 │  30 │     │  Capacidad: 4 (no puede crecer)
└─────┴─────┴─────┴─────┘

Array dinamico (list de Python):
┌─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┐
│  10 │  20 │  30 │     │     │     │     │     │  Capacidad: 8
└─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┘
  Tamaño actual: 3       ↑ espacio reservado

Cuando se llena, se crea uno nuevo con el doble de capacidad
y se copian todos los elementos.
```

### Acceso O(1) - La gran ventaja

```
arr = [10, 20, 30, 40, 50]

arr[3]  →  direccion_base + 3 * 4 bytes = 0x00 + 0x0C = 0x0C
        →  valor: 40   (un solo paso, sin importar el tamaño)
```

## Cuando usarla

**Usar arrays cuando:**
- Necesitas acceso rapido por indice (O(1))
- Los datos tienen un orden logico (secuencias, series)
- El tamaño es conocido o las inserciones son al final
- Necesitas recorrer elementos secuencialmente (buena localidad de cache)

**NO usar arrays cuando:**
- Hay muchas inserciones/eliminaciones en medio (usar listas enlazadas)
- Necesitas busquedas frecuentes por valor (usar tablas hash)
- El tamaño varia mucho y la memoria es limitada

### Comparacion con listas enlazadas

```
                    Array       Lista enlazada
Acceso por indice   O(1)        O(n)
Insercion inicio    O(n)        O(1)
Insercion medio     O(n)        O(1)*
Uso de memoria      Compacto    Extra por punteros
Localidad cache     Excelente   Pobre
```
*Asumiendo que ya tienes referencia al nodo.

## Casos de uso en el mundo real

- **Imagenes**: matrices de pixeles (arrays 2D)
- **Buffers de audio/video**: datos secuenciales en tiempo real
- **Lookup tables**: tablas de valores precalculados
- **Strings**: internamente son arrays de caracteres
- **Pilas y colas**: implementacion subyacente comun

## Errores comunes

1. **Indice fuera de rango**: acceder a `arr[n]` cuando el tamaño es `n` (los indices van de 0 a n-1).
2. **Confundir tamaño con capacidad**: en arrays dinamicos, la capacidad reservada puede ser mayor que la cantidad de elementos.
3. **Copias superficiales**: al copiar un array de objetos, solo se copian las referencias, no los objetos mismos.
4. **Insercion ineficiente**: insertar repetidamente al inicio de un array es O(n^2) en total. Usar `collections.deque` en Python si se necesita.
5. **No considerar el costo de redimensionar**: el `.append()` de Python es O(1) amortizado, pero un append individual puede ser O(n) cuando se redimensiona.

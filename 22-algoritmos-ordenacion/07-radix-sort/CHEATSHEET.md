# Cheatsheet — Radix Sort

## En una frase
Ordena los elementos digito por digito, del menos significativo al mas significativo (LSD), usando un ordenamiento estable como subrutina.

## Diagrama rapido
```
Arreglo: [170, 045, 075, 090, 002, 024, 802, 066]

Paso 1 — Ordenar por digito de UNIDADES:
  170  045  075  090  002  024  802  066
   ^    ^    ^    ^    ^    ^    ^    ^
  [170, 090, 002, 802, 024, 045, 075, 066]

Paso 2 — Ordenar por digito de DECENAS:
  170  090  002  802  024  045  075  066
    ^   ^    ^    ^    ^    ^    ^    ^
  [002, 802, 024, 045, 066, 170, 075, 090]

Paso 3 — Ordenar por digito de CENTENAS:
  002  802  024  045  066  170  075  090
  ^    ^    ^    ^    ^    ^    ^    ^
  [002, 024, 045, 066, 075, 090, 170, 802]

Resultado: [002, 024, 045, 066, 075, 090, 170, 802]
```

## Complejidad
| Caso    | Tiempo    | Espacio |
|---------|-----------|---------|
| Mejor   | O(d*(n+k)) | O(n+k) |
| Promedio | O(d*(n+k)) | O(n+k) |
| Peor    | O(d*(n+k)) | O(n+k) |

> **d** = numero de digitos, **k** = base (10 para decimal), **n** = elementos

**Estable:** Si — **In-place:** No

## LSD vs MSD
| Aspecto          | LSD (Least Significant) | MSD (Most Significant)  |
|------------------|-------------------------|-------------------------|
| Direccion        | Derecha a izquierda     | Izquierda a derecha     |
| Implementacion   | Mas simple, iterativa   | Recursiva, mas compleja |
| Estabilidad      | Estable naturalmente    | Requiere cuidado extra  |
| Mejor para       | Enteros, largo fijo     | Cadenas de largo variable |
| Puede parar antes | No                     | Si (si ya esta ordenado) |

## Python en 10 lineas
```python
def counting_sort_by_digit(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    for x in arr:
        idx = (x // exp) % 10
        count[idx] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    for x in reversed(arr):
        idx = (x // exp) % 10
        output[count[idx] - 1] = x
        count[idx] -= 1
    arr[:] = output

def radix_sort(arr):
    if not arr:
        return
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        counting_sort_by_digit(arr, exp)
        exp *= 10
```

## Cuando SI / Cuando NO
**Usar cuando:**
- Los datos son enteros o cadenas de longitud fija
- n es grande pero d (digitos) es pequeno y constante
- Se necesita estabilidad y rendimiento mejor que O(n log n)
- Se ordenan claves como codigos postales, telefonos, IPs, fechas

**NO usar cuando:**
- Los datos tienen longitud variable o muchos digitos (d grande)
- Los datos son de punto flotante (requiere transformacion especial)
- La memoria es limitada (necesita O(n+k) espacio extra)
- n es pequeno (el overhead no se justifica)

## Tip clave
Radix Sort es lineal en la practica cuando d es constante. Ordenar 1 millon de enteros de 32 bits toma O(4 * (n + 256)) con base 256, mucho mas rapido que O(n log n). La clave es que Counting Sort como subrutina **debe ser estable** para que el resultado final sea correcto.

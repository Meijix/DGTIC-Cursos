# Cheatsheet — Tablas Hash

## Diagrama rapido

```
FLUJO DE UNA TABLA HASH:

  clave ──► hash(clave) ──► indice ──► bucket ──► valor
  "gato"    hash("gato")     [3]        ┌───┐
                                         │ v │
                                         └───┘

TABLA COMPLETA:
  indice   bucket
  [0]  ──► [ "perro": 5 ]
  [1]  ──► [ vacio ]
  [2]  ──► [ "ave": 2 ] ──► [ "pez": 8 ]   ← colision (encadenamiento)
  [3]  ──► [ "gato": 3 ]
  [4]  ──► [ vacio ]

MANEJO DE COLISIONES:

  Encadenamiento (chaining):       Direccionamiento abierto (open addressing):
  [2] ──► [k1,v1] ──► [k2,v2]     [2] → ocupado (k1) → busca [3] → libre → inserta k2

  Cada bucket es una lista.        Si el slot esta ocupado, busca el siguiente libre.
```

## Operaciones — O(?)

```
┌───────────────────┬──────────────┬──────────────┐
│ Operacion         │ Promedio     │ Peor caso    │
├───────────────────┼──────────────┼──────────────┤
│ Buscar (lookup)   │    O(1)      │    O(n)      │
│ Insertar          │    O(1)      │    O(n)      │
│ Eliminar          │    O(1)      │    O(n)      │
│ Iterar todo       │    O(n)      │    O(n)      │
│ Rehashing         │    O(n)      │    O(n)      │
└───────────────────┴──────────────┴──────────────┘

Peor caso = muchas colisiones (todas las claves en el mismo bucket).
Factor de carga = n / m  (n=elementos, m=buckets).
Se hace rehashing cuando factor de carga > ~0.75.
```

## Python en 30 segundos

```python
# dict — tabla hash clave:valor
d = {"x": 1, "y": 2}
d["z"] = 3              # insertar O(1)
val = d["x"]             # buscar O(1)
del d["y"]               # eliminar O(1)
"x" in d                 # pertenencia O(1)

# set — tabla hash de claves unicas (sin valor)
s = {1, 2, 3}
s.add(4)                 # O(1)
s.discard(2)             # O(1), no lanza error si no existe
3 in s                   # O(1)

# defaultdict — valor por defecto automatico
from collections import defaultdict
dd = defaultdict(list)
dd["frutas"].append("manzana")  # no necesitas verificar si existe la clave

# Counter — contar frecuencias
from collections import Counter
c = Counter("abracadabra")
c.most_common(3)         # [('a', 5), ('b', 2), ('r', 2)]
```

## Cuando usar / Cuando NO usar

- **Usar** cuando necesitas busqueda/insercion/eliminacion en O(1) promedio.
- **Usar** para contar frecuencias, agrupar datos, cachear resultados.
- **Usar** `set` para verificar pertenencia rapida (`in`).
- **NO usar** si necesitas datos ordenados (usa arbol o lista ordenada).
- **NO usar** si la memoria es muy limitada (overhead de buckets vacios).
- **NO usar** si las claves no son hashables (listas, dicts, sets mutables).

## Errores clasicos

- **Usar listas/dicts como claves**: son mutables, no son hashables. Usa tuplas o frozensets.
- **Asumir orden de insercion en Python < 3.7**: solo desde Python 3.7+ `dict` preserva orden.
- **Ignorar colisiones**: un hash malo degrada todo a O(n). Python lo maneja bien internamente.
- **Modificar un dict mientras iteras**: lanza `RuntimeError`. Itera sobre una copia: `list(d.items())`.
- **Confundir `d[k]` con `d.get(k)`**: el primero lanza `KeyError`, el segundo retorna `None`.
- **Olvidar que `set` no permite duplicados**: `{1, 1, 2}` es `{1, 2}`.

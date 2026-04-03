# Tablas Hash (Hash Tables)

## Que es

Una **tabla hash** (hash table o hash map) es una estructura de datos que asocia **claves** con **valores** usando una **funcion hash** para calcular la posicion donde almacenar cada par. Proporciona acceso, insercion y eliminacion en tiempo promedio O(1). En Python, `dict` y `set` son implementaciones de tablas hash.

## Diagrama

### Funcionamiento basico

```
         Funcion Hash
Clave ──────────────────► Indice ──► Valor

"ana"  ── hash("ana")  ── 2 ──► "Ingeniera"
"bob"  ── hash("bob")  ── 5 ──► "Doctor"
"eva"  ── hash("eva")  ── 1 ──► "Abogada"

Tabla interna (array):
  Indice   Clave    Valor
  ┌─────┬────────┬────────────┐
  │  0  │        │            │
  ├─────┼────────┼────────────┤
  │  1  │ "eva"  │ "Abogada"  │
  ├─────┼────────┼────────────┤
  │  2  │ "ana"  │ "Ingeniera"│
  ├─────┼────────┼────────────┤
  │  3  │        │            │
  ├─────┼────────┼────────────┤
  │  4  │        │            │
  ├─────┼────────┼────────────┤
  │  5  │ "bob"  │ "Doctor"   │
  └─────┴────────┴────────────┘
```

### Colision y encadenamiento (chaining)

```
hash("ana") = 2
hash("dan") = 2   ← colision! misma posicion

Resolucion por encadenamiento:

  Indice
  ┌─────┐    ┌──────────────┐    ┌──────────────┐
  │  2  │───►│ "ana":"Ing." │───►│ "dan":"Chef" │───► None
  └─────┘    └──────────────┘    └──────────────┘
```

### Colision y direccionamiento abierto (open addressing)

```
hash("ana") = 2  →  posicion 2 (libre, se inserta)
hash("dan") = 2  →  posicion 2 (ocupada!)
                 →  posicion 3 (libre, se inserta aqui)

  ┌─────┬────────┬────────────┐
  │  1  │        │            │
  ├─────┼────────┼────────────┤
  │  2  │ "ana"  │ "Ingeniera"│  ← posicion original
  ├─────┼────────┼────────────┤
  │  3  │ "dan"  │ "Chef"     │  ← desplazado (probing)
  ├─────┼────────┼────────────┤
  │  4  │        │            │
  └─────┴────────┴────────────┘
```

## Operaciones principales

| Operacion          | Promedio | Peor caso | Descripcion                  |
|--------------------|----------|-----------|------------------------------|
| Insercion          | O(1)     | O(n)      | Calcular hash e insertar     |
| Busqueda por clave | O(1)     | O(n)      | Calcular hash y acceder      |
| Eliminacion        | O(1)     | O(n)      | Calcular hash y remover      |
| Busqueda por valor | O(n)     | O(n)      | Recorrer todos los valores   |

El peor caso O(n) ocurre cuando todas las claves colisionan en la misma posicion.

## Como funciona

### La funcion hash

```
Entrada: cualquier dato inmutable (string, numero, tupla)
Salida:  un numero entero

hash("hola") = 1234567   →  1234567 % tamaño_tabla = indice

Buena funcion hash:
  - Distribuye uniformemente
  - Es determinista (misma entrada = misma salida)
  - Es rapida de calcular
```

### Factor de carga y rehashing

```
Factor de carga = numero_elementos / tamaño_tabla

  Factor 0.3 (disperso):        Factor 0.9 (denso):
  ┌───┬───┬───┬───┬───┐        ┌───┬───┬───┬───┬───┐
  │ X │   │   │ X │   │        │ X │ X │   │ X │ X │
  ├───┼───┼───┼───┼───┤        ├───┼───┼───┼───┼───┤
  │   │   │ X │   │   │        │ X │ X │ X │ X │   │
  └───┴───┴───┴───┴───┘        └───┴───┴───┴───┴───┘
  Pocas colisiones              Muchas colisiones

Rehashing (cuando factor > umbral, tipicamente 0.75):
1. Crear nueva tabla con el doble de tamaño
2. Recalcular hash de cada elemento
3. Insertar en la nueva tabla
```

## Cuando usarla

**Usar tablas hash cuando:**
- Necesitas busqueda rapida por clave (O(1) promedio)
- Quieres contar frecuencias de elementos
- Necesitas eliminar duplicados (set)
- Implementas caches o memorizacion
- Necesitas mapear relaciones clave-valor

**NO usar tablas hash cuando:**
- Necesitas elementos ordenados (usar arbol BST o sorted list)
- Las claves no son hashables (objetos mutables)
- La memoria es muy limitada (overhead de tabla subyacente)
- Necesitas recorrer en orden (el orden no esta garantizado)

## Casos de uso en el mundo real

- **Diccionarios Python**: `dict` es una tabla hash optimizada
- **Caches**: almacenar resultados ya calculados
- **Bases de datos**: indices hash para busqueda rapida
- **Conteo de palabras**: frecuencia de cada palabra en un texto
- **Deteccion de duplicados**: verificar si un elemento ya existe
- **DNS**: mapear nombres de dominio a direcciones IP

## Errores comunes

1. **Claves mutables**: en Python, las listas no pueden ser claves de dict porque son mutables. Usar tuplas.
2. **Asumir orden**: antes de Python 3.7, los dict no mantenian orden de insercion. Aunque ahora lo hacen, no es una propiedad general de las tablas hash.
3. **Ignorar colisiones**: una mala funcion hash causa muchas colisiones, degradando el rendimiento a O(n).
4. **No manejar claves inexistentes**: acceder a `dict[clave]` cuando la clave no existe lanza `KeyError`. Usar `.get(clave, default)` o `defaultdict`.
5. **Confundir hash con cifrado**: una funcion hash no es reversible por diseño, pero no todas son seguras criptograficamente. No usar `hash()` de Python para seguridad.

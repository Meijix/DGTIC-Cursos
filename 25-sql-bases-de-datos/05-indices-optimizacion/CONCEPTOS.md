# 05 — Indices y Optimizacion

## Que es un Indice

Un indice es una estructura de datos que acelera la busqueda de filas en una tabla,
similar al indice de un libro. Sin indice, la base de datos debe recorrer
**todas** las filas (full table scan). Con indice, localiza los datos directamente.

```
  Sin indice (Full Scan):          Con indice (B-tree):
  +---+---+---+---+---+---+       Buscar "Garcia"
  | 1 | 2 | 3 | 4 | 5 | 6 |       +-------+
  +---+---+---+---+---+---+       |  M    |
  Revisa fila por fila             /         \
  O(n)                           /             \
                              +---+           +---+
                              | D |           | R |
                             / \             / \
                           +--+ +--+       +--+ +--+
                           |A | |G |       |M | |T |
                           +--+ +--+       +--+ +--+
                                 ^
                              Encontrado! O(log n)
```

## Arbol B-tree (B-tree)

La estructura mas comun para indices. Es un arbol balanceado donde:
- Cada nodo puede tener multiples claves
- Las hojas estan al mismo nivel (balanceado)
- Busqueda, insercion y eliminacion en **O(log n)**

```
  B-tree de orden 3 (max 2 claves por nodo):

                    +--------+
                    | 30 | 60|
                    +--------+
                   /    |     \
            +------+ +------+ +------+
            |10|20 | |40|50 | |70|80 |
            +------+ +------+ +------+
           / |  \    / |  \   / |  \
          hojas con punteros a las filas reales
          de la tabla

  Buscar el valor 50:
  1. Raiz: 50 > 30, 50 < 60 --> hijo central
  2. Nodo [40,50]: 50 encontrado!
  Solo 2 comparaciones para encontrar entre miles de filas
```

## Crear Indices

```sql
-- Indice simple
CREATE INDEX idx_apellido ON estudiantes(apellido);

-- Indice unico (no permite duplicados)
CREATE UNIQUE INDEX idx_email ON usuarios(email);

-- Indice compuesto (multiples columnas)
CREATE INDEX idx_ciudad_edad ON estudiantes(ciudad, edad);

-- Eliminar indice
DROP INDEX idx_apellido;
```

## Indice Compuesto

El orden de las columnas **importa**. Un indice (ciudad, edad) sirve para:

```
  idx_ciudad_edad(ciudad, edad)

  Sirve para:                    NO sirve para:
  WHERE ciudad = 'CDMX'          WHERE edad = 22
  WHERE ciudad = 'CDMX'          (edad sola, no es prefijo)
    AND edad > 20
  ORDER BY ciudad, edad

  Regla: el indice se usa de izquierda a derecha
         (leftmost prefix rule)
```

## EXPLAIN — Analizar Plan de Ejecucion

EXPLAIN muestra **como** la base de datos ejecutara una consulta,
sin ejecutarla realmente.

```sql
EXPLAIN SELECT * FROM estudiantes WHERE apellido = 'Garcia';
```

```
  Resultado (ejemplo PostgreSQL):
  +---------------------------------------------------------+
  | QUERY PLAN                                              |
  +---------------------------------------------------------+
  | Index Scan using idx_apellido on estudiantes            |
  |   Index Cond: (apellido = 'Garcia')                     |
  |   Cost: 0.29..8.30  Rows: 1  Width: 120                |
  +---------------------------------------------------------+
```

```sql
-- EXPLAIN ANALYZE: ejecuta la consulta y muestra tiempos reales
EXPLAIN ANALYZE SELECT * FROM estudiantes WHERE apellido = 'Garcia';
```

### Tipos de Scan

```
  +-------------------+------------------------------------+
  | Tipo de Scan      | Significado                        |
  +-------------------+------------------------------------+
  | Seq Scan          | Recorre toda la tabla (lento)      |
  | Index Scan        | Usa un indice (rapido)             |
  | Index Only Scan   | Todo se resuelve con el indice     |
  | Bitmap Index Scan | Indice + filtrado por bloques      |
  +-------------------+------------------------------------+
```

## Consejos de Optimizacion

### Cuando SI crear indices

```
  - Columnas en WHERE frecuentemente
  - Columnas en JOIN (Foreign Keys)
  - Columnas en ORDER BY
  - Columnas con alta cardinalidad (muchos valores unicos)
```

### Cuando NO crear indices

```
  - Tablas muy pequenias (< 1000 filas)
  - Columnas con pocos valores unicos (booleanos, estado)
  - Tablas con muchas escrituras y pocas lecturas
  - Columnas que casi nunca se filtran
```

### Costo de los Indices

```
  Beneficio:                  Costo:
  +-------------------+       +-------------------+
  | SELECT mas rapido |       | INSERT mas lento  |
  | WHERE optimizado  |       | UPDATE mas lento  |
  | JOIN eficiente    |       | DELETE mas lento  |
  +-------------------+       | Mas espacio disco |
                              +-------------------+

  Cada indice se debe actualizar con cada escritura.
```

## Estrategias de Optimizacion de Consultas

```
  1. Seleccionar solo columnas necesarias (evitar SELECT *)
  2. Usar WHERE para filtrar temprano
  3. Crear indices en columnas de filtrado/join
  4. Evitar funciones en columnas indexadas en WHERE
     MAL:  WHERE UPPER(nombre) = 'ANA'
     BIEN: WHERE nombre = 'Ana'
  5. Usar LIMIT cuando no necesitas todas las filas
  6. Preferir JOIN sobre subqueries correlacionadas
  7. Usar EXPLAIN para verificar que se usen indices
  8. Evitar SELECT DISTINCT innecesario
  9. Usar EXISTS en lugar de IN para subqueries grandes
  10. Mantener estadisticas actualizadas (ANALYZE)
```

## Tipos de Indices Especiales

```
  +--------------------+-------------------------------------+
  | Tipo               | Uso                                 |
  +--------------------+-------------------------------------+
  | B-tree (default)   | Comparaciones =, <, >, BETWEEN      |
  | Hash               | Solo igualdad (=)                    |
  | GIN                | Arrays, JSONB, busqueda de texto     |
  | GiST               | Datos geometricos, rangos            |
  | BRIN               | Datos ordenados fisicamente          |
  +--------------------+-------------------------------------+
```

## Indice Parcial

Indice que solo cubre un subconjunto de filas:

```sql
-- Solo indexar pedidos activos (los mas consultados)
CREATE INDEX idx_pedidos_activos
ON pedidos(fecha)
WHERE estado = 'activo';
```

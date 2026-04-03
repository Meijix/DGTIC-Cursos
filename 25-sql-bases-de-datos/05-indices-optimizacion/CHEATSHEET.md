# 05 — Indices y Optimizacion: Cheatsheet

## Crear / Eliminar Indices

```sql
CREATE INDEX idx_nombre ON tabla(columna);
CREATE UNIQUE INDEX idx_email ON tabla(email);
CREATE INDEX idx_comp ON tabla(col1, col2);    -- compuesto
CREATE INDEX idx_parcial ON tabla(col) WHERE condicion;
DROP INDEX idx_nombre;
```

## Tipos de Indice

```
  B-tree (default)  — =, <, >, <=, >=, BETWEEN, LIKE 'abc%'
  Hash              — solo =
  GIN               — arrays, JSONB, full-text
  GiST              — geometria, rangos
  BRIN              — datos fisicamente ordenados
```

## EXPLAIN

```sql
EXPLAIN SELECT ...;                -- plan sin ejecutar
EXPLAIN ANALYZE SELECT ...;        -- plan + tiempos reales
EXPLAIN (FORMAT JSON) SELECT ...;  -- salida en JSON
```

## Tipos de Scan (de mejor a peor)

```
  Index Only Scan   — todo del indice, no toca la tabla
  Index Scan        — usa indice + accede a tabla
  Bitmap Index Scan — indice por bloques
  Seq Scan          — recorre toda la tabla (full scan)
```

## Reglas de Indice Compuesto

```
  INDEX(a, b, c) sirve para:
    WHERE a = ?
    WHERE a = ? AND b = ?
    WHERE a = ? AND b = ? AND c = ?
    ORDER BY a, b, c

  NO sirve para:
    WHERE b = ?           (falta prefijo a)
    WHERE c = ?           (falta prefijo a, b)
    ORDER BY b, c         (falta prefijo a)
```

## Cuando Indexar

```
  SI:                              NO:
  - Columnas en WHERE              - Tablas < 1000 filas
  - Foreign Keys                   - Columnas boolean/estado
  - Columnas en ORDER BY           - Muchas escrituras
  - Alta cardinalidad              - Columnas rara vez filtradas
```

## Tips de Optimizacion

```
  1. Evitar SELECT *
  2. Filtrar con WHERE temprano
  3. Indices en FK y columnas de filtro
  4. No usar funciones en columnas indexadas
  5. LIMIT cuando sea posible
  6. JOIN > subquery correlacionada
  7. EXISTS > IN para subqueries grandes
  8. Revisar con EXPLAIN
  9. ANALYZE para estadisticas
```

## Anti-patrones

```sql
-- MAL: funcion anula el indice
WHERE YEAR(fecha) = 2026
-- BIEN:
WHERE fecha >= '2026-01-01' AND fecha < '2027-01-01'

-- MAL: LIKE con comodin al inicio
WHERE nombre LIKE '%ana'
-- BIEN:
WHERE nombre LIKE 'Ana%'

-- MAL: SELECT *
SELECT * FROM tabla_grande
-- BIEN:
SELECT col1, col2 FROM tabla_grande
```

## Ver Indices Existentes

```sql
-- PostgreSQL
SELECT indexname, tablename FROM pg_indexes WHERE tablename = 'mi_tabla';

-- MySQL
SHOW INDEX FROM mi_tabla;
```

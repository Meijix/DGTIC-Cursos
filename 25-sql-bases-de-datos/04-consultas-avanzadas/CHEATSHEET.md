# 04 — Consultas Avanzadas: Cheatsheet

## Subqueries

```sql
-- Escalar (un valor)
WHERE col > (SELECT AVG(col) FROM tabla)

-- Lista (IN)
WHERE col IN (SELECT col FROM otra_tabla WHERE ...)

-- Tabla (en FROM)
FROM (SELECT ... GROUP BY ...) AS alias

-- Correlacionada (referencia a consulta externa)
WHERE col > (SELECT AVG(col) FROM tabla t2 WHERE t2.grupo = t1.grupo)

-- EXISTS
WHERE EXISTS (SELECT 1 FROM tabla WHERE condicion)
WHERE NOT EXISTS (SELECT 1 FROM tabla WHERE condicion)
```

## Funciones de Agregacion

```sql
COUNT(*)       -- total de filas
COUNT(col)     -- filas no-NULL
SUM(col)       -- suma
AVG(col)       -- promedio
MIN(col)       -- minimo
MAX(col)       -- maximo
```

## GROUP BY + HAVING

```sql
SELECT grupo, COUNT(*), AVG(valor)
FROM tabla
WHERE condicion_filas
GROUP BY grupo
HAVING COUNT(*) > 5
ORDER BY AVG(valor) DESC;
```

## CASE / WHEN

```sql
CASE
    WHEN condicion1 THEN resultado1
    WHEN condicion2 THEN resultado2
    ELSE resultado_default
END AS alias
```

## COALESCE

```sql
COALESCE(valor1, valor2, valor3)   -- primer no-NULL
COALESCE(col, 'valor_default')     -- reemplazar NULL
```

## Window Functions

```sql
-- Ranking
ROW_NUMBER() OVER (ORDER BY col DESC)
RANK()       OVER (ORDER BY col DESC)
DENSE_RANK() OVER (ORDER BY col DESC)

-- Con particion
RANK() OVER (PARTITION BY grupo ORDER BY col DESC)

-- Filas vecinas
LAG(col, 1)  OVER (ORDER BY col)    -- fila anterior
LEAD(col, 1) OVER (ORDER BY col)    -- fila siguiente

-- Agregaciones de ventana
SUM(col)  OVER (PARTITION BY grupo)
AVG(col)  OVER (PARTITION BY grupo)
COUNT(*)  OVER (PARTITION BY grupo)
SUM(col)  OVER (ORDER BY col)       -- acumulado
```

## Diferencia entre RANK y DENSE_RANK

```
  Valores:     100, 100, 90, 80
  ROW_NUMBER:   1,   2,  3,  4
  RANK:         1,   1,  3,  4   (salta 2)
  DENSE_RANK:   1,   1,  2,  3   (no salta)
```

## Orden de Ejecucion

```
  FROM  ->  WHERE  ->  GROUP BY  ->  HAVING  ->  SELECT  ->  WINDOW  ->  ORDER BY  ->  LIMIT
```

## Patrones Comunes

```sql
-- Top N por grupo
SELECT * FROM (
    SELECT *, ROW_NUMBER() OVER (PARTITION BY grupo ORDER BY valor DESC) AS rn
    FROM tabla
) sub WHERE rn <= 3;

-- Diferencia con fila anterior
SELECT col, col - LAG(col) OVER (ORDER BY fecha) AS cambio FROM tabla;

-- Porcentaje del total
SELECT col, valor, valor * 100.0 / SUM(valor) OVER () AS pct FROM tabla;
```

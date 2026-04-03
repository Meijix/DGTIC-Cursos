# 04 — Consultas Avanzadas

## Subqueries (Subconsultas)

Una subquery es una consulta dentro de otra consulta. Pueden aparecer
en WHERE, FROM, SELECT o HAVING.

### Subquery Escalar (un solo valor)

```sql
-- Estudiantes con promedio superior al promedio general
SELECT nombre, promedio
FROM estudiantes
WHERE promedio > (SELECT AVG(promedio) FROM estudiantes);
```

### Subquery de Columna (lista de valores)

```sql
-- Estudiantes inscritos en algun curso de Computacion
SELECT nombre FROM estudiantes
WHERE id IN (
    SELECT estudiante_id FROM inscripciones
    WHERE curso_id IN (
        SELECT id FROM cursos WHERE departamento = 'Computacion'
    )
);
```

### Subquery de Tabla (tabla temporal)

```sql
-- Promedio de promedios por departamento
SELECT departamento, AVG(prom_curso) AS promedio_depto
FROM (
    SELECT c.departamento, AVG(i.calificacion) AS prom_curso
    FROM cursos c
    JOIN inscripciones i ON c.id = i.curso_id
    GROUP BY c.departamento, c.id
) AS promedios_por_curso
GROUP BY departamento;
```

### Subquery Correlacionada

Referencia la consulta externa. Se ejecuta una vez **por cada fila**.

```sql
-- Estudiantes cuyo promedio es mayor al promedio de su ciudad
SELECT nombre, ciudad, promedio
FROM estudiantes e1
WHERE promedio > (
    SELECT AVG(promedio) FROM estudiantes e2
    WHERE e2.ciudad = e1.ciudad  -- referencia a la consulta externa
);
```

### EXISTS / NOT EXISTS

```sql
-- Cursos que tienen al menos un estudiante inscrito
SELECT nombre FROM cursos c
WHERE EXISTS (
    SELECT 1 FROM inscripciones i WHERE i.curso_id = c.id
);

-- Cursos SIN estudiantes
SELECT nombre FROM cursos c
WHERE NOT EXISTS (
    SELECT 1 FROM inscripciones i WHERE i.curso_id = c.id
);
```

## Funciones de Agregacion

```
  +----------+----------------------------------+
  | Funcion  | Descripcion                      |
  +----------+----------------------------------+
  | COUNT(*) | Cuenta todas las filas           |
  | COUNT(c) | Cuenta filas donde c no es NULL  |
  | SUM(c)   | Suma los valores de la columna   |
  | AVG(c)   | Promedio de los valores           |
  | MIN(c)   | Valor minimo                     |
  | MAX(c)   | Valor maximo                     |
  +----------+----------------------------------+
```

```sql
SELECT
    COUNT(*) AS total,
    AVG(precio) AS precio_promedio,
    MIN(precio) AS mas_barato,
    MAX(precio) AS mas_caro,
    SUM(precio) AS valor_total
FROM productos;
```

## GROUP BY — Agrupar Resultados

Agrupa filas que comparten un valor y aplica funciones de agregacion a cada grupo.

```sql
SELECT ciudad, COUNT(*) AS total, AVG(edad) AS edad_promedio
FROM estudiantes
GROUP BY ciudad;
```

```
  Resultado:
  +----------+-------+----------------+
  | ciudad   | total | edad_promedio  |
  +----------+-------+----------------+
  | CDMX     |     4 |          20.5  |
  | Monterrey|     3 |          23.7  |
  | Puebla   |     2 |          24.5  |
  +----------+-------+----------------+
```

## HAVING — Filtrar Grupos

WHERE filtra filas **antes** de agrupar. HAVING filtra **despues** de agrupar.

```sql
-- Ciudades con mas de 3 estudiantes
SELECT ciudad, COUNT(*) AS total
FROM estudiantes
GROUP BY ciudad
HAVING COUNT(*) > 3;
```

```
  Orden de ejecucion:
  FROM -> WHERE -> GROUP BY -> HAVING -> SELECT -> ORDER BY
```

## CASE / WHEN — Logica Condicional

```sql
SELECT nombre, promedio,
    CASE
        WHEN promedio >= 9.0 THEN 'Excelente'
        WHEN promedio >= 8.0 THEN 'Bueno'
        WHEN promedio >= 7.0 THEN 'Regular'
        ELSE 'Insuficiente'
    END AS evaluacion
FROM estudiantes;
```

## COALESCE — Manejar NULLs

Devuelve el primer valor que no sea NULL.

```sql
-- Si telefono es NULL, mostrar 'Sin telefono'
SELECT nombre, COALESCE(telefono, 'Sin telefono') AS contacto
FROM estudiantes;

-- Primer contacto disponible
SELECT nombre, COALESCE(celular, telefono, email, 'Sin contacto') AS contacto
FROM personas;
```

## Window Functions (Funciones de Ventana)

Realizan calculos sobre un conjunto de filas **relacionadas** con la fila actual,
sin colapsar los resultados como GROUP BY.

```
  +------+--------+----------+-----------+
  | fila | nombre | promedio | ranking   |
  +------+--------+----------+-----------+
  |  1   | Maria  |  9.8     |  1        |  -- ROW_NUMBER()
  |  2   | Ana    |  9.5     |  2        |  sobre toda
  |  3   | Sofia  |  9.1     |  3        |  la tabla
  +------+--------+----------+-----------+
```

### ROW_NUMBER, RANK, DENSE_RANK

```sql
SELECT nombre, promedio,
    ROW_NUMBER() OVER (ORDER BY promedio DESC) AS fila,
    RANK()       OVER (ORDER BY promedio DESC) AS rango,
    DENSE_RANK() OVER (ORDER BY promedio DESC) AS rango_denso
FROM estudiantes;
```

```
  Diferencia con empates (promedio 9.0, 9.0, 8.5):
  ROW_NUMBER:  1, 2, 3    (siempre consecutivo)
  RANK:        1, 1, 3    (salta posiciones)
  DENSE_RANK:  1, 1, 2    (no salta)
```

### PARTITION BY — Ventana por Grupos

```sql
-- Ranking por ciudad
SELECT nombre, ciudad, promedio,
    RANK() OVER (PARTITION BY ciudad ORDER BY promedio DESC) AS rank_ciudad
FROM estudiantes;
```

### LAG / LEAD — Valores de Filas Vecinas

```sql
SELECT nombre, promedio,
    LAG(promedio, 1)  OVER (ORDER BY promedio DESC) AS anterior,
    LEAD(promedio, 1) OVER (ORDER BY promedio DESC) AS siguiente
FROM estudiantes;
```

### Agregaciones como Ventana

```sql
-- Promedio acumulado y total por departamento
SELECT nombre, departamento, salario,
    SUM(salario)   OVER (PARTITION BY departamento) AS total_depto,
    AVG(salario)   OVER (PARTITION BY departamento) AS promedio_depto,
    SUM(salario)   OVER (ORDER BY id) AS acumulado
FROM empleados;
```

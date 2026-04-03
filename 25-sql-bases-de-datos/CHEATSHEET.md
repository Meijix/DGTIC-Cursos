# SQL — Cheatsheet de Referencia Rapida

## CRUD Basico

```sql
-- SELECT: leer datos
SELECT columna1, columna2 FROM tabla WHERE condicion;
SELECT * FROM usuarios ORDER BY nombre ASC LIMIT 10;
SELECT DISTINCT ciudad FROM clientes;

-- INSERT: insertar datos
INSERT INTO tabla (col1, col2) VALUES ('val1', 'val2');
INSERT INTO tabla (col1, col2) VALUES ('a', 1), ('b', 2), ('c', 3);

-- UPDATE: actualizar datos
UPDATE tabla SET col1 = 'nuevo' WHERE id = 1;

-- DELETE: eliminar datos
DELETE FROM tabla WHERE condicion;
```

## Operadores WHERE

```sql
=, <>, !=, <, >, <=, >=       -- comparacion
AND, OR, NOT                   -- logicos
BETWEEN 10 AND 20             -- rango inclusivo
IN ('a', 'b', 'c')            -- lista de valores
LIKE 'A%'                     -- patron (% = cualquier cosa, _ = un caracter)
IS NULL / IS NOT NULL          -- valores nulos
EXISTS (subquery)              -- existencia de resultados
```

## JOINs — Diagrama de Referencia

```
  INNER JOIN          LEFT JOIN           RIGHT JOIN          FULL JOIN
  +---+---+           +---+---+           +---+---+           +---+---+
  |   |XXX|           |XXX|XXX|           |   |XXX|           |XXX|XXX|
  | A |XXX| B         | A |XXX| B         | A |XXX| B         | A |XXX| B
  |   |XXX|           |XXX|XXX|           |   |XXX|           |XXX|XXX|
  +---+---+           +---+---+           +---+---+           +---+---+
  Solo coinciden       Todo A +            Todo B +            Todo A y B
                       coinciden            coinciden
```

```sql
SELECT * FROM A INNER JOIN B ON A.id = B.a_id;
SELECT * FROM A LEFT JOIN B ON A.id = B.a_id;
SELECT * FROM A RIGHT JOIN B ON A.id = B.a_id;
SELECT * FROM A FULL OUTER JOIN B ON A.id = B.a_id;
```

## Funciones de Agregacion

```sql
COUNT(*)           -- contar filas
COUNT(col)         -- contar no-NULL
SUM(col)           -- sumar valores
AVG(col)           -- promedio
MIN(col)           -- valor minimo
MAX(col)           -- valor maximo
```

## GROUP BY / HAVING

```sql
SELECT departamento, COUNT(*) AS total, AVG(salario) AS promedio
FROM empleados
WHERE activo = true
GROUP BY departamento
HAVING COUNT(*) > 5
ORDER BY promedio DESC;
```

## CREATE TABLE con Restricciones

```sql
CREATE TABLE productos (
    id          SERIAL PRIMARY KEY,
    nombre      VARCHAR(100) NOT NULL,
    precio      DECIMAL(10,2) CHECK (precio > 0),
    categoria   VARCHAR(50) DEFAULT 'General',
    codigo      VARCHAR(20) UNIQUE,
    created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## Restricciones (Constraints)

```
  PRIMARY KEY   — identifica unico, no NULL
  FOREIGN KEY   — referencia a otra tabla
  NOT NULL      — no permite valores nulos
  UNIQUE        — no permite duplicados
  CHECK         — validacion personalizada
  DEFAULT       — valor por defecto
```

## Indices

```sql
CREATE INDEX idx_nombre ON tabla(columna);
CREATE UNIQUE INDEX idx_email ON usuarios(email);
CREATE INDEX idx_compuesto ON tabla(col1, col2);
DROP INDEX idx_nombre;
```

## Subqueries

```sql
-- Escalar (un valor)
SELECT nombre FROM productos WHERE precio > (SELECT AVG(precio) FROM productos);

-- Lista
SELECT * FROM usuarios WHERE id IN (SELECT user_id FROM ordenes WHERE total > 100);

-- Existe
SELECT * FROM productos p WHERE EXISTS (SELECT 1 FROM reviews r WHERE r.prod_id = p.id);
```

## Funciones de Ventana (Window Functions)

```sql
ROW_NUMBER() OVER (ORDER BY col)              -- numero secuencial
RANK() OVER (ORDER BY col)                    -- rango con saltos
DENSE_RANK() OVER (ORDER BY col)              -- rango sin saltos
LAG(col, 1) OVER (ORDER BY col)              -- valor anterior
LEAD(col, 1) OVER (ORDER BY col)             -- valor siguiente
SUM(col) OVER (PARTITION BY grupo)            -- suma por grupo
```

## Transacciones

```sql
BEGIN;
  UPDATE cuentas SET saldo = saldo - 100 WHERE id = 1;
  UPDATE cuentas SET saldo = saldo + 100 WHERE id = 2;
COMMIT;
-- Si algo falla: ROLLBACK;
```

## Orden de Ejecucion SQL

```
  1. FROM / JOIN       -- de donde vienen los datos
  2. WHERE             -- filtrar filas
  3. GROUP BY          -- agrupar
  4. HAVING            -- filtrar grupos
  5. SELECT            -- elegir columnas
  6. DISTINCT          -- eliminar duplicados
  7. ORDER BY          -- ordenar resultado
  8. LIMIT / OFFSET    -- limitar filas
```

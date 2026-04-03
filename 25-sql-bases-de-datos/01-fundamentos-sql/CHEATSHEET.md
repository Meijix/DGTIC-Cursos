# 01 — Fundamentos SQL: Cheatsheet

## SELECT

```sql
SELECT * FROM tabla;                          -- todas las columnas
SELECT col1, col2 FROM tabla;                 -- columnas especificas
SELECT DISTINCT col FROM tabla;               -- sin duplicados
SELECT col AS alias FROM tabla;               -- con alias
```

## INSERT

```sql
INSERT INTO tabla (col1, col2) VALUES ('a', 'b');
INSERT INTO tabla (col1, col2) VALUES ('a', 1), ('b', 2);
```

## UPDATE

```sql
UPDATE tabla SET col = 'nuevo' WHERE condicion;
UPDATE tabla SET col1 = 'a', col2 = 'b' WHERE id = 1;
```

## DELETE

```sql
DELETE FROM tabla WHERE condicion;
```

## WHERE — Operadores

```
  =              igual
  <> o !=        diferente
  > >= < <=      comparacion
  AND            ambas condiciones
  OR             al menos una
  NOT            negacion
  BETWEEN a AND b  rango inclusivo
  IN (a, b, c)  lista de valores
  LIKE 'patron'  coincidencia de texto
  IS NULL        es nulo
  IS NOT NULL    no es nulo
```

## LIKE — Comodines

```
  %    = cero o mas caracteres
  _    = exactamente un caracter

  'A%'     empieza con A
  '%ez'    termina con ez
  '%ar%'   contiene ar
  '_a%'    segunda letra es a
  'A___'   A seguida de 3 caracteres
```

## ORDER BY

```sql
SELECT * FROM tabla ORDER BY col ASC;          -- ascendente (A-Z, 0-9)
SELECT * FROM tabla ORDER BY col DESC;         -- descendente
SELECT * FROM tabla ORDER BY col1 ASC, col2 DESC;
```

## LIMIT / OFFSET

```sql
SELECT * FROM tabla LIMIT 10;                  -- primeros 10
SELECT * FROM tabla LIMIT 10 OFFSET 20;        -- 10 a partir del 21
```

## Orden de Ejecucion

```
  FROM  ->  WHERE  ->  SELECT  ->  DISTINCT  ->  ORDER BY  ->  LIMIT
```

## Ejemplos Rapidos

```sql
-- Buscar estudiantes mayores de 20 en CDMX
SELECT nombre, edad FROM estudiantes
WHERE edad > 20 AND ciudad = 'CDMX'
ORDER BY edad DESC;

-- Los 5 mas jovenes
SELECT nombre, edad FROM estudiantes
ORDER BY edad ASC LIMIT 5;

-- Nombres que empiezan con M
SELECT * FROM estudiantes WHERE nombre LIKE 'M%';
```

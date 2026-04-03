# 01 — Fundamentos SQL

## Que es SQL

SQL (Structured Query Language) es el lenguaje estandar para interactuar con
bases de datos relacionales. Permite consultar, insertar, actualizar y eliminar
datos de forma declarativa: describes **que** quieres obtener, no **como** obtenerlo.

## Anatomia de una Consulta SELECT

```
  SELECT columnas        <-- que columnas quiero
  FROM tabla             <-- de que tabla
  WHERE condicion        <-- filtrar filas
  ORDER BY columna       <-- ordenar resultado
  LIMIT n                <-- limitar cantidad
```

```sql
SELECT nombre, edad
FROM estudiantes
WHERE edad >= 18
ORDER BY nombre ASC
LIMIT 10;
```

## Operaciones CRUD

CRUD = Create, Read, Update, Delete. Son las cuatro operaciones fundamentales:

```
  +----------+-------------+---------------------------+
  | Operacion| Comando SQL | Descripcion               |
  +----------+-------------+---------------------------+
  | Create   | INSERT INTO | Insertar nuevos registros |
  | Read     | SELECT      | Leer/consultar datos      |
  | Update   | UPDATE      | Modificar datos existentes|
  | Delete   | DELETE FROM | Eliminar registros        |
  +----------+-------------+---------------------------+
```

## SELECT — Leer Datos

```sql
-- Todas las columnas
SELECT * FROM estudiantes;

-- Columnas especificas
SELECT nombre, apellido FROM estudiantes;

-- Con alias
SELECT nombre AS "Nombre Completo", edad AS "Edad" FROM estudiantes;

-- Valores unicos (sin duplicados)
SELECT DISTINCT ciudad FROM estudiantes;
```

## INSERT — Insertar Datos

```sql
-- Insertar una fila
INSERT INTO estudiantes (nombre, apellido, edad)
VALUES ('Ana', 'Garcia', 22);

-- Insertar multiples filas
INSERT INTO estudiantes (nombre, apellido, edad) VALUES
  ('Carlos', 'Lopez', 25),
  ('Maria', 'Torres', 21),
  ('Pedro', 'Ramirez', 23);
```

## UPDATE — Actualizar Datos

```sql
-- Actualizar un campo
UPDATE estudiantes SET edad = 23 WHERE nombre = 'Ana';

-- Actualizar multiples campos
UPDATE estudiantes SET edad = 26, ciudad = 'CDMX' WHERE id = 2;
```

**IMPORTANTE:** Siempre usar WHERE en UPDATE, o se modificaran TODAS las filas.

## DELETE — Eliminar Datos

```sql
-- Eliminar filas especificas
DELETE FROM estudiantes WHERE edad < 18;

-- Eliminar todo (peligroso!)
DELETE FROM estudiantes;
```

## WHERE — Filtrado de Filas

### Operadores de comparacion
```sql
SELECT * FROM estudiantes WHERE edad = 22;       -- igual
SELECT * FROM estudiantes WHERE edad <> 22;      -- diferente
SELECT * FROM estudiantes WHERE edad > 20;       -- mayor que
SELECT * FROM estudiantes WHERE edad >= 20;      -- mayor o igual
```

### Operadores logicos
```sql
SELECT * FROM estudiantes WHERE edad > 18 AND ciudad = 'CDMX';
SELECT * FROM estudiantes WHERE edad < 18 OR edad > 30;
SELECT * FROM estudiantes WHERE NOT ciudad = 'Puebla';
```

### BETWEEN — Rango
```sql
SELECT * FROM estudiantes WHERE edad BETWEEN 18 AND 25;
```

### IN — Lista de valores
```sql
SELECT * FROM estudiantes WHERE ciudad IN ('CDMX', 'Puebla', 'Monterrey');
```

### LIKE — Patrones de texto
```sql
SELECT * FROM estudiantes WHERE nombre LIKE 'A%';     -- empieza con A
SELECT * FROM estudiantes WHERE nombre LIKE '%ez';     -- termina en ez
SELECT * FROM estudiantes WHERE nombre LIKE '_a%';     -- segunda letra a
```

```
  Comodines LIKE:
  %  = cualquier secuencia de caracteres (0 o mas)
  _  = exactamente un caracter
```

### IS NULL — Valores nulos
```sql
SELECT * FROM estudiantes WHERE telefono IS NULL;
SELECT * FROM estudiantes WHERE telefono IS NOT NULL;
```

## ORDER BY — Ordenar Resultados

```sql
SELECT * FROM estudiantes ORDER BY nombre ASC;         -- A-Z (por defecto)
SELECT * FROM estudiantes ORDER BY edad DESC;          -- mayor a menor
SELECT * FROM estudiantes ORDER BY ciudad ASC, edad DESC;  -- doble orden
```

## LIMIT y OFFSET — Paginacion

```sql
SELECT * FROM estudiantes LIMIT 10;                    -- primeros 10
SELECT * FROM estudiantes LIMIT 10 OFFSET 20;          -- 10 desde la fila 21
```

```
  Filas:  1  2  3 ... 20 | 21 22 23 ... 30 | 31 ...
                           ^^^^^^^^^^^^^^^^^
                           LIMIT 10 OFFSET 20
```

## Flujo de Ejecucion de una Consulta

```
  1. FROM        --> identifica la tabla
  2. WHERE       --> filtra filas
  3. SELECT      --> elige columnas
  4. DISTINCT    --> elimina duplicados
  5. ORDER BY    --> ordena resultado
  6. LIMIT       --> limita cantidad
```

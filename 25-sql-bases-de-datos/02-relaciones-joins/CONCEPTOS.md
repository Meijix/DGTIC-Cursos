# 02 — Relaciones y JOINs

## Claves en Bases de Datos Relacionales

### PRIMARY KEY (Clave Primaria)
Identifica de forma **unica** cada fila en una tabla. No admite NULL ni duplicados.

```sql
CREATE TABLE estudiantes (
    id SERIAL PRIMARY KEY,    -- clave primaria auto-incremental
    nombre VARCHAR(50)
);
```

### FOREIGN KEY (Clave Foranea)
Referencia la clave primaria de **otra tabla**, creando una relacion entre ambas.

```sql
CREATE TABLE inscripciones (
    id SERIAL PRIMARY KEY,
    estudiante_id INTEGER REFERENCES estudiantes(id),  -- FK
    curso_id INTEGER REFERENCES cursos(id)             -- FK
);
```

## Tipos de Relaciones

### 1:1 — Uno a Uno
Cada registro de A se relaciona con exactamente un registro de B.

```
  usuarios              perfiles
  +----+--------+       +----+---------+-----------+
  | id | nombre |       | id | user_id | biografia |
  +----+--------+       +----+---------+-----------+
  |  1 | Ana    |------>|  1 |    1    | Dev...    |
  |  2 | Carlos |------>|  2 |    2    | DBA...    |
  +----+--------+       +----+---------+-----------+
                               UNIQUE FK
```

### 1:N — Uno a Muchos
Un registro de A se relaciona con muchos registros de B. La relacion mas comun.

```
  profesores             cursos
  +----+---------+       +----+--------+---------+
  | id | nombre  |       | id | nombre | prof_id |
  +----+---------+       +----+--------+---------+
  |  1 | Garcia  |--+--->|  1 | SQL    |    1    |
  |  2 | Lopez   |  +--->|  2 | Python |    1    |
  +----+---------+  +--->|  3 | Java   |    2    |
                         +----+--------+---------+
                                         FK
```

### N:M — Muchos a Muchos
Requiere una **tabla intermedia** (junction/pivot table).

```
  estudiantes        inscripciones        cursos
  +----+--------+    +--------+--------+  +----+--------+
  | id | nombre |    | est_id | cur_id |  | id | nombre |
  +----+--------+    +--------+--------+  +----+--------+
  |  1 | Ana    |--->|   1    |   1    |<-|  1 | SQL    |
  |  2 | Carlos |--->|   1    |   2    |<-|  2 | Python |
  +----+--------+    |   2    |   1    |  +----+--------+
                     +--------+--------+
                     Tabla intermedia
```

## JOINs — Combinar Tablas

Los JOINs permiten consultar datos de multiples tablas simultaneamente.

### INNER JOIN — Solo coincidencias

Devuelve unicamente las filas que tienen coincidencia en **ambas** tablas.

```
  Tabla A         Tabla B
  +-------+       +-------+
  | . . . |       | . . . |
  | . [XXX|XXXXXXX|XXX] . |
  | . . . |       | . . . |
  +-------+       +-------+
        Solo la interseccion
```

```sql
SELECT e.nombre, c.nombre AS curso
FROM estudiantes e
INNER JOIN inscripciones i ON e.id = i.estudiante_id
INNER JOIN cursos c ON i.curso_id = c.id;
```

### LEFT JOIN — Todo A + coincidencias de B

Devuelve **todas** las filas de A, y las coincidencias de B (NULL si no hay).

```
  Tabla A         Tabla B
  +-------+       +-------+
  |XXXXXXX|       | . . . |
  |XXXXXXX|XXXXXXX|XXX] . |
  |XXXXXXX|       | . . . |
  +-------+       +-------+
  Todo A + coincidencias
```

```sql
SELECT e.nombre, c.nombre AS curso
FROM estudiantes e
LEFT JOIN inscripciones i ON e.id = i.estudiante_id
LEFT JOIN cursos c ON i.curso_id = c.id;
-- Incluye estudiantes SIN inscripciones (curso = NULL)
```

### RIGHT JOIN — Todo B + coincidencias de A

Devuelve **todas** las filas de B, y las coincidencias de A (NULL si no hay).

```
  Tabla A         Tabla B
  +-------+       +-------+
  | . . . |       |XXXXXXX|
  | . [XXX|XXXXXXX|XXXXXXX|
  | . . . |       |XXXXXXX|
  +-------+       +-------+
  Coincidencias + todo B
```

```sql
SELECT e.nombre, c.nombre AS curso
FROM estudiantes e
RIGHT JOIN cursos c ON e.id = c.estudiante_id;
-- Incluye cursos SIN estudiantes
```

### FULL OUTER JOIN — Todo A + Todo B

Devuelve **todas** las filas de ambas tablas, con NULL donde no hay coincidencia.

```
  Tabla A         Tabla B
  +-------+       +-------+
  |XXXXXXX|       |XXXXXXX|
  |XXXXXXX|XXXXXXX|XXXXXXX|
  |XXXXXXX|       |XXXXXXX|
  +-------+       +-------+
  Todo A + todo B
```

```sql
SELECT e.nombre, c.nombre AS curso
FROM estudiantes e
FULL OUTER JOIN cursos c ON e.id = c.estudiante_id;
```

### SELF JOIN — Tabla consigo misma

Una tabla se une a si misma, util para jerarquias.

```sql
-- Empleados y sus jefes (en la misma tabla)
SELECT
    emp.nombre AS empleado,
    jefe.nombre AS jefe
FROM empleados emp
LEFT JOIN empleados jefe ON emp.jefe_id = jefe.id;
```

```
  empleados
  +----+---------+---------+
  | id | nombre  | jefe_id |
  +----+---------+---------+
  |  1 | Director|  NULL   |  <-- sin jefe
  |  2 | Gerente |    1    |  <-- jefe: Director
  |  3 | Analista|    2    |  <-- jefe: Gerente
  +----+---------+---------+
```

## Tabla Intermedia (Junction Table)

Para relaciones N:M, la tabla intermedia contiene las FKs de ambas tablas:

```sql
CREATE TABLE inscripciones (
    estudiante_id INTEGER REFERENCES estudiantes(id),
    curso_id      INTEGER REFERENCES cursos(id),
    fecha         DATE DEFAULT CURRENT_DATE,
    PRIMARY KEY (estudiante_id, curso_id)  -- PK compuesta
);
```

## Resumen Visual de JOINs

```
  INNER JOIN       LEFT JOIN        RIGHT JOIN       FULL JOIN
  A [X] B          [AX] B           A [XB]           [AXB]
  Solo ambos       Todo A            Todo B           Todos
```

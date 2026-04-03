# 02 — Relaciones y JOINs: Cheatsheet

## Claves

```sql
PRIMARY KEY        -- identifica unico, no NULL, no duplicados
FOREIGN KEY        -- referencia PK de otra tabla
UNIQUE             -- no duplicados (permite 1 NULL)
```

## Tipos de Relaciones

```
  1:1    Un usuario  --> un perfil
  1:N    Un profesor --> muchos cursos
  N:M    Muchos estudiantes <--> muchos cursos (necesita tabla intermedia)
```

## JOINs — Sintaxis Rapida

```sql
-- INNER JOIN: solo coincidencias
SELECT * FROM A INNER JOIN B ON A.id = B.a_id;

-- LEFT JOIN: todo A + coincidencias de B
SELECT * FROM A LEFT JOIN B ON A.id = B.a_id;

-- RIGHT JOIN: todo B + coincidencias de A
SELECT * FROM A RIGHT JOIN B ON A.id = B.a_id;

-- FULL OUTER JOIN: todo A y todo B
SELECT * FROM A FULL OUTER JOIN B ON A.id = B.a_id;

-- SELF JOIN: tabla consigo misma
SELECT * FROM A a1 JOIN A a2 ON a1.parent_id = a2.id;

-- CROSS JOIN: producto cartesiano
SELECT * FROM A CROSS JOIN B;
```

## Diagrama de JOINs

```
  INNER        LEFT         RIGHT        FULL
  +---+---+    +---+---+    +---+---+    +---+---+
  |   |XXX|    |XXX|XXX|    |   |XXX|    |XXX|XXX|
  | A |XXX| B  | A |XXX| B  | A |XXX| B  | A |XXX| B
  |   |XXX|    |XXX|XXX|    |   |XXX|    |XXX|XXX|
  +---+---+    +---+---+    +---+---+    +---+---+
```

## LEFT JOIN para encontrar "sin relacion"

```sql
-- Estudiantes SIN inscripciones
SELECT e.nombre
FROM estudiantes e
LEFT JOIN inscripciones i ON e.id = i.estudiante_id
WHERE i.id IS NULL;
```

## Tabla Intermedia (N:M)

```sql
CREATE TABLE estudiante_curso (
    estudiante_id INT REFERENCES estudiantes(id),
    curso_id      INT REFERENCES cursos(id),
    PRIMARY KEY (estudiante_id, curso_id)
);
```

## JOIN Multiple

```sql
SELECT e.nombre, c.nombre AS curso, p.nombre AS profesor
FROM estudiantes e
JOIN inscripciones i ON e.id = i.estudiante_id
JOIN cursos c ON i.curso_id = c.id
JOIN profesores p ON c.profesor_id = p.id;
```

## Errores Comunes

```
  -- Olvidar la condicion ON (produce CROSS JOIN)
  -- Ambiguedad de columnas: usar alias (e.id, c.id)
  -- JOIN sin indice en FK: consulta lenta
  -- Confundir LEFT con INNER: filas perdidas
```

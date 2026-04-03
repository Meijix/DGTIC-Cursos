# 03 — Diseno de Esquema

## Diagrama Entidad-Relacion (ER)

Un diagrama ER modela las entidades, sus atributos y las relaciones entre ellas.
Es el primer paso antes de crear las tablas SQL.

```
  +-------------+        +----------------+        +-----------+
  |    AUTOR    |        |     LIBRO      |        |  GENERO   |
  |-------------|        |----------------|        |-----------|
  | PK id       |---1:N--| PK id          |--N:1---| PK id     |
  | nombre      |        | titulo         |        | nombre    |
  | nacionalidad|        | isbn           |        +-----------+
  | fecha_nac   |        | FK autor_id    |
  +-------------+        | FK genero_id   |
                         | anio_pub       |
        +-------------+  +----------------+
        |  PRESTAMO   |         |
        |-------------|         |
        | PK id       |         |
        | FK libro_id |---------+
        | FK socio_id |
        | fecha_prest |
        | fecha_devol |
        +-------------+
              |
        +-------------+
        |    SOCIO    |
        |-------------|
        | PK id       |
        | nombre      |
        | email       |
        | telefono    |
        +-------------+
```

## Normalizacion

La normalizacion organiza las tablas para reducir **redundancia** y evitar
**anomalias** de insercion, actualizacion y eliminacion.

### Primera Forma Normal (1NF)

- Cada celda contiene un **unico valor** (atomico).
- No hay grupos repetidos ni arrays en una celda.

```
  MAL (viola 1NF):                    BIEN (cumple 1NF):
  +----+---------+----------------+   +----+---------+-----------+
  | id | nombre  | telefonos      |   | id | nombre  | telefono  |
  +----+---------+----------------+   +----+---------+-----------+
  |  1 | Ana     | 555-1234,      |   |  1 | Ana     | 555-1234  |
  |    |         |  555-5678      |   |  1 | Ana     | 555-5678  |
  +----+---------+----------------+   +----+---------+-----------+
    Multiples valores en una celda     Un valor por celda
```

### Segunda Forma Normal (2NF)

- Cumple 1NF.
- Todos los atributos no-clave dependen de **toda** la clave primaria
  (no de una parte).

```
  MAL (viola 2NF, PK compuesta):
  +----------+----------+--------+--------------+
  | est_id   | curso_id | calif  | nombre_curso |
  +----------+----------+--------+--------------+
  nombre_curso depende solo de curso_id, no de la PK completa

  BIEN (cumple 2NF):
  inscripciones                    cursos
  +--------+--------+--------+    +----+---------+
  | est_id | cur_id | calif  |    | id | nombre  |
  +--------+--------+--------+    +----+---------+
```

### Tercera Forma Normal (3NF)

- Cumple 2NF.
- No hay dependencias **transitivas**: ningun atributo no-clave depende
  de otro atributo no-clave.

```
  MAL (viola 3NF):
  +----+--------+--------+-------------+
  | id | nombre | depto  | depto_ubica |
  +----+--------+--------+-------------+
  depto_ubica depende de depto, no de id (transitiva)

  BIEN (cumple 3NF):
  empleados                  departamentos
  +----+--------+--------+  +--------+----------+
  | id | nombre | dep_id |  | id     | ubicacion|
  +----+--------+--------+  +--------+----------+
```

## Denormalizacion

A veces se **denormaliza** intencionalmente para mejorar rendimiento
de lectura, aceptando cierta redundancia.

```
  Normalizacion              vs         Denormalizacion
  +-----------------------+            +------------------------+
  | Menos redundancia     |            | Consultas mas rapidas  |
  | Mas integridad        |            | Menos JOINs            |
  | Mas JOINs necesarios  |            | Mas espacio en disco   |
  | Escrituras mas rapidas|            | Riesgo de inconsistencia|
  +-----------------------+            +------------------------+
```

## CREATE TABLE con Restricciones

```sql
CREATE TABLE libros (
    id          SERIAL PRIMARY KEY,
    titulo      VARCHAR(200) NOT NULL,
    isbn        VARCHAR(13) UNIQUE NOT NULL,
    anio_pub    INTEGER CHECK (anio_pub > 1450),
    precio      DECIMAL(8,2) CHECK (precio >= 0),
    paginas     INTEGER DEFAULT 0,
    autor_id    INTEGER NOT NULL REFERENCES autores(id),
    genero_id   INTEGER REFERENCES generos(id),
    created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## Restricciones (Constraints)

```
  +-------------+-------------------------------------------+
  | Constraint  | Descripcion                               |
  +-------------+-------------------------------------------+
  | PRIMARY KEY | Identifica unica, no NULL                 |
  | FOREIGN KEY | Referencia PK de otra tabla               |
  | NOT NULL    | No permite valores nulos                  |
  | UNIQUE      | No permite duplicados                     |
  | CHECK       | Validacion personalizada                  |
  | DEFAULT     | Valor por defecto si no se especifica     |
  +-------------+-------------------------------------------+
```

## Acciones Referenciales (ON DELETE / ON UPDATE)

```sql
CREATE TABLE prestamos (
    id       SERIAL PRIMARY KEY,
    libro_id INTEGER REFERENCES libros(id) ON DELETE CASCADE,
    socio_id INTEGER REFERENCES socios(id) ON DELETE SET NULL
);
```

```
  CASCADE      — elimina/actualiza en cascada
  SET NULL     — pone NULL en la FK
  SET DEFAULT  — pone el valor DEFAULT
  RESTRICT     — impide la operacion (por defecto)
  NO ACTION    — similar a RESTRICT
```

## Convenciones de Nombres

```
  Tablas:     plural, snake_case     (estudiantes, prestamos_libros)
  Columnas:   singular, snake_case   (nombre, fecha_nacimiento)
  PK:         id
  FK:         tabla_singular_id      (autor_id, genero_id)
  Indices:    idx_tabla_columna      (idx_libros_isbn)
  Booleanos:  is_/has_ prefijo       (is_activo, has_descuento)
```

## Ejemplo Completo: Sistema de Biblioteca

```
  +----------+       +----------+       +---------+
  | autores  |--1:N--| libros   |--N:1--| generos |
  +----------+       +----------+       +---------+
                          |
                         1:N
                          |
                     +----------+
                     | prestamos|
                     +----------+
                          |
                         N:1
                          |
                     +----------+
                     |  socios  |
                     +----------+
```

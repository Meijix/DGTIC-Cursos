-- ============================================================
-- 02 — Relaciones y JOINs: Ejemplos Practicos
-- Base de datos: Sistema escolar con multiples tablas
-- ============================================================

-- ------------------------------------------------------------
-- CREAR TABLAS CON RELACIONES
-- ------------------------------------------------------------

-- Tabla de profesores
CREATE TABLE profesores (
    id      SERIAL PRIMARY KEY,
    nombre  VARCHAR(100) NOT NULL,
    email   VARCHAR(100) UNIQUE,
    depto   VARCHAR(50)
);

-- Tabla de cursos (1:N con profesores)
CREATE TABLE cursos (
    id          SERIAL PRIMARY KEY,
    nombre      VARCHAR(100) NOT NULL,
    creditos    INTEGER DEFAULT 6,
    profesor_id INTEGER REFERENCES profesores(id)
);

-- Tabla de estudiantes
CREATE TABLE estudiantes (
    id       SERIAL PRIMARY KEY,
    nombre   VARCHAR(100) NOT NULL,
    email    VARCHAR(100) UNIQUE,
    semestre INTEGER CHECK (semestre BETWEEN 1 AND 12)
);

-- Tabla intermedia: inscripciones (N:M entre estudiantes y cursos)
CREATE TABLE inscripciones (
    estudiante_id INTEGER REFERENCES estudiantes(id),
    curso_id      INTEGER REFERENCES cursos(id),
    fecha         DATE DEFAULT CURRENT_DATE,
    calificacion  DECIMAL(4,2),
    PRIMARY KEY (estudiante_id, curso_id)
);

-- Tabla de empleados con auto-referencia (SELF JOIN)
CREATE TABLE empleados (
    id       SERIAL PRIMARY KEY,
    nombre   VARCHAR(100) NOT NULL,
    puesto   VARCHAR(50),
    jefe_id  INTEGER REFERENCES empleados(id)
);

-- ------------------------------------------------------------
-- INSERTAR DATOS DE EJEMPLO
-- ------------------------------------------------------------

INSERT INTO profesores (nombre, email, depto) VALUES
    ('Dr. Garcia',   'garcia@uni.edu',   'Computacion'),
    ('Dra. Lopez',   'lopez@uni.edu',    'Matematicas'),
    ('Dr. Martinez', 'martinez@uni.edu', 'Computacion'),
    ('Dra. Torres',  'torres@uni.edu',   'Fisica');

INSERT INTO cursos (nombre, creditos, profesor_id) VALUES
    ('SQL Basico',          6, 1),
    ('Python Avanzado',     8, 1),
    ('Calculo III',         8, 2),
    ('Inteligencia Artificial', 10, 3),
    ('Mecanica Cuantica',   8, 4),
    ('Estadistica',         6, NULL);  -- curso sin profesor asignado

INSERT INTO estudiantes (nombre, email, semestre) VALUES
    ('Ana Reyes',     'ana@uni.edu',     3),
    ('Carlos Diaz',   'carlos@uni.edu',  5),
    ('Maria Flores',  'maria@uni.edu',   3),
    ('Pedro Sanchez',  'pedro@uni.edu',   7),
    ('Laura Moreno',  'laura@uni.edu',   1);  -- sin inscripciones

INSERT INTO inscripciones (estudiante_id, curso_id, calificacion) VALUES
    (1, 1, 9.5),   -- Ana en SQL
    (1, 2, 8.8),   -- Ana en Python
    (2, 1, 7.2),   -- Carlos en SQL
    (2, 3, 8.0),   -- Carlos en Calculo
    (2, 4, 9.1),   -- Carlos en IA
    (3, 1, 9.8),   -- Maria en SQL
    (3, 2, 9.0),   -- Maria en Python
    (4, 4, 6.5),   -- Pedro en IA
    (4, 5, 7.8);   -- Pedro en Mecanica

INSERT INTO empleados (nombre, puesto, jefe_id) VALUES
    ('Director General', 'Director',  NULL),
    ('Gerente TI',       'Gerente',   1),
    ('Gerente RRHH',     'Gerente',   1),
    ('Analista Sr.',     'Analista',  2),
    ('Analista Jr.',     'Analista',  2),
    ('Reclutador',       'Asistente', 3);

-- ------------------------------------------------------------
-- INNER JOIN: Solo filas que coinciden en ambas tablas
-- ------------------------------------------------------------

-- Estudiantes y sus cursos (solo los inscritos)
SELECT
    e.nombre AS estudiante,
    c.nombre AS curso,
    i.calificacion
FROM estudiantes e
INNER JOIN inscripciones i ON e.id = i.estudiante_id
INNER JOIN cursos c ON i.curso_id = c.id
ORDER BY e.nombre, c.nombre;

-- Cursos con su profesor
SELECT c.nombre AS curso, p.nombre AS profesor
FROM cursos c
INNER JOIN profesores p ON c.profesor_id = p.id;

-- ------------------------------------------------------------
-- LEFT JOIN: Todas las filas de la tabla izquierda
-- ------------------------------------------------------------

-- Todos los estudiantes, incluyendo los SIN inscripciones
SELECT
    e.nombre AS estudiante,
    c.nombre AS curso
FROM estudiantes e
LEFT JOIN inscripciones i ON e.id = i.estudiante_id
LEFT JOIN cursos c ON i.curso_id = c.id
ORDER BY e.nombre;
-- Laura aparece con curso = NULL (no esta inscrita)

-- Todos los cursos, incluyendo los SIN profesor
SELECT c.nombre AS curso, p.nombre AS profesor
FROM cursos c
LEFT JOIN profesores p ON c.profesor_id = p.id;
-- Estadistica aparece con profesor = NULL

-- Encontrar estudiantes que NO tienen inscripciones
SELECT e.nombre AS estudiante_sin_cursos
FROM estudiantes e
LEFT JOIN inscripciones i ON e.id = i.estudiante_id
WHERE i.estudiante_id IS NULL;

-- ------------------------------------------------------------
-- RIGHT JOIN: Todas las filas de la tabla derecha
-- ------------------------------------------------------------

-- Todos los profesores, incluyendo los que no dan cursos
SELECT p.nombre AS profesor, c.nombre AS curso
FROM cursos c
RIGHT JOIN profesores p ON c.profesor_id = p.id;

-- ------------------------------------------------------------
-- FULL OUTER JOIN: Todas las filas de ambas tablas
-- ------------------------------------------------------------

-- Todos los estudiantes y todos los cursos
SELECT
    e.nombre AS estudiante,
    c.nombre AS curso
FROM estudiantes e
FULL OUTER JOIN inscripciones i ON e.id = i.estudiante_id
FULL OUTER JOIN cursos c ON i.curso_id = c.id
ORDER BY e.nombre;

-- ------------------------------------------------------------
-- SELF JOIN: Tabla consigo misma
-- ------------------------------------------------------------

-- Empleados y sus jefes
SELECT
    emp.nombre   AS empleado,
    emp.puesto   AS puesto,
    jefe.nombre  AS jefe
FROM empleados emp
LEFT JOIN empleados jefe ON emp.jefe_id = jefe.id
ORDER BY emp.id;

-- Solo empleados que tienen jefe
SELECT
    emp.nombre  AS empleado,
    jefe.nombre AS reporta_a
FROM empleados emp
INNER JOIN empleados jefe ON emp.jefe_id = jefe.id;

-- ------------------------------------------------------------
-- CONSULTAS COMBINADAS AVANZADAS
-- ------------------------------------------------------------

-- Estudiantes, cursos y profesores en una sola consulta
SELECT
    e.nombre  AS estudiante,
    c.nombre  AS curso,
    p.nombre  AS profesor,
    i.calificacion
FROM estudiantes e
JOIN inscripciones i ON e.id = i.estudiante_id
JOIN cursos c ON i.curso_id = c.id
JOIN profesores p ON c.profesor_id = p.id
ORDER BY e.nombre;

-- Promedio por curso con nombre del profesor
SELECT
    c.nombre        AS curso,
    p.nombre        AS profesor,
    COUNT(*)        AS inscritos,
    AVG(i.calificacion) AS promedio
FROM cursos c
JOIN inscripciones i ON c.id = i.curso_id
JOIN profesores p ON c.profesor_id = p.id
GROUP BY c.nombre, p.nombre
ORDER BY promedio DESC;

-- Cursos sin estudiantes inscritos
SELECT c.nombre AS curso_vacio
FROM cursos c
LEFT JOIN inscripciones i ON c.id = i.curso_id
WHERE i.curso_id IS NULL;

-- Estudiantes inscritos en mas de 2 cursos
SELECT e.nombre, COUNT(*) AS total_cursos
FROM estudiantes e
JOIN inscripciones i ON e.id = i.estudiante_id
GROUP BY e.nombre
HAVING COUNT(*) > 2;

-- ============================================================
-- 01 — Fundamentos SQL: Ejemplos Practicos
-- Base de datos: Sistema escolar de estudiantes
-- ============================================================

-- ------------------------------------------------------------
-- CREAR LA TABLA DE ESTUDIANTES
-- ------------------------------------------------------------
CREATE TABLE estudiantes (
    id          SERIAL PRIMARY KEY,
    nombre      VARCHAR(50) NOT NULL,
    apellido    VARCHAR(50) NOT NULL,
    edad        INTEGER CHECK (edad > 0),
    email       VARCHAR(100) UNIQUE,
    ciudad      VARCHAR(50),
    promedio    DECIMAL(4,2),
    activo      BOOLEAN DEFAULT true,
    created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ------------------------------------------------------------
-- INSERT: Insertar datos de ejemplo
-- ------------------------------------------------------------

-- Insertar un registro
INSERT INTO estudiantes (nombre, apellido, edad, email, ciudad, promedio)
VALUES ('Ana', 'Garcia', 22, 'ana@correo.com', 'CDMX', 9.5);

-- Insertar multiples registros
INSERT INTO estudiantes (nombre, apellido, edad, email, ciudad, promedio) VALUES
    ('Carlos',   'Lopez',     25, 'carlos@correo.com',   'Monterrey',  8.2),
    ('Maria',    'Torres',    21, 'maria@correo.com',    'CDMX',       9.8),
    ('Pedro',    'Ramirez',   23, 'pedro@correo.com',    'Puebla',     7.5),
    ('Laura',    'Hernandez', 20, 'laura@correo.com',    'CDMX',       8.9),
    ('Miguel',   'Diaz',      24, 'miguel@correo.com',   'Guadalajara', 6.8),
    ('Sofia',    'Martinez',  22, 'sofia@correo.com',    'Monterrey',  9.1),
    ('Diego',    'Sanchez',   26, 'diego@correo.com',    'Puebla',     7.2),
    ('Valentina','Flores',    19, 'vale@correo.com',     'CDMX',       9.4),
    ('Andres',   'Moreno',    21, 'andres@correo.com',   'Guadalajara', 8.0),
    ('Isabella', 'Ruiz',      23, NULL,                  'Monterrey',  8.6),
    ('Fernando', 'Castro',    20, 'fer@correo.com',      NULL,         7.8);

-- ------------------------------------------------------------
-- SELECT: Consultas basicas
-- ------------------------------------------------------------

-- Todos los estudiantes
SELECT * FROM estudiantes;

-- Solo nombre y edad
SELECT nombre, apellido, edad FROM estudiantes;

-- Con alias para columnas
SELECT
    nombre || ' ' || apellido AS nombre_completo,
    edad,
    promedio AS calificacion
FROM estudiantes;

-- Valores unicos de ciudad
SELECT DISTINCT ciudad FROM estudiantes;

-- Contar total de estudiantes
SELECT COUNT(*) AS total_estudiantes FROM estudiantes;

-- ------------------------------------------------------------
-- WHERE: Filtrar resultados
-- ------------------------------------------------------------

-- Estudiantes mayores de 22
SELECT nombre, edad FROM estudiantes WHERE edad > 22;

-- Estudiantes de CDMX
SELECT nombre, ciudad FROM estudiantes WHERE ciudad = 'CDMX';

-- Combinando condiciones con AND
SELECT nombre, edad, ciudad
FROM estudiantes
WHERE edad >= 20 AND ciudad = 'CDMX';

-- Combinando condiciones con OR
SELECT nombre, ciudad
FROM estudiantes
WHERE ciudad = 'CDMX' OR ciudad = 'Monterrey';

-- Negacion con NOT
SELECT nombre, ciudad FROM estudiantes WHERE NOT ciudad = 'Puebla';

-- ------------------------------------------------------------
-- BETWEEN: Rangos
-- ------------------------------------------------------------

-- Estudiantes entre 20 y 23 anios
SELECT nombre, edad FROM estudiantes WHERE edad BETWEEN 20 AND 23;

-- Promedio entre 8.0 y 9.5
SELECT nombre, promedio FROM estudiantes WHERE promedio BETWEEN 8.0 AND 9.5;

-- ------------------------------------------------------------
-- IN: Lista de valores
-- ------------------------------------------------------------

-- Ciudades especificas
SELECT nombre, ciudad
FROM estudiantes
WHERE ciudad IN ('CDMX', 'Monterrey');

-- Edades especificas
SELECT nombre, edad FROM estudiantes WHERE edad IN (20, 22, 24);

-- ------------------------------------------------------------
-- LIKE: Busqueda por patrones
-- ------------------------------------------------------------

-- Nombres que empiezan con 'M'
SELECT nombre FROM estudiantes WHERE nombre LIKE 'M%';

-- Nombres que terminan en 'a'
SELECT nombre FROM estudiantes WHERE nombre LIKE '%a';

-- Nombres que contienen 'ar'
SELECT nombre FROM estudiantes WHERE nombre LIKE '%ar%';

-- Segunda letra es 'a'
SELECT nombre FROM estudiantes WHERE nombre LIKE '_a%';

-- ILIKE para busqueda sin importar mayusculas (PostgreSQL)
SELECT nombre FROM estudiantes WHERE nombre ILIKE '%ana%';

-- ------------------------------------------------------------
-- IS NULL / IS NOT NULL
-- ------------------------------------------------------------

-- Estudiantes sin email registrado
SELECT nombre, email FROM estudiantes WHERE email IS NULL;

-- Estudiantes con ciudad registrada
SELECT nombre, ciudad FROM estudiantes WHERE ciudad IS NOT NULL;

-- ------------------------------------------------------------
-- ORDER BY: Ordenar resultados
-- ------------------------------------------------------------

-- Ordenar por nombre alfabeticamente
SELECT nombre, apellido FROM estudiantes ORDER BY nombre ASC;

-- Ordenar por edad descendente
SELECT nombre, edad FROM estudiantes ORDER BY edad DESC;

-- Orden multiple: primero por ciudad, luego por promedio
SELECT nombre, ciudad, promedio
FROM estudiantes
ORDER BY ciudad ASC, promedio DESC;

-- ------------------------------------------------------------
-- LIMIT y OFFSET: Paginacion
-- ------------------------------------------------------------

-- Los 5 mejores promedios
SELECT nombre, promedio
FROM estudiantes
ORDER BY promedio DESC
LIMIT 5;

-- Pagina 2 (registros 6 al 10)
SELECT nombre, promedio
FROM estudiantes
ORDER BY promedio DESC
LIMIT 5 OFFSET 5;

-- El estudiante mas joven
SELECT nombre, edad
FROM estudiantes
ORDER BY edad ASC
LIMIT 1;

-- ------------------------------------------------------------
-- COMBINANDO TODO: Consultas completas
-- ------------------------------------------------------------

-- Top 3 estudiantes de CDMX con mejor promedio
SELECT nombre, apellido, promedio
FROM estudiantes
WHERE ciudad = 'CDMX' AND activo = true
ORDER BY promedio DESC
LIMIT 3;

-- Estudiantes activos entre 20-25 anios cuyo nombre empieza con vocal
SELECT nombre, edad, ciudad, promedio
FROM estudiantes
WHERE edad BETWEEN 20 AND 25
  AND nombre LIKE 'A%'
  OR nombre LIKE 'E%'
  OR nombre LIKE 'I%'
ORDER BY nombre;

-- ------------------------------------------------------------
-- UPDATE: Modificar datos
-- ------------------------------------------------------------

-- Actualizar la edad de un estudiante
UPDATE estudiantes SET edad = 23 WHERE nombre = 'Ana' AND apellido = 'Garcia';

-- Actualizar multiples columnas
UPDATE estudiantes
SET ciudad = 'CDMX', promedio = 8.5
WHERE id = 6;

-- Incrementar promedio de todos los de Puebla
UPDATE estudiantes SET promedio = promedio + 0.5 WHERE ciudad = 'Puebla';

-- ------------------------------------------------------------
-- DELETE: Eliminar datos
-- ------------------------------------------------------------

-- Eliminar un estudiante especifico
DELETE FROM estudiantes WHERE id = 12;

-- Eliminar estudiantes inactivos
DELETE FROM estudiantes WHERE activo = false;

-- Eliminar estudiantes con promedio menor a 7.0
DELETE FROM estudiantes WHERE promedio < 7.0;

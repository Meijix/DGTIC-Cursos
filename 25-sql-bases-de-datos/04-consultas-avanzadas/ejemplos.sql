-- ============================================================
-- 04 — Consultas Avanzadas: Ejemplos Practicos
-- Base de datos: Sistema de ventas con empleados y productos
-- ============================================================

-- ------------------------------------------------------------
-- CREAR TABLAS
-- ------------------------------------------------------------

CREATE TABLE departamentos (
    id     SERIAL PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL
);

CREATE TABLE empleados (
    id       SERIAL PRIMARY KEY,
    nombre   VARCHAR(100) NOT NULL,
    depto_id INTEGER REFERENCES departamentos(id),
    salario  DECIMAL(10,2),
    fecha_ingreso DATE
);

CREATE TABLE categorias (
    id     SERIAL PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL
);

CREATE TABLE productos (
    id           SERIAL PRIMARY KEY,
    nombre       VARCHAR(100) NOT NULL,
    precio       DECIMAL(10,2),
    categoria_id INTEGER REFERENCES categorias(id),
    stock        INTEGER DEFAULT 0
);

CREATE TABLE ventas (
    id          SERIAL PRIMARY KEY,
    producto_id INTEGER REFERENCES productos(id),
    empleado_id INTEGER REFERENCES empleados(id),
    cantidad    INTEGER NOT NULL CHECK (cantidad > 0),
    fecha       DATE DEFAULT CURRENT_DATE,
    total       DECIMAL(10,2)
);

-- ------------------------------------------------------------
-- DATOS DE EJEMPLO
-- ------------------------------------------------------------

INSERT INTO departamentos (nombre) VALUES
    ('Ventas'), ('Tecnologia'), ('Marketing'), ('RRHH');

INSERT INTO empleados (nombre, depto_id, salario, fecha_ingreso) VALUES
    ('Ana Torres',    1, 35000, '2023-01-15'),
    ('Carlos Diaz',   1, 38000, '2022-06-01'),
    ('Maria Lopez',   2, 52000, '2021-03-20'),
    ('Pedro Sanchez',  2, 48000, '2023-09-10'),
    ('Laura Reyes',   3, 42000, '2022-11-05'),
    ('Miguel Flores', 3, 40000, '2024-02-01'),
    ('Sofia Garcia',  1, 36000, '2024-01-10'),
    ('Diego Moreno',  2, 55000, '2020-07-15'),
    ('Elena Ruiz',    4, 45000, '2022-04-20'),
    ('Andres Castro', NULL, 30000, '2025-01-01');

INSERT INTO categorias (nombre) VALUES
    ('Electronicos'), ('Ropa'), ('Alimentos'), ('Libros');

INSERT INTO productos (nombre, precio, categoria_id, stock) VALUES
    ('Laptop',       15999.00, 1, 25),
    ('Teclado',        899.00, 1, 100),
    ('Monitor',       5499.00, 1, 40),
    ('Camiseta',       349.00, 2, 200),
    ('Pantalon',       599.00, 2, 150),
    ('Cafe 1kg',       189.00, 3, 300),
    ('Galletas',        45.00, 3, 500),
    ('SQL Avanzado',   450.00, 4, 60),
    ('Clean Code',     599.00, 4, 45);

INSERT INTO ventas (producto_id, empleado_id, cantidad, fecha, total) VALUES
    (1, 1, 2, '2026-01-15', 31998.00),
    (2, 1, 5, '2026-01-20', 4495.00),
    (3, 2, 1, '2026-02-10', 5499.00),
    (4, 5, 10, '2026-02-14', 3490.00),
    (6, 1, 20, '2026-02-20', 3780.00),
    (8, 2, 3, '2026-03-01', 1350.00),
    (1, 7, 1, '2026-03-05', 15999.00),
    (5, 5, 8, '2026-03-10', 4792.00),
    (9, 2, 2, '2026-03-15', 1198.00),
    (2, 1, 3, '2026-03-20', 2697.00),
    (7, 7, 50, '2026-03-22', 2250.00),
    (3, 2, 2, '2026-03-25', 10998.00);

-- ============================================================
-- SUBQUERIES
-- ============================================================

-- Subquery escalar: empleados que ganan mas que el promedio
SELECT nombre, salario
FROM empleados
WHERE salario > (SELECT AVG(salario) FROM empleados)
ORDER BY salario DESC;

-- Subquery de lista (IN): productos que se han vendido
SELECT nombre, precio
FROM productos
WHERE id IN (SELECT DISTINCT producto_id FROM ventas);

-- Subquery de lista (NOT IN): productos que nunca se vendieron
SELECT nombre, precio
FROM productos
WHERE id NOT IN (SELECT DISTINCT producto_id FROM ventas);

-- Subquery en FROM: promedio de ventas por categoria
SELECT cat_nombre, ROUND(avg_total, 2) AS promedio_venta
FROM (
    SELECT c.nombre AS cat_nombre, AVG(v.total) AS avg_total
    FROM ventas v
    JOIN productos p ON v.producto_id = p.id
    JOIN categorias c ON p.categoria_id = c.id
    GROUP BY c.nombre
) AS promedios
ORDER BY promedio_venta DESC;

-- Subquery correlacionada: empleados cuyo salario supera
-- el promedio de su departamento
SELECT e.nombre, e.salario, d.nombre AS departamento
FROM empleados e
JOIN departamentos d ON e.depto_id = d.id
WHERE e.salario > (
    SELECT AVG(e2.salario)
    FROM empleados e2
    WHERE e2.depto_id = e.depto_id
)
ORDER BY e.salario DESC;

-- EXISTS: departamentos que tienen al menos un empleado
SELECT d.nombre
FROM departamentos d
WHERE EXISTS (
    SELECT 1 FROM empleados e WHERE e.depto_id = d.id
);

-- NOT EXISTS: departamentos sin empleados
SELECT d.nombre AS departamento_vacio
FROM departamentos d
WHERE NOT EXISTS (
    SELECT 1 FROM empleados e WHERE e.depto_id = d.id
);

-- ============================================================
-- FUNCIONES DE AGREGACION
-- ============================================================

-- Resumen general de ventas
SELECT
    COUNT(*)          AS total_ventas,
    SUM(total)        AS ingreso_total,
    ROUND(AVG(total), 2) AS venta_promedio,
    MIN(total)        AS venta_minima,
    MAX(total)        AS venta_maxima
FROM ventas;

-- Contar empleados por departamento
SELECT d.nombre AS departamento, COUNT(e.id) AS empleados
FROM departamentos d
LEFT JOIN empleados e ON d.id = e.depto_id
GROUP BY d.nombre
ORDER BY empleados DESC;

-- ============================================================
-- GROUP BY + HAVING
-- ============================================================

-- Ventas totales por empleado (solo los que vendieron mas de 10,000)
SELECT
    e.nombre,
    COUNT(v.id) AS num_ventas,
    SUM(v.total) AS total_vendido
FROM empleados e
JOIN ventas v ON e.id = v.empleado_id
GROUP BY e.nombre
HAVING SUM(v.total) > 10000
ORDER BY total_vendido DESC;

-- Categorias con mas de 2 productos
SELECT c.nombre, COUNT(*) AS total_productos
FROM categorias c
JOIN productos p ON c.id = p.categoria_id
GROUP BY c.nombre
HAVING COUNT(*) > 2;

-- Mes con mayor ingreso
SELECT
    DATE_TRUNC('month', fecha) AS mes,
    SUM(total) AS ingreso_mensual,
    COUNT(*) AS num_ventas
FROM ventas
GROUP BY DATE_TRUNC('month', fecha)
ORDER BY ingreso_mensual DESC
LIMIT 1;

-- ============================================================
-- CASE / WHEN
-- ============================================================

-- Clasificar empleados por rango salarial
SELECT nombre, salario,
    CASE
        WHEN salario >= 50000 THEN 'Senior'
        WHEN salario >= 40000 THEN 'Mid'
        WHEN salario >= 35000 THEN 'Junior'
        ELSE 'Trainee'
    END AS nivel
FROM empleados
ORDER BY salario DESC;

-- Contar productos por rango de precio
SELECT
    CASE
        WHEN precio >= 5000 THEN 'Premium'
        WHEN precio >= 500  THEN 'Medio'
        ELSE 'Economico'
    END AS rango,
    COUNT(*) AS cantidad
FROM productos
GROUP BY rango
ORDER BY cantidad DESC;

-- ============================================================
-- COALESCE
-- ============================================================

-- Empleados con departamento (manejar NULL)
SELECT
    nombre,
    COALESCE(d.nombre, 'Sin departamento') AS departamento
FROM empleados e
LEFT JOIN departamentos d ON e.depto_id = d.id;

-- ============================================================
-- WINDOW FUNCTIONS
-- ============================================================

-- ROW_NUMBER: ranking de empleados por salario
SELECT
    nombre,
    salario,
    ROW_NUMBER() OVER (ORDER BY salario DESC) AS posicion
FROM empleados;

-- RANK vs DENSE_RANK
SELECT
    nombre, salario,
    RANK()       OVER (ORDER BY salario DESC) AS rank,
    DENSE_RANK() OVER (ORDER BY salario DESC) AS dense_rank
FROM empleados;

-- PARTITION BY: ranking de salario dentro de cada departamento
SELECT
    e.nombre,
    d.nombre AS departamento,
    e.salario,
    RANK() OVER (PARTITION BY e.depto_id ORDER BY e.salario DESC) AS rank_depto
FROM empleados e
JOIN departamentos d ON e.depto_id = d.id;

-- Top 2 empleados mejor pagados por departamento
SELECT * FROM (
    SELECT
        e.nombre,
        d.nombre AS departamento,
        e.salario,
        ROW_NUMBER() OVER (PARTITION BY e.depto_id ORDER BY e.salario DESC) AS rn
    FROM empleados e
    JOIN departamentos d ON e.depto_id = d.id
) sub
WHERE rn <= 2;

-- LAG / LEAD: comparar venta con la anterior
SELECT
    fecha,
    total,
    LAG(total, 1)  OVER (ORDER BY fecha) AS venta_anterior,
    total - LAG(total, 1) OVER (ORDER BY fecha) AS diferencia
FROM ventas
ORDER BY fecha;

-- Suma acumulada de ventas por fecha
SELECT
    fecha,
    total,
    SUM(total) OVER (ORDER BY fecha) AS acumulado
FROM ventas
ORDER BY fecha;

-- Porcentaje de cada venta sobre el total
SELECT
    fecha,
    e.nombre AS vendedor,
    total,
    ROUND(total * 100.0 / SUM(total) OVER (), 2) AS pct_total
FROM ventas v
JOIN empleados e ON v.empleado_id = e.id
ORDER BY total DESC;

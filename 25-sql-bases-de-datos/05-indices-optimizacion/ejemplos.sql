-- ============================================================
-- 05 — Indices y Optimizacion: Ejemplos Practicos
-- Demostracion de indices, EXPLAIN y optimizacion
-- ============================================================

-- ------------------------------------------------------------
-- CREAR TABLA DE EJEMPLO (gran volumen simulado)
-- ------------------------------------------------------------

CREATE TABLE pedidos (
    id              SERIAL PRIMARY KEY,
    cliente_nombre  VARCHAR(100) NOT NULL,
    email           VARCHAR(100),
    producto        VARCHAR(100) NOT NULL,
    cantidad        INTEGER NOT NULL CHECK (cantidad > 0),
    precio_unitario DECIMAL(10,2) NOT NULL,
    total           DECIMAL(12,2),
    estado          VARCHAR(20) DEFAULT 'pendiente'
                    CHECK (estado IN ('pendiente', 'procesando', 'enviado', 'entregado', 'cancelado')),
    ciudad          VARCHAR(50),
    fecha           DATE DEFAULT CURRENT_DATE,
    created_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insertar datos de ejemplo
INSERT INTO pedidos (cliente_nombre, email, producto, cantidad, precio_unitario, total, estado, ciudad, fecha)
SELECT
    'Cliente_' || i,
    'cliente' || i || '@mail.com',
    CASE (i % 5)
        WHEN 0 THEN 'Laptop'
        WHEN 1 THEN 'Teclado'
        WHEN 2 THEN 'Monitor'
        WHEN 3 THEN 'Mouse'
        WHEN 4 THEN 'Audifonos'
    END,
    (i % 10) + 1,
    CASE (i % 5)
        WHEN 0 THEN 15999.00
        WHEN 1 THEN 899.00
        WHEN 2 THEN 5499.00
        WHEN 3 THEN 349.00
        WHEN 4 THEN 1299.00
    END,
    ((i % 10) + 1) * CASE (i % 5)
        WHEN 0 THEN 15999.00
        WHEN 1 THEN 899.00
        WHEN 2 THEN 5499.00
        WHEN 3 THEN 349.00
        WHEN 4 THEN 1299.00
    END,
    CASE (i % 4)
        WHEN 0 THEN 'pendiente'
        WHEN 1 THEN 'procesando'
        WHEN 2 THEN 'enviado'
        WHEN 3 THEN 'entregado'
    END,
    CASE (i % 6)
        WHEN 0 THEN 'CDMX'
        WHEN 1 THEN 'Monterrey'
        WHEN 2 THEN 'Guadalajara'
        WHEN 3 THEN 'Puebla'
        WHEN 4 THEN 'Merida'
        WHEN 5 THEN 'Queretaro'
    END,
    CURRENT_DATE - ((i % 365) || ' days')::INTERVAL
FROM generate_series(1, 10000) AS s(i);

-- ============================================================
-- EXPLAIN: ANTES DE CREAR INDICES
-- ============================================================

-- Sin indice: Seq Scan (recorre toda la tabla)
EXPLAIN ANALYZE
SELECT * FROM pedidos WHERE email = 'cliente500@mail.com';
-- Resultado esperado: Seq Scan on pedidos
-- Tiempo: alto (recorre 10,000 filas)

EXPLAIN ANALYZE
SELECT * FROM pedidos WHERE ciudad = 'CDMX' AND estado = 'pendiente';
-- Seq Scan: sin indices, recorre todo

-- ============================================================
-- CREAR INDICES
-- ============================================================

-- Indice simple en email (busquedas frecuentes por email)
CREATE INDEX idx_pedidos_email ON pedidos(email);

-- Indice compuesto: ciudad + estado (para filtros combinados)
CREATE INDEX idx_pedidos_ciudad_estado ON pedidos(ciudad, estado);

-- Indice en fecha (para consultas por rango de fechas)
CREATE INDEX idx_pedidos_fecha ON pedidos(fecha);

-- Indice unico en email (si queremos prevenir duplicados)
-- CREATE UNIQUE INDEX idx_pedidos_email_unique ON pedidos(email);

-- Indice parcial: solo pedidos pendientes (los mas consultados)
CREATE INDEX idx_pedidos_pendientes ON pedidos(fecha)
WHERE estado = 'pendiente';

-- ============================================================
-- EXPLAIN: DESPUES DE CREAR INDICES
-- ============================================================

-- Con indice: Index Scan (busqueda directa)
EXPLAIN ANALYZE
SELECT * FROM pedidos WHERE email = 'cliente500@mail.com';
-- Resultado esperado: Index Scan using idx_pedidos_email
-- Tiempo: mucho menor

-- Indice compuesto en accion
EXPLAIN ANALYZE
SELECT * FROM pedidos WHERE ciudad = 'CDMX' AND estado = 'pendiente';
-- Resultado: Index Scan using idx_pedidos_ciudad_estado

-- Indice parcial: consultas sobre pedidos pendientes
EXPLAIN ANALYZE
SELECT * FROM pedidos WHERE estado = 'pendiente' AND fecha > '2026-01-01';
-- Usa idx_pedidos_pendientes (indice mas pequenio y rapido)

-- ============================================================
-- REGLAS DEL INDICE COMPUESTO
-- ============================================================

-- FUNCIONA: usa el prefijo del indice (ciudad)
EXPLAIN ANALYZE
SELECT * FROM pedidos WHERE ciudad = 'Monterrey';
-- Usa idx_pedidos_ciudad_estado

-- NO FUNCIONA: estado sin ciudad (no es prefijo)
EXPLAIN ANALYZE
SELECT * FROM pedidos WHERE estado = 'enviado';
-- Seq Scan (el indice no ayuda si falta el prefijo)

-- FUNCIONA: ambas columnas del indice
EXPLAIN ANALYZE
SELECT * FROM pedidos
WHERE ciudad = 'Guadalajara' AND estado = 'entregado';

-- ============================================================
-- OPTIMIZACION DE CONSULTAS
-- ============================================================

-- MAL: SELECT * cuando solo necesitas algunas columnas
EXPLAIN ANALYZE
SELECT * FROM pedidos WHERE ciudad = 'CDMX';

-- BIEN: solo las columnas necesarias
EXPLAIN ANALYZE
SELECT id, cliente_nombre, total FROM pedidos WHERE ciudad = 'CDMX';

-- MAL: funcion en columna indexada (anula el indice)
EXPLAIN ANALYZE
SELECT * FROM pedidos WHERE UPPER(email) = 'CLIENTE100@MAIL.COM';
-- Seq Scan: la funcion impide usar el indice

-- BIEN: comparar directamente
EXPLAIN ANALYZE
SELECT * FROM pedidos WHERE email = 'cliente100@mail.com';
-- Index Scan: usa el indice

-- MAL: LIKE con comodin al inicio
EXPLAIN ANALYZE
SELECT * FROM pedidos WHERE producto LIKE '%top';
-- Seq Scan

-- BIEN: LIKE con comodin al final (usa indice B-tree)
CREATE INDEX idx_pedidos_producto ON pedidos(producto);
EXPLAIN ANALYZE
SELECT * FROM pedidos WHERE producto LIKE 'Lap%';
-- Index Scan

-- ============================================================
-- OPTIMIZACION CON RANGOS DE FECHA
-- ============================================================

-- MAL: funcion en columna de fecha
EXPLAIN ANALYZE
SELECT COUNT(*) FROM pedidos
WHERE EXTRACT(YEAR FROM fecha) = 2026;
-- Seq Scan

-- BIEN: rango de fechas directo
EXPLAIN ANALYZE
SELECT COUNT(*) FROM pedidos
WHERE fecha >= '2026-01-01' AND fecha < '2027-01-01';
-- Index Scan usando idx_pedidos_fecha

-- ============================================================
-- EXISTS vs IN
-- ============================================================

-- Crear tabla auxiliar para demostrar
CREATE TABLE clientes_vip (
    email VARCHAR(100) PRIMARY KEY
);

INSERT INTO clientes_vip (email)
SELECT DISTINCT email FROM pedidos WHERE total > 50000;

-- Con IN (puede ser lento con subqueries grandes)
EXPLAIN ANALYZE
SELECT * FROM pedidos
WHERE email IN (SELECT email FROM clientes_vip);

-- Con EXISTS (generalmente mas eficiente)
EXPLAIN ANALYZE
SELECT * FROM pedidos p
WHERE EXISTS (
    SELECT 1 FROM clientes_vip v WHERE v.email = p.email
);

-- ============================================================
-- VER INDICES EXISTENTES (PostgreSQL)
-- ============================================================

-- Listar todos los indices de una tabla
SELECT
    indexname   AS nombre_indice,
    indexdef    AS definicion
FROM pg_indexes
WHERE tablename = 'pedidos'
ORDER BY indexname;

-- Tamanio de los indices
SELECT
    indexrelname AS indice,
    pg_size_pretty(pg_relation_size(indexrelid)) AS tamanio
FROM pg_stat_user_indexes
WHERE relname = 'pedidos'
ORDER BY pg_relation_size(indexrelid) DESC;

-- ============================================================
-- MANTENIMIENTO: Actualizar estadisticas
-- ============================================================

-- PostgreSQL: actualizar estadisticas para el optimizador
ANALYZE pedidos;

-- Ver estadisticas de uso de indices
SELECT
    indexrelname AS indice,
    idx_scan     AS veces_usado,
    idx_tup_read AS filas_leidas
FROM pg_stat_user_indexes
WHERE relname = 'pedidos'
ORDER BY idx_scan DESC;

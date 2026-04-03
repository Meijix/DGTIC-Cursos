-- ============================================================
-- 07 — Proyecto Final: Sistema E-Commerce Completo
-- Base de datos PostgreSQL
-- ============================================================

-- ============================================================
-- PARTE 1: CREACION DEL ESQUEMA
-- ============================================================

-- Tabla de categorias
CREATE TABLE categorias (
    id          SERIAL PRIMARY KEY,
    nombre      VARCHAR(50) NOT NULL UNIQUE,
    descripcion TEXT,
    created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabla de productos
CREATE TABLE productos (
    id              SERIAL PRIMARY KEY,
    nombre          VARCHAR(150) NOT NULL,
    descripcion     TEXT,
    precio          DECIMAL(10,2) NOT NULL CHECK (precio > 0),
    stock           INTEGER NOT NULL DEFAULT 0 CHECK (stock >= 0),
    imagen_url      VARCHAR(255),
    categoria_id    INTEGER REFERENCES categorias(id) ON DELETE SET NULL,
    is_activo       BOOLEAN DEFAULT true,
    created_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabla de usuarios
CREATE TABLE usuarios (
    id          SERIAL PRIMARY KEY,
    nombre      VARCHAR(100) NOT NULL,
    email       VARCHAR(100) UNIQUE NOT NULL,
    password    VARCHAR(255) NOT NULL,
    telefono    VARCHAR(15),
    direccion   TEXT,
    ciudad      VARCHAR(50),
    is_activo   BOOLEAN DEFAULT true,
    created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabla de ordenes
CREATE TABLE ordenes (
    id              SERIAL PRIMARY KEY,
    usuario_id      INTEGER NOT NULL REFERENCES usuarios(id) ON DELETE RESTRICT,
    estado          VARCHAR(20) DEFAULT 'pendiente'
                    CHECK (estado IN ('pendiente', 'pagada', 'enviada', 'entregada', 'cancelada')),
    total           DECIMAL(12,2) NOT NULL DEFAULT 0.00 CHECK (total >= 0),
    direccion_envio TEXT NOT NULL,
    notas           TEXT,
    fecha_orden     TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    fecha_envio     TIMESTAMP,
    fecha_entrega   TIMESTAMP,
    created_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabla de detalles de orden
CREATE TABLE orden_detalles (
    id              SERIAL PRIMARY KEY,
    orden_id        INTEGER NOT NULL REFERENCES ordenes(id) ON DELETE CASCADE,
    producto_id     INTEGER NOT NULL REFERENCES productos(id) ON DELETE RESTRICT,
    cantidad        INTEGER NOT NULL CHECK (cantidad > 0),
    precio_unitario DECIMAL(10,2) NOT NULL CHECK (precio_unitario > 0),
    subtotal        DECIMAL(12,2) NOT NULL,
    created_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabla de resenas
CREATE TABLE resenas (
    id          SERIAL PRIMARY KEY,
    producto_id INTEGER NOT NULL REFERENCES productos(id) ON DELETE CASCADE,
    usuario_id  INTEGER NOT NULL REFERENCES usuarios(id) ON DELETE CASCADE,
    rating      INTEGER NOT NULL CHECK (rating BETWEEN 1 AND 5),
    titulo      VARCHAR(100),
    comentario  TEXT,
    fecha       TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (producto_id, usuario_id)  -- un usuario, una resena por producto
);

-- ============================================================
-- PARTE 2: INDICES PARA OPTIMIZACION
-- ============================================================

CREATE INDEX idx_productos_categoria ON productos(categoria_id);
CREATE INDEX idx_productos_precio ON productos(precio);
CREATE INDEX idx_productos_activos ON productos(is_activo) WHERE is_activo = true;

CREATE INDEX idx_ordenes_usuario ON ordenes(usuario_id);
CREATE INDEX idx_ordenes_estado ON ordenes(estado);
CREATE INDEX idx_ordenes_fecha ON ordenes(fecha_orden);

CREATE INDEX idx_detalles_orden ON orden_detalles(orden_id);
CREATE INDEX idx_detalles_producto ON orden_detalles(producto_id);

CREATE INDEX idx_resenas_producto ON resenas(producto_id);
CREATE INDEX idx_resenas_usuario ON resenas(usuario_id);

-- ============================================================
-- PARTE 3: DATOS DE EJEMPLO
-- ============================================================

INSERT INTO categorias (nombre, descripcion) VALUES
    ('Electronicos',  'Dispositivos y gadgets electronicos'),
    ('Ropa',          'Prendas de vestir para hombre y mujer'),
    ('Hogar',         'Articulos para el hogar y cocina'),
    ('Libros',        'Libros fisicos y digitales'),
    ('Deportes',      'Equipamiento deportivo y fitness');

INSERT INTO productos (nombre, descripcion, precio, stock, categoria_id) VALUES
    ('Laptop Pro 15',      'Laptop 15 pulgadas, 16GB RAM, 512GB SSD',    18999.00, 50, 1),
    ('Audifonos Bluetooth', 'Cancelacion de ruido activa',                 2499.00, 200, 1),
    ('Teclado Mecanico',   'Switches Cherry MX, retroiluminado',          1899.00, 150, 1),
    ('Camisa Casual',      'Algodon 100%, varios colores',                 599.00, 300, 2),
    ('Jeans Slim',         'Mezclilla premium, corte slim',                899.00, 250, 2),
    ('Sudadera Hoodie',    'Felpa interior, capucha ajustable',            749.00, 180, 2),
    ('Cafetera Italiana',  'Acero inoxidable, 6 tazas',                    689.00, 100, 3),
    ('Juego de Cuchillos',  'Set 5 piezas, acero alemán',                 1299.00, 80, 3),
    ('Lampara LED Escritorio', 'Regulable, 3 tonos de luz',                459.00, 120, 3),
    ('Clean Code',         'Robert C. Martin - Codigo limpio',              599.00, 60, 4),
    ('SQL Avanzado',       'Guia completa de bases de datos',               450.00, 45, 4),
    ('Mancuernas 10kg',    'Par de mancuernas hexagonales',                 899.00, 75, 5),
    ('Banda Elastica Set', 'Set 5 niveles de resistencia',                  349.00, 200, 5);

INSERT INTO usuarios (nombre, email, password, telefono, direccion, ciudad) VALUES
    ('Ana Garcia',     'ana@tienda.com',    'hash_seguro_1', '555-0101', 'Av. Reforma 100',   'CDMX'),
    ('Carlos Lopez',   'carlos@tienda.com', 'hash_seguro_2', '555-0102', 'Calle 5 de Mayo 20', 'Monterrey'),
    ('Maria Torres',   'maria@tienda.com',  'hash_seguro_3', '555-0103', 'Blvd. Insurgentes 50', 'CDMX'),
    ('Pedro Ramirez',  'pedro@tienda.com',  'hash_seguro_4', '555-0104', 'Av. Juarez 300',    'Guadalajara'),
    ('Laura Moreno',   'laura@tienda.com',  'hash_seguro_5', '555-0105', 'Calle Hidalgo 15',  'Puebla');

-- Ordenes de ejemplo
INSERT INTO ordenes (usuario_id, estado, total, direccion_envio, fecha_orden) VALUES
    (1, 'entregada', 21498.00, 'Av. Reforma 100, CDMX',       '2026-01-15'),
    (2, 'entregada', 1498.00,  'Calle 5 de Mayo 20, Monterrey', '2026-02-01'),
    (1, 'enviada',   2248.00,  'Av. Reforma 100, CDMX',       '2026-03-10'),
    (3, 'pagada',    3148.00,  'Blvd. Insurgentes 50, CDMX',  '2026-03-20'),
    (4, 'pendiente', 899.00,   'Av. Juarez 300, Guadalajara',  '2026-03-28'),
    (2, 'entregada', 689.00,   'Calle 5 de Mayo 20, Monterrey', '2026-02-15'),
    (5, 'cancelada', 18999.00, 'Calle Hidalgo 15, Puebla',    '2026-03-01');

-- Detalles de ordenes
INSERT INTO orden_detalles (orden_id, producto_id, cantidad, precio_unitario, subtotal) VALUES
    (1, 1, 1, 18999.00, 18999.00),   -- Orden 1: Laptop
    (1, 2, 1, 2499.00,  2499.00),    -- Orden 1: Audifonos
    (2, 4, 2, 599.00,   1198.00),    -- Orden 2: 2 Camisas
    (2, 13, 1, 349.00,  349.00),     -- Orden 2: Banda elastica (ajustado a 1498 total aprox)
    (3, 3, 1, 1899.00,  1899.00),    -- Orden 3: Teclado
    (3, 13, 1, 349.00,  349.00),     -- Orden 3: Banda elastica
    (4, 5, 2, 899.00,   1798.00),    -- Orden 4: 2 Jeans
    (4, 7, 1, 689.00,   689.00),     -- Orden 4: Cafetera
    (4, 9, 1, 459.00,   459.00),     -- Orden 4: Lampara (ajustado)
    (5, 5, 1, 899.00,   899.00),     -- Orden 5: Jeans
    (6, 7, 1, 689.00,   689.00),     -- Orden 6: Cafetera
    (7, 1, 1, 18999.00, 18999.00);   -- Orden 7: Laptop (cancelada)

-- Resenas
INSERT INTO resenas (producto_id, usuario_id, rating, titulo, comentario) VALUES
    (1, 1, 5, 'Excelente laptop',      'Rapida y con buena pantalla. La recomiendo.'),
    (2, 1, 4, 'Buenos audifonos',       'Buena cancelacion de ruido, comodos.'),
    (1, 2, 4, 'Muy buena',             'Perfecta para programar, algo pesada.'),
    (4, 2, 5, 'Calidad premium',       'Tela suave y buen corte.'),
    (7, 2, 5, 'Cafe delicioso',         'Hace un espresso perfecto.'),
    (3, 3, 5, 'Teclado increible',     'Los switches son muy satisfactorios.'),
    (5, 4, 4, 'Buen jean',             'Buen fit, talla correcta.'),
    (12, 4, 3, 'Regulares',            'El recubrimiento se desgasta rapido.'),
    (10, 3, 5, 'Libro imprescindible', 'Todo developer deberia leerlo.'),
    (11, 1, 5, 'Muy completo',         'Excelente para aprender SQL desde cero.');

-- ============================================================
-- PARTE 4: CONSULTAS COMPLEJAS
-- ============================================================

-- Productos con su categoria, precio y rating promedio
SELECT
    p.nombre AS producto,
    c.nombre AS categoria,
    p.precio,
    p.stock,
    COALESCE(ROUND(AVG(r.rating), 1), 0) AS rating_promedio,
    COUNT(r.id) AS total_resenas
FROM productos p
LEFT JOIN categorias c ON p.categoria_id = c.id
LEFT JOIN resenas r ON p.id = r.producto_id
WHERE p.is_activo = true
GROUP BY p.id, p.nombre, c.nombre, p.precio, p.stock
ORDER BY rating_promedio DESC;

-- Top 5 productos mas vendidos
SELECT
    p.nombre,
    SUM(od.cantidad) AS unidades_vendidas,
    SUM(od.subtotal) AS ingresos
FROM orden_detalles od
JOIN productos p ON od.producto_id = p.id
JOIN ordenes o ON od.orden_id = o.id
WHERE o.estado != 'cancelada'
GROUP BY p.id, p.nombre
ORDER BY unidades_vendidas DESC
LIMIT 5;

-- Ventas por categoria
SELECT
    c.nombre AS categoria,
    COUNT(DISTINCT o.id) AS total_ordenes,
    SUM(od.cantidad) AS unidades,
    SUM(od.subtotal) AS ingresos
FROM categorias c
JOIN productos p ON c.id = p.categoria_id
JOIN orden_detalles od ON p.id = od.producto_id
JOIN ordenes o ON od.orden_id = o.id
WHERE o.estado != 'cancelada'
GROUP BY c.nombre
ORDER BY ingresos DESC;

-- Historial completo de compras de un usuario
SELECT
    o.id AS orden,
    o.estado,
    o.fecha_orden,
    p.nombre AS producto,
    od.cantidad,
    od.precio_unitario,
    od.subtotal
FROM ordenes o
JOIN orden_detalles od ON o.id = od.orden_id
JOIN productos p ON od.producto_id = p.id
WHERE o.usuario_id = 1
ORDER BY o.fecha_orden DESC, p.nombre;

-- Usuarios con mayor gasto total
SELECT
    u.nombre,
    u.email,
    COUNT(DISTINCT o.id) AS total_ordenes,
    SUM(o.total) AS gasto_total,
    ROUND(AVG(o.total), 2) AS ticket_promedio
FROM usuarios u
JOIN ordenes o ON u.id = o.usuario_id
WHERE o.estado NOT IN ('cancelada', 'pendiente')
GROUP BY u.id, u.nombre, u.email
ORDER BY gasto_total DESC;

-- Productos que nunca se han vendido
SELECT p.nombre, p.precio, p.stock
FROM productos p
WHERE NOT EXISTS (
    SELECT 1 FROM orden_detalles od
    JOIN ordenes o ON od.orden_id = o.id
    WHERE od.producto_id = p.id AND o.estado != 'cancelada'
);

-- Ventas mensuales
SELECT
    TO_CHAR(o.fecha_orden, 'YYYY-MM') AS mes,
    COUNT(DISTINCT o.id) AS ordenes,
    SUM(o.total) AS ingresos,
    ROUND(AVG(o.total), 2) AS ticket_promedio
FROM ordenes o
WHERE o.estado NOT IN ('cancelada')
GROUP BY TO_CHAR(o.fecha_orden, 'YYYY-MM')
ORDER BY mes;

-- Productos con stock bajo y alta demanda
SELECT
    p.nombre,
    p.stock AS stock_actual,
    COALESCE(SUM(od.cantidad), 0) AS total_vendido
FROM productos p
LEFT JOIN orden_detalles od ON p.id = od.producto_id
LEFT JOIN ordenes o ON od.orden_id = o.id AND o.estado != 'cancelada'
WHERE p.is_activo = true
GROUP BY p.id, p.nombre, p.stock
HAVING p.stock < 100
ORDER BY total_vendido DESC;

-- Ranking de productos por ingresos (Window Function)
SELECT
    p.nombre,
    c.nombre AS categoria,
    SUM(od.subtotal) AS ingresos,
    RANK() OVER (ORDER BY SUM(od.subtotal) DESC) AS rank_general,
    RANK() OVER (PARTITION BY c.nombre ORDER BY SUM(od.subtotal) DESC) AS rank_categoria
FROM productos p
JOIN categorias c ON p.categoria_id = c.id
JOIN orden_detalles od ON p.id = od.producto_id
JOIN ordenes o ON od.orden_id = o.id
WHERE o.estado != 'cancelada'
GROUP BY p.id, p.nombre, c.nombre;

-- ============================================================
-- PARTE 5: VISTAS
-- ============================================================

-- Vista: Catalogo de productos con rating
CREATE VIEW v_catalogo AS
SELECT
    p.id,
    p.nombre,
    p.descripcion,
    p.precio,
    p.stock,
    c.nombre AS categoria,
    COALESCE(ROUND(AVG(r.rating), 1), 0) AS rating,
    COUNT(r.id) AS num_resenas
FROM productos p
LEFT JOIN categorias c ON p.categoria_id = c.id
LEFT JOIN resenas r ON p.id = r.producto_id
WHERE p.is_activo = true
GROUP BY p.id, p.nombre, p.descripcion, p.precio, p.stock, c.nombre;

-- Vista: Resumen de ventas por mes
CREATE VIEW v_ventas_mensuales AS
SELECT
    TO_CHAR(o.fecha_orden, 'YYYY-MM') AS mes,
    COUNT(DISTINCT o.id) AS total_ordenes,
    COUNT(DISTINCT o.usuario_id) AS clientes_unicos,
    SUM(o.total) AS ingresos_totales,
    ROUND(AVG(o.total), 2) AS ticket_promedio
FROM ordenes o
WHERE o.estado NOT IN ('cancelada')
GROUP BY TO_CHAR(o.fecha_orden, 'YYYY-MM');

-- Vista: Top clientes
CREATE VIEW v_top_clientes AS
SELECT
    u.id,
    u.nombre,
    u.email,
    u.ciudad,
    COUNT(DISTINCT o.id) AS ordenes,
    SUM(o.total) AS gasto_total
FROM usuarios u
JOIN ordenes o ON u.id = o.usuario_id
WHERE o.estado NOT IN ('cancelada')
GROUP BY u.id, u.nombre, u.email, u.ciudad;

-- Usar las vistas
SELECT * FROM v_catalogo ORDER BY rating DESC;
SELECT * FROM v_ventas_mensuales ORDER BY mes;
SELECT * FROM v_top_clientes ORDER BY gasto_total DESC;

-- ============================================================
-- PARTE 6: PROCEDIMIENTOS ALMACENADOS
-- ============================================================

-- Procedimiento: Crear una nueva orden
CREATE OR REPLACE FUNCTION crear_orden(
    p_usuario_id INTEGER,
    p_direccion TEXT
) RETURNS INTEGER AS $$
DECLARE
    v_orden_id INTEGER;
BEGIN
    INSERT INTO ordenes (usuario_id, estado, total, direccion_envio)
    VALUES (p_usuario_id, 'pendiente', 0.00, p_direccion)
    RETURNING id INTO v_orden_id;

    RETURN v_orden_id;
END;
$$ LANGUAGE plpgsql;

-- Procedimiento: Agregar item a una orden
CREATE OR REPLACE FUNCTION agregar_item_orden(
    p_orden_id INTEGER,
    p_producto_id INTEGER,
    p_cantidad INTEGER
) RETURNS VOID AS $$
DECLARE
    v_precio DECIMAL(10,2);
    v_stock INTEGER;
BEGIN
    -- Obtener precio y verificar stock
    SELECT precio, stock INTO v_precio, v_stock
    FROM productos WHERE id = p_producto_id FOR UPDATE;

    IF v_stock < p_cantidad THEN
        RAISE EXCEPTION 'Stock insuficiente. Disponible: %, Solicitado: %', v_stock, p_cantidad;
    END IF;

    -- Insertar detalle
    INSERT INTO orden_detalles (orden_id, producto_id, cantidad, precio_unitario, subtotal)
    VALUES (p_orden_id, p_producto_id, p_cantidad, v_precio, v_precio * p_cantidad);

    -- Descontar stock
    UPDATE productos SET stock = stock - p_cantidad WHERE id = p_producto_id;

    -- Actualizar total de la orden
    UPDATE ordenes SET total = (
        SELECT SUM(subtotal) FROM orden_detalles WHERE orden_id = p_orden_id
    ) WHERE id = p_orden_id;
END;
$$ LANGUAGE plpgsql;

-- Procedimiento: Actualizar estado de orden
CREATE OR REPLACE FUNCTION actualizar_estado_orden(
    p_orden_id INTEGER,
    p_nuevo_estado VARCHAR(20)
) RETURNS VOID AS $$
BEGIN
    UPDATE ordenes
    SET estado = p_nuevo_estado,
        fecha_envio = CASE WHEN p_nuevo_estado = 'enviada' THEN CURRENT_TIMESTAMP ELSE fecha_envio END,
        fecha_entrega = CASE WHEN p_nuevo_estado = 'entregada' THEN CURRENT_TIMESTAMP ELSE fecha_entrega END
    WHERE id = p_orden_id;
END;
$$ LANGUAGE plpgsql;

-- ============================================================
-- PARTE 7: USAR LOS PROCEDIMIENTOS
-- ============================================================

-- Crear una nueva orden para el usuario 5
BEGIN;
    -- Crear la orden
    SELECT crear_orden(5, 'Calle Hidalgo 15, Puebla');
    -- Suponiendo que retorna orden_id = 8

    -- Agregar items (usar el id retornado)
    -- SELECT agregar_item_orden(8, 10, 2);   -- 2 libros Clean Code
    -- SELECT agregar_item_orden(8, 11, 1);   -- 1 libro SQL Avanzado
COMMIT;

-- Actualizar estado
-- SELECT actualizar_estado_orden(4, 'enviada');

-- ============================================================
-- PARTE 8: METRICAS DEL NEGOCIO
-- ============================================================

-- Dashboard resumido
SELECT
    (SELECT COUNT(*) FROM usuarios WHERE is_activo = true) AS usuarios_activos,
    (SELECT COUNT(*) FROM productos WHERE is_activo = true) AS productos_activos,
    (SELECT COUNT(*) FROM ordenes WHERE estado != 'cancelada') AS ordenes_validas,
    (SELECT SUM(total) FROM ordenes WHERE estado NOT IN ('cancelada', 'pendiente')) AS ingresos_totales,
    (SELECT ROUND(AVG(total), 2) FROM ordenes WHERE estado = 'entregada') AS ticket_promedio;

-- Tasa de cancelacion
SELECT
    COUNT(*) FILTER (WHERE estado = 'cancelada') AS canceladas,
    COUNT(*) AS total,
    ROUND(
        COUNT(*) FILTER (WHERE estado = 'cancelada') * 100.0 / COUNT(*), 1
    ) AS tasa_cancelacion_pct
FROM ordenes;

-- Distribucion de ratings
SELECT
    rating,
    COUNT(*) AS cantidad,
    ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (), 1) AS porcentaje
FROM resenas
GROUP BY rating
ORDER BY rating DESC;

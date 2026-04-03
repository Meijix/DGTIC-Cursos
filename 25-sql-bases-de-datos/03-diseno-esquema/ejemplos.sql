-- ============================================================
-- 03 — Diseno de Esquema: Ejemplos Practicos
-- Proyecto: Sistema de gestion de biblioteca
-- ============================================================

-- ------------------------------------------------------------
-- CREAR ESQUEMA: Sistema de Biblioteca Normalizado
-- ------------------------------------------------------------

-- Tabla de generos literarios
CREATE TABLE generos (
    id          SERIAL PRIMARY KEY,
    nombre      VARCHAR(50) NOT NULL UNIQUE,
    descripcion TEXT
);

-- Tabla de autores
CREATE TABLE autores (
    id              SERIAL PRIMARY KEY,
    nombre          VARCHAR(100) NOT NULL,
    nacionalidad    VARCHAR(50),
    fecha_nacimiento DATE,
    biografia       TEXT,
    created_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabla de libros (FK a autores y generos)
CREATE TABLE libros (
    id          SERIAL PRIMARY KEY,
    titulo      VARCHAR(200) NOT NULL,
    isbn        VARCHAR(13) UNIQUE NOT NULL,
    anio_pub    INTEGER CHECK (anio_pub >= 1450 AND anio_pub <= 2030),
    precio      DECIMAL(8,2) CHECK (precio >= 0),
    paginas     INTEGER CHECK (paginas > 0),
    ejemplares  INTEGER DEFAULT 1 CHECK (ejemplares >= 0),
    autor_id    INTEGER NOT NULL REFERENCES autores(id) ON DELETE RESTRICT,
    genero_id   INTEGER REFERENCES generos(id) ON DELETE SET NULL,
    created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabla de socios de la biblioteca
CREATE TABLE socios (
    id          SERIAL PRIMARY KEY,
    nombre      VARCHAR(100) NOT NULL,
    email       VARCHAR(100) UNIQUE NOT NULL,
    telefono    VARCHAR(15),
    direccion   TEXT,
    is_activo   BOOLEAN DEFAULT true,
    fecha_alta  DATE DEFAULT CURRENT_DATE,
    created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabla de prestamos (relaciona socios y libros)
CREATE TABLE prestamos (
    id              SERIAL PRIMARY KEY,
    libro_id        INTEGER NOT NULL REFERENCES libros(id) ON DELETE RESTRICT,
    socio_id        INTEGER NOT NULL REFERENCES socios(id) ON DELETE RESTRICT,
    fecha_prestamo  DATE NOT NULL DEFAULT CURRENT_DATE,
    fecha_devolucion DATE,
    fecha_limite    DATE NOT NULL,
    estado          VARCHAR(20) DEFAULT 'activo'
                    CHECK (estado IN ('activo', 'devuelto', 'vencido')),
    notas           TEXT,
    created_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabla de categorias de libro (N:M con tabla intermedia)
CREATE TABLE etiquetas (
    id     SERIAL PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE libro_etiquetas (
    libro_id    INTEGER REFERENCES libros(id) ON DELETE CASCADE,
    etiqueta_id INTEGER REFERENCES etiquetas(id) ON DELETE CASCADE,
    PRIMARY KEY (libro_id, etiqueta_id)
);

-- ------------------------------------------------------------
-- INSERTAR DATOS DE EJEMPLO
-- ------------------------------------------------------------

INSERT INTO generos (nombre, descripcion) VALUES
    ('Novela',       'Narrativa extensa de ficcion'),
    ('Ciencia',      'Textos cientificos y divulgacion'),
    ('Historia',     'Textos historicos y biografias'),
    ('Programacion', 'Libros tecnicos de desarrollo'),
    ('Poesia',       'Obras poeticas');

INSERT INTO autores (nombre, nacionalidad, fecha_nacimiento) VALUES
    ('Gabriel Garcia Marquez', 'Colombiana', '1927-03-06'),
    ('Isabel Allende',         'Chilena',    '1942-08-02'),
    ('Robert C. Martin',       'Estadounidense', '1952-12-05'),
    ('Octavio Paz',            'Mexicana',   '1914-03-31'),
    ('Martin Fowler',          'Britanica',  '1963-12-18');

INSERT INTO libros (titulo, isbn, anio_pub, precio, paginas, ejemplares, autor_id, genero_id) VALUES
    ('Cien anios de soledad',     '9780060883287', 1967, 299.00, 417, 5, 1, 1),
    ('El amor en los tiempos del colera', '9780307389732', 1985, 279.00, 348, 3, 1, 1),
    ('La casa de los espiritus',  '9780553383805', 1982, 259.00, 433, 4, 2, 1),
    ('Clean Code',                '9780132350884', 2008, 599.00, 464, 2, 3, 4),
    ('El laberinto de la soledad','9780802150424', 1950, 189.00, 310, 3, 4, 3),
    ('Refactoring',               '9780134757599', 2018, 649.00, 418, 2, 5, 4);

INSERT INTO socios (nombre, email, telefono) VALUES
    ('Elena Rodriguez', 'elena@mail.com',   '555-0101'),
    ('Jose Hernandez',  'jose@mail.com',    '555-0102'),
    ('Carmen Vega',     'carmen@mail.com',   '555-0103'),
    ('Luis Morales',    'luis@mail.com',     '555-0104');

INSERT INTO prestamos (libro_id, socio_id, fecha_prestamo, fecha_limite, estado) VALUES
    (1, 1, '2026-03-01', '2026-03-15', 'devuelto'),
    (4, 2, '2026-03-10', '2026-03-24', 'activo'),
    (1, 3, '2026-03-15', '2026-03-29', 'activo'),
    (3, 1, '2026-03-20', '2026-04-03', 'activo'),
    (6, 2, '2026-02-15', '2026-03-01', 'vencido');

INSERT INTO etiquetas (nombre) VALUES
    ('clasico'), ('best-seller'), ('tecnico'), ('latinoamerica'), ('obligatorio');

INSERT INTO libro_etiquetas (libro_id, etiqueta_id) VALUES
    (1, 1), (1, 2), (1, 4),  -- Cien anios: clasico, best-seller, latam
    (2, 1), (2, 4),           -- Amor tiempos: clasico, latam
    (3, 2), (3, 4),           -- Casa espiritus: best-seller, latam
    (4, 3), (4, 2),           -- Clean Code: tecnico, best-seller
    (5, 1), (5, 4),           -- Laberinto: clasico, latam
    (6, 3);                   -- Refactoring: tecnico

-- ------------------------------------------------------------
-- ALTER TABLE: Modificar estructura existente
-- ------------------------------------------------------------

-- Agregar columna
ALTER TABLE libros ADD COLUMN idioma VARCHAR(20) DEFAULT 'Espaniol';

-- Agregar restriccion
ALTER TABLE socios ADD CONSTRAINT chk_email CHECK (email LIKE '%@%.%');

-- Renombrar columna
ALTER TABLE prestamos RENAME COLUMN notas TO observaciones;

-- Cambiar default
ALTER TABLE libros ALTER COLUMN ejemplares SET DEFAULT 1;

-- Agregar indice para busquedas frecuentes
CREATE INDEX idx_libros_titulo ON libros(titulo);
CREATE INDEX idx_libros_isbn ON libros(isbn);
CREATE INDEX idx_prestamos_socio ON prestamos(socio_id);
CREATE INDEX idx_prestamos_estado ON prestamos(estado);

-- ------------------------------------------------------------
-- CONSULTAS SOBRE EL ESQUEMA
-- ------------------------------------------------------------

-- Libros con autor y genero
SELECT
    l.titulo,
    a.nombre AS autor,
    g.nombre AS genero,
    l.anio_pub,
    l.ejemplares
FROM libros l
JOIN autores a ON l.autor_id = a.id
LEFT JOIN generos g ON l.genero_id = g.id
ORDER BY l.anio_pub;

-- Prestamos activos con informacion completa
SELECT
    s.nombre  AS socio,
    l.titulo  AS libro,
    p.fecha_prestamo,
    p.fecha_limite,
    p.estado
FROM prestamos p
JOIN socios s ON p.socio_id = s.id
JOIN libros l ON p.libro_id = l.id
WHERE p.estado = 'activo'
ORDER BY p.fecha_limite;

-- Libros con sus etiquetas
SELECT
    l.titulo,
    STRING_AGG(e.nombre, ', ') AS etiquetas
FROM libros l
JOIN libro_etiquetas le ON l.id = le.libro_id
JOIN etiquetas e ON le.etiqueta_id = e.id
GROUP BY l.titulo
ORDER BY l.titulo;

-- Socios con total de prestamos
SELECT
    s.nombre,
    COUNT(p.id) AS total_prestamos,
    COUNT(CASE WHEN p.estado = 'activo' THEN 1 END) AS activos
FROM socios s
LEFT JOIN prestamos p ON s.id = p.socio_id
GROUP BY s.nombre
ORDER BY total_prestamos DESC;

-- Verificar integridad: libros sin suficientes ejemplares
SELECT
    l.titulo,
    l.ejemplares AS ejemplares_totales,
    COUNT(p.id) AS prestamos_activos
FROM libros l
LEFT JOIN prestamos p ON l.id = p.libro_id AND p.estado = 'activo'
GROUP BY l.id, l.titulo, l.ejemplares
HAVING COUNT(p.id) >= l.ejemplares;

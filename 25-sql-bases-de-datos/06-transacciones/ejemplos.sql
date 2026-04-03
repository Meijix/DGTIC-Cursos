-- ============================================================
-- 06 — Transacciones: Ejemplos Practicos
-- Escenario: Sistema bancario con cuentas y movimientos
-- ============================================================

-- ------------------------------------------------------------
-- CREAR TABLAS DEL SISTEMA BANCARIO
-- ------------------------------------------------------------

CREATE TABLE clientes (
    id       SERIAL PRIMARY KEY,
    nombre   VARCHAR(100) NOT NULL,
    email    VARCHAR(100) UNIQUE NOT NULL,
    is_activo BOOLEAN DEFAULT true
);

CREATE TABLE cuentas (
    id          SERIAL PRIMARY KEY,
    cliente_id  INTEGER NOT NULL REFERENCES clientes(id),
    tipo        VARCHAR(20) CHECK (tipo IN ('ahorro', 'corriente', 'nomina')),
    saldo       DECIMAL(12,2) NOT NULL DEFAULT 0.00 CHECK (saldo >= 0),
    moneda      VARCHAR(3) DEFAULT 'MXN',
    created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE movimientos (
    id              SERIAL PRIMARY KEY,
    cuenta_origen   INTEGER REFERENCES cuentas(id),
    cuenta_destino  INTEGER REFERENCES cuentas(id),
    tipo            VARCHAR(30) NOT NULL,
    monto           DECIMAL(12,2) NOT NULL CHECK (monto > 0),
    descripcion     TEXT,
    fecha           TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ------------------------------------------------------------
-- DATOS INICIALES
-- ------------------------------------------------------------

INSERT INTO clientes (nombre, email) VALUES
    ('Ana Garcia',    'ana@banco.com'),
    ('Carlos Lopez',  'carlos@banco.com'),
    ('Maria Torres',  'maria@banco.com'),
    ('Pedro Ramirez', 'pedro@banco.com');

INSERT INTO cuentas (cliente_id, tipo, saldo) VALUES
    (1, 'corriente', 50000.00),
    (1, 'ahorro',    100000.00),
    (2, 'corriente', 30000.00),
    (3, 'nomina',    25000.00),
    (4, 'corriente', 5000.00);

-- ============================================================
-- EJEMPLO 1: Transferencia basica entre cuentas
-- ============================================================

-- Transferir $5,000 de la cuenta 1 a la cuenta 3
BEGIN;
    -- Debitar de la cuenta origen
    UPDATE cuentas SET saldo = saldo - 5000.00 WHERE id = 1;

    -- Acreditar en la cuenta destino
    UPDATE cuentas SET saldo = saldo + 5000.00 WHERE id = 3;

    -- Registrar el movimiento
    INSERT INTO movimientos (cuenta_origen, cuenta_destino, tipo, monto, descripcion)
    VALUES (1, 3, 'transferencia', 5000.00, 'Pago de servicios');
COMMIT;

-- Verificar saldos
SELECT id, cliente_id, tipo, saldo FROM cuentas WHERE id IN (1, 3);

-- ============================================================
-- EJEMPLO 2: Transferencia con validacion de saldo
-- ============================================================

-- Intentar transferir $100,000 de cuenta 5 (solo tiene $5,000)
BEGIN;
    -- Verificar saldo suficiente (con bloqueo)
    -- Si el saldo es insuficiente, hacemos ROLLBACK
    DO $$
    DECLARE
        saldo_actual DECIMAL(12,2);
    BEGIN
        SELECT saldo INTO saldo_actual
        FROM cuentas WHERE id = 5 FOR UPDATE;

        IF saldo_actual < 100000.00 THEN
            RAISE EXCEPTION 'Saldo insuficiente. Disponible: %, Requerido: %',
                            saldo_actual, 100000.00;
        END IF;

        UPDATE cuentas SET saldo = saldo - 100000.00 WHERE id = 5;
        UPDATE cuentas SET saldo = saldo + 100000.00 WHERE id = 1;

        INSERT INTO movimientos (cuenta_origen, cuenta_destino, tipo, monto)
        VALUES (5, 1, 'transferencia', 100000.00);
    END $$;
COMMIT;
-- Esto fallara y hara ROLLBACK automatico por la excepcion

-- ============================================================
-- EJEMPLO 3: SAVEPOINT para operaciones parciales
-- ============================================================

-- Procesar multiples pagos, algunos pueden fallar
BEGIN;
    -- Pago 1: exitoso
    UPDATE cuentas SET saldo = saldo - 1000.00 WHERE id = 1;
    INSERT INTO movimientos (cuenta_origen, tipo, monto, descripcion)
    VALUES (1, 'pago', 1000.00, 'Pago luz');

    SAVEPOINT despues_pago_1;

    -- Pago 2: puede fallar
    UPDATE cuentas SET saldo = saldo - 2000.00 WHERE id = 1;
    INSERT INTO movimientos (cuenta_origen, tipo, monto, descripcion)
    VALUES (1, 'pago', 2000.00, 'Pago internet');

    -- Simular que hubo un problema con el pago 2
    -- ROLLBACK TO despues_pago_1;

    SAVEPOINT despues_pago_2;

    -- Pago 3: exitoso
    UPDATE cuentas SET saldo = saldo - 500.00 WHERE id = 1;
    INSERT INTO movimientos (cuenta_origen, tipo, monto, descripcion)
    VALUES (1, 'pago', 500.00, 'Pago telefono');

COMMIT;
-- Todos los pagos exitosos se confirman

-- ============================================================
-- EJEMPLO 4: Transferencia entre cuentas propias
-- ============================================================

-- Ana transfiere de su cuenta corriente a su cuenta de ahorro
BEGIN;
    -- Bloquear ambas cuentas en orden (prevenir deadlock)
    SELECT id, saldo FROM cuentas
    WHERE id IN (1, 2) AND cliente_id = 1
    ORDER BY id
    FOR UPDATE;

    UPDATE cuentas SET saldo = saldo - 10000.00 WHERE id = 1;
    UPDATE cuentas SET saldo = saldo + 10000.00 WHERE id = 2;

    INSERT INTO movimientos (cuenta_origen, cuenta_destino, tipo, monto, descripcion)
    VALUES (1, 2, 'traspaso_propio', 10000.00, 'Ahorro mensual');
COMMIT;

-- ============================================================
-- EJEMPLO 5: Deposito con registro de auditoria
-- ============================================================

BEGIN;
    -- Depositar $15,000 en la cuenta 4
    UPDATE cuentas SET saldo = saldo + 15000.00 WHERE id = 4;

    -- Registrar movimiento
    INSERT INTO movimientos (cuenta_destino, tipo, monto, descripcion)
    VALUES (4, 'deposito', 15000.00, 'Deposito en ventanilla');

COMMIT;

-- ============================================================
-- EJEMPLO 6: Retiro con validacion
-- ============================================================

BEGIN;
    -- Retirar $3,000 de la cuenta 3
    UPDATE cuentas
    SET saldo = saldo - 3000.00
    WHERE id = 3 AND saldo >= 3000.00;

    -- Verificar que se actualizo (GET DIAGNOSTICS en PL/pgSQL)
    -- Si no se actualizo ninguna fila, el saldo era insuficiente

    INSERT INTO movimientos (cuenta_origen, tipo, monto, descripcion)
    VALUES (3, 'retiro', 3000.00, 'Retiro en cajero');
COMMIT;

-- ============================================================
-- EJEMPLO 7: Cierre de cuenta (operacion compleja)
-- ============================================================

BEGIN;
    -- Transferir saldo restante a otra cuenta del mismo cliente
    UPDATE cuentas
    SET saldo = saldo + (SELECT saldo FROM cuentas WHERE id = 5)
    WHERE id = 3;  -- cuenta destino del mismo cliente? (verificar)

    -- Poner saldo en cero
    UPDATE cuentas SET saldo = 0.00 WHERE id = 5;

    -- Registrar movimiento de cierre
    INSERT INTO movimientos (cuenta_origen, cuenta_destino, tipo, monto, descripcion)
    VALUES (5, 3, 'cierre_cuenta',
            (SELECT saldo FROM cuentas WHERE id = 5),
            'Transferencia por cierre de cuenta');

    -- Marcar cuenta como inactiva (si tuvieramos columna is_activo)
    -- UPDATE cuentas SET is_activo = false WHERE id = 5;

COMMIT;

-- ============================================================
-- EJEMPLO 8: Nivel de aislamiento SERIALIZABLE
-- ============================================================

-- Para operaciones criticas que requieren maximo aislamiento
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
BEGIN;
    -- Calcular interes sobre el saldo actual
    UPDATE cuentas
    SET saldo = saldo * 1.005  -- 0.5% de interes mensual
    WHERE tipo = 'ahorro';

    -- Registrar el calculo de intereses
    INSERT INTO movimientos (cuenta_destino, tipo, monto, descripcion)
    SELECT id, 'interes', saldo * 0.005, 'Interes mensual ' || TO_CHAR(CURRENT_DATE, 'YYYY-MM')
    FROM cuentas
    WHERE tipo = 'ahorro';
COMMIT;

-- ============================================================
-- CONSULTAS DE VERIFICACION
-- ============================================================

-- Estado actual de todas las cuentas
SELECT
    c.id AS cuenta,
    cl.nombre AS cliente,
    c.tipo,
    c.saldo
FROM cuentas c
JOIN clientes cl ON c.cliente_id = cl.id
ORDER BY cl.nombre, c.tipo;

-- Historial de movimientos
SELECT
    m.id,
    m.tipo,
    m.monto,
    co.id AS origen,
    cd.id AS destino,
    m.descripcion,
    m.fecha
FROM movimientos m
LEFT JOIN cuentas co ON m.cuenta_origen = co.id
LEFT JOIN cuentas cd ON m.cuenta_destino = cd.id
ORDER BY m.fecha DESC;

-- Balance: suma de depositos vs retiros por cuenta
SELECT
    c.id AS cuenta,
    COALESCE(SUM(CASE WHEN m.cuenta_destino = c.id THEN m.monto END), 0) AS total_entradas,
    COALESCE(SUM(CASE WHEN m.cuenta_origen = c.id THEN m.monto END), 0) AS total_salidas
FROM cuentas c
LEFT JOIN movimientos m ON c.id = m.cuenta_origen OR c.id = m.cuenta_destino
GROUP BY c.id
ORDER BY c.id;

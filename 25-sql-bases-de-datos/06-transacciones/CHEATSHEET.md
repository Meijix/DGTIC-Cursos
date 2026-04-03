# 06 — Transacciones: Cheatsheet

## Comandos Basicos

```sql
BEGIN;                  -- iniciar transaccion
COMMIT;                 -- confirmar cambios
ROLLBACK;               -- revertir todo

SAVEPOINT nombre;              -- punto de guardado
ROLLBACK TO nombre;            -- revertir al savepoint
RELEASE SAVEPOINT nombre;      -- liberar savepoint
```

## ACID

```
  A — Atomicidad:    todo o nada
  C — Consistencia:  estado valido a estado valido
  I — Aislamiento:   transacciones no se interfieren
  D — Durabilidad:   COMMIT persiste ante fallos
```

## Niveles de Aislamiento

```
  READ UNCOMMITTED   — ve datos no confirmados (dirty read)
  READ COMMITTED     — solo datos confirmados (default PostgreSQL)
  REPEATABLE READ    — misma lectura da mismo resultado
  SERIALIZABLE       — maximo aislamiento, como si fueran secuenciales
```

```sql
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
```

## Problemas de Concurrencia

```
  Dirty Read:           leer datos no confirmados
  Non-Repeatable Read:  misma fila, valor diferente
  Phantom Read:         misma query, filas diferentes
```

## Bloqueos

```sql
-- Bloqueo de fila para actualizacion
SELECT * FROM tabla WHERE id = 1 FOR UPDATE;

-- Bloqueo sin esperar (falla si esta bloqueado)
SELECT * FROM tabla WHERE id = 1 FOR UPDATE NOWAIT;

-- Bloqueo con timeout
SELECT * FROM tabla WHERE id = 1 FOR UPDATE SKIP LOCKED;
```

## Patron: Transferencia Bancaria

```sql
BEGIN;
  SELECT saldo FROM cuentas WHERE id = 1 FOR UPDATE;
  UPDATE cuentas SET saldo = saldo - 100 WHERE id = 1;
  UPDATE cuentas SET saldo = saldo + 100 WHERE id = 2;
  INSERT INTO movimientos (origen, destino, monto) VALUES (1, 2, 100);
COMMIT;
```

## Patron: Con SAVEPOINT

```sql
BEGIN;
  INSERT INTO pedidos (...) VALUES (...);
  SAVEPOINT sp_items;
    INSERT INTO items (...) VALUES (...);  -- puede fallar
  -- Si fallo:
  ROLLBACK TO sp_items;
  -- Reintentar o continuar
COMMIT;
```

## Prevenir Deadlocks

```
  1. Acceder a recursos en orden consistente
  2. Transacciones cortas
  3. No esperar input del usuario dentro de BEGIN/COMMIT
  4. Usar NOWAIT o timeouts
```

## Tips

```
  - Mantener transacciones lo mas cortas posible
  - No incluir logica de aplicacion larga entre BEGIN y COMMIT
  - Siempre manejar errores con ROLLBACK
  - Usar READ COMMITTED como default seguro
  - SERIALIZABLE solo cuando sea estrictamente necesario
```

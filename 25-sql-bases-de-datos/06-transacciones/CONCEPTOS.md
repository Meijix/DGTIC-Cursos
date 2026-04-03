# 06 — Transacciones

## Que es una Transaccion

Una transaccion es un conjunto de operaciones SQL que se ejecutan como una
**unidad indivisible**. O se ejecutan TODAS correctamente, o NO se ejecuta
ninguna. Son fundamentales para mantener la integridad de los datos.

```
  Ejemplo clasico: Transferencia bancaria

  BEGIN;
    1. Restar $1000 de cuenta A
    2. Sumar $1000 a cuenta B
  COMMIT;

  Si falla el paso 2, el paso 1 se deshace automaticamente.
  Nunca se pierde dinero.
```

## Propiedades ACID

Toda transaccion debe cumplir estas cuatro propiedades:

```
  +---+----------------+------------------------------------------+
  | A | Atomicidad     | Todo o nada. Si una parte falla,         |
  |   |                | se revierte todo.                        |
  +---+----------------+------------------------------------------+
  | C | Consistencia   | La BD pasa de un estado valido a otro    |
  |   |                | estado valido. Las reglas se mantienen.  |
  +---+----------------+------------------------------------------+
  | I | Aislamiento    | Las transacciones concurrentes no se     |
  |   |                | interfieren entre si.                    |
  +---+----------------+------------------------------------------+
  | D | Durabilidad    | Una vez confirmada (COMMIT), los datos   |
  |   |                | persisten incluso ante fallos del sistema.|
  +---+----------------+------------------------------------------+
```

```
  ACID en accion:

  Transaccion 1          Transaccion 2
  +-----------+          +-----------+
  | BEGIN     |          | BEGIN     |
  | UPDATE A  |          | SELECT A  | <-- ve datos consistentes
  | UPDATE B  |          | SELECT B  | <-- no ve cambios parciales
  | COMMIT    |          | COMMIT    |
  +-----------+          +-----------+
       Atomica              Aislada
```

## Sintaxis Basica

```sql
-- Iniciar transaccion
BEGIN;
-- o: START TRANSACTION;

-- Operaciones SQL
UPDATE cuentas SET saldo = saldo - 1000 WHERE id = 1;
UPDATE cuentas SET saldo = saldo + 1000 WHERE id = 2;

-- Confirmar (guardar cambios)
COMMIT;

-- O revertir (deshacer cambios)
ROLLBACK;
```

## SAVEPOINT — Puntos de Guardado

Permite revertir parcialmente una transaccion.

```sql
BEGIN;
  UPDATE cuentas SET saldo = saldo - 500 WHERE id = 1;

  SAVEPOINT punto_1;

  UPDATE cuentas SET saldo = saldo + 500 WHERE id = 2;
  -- Ups, error! Revertir solo hasta el savepoint
  ROLLBACK TO punto_1;

  -- Intentar con otra cuenta
  UPDATE cuentas SET saldo = saldo + 500 WHERE id = 3;
COMMIT;
```

```
  BEGIN
    |
    UPDATE A  ------>  guardado
    |
    SAVEPOINT sp1
    |
    UPDATE B  ------>  error!
    |
    ROLLBACK TO sp1    (deshace solo UPDATE B)
    |
    UPDATE C  ------>  guardado
    |
  COMMIT               (A y C se confirman)
```

## Niveles de Aislamiento

Controlan que tan "visible" es una transaccion para las demas.

```
  +--------------------+----------+----------------+-------------+
  | Nivel              | Dirty    | Non-Repeatable | Phantom     |
  |                    | Read     | Read           | Read        |
  +--------------------+----------+----------------+-------------+
  | READ UNCOMMITTED   | Posible  | Posible        | Posible     |
  | READ COMMITTED     | No       | Posible        | Posible     |
  | REPEATABLE READ    | No       | No             | Posible     |
  | SERIALIZABLE       | No       | No             | No          |
  +--------------------+----------+----------------+-------------+
        Menos seguro                               Mas seguro
        Mas rapido                                 Mas lento
```

### Dirty Read (Lectura sucia)
Leer datos que otra transaccion aun no ha confirmado.

### Non-Repeatable Read (Lectura no repetible)
Leer la misma fila dos veces y obtener valores diferentes porque
otra transaccion hizo COMMIT entre ambas lecturas.

### Phantom Read (Lectura fantasma)
Ejecutar la misma consulta dos veces y obtener filas diferentes
porque otra transaccion inserto/elimino filas.

```sql
-- Establecer nivel de aislamiento
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
BEGIN;
  -- operaciones
COMMIT;
```

## Deadlocks (Bloqueos Mutuos)

Ocurren cuando dos transacciones esperan mutuamente a que la otra
libere un recurso.

```
  Transaccion 1             Transaccion 2
  +------------------+      +------------------+
  | BEGIN            |      | BEGIN            |
  | LOCK fila A      |      | LOCK fila B      |
  | ...              |      | ...              |
  | quiere fila B    |      | quiere fila A    |
  | ESPERA...    <---|----->| ESPERA...        |
  +------------------+      +------------------+
       Deadlock! Ninguna puede continuar.
       La BD detecta esto y cancela una.
```

### Prevenir Deadlocks

```
  1. Acceder a recursos siempre en el mismo orden
  2. Mantener transacciones cortas
  3. Evitar interaccion del usuario dentro de transacciones
  4. Usar timeouts apropiados
```

## Bloqueos (Locks)

```
  +------------------+--------------------------------------+
  | Tipo de Lock     | Descripcion                          |
  +------------------+--------------------------------------+
  | Row-level        | Bloquea filas individuales           |
  | Table-level      | Bloquea toda la tabla                |
  | Shared (Read)    | Permite lecturas, bloquea escrituras |
  | Exclusive (Write)| Bloquea lecturas y escrituras        |
  +------------------+--------------------------------------+
```

```sql
-- Bloqueo explicito de filas (FOR UPDATE)
BEGIN;
  SELECT * FROM cuentas WHERE id = 1 FOR UPDATE;
  -- Esta fila queda bloqueada hasta COMMIT/ROLLBACK
  UPDATE cuentas SET saldo = saldo - 100 WHERE id = 1;
COMMIT;
```

## Patron Comun: Transferencia Segura

```sql
BEGIN;
  -- Verificar saldo suficiente
  SELECT saldo FROM cuentas WHERE id = 1 FOR UPDATE;

  -- Solo si hay saldo suficiente
  UPDATE cuentas SET saldo = saldo - 1000 WHERE id = 1;
  UPDATE cuentas SET saldo = saldo + 1000 WHERE id = 2;

  -- Registrar la operacion
  INSERT INTO movimientos (cuenta_origen, cuenta_destino, monto, fecha)
  VALUES (1, 2, 1000, CURRENT_TIMESTAMP);
COMMIT;
```

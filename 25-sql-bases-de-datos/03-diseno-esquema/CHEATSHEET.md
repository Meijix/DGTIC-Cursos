# 03 — Diseno de Esquema: Cheatsheet

## CREATE TABLE

```sql
CREATE TABLE nombre_tabla (
    id          SERIAL PRIMARY KEY,
    texto       VARCHAR(100) NOT NULL,
    numero      INTEGER CHECK (numero > 0),
    decimal_    DECIMAL(10,2) DEFAULT 0.00,
    booleano    BOOLEAN DEFAULT true,
    fecha       DATE DEFAULT CURRENT_DATE,
    timestamp_  TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    fk_id       INTEGER REFERENCES otra_tabla(id)
);
```

## Tipos de Datos Comunes

```
  INTEGER / INT        numeros enteros
  SERIAL               entero auto-incremental
  DECIMAL(p,s)         numeros con decimales
  VARCHAR(n)           texto variable (max n)
  TEXT                 texto sin limite
  BOOLEAN              true / false
  DATE                 fecha (YYYY-MM-DD)
  TIMESTAMP            fecha y hora
  UUID                 identificador unico universal
```

## Restricciones

```sql
PRIMARY KEY            -- unico + no null
FOREIGN KEY            -- referencia otra tabla
NOT NULL               -- obligatorio
UNIQUE                 -- sin duplicados
CHECK (condicion)      -- validacion
DEFAULT valor          -- valor por defecto
```

## Foreign Key con Acciones

```sql
REFERENCES tabla(id) ON DELETE CASCADE      -- elimina hijos
REFERENCES tabla(id) ON DELETE SET NULL      -- pone NULL
REFERENCES tabla(id) ON DELETE RESTRICT      -- impide borrar
```

## Normalizacion Rapida

```
  1NF: Valores atomicos (un valor por celda)
  2NF: Todo depende de toda la PK
  3NF: No dependencias transitivas
```

## ALTER TABLE

```sql
ALTER TABLE t ADD COLUMN col VARCHAR(50);
ALTER TABLE t DROP COLUMN col;
ALTER TABLE t ALTER COLUMN col SET NOT NULL;
ALTER TABLE t ADD CONSTRAINT nombre CHECK (col > 0);
ALTER TABLE t RENAME COLUMN old TO new;
```

## DROP / TRUNCATE

```sql
DROP TABLE tabla;                    -- elimina tabla completa
DROP TABLE IF EXISTS tabla CASCADE;  -- con dependencias
TRUNCATE TABLE tabla;                -- vacia sin eliminar estructura
```

## Convenciones de Nombres

```
  Tablas:    plural, snake_case     (productos, orden_detalles)
  Columnas:  singular, snake_case   (nombre, fecha_creacion)
  PK:        id
  FK:        tabla_id               (usuario_id, producto_id)
  Indices:   idx_tabla_columna      (idx_productos_nombre)
```

## Checklist de Diseno

```
  [ ] Cada tabla tiene PRIMARY KEY
  [ ] FKs tienen indice
  [ ] Columnas obligatorias son NOT NULL
  [ ] Valores unicos marcados con UNIQUE
  [ ] Validaciones con CHECK donde aplique
  [ ] Nombres consistentes en snake_case
  [ ] Sin datos redundantes (normalizado)
  [ ] Timestamps de auditoria (created_at, updated_at)
```

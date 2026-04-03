# SQL y Bases de Datos Relacionales — Conceptos Generales

## Que es una Base de Datos Relacional

Una base de datos relacional organiza la informacion en **tablas** (relaciones)
compuestas por **filas** (registros/tuplas) y **columnas** (campos/atributos).
Cada tabla representa una entidad del mundo real y las relaciones entre tablas
se establecen mediante **claves**.

```
  TABLA: estudiantes
  +----+----------+-----------+-------+
  | id | nombre   | apellido  | edad  |
  +----+----------+-----------+-------+
  |  1 | Ana      | Garcia    |   22  |  <-- fila (registro)
  |  2 | Carlos   | Lopez     |   25  |
  |  3 | Maria    | Torres    |   21  |
  +----+----------+-----------+-------+
    ^       ^          ^          ^
    columnas (campos/atributos)
```

## Claves: Primaria y Foranea

- **PRIMARY KEY (PK):** Identifica de forma unica cada fila. No admite NULL ni duplicados.
- **FOREIGN KEY (FK):** Referencia la PK de otra tabla, estableciendo una relacion.

```
  estudiantes                    inscripciones
  +----+--------+               +----+--------+--------+
  | id | nombre |               | id | est_id | curso  |
  +----+--------+    1:N        +----+--------+--------+
  |  1 | Ana    | ------------> |  1 |    1   | SQL    |
  |  2 | Carlos |               |  2 |    1   | Python |
  +----+--------+               |  3 |    2   | SQL    |
                                +----+--------+--------+
                                       ^
                                       FK --> estudiantes.id
```

## Modelo Entidad-Relacion (ER)

```
  +-------------+        +----------------+        +-----------+
  |  ESTUDIANTE |        |  INSCRIPCION   |        |   CURSO   |
  |-------------|        |----------------|        |-----------|
  | PK id       |---1:N--| PK id          |--N:1---| PK id     |
  | nombre      |        | FK est_id      |        | nombre    |
  | email       |        | FK curso_id    |        | creditos  |
  | edad        |        | fecha          |        | profesor  |
  +-------------+        +----------------+        +-----------+
```

## Categorias del Lenguaje SQL

SQL se divide en cuatro categorias principales:

### DDL — Data Definition Language (Definicion)
Define la estructura de la base de datos.
```sql
CREATE TABLE, ALTER TABLE, DROP TABLE, TRUNCATE
```

### DML — Data Manipulation Language (Manipulacion)
Opera sobre los datos almacenados.
```sql
SELECT, INSERT, UPDATE, DELETE
```

### DCL — Data Control Language (Control de acceso)
Gestiona permisos y seguridad.
```sql
GRANT, REVOKE
```

### TCL — Transaction Control Language (Transacciones)
Controla las transacciones de datos.
```sql
BEGIN, COMMIT, ROLLBACK, SAVEPOINT
```

```
  +-------------------------------------------------------+
  |                        SQL                             |
  |  +----------+  +---------+  +--------+  +-----------+ |
  |  |   DDL    |  |   DML   |  |  DCL   |  |    TCL    | |
  |  | CREATE   |  | SELECT  |  | GRANT  |  | BEGIN     | |
  |  | ALTER    |  | INSERT  |  | REVOKE |  | COMMIT    | |
  |  | DROP     |  | UPDATE  |  +--------+  | ROLLBACK  | |
  |  | TRUNCATE |  | DELETE  |              | SAVEPOINT | |
  |  +----------+  +---------+              +-----------+ |
  +-------------------------------------------------------+
```

## SQL vs NoSQL — Comparacion

| Caracteristica     | SQL (Relacional)         | NoSQL (No Relacional)      |
|--------------------|--------------------------|----------------------------|
| Estructura         | Tablas con esquema fijo   | Documentos, clave-valor... |
| Esquema            | Rigido (predefinido)      | Flexible (dinamico)        |
| Lenguaje           | SQL estandar              | Varia por motor            |
| Escalabilidad      | Vertical (mas hardware)   | Horizontal (mas nodos)     |
| Transacciones      | ACID completo             | BASE (eventual)            |
| Relaciones         | JOINs nativos             | Embebido o referencia      |
| Ejemplos           | PostgreSQL, MySQL, Oracle | MongoDB, Redis, Cassandra  |
| Ideal para         | Datos estructurados       | Datos flexibles/masivos    |

## Cuando Usar Cada Uno

**SQL es ideal cuando:**
- Los datos tienen relaciones claras entre entidades
- Se requiere integridad transaccional (bancos, inventarios)
- El esquema es estable y bien definido

**NoSQL es ideal cuando:**
- El esquema cambia frecuentemente
- Se necesita escalabilidad horizontal masiva
- Los datos son semi-estructurados o no estructurados

## Motores de Bases de Datos Populares

```
  Relacionales (SQL):          No Relacionales (NoSQL):
  +------------------+         +------------------+
  | PostgreSQL       |         | MongoDB (doc)    |
  | MySQL / MariaDB  |         | Redis (kv)       |
  | SQLite           |         | Cassandra (col)  |
  | SQL Server       |         | Neo4j (grafo)    |
  | Oracle           |         | DynamoDB (kv)    |
  +------------------+         +------------------+
```

## Estructura del Modulo

1. **Fundamentos SQL** — CRUD basico y filtrado
2. **Relaciones y JOINs** — Conectar tablas entre si
3. **Diseno de Esquema** — Normalizacion y buenas practicas
4. **Consultas Avanzadas** — Subqueries, agrupaciones, ventanas
5. **Indices y Optimizacion** — Rendimiento de consultas
6. **Transacciones** — ACID, aislamiento y concurrencia
7. **Proyecto Final** — Sistema e-commerce completo

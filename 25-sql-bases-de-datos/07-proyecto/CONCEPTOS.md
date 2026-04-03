# 07 — Proyecto Final: Sistema E-Commerce

## Descripcion del Proyecto

Diseno completo de una base de datos para un sistema de comercio electronico.
Incluye usuarios, productos, categorias, ordenes de compra, detalles de orden
y resenas de productos.

## Diagrama Entidad-Relacion

```
  +-------------+         +------------------+         +-----------+
  |  CATEGORIAS |         |    PRODUCTOS     |         | RESENAS   |
  |-------------|         |------------------|         |-----------|
  | PK id       |---1:N---| PK id            |---1:N---| PK id     |
  | nombre      |         | nombre           |         | FK prod_id|
  | descripcion |         | descripcion      |         | FK user_id|
  +-------------+         | precio           |         | rating    |
                          | stock            |         | comentario|
                          | FK categoria_id  |         | fecha     |
                          | is_activo        |         +-----------+
                          +------------------+
                                  |
                                 1:N
                                  |
  +-------------+         +------------------+
  |  USUARIOS   |         | ORDEN_DETALLES   |
  |-------------|         |------------------|
  | PK id       |---1:N---| PK id            |
  | nombre      |         | FK orden_id      |
  | email       |    |    | FK producto_id   |
  | password    |    |    | cantidad         |
  | direccion   |    |    | precio_unitario  |
  | telefono    |    |    | subtotal         |
  +-------------+    |    +------------------+
       |             |           |
      1:N           1:N         N:1
       |             |           |
  +-------------+         +------------------+
  |  ORDENES    |---------| (relacion)       |
  |-------------|         +------------------+
  | PK id       |
  | FK user_id  |
  | estado      |
  | total       |
  | direccion   |
  | fecha       |
  +-------------+
```

## Entidades del Sistema

```
  +------------------+------------------------------------+
  | Entidad          | Descripcion                        |
  +------------------+------------------------------------+
  | usuarios         | Compradores registrados            |
  | categorias       | Clasificacion de productos         |
  | productos        | Articulos a la venta               |
  | ordenes          | Pedidos de compra                  |
  | orden_detalles   | Items individuales de cada orden   |
  | resenas          | Opiniones de usuarios sobre prod.  |
  +------------------+------------------------------------+
```

## Relaciones

```
  usuarios    --1:N-->  ordenes        (un usuario, muchas ordenes)
  usuarios    --1:N-->  resenas        (un usuario, muchas resenas)
  ordenes     --1:N-->  orden_detalles (una orden, muchos items)
  productos   --1:N-->  orden_detalles (un producto en muchos items)
  productos   --1:N-->  resenas        (un producto, muchas resenas)
  categorias  --1:N-->  productos      (una categoria, muchos prod.)
```

## Flujo del Sistema

```
  1. Usuario se registra
         |
  2. Navega productos por categoria
         |
  3. Agrega productos al carrito
         |
  4. Crea una orden (estado: 'pendiente')
         |
  5. Se procesan los detalles de la orden
     (se descuenta stock, se calcula total)
         |
  6. Orden cambia de estado:
     pendiente -> pagada -> enviada -> entregada
         |
  7. Usuario deja resena del producto
```

## Funcionalidades Implementadas

- **Esquema completo** con restricciones y relaciones
- **Datos de ejemplo** para pruebas
- **Consultas complejas** con JOINs, agregaciones y subqueries
- **Vistas** para reportes frecuentes
- **Procedimientos almacenados** para operaciones de negocio
- **Indices** para optimizacion de consultas frecuentes

## Consideraciones de Diseno

```
  Normalizacion:
  - Categorias separadas de productos (3NF)
  - Detalles de orden separados de ordenes (2NF)
  - Precio unitario guardado en detalle (precio historico)

  Integridad:
  - CHECK en stock >= 0
  - CHECK en rating BETWEEN 1 AND 5
  - ON DELETE RESTRICT en relaciones criticas
  - Indices en FKs y columnas de busqueda

  Auditoria:
  - created_at en todas las tablas
  - updated_at con trigger en tablas mutables
```

## Extensiones Posibles

```
  - Carrito de compras (tabla separada antes de crear orden)
  - Sistema de cupones y descuentos
  - Direcciones multiples por usuario
  - Metodos de pago
  - Historial de precios de productos
  - Sistema de envios con tracking
  - Wishlist / lista de deseos
```

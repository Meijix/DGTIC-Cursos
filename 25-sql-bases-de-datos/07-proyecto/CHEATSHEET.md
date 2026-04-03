# 07 — Proyecto E-Commerce: Cheatsheet

## Tablas del Sistema

```
  categorias       — clasificacion de productos
  productos        — articulos a la venta
  usuarios         — compradores registrados
  ordenes          — pedidos de compra
  orden_detalles   — items de cada pedido
  resenas          — opiniones y calificaciones
```

## Relaciones Clave

```
  categorias  --1:N-->  productos
  usuarios    --1:N-->  ordenes
  usuarios    --1:N-->  resenas
  ordenes     --1:N-->  orden_detalles
  productos   --1:N-->  orden_detalles
  productos   --1:N-->  resenas
```

## Estados de Orden

```
  pendiente -> pagada -> enviada -> entregada
                                 -> cancelada (desde cualquier estado)
```

## Consultas Frecuentes

```sql
-- Productos de una categoria
SELECT * FROM productos WHERE categoria_id = ? AND is_activo = true;

-- Detalle de una orden
SELECT od.*, p.nombre FROM orden_detalles od
JOIN productos p ON od.producto_id = p.id
WHERE od.orden_id = ?;

-- Historial de compras de un usuario
SELECT o.*, COUNT(od.id) AS items
FROM ordenes o JOIN orden_detalles od ON o.id = od.orden_id
WHERE o.usuario_id = ? GROUP BY o.id;

-- Rating promedio de un producto
SELECT AVG(rating), COUNT(*) FROM resenas WHERE producto_id = ?;
```

## Vistas Utiles

```sql
-- Vista de productos con categoria y rating
CREATE VIEW v_productos_completos AS ...

-- Vista de ventas por mes
CREATE VIEW v_ventas_mensuales AS ...

-- Vista de mejores clientes
CREATE VIEW v_top_clientes AS ...
```

## Procedimientos Clave

```sql
-- Crear una orden completa
CALL crear_orden(usuario_id, items[]);

-- Actualizar estado de orden
CALL actualizar_estado_orden(orden_id, nuevo_estado);

-- Procesar devolucion
CALL procesar_devolucion(orden_id);
```

## Indices Recomendados

```sql
CREATE INDEX idx_productos_categoria ON productos(categoria_id);
CREATE INDEX idx_ordenes_usuario ON ordenes(usuario_id);
CREATE INDEX idx_ordenes_estado ON ordenes(estado);
CREATE INDEX idx_detalles_orden ON orden_detalles(orden_id);
CREATE INDEX idx_detalles_producto ON orden_detalles(producto_id);
CREATE INDEX idx_resenas_producto ON resenas(producto_id);
CREATE INDEX idx_resenas_usuario ON resenas(usuario_id);
```

## Validaciones Importantes

```
  productos.precio > 0
  productos.stock >= 0
  resenas.rating BETWEEN 1 AND 5
  orden_detalles.cantidad > 0
  ordenes.total >= 0
  usuarios.email UNIQUE
```

## Metricas de Negocio

```sql
-- Total de ventas
SELECT SUM(total) FROM ordenes WHERE estado != 'cancelada';

-- Producto mas vendido
SELECT producto_id, SUM(cantidad) FROM orden_detalles GROUP BY 1 ORDER BY 2 DESC LIMIT 1;

-- Ticket promedio
SELECT AVG(total) FROM ordenes WHERE estado = 'entregada';

-- Tasa de conversion (ordenes/usuarios)
SELECT COUNT(DISTINCT usuario_id)::FLOAT / (SELECT COUNT(*) FROM usuarios) FROM ordenes;
```

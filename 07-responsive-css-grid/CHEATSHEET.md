# Cheatsheet — Modulo 07: CSS Grid

## Grid = Layout bidimensional

```
  FLEXBOX = 1 Dimension             CSS GRID = 2 Dimensiones
  (fila O columna)                  (filas Y columnas a la vez)

  +-----+-----+-----+-----+        +-----+-----+-----+
  |  A  |  B  |  C  |  D  |        |  A  |  B  |  C  | fila 1
  +-----+-----+-----+-----+        +-----+-----+-----+
  Solo controla UN eje              |  D  |     E     | fila 2
                                    +-----+---+-------+
                                    |    F    |   G   | fila 3
                                    +---------+-------+
```

## Terminologia del Grid

```
  Lineas de columna:  1     2     3     4
                      |     |     |     |
  Linea de fila 1 ----+-----+-----+-----+
                      |celda|celda|celda |  <-- Track de fila 1
  Linea de fila 2 ----+-----+-----+-----+
                      |celda|celda|celda |  <-- Track de fila 2
  Linea de fila 3 ----+-----+-----+-----+

                      ^           ^
                  Track de    Track de
                  columna 1   columna 2

  N columnas = N+1 lineas de columna
  N filas    = N+1 lineas de fila
```

## Referencia rapida: propiedades del CONTENEDOR

| Propiedad                | Ejemplo                               | Efecto                       |
|--------------------------|---------------------------------------|------------------------------|
| `display`                | `grid`                                | Activa CSS Grid              |
| `grid-template-columns`  | `200px 1fr 2fr`                       | Define columnas              |
| `grid-template-rows`     | `100px auto`                          | Define filas                 |
| `grid-template-areas`    | `"header header" "sidebar main"`      | Layout con nombres           |
| `gap`                    | `10px 20px`                           | Espacio entre tracks         |
| `justify-items`          | `start`, `center`, `end`, `stretch`   | Items horizontal en celda    |
| `align-items`            | `start`, `center`, `end`, `stretch`   | Items vertical en celda      |
| `grid-auto-rows`         | `minmax(100px, auto)`                 | Tamano filas implicitas      |

## Referencia rapida: propiedades del ITEM

| Propiedad       | Ejemplo          | Efecto                                |
|-----------------|------------------|---------------------------------------|
| `grid-column`   | `1 / 4`          | Ocupa de linea 1 a linea 4           |
| `grid-row`      | `1 / 3`          | Ocupa de linea de fila 1 a 3         |
| `grid-column`   | `span 3`         | Ocupa 3 columnas desde donde le toque|
| `grid-area`     | `1 / 1 / 3 / 4`  | Shorthand: fila-ini/col-ini/fila-fin/col-fin |
| `grid-area`     | `header`         | Nombre asignado en template-areas    |
| `justify-self`  | `center`         | Alinea ESTE item horizontalmente     |
| `align-self`    | `center`         | Alinea ESTE item verticalmente       |

## Unidades clave de Grid

| Unidad        | Descripcion                                | Ejemplo              |
|---------------|--------------------------------------------|----------------------|
| `fr`          | Fraccion del espacio RESTANTE              | `1fr 2fr` = 1/3 2/3 |
| `minmax()`    | Tamano entre un minimo y un maximo         | `minmax(200px, 1fr)` |
| `repeat()`    | Repite un patron de tracks                 | `repeat(3, 1fr)`     |
| `auto-fill`   | Crea tantas columnas como quepan           | `repeat(auto-fill, minmax(200px, 1fr))` |
| `auto-fit`    | Igual pero COLAPSA columnas vacias         | `repeat(auto-fit, minmax(200px, 1fr))`  |
| `auto`        | Se ajusta al contenido                     | `auto`               |

## auto-fill vs auto-fit

```
  auto-fill: +----+----+----+----+   columnas vacias EXISTEN (no se estiran)
  auto-fit:  +------+------+------+  columnas vacias COLAPSADAS (items se estiran)
```

## grid-template-areas (layout con nombres)

```css
.contenedor {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    grid-template-areas:
        "header  header  header"    /* +--header---+ */
        "sidebar main    main"     /* |side| main  | */
        "footer  footer  footer";  /* +--footer---+ */
}
.mi-header { grid-area: header; }  .mi-main { grid-area: main; }
```

Reglas: areas deben ser rectangulares. Usar `.` para celdas vacias.

## Patron responsivo sin media queries

```css
/* Grid que se adapta automaticamente */
.grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 20px;
}
```

## Grid + Flexbox: patron combinado

Grid para layout de pagina (2D), Flexbox para componentes internos (1D).
Un elemento puede ser item-grid Y contenedor-flex a la vez.

## fr vs %: por que preferir fr

`%` NO descuenta el `gap` (desborda). `fr` SI lo descuenta (perfecto).

## Errores comunes

| Error | Problema | Solucion |
|-------|----------|----------|
| Usar `%` en columnas con `gap` | El total excede 100%, desborda | Usar `fr` en vez de `%` |
| Areas no rectangulares en template-areas | CSS invalido, no funciona | Las areas deben ser rectangulos |
| Olvidar que las lineas empiezan en 1 | `grid-column: 0/3` es invalido | Las lineas van de 1 a N+1 |
| Confundir `auto-fill` con `auto-fit` | Items no se estiran como se espera | `auto-fit` colapsa vacias, `auto-fill` no |
| Usar Grid donde basta Flexbox | Complejidad innecesaria | Un solo eje = Flexbox; dos ejes = Grid |
| No definir `grid-auto-rows` | Filas implicitas con altura `auto` inesperada | Definir `grid-auto-rows: minmax(100px, auto)` |

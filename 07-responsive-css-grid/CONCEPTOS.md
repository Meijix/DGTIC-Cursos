# Modulo 07 — CSS Grid: El Sistema de Layout Bidimensional

> **Prerequisitos:** Modulos 01-06 (HTML semantico, CSS base, Flexbox, responsive design).
> **Archivos del ejercicio:** `index.html` y `styles.css` en esta misma carpeta.

---

## Indice

1. [Que problema resuelve CSS Grid](#1-que-problema-resuelve-css-grid)
2. [Terminologia de Grid](#2-terminologia-de-grid)
3. [Definiendo columnas y filas](#3-definiendo-columnas-y-filas)
4. [Posicionando items](#4-posicionando-items)
5. [Alineacion en Grid](#5-alineacion-en-grid)
6. [Grid + Flexbox: el patron combinado](#6-grid--flexbox-el-patron-combinado)
7. [Grid implicito vs explicito](#7-grid-implicito-vs-explicito)
8. [Patrones Grid responsivos](#8-patrones-grid-responsivos)
9. [Errores comunes](#9-errores-comunes)
10. [Grid vs Flexbox: Guia de decision completa](#10-grid-vs-flexbox-guia-de-decision-completa)
11. [Ejercicios de practica](#11-ejercicios-de-practica)

---

## 1. Que problema resuelve CSS Grid

### El problema

Antes de CSS Grid, crear layouts bidimensionales (controlar filas Y columnas al mismo
tiempo) requeria trucos con `float`, `inline-block`, tablas CSS, o combinaciones
complejas de Flexbox anidado. Ninguna de estas soluciones fue disenada para ese proposito.

### La solucion

CSS Grid es el **primer sistema de layout nativo de CSS disenado para trabajar en
dos dimensiones**. Permite definir filas y columnas simultaneamente y colocar
elementos en cualquier celda de la cuadricula.

```
  FLEXBOX = 1 Dimension               CSS GRID = 2 Dimensiones
  (un eje a la vez)                    (filas Y columnas a la vez)

  ┌─────┬─────┬─────┬─────┐           ┌─────┬─────┬─────┐
  │  A  │  B  │  C  │  D  │ ← fila    │  A  │  B  │  C  │ ← fila 1
  └─────┴─────┴─────┴─────┘           ├─────┼─────┴─────┤
  Solo controla UNA fila               │  D  │     E     │ ← fila 2
  o UNA columna                        ├─────┴───┬───────┤
                                       │    F    │   G   │ ← fila 3
                                       └─────────┴───────┘
                                       Controla filas Y columnas
```

### Modelo mental clave

```
  ┌──────────────────────────────────────────────────────────┐
  │  Grid es para LAYOUT (la estructura de la pagina)        │
  │  Flexbox es para ALINEACION (distribuir items en 1 eje)  │
  └──────────────────────────────────────────────────────────┘
```

### Diagrama de decision rapido

```
  ¿Necesitas controlar filas Y columnas al mismo tiempo?
       │
       ├── SI ──→ Usa CSS GRID
       │           Ejemplos: formularios en cuadricula, dashboards,
       │           layouts de pagina completa, galerias de imagenes
       │
       └── NO ──→ ¿Trabajas en UN solo eje (fila o columna)?
                    │
                    ├── SI ──→ Usa FLEXBOX
                    │           Ejemplos: barra de navegacion, grupo de
                    │           botones, centrar un elemento, apilar cards
                    │
                    └── AMBOS ──→ Usa Grid para el layout general
                                  y Flexbox para los componentes internos
```

---

## 2. Terminologia de Grid

Antes de escribir una sola linea de CSS Grid, es fundamental dominar la
terminologia. Cada termino tiene un significado preciso.

### 2.1 Contenedor Grid vs Items Grid

```
  contenedor grid (display: grid)
  ┌───────────────────────────────────────────┐
  │                                           │
  │   ┌─────────┐  ┌─────────┐  ┌─────────┐  │
  │   │ Item 1  │  │ Item 2  │  │ Item 3  │  │  ← Items Grid
  │   └─────────┘  └─────────┘  └─────────┘  │    (hijos DIRECTOS)
  │                                           │
  │   ┌─────────┐  ┌─────────┐               │
  │   │ Item 4  │  │ Item 5  │               │
  │   └─────────┘  └─────────┘               │
  │                                           │
  └───────────────────────────────────────────┘

  IMPORTANTE: Solo los hijos DIRECTOS son items grid.
  Los nietos, bisnietos, etc. NO son items grid.
```

### 2.2 Lineas Grid (Grid Lines)

Las lineas son las **divisiones invisibles** que forman la estructura del grid.
Se numeran empezando desde **1** (NO desde 0).

```
  Lineas de columna:
         1     2     3     4     5     6     7
         │     │     │     │     │     │     │
         ▼     ▼     ▼     ▼     ▼     ▼     ▼
    1 ───┬─────┬─────┬─────┬─────┬─────┬─────┐
         │     │     │     │     │     │     │
    2 ───┼─────┼─────┼─────┼─────┼─────┼─────┤  ← Lineas
         │     │     │     │     │     │     │     de fila
    3 ───┼─────┼─────┼─────┼─────┼─────┼─────┤
         │     │     │     │     │     │     │
    4 ───┴─────┴─────┴─────┴─────┴─────┴─────┘

  Un grid de 6 columnas tiene 7 lineas de columna (N+1).
  Un grid de 3 filas tiene 4 lineas de fila (N+1).
```

**Regla de oro:** Para N tracks (columnas o filas), siempre hay **N+1** lineas.

### 2.3 Tracks (Pistas)

Un track es el espacio **entre dos lineas adyacentes**. Los tracks son las
columnas y filas reales donde se coloca contenido.

```
  Lineas:  1     2     3     4
           │     │     │     │
  1 ───────┼─────┼─────┼─────┤
           │  A  │  B  │  C  │   ← Track de fila 1
  2 ───────┼─────┼─────┼─────┤
           │  D  │  E  │  F  │   ← Track de fila 2
  3 ───────┼─────┼─────┼─────┤

           ↑        ↑
    Track de     Track de
    columna 1    columna 2
```

### 2.4 Celdas Grid (Grid Cells)

Una celda es la interseccion de UN track de fila con UN track de columna.
Es la unidad mas pequena del grid.

```
           col 1   col 2   col 3
         ┌───────┬───────┬───────┐
  fila 1 │ celda │ celda │ celda │
         │ (1,1) │ (1,2) │ (1,3) │
         ├───────┼───────┼───────┤
  fila 2 │ celda │ celda │ celda │
         │ (2,1) │ (2,2) │ (2,3) │
         └───────┴───────┴───────┘

  Un grid de 3 columnas x 2 filas tiene 6 celdas.
```

### 2.5 Areas Grid (Grid Areas)

Un area es un **rectangulo de una o mas celdas**. Un item puede ocupar
multiples celdas formando un area.

```
         col 1   col 2   col 3
       ┌───────┬───────┬───────┐
       │       │               │
       │   A   │      B        │  ← B ocupa un AREA de 2 celdas
       │       │               │
       ├───────┴───────┬───────┤
       │               │       │
       │      C        │   D   │  ← C ocupa un AREA de 2 celdas
       │               │       │
       └───────────────┴───────┘
```

### 2.6 Gaps (Espacios)

Los gaps son los **espacios entre tracks** (no entre los items y el borde
del contenedor).

```
         col 1       col 2       col 3
       ┌───────┐   ┌───────┐   ┌───────┐
       │       │   │       │   │       │
       │       │   │       │   │       │
       └───────┘   └───────┘   └───────┘
                 ↑           ↑
              column-gap  column-gap
       ┌───────┐   ┌───────┐   ┌───────┐  ← row-gap entre filas
       │       │   │       │   │       │
       │       │   │       │   │       │
       └───────┘   └───────┘   └───────┘

  gap: 10px 20px;    → row-gap: 10px, column-gap: 20px
  gap: 15px;         → row-gap Y column-gap: 15px ambos
  row-gap: 10px;     → solo espacio entre filas
  column-gap: 20px;  → solo espacio entre columnas
```

---

## 3. Definiendo columnas y filas

### 3.1 grid-template-columns y grid-template-rows

Estas propiedades definen la estructura del grid: cuantos tracks hay y
que tamanio tiene cada uno.

```css
/* 3 columnas de tamanios fijos */
grid-template-columns: 200px 300px 200px;

/* 2 filas: la primera de 100px, la segunda automatica */
grid-template-rows: 100px auto;
```

```
  200px    300px    200px
  ┌───────┬──────────┬───────┐
  │       │          │       │ 100px
  ├───────┼──────────┼───────┤
  │       │          │       │ auto (se ajusta al contenido)
  └───────┴──────────┴───────┘
```

### 3.2 Unidades disponibles

| Unidad      | Descripcion                                    | Ejemplo                     |
|-------------|------------------------------------------------|-----------------------------|
| `px`        | Pixeles fijos                                  | `200px`                     |
| `%`         | Porcentaje del contenedor                      | `50%`                       |
| `fr`        | Fraccion del espacio RESTANTE                  | `1fr`                       |
| `auto`      | Se ajusta al contenido                         | `auto`                      |
| `minmax()`  | Tamanio minimo y maximo                        | `minmax(200px, 1fr)`        |
| `repeat()`  | Repetir un patron de tracks                    | `repeat(3, 1fr)`            |
| `min-content` | El ancho minimo sin desbordamiento           | `min-content`               |
| `max-content` | El ancho ideal sin saltos de linea            | `max-content`               |
| `fit-content()` | Como max-content pero con un tope          | `fit-content(300px)`        |

### 3.3 La unidad `fr` (fraccional)

La unidad `fr` es **exclusiva de CSS Grid**. Representa una fraccion del
espacio **restante** despues de asignar el espacio fijo.

```css
grid-template-columns: 200px 1fr 2fr;
```

```
  Contenedor de 800px de ancho:

  1. Espacio fijo:     200px para la primera columna
  2. Espacio restante: 800px - 200px = 600px
  3. Total de fr:      1fr + 2fr = 3fr
  4. Valor de 1fr:     600px / 3 = 200px
  5. Resultado:

     200px      200px          400px
     (fijo)     (1fr)          (2fr)
     ┌─────────┬──────────┬──────────────────┐
     │         │          │                  │
     └─────────┴──────────┴──────────────────┘
```

**Comparacion de unidades:**

```css
/* Porcentajes: NO consideran el gap */
grid-template-columns: 33.33% 33.33% 33.33%;
/* Con gap: 20px, el total es 100% + 40px = DESBORDAMIENTO */

/* fr: SI considera el gap automaticamente */
grid-template-columns: 1fr 1fr 1fr;
/* Con gap: 20px, cada fr = (ancho - 40px) / 3 = PERFECTO */
```

**Conclusion:** Usa `fr` en lugar de `%` siempre que sea posible. La unidad `fr`
evita problemas de desbordamiento cuando se usa `gap`.

### 3.4 La funcion `repeat()`

Evita escribir el mismo valor multiples veces.

```css
/* Estas dos lineas son equivalentes: */
grid-template-columns: 1fr 1fr 1fr 1fr 1fr 1fr;
grid-template-columns: repeat(6, 1fr);

/* Repetir un patron: */
grid-template-columns: repeat(3, 100px 1fr);
/* Equivale a: 100px 1fr 100px 1fr 100px 1fr */
```

En nuestro ejercicio (`styles.css`, linea 277):

```css
.grid {
  grid-template-columns: repeat(6, 16.66%);
}
```

Esto crea 6 columnas de ~16.66% cada una. **Nota:** Una alternativa mas precisa
seria `repeat(6, 1fr)`, que divide el espacio exactamente en sextos sin riesgo
de desbordamiento.

### 3.5 `auto-fill` vs `auto-fit`

Ambos se usan dentro de `repeat()` para crear un numero **automatico** de columnas.

```css
/* auto-fill: crea tantas columnas como quepan */
grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));

/* auto-fit: igual, pero COLAPSA las columnas vacias */
grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
```

```
  Contenedor de 900px, minmax(200px, 1fr):

  auto-fill (4 columnas creadas, solo 3 con contenido):
  ┌──────┬──────┬──────┬──────┐
  │  A   │  B   │  C   │      │  ← columna vacia EXISTE
  └──────┴──────┴──────┴──────┘
   225px  225px  225px  225px

  auto-fit (columnas vacias COLAPSADAS):
  ┌──────────┬──────────┬──────────┐
  │    A     │    B     │    C     │  ← sin columnas vacias
  └──────────┴──────────┴──────────┘
     300px      300px      300px
```

| Caracteristica           | `auto-fill`                      | `auto-fit`                       |
|--------------------------|----------------------------------|----------------------------------|
| Columnas vacias          | Se mantienen (ocupan espacio)    | Se colapsan (ancho 0)            |
| Items se estiran         | NO (respetan el tamanio maximo)  | SI (ocupan el espacio sobrante)  |
| Caso de uso tipico       | Grids con items de tamanio fijo  | Grids donde los items deben llenar todo el ancho |

---

## 4. Posicionando items

### 4.1 `grid-column` y `grid-row`

Estas propiedades permiten colocar un item en una posicion especifica del grid
usando **numeros de linea**.

```css
.item {
  grid-column: 1 / 4;   /* Desde la LINEA 1 hasta la LINEA 4 */
  grid-row: 1 / 3;      /* Desde la LINEA de fila 1 hasta la 3 */
}
```

```
  Lineas:  1     2     3     4     5     6     7
  1 ───────┬─────┬─────┬─────┬─────┬─────┬─────┐
           │                 │     │     │     │
           │  grid-column:   │     │     │     │
           │    1 / 4        │     │     │     │
           │  (3 columnas)   │     │     │     │
  2 ───────┼─────────────────┼─────┼─────┼─────┤
           │                 │     │     │     │
  3 ───────┴─────┴─────┴─────┴─────┴─────┴─────┘
```

**En nuestro ejercicio** (`styles.css`, lineas 284-310), los campos del formulario
se posicionan asi:

```
  Grid de 6 columnas (7 lineas):
  Lineas:  1     2     3     4     5     6     7

  Fila 1:  ┌─────────────────┬─────────────────┐
           │    .nombre       │    .correo       │
           │  grid-column:    │  grid-column:    │
           │     1 / 4        │     4 / 7        │
           │  (3 columnas)    │  (3 columnas)    │
           ├───────────┬─────┴───────────────────┤
  Fila 2:  │ .procede   │       .sabor            │
           │ grid-column│    grid-column:          │
           │   1 / 3    │       3 / 7              │
           │(2 columnas)│    (4 columnas)          │
           └───────────┴──────────────────────────┘
```

### 4.2 La palabra clave `span`

En lugar de especificar la linea final, puedes decir "ocupa N tracks":

```css
/* Estas dos lineas son equivalentes: */
grid-column: 1 / 4;
grid-column: 1 / span 3;   /* "empieza en 1, ocupa 3 columnas" */

/* Tambien puedes omitir el inicio: */
grid-column: span 3;       /* "ocupa 3 columnas desde donde me toque" */
```

### 4.3 Shorthand `grid-column` y `grid-row`

```css
/* Forma larga: */
grid-column-start: 1;
grid-column-end: 4;

/* Shorthand equivalente: */
grid-column: 1 / 4;

/* Forma larga filas: */
grid-row-start: 1;
grid-row-end: 3;

/* Shorthand equivalente: */
grid-row: 1 / 3;
```

### 4.4 `grid-area` shorthand

Combina fila y columna en una sola declaracion:

```css
/* grid-area: fila-inicio / col-inicio / fila-fin / col-fin */
grid-area: 1 / 1 / 3 / 4;

/* Equivale a: */
grid-row: 1 / 3;
grid-column: 1 / 4;
```

**Mnemotecnia:** El orden es como las agujas del reloj empezando arriba:
**arriba / izquierda / abajo / derecha** (fila-inicio / col-inicio / fila-fin / col-fin).

### 4.5 Areas con nombre: `grid-template-areas`

Este es el enfoque mas visual para definir layouts. Se usa "arte ASCII" directamente
en el CSS:

```css
.contenedor {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  grid-template-rows: auto 1fr auto;
  grid-template-areas:
    "header  header  header"
    "sidebar main    main"
    "footer  footer  footer";
}

.mi-header  { grid-area: header;  }
.mi-sidebar { grid-area: sidebar; }
.mi-main    { grid-area: main;    }
.mi-footer  { grid-area: footer;  }
```

```
  ┌─────────────────────────────────┐
  │           header                │
  ├──────────┬──────────────────────┤
  │          │                      │
  │ sidebar  │       main           │
  │          │                      │
  ├──────────┴──────────────────────┤
  │           footer                │
  └─────────────────────────────────┘
```

**Reglas de `grid-template-areas`:**
- Cada cadena entre comillas es una fila
- Los nombres se separan con espacios
- Un nombre repetido forma un area rectangular
- Un punto (`.`) indica una celda vacia
- Las areas deben ser **rectangulares** (no formas en L o T)

```css
/* Celda vacia con punto: */
grid-template-areas:
  "header header header"
  "sidebar . main"
  "footer footer footer";
```

---

## 5. Alineacion en Grid

CSS Grid tiene **6 propiedades de alineacion**. Entenderlas requiere distinguir
dos niveles: el grid completo dentro de su contenedor, y los items dentro de sus celdas.

### 5.1 Tabla completa de alineacion

| Propiedad          | Eje         | Se aplica a...              | Afecta a...                    |
|--------------------|-------------|-----------------------------|--------------------------------|
| `justify-items`    | Horizontal  | Contenedor                  | Todos los items (en su celda)  |
| `align-items`      | Vertical    | Contenedor                  | Todos los items (en su celda)  |
| `place-items`      | Ambos       | Contenedor (shorthand)      | Todos los items (en su celda)  |
| `justify-content`  | Horizontal  | Contenedor                  | El grid completo               |
| `align-content`    | Vertical    | Contenedor                  | El grid completo               |
| `place-content`    | Ambos       | Contenedor (shorthand)      | El grid completo               |
| `justify-self`     | Horizontal  | Item individual             | Solo ESE item (en su celda)    |
| `align-self`       | Vertical    | Item individual             | Solo ESE item (en su celda)    |
| `place-self`       | Ambos       | Item individual (shorthand) | Solo ESE item (en su celda)    |

### 5.2 Valores posibles

```
  justify-items / align-items / justify-self / align-self:
  ┌───────────┬────────────────────────────────────────────┐
  │ start     │ Alinea al inicio del area                  │
  │ end       │ Alinea al final del area                   │
  │ center    │ Centra dentro del area                     │
  │ stretch   │ Estira para llenar el area (por defecto)   │
  └───────────┴────────────────────────────────────────────┘

  justify-content / align-content:
  ┌───────────────┬─────────────────────────────────────────┐
  │ start         │ Grid al inicio del contenedor           │
  │ end           │ Grid al final del contenedor            │
  │ center        │ Grid centrado en el contenedor          │
  │ stretch       │ Tracks se estiran (por defecto)         │
  │ space-between │ Espacio igual ENTRE tracks              │
  │ space-around  │ Espacio igual ALREDEDOR de cada track   │
  │ space-evenly  │ Espacio IDENTICO entre y alrededor      │
  └───────────────┴─────────────────────────────────────────┘
```

### 5.3 Alineacion visual: `justify-items`

```
  justify-items: start         justify-items: center        justify-items: end
  ┌──────────────────┐         ┌──────────────────┐         ┌──────────────────┐
  │▓▓▓               │         │     ▓▓▓          │         │            ▓▓▓   │
  ├──────────────────┤         ├──────────────────┤         ├──────────────────┤
  │▓▓▓▓▓             │         │    ▓▓▓▓▓         │         │         ▓▓▓▓▓   │
  └──────────────────┘         └──────────────────┘         └──────────────────┘
  (items pegados a la izq.)    (items centrados)            (items pegados a la der.)
```

### 5.4 Alineacion visual: `align-items`

```
  align-items: start     align-items: center    align-items: end
  ┌──────┐               ┌──────┐               ┌──────┐
  │▓▓▓▓▓▓│               │      │               │      │
  │      │               │▓▓▓▓▓▓│               │      │
  │      │               │      │               │▓▓▓▓▓▓│
  └──────┘               └──────┘               └──────┘
```

### 5.5 Shorthand `place-items` y `place-content`

```css
/* place-items: align-items  justify-items */
place-items: center start;

/* Equivale a: */
align-items: center;
justify-items: start;

/* Si solo se da un valor, aplica a ambos ejes: */
place-items: center;
/* Equivale a: align-items: center; justify-items: center; */
```

---

## 6. Grid + Flexbox: el patron combinado

### Como se combinan en ESTE ejercicio

Nuestro `styles.css` demuestra un patron profesional muy comun: usar Grid y
Flexbox juntos, cada uno para lo que mejor sabe hacer.

```
  PAGINA COMPLETA (Flexbox en .contenedor)
  ┌────────────────────────────────────────────────────────┐
  │  .contenedor { display: flex; flex-wrap: wrap; }       │
  │                                                        │
  │  ┌──────────────────────────────┬────────────────────┐ │
  │  │  <section>                   │  <aside>           │ │
  │  │  flex: 1 1 66.66%            │  flex: 1 1 33.33%  │ │
  │  │                              │                    │ │
  │  │  ┌──────────────────────┐    │                    │ │
  │  │  │  FORMULARIO          │    │                    │ │
  │  │  │  (Grid en .grid)     │    │                    │ │
  │  │  │                      │    │                    │ │
  │  │  │  ┌────────┬────────┐ │    │                    │ │
  │  │  │  │nombre  │ correo │ │    │                    │ │
  │  │  │  ├─────┬──┴────────┤ │    │                    │ │
  │  │  │  │proc.│  sabor    │ │    │                    │ │
  │  │  │  └─────┴───────────┘ │    │                    │ │
  │  │  └──────────────────────┘    │                    │ │
  │  └──────────────────────────────┴────────────────────┘ │
  └────────────────────────────────────────────────────────┘
```

### Por que esta combinacion es correcta

| Componente     | Sistema usado | Razon                                            |
|----------------|---------------|--------------------------------------------------|
| `.contenedor`  | **Flexbox**   | Solo necesita distribuir section + aside en 1 eje |
| `.grid`        | **CSS Grid**  | Necesita alinear campos en filas Y columnas       |
| `.campo`       | **Flexbox**   | Apila label + input en columna (1 eje vertical)   |

### El patron "Item Grid + Contenedor Flex"

Un mismo elemento puede ser **item de grid** Y **contenedor flex** simultaneamente:

```css
/* .campo es un ITEM del grid (.grid) */
/* Y al mismo tiempo es un CONTENEDOR flex para su label + input */
.campo {
  display: flex;           /* Contenedor flex */
  flex-direction: column;  /* Label arriba, input abajo */
  padding: 0 5px;
}
```

```
  .grid (display: grid)
  ┌─────────────────────────┬─────────────────────────┐
  │ .campo (grid item       │ .campo (grid item       │
  │    + flex container)    │    + flex container)    │
  │ ┌─────────────────────┐ │ ┌─────────────────────┐ │
  │ │ <label>  ← flex item│ │ │ <label>  ← flex item│ │
  │ ├─────────────────────┤ │ ├─────────────────────┤ │
  │ │ <input>  ← flex item│ │ │ <input>  ← flex item│ │
  │ └─────────────────────┘ │ └─────────────────────┘ │
  └─────────────────────────┴─────────────────────────┘
```

### Patrones reales que combinan Grid + Flexbox

```
  1. DASHBOARD
     Grid: layout general (sidebar + header + contenido + widgets)
     Flexbox: barra de navegacion, grupo de botones, tarjetas internas

  2. E-COMMERCE
     Grid: cuadricula de productos (3x4, 4x3, etc.)
     Flexbox: cada tarjeta de producto (imagen + titulo + precio + boton)

  3. FORMULARIO (como nuestro ejercicio)
     Grid: distribucion de campos en filas y columnas
     Flexbox: cada campo individual (label + input)

  4. BLOG
     Grid: layout de la pagina (contenido + sidebar)
     Flexbox: lista de articulos, barra de categorias, paginacion
```

---

## 7. Grid implicito vs explicito

### 7.1 Grid explicito

El grid **explicito** es el que TU defines con `grid-template-columns` y
`grid-template-rows`. Tienes control total sobre el.

```css
.grid {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;  /* 3 columnas explicitas */
  grid-template-rows: 100px 100px;      /* 2 filas explicitas */
}
```

```
  Grid EXPLICITO (3 columnas x 2 filas = 6 celdas):
  ┌─────┬─────┬─────┐
  │  1  │  2  │  3  │  100px
  ├─────┼─────┼─────┤
  │  4  │  5  │  6  │  100px
  └─────┴─────┴─────┘
```

### 7.2 Grid implicito

Pero que pasa si tienes **mas items** de los que caben en el grid explicito?
CSS Grid crea filas (o columnas) **adicionales automaticamente**. Esas filas
extra son el grid **implicito**.

```
  Grid con 3 columnas x 2 filas, pero 9 items:
  ┌─────┬─────┬─────┐
  │  1  │  2  │  3  │  100px (explicito)
  ├─────┼─────┼─────┤
  │  4  │  5  │  6  │  100px (explicito)
  ├─────┼─────┼─────┤
  │  7  │  8  │  9  │  auto  (IMPLICITO — creado automaticamente)
  └─────┴─────┴─────┘
```

### 7.3 Controlando el grid implicito

```css
/* Tamanio de las filas implicitas (las que se crean automaticamente) */
grid-auto-rows: 150px;

/* Tamanio de las columnas implicitas */
grid-auto-columns: 100px;

/* Direccion del flujo automatico */
grid-auto-flow: row;      /* Por defecto: llena filas de izq a der */
grid-auto-flow: column;   /* Llena columnas de arriba a abajo */
grid-auto-flow: dense;    /* Rellena huecos (empaquetado denso) */
```

### 7.4 `grid-auto-flow: dense`

Cuando hay items de diferentes tamanios, pueden quedar **huecos** en el grid.
`dense` intenta rellenar esos huecos con items mas pequenos.

```
  grid-auto-flow: row (normal):     grid-auto-flow: dense:
  ┌──────────┬─────┬─────┐          ┌──────────┬─────┬─────┐
  │  A (2col)│  B  │  C  │          │  A (2col)│  B  │  C  │
  ├──────────┼─────┴─────┤          ├──────────┼─────┼─────┤
  │  D (2col)│           │          │  D (2col)│  F  │  G  │
  ├─────┬────┴─────┬─────┤          ├─────┬────┴─────┴─────┤
  │     │  E (2col)│     │          │  E  │   E (2col)     │
  ├─────┴──────────┼─────┤          └─────┴────────────────┘
  │  F  │  G       │     │
  └─────┴──────────┴─────┘          F y G "rellenaron" el hueco
       ↑
  Hueco vacio
```

**Precaucion:** `dense` cambia el orden visual de los items, lo que puede causar
problemas de accesibilidad si el orden de lectura importa.

---

## 8. Patrones Grid responsivos

### 8.1 El patron auto-fill + minmax (sin media queries)

Este es el patron **mas poderoso** de CSS Grid para layouts responsivos.
No necesita ni una sola media query:

```css
.galeria {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 1rem;
}
```

```
  Pantalla ancha (1200px):
  ┌──────┬──────┬──────┬──────┐
  │  A   │  B   │  C   │  D   │   4 columnas de ~300px
  └──────┴──────┴──────┴──────┘

  Pantalla mediana (800px):
  ┌─────────┬─────────┬─────────┐
  │    A    │    B    │    C    │   3 columnas de ~266px
  ├─────────┼─────────┼─────────┤
  │    D    │         │         │
  └─────────┴─────────┴─────────┘

  Pantalla pequena (550px):
  ┌──────────────┬──────────────┐
  │      A       │      B       │   2 columnas de ~275px
  ├──────────────┼──────────────┤
  │      C       │      D       │
  └──────────────┴──────────────┘

  Pantalla movil (350px):
  ┌────────────────────────────┐
  │             A              │   1 columna de ~350px
  ├────────────────────────────┤
  │             B              │
  ├────────────────────────────┤
  │             C              │
  ├────────────────────────────┤
  │             D              │
  └────────────────────────────┘
```

**Como funciona:**
1. `auto-fill` crea tantas columnas como quepan
2. `minmax(250px, 1fr)` dice: cada columna mide al menos 250px y como maximo 1fr
3. Cuando no caben 2 columnas de 250px, se reduce a 1 columna

### 8.2 Grid con media queries (control preciso)

En nuestro ejercicio usamos media queries porque necesitamos control exacto
sobre que campos van en que columnas:

```css
/* Movil: sin grid-template-columns definido = 1 columna */
.grid {
  display: grid;
  row-gap: 10px;
}

/* Desktop: cuadricula de 6 columnas con posiciones exactas */
@media (min-width: 798px) {
  .grid {
    grid-template-columns: repeat(6, 16.66%);
  }
  .nombre  { grid-column: 1 / 4; }
  .correo  { grid-column: 4 / 7; }
  .procede { grid-column: 1 / 3; }
  .sabor   { grid-column: 3 / 7; }
}
```

### 8.3 El concepto del sistema de 12 columnas

Muchos frameworks CSS (Bootstrap, Foundation) usan un grid de 12 columnas.
12 es un numero magico porque se divide exactamente por 1, 2, 3, 4, 6 y 12.

```css
.layout-12-cols {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  gap: 1rem;
}
```

```
  12 columnas = flexibilidad maxima:

  1 elemento de 12 cols:   ┌────────────────────────────────────────────────┐
                           └────────────────────────────────────────────────┘

  2 elementos de 6 cols:   ┌───────────────────────┬────────────────────────┐
                           └───────────────────────┴────────────────────────┘

  3 elementos de 4 cols:   ┌───────────────┬───────────────┬────────────────┐
                           └───────────────┴───────────────┴────────────────┘

  4 elementos de 3 cols:   ┌──────────┬───────────┬──────────┬──────────────┐
                           └──────────┴───────────┴──────────┴──────────────┘

  8 + 4 cols:              ┌──────────────────────────────────┬──────────────┐
                           └──────────────────────────────────┴──────────────┘

  3 + 6 + 3 cols:          ┌────────┬────────────────────────┬──────────────┐
                           └────────┴────────────────────────┴──────────────┘
```

Con CSS Grid puedes crear tu propio sistema de 12 columnas sin frameworks:

```css
.col-1  { grid-column: span 1;  }
.col-2  { grid-column: span 2;  }
.col-3  { grid-column: span 3;  }
.col-4  { grid-column: span 4;  }
.col-6  { grid-column: span 6;  }
.col-8  { grid-column: span 8;  }
.col-12 { grid-column: span 12; }
```

---

## 9. Errores comunes

### Error 1: Confundir LINEAS con TRACKS

```
  ¡ Los numeros en grid-column son LINEAS, no columnas !

  INCORRECTO (pensamiento):
  "grid-column: 1 / 3 ocupa las columnas 1, 2 y 3" ← MAL

  CORRECTO (pensamiento):
  "grid-column: 1 / 3 va de la LINEA 1 a la LINEA 3" = 2 columnas

  Lineas:  1     2     3
           │     │     │
           │col 1│col 2│   ← Solo 2 tracks (columnas), NO 3
           │     │     │

  Para ocupar 3 columnas: grid-column: 1 / 4  (linea 1 a linea 4)
```

### Error 2: Items que no son hijos directos

```css
/* PROBLEMA: */
<div class="grid">
  <div class="wrapper">        <!-- Este es el item grid -->
    <div class="campo">...</div>  <!-- Este NO es item grid -->
  </div>
</div>

/* Solo los hijos DIRECTOS del contenedor grid son items grid */
/* Por eso en nuestro ejercicio, los .campo son hijos directos de .grid */
```

### Error 3: Usar Grid cuando Flexbox es mas simple

```css
/* EXCESIVO — solo centrar un elemento: */
.contenedor {
  display: grid;
  place-items: center;   /* Funciona, pero... */
}

/* MEJOR — Flexbox es mas intuitivo para esto: */
.contenedor {
  display: flex;
  justify-content: center;
  align-items: center;
}
```

**Regla practica:** Si solo necesitas alinear items en un eje, usa Flexbox.
Si necesitas controlar filas Y columnas, usa Grid.

### Error 4: Porcentajes + gap = desbordamiento

```css
/* PROBLEMA: */
.grid {
  display: grid;
  grid-template-columns: 50% 50%;   /* 100% del ancho */
  gap: 20px;                         /* + 20px de gap */
  /* Total: 100% + 20px = DESBORDAMIENTO horizontal */
}

/* SOLUCION 1: Usar fr */
grid-template-columns: 1fr 1fr;      /* fr descuenta el gap automaticamente */

/* SOLUCION 2: Usar calc */
grid-template-columns: calc(50% - 10px) calc(50% - 10px);
```

Nuestro ejercicio tiene este riesgo potencial con `repeat(6, 16.66%)`.
Si se agrega `column-gap`, habra desbordamiento. La solucion seria cambiar a
`repeat(6, 1fr)`.

### Error 5: Olvidar la respuesta movil

```css
/* PROBLEMA: definir solo la cuadricula desktop */
.grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  /* En movil, 4 columnas estrechas = ilegible */
}

/* SOLUCION: mobile-first */
.grid {
  display: grid;
  /* Movil: sin columnas = 1 sola columna */
}

@media (min-width: 768px) {
  .grid {
    grid-template-columns: repeat(4, 1fr);
  }
}
```

### Error 6: areas no rectangulares

```css
/* INVALIDO — el area "header" forma una L: */
grid-template-areas:
  "header header sidebar"
  "header main   main";   /* ERROR: header no es rectangular */

/* VALIDO: */
grid-template-areas:
  "header header header"
  "sidebar main  main";
```

---

## 10. Grid vs Flexbox: Guia de decision completa

### Diagrama de decision detallado

```
  ¿Que tipo de layout necesitas?
  │
  ├── "Necesito organizar elementos en UNA fila o UNA columna"
  │    └── Usa FLEXBOX
  │         Ejemplos:
  │         - Barra de navegacion horizontal
  │         - Lista de botones
  │         - Centrar un elemento
  │         - Apilar tarjetas en columna
  │
  ├── "Necesito una CUADRICULA con filas Y columnas"
  │    └── Usa CSS GRID
  │         Ejemplos:
  │         - Formulario con campos alineados
  │         - Galeria de imagenes
  │         - Dashboard con widgets
  │         - Layout de pagina (header/main/sidebar/footer)
  │
  ├── "Necesito que los items se ajusten automaticamente al espacio"
  │    └── Usa FLEXBOX (flex-wrap: wrap)
  │         Ejemplos:
  │         - Tags/etiquetas que saltan de linea
  │         - Galeria simple sin control de filas
  │
  ├── "Necesito un layout responsivo SIN media queries"
  │    └── Usa CSS GRID (auto-fill + minmax)
  │         grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  │
  └── "Necesito ambas cosas"
       └── Usa GRID para el layout general y FLEXBOX para los componentes
           Ejemplo: nuestro ejercicio 07
```

### Tabla comparativa completa

| Caracteristica                 | Flexbox                        | CSS Grid                          |
|-------------------------------|--------------------------------|-----------------------------------|
| Dimensiones                   | 1D (fila O columna)           | 2D (filas Y columnas)            |
| Eje principal                 | Lo defines tu (row/column)    | Siempre ambos ejes               |
| Control del layout            | Desde los ITEMS (flex-grow)   | Desde el CONTENEDOR (template)   |
| Posicionamiento               | Relativo al flujo             | Exacto (numeros de linea/areas)  |
| Alineacion                    | Excelente en 1 eje            | Excelente en ambos ejes          |
| Espaciado (gap)               | Soportado (gap)               | Soportado (gap, row-gap, col-gap)|
| Wrap                          | flex-wrap: wrap                | Implicito o auto-fill/auto-fit   |
| Sobreposicion de items        | No                             | Si (items pueden solaparse)      |
| Areas con nombre              | No                             | Si (grid-template-areas)         |
| Orden visual                  | order                          | grid-column/row, order           |
| Mejor para...                 | Componentes, alineacion        | Layouts de pagina, cuadriculas   |
| Soporte navegadores           | Excelente (IE10+)             | Excelente (IE no soporta bien)   |

### Cuando usar ambos juntos

```
  GRID para la estructura macro:
  ┌───────────────────────────────────────┐
  │  HEADER (grid-area: header)           │
  ├────────────┬──────────────────────────┤
  │  SIDEBAR   │  CONTENIDO PRINCIPAL     │
  │            │                          │
  │  (Flexbox  │  ┌────┬────┬────┬────┐  │
  │   para los │  │Card│Card│Card│Card│  │  ← FLEXBOX para
  │   links    │  │    │    │    │    │  │    las tarjetas
  │   del menu)│  └────┴────┴────┴────┘  │
  │            │                          │
  ├────────────┴──────────────────────────┤
  │  FOOTER (grid-area: footer)           │
  └───────────────────────────────────────┘
```

---

## 11. Ejercicios de practica

Los siguientes ejercicios estan pensados para practicar con los archivos
`index.html` y `styles.css` de esta misma carpeta (modulo 07).

### Ejercicio 1 — Convertir porcentajes a fr

**Objetivo:** Eliminar el riesgo de desbordamiento.

Abre `styles.css` y busca la linea:
```css
grid-template-columns: repeat(6, 16.66%);
```

Cambiala por:
```css
grid-template-columns: repeat(6, 1fr);
```

Luego agrega `column-gap: 10px;` a `.grid` y verifica que **no hay
desbordamiento horizontal**. Con porcentajes, habria desbordamiento.

---

### Ejercicio 2 — Agregar una tercera fila al formulario

**Objetivo:** Practicar el posicionamiento con grid-column.

1. En `index.html`, agrega un nuevo campo dentro del `<fieldset class="grid">`:
   ```html
   <div class="campo comentario">
     <label for="comentario">Comentarios:</label>
     <textarea id="comentario" rows="4"></textarea>
   </div>
   ```

2. En `styles.css`, dentro del media query de desktop, agrega:
   ```css
   .comentario {
     grid-column: 1 / 7;   /* Ocupa las 6 columnas completas */
   }
   ```

3. Verifica que en movil el textarea se apila como los demas campos, y en
   desktop ocupa todo el ancho del formulario.

---

### Ejercicio 3 — Usar grid-template-areas

**Objetivo:** Practicar la sintaxis de areas con nombre.

Reescribe la media query de desktop para usar `grid-template-areas`:

```css
@media (min-width: 798px) {
  .grid {
    grid-template-columns: repeat(6, 1fr);
    grid-template-areas:
      "nombre nombre nombre correo correo correo"
      "procede procede sabor sabor  sabor  sabor";
  }
  .nombre  { grid-area: nombre;  }
  .correo  { grid-area: correo;  }
  .procede { grid-area: procede; }
  .sabor   { grid-area: sabor;   }
}
```

Compara el resultado visual: debe ser identico al original.

---

### Ejercicio 4 — Grid responsivo sin media queries

**Objetivo:** Practicar el patron auto-fill + minmax.

Crea una pequena galeria debajo del formulario:

1. En `index.html`, agrega despues del `</form>`:
   ```html
   <div class="galeria">
     <div class="galeria-item">Imagen 1</div>
     <div class="galeria-item">Imagen 2</div>
     <div class="galeria-item">Imagen 3</div>
     <div class="galeria-item">Imagen 4</div>
     <div class="galeria-item">Imagen 5</div>
     <div class="galeria-item">Imagen 6</div>
   </div>
   ```

2. En `styles.css`, agrega (fuera de media queries):
   ```css
   .galeria {
     display: grid;
     grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
     gap: 10px;
     margin-top: 1rem;
   }
   .galeria-item {
     background: var(--azulclaro);
     color: var(--azulmarino);
     padding: 2rem;
     text-align: center;
     border-radius: 8px;
   }
   ```

3. Redimensiona el navegador y observa como las columnas se ajustan solas.

---

### Ejercicio 5 — Diagnostico de grid en DevTools

**Objetivo:** Aprender a usar las herramientas de desarrollador.

1. Abre `index.html` en Chrome o Firefox
2. Abre DevTools (F12 o Ctrl+Shift+I)
3. En el panel Elements, busca el `<fieldset class="grid">`
4. Haz clic en el badge `grid` que aparece junto al elemento
5. Activa la superposicion de grid (Grid overlay)
6. Identifica visualmente:
   - Las 7 lineas de columna (numeradas del 1 al 7)
   - Los 6 tracks de columna
   - Las celdas que ocupa cada `.campo`
   - Los gaps entre filas

---

### Ejercicio 6 — Layout de pagina completo con Grid

**Objetivo:** Crear un layout clasico header/nav/main/aside/footer con Grid.

```
  ┌──────────────────────────────────┐
  │           HEADER                 │
  ├──────────────────────────────────┤
  │             NAV                  │
  ├───────────┬──────────────────────┤
  │           │                      │
  │  ASIDE    │       MAIN           │
  │           │                      │
  ├───────────┴──────────────────────┤
  │           FOOTER                 │
  └──────────────────────────────────┘
```

Escribe el CSS usando `grid-template-areas`:

```css
body {
  display: grid;
  grid-template-columns: 200px 1fr;
  grid-template-rows: auto auto 1fr auto;
  grid-template-areas:
    "header  header"
    "nav     nav"
    "aside   main"
    "footer  footer";
  min-height: 100vh;
}
```

Asigna cada seccion a su area y observa el resultado.

---

### Ejercicio 7 — Breakpoint movil del grid

**Objetivo:** Entender el comportamiento mobile-first del grid.

1. Abre `styles.css` y observa que `.grid` en su estado base (sin media query)
   NO define `grid-template-columns`
2. Abre la pagina en un navegador y usa DevTools para emular un dispositivo movil
3. Responde:
   - ¿Cuantas columnas tiene el grid en movil? (Respuesta: 1)
   - ¿Por que los campos se apilan verticalmente?
   - ¿Que pasaria si agregaras `grid-template-columns: 1fr` al grid base?

---

**Siguiente modulo:** [08 - Proyecto Web de Servicios](../08-proyecto-web-servicios/)
donde integraremos todo lo aprendido en los modulos 01-07 para crear un sitio web
completo y profesional.

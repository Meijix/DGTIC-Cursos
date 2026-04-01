# Modulo 04 — Flexbox: El Sistema de Layout Unidimensional

> **Archivo de referencia del ejercicio:** `dados.html` y `dados.css` en esta misma carpeta.
> **Prerequisitos:** Modulos 01 (HTML), 02 (CSS basico) y 03 (pagina web basica).

---

## Indice

1. [Que problema resuelve Flexbox](#1-que-problema-resuelve-flexbox)
2. [El modelo mental: Container y Items](#2-el-modelo-mental-container-y-items)
3. [Ejes: Main Axis y Cross Axis](#3-ejes-main-axis-y-cross-axis)
4. [justify-content (Main Axis)](#4-justify-content-main-axis)
5. [align-items (Cross Axis)](#5-align-items-cross-axis)
6. [align-self](#6-align-self)
7. [flex-wrap y multi-linea](#7-flex-wrap-y-multi-linea)
8. [El shorthand flex](#8-el-shorthand-flex)
9. [gap](#9-gap)
10. [Flexbox aplicado: el ejercicio de dados](#10-flexbox-aplicado-el-ejercicio-de-dados)
11. [Errores comunes](#11-errores-comunes)
12. [Ejercicios de practica](#12-ejercicios-de-practica)

---

## 1. Que problema resuelve Flexbox

Antes de Flexbox (introducido en CSS3, ampliamente soportado desde ~2015),
los desarrolladores dependian de tecnicas que eran **hacks** para posicionar
elementos. Cada una tenia problemas serios:

### Tecnicas pre-Flexbox y sus limitaciones

```
TECNICA           | COMO FUNCIONA                | PROBLEMA
------------------|------------------------------|----------------------------------
float: left/right | Saca el elemento del flujo   | Requiere "clearfix" para que el
                  | normal y lo empuja a un lado  | padre no colapse. No centra
                  |                              | verticalmente. Pensado para
                  |                              | texto alrededor de imagenes,
                  |                              | NO para layouts.
------------------|------------------------------|----------------------------------
display:          | Coloca los elementos como si | Espacios en blanco del HTML
inline-block      | fueran palabras de texto en  | generan huecos fantasma entre
                  | una misma linea              | elementos. No distribuye
                  |                              | espacio sobrante.
------------------|------------------------------|----------------------------------
display: table /  | Simula el comportamiento de  | Semanticamente incorrecto
table-cell        | tablas HTML                  | (no son datos tabulares).
                  |                              | Dificil de hacer responsivo.
                  |                              | Inflexible para reordenar.
------------------|------------------------------|----------------------------------
position:         | Coloca elementos con         | Saca los elementos del flujo.
absolute          | coordenadas exactas          | Los demas elementos no saben
                  |                              | que existe. Fragil al cambiar
                  |                              | tamanos de pantalla.
```

### Lo que Flexbox resuelve

Flexbox distribuye espacio y alinea elementos a lo largo de **UN eje**
(fila o columna) de forma predecible y flexible:

```
  Sin Flexbox (floats):                  Con Flexbox:
  +------+ +------+ +------+            +------+ +------+ +------+
  | Item | | Item | | Item |            | Item | | Item | | Item |
  +------+ +------+ +------+            +------+ +------+ +------+
  ^ Requiere clearfix                    ^ Solo display: flex
  ^ Margenes dobles en IE                ^ Espacio se distribuye solo
  ^ No centra verticalmente              ^ Centra en ambos ejes
  ^ Colapsa el contenedor padre          ^ El padre envuelve los hijos
```

**Regla de oro:** Flexbox es para distribuir elementos en **una dimension**
(fila O columna). Para layouts en **dos dimensiones** (filas Y columnas
a la vez), se usa CSS Grid (modulo 07).

---

## 2. El modelo mental: Container y Items

Flexbox se basa en una relacion **padre-hijo** con dos roles:

```
  +================================================================+
  |  CONTENEDOR FLEX (padre)          display: flex                 |
  |  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  |
  |                                                                |
  |   +----------+    +----------+    +----------+    +----------+ |
  |   |  ITEM 1  |    |  ITEM 2  |    |  ITEM 3  |    |  ITEM 4  | |
  |   | (hijo    |    | (hijo    |    | (hijo    |    | (hijo    | |
  |   | directo) |    | directo) |    | directo) |    | directo) | |
  |   +----------+    +----------+    +----------+    +----------+ |
  |                                                                |
  +================================================================+

  IMPORTANTE: Solo los hijos DIRECTOS son items flex.
  Los nietos NO se ven afectados (a menos que su padre
  tambien tenga display: flex).
```

### En el ejercicio de dados (`dados.css`):

Hay **dos niveles** de Flexbox anidados:

```
  .contenedor (display: flex)      <-- NIVEL 1: organiza las caras
  |
  +-- .cara1 (display: flex)       <-- NIVEL 2: organiza los puntos
  |   +-- .punto
  |
  +-- .cara2 (display: flex)
  |   +-- .punto
  |   +-- .punto
  |
  +-- .cara3 (display: flex)
  |   +-- .punto
  |   +-- .punto
  |   +-- .punto
  |
  +-- .cara4 ...
  +-- .cara5 ...
  +-- .cara6 ...
```

### Tabla completa: propiedades del CONTENEDOR flex

```
  PROPIEDAD          | VALORES                          | QUE HACE
  -------------------|----------------------------------|------------------------------
  display            | flex | inline-flex               | Activa Flexbox en el
                     |                                  | contenedor. inline-flex es
                     |                                  | como inline-block pero flex.
  -------------------|----------------------------------|------------------------------
  flex-direction     | row | row-reverse |              | Define la DIRECCION del eje
                     | column | column-reverse          | principal.
  -------------------|----------------------------------|------------------------------
  flex-wrap          | nowrap | wrap | wrap-reverse     | Permite o impide saltos de
                     |                                  | linea cuando los items no
                     |                                  | caben.
  -------------------|----------------------------------|------------------------------
  flex-flow          | <direction> <wrap>               | Shorthand que combina
                     | Ej: row wrap                     | flex-direction + flex-wrap.
  -------------------|----------------------------------|------------------------------
  justify-content    | flex-start | flex-end | center   | Distribuye el espacio
                     | space-between | space-around     | SOBRANTE en el eje
                     | space-evenly                     | PRINCIPAL.
  -------------------|----------------------------------|------------------------------
  align-items        | stretch | flex-start | flex-end  | Alinea los items en el eje
                     | center | baseline               | CRUZADO (perpendicular).
  -------------------|----------------------------------|------------------------------
  align-content      | stretch | flex-start | flex-end  | Distribuye las LINEAS (filas
                     | center | space-between |         | o columnas) en el eje
                     | space-around | space-evenly      | cruzado. Solo funciona con
                     |                                  | flex-wrap: wrap y multiples
                     |                                  | lineas.
  -------------------|----------------------------------|------------------------------
  gap                | <row-gap> <column-gap>           | Espacio ENTRE items (no en
                     | Ej: 10px, 10px 20px              | los bordes externos).
  -------------------|----------------------------------|------------------------------
  row-gap            | <longitud>                       | Espacio entre filas.
  column-gap         | <longitud>                       | Espacio entre columnas.
```

### Tabla completa: propiedades de cada ITEM flex

```
  PROPIEDAD     | VALORES                     | QUE HACE
  --------------|-----------------------------|-----------------------------------------
  order         | <numero> (defecto: 0)       | Cambia el orden visual del item
                |                             | sin alterar el HTML. Menor numero
                |                             | = aparece primero.
  --------------|-----------------------------|-----------------------------------------
  flex-grow     | <numero> (defecto: 0)       | Cuanto del espacio SOBRANTE absorbe
                |                             | este item. 0 = no crece.
  --------------|-----------------------------|-----------------------------------------
  flex-shrink   | <numero> (defecto: 1)       | Cuanto se ENCOGE este item cuando no
                |                             | hay espacio. 0 = no se encoge.
  --------------|-----------------------------|-----------------------------------------
  flex-basis    | <longitud> | auto | content | Tamano INICIAL del item antes de que
                | (defecto: auto)             | se apliquen grow/shrink. Funciona
                |                             | como width (en row) o height (en
                |                             | column), pero respeta el eje flex.
  --------------|-----------------------------|-----------------------------------------
  flex          | <grow> <shrink> <basis>     | Shorthand. flex: 1 = flex: 1 1 0%.
                | Ej: 1 1 200px              | flex: auto = flex: 1 1 auto.
                |                             | flex: none = flex: 0 0 auto.
  --------------|-----------------------------|-----------------------------------------
  align-self    | auto | flex-start | flex-end| SOBREESCRIBE align-items del padre
                | center | stretch | baseline | para ESTE item en particular.
```

---

## 3. Ejes: Main Axis y Cross Axis

Flexbox tiene **dos ejes** que cambian segun `flex-direction`:

### flex-direction: row (valor por defecto)

```
      MAIN AXIS (eje principal)
      ─────────────────────────────────────────────────►

  |   +----------+    +----------+    +----------+
  |   |  Item 1  |    |  Item 2  |    |  Item 3  |
  |   +----------+    +----------+    +----------+
  |
  ▼  CROSS AXIS (eje cruzado)

  justify-content  -->  distribuye en la HORIZONTAL  -->
  align-items      -->  alinea en la VERTICAL        |
```

### flex-direction: row-reverse

```
                          MAIN AXIS (eje principal)
      ◄─────────────────────────────────────────────────

  |           +----------+    +----------+    +----------+
  |           |  Item 3  |    |  Item 2  |    |  Item 1  |
  |           +----------+    +----------+    +----------+
  |
  ▼  CROSS AXIS (eje cruzado)

  Los items se colocan de DERECHA a IZQUIERDA.
  flex-start = derecha, flex-end = izquierda.
```

### flex-direction: column

```
      CROSS AXIS (eje cruzado)
      ─────────────────────────────────────────────────►

  |   +---------------------------------------------+
  |   |                  Item 1                      |
  |   +---------------------------------------------+
  |   +---------------------------------------------+
  |   |                  Item 2                      |
  |   +---------------------------------------------+
  |   +---------------------------------------------+
  |   |                  Item 3                      |
  |   +---------------------------------------------+
  |
  ▼  MAIN AXIS (eje principal)

  justify-content  -->  distribuye en la VERTICAL    |
  align-items      -->  alinea en la HORIZONTAL      -->
```

### flex-direction: column-reverse

```
      CROSS AXIS (eje cruzado)
      ─────────────────────────────────────────────────►

  ▲
  |   +---------------------------------------------+
  |   |                  Item 3                      |
  |   +---------------------------------------------+
  |   +---------------------------------------------+
  |   |                  Item 2                      |
  |   +---------------------------------------------+
  |   +---------------------------------------------+
  |   |                  Item 1                      |
  |   +---------------------------------------------+

  MAIN AXIS (eje principal, hacia ARRIBA)

  Los items se apilan de ABAJO hacia ARRIBA.
  flex-start = abajo, flex-end = arriba.
```

### Tabla resumen de ejes

```
  flex-direction   | Main Axis      | Cross Axis     | justify = ?     | align = ?
  -----------------|----------------|----------------|-----------------|----------------
  row              | Horizontal ->  | Vertical   |   | Horizontal      | Vertical
  row-reverse      | Horizontal <-  | Vertical   |   | Horizontal      | Vertical
  column           | Vertical   |   | Horizontal ->  | Vertical        | Horizontal
  column-reverse   | Vertical   ^   | Horizontal ->  | Vertical        | Horizontal
```

**Mnemotecnia:** "**J**ustify = a lo largo del eje principal (Main).
**A**lign = perpendicular, en el eje cruzado (Cross)."

---

## 4. justify-content (Main Axis)

`justify-content` distribuye el **espacio sobrante** a lo largo del eje principal.
Solo tiene efecto cuando los items no llenan todo el contenedor.

En los diagramas siguientes, asumimos `flex-direction: row`:

### flex-start (valor por defecto)

```
  +-----------------------------------------------------+
  | [A]  [B]  [C]                                       |
  +-----------------------------------------------------+
    ^                    espacio sobrante ──────────────^
```

### flex-end

```
  +-----------------------------------------------------+
  |                                       [A]  [B]  [C] |
  +-----------------------------------------------------+
  ^──────────────── espacio sobrante        ^
```

### center

```
  +-----------------------------------------------------+
  |                  [A]  [B]  [C]                       |
  +-----------------------------------------------------+
       espacio            ^            espacio
       igual                           igual
```

### space-between

```
  +-----------------------------------------------------+
  | [A]                  [B]                  [C]        |
  +-----------------------------------------------------+
    ^                    ^                    ^
    | primer item        | espacio = espacio  | ultimo item
    | pegado al inicio                          pegado al final

  El espacio entre A y B es IGUAL al espacio entre B y C.
  NO hay espacio antes de A ni despues de C.
```

### space-around

```
  +-----------------------------------------------------+
  |    [A]          [B]          [C]    |
  +-----------------------------------------------------+
    ^       ^    ^       ^    ^       ^
   0.5x    1x  0.5x+0.5x=1x  0.5x+0.5x=1x   0.5x

  Cada item tiene espacio IGUAL a su alrededor.
  Pero los bordes reciben la MITAD del espacio que hay entre items.
  Espacio borde = 1/2 * espacio entre items.
```

### space-evenly

```
  +-----------------------------------------------------+
  |      [A]        [B]        [C]      |
  +-----------------------------------------------------+
    ^         ^   ^         ^   ^         ^
   1x        1x  1x        1x  1x        1x

  Espacio EXACTAMENTE IGUAL entre todos los items
  Y tambien en los bordes.
  Todos los espacios son identicos.
```

### Comparacion visual directa

```
  space-between:  |[A]        [B]        [C]|     bordes = 0
  space-around:   |  [A]    [B]    [C]  |         bordes = mitad
  space-evenly:   |   [A]   [B]   [C]   |         bordes = iguales
```

---

## 5. align-items (Cross Axis)

`align-items` controla la alineacion de los items en el **eje cruzado**.
En los diagramas, asumimos `flex-direction: row` (eje cruzado = vertical):

### stretch (valor por defecto)

```
  +-----------------------------------------------------+
  |                                                     |
  | +----------+    +----------+    +----------+        |
  | |          |    |          |    |          |        |
  | |  Item 1  |    |  Item 2  |    |  Item 3  |        |
  | |          |    |          |    |          |        |
  | +----------+    +----------+    +----------+        |
  |                                                     |
  +-----------------------------------------------------+

  Los items se ESTIRAN para llenar toda la altura
  del contenedor. (Solo funciona si los items NO
  tienen una altura explicita definida.)
```

### flex-start

```
  +-----------------------------------------------------+
  | +------+    +---------+    +----+                    |
  | |  A   |    |    B    |    | C  |                    |
  | +------+    +---------+    +----+                    |
  |                                                     |
  |                                                     |
  +-----------------------------------------------------+

  Los items se pegan al INICIO del eje cruzado (arriba).
  Cada item mantiene su altura natural.
```

### flex-end

```
  +-----------------------------------------------------+
  |                                                     |
  |                                                     |
  | +------+    +---------+    +----+                    |
  | |  A   |    |    B    |    | C  |                    |
  | +------+    +---------+    +----+                    |
  +-----------------------------------------------------+

  Los items se pegan al FINAL del eje cruzado (abajo).
```

### center

```
  +-----------------------------------------------------+
  |                                                     |
  | +------+    +---------+    +----+                    |
  | |  A   |    |    B    |    | C  |                    |
  | +------+    +---------+    +----+                    |
  |                                                     |
  +-----------------------------------------------------+

  Los items se centran verticalmente.
```

### baseline

```
  +-----------------------------------------------------+
  |                                                     |
  | +------+    +---------+    +----+                    |
  | | Hola |    |  Mundo  |    | !  |  <-- linea base   |
  | +------+    |         |    +----+      del texto    |
  |             +---------+                              |
  +-----------------------------------------------------+

  Los items se alinean segun la LINEA BASE de su texto.
  Util cuando los items tienen diferentes tamanos de fuente
  pero quieres que el texto quede en la misma linea visual.
```

---

## 6. align-self

`align-self` permite que **un item individual** tenga una alineacion
diferente a la definida por `align-items` en su contenedor padre.

```
  Contenedor con align-items: flex-start

  +-----------------------------------------------------+
  | +------+    +---------+    +------+                  |
  | |  A   |    |    B    |    |  C   |                  |
  | +------+    |         |    +------+                  |
  |             |  align- |                              |
  |             |  self:  |                              |
  |             |  center |                              |
  |             +---------+                              |
  |                                                     |
  +-----------------------------------------------------+

  A y C siguen align-items: flex-start (arriba).
  B usa align-self: center y se centra verticalmente.
```

### Valores de align-self

```
  auto       -> hereda el valor de align-items del padre (defecto)
  flex-start -> inicio del eje cruzado
  flex-end   -> final del eje cruzado
  center     -> centro del eje cruzado
  stretch    -> se estira para llenar el eje cruzado
  baseline   -> alineado a la linea base del texto
```

### Por que align-self es clave en los dados

En las caras 2 y 3 del dado, `align-self` permite que cada punto tenga
una posicion INDEPENDIENTE en el eje cruzado:

```
  Cara 2 (flex-direction: column, justify-content: space-between):

  +----------+
  | *        |  <- punto 1: align-self: flex-start (izquierda)
  |          |
  |        * |  <- punto 2: align-self: flex-end (derecha)
  +----------+

  Con column, el eje cruzado es HORIZONTAL.
  flex-start = izquierda, flex-end = derecha.


  Cara 3 (flex-direction: column, justify-content: space-between):

  +----------+
  | *        |  <- punto 1: align-self: flex-start
  |    *     |  <- punto 2: align-self: center
  |        * |  <- punto 3: align-self: flex-end
  +----------+
```

**No existe `justify-self` en Flexbox.** Para controlar un item individual
en el eje principal, se usan margenes auto (`margin-left: auto` para empujar
un item a la derecha, por ejemplo).

---

## 7. flex-wrap y multi-linea

### flex-wrap: nowrap (por defecto)

```
  Contenedor de 300px con 4 items de 100px:

  +--------------------------------------+
  | [75px] [75px] [75px] [75px]          |   <- Los items se ENCOGEN
  +--------------------------------------+       para caber en una linea.
                                                 Cada uno pasa de 100px a 75px.
```

### flex-wrap: wrap

```
  Contenedor de 300px con 4 items de 100px:

  +--------------------------------------+
  | [100px]  [100px]  [100px]            |   <- Linea 1: caben 3
  |                                      |
  | [100px]                              |   <- Linea 2: el 4to salta aqui
  +--------------------------------------+
```

### flex-wrap: wrap-reverse

```
  +--------------------------------------+
  | [100px]                              |   <- Linea 2 (arriba ahora)
  |                                      |
  | [100px]  [100px]  [100px]            |   <- Linea 1 (abajo ahora)
  +--------------------------------------+

  Las lineas se apilan en orden INVERSO.
```

### align-content vs align-items (multi-linea)

Cuando hay multiples lineas (con `flex-wrap: wrap`), aparecen dos
propiedades distintas para el eje cruzado:

```
  align-items:    alinea los items DENTRO de cada linea
  align-content:  distribuye las LINEAS COMPLETAS en el contenedor

  Ejemplo visual con flex-direction: row y dos lineas:

  align-items: center, align-content: flex-start
  +-----------------------------------------------------+
  | Linea 1:    [A]  [B]  [C]                           |
  | Linea 2:    [D]                                     |
  |                                                     |
  |                                                     |
  +-----------------------------------------------------+
  ^ Las lineas estan al inicio (align-content: flex-start)
  ^ Dentro de cada linea, los items estan centrados (align-items: center)


  align-items: center, align-content: center
  +-----------------------------------------------------+
  |                                                     |
  | Linea 1:    [A]  [B]  [C]                           |
  | Linea 2:    [D]                                     |
  |                                                     |
  +-----------------------------------------------------+
  ^ Las lineas estan centradas como grupo
```

**Regla:** `align-content` NO tiene efecto cuando hay una sola linea
de items (`flex-wrap: nowrap` o todos los items caben en una linea).

### En el ejercicio de dados

Las caras 4, 5 y 6 usan `flex-wrap: wrap` para distribuir los puntos
en multiples lineas/columnas:

```
  Cara 4: row + wrap + gap:40px     -> 4 puntos en 2 filas de 2
  Cara 5: row + wrap + gap:40px     -> 4 puntos + 1 absoluto
  Cara 6: column + wrap + gap:20px  -> 6 puntos en 2 columnas de 3
```

---

## 8. El shorthand flex

La propiedad `flex` combina tres propiedades en una:

```
  flex: <flex-grow> <flex-shrink> <flex-basis>;

  Ejemplo: flex: 1 1 200px;
           ^     ^ ^  ^
           |     | |  +-- flex-basis: 200px (tamano inicial)
           |     | +----- flex-shrink: 1 (puede encogerse)
           |     +------- (separador)
           +------------- flex-grow: 1 (puede crecer)
```

### flex-grow: como se reparte el espacio sobrante

```
  Contenedor: 600px
  Tres items con flex-basis: 100px cada uno.
  Espacio sobrante: 600 - 300 = 300px

  Caso 1: Todos con flex-grow: 1
  +------------------------------------------------------------------+
  | [----200px----]  [----200px----]  [----200px----]                 |
  +------------------------------------------------------------------+
  Cada item recibe: 300px / 3 = 100px extra -> 100 + 100 = 200px

  Caso 2: Item A = grow:2, B = grow:1, C = grow:1 (total = 4 partes)
  +------------------------------------------------------------------+
  | [------250px------]  [--175px--]  [--175px--]                    |
  +------------------------------------------------------------------+
  A recibe: 300 * (2/4) = 150px extra -> 100 + 150 = 250px
  B recibe: 300 * (1/4) = 75px extra  -> 100 + 75  = 175px
  C recibe: 300 * (1/4) = 75px extra  -> 100 + 75  = 175px
```

### flex-shrink: como se encogen los items

```
  Contenedor: 300px
  Tres items con flex-basis: 150px = necesitan 450px
  Deficit: 450 - 300 = 150px que hay que quitar

  Todos con flex-shrink: 1:
  +------------------------------------------+
  | [--100px--]  [--100px--]  [--100px--]    |
  +------------------------------------------+
  Cada item pierde: 150px / 3 = 50px -> 150 - 50 = 100px
```

### flex-basis vs width

```
  PROPIEDAD   | EN flex-direction: row  | EN flex-direction: column
  ------------|-------------------------|---------------------------
  flex-basis   | Actua como WIDTH       | Actua como HEIGHT
  width        | Siempre es WIDTH       | Siempre es WIDTH
  height       | Siempre es HEIGHT      | Siempre es HEIGHT

  flex-basis RESPETA el eje del contenedor flex.
  width/height son fijos independientemente del eje.

  Si defines AMBOS (flex-basis y width), flex-basis tiene prioridad
  (excepto cuando flex-basis es "auto", en cuyo caso usa width/height).
```

### Shorthands comunes

```
  SHORTHAND         | EQUIVALE A              | SIGNIFICADO
  ------------------|-------------------------|----------------------------------
  flex: 1           | flex: 1 1 0%            | Crece, se encoge, empieza en 0
                    |                         | (reparte espacio equitativamente)
  ------------------|-------------------------|----------------------------------
  flex: auto        | flex: 1 1 auto          | Crece, se encoge, empieza en su
                    |                         | tamano natural de contenido
  ------------------|-------------------------|----------------------------------
  flex: none        | flex: 0 0 auto          | NO crece, NO se encoge, tamano
                    |                         | fijo segun contenido
  ------------------|-------------------------|----------------------------------
  flex: 0 0 200px   | flex-grow: 0            | Tamano fijo de 200px, no cambia
                    | flex-shrink: 0          |
                    | flex-basis: 200px       |
  ------------------|-------------------------|----------------------------------
  flex: 1 1 280px   | (como en el modulo 05)  | Empieza en 280px, puede crecer
                    |                         | o encogerse segun el espacio
```

---

## 9. gap

`gap` define el espacio **entre** items flex, sin afectar los bordes
exteriores del contenedor.

### gap vs margin

```
  CON MARGIN (forma antigua):

  +-----------------------------------------------------------+
  |  +--+  +--+  +--+  +--+  +--+                            |
  | m|  |m m|  |m m|  |m m|  |m m|  |m                       |
  |  +--+  +--+  +--+  +--+  +--+                            |
  +-----------------------------------------------------------+
     ^  ^  ^
     |  |  +-- margen derecho de item 1
     |  +----- margen izquierdo de item 2
     +-------- estos DOS margenes se SUMAN = doble espacio en los bordes
               vs espacio simple entre items

  Problemas:
  - El primer y ultimo item tienen margen extra en los bordes
  - Margenes dobles entre items si no usas selectores especiales
  - Necesitas :first-child / :last-child para quitar margenes sobrantes


  CON GAP (forma moderna):

  +-----------------------------------------------------------+
  | +--+  +--+  +--+  +--+  +--+                             |
  | |  |  |  |  |  |  |  |  |  |                             |
  | +--+  +--+  +--+  +--+  +--+                             |
  +-----------------------------------------------------------+
       ^     ^     ^     ^
       |     |     |     +-- gap entre 4 y 5
       |     |     +-------- gap entre 3 y 4
       |     +-------------- gap entre 2 y 3
       +-------------------- gap entre 1 y 2
  NO hay espacio extra en los bordes. Limpio y predecible.
```

### Sintaxis

```css
/* Espacio uniforme en ambas direcciones */
gap: 10px;

/* Espacio diferente: fila vs columna */
gap: 10px 20px;    /* row-gap: 10px, column-gap: 20px */

/* Tambien se pueden usar por separado */
row-gap: 10px;
column-gap: 20px;
```

### En el ejercicio de dados

```css
.cara3 { gap: 20px; }      /* Separa los 3 puntos en diagonal */
.cara4 { gap: 40px; }      /* Espacio grande crea la cuadricula 2x2 */
.cara5 { gap: 40px; }      /* Igual que cara 4 para los 4 puntos exteriores */
.cara6 { gap: 20px; }      /* Separa los puntos en las 2 columnas */
```

---

## 10. Flexbox aplicado: el ejercicio de dados

Cada cara del dado en `dados.css` presenta un desafio de distribucion
diferente. Esta tabla resume como se resuelve cada una:

### Tabla: cara por cara

```
  CARA | PATRON          | flex-direction | justify-content | align-items | Extras
  -----|-----------------|----------------|-----------------|-------------|------------------
   1   | 1 punto         | row (defecto)  | center          | center      | Nada mas.
       | centrado        |                |                 | (base)      | Solo un hijo,
       |    *            |                |                 |             | se centra en
       |                 |                |                 |             | ambos ejes.
  -----|-----------------|----------------|-----------------|-------------|------------------
   2   | 2 puntos en     | column         | space-between   | center      | align-self:
       | diagonal        |                |                 | (base)      | flex-start en
       | *          *    |                |                 |             | :first-child
       |                 |                |                 |             | flex-end en
       |                 |                |                 |             | :last-child
  -----|-----------------|----------------|-----------------|-------------|------------------
   3   | 3 puntos en     | column         | space-between   | center      | align-self:
       | diagonal        |                |                 | (base)      | flex-start,
       | *     *     *   |                |                 |             | center,
       |                 |                |                 |             | flex-end
       |                 |                |                 |             | + gap: 20px
  -----|-----------------|----------------|-----------------|-------------|------------------
   4   | 4 puntos en     | row (defecto)  | space-between   | center      | flex-wrap: wrap
       | esquinas 2x2    |                |                 | (base)      | gap: 40px
       | *  *            |                |                 |             |
       | *  *            |                |                 |             |
  -----|-----------------|----------------|-----------------|-------------|------------------
   5   | 4 esquinas +    | row (defecto)  | space-between   | center      | flex-wrap: wrap
       | 1 centro        |                |                 | (base)      | gap: 40px
       | *  *            |                |                 |             | + position:
       |   *             |                |                 |             |   absolute en
       | *  *            |                |                 |             |   nth-child(3)
  -----|-----------------|----------------|-----------------|-------------|------------------
   6   | 6 puntos en     | column         | space-between   | center      | flex-wrap: wrap
       | 2 columnas      |                |                 | (base)      | gap: 20px
       | *  *            |                |                 |             |
       | *  *            |                |                 |             |
       | *  *            |                |                 |             |
```

### Diagrama de flujo conceptual

```
  Necesito centrar UN item?
       |
       SI --> justify-content: center + align-items: center
              (Cara 1)

  Necesito poner items en DIAGONAL?
       |
       SI --> flex-direction: column + justify-content: space-between
              + align-self diferente para cada item
              (Caras 2 y 3)

  Necesito una CUADRICULA?
       |
       SI --> flex-wrap: wrap + gap grande
              (Caras 4 y 5)

  Necesito un item FUERA del flujo flex?
       |
       SI --> position: absolute en ese item
              (Cara 5, punto central)

  Necesito COLUMNAS con items que fluyen hacia abajo?
       |
       SI --> flex-direction: column + flex-wrap: wrap
              (Cara 6)
```

---

## 11. Errores comunes

### Error 1: Olvidar `display: flex` en el padre

```css
/* MAL: los hijos no se alinean */
.contenedor {
    justify-content: center;     /* No hace nada sin display: flex */
    align-items: center;
}

/* BIEN */
.contenedor {
    display: flex;               /* PRIMERO activas Flexbox */
    justify-content: center;
    align-items: center;
}
```

**Sintoma:** Los items se apilan normalmente como bloques. Las propiedades
`justify-content` y `align-items` parecen no funcionar.

---

### Error 2: Confundir justify-content con align-items

```
  "Quiero centrar verticalmente" con flex-direction: row

  MAL:  justify-content: center;     <- centra HORIZONTAL (eje principal)
  BIEN: align-items: center;         <- centra VERTICAL (eje cruzado)

  "Quiero centrar verticalmente" con flex-direction: column

  MAL:  align-items: center;         <- centra HORIZONTAL (eje cruzado)
  BIEN: justify-content: center;     <- centra VERTICAL (eje principal)
```

**Mnemotecnia:** No pienses en "horizontal/vertical". Piensa en
"**eje principal** (justify) vs **eje cruzado** (align)". Luego
identifica cual es cada eje segun `flex-direction`.

---

### Error 3: Usar width cuando flex-basis es mas apropiado

```css
/* Funciona, pero no es la forma flex */
.item {
    width: 200px;
}

/* Mejor: respeta el sistema flex */
.item {
    flex: 0 0 200px;    /* No crece, no se encoge, 200px fijo */
}
```

**Por que:** `flex-basis` se adapta automaticamente al eje del contenedor.
Si cambias `flex-direction` de `row` a `column`, `flex-basis` pasa de
actuar como width a actuar como height. `width` siempre es width.

---

### Error 4: Esperar que los nietos sean flex items

```html
<div class="contenedor">      <!-- flex container -->
    <div class="hijo">         <!-- flex item -->
        <span class="nieto">   <!-- NO es flex item -->
        </span>
    </div>
</div>
```

**Solo los hijos DIRECTOS** son flex items. Si necesitas que `.nieto`
tambien participe en un layout flex, agrega `display: flex` a `.hijo`.

---

### Error 5: align-content sin wrap

```css
.contenedor {
    display: flex;
    flex-wrap: nowrap;          /* o no declarar flex-wrap */
    align-content: center;     /* NO TIENE EFECTO con una sola linea */
}
```

`align-content` solo funciona cuando hay **multiples lineas**
(es decir, con `flex-wrap: wrap` y suficientes items para crear
mas de una linea).

---

### Error 6: No entender por que los items se encogen

```css
.contenedor {
    display: flex;
    width: 300px;
}
.item {
    width: 200px;    /* 3 items x 200px = 600px > 300px */
}
```

Los items no mediran 200px. Por defecto, `flex-shrink: 1`, asi que
se encogeran para caber. Si necesitas que NO se encojan:

```css
.item {
    flex-shrink: 0;    /* Ahora mantiene sus 200px */
}
/* O usa flex-wrap: wrap en el contenedor para que salten de linea */
```

---

## 12. Ejercicios de practica

Todos los ejercicios se basan en el archivo `dados.css` de esta carpeta.
Abre `dados.html` en tu navegador y edita `dados.css` para practicar.

### Ejercicio 1 — Cara 1 invertida
Modifica la cara 1 para que el punto este en la esquina inferior derecha
en lugar del centro.

**Pistas:**
- Necesitas cambiar `justify-content` y `align-items` (o usar `align-self`).
- Recuerda: con `flex-direction: row`, `justify-content: flex-end` =
  derecha, `align-items: flex-end` = abajo.

---

### Ejercicio 2 — Cara 2 invertida
Haz que la cara 2 muestre los puntos en la diagonal INVERSA
(arriba-derecha a abajo-izquierda).

```
  Resultado esperado:
  +----------+
  |        * |
  |          |
  | *        |
  +----------+
```

**Pistas:**
- Intercambia los valores de `align-self` en `:first-child` y `:last-child`.

---

### Ejercicio 3 — Cara de 4 puntos alternativa
Crea una disposicion alternativa para 4 puntos: una fila de 4 centrados.

```
  Resultado esperado:
  +------------------+
  |  *   *   *   *   |
  +------------------+
```

**Pistas:**
- `flex-direction: row`, `justify-content: space-evenly`, sin `flex-wrap`.
- Puede que necesites reducir el tamano de los puntos o del gap.

---

### Ejercicio 4 — Contenedor con gap
Elimina el `margin: 10px` de las caras del dado y reemplazalo con
`gap: 20px` en `.contenedor`. Observa la diferencia en los bordes.

**Pistas:**
- Con margin, hay espacio en los bordes exteriores.
- Con gap, los bordes exteriores quedan limpios.
- Puedes necesitar mantener `padding` en `.contenedor` para compensar.

---

### Ejercicio 5 — Orden visual
Usa la propiedad `order` para que las caras del dado se muestren
en orden inverso (6, 5, 4, 3, 2, 1) sin cambiar el HTML.

```css
/* Ejemplo: */
.cara1 { order: 6; }
.cara2 { order: 5; }
/* ... completa el resto */
```

---

### Ejercicio 6 — Cara de 8 puntos (inventada)
Agrega una nueva cara con 8 puntos distribuidos en una cuadricula 4x2.

**Pistas:**
- Copia la estructura HTML de la cara 4 y agrega 4 puntos mas.
- Experimenta con `flex-wrap: wrap` y diferentes valores de `gap`.
- Piensa en cuantos puntos deben caber en cada fila.

---

### Ejercicio 7 — Centra vertical y horizontalmente
Crea un `<div>` de 400x400px con fondo gris. Dentro, coloca un cuadrado
de 100x100px con fondo rojo. Usa Flexbox para centrarlo **perfecta y
completamente** (horizontal + vertical).

```css
/* Solo necesitas estas 3 propiedades en el contenedor: */
display: flex;
justify-content: center;
align-items: center;
```

Este es el patron de centrado perfecto mas sencillo que existe en CSS.

---

### Ejercicio 8 — Navegacion flex
Modifica la barra de navegacion (`nav ul`) en `dados.html` para que:
1. En movil, los enlaces se apilen verticalmente (`flex-direction: column`)
2. En escritorio (a partir de 768px), se muestren en fila con `space-between`

**Pistas:**
- Agrega una media query `@media (min-width: 768px)` al final de `dados.css`.
- Los estilos base (mobile) usan `flex-direction: column`.
- La media query cambia a `flex-direction: row` y `justify-content: space-between`.

---

> **Siguiente modulo:** `05-componentes-css/CONCEPTOS.md` — Componentes CSS: Diseno Modular

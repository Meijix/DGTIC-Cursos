# Modulo 02 -- Fundamentos de CSS

> **Archivos de referencia:** `index.html` y `styles.css` en esta misma carpeta.
> Este modulo usa el mismo HTML del modulo 01, pero con una hoja de estilos
> externa. La estructura NO cambio; solo se le agrego presentacion visual.

---

## Indice

1.  [Que es CSS y como funciona](#1-que-es-css-y-como-funciona)
2.  [Selectores CSS](#2-selectores-css)
3.  [La Cascada y Especificidad](#3-la-cascada-y-especificidad)
4.  [El Modelo de Caja (Box Model)](#4-el-modelo-de-caja-box-model)
5.  [Variables CSS (Custom Properties)](#5-variables-css-custom-properties)
6.  [Unidades CSS](#6-unidades-css)
7.  [Colores en CSS](#7-colores-en-css)
8.  [Tipografia web](#8-tipografia-web)
9.  [Responsive: Media Queries](#9-responsive-media-queries)
10. [Errores comunes](#10-errores-comunes)
11. [Ejercicios de practica](#11-ejercicios-de-practica)

---

## 1. Que es CSS y como funciona

### Tres formas de agregar CSS

| Metodo              | Sintaxis                                         | Especificidad | Reutilizable? | Cacheable? |
|---------------------|--------------------------------------------------|---------------|---------------|------------|
| **Inline**          | `<p style="color: red">`                         | 1,0,0,0       | No            | No         |
| **Interno** (`<style>`) | `<style> p { color: red; } </style>` en `<head>` | Normal        | No (1 pagina) | No         |
| **Externo** (`<link>`)  | `<link rel="stylesheet" href="styles.css">`      | Normal        | Si (N paginas) | Si         |

> **En `styles.css`:** Usamos CSS externo. Observa en `index.html` linea 92
> el `<link rel="stylesheet" href="styles.css">` que conecta ambos archivos.

**Por que CSS externo es casi siempre la mejor opcion:**

1. **Cache:** El navegador descarga `styles.css` UNA vez y lo reutiliza
   en todas las paginas. En visitas posteriores ni siquiera lo descarga.
2. **Mantenimiento:** Un solo cambio en `styles.css` afecta todas las paginas.
3. **Separacion de responsabilidades:** El HTML queda limpio. Un disenador
   puede trabajar en CSS mientras otro trabaja en HTML.
4. **Rendimiento:** El archivo CSS se comprime y se envia por separado.

### Como el navegador procesa CSS

```
  1. Descarga HTML               2. Parsea HTML y            3. Encuentra <link>
     del servidor                   construye el DOM            al CSS externo
  ┌──────────┐                   ┌──────────────┐           ┌──────────────┐
  │  HTML     │ ───────────────> │    DOM        │ ────────> │ Peticion HTTP │
  │  (texto)  │                  │  (arbol de    │           │ para styles.css│
  └──────────┘                   │   nodos)      │           └──────┬───────┘
                                 └──────────────┘                  │
                                                                   ▼
  6. Pinta en                    5. Layout: calcula          4. Construye el
     pantalla                       posicion y tamano           CSSOM
  ┌──────────┐                   ┌──────────────┐           ┌──────────────┐
  │  PAINT    │ <─────────────── │   LAYOUT      │ <──────── │   CSSOM       │
  │  (pixeles)│                  │  (geometria)  │           │ (arbol de     │
  └──────────┘                   └──────────────┘           │  reglas CSS)  │
                                                            └──────────────┘
                                         ▲
                                         │
                                 ┌──────────────┐
                                 │  RENDER TREE  │ ← DOM + CSSOM combinados
                                 │ (solo nodos   │   (elementos con display:none
                                 │  visibles)    │    NO aparecen aqui)
                                 └──────────────┘
```

**Punto clave:** CSS es "render-blocking". El navegador NO pinta nada hasta
tener el CSS. Esto evita el FOUC (Flash Of Unstyled Content) -- ese destello
de contenido sin estilos que se ve cuando el CSS tarda en cargar.

---

## 2. Selectores CSS

### Tabla de referencia completa

| Tipo                    | Sintaxis            | Ejemplo                | Selecciona                                     | Especificidad |
|-------------------------|---------------------|------------------------|-------------------------------------------------|---------------|
| **Elemento/tipo**       | `elemento`          | `p`                    | Todos los `<p>`                                 | 0,0,0,1       |
| **Clase**               | `.clase`            | `.menu`                | Todos con `class="menu"`                        | 0,0,1,0       |
| **ID**                  | `#id`               | `#header`              | El unico con `id="header"`                      | 0,1,0,0       |
| **Universal**           | `*`                 | `*`                    | TODOS los elementos                             | 0,0,0,0       |
| **Atributo**            | `[attr]`            | `[type="email"]`       | Inputs con type="email"                         | 0,0,1,0       |
| **Atributo parcial**    | `[attr^="val"]`     | `[href^="https"]`      | Enlaces que empiezan con "https"                | 0,0,1,0       |
| **Pseudo-clase**        | `:pseudo`           | `:hover`               | Elementos en estado hover                       | 0,0,1,0       |
| **Pseudo-elemento**     | `::pseudo`          | `::first-line`         | La primera linea de un elemento                 | 0,0,0,1       |
| **Descendiente**        | `A B`               | `nav li`               | Todos los `<li>` DENTRO de `<nav>` (cualquier nivel) | Suma de ambos |
| **Hijo directo**        | `A > B`             | `nav > ul`             | `<ul>` que son hijos DIRECTOS de `<nav>`        | Suma de ambos |
| **Hermano adyacente**   | `A + B`             | `h2 + p`               | El `<p>` que viene INMEDIATAMENTE despues de `<h2>` | Suma de ambos |
| **Hermano general**     | `A ~ B`             | `h2 ~ p`               | Todos los `<p>` que vienen despues de `<h2>`    | Suma de ambos |
| **Grupo**               | `A, B`              | `h1, h2, h3`           | Todos los h1, h2 Y h3                           | Independiente |

### Pseudo-clases mas usadas

| Pseudo-clase            | Selecciona                                         | Ejemplo de uso                    |
|-------------------------|----------------------------------------------------|-----------------------------------|
| `:hover`                | Cuando el cursor esta encima                       | `a:hover { color: red; }`        |
| `:focus`                | Cuando el elemento tiene el foco (teclado/clic)    | `input:focus { border: blue; }`  |
| `:active`               | Mientras se hace clic (boton presionado)           | `button:active { scale: 0.95; }` |
| `:first-child`          | El primer hijo de su padre                         | `li:first-child { font-weight: bold; }` |
| `:last-child`           | El ultimo hijo de su padre                         | `li:last-child { border: none; }`|
| `:nth-child(n)`         | El n-esimo hijo (acepta formulas)                  | `tr:nth-child(2n) { background: #eee; }` |
| `:not(selector)`        | Todos EXCEPTO los que coincidan                    | `p:not(.intro) { color: gray; }` |
| `:checked`              | Radio/checkbox seleccionado                        | `input:checked + label { bold; }`|
| `:disabled`             | Elementos deshabilitados                           | `input:disabled { opacity: 0.5; }` |
| `:root`                 | El elemento raiz (`<html>`)                        | `:root { --color: blue; }`       |

### Selectores combinadores (visual)

```
  <nav>
    <ul>                        Descendiente: nav li     --> Selecciona A, B, C y D
      <li>A</li>                Hijo directo: nav > li   --> NO selecciona nada
      <li>B                                                  (li NO es hijo directo de nav)
        <ul>                    Hijo directo: ul > li    --> Selecciona A, B, C y D
          <li>C</li>                                         (cada li es hijo de SU ul)
          <li>D</li>
        </ul>
      </li>
    </ul>
  </nav>

  Hermano adyacente: A + B     --> Selecciona SOLO el elemento B
                                    (el inmediatamente siguiente)

  Hermano general: A ~ B       --> Selecciona B, C, D...
                                    (todos los hermanos posteriores)
```

> **En `styles.css`:** Las lineas 175-185 usan un selector de grupo
> (`div, header, nav, main, footer, section, article, aside, ul`)
> para aplicar los mismos bordes de depuracion a multiples elementos.

---

## 3. La Cascada y Especificidad

### El algoritmo de la cascada

Cuando multiples reglas CSS apuntan al mismo elemento, el navegador
decide cual gana siguiendo este orden de prioridad:

```
  PRIORIDAD (de menor a mayor):

  1. Estilos del navegador (user-agent stylesheet)
     └── Los estilos por defecto: <h1> es grande, <a> es azul, etc.

  2. Estilos del autor (TU CSS)
     └── Todo lo que escribes en styles.css

  3. Estilos del usuario (configuracion del navegador)
     └── El usuario puede tener CSS propio (raro hoy en dia)

  4. !important del autor
     └── Reglas marcadas con !important en tu CSS

  5. !important del usuario
     └── Reglas !important del usuario (accesibilidad)

  Si hay EMPATE en el paso anterior, se resuelve por:

  6. Especificidad (la tabla de abajo)

  Si hay EMPATE en especificidad:

  7. Orden de aparicion (la ultima regla gana)
```

### Calculo de especificidad detallado

La especificidad se expresa como cuatro numeros: `(inline, IDs, clases, elementos)`

```
  Selector                          Calculo                             Especificidad
  ──────────────────────────────    ─────────────────────────────       ─────────────
  p                                 0 inline, 0 IDs, 0 clases, 1 elem  0,0,0,1
  .card                             0 inline, 0 IDs, 1 clase,  0 elem  0,0,1,0
  p.card                            0 inline, 0 IDs, 1 clase,  1 elem  0,0,1,1
  #main                             0 inline, 1 ID,  0 clases, 0 elem  0,1,0,0
  #main .card                       0 inline, 1 ID,  1 clase,  0 elem  0,1,1,0
  #main .card p                     0 inline, 1 ID,  1 clase,  1 elem  0,1,1,1
  #main .card p:hover               0 inline, 1 ID,  2 clases, 1 elem  0,1,2,1
  #main .card p::first-line          0 inline, 1 ID,  1 clase,  2 elem  0,1,1,2
  style="color:red"                 1 inline, 0 IDs, 0 clases, 0 elem  1,0,0,0
```

**Como comparar:** Se leen de izquierda a derecha. El primer numero mayor gana.
`0,1,0,0` siempre le gana a `0,0,99,99` (un solo ID supera a 99 clases).

### Ejemplo practico con el archivo styles.css

```css
  /* En styles.css: */
  body    { color: var(--azulclaro); }     /* Especificidad: 0,0,0,1 */
  section { color: var(--azulmarino); }    /* Especificidad: 0,0,0,1 */
  article { color: #fff; }                /* Especificidad: 0,0,0,1 */
```

Un `<p>` dentro de `<article>` hereda `color: #fff` porque `article`
es su ancestro mas cercano con la propiedad `color` definida. La cascada
funciona de lo mas especifico (cercano) a lo mas general (lejano).

### Por que !important es (casi) siempre incorrecto

```css
  /* Alguien escribe esto: */
  .boton { background: blue !important; }

  /* Despues otro necesita un boton rojo: */
  .boton-peligro { background: red; }              /* NO funciona -- !important gana */
  .boton-peligro { background: red !important; }   /* "Solucion": otro !important */

  /* Despues otro necesita un boton verde: */
  #form .boton-peligro { background: green !important; }  /* Aun MAS !important */

  /* Esto se llama "guerra de !important" y es un infierno de mantenimiento */
```

**La unica excepcion aceptable:** Sobreescribir estilos de terceros (una libreria
de componentes que usa estilos inline que no puedes cambiar).

### Herencia en CSS

| Propiedades que SI se heredan           | Propiedades que NO se heredan          |
|-----------------------------------------|----------------------------------------|
| `color`                                 | `margin`                               |
| `font-family`                           | `padding`                              |
| `font-size`                             | `border`                               |
| `font-weight`                           | `background`                           |
| `line-height`                           | `width`, `height`                      |
| `text-align`                            | `display`                              |
| `letter-spacing`                        | `position`                             |
| `word-spacing`                          | `overflow`                             |
| `visibility`                            | `box-shadow`                           |
| `cursor`                                | `transform`                            |
| `list-style`                            | `opacity`                              |

**Regla general:** Las propiedades de TEXTO se heredan. Las propiedades de CAJA no.

> **En `styles.css`:** El `body` define `color: var(--azulclaro)` (linea 285).
> Todos los elementos hijos heredan ese color EXCEPTO los que lo sobreescriben
> (`section`, `article`, `aside`).

---

## 4. El Modelo de Caja (Box Model)

### Diagrama completo

```
  ┌────────────────── MARGIN ──────────────────────────────────┐
  │                   (espacio exterior, transparente)          │
  │   ┌────────────── BORDER ────────────────────────────┐     │
  │   │               (linea visible)                     │     │
  │   │   ┌────────── PADDING ──────────────────────┐    │     │
  │   │   │           (espacio interior)             │    │     │
  │   │   │   ┌────── CONTENT ────────────────┐     │    │     │
  │   │   │   │                                │     │    │     │
  │   │   │   │      width  x  height          │     │    │     │
  │   │   │   │                                │     │    │     │
  │   │   │   │   (texto, imagenes, hijos)     │     │    │     │
  │   │   │   │                                │     │    │     │
  │   │   │   └────────────────────────────────┘     │    │     │
  │   │   │          padding-bottom                  │    │     │
  │   │   └──────────────────────────────────────────┘    │     │
  │   │              border-bottom                        │     │
  │   └───────────────────────────────────────────────────┘     │
  │                  margin-bottom                              │
  └─────────────────────────────────────────────────────────────┘
```

### content-box vs border-box (con numeros)

```
  CONTENT-BOX (por defecto):
  ──────────────────────────

  width: 300px;
  padding: 20px;
  border: 5px solid black;

  Ancho REAL en pantalla:
  content   + padding-left + padding-right + border-left + border-right
  300px     + 20px         + 20px          + 5px         + 5px          = 350px

  ¡¡Sorpresa!! Dijiste 300px pero ocupa 350px.

  ────────────────────────────────────────────────────────

  BORDER-BOX (recomendado):
  ──────────────────────────

  box-sizing: border-box;
  width: 300px;
  padding: 20px;
  border: 5px solid black;

  Ancho REAL en pantalla: 300px (padding y border se RESTAN del content)

  content = 300 - 20 - 20 - 5 - 5 = 250px

  El ancho total SIEMPRE es lo que dijiste: 300px. Sin sorpresas.
```

**Recomendacion universal:** Muchos frameworks y reset CSS usan:
```css
*, *::before, *::after {
    box-sizing: border-box;
}
```

> **En `styles.css`:** No se declara `box-sizing` global, por lo que se usa
> el default `content-box`. Tenlo en cuenta al calcular tamanos.

### Colapso de margenes (margin collapse)

Este es uno de los comportamientos mas confusos de CSS.

```
  SIN colapso (lo que esperarias):         CON colapso (lo que pasa):

  ┌──────────────────┐                     ┌──────────────────┐
  │    Parrafo 1     │                     │    Parrafo 1     │
  │  margin-bottom:  │                     │  margin-bottom:  │
  │     30px         │                     │     30px         │
  └──────────────────┘                     └──────────────────┘
        30px espacio                             30px espacio    <-- Solo 30px, no 50px!
        20px espacio                                             <-- El margin-top de 20px
  ┌──────────────────┐                     ┌──────────────────┐      se "absorbe" dentro
  │    Parrafo 2     │                     │    Parrafo 2     │      del margin-bottom de 30px
  │  margin-top:     │                     │  margin-top:     │
  │     20px         │                     │     20px         │
  └──────────────────┘                     └──────────────────┘

  Esperabas 50px (30+20)                   Solo hay 30px (el MAYOR gana)
```

**Reglas del colapso:**
1. Solo ocurre con margenes **verticales** (top/bottom), nunca horizontales.
2. Solo ocurre entre elementos **en bloque** en el flujo normal.
3. Los margenes colapsan al **mayor** de los dos (no se suman).
4. **No colapsa** si hay padding, border, o el padre es flex/grid.

---

## 5. Variables CSS (Custom Properties)

### Sintaxis y alcance

```css
  :root {
      /* Variables GLOBALES -- disponibles en todo el documento */
      --color-primario: #7ee8fd;
      --color-fondo: #001f3f;
      --espaciado-grande: 1rem;
  }

  .tarjeta {
      /* Variable LOCAL -- solo disponible dentro de .tarjeta y sus hijos */
      --radio-borde: 8px;
      background: var(--color-primario);     /* Usa variable global */
      border-radius: var(--radio-borde);     /* Usa variable local */
  }

  .tarjeta .titulo {
      color: var(--color-fondo);             /* Hereda acceso a variables globales */
      padding: var(--espaciado-grande);      /* Funciona porque hereda de :root */
  }
```

### Valor de respaldo (fallback)

```css
  color: var(--color-texto, black);
  /*                        ^^^^^^
       Si --color-texto NO esta definida, usa "black" como respaldo */

  color: var(--color-texto, var(--color-default, #333));
  /*     Encadenamiento: si --color-texto no existe,
         prueba --color-default; si tampoco, usa #333 */
```

### Variables CSS vs variables de preprocesadores (Sass)

```
  SASS ($variable):                       CSS (--variable):
  ──────────────                          ──────────────────

  $color: blue;                           :root { --color: blue; }
  .boton { color: $color; }              .boton { color: var(--color); }

  Compilado a CSS final:                  En el CSS final:
  .boton { color: blue; }                .boton { color: var(--color); }

  La variable DESAPARECE.                 La variable SIGUE VIVA.
  No puedes cambiarla despues.            Puedes cambiarla con JS:
                                          document.documentElement.style
                                            .setProperty('--color', 'red');

  No reacciona a media queries.           Reacciona a media queries:
                                          @media (prefers-color-scheme: dark) {
                                              :root { --color: lightblue; }
                                          }
```

> **En `styles.css`:** Las lineas 72-77 definen variables en `:root`:
> `--azulclaro`, `--azulmarino`, `--grande`, `--mediano`. Despues se usan
> con `var(--azulclaro)` en el body, section, aside, etc.

### Ejemplo: tema oscuro/claro con variables

```css
  :root {
      --bg: #ffffff;
      --texto: #333333;
  }

  @media (prefers-color-scheme: dark) {
      :root {
          --bg: #1a1a2e;
          --texto: #e0e0e0;
      }
  }

  body {
      background: var(--bg);
      color: var(--texto);
      /* Cambia automaticamente segun las preferencias del sistema operativo */
  }
```

---

## 6. Unidades CSS

### Tabla completa de unidades

| Unidad  | Tipo      | Relativa a                          | Ejemplo          | Mejor para                        |
|---------|-----------|-------------------------------------|------------------|-----------------------------------|
| `px`    | Absoluta  | Nada (fija)                         | `16px`           | Bordes, sombras, detalles finos   |
| `rem`   | Relativa  | `font-size` del `<html>` (root)     | `1.5rem = 24px`  | Fuentes, padding, margin          |
| `em`    | Relativa  | `font-size` del PADRE               | `1.5em`          | Padding/margin relativo al texto  |
| `%`     | Relativa  | Propiedad del padre                 | `50%`            | Anchos fluidos                    |
| `vw`    | Relativa  | 1% del ancho del viewport           | `100vw`          | Elementos full-width              |
| `vh`    | Relativa  | 1% del alto del viewport            | `100vh`          | Secciones full-height             |
| `vmin`  | Relativa  | 1% del lado MAS PEQUENO del viewport| `50vmin`         | Tipografia responsiva             |
| `vmax`  | Relativa  | 1% del lado MAS GRANDE del viewport | `50vmax`         | (poco comun)                      |
| `ch`    | Relativa  | Ancho del caracter "0" de la fuente | `60ch`           | Ancho maximo de texto legible     |
| `fr`    | Relativa  | Fraccion del espacio disponible     | `1fr 2fr`        | CSS Grid (columnas)               |

### Cuando usar cada unidad: guia de decision

```
  Que estas definiendo?
          │
    ┌─────┼──────────────────────────────┐
    │     │                              │
    ▼     ▼                              ▼
  Fuentes  Espaciado                    Ancho de
  (font-   (padding,                    contenedores
  size)    margin, gap)
    │        │                              │
    ▼        ▼                              ▼
  usa REM   Debe escalar con              usa % o vw
             el texto local?              (o max-width con px)
                  │
             ┌────┴────┐
             │ SI      │ NO
             ▼         ▼
           usa EM    usa REM

  Excepciones:
  - Bordes finos: usa px (1px, 2px)
  - Sombras: usa px
  - Media queries: usa px o em (no rem)
  - max-width de texto legible: usa ch (60-80ch ideal)
```

### El problema del em compuesto

```css
  body    { font-size: 1.2em; }    /* 16px * 1.2 = 19.2px  */
  section { font-size: 1.2em; }    /* 19.2px * 1.2 = 23.04px -- HEREDA del body */
  article { font-size: 1.2em; }    /* 23.04px * 1.2 = 27.65px -- HEREDA de section */
  p       { font-size: 1.2em; }    /* 27.65px * 1.2 = 33.18px -- HEREDA de article */

  /* Esperabas 1.2em en todos, pero el <p> dentro de article/section/body
     tiene un font-size de 33px en lugar de los ~19px que querias.
     Esto se llama el "efecto compuesto" del em. */

  /* SOLUCION: Usa rem */
  body    { font-size: 1.2rem; }   /* 16px * 1.2 = 19.2px */
  section { font-size: 1.2rem; }   /* 16px * 1.2 = 19.2px -- SIEMPRE relativo a root */
  article { font-size: 1.2rem; }   /* 16px * 1.2 = 19.2px -- SIEMPRE relativo a root */
  p       { font-size: 1.2rem; }   /* 16px * 1.2 = 19.2px -- Predecible y consistente */
```

> **En `styles.css`:** Se usan variables con `rem` (`--grande: 1rem` y
> `--mediano: 0.8rem`). Esto evita el problema del em compuesto.

---

## 7. Colores en CSS

### Comparacion de formatos

| Formato           | Sintaxis                    | Ejemplo                | Transparencia  | Legibilidad |
|-------------------|-----------------------------|------------------------|----------------|-------------|
| **Hexadecimal**   | `#RRGGBB`                   | `#001f3f`              | `#001f3f80`    | Baja        |
| **Hex corto**     | `#RGB`                      | `#fff`                 | `#fff8`        | Media       |
| **RGB**           | `rgb(R, G, B)`              | `rgb(0, 31, 63)`       | --             | Alta        |
| **RGBA**          | `rgba(R, G, B, A)`          | `rgba(0, 31, 63, 0.5)` | Si (0-1)      | Alta        |
| **HSL**           | `hsl(H, S%, L%)`            | `hsl(210, 100%, 12%)`  | --             | Muy alta    |
| **HSLA**          | `hsla(H, S%, L%, A)`        | `hsla(210, 100%, 12%, 0.5)` | Si (0-1) | Muy alta    |
| **Nombre**        | `nombre`                    | `navy`                 | No             | Muy alta    |
| **RGB moderno**   | `rgb(R G B / A)`            | `rgb(0 31 63 / 50%)`   | Si             | Alta        |

### HSL explicado visualmente

```
  H (Hue / Matiz): El "color" en un circulo de 0 a 360 grados
  ──────────────────────────────────────────────────────────
     0/360 = Rojo
        60 = Amarillo
       120 = Verde
       180 = Cian
       240 = Azul
       300 = Magenta

  S (Saturation / Saturacion): Que tan "vivo" es el color
  ──────────────────────────────────────────────────────────
     0%  = Gris (sin color)
    50%  = Color apagado/pastel
   100%  = Color puro/vibrante

  L (Lightness / Luminosidad): Que tan claro u oscuro
  ──────────────────────────────────────────────────────────
     0%  = Negro
    50%  = Color puro
   100%  = Blanco
```

**Por que HSL es mas intuitivo:** Si quieres una version mas clara del mismo
color, solo aumentas la L. Con hex o rgb, tendrias que calcular valores
nuevos para los tres canales.

> **En `styles.css`:** Se usan hex (`#7ee8fd`, `#001f3f`, `#d2a8fd`, `#9005a5`),
> rgb (`rgb(245, 241, 241)`), y nombre (`#fff` equivalente a `white`).

---

## 8. Tipografia web

### Font stacks (pilas de fuentes)

```css
  font-family: 'Arial', sans-serif;
  /*            ^^^^^    ^^^^^^^^^^
       Fuente preferida   Familia generica de respaldo (OBLIGATORIA) */
```

El navegador recorre la lista de izquierda a derecha y usa la primera
fuente que encuentre instalada en el sistema del usuario.

### Tabla de familias genericas

| Familia        | Aspecto                                    | Ejemplo de fuentes             | Uso comun                    |
|----------------|--------------------------------------------|-------------------------------|------------------------------|
| `sans-serif`   | Sin serifas (patas), moderna y limpia      | Arial, Helvetica, Verdana      | Interfaces, cuerpo de texto  |
| `serif`        | Con serifas, clasica y formal              | Times New Roman, Georgia       | Editoriales, titulos formales|
| `monospace`    | Cada caracter ocupa el mismo ancho         | Courier New, Consolas          | Codigo, datos tabulares      |
| `cursive`      | Simula escritura a mano                    | Comic Sans MS, Brush Script    | Invitaciones (poco en web)   |
| `fantasy`      | Decorativas                                | Impact, Papyrus                | Casi nunca en web profesional|
| `system-ui`    | La fuente por defecto del sistema operativo | San Francisco (Mac), Segoe (Win) | Aspecto nativo moderno     |

### Propiedades tipograficas fundamentales

| Propiedad         | Valores comunes                       | Buena practica                         |
|-------------------|---------------------------------------|----------------------------------------|
| `font-size`       | `1rem`, `16px`, `clamp(1rem, 2vw, 2rem)` | Usar `rem` para accesibilidad     |
| `line-height`     | `1.5`, `1.6`, `24px`                 | 1.5-1.7 para cuerpo de texto           |
| `font-weight`     | `normal` (400), `bold` (700), 100-900 | Evitar valores menores a 300 para legibilidad |
| `letter-spacing`  | `0.05em`, `1px`, `-0.5px`            | Ligero aumento para encabezados en mayuscula |
| `word-spacing`    | `normal`, `0.1em`                     | Rara vez se modifica                   |
| `text-transform`  | `uppercase`, `lowercase`, `capitalize` | `uppercase` para botones/navs         |
| `font-style`      | `normal`, `italic`, `oblique`         | `italic` solo para enfasis o citas     |
| `text-decoration` | `none`, `underline`, `line-through`   | `none` en enlaces dentro de navs       |

### Web-safe fonts vs Google Fonts

```
  WEB-SAFE (instaladas en casi todos los sistemas):
  ──────────────────────────────────────────────────
  Arial, Verdana, Helvetica, Tahoma, Trebuchet MS,
  Times New Roman, Georgia, Courier New, Comic Sans MS

  Ventaja: No requieren descarga
  Desventaja: Opciones limitadas y genericas

  GOOGLE FONTS (se descargan del CDN de Google):
  ──────────────────────────────────────────────────
  <link href="https://fonts.googleapis.com/css2?family=Roboto&display=swap"
        rel="stylesheet">

  font-family: 'Roboto', sans-serif;

  Ventaja: Miles de fuentes profesionales
  Desventaja: Requiere conexion a internet; impacto en rendimiento

  SYSTEM FONTS STACK (moderna y rapida):
  ──────────────────────────────────────────────────
  font-family: system-ui, -apple-system, BlinkMacSystemFont,
               'Segoe UI', Roboto, sans-serif;

  Usa la fuente nativa de cada SO. Carga instantanea. Se ve "nativa".
```

> **En `styles.css`:** Se usa `'Arial', sans-serif` (linea 281), un
> font stack sencillo con respaldo generico.

---

## 9. Responsive: Media Queries

### El concepto de breakpoints

```
  Movil          Tablet           Laptop           Escritorio        Pantalla grande
  < 480px        480-768px        768-1024px       1024-1200px       > 1200px
  ─────│────────────│────────────────│─────────────────│────────────────│──────
       │            │                │                 │                │
       ▼            ▼                ▼                 ▼                ▼
  1 columna    1-2 columnas      2 columnas        2-3 columnas      3+ columnas
  Nav vertical Nav colapsable    Nav horizontal    Nav completa      Nav + sidebar
```

### Mobile-first (min-width) vs Desktop-first (max-width)

```
  MOBILE-FIRST (recomendado):                DESKTOP-FIRST:
  ───────────────────────────                ─────────────────

  /* Base: estilos para movil */             /* Base: estilos para escritorio */
  .menu { display: block; }                 .menu { display: flex; }

  /* Tableta en adelante */                  /* Tableta hacia abajo */
  @media (min-width: 768px) {               @media (max-width: 768px) {
      .menu { display: flex; }                  .menu { display: block; }
  }                                         }

  LOGICA: "Si el ancho es >= 768px,          LOGICA: "Si el ancho es <= 768px,
  AGREGA estos estilos"                      QUITA/CAMBIA estos estilos"

  FILOSOFIA: Empieza simple,                 FILOSOFIA: Empieza complejo,
  agrega complejidad.                        quita complejidad.
  (MAS facil de mantener)                    (MAS dificil de mantener)
```

### Breakpoints comunes

| Breakpoint  | Dispositivo tipico               | Uso                               |
|-------------|----------------------------------|-----------------------------------|
| `480px`     | Moviles grandes                  | Ajustes menores de font-size      |
| `768px`     | Tablets verticales               | De 1 columna a 2 columnas         |
| `1024px`    | Tablets horizontales / laptops   | Layout completo                   |
| `1200px`    | Escritorios                      | Max-width del contenedor           |
| `1440px`    | Pantallas grandes                | Ajustes de espaciado              |

> **IMPORTANTE:** Estos son valores de referencia, no reglas fijas.
> El mejor breakpoint es donde TU contenido "se rompe" visualmente.

> **En `styles.css`:** La linea 467 usa `@media (min-width: 768px)` para
> activar Flexbox en el layout. Es un enfoque mobile-first: en moviles
> todo es una columna (comportamiento default de bloques), y en 768px+
> se reorganiza en filas con flex.

### Ejemplo del layout responsive en styles.css

```
  MOVIL (< 768px):                    ESCRITORIO (>= 768px):
  ┌────────────────────┐              ┌──────────────────────────────────┐
  │     HEADER         │              │           HEADER (100%)          │
  ├────────────────────┤              ├──────────────────────────────────┤
  │     NAV            │              │           NAV (100%)             │
  ├────────────────────┤              ├─────────────────────┬────────────┤
  │     SECTION        │              │   SECTION (65%)     │ ASIDE (30%)│
  ├────────────────────┤              │                     │            │
  │     ASIDE          │              │                     │            │
  ├────────────────────┤              ├─────────────────────┴────────────┤
  │     FOOTER         │              │           FOOTER (100%)          │
  └────────────────────┘              └──────────────────────────────────┘

  Todo apilado verticalmente          Section y aside lado a lado
  (comportamiento por defecto)        (Flexbox activado por media query)
```

---

## 10. Errores comunes

### Error 1: Olvidar `rel="stylesheet"` en el link

```html
  <!-- MAL: el CSS se descarga pero NO se aplica -->
  <link href="styles.css">

  <!-- BIEN -->
  <link rel="stylesheet" href="styles.css">
```

### Error 2: Especificidad accidental con IDs

```css
  /* Un solo ID ya supera a CUALQUIER cantidad de clases */
  #sidebar .link .icon span { color: red; }    /* 0,1,3,1 */
  .nav .menu .item .link .icon span { color: blue; }  /* 0,0,6,1 */

  /* Gana el rojo porque 0,1,X,X > 0,0,X,X SIEMPRE */
  /* Solucion: Evitar IDs en selectores CSS; usalos solo para JS y for/id */
```

### Error 3: Margenes que no aparecen (margin collapse)

```css
  /* El margin-top del h1 colapsa con el margin del contenedor padre */
  .contenedor { background: gray; }
  .contenedor h1 { margin-top: 30px; }  /* Este margen "se escapa" del padre */

  /* Solucion: agrega padding, border, o overflow al padre */
  .contenedor { background: gray; padding-top: 1px; }  /* Rompe el colapso */
  /* O mejor: */
  .contenedor { background: gray; overflow: auto; }
```

### Error 4: Usar px para font-size

```css
  /* MAL: Si el usuario cambia el tamano base del navegador, esto NO escala */
  body { font-size: 16px; }

  /* BIEN: Respeta las preferencias del usuario */
  body { font-size: 1rem; }
```

### Error 5: No incluir la familia generica de respaldo

```css
  /* MAL: Si 'Roboto' no esta disponible, el navegador usa SU default
     (que podria ser Times New Roman en algunos sistemas) */
  font-family: 'Roboto';

  /* BIEN */
  font-family: 'Roboto', sans-serif;
```

### Error 6: Confundir content-box con border-box

```css
  /* Con el default content-box: */
  .caja { width: 100%; padding: 20px; }
  /* Ancho real: 100% + 40px -- SE DESBORDA del contenedor padre */

  /* Solucion: */
  .caja { width: 100%; padding: 20px; box-sizing: border-box; }
  /* Ahora el padding esta DENTRO del 100% */
```

### Error 7: z-index sin position

```css
  /* MAL: z-index no funciona en elementos con position: static (default) */
  .modal { z-index: 9999; }  /* No tiene efecto */

  /* BIEN */
  .modal { position: relative; z-index: 9999; }
  /* O: position: absolute, fixed, sticky -- cualquiera menos static */
```

---

## 11. Ejercicios de practica

### Ejercicio 1: Especificidad (Principiante)

Sin ejecutar el codigo, predice que color tendra el texto:

```html
<p id="intro" class="texto destacado">Hola mundo</p>
```

```css
p { color: blue; }
.texto { color: green; }
.destacado { color: orange; }
#intro { color: red; }
p.texto.destacado { color: purple; }
```

Calcula la especificidad de cada selector y ordenalos. Despues verifica en el navegador.

### Ejercicio 2: Box Model (Principiante)

Crea una caja con estos requisitos:
- Ancho total visible: exactamente 400px
- Padding: 20px en todos los lados
- Border: 3px solid negro
- Calcula el `width` que necesitas para `content-box`
- Ahora hazlo con `border-box` (que `width` usas?)

### Ejercicio 3: Variables y tema (Intermedio)

Toma el archivo `styles.css` de este modulo y:
1. Agrega 3 variables nuevas en `:root` para colores del formulario
2. Crea una media query `@media (prefers-color-scheme: dark)` que
   redefina las variables `--azulclaro` y `--azulmarino` para un tema oscuro alternativo
3. Agrega una variable `--radio-borde` y usala en al menos 3 elementos

### Ejercicio 4: Layout responsive (Avanzado)

Modifica el archivo `styles.css` para agregar un segundo breakpoint:
- En movil (< 768px): todo en una columna (ya esta asi)
- En tablet (768px - 1024px): section 60%, aside 35%
- En escritorio (> 1024px): agrega max-width: 1200px al body y centralo

Pista: Necesitaras dos `@media` queries con `min-width`.

---

## Para profundizar

### El contexto de apilamiento (stacking context)

`z-index` no funciona de manera global. Cada elemento con `position` distinta
de `static` y un `z-index` crea un **nuevo contexto de apilamiento**. Los hijos
de ese elemento solo compiten entre si, no con elementos fuera del contexto.

```
  Contexto raiz (document)
  │
  ├── .modal (z-index: 100, position: fixed)
  │     └── .boton-cerrar (z-index: 9999)    <-- Este 9999 solo compite
  │                                               dentro de .modal
  │
  └── .tooltip (z-index: 200, position: absolute)
        └── (cualquier hijo con z-index solo compite aqui dentro)

  .tooltip (z-index: 200) aparece ENCIMA de .modal (z-index: 100),
  y el .boton-cerrar con z-index: 9999 NO puede escapar de .modal.
```

### Propiedades logicas (CSS moderno)

Las propiedades logicas reemplazan `top/right/bottom/left` con terminos que
se adaptan a la direccion del texto (LTR/RTL):

| Propiedad fisica   | Propiedad logica (LTR)          | Propiedad logica (RTL)          |
|---------------------|---------------------------------|---------------------------------|
| `margin-top`        | `margin-block-start`            | `margin-block-start`            |
| `margin-bottom`     | `margin-block-end`              | `margin-block-end`              |
| `margin-left`       | `margin-inline-start`           | `margin-inline-end`             |
| `margin-right`      | `margin-inline-end`             | `margin-inline-start`           |
| `padding-left`      | `padding-inline-start`          | `padding-inline-end`            |
| `width`             | `inline-size`                   | `inline-size`                   |
| `height`            | `block-size`                    | `block-size`                    |

### La funcion clamp() para tipografia fluida

```css
  /* En lugar de media queries para cada breakpoint: */
  h1 { font-size: clamp(1.5rem, 4vw, 3rem); }
  /*                     ^^^^^  ^^^  ^^^^^
                         minimo  ideal  maximo

  - Nunca menor que 1.5rem (24px)
  - Escala con 4vw (4% del ancho del viewport)
  - Nunca mayor que 3rem (48px)

  Una sola linea reemplaza multiples media queries. */
```

### Metodologia BEM para nombrar clases

```css
  /* BEM = Block, Element, Modifier */

  /* Bloque: componente independiente */
  .tarjeta { ... }

  /* Elemento: parte del bloque (separador: __) */
  .tarjeta__titulo { ... }
  .tarjeta__imagen { ... }
  .tarjeta__boton { ... }

  /* Modificador: variante del bloque o elemento (separador: --) */
  .tarjeta--destacada { ... }
  .tarjeta__boton--deshabilitado { ... }
```

BEM mantiene la especificidad baja (todo son clases simples) y hace
el codigo auto-documentable: al leer `.tarjeta__boton--deshabilitado`
sabes exactamente que es y a que componente pertenece.

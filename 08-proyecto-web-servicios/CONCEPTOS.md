# Modulo 08 — Proyecto Integrador: Sitio Web de Servicios

> **Prerequisitos:** Modulos 01-07 (HTML semantico, CSS, Flexbox, Grid, responsive).
> **Archivos del ejercicio:** `index.html`, `styles.css` y carpeta `images/` en esta misma carpeta.

---

## Indice

1. [Planificacion de un proyecto web](#1-planificacion-de-un-proyecto-web)
2. [Estructura semantica para sitios reales](#2-estructura-semantica-para-sitios-reales)
3. [Estrategia de multiples breakpoints](#3-estrategia-de-multiples-breakpoints)
4. [Bugs y lecciones en este ejercicio](#4-bugs-y-lecciones-en-este-ejercicio)
5. [Gradientes como fondos de tarjetas](#5-gradientes-como-fondos-de-tarjetas)
6. [Iconografia web](#6-iconografia-web)
7. [Consideraciones de rendimiento](#7-consideraciones-de-rendimiento)
8. [Checklist de proyecto completo](#8-checklist-de-proyecto-completo)
9. [Ejercicios de practica](#9-ejercicios-de-practica)

---

## 1. Planificacion de un proyecto web

### El proceso de diseno

Todo proyecto web profesional sigue un flujo antes de escribir codigo:

```
  ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐
  │          │    │          │    │          │    │          │
  │ BRIEF    │───→│ WIREFRAME│───→│ MOCKUP   │───→│ CODIGO   │
  │          │    │          │    │          │    │          │
  └──────────┘    └──────────┘    └──────────┘    └──────────┘
  Que necesita    Estructura      Diseno visual    Implementacion
  el cliente      y layout        con colores,     en HTML, CSS
                  (sin color,     tipografia,      y JavaScript
                  solo cajas)     imagenes
```

### Wireframe de nuestro proyecto

Antes de codificar, asi se veria el wireframe de la pagina de servicios:

```
  MOVIL (< 560px)            TABLET (560-768px)         DESKTOP (> 768px)
  ┌──────────────┐           ┌────────────────────┐      ┌──────────────────────────┐
  │   [LOGO]     │           │      [LOGO]        │      │ [LOGO]                   │
  ├──────────────┤           ├────────────────────┤      ├──────────────────────────┤
  │ NAV NAV NAV  │           │  NAV  NAV NAV NAV  │      │  NAV  NAV  NAV  NAV     │
  ├──────────────┤           ├─────────┬──────────┤      ├──────┬──────┬─────┬─────┤
  │              │           │         │          │      │      │      │     │     │
  │  Tarjeta 1   │           │ Tarjeta │ Tarjeta  │      │ T.1  │ T.2  │ T.3 │ T.4 │
  │              │           │   1     │   2      │      │      │      │     │     │
  ├──────────────┤           │         │          │      │      │      │     │     │
  │              │           ├─────────┼──────────┤      │      │      │     │     │
  │  Tarjeta 2   │           │         │          │      │      │      │     │     │
  │              │           │ Tarjeta │ Tarjeta  │      └──────┴──────┴─────┴─────┘
  ├──────────────┤           │   3     │   4      │      │       (c) WebB2B         │
  │              │           │         │          │      └──────────────────────────┘
  │  Tarjeta 3   │           └─────────┴──────────┤
  │              │           │    (c) WebB2B       │
  ├──────────────┤           └────────────────────┘
  │              │
  │  Tarjeta 4   │
  │              │
  ├──────────────┤
  │ (c) WebB2B   │
  └──────────────┘
```

### Organizacion de archivos

Para un proyecto pequeno como este, una estructura plana es suficiente:

```
  08-proyecto-web-servicios/
  ├── index.html          ← Estructura HTML (unico archivo HTML)
  ├── styles.css          ← Todos los estilos CSS
  └── images/             ← Recursos graficos
      ├── logo.png        ← Logo de la empresa
      ├── ico_sistemas.png
      ├── ico_apps.png
      ├── ico_web.png
      └── ico_consultoria.png
```

Para proyectos mas grandes, la organizacion crece:

```
  proyecto-profesional/
  ├── index.html
  ├── css/
  │   ├── reset.css           ← Reset/normalize
  │   ├── variables.css       ← Custom properties
  │   ├── layout.css          ← Grid y estructura
  │   ├── components.css      ← Tarjetas, botones, nav
  │   └── responsive.css      ← Media queries
  ├── images/
  │   ├── icons/
  │   ├── photos/
  │   └── logo/
  ├── fonts/                  ← Tipografias locales
  └── js/                     ← JavaScript
```

### El inventario de componentes

Antes de codificar, lista TODOS los componentes que necesitas. Para nuestro proyecto:

```
  ┌─────────────────────────────────────────────────┐
  │  INVENTARIO DE COMPONENTES — WebB2B             │
  ├──────────────────────┬──────────────────────────┤
  │ Componente           │ Elemento HTML            │
  ├──────────────────────┼──────────────────────────┤
  │ Logo                 │ <img> dentro de <header> │
  │ Navegacion principal │ <nav> con <ul>/<li>/<a>  │
  │ Tarjeta de servicio  │ <article class="cajita"> │
  │   - Titulo           │   <h2>                   │
  │   - Icono            │   <img>                  │
  │   - Descripcion      │   <p>                    │
  │ Grid de tarjetas     │ <div class="contenedor"> │
  │ Footer               │ <footer>                 │
  └──────────────────────┴──────────────────────────┘
```

---

## 2. Estructura semantica para sitios reales

### Como elegir los elementos correctos

La eleccion de elementos HTML no es arbitraria. Cada elemento tiene un
**significado semantico** que comunica la funcion del contenido a navegadores,
lectores de pantalla y motores de busqueda.

```
  ESTRUCTURA SEMANTICA de nuestro proyecto:

  <body>
  │
  ├── <header role="banner">         ← Encabezado del sitio
  │   └── <img class="logo">        ← Logo de la empresa
  │
  ├── <nav aria-label="...">        ← Navegacion principal
  │   └── <ul>
  │       ├── <li><a>NOSOTROS</a>
  │       ├── <li><a>SERVICIOS</a>
  │       ├── <li><a>CONTACTO</a>
  │       └── <li><a>PROYECTOS</a>
  │
  ├── <main>                         ← Contenido principal (UNICO)
  │   └── <div class="contenedor">  ← Wrapper de layout (sin semantica)
  │       ├── <article class="cajita sistemas">
  │       │   ├── <h2>DESARROLLO DE SISTEMAS</h2>
  │       │   ├── <img alt="Icono de...">
  │       │   └── <p>Descripcion...</p>
  │       ├── <article class="cajita aplicaciones">
  │       ├── <article class="cajita web">
  │       └── <article class="cajita consultorias">
  │
  └── <footer role="contentinfo">    ← Pie de pagina
      └── (c) WebB2B 2021
```

### ¿Por que `<article>` y no `<div>` para las tarjetas?

Se usa `<article>` porque cada tarjeta de servicio es un **bloque de
contenido autocontenido**: tiene titulo, imagen y descripcion. Podria
publicarse de manera independiente (en un newsletter, una red social,
otro sitio) y seguiria teniendo sentido completo.

```
  ¿Cuando usar <article> vs <div> vs <section>?

  ┌──────────────────────────────────────────────────────────────────┐
  │ ¿Tiene sentido el contenido fuera de su contexto actual?         │
  │                                                                  │
  │  SI ──→ <article>                                                │
  │         Ejemplos: post de blog, tarjeta de producto, comentario  │
  │                                                                  │
  │  NO ──→ ¿Agrupa contenido tematico relacionado?                  │
  │          │                                                       │
  │          ├── SI ──→ <section>                                    │
  │          │         Ejemplo: seccion "Sobre nosotros" de una      │
  │          │         pagina, capitulo de un documento               │
  │          │                                                       │
  │          └── NO ──→ <div>                                        │
  │                    Ejemplo: wrapper para layout, contenedor      │
  │                    visual sin significado semantico               │
  └──────────────────────────────────────────────────────────────────┘
```

### Patron Header: logo + navegacion

Nuestro proyecto separa `<header>` y `<nav>` como elementos hermanos:

```html
<header role="banner">
    <img src="images/logo.png" alt="Logo de WebB2B" class="logo">
</header>
<nav aria-label="Navegacion principal">
    <ul>...</ul>
</nav>
```

Otra opcion comun (igualmente valida) es anidar el nav dentro del header:

```html
<header role="banner">
    <img src="images/logo.png" alt="Logo de WebB2B" class="logo">
    <nav aria-label="Navegacion principal">
        <ul>...</ul>
    </nav>
</header>
```

Ambos patrones son semanticamente correctos. La diferencia es de organizacion
y estilo.

### Patron de tarjetas (Card Grid)

Las tarjetas son uno de los patrones mas usados en la web moderna. La estructura
tipica es:

```
  ┌─────────────────────────┐
  │  ┌───────────────────┐  │
  │  │     TITULO         │  │  ← <h2> o <h3>
  │  └───────────────────┘  │
  │  ┌───────────────────┐  │
  │  │                   │  │
  │  │     IMAGEN        │  │  ← <img> con alt descriptivo
  │  │                   │  │
  │  └───────────────────┘  │
  │                         │
  │  Texto descriptivo del  │  ← <p>
  │  servicio o producto.   │
  │                         │
  │  [Boton de accion]      │  ← <a> o <button> (opcional)
  │                         │
  └─────────────────────────┘
       <article class="cajita">
```

### Patron Footer

```html
<footer role="contentinfo">
    &copy; WebB2B 2021
</footer>
```

Entidades HTML usadas en footers:

| Entidad   | Resultado | Nombre                    |
|-----------|-----------|---------------------------|
| `&copy;`  | (c)       | Simbolo de copyright      |
| `&reg;`   | (R)       | Marca registrada          |
| `&trade;` | (TM)      | Trademark                 |
| `&amp;`   | &         | Ampersand                 |
| `&nbsp;`  | (espacio) | Espacio que no se rompe   |
| `&mdash;` | --        | Guion largo (em dash)     |

---

## 3. Estrategia de multiples breakpoints

### Filosofia: breakpoints basados en CONTENIDO, no en dispositivos

```
  ✗ INCORRECTO: "Voy a poner un breakpoint a 768px porque es el iPad"
  ✓ CORRECTO:   "A 560px mi contenido deja de verse bien en una columna,
                 asi que aqui cambio a dos columnas"
```

Los breakpoints deben definirse donde el **contenido** lo necesita, no donde
un dispositivo especifico tiene su resolucion.

### Los breakpoints de nuestro proyecto

```css
/* Movil (estilos base, sin media query): < 560px */
/* Tablet: 560px - 768px */
/* Desktop: > 768px */
```

```
  Progresion del layout:

  < 560px (Movil)        560-768px (Tablet)      > 768px (Desktop)
  1 columna              2 columnas               4 columnas

  ┌──────────┐           ┌─────┬─────┐           ┌────┬────┬────┬────┐
  │ Sistemas │           │Sist.│Apps │           │Sis │App │Web │Con │
  ├──────────┤           ├─────┼─────┤           │    │    │    │    │
  │   Apps   │           │ Web │Cons.│           │    │    │    │    │
  ├──────────┤           └─────┴─────┘           └────┴────┴────┴────┘
  │   Web    │
  ├──────────┤
  │ Consult. │
  └──────────┘

  flex-direction:         flex-direction:           flex-direction:
    column                  row                       row
  flex: 1 1 100%          flex: 1 1 45%             flex: 1 1 calc(100%/4)
                          flex-wrap: wrap            flex-wrap: nowrap
```

### El proceso de prueba de breakpoints

```
  1. Empieza con el navegador en el ancho MAS ESTRECHO (~320px)
  2. Aumenta el ancho LENTAMENTE
  3. Cuando algo se "rompe" visualmente → necesitas un breakpoint
  4. Escribe el media query para ESE ancho
  5. Continua aumentando hasta el ancho maximo

  ┌─────────────────────────────────────────────────────────────────┐
  │ 320px          560px                 768px              1200px  │
  │  │              │                     │                   │    │
  │  │  1 columna   │    2 columnas       │    4 columnas     │    │
  │  │  (base)      │    (media query 1)  │   (media query 2) │    │
  │  │              │                     │                   │    │
  │  ├──────────────┼─────────────────────┼───────────────────┤    │
  │  │   Contenido  │     Contenido       │     Contenido     │    │
  │  │   se ve bien │     se ve bien      │     se ve bien    │    │
  │  │   en 1 col   │     en 2 cols       │     en 4 cols     │    │
  └─────────────────────────────────────────────────────────────────┘
```

### Patron comun: 1 columna, 2 columnas, 4 columnas

Este patron se usa en nuestro proyecto y es uno de los mas frecuentes en la web:

```css
/* MOVIL — Estilos base (sin media query) */
.contenedor {
  display: flex;
  flex-direction: column;     /* 1 columna */
}
.cajita {
  flex: 1 1 100%;             /* Cada tarjeta = ancho completo */
}

/* TABLET — 2 columnas */
@media (min-width: 560px) and (max-width: 768px) {
  .contenedor {
    flex-direction: row;
    flex-wrap: wrap;           /* Permite salto de linea */
  }
  .cajita {
    flex: 1 1 45%;            /* ~mitad del ancho (2 por fila) */
  }
}

/* DESKTOP — 4 columnas */
@media (min-width: 768px) {
  .contenedor {
    flex-direction: row;
    flex-wrap: nowrap;         /* Todo en una sola fila */
  }
  .cajita {
    flex: 1 1 calc(100% / 4); /* Un cuarto del ancho */
  }
}
```

### Anatomia del `flex` shorthand

El shorthand `flex` tiene tres valores que controlan el comportamiento responsivo:

```
  flex: flex-grow  flex-shrink  flex-basis;
        │          │            │
        │          │            └── Tamanio BASE antes de distribuir espacio
        │          │                (100%, 45%, calc(100%/4), 200px, etc.)
        │          │
        │          └── ¿Puede ENCOGERSE si falta espacio?
        │              0 = no, 1 = si
        │
        └── ¿Puede CRECER si sobra espacio?
            0 = no, 1 = si

  Ejemplos:
  flex: 1 1 100%  → Crece, encoge, base de 100% (ocupa toda la fila)
  flex: 1 1 45%   → Crece, encoge, base de 45% (2 por fila con margen)
  flex: 0 0 200px → No crece, no encoge, siempre 200px
```

---

## 4. Bugs y lecciones en este ejercicio

Este ejercicio contiene **bugs intencionales** como oportunidades de aprendizaje.
Cada bug ensena una leccion importante sobre CSS.

### Bug 1: Orden de media queries (lineas 305 y 346 de styles.css)

**Que esta mal:**

La media query de desktop (`min-width: 768px`) esta ANTES de la de tablet
(`min-width: 560px and max-width: 768px`) en el codigo fuente.

```css
/* PRIMERO en el codigo: desktop */
@media screen and (min-width: 768px) { ... }

/* DESPUES en el codigo: tablet */
@media screen and (min-width: 560px) and (max-width: 768px) { ... }
```

**Que sucede:**

Cuando la pantalla mide exactamente **768px**, AMBAS queries se cumplen:
- `768 >= 768` es verdadero (desktop se activa)
- `560 <= 768 <= 768` es verdadero (tablet se activa)

Por la regla de **cascada CSS** (la ultima regla gana cuando tienen la misma
especificidad), los estilos de tablet sobreescriben a los de desktop.

```
  A 768px exactos:

  Esperado:                        Real:
  ┌────┬────┬────┬────┐           ┌─────────┬─────────┐
  │ T1 │ T2 │ T3 │ T4 │           │   T1    │   T2    │
  └────┴────┴────┴────┘           ├─────────┼─────────┤
  4 columnas (desktop)            │   T3    │   T4    │
                                  └─────────┴─────────┘
                                  2 columnas (tablet!)
```

**Como corregirlo:**

Opcion A: Cambiar el orden (tablet primero, desktop despues):
```css
/* Primero tablet: */
@media screen and (min-width: 560px) and (max-width: 767px) { ... }
/* Despues desktop: */
@media screen and (min-width: 768px) { ... }
```

Opcion B: Evitar solapamiento en los rangos:
```css
/* Tablet: hasta 767px (un pixel menos que desktop) */
@media screen and (min-width: 560px) and (max-width: 767px) { ... }
/* Desktop: desde 768px */
@media screen and (min-width: 768px) { ... }
```

**Leccion:** En CSS, el **orden del codigo importa**. Cuando dos reglas tienen
la misma especificidad y ambas se aplican, la **ultima en el codigo fuente gana**.

---

### Bug 2: Comas en el shorthand `flex` (linea 143 de styles.css)

**Que esta mal:**

```css
li {
  flex: 1, 1, 25%;    /* INCORRECTO */
}
```

**Que deberia ser:**

```css
li {
  flex: 1 1 25%;      /* CORRECTO — separado por ESPACIOS */
}
```

**Que sucede:**

El shorthand `flex` espera valores separados por **espacios**, no por comas.
Con comas, el navegador no puede interpretar correctamente los tres valores.
El resultado es que `flex-basis: 25%` NO se aplica, y los items de navegacion
no ocupan el 25% esperado.

```
  Con comas (bug):                    Con espacios (correcto):

  ┌──────┬──────┬──────┬──────┐      ┌────────┬────────┬────────┬────────┐
  │ NOS  │ SER  │ CON  │ PRO  │      │NOSOTROS│SERVICIOS│CONTACTO│PROYECTOS│
  └──────┴──────┴──────┴──────┘      └────────┴────────┴────────┴────────┘
  Items con tamanio automatico        Items de 25% cada uno (llenan la fila)
```

**Leccion:** Los shorthands CSS separan sus valores con **espacios**, nunca con
comas (excepto funciones como `rgb()`, `linear-gradient()`, etc.). Esta regla
aplica a: `flex`, `margin`, `padding`, `border`, `font`, `background`, etc.

**Referencia rapida de shorthands:**

```
  ✓ flex: 1 1 25%;           (espacios)
  ✓ margin: 10px 20px;       (espacios)
  ✓ border: 1px solid red;   (espacios)
  ✓ font: bold 1.3em Arial;  (espacios)

  ✗ flex: 1, 1, 25%;         (comas — INCORRECTO)
  ✗ margin: 10px, 20px;      (comas — INCORRECTO)
```

---

### Bug 3: `justify-content: left` (linea 316 de styles.css)

**Que esta mal:**

```css
@media screen and (min-width: 768px) {
  header {
    justify-content: left;    /* NO es un valor valido en Flexbox */
  }
}
```

**Que deberia ser:**

```css
header {
  justify-content: flex-start;  /* Valor correcto */
}
```

**Que sucede:**

`left` NO es un valor valido para `justify-content` en el contexto de Flexbox.
Los valores validos son:

| Valor           | Efecto                                           |
|-----------------|--------------------------------------------------|
| `flex-start`    | Items al inicio del eje principal                |
| `flex-end`      | Items al final del eje principal                 |
| `center`        | Items centrados                                  |
| `space-between` | Primer item al inicio, ultimo al final, espacio igual entre ellos |
| `space-around`  | Espacio igual alrededor de cada item             |
| `space-evenly`  | Espacio identico entre y alrededor de cada item  |

**Por que "funciona" en Chrome:**

Algunos navegadores (como Chrome) aceptan `left` como alias de `flex-start`
porque implementan la especificacion CSS Box Alignment Level 3 de forma
anticipada. Pero esto NO es portable: otros navegadores pueden ignorarlo.

```
  Chrome:                            Otros navegadores:
  justify-content: left              justify-content: left
  → Interpreta como flex-start       → Valor invalido, se ignora
  → Logo se mueve a la izquierda     → Logo se queda centrado (estilo base)

  ┌─────────────────────┐            ┌─────────────────────┐
  │[Logo]               │            │      [Logo]         │
  └─────────────────────┘            └─────────────────────┘
  Solo en Chrome                     En Firefox, Safari, etc.
```

**Leccion:** Siempre usa los valores **estandar** de la especificacion.
"Si funciona en mi navegador" no significa que sea correcto.

---

## 5. Gradientes como fondos de tarjetas

### La funcion `linear-gradient()`

En nuestro proyecto, cada tarjeta tiene un gradiente que va del color tematico
al blanco:

```css
.sistemas {
  background: linear-gradient(180deg, var(--azulclaro), #ffffff);
}
```

### Direccion del gradiente

```
  linear-gradient(ANGULO, color-inicio, color-fin)

     0deg          90deg         180deg         270deg
    (abajo→arriba) (izq→der)    (arriba→abajo) (der→izq)

    ┌─────────┐   ┌─────────┐   ┌─────────┐   ┌─────────┐
    │ #ffffff  │   │         │   │ #color   │   │         │
    │         │   │ #color →│   │         │   │← #color │
    │         │   │         │   │         │   │         │
    │ #color   │   │ #ffffff │   │ #ffffff  │   │ #ffffff │
    └─────────┘   └─────────┘   └─────────┘   └─────────┘

  Nuestro proyecto usa 180deg: color arriba, blanco abajo.
```

### Angulos y palabras clave equivalentes

| Angulo   | Palabra clave     | Direccion                 |
|----------|-------------------|---------------------------|
| `0deg`   | `to top`          | De abajo hacia arriba     |
| `45deg`  | `to top right`    | Diagonal hacia arriba-der |
| `90deg`  | `to right`        | De izquierda a derecha    |
| `180deg` | `to bottom`       | De arriba hacia abajo     |
| `270deg` | `to left`         | De derecha a izquierda    |

### El patron "desvanecimiento al blanco"

Nuestro proyecto usa un patron muy comun en diseno web: un color solido que
se desvanece gradualmente hacia blanco. Esto tiene dos propositos:

1. **Legibilidad:** El texto oscuro es facil de leer contra el blanco del fondo
2. **Profesionalismo:** Es mas sutil y elegante que un color solido

```
  Tarjeta con gradiente:
  ┌─────────────────────────┐
  │ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ │  ← Color tematico (azul, naranja, etc.)
  │ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ │
  │ ░░░░░░░░░░░░░░░░░░░░░ │  ← Transicion gradual
  │ ░░░░░░░░░░░░░░░░░░░░░ │
  │                         │  ← Blanco (texto legible aqui)
  │                         │
  └─────────────────────────┘
```

### Colores tematicos del proyecto

```css
:root {
  --azulclaro: #b0e1ff;   /* Sistemas — confianza, tecnologia */
  --naranja:   #fbb273;   /* Aplicaciones — energia, creatividad */
  --verde:     #8cfe84;   /* Web — crecimiento, innovacion */
  --morado:    #efa3fb;   /* Consultoria — sabiduria, experiencia */
}
```

### Psicologia del color en contextos de negocios

| Color     | Asociaciones comunes                  | Uso tipico                     |
|-----------|---------------------------------------|--------------------------------|
| Azul      | Confianza, seguridad, tecnologia      | Bancos, tech, salud            |
| Naranja   | Energia, creatividad, entusiasmo      | Startups, entretenimiento      |
| Verde     | Crecimiento, naturaleza, exito        | Ecologia, finanzas, salud      |
| Morado    | Sabiduria, lujo, creatividad          | Consultoria, educacion, beauty |
| Rojo      | Urgencia, pasion, atencion            | Ventas, alimentos, emergencias |

### Gradientes avanzados (para explorar)

```css
/* Multiples colores: */
background: linear-gradient(180deg, #b0e1ff, #a3d1ff 50%, #ffffff);

/* Gradiente radial (circular): */
background: radial-gradient(circle, #b0e1ff, #ffffff);

/* Gradiente con parada definida: */
background: linear-gradient(180deg, #b0e1ff 0%, #b0e1ff 30%, #ffffff 100%);
/* El color azul se mantiene solido hasta el 30%, luego transiciona */
```

---

## 6. Iconografia web

### Tipos de iconos en la web

Nuestro proyecto usa **imagenes PNG** para los iconos. Existen tres enfoques
principales:

| Tipo            | Formato        | Ventajas                          | Desventajas                    |
|-----------------|----------------|-----------------------------------|--------------------------------|
| Imagenes raster | PNG, JPG, WebP | Facil de usar, fotografias        | No escalan bien, peso grande   |
| Icon fonts      | WOFF, TTF      | Escalables, coloreables con CSS   | Un solo color, carga de fuente |
| SVG             | SVG            | Escalables, multicolor, animables | Mas complejo de implementar    |

```
  COMPARACION VISUAL:

  PNG (raster):          Icon Font:           SVG (vectorial):
  ┌──────────┐           ┌──────────┐         ┌──────────┐
  │ ██  ██   │           │    ☁     │         │   /\     │
  │ ██████   │ x2 →      │   font:  │ x2 →    │  /  \    │ x2 →
  │ ██  ██   │ pixelado  │   2em    │ nitido  │ /____\   │ nitido
  └──────────┘           └──────────┘         └──────────┘
  Resolucion fija        Escala perfecto      Escala perfecto
```

### Alt text para iconos

En nuestro proyecto, los iconos tienen alt text descriptivo:

```html
<img src="images/ico_sistemas.png" alt="Icono de desarrollo de sistemas">
<img src="images/ico_apps.png" alt="Icono de desarrollo de aplicaciones">
```

**Reglas para alt text en iconos:**

| Situacion                          | Que hacer                               | Ejemplo                                   |
|------------------------------------|-----------------------------------------|-------------------------------------------|
| Icono con significado unico        | Alt text descriptivo                    | `alt="Icono de desarrollo de sistemas"`   |
| Icono decorativo (junto a texto)   | Alt vacio + aria-hidden                 | `alt="" aria-hidden="true"`               |
| Icono como unico contenido de link | Alt que describe la accion              | `alt="Ir al inicio"`                      |
| Logo                               | Alt con nombre de la empresa            | `alt="Logo de WebB2B"`                    |

**Cuando usar alt vacio vs aria-hidden:**

```html
<!-- Icono DECORATIVO junto a texto que ya lo describe: -->
<button>
  <img src="search.png" alt="" aria-hidden="true">
  Buscar
</button>
<!-- El texto "Buscar" ya comunica la funcion. El icono es decorativo. -->

<!-- Icono que ES el unico contenido: -->
<button>
  <img src="search.png" alt="Buscar">
</button>
<!-- Sin el alt, el boton seria invisible para lectores de pantalla. -->
```

### Dimensionamiento responsivo de iconos

En nuestro proyecto, las imagenes (incluidos iconos) se dimensionan con porcentaje:

```css
img {
  width: 60%;       /* 60% del ancho del contenedor */
  height: auto;     /* Mantiene la proporcion */
  display: block;   /* Necesario para que margin auto funcione */
  margin: 0 auto;   /* Centra horizontalmente */
}
```

**Por que `display: block` es necesario:**

```
  <img> es un elemento INLINE por defecto.
  margin: 0 auto NO funciona en elementos inline.

  display: inline (defecto):        display: block:
  ┌──────────────────────┐          ┌──────────────────────┐
  │    [img]texto         │          │                      │
  │                      │          │       [img]           │  ← centrado
  └──────────────────────┘          │                      │
  No se puede centrar con           └──────────────────────┘
  margin auto                       margin: 0 auto funciona
```

---

## 7. Consideraciones de rendimiento

### Optimizacion de imagenes

Las imagenes son tipicamente el recurso **mas pesado** de una pagina web.
Optimizarlas tiene el mayor impacto en el rendimiento.

```
  Pagina web tipica — distribucion del peso:

  ┌──────────────────────────────────────────────────┐
  │████████████████████████████████████ Imagenes: 60% │
  │████████████ CSS: 15%                              │
  │██████ JavaScript: 10%                             │
  │████ HTML: 5%                                      │
  │████ Fuentes: 5%                                   │
  │███ Otros: 5%                                      │
  └──────────────────────────────────────────────────┘
```

**Checklist de optimizacion de imagenes:**

| Tecnica                  | Que hacer                                              |
|--------------------------|--------------------------------------------------------|
| Formato correcto         | PNG para iconos, JPG para fotos, WebP para ambos       |
| Dimensiones correctas    | No cargar una imagen de 2000px si se muestra a 200px   |
| Compresion               | Usar herramientas como TinyPNG, Squoosh, ImageOptim    |
| Atributo width y height  | Definir dimensiones en HTML para evitar layout shift    |
| Lazy loading             | `loading="lazy"` para imagenes fuera del viewport       |

### Especificidad CSS y organizacion

La organizacion del CSS afecta tanto la mantenibilidad como el rendimiento:

```
  ORDEN RECOMENDADO de un archivo CSS:

  1. Variables (:root)           ← Primero: valores reutilizables
  2. Reset/Normalize             ← Segundo: eliminar estilos del navegador
  3. Estilos base (body, h1-h6)  ← Tercero: tipografia y colores base
  4. Layout (header, nav, main)  ← Cuarto: estructura de la pagina
  5. Componentes (.cajita, .btn) ← Quinto: estilos de componentes
  6. Utilidades (.text-center)   ← Sexto: clases de uso general
  7. Media queries               ← Ultimo: adaptaciones responsivas
```

### La ruta critica de renderizado

```
  Navegador recibe HTML
        │
        ├── Parsea HTML → Construye DOM
        │                      │
        │                      │ (bloqueo)
        │                      ▼
        ├── Descarga CSS → Parsea CSS → Construye CSSOM
        │                                    │
        │                                    │
        ▼                                    ▼
  Combina DOM + CSSOM → Render Tree → Layout → Paint → Display
                                      (donde va    (colores,
                                      cada cosa)   sombras)

  ¿Que bloquea el renderizado?
  - CSS: SIEMPRE bloquea (el navegador espera a tener todo el CSS)
  - Imagenes: NO bloquean (se muestran cuando llegan)
  - JS: Puede bloquear (depende de donde se coloque)
```

**Consejos practicos:**

1. **Un solo archivo CSS** para proyectos pequenos (como el nuestro)
2. **Minimizar CSS** en produccion (eliminar espacios, comentarios)
3. **Evitar selectores complejos** (`.contenedor > div:nth-child(3) > p:first-of-type`)
4. **No duplicar propiedades** (como el `align-items: center` repetido en nuestro `nav`)

---

## 8. Checklist de proyecto completo

### Checklist de accesibilidad

```
  [ ] Todas las imagenes tienen atributo alt descriptivo
  [ ] El alt text describe lo que REPRESENTA la imagen, no solo "imagen"
  [ ] Los iconos decorativos tienen alt="" y aria-hidden="true"
  [ ] El <html> tiene lang="es" (idioma del contenido)
  [ ] Se usa <header>, <nav>, <main>, <footer> en lugar de <div>
  [ ] Roles ARIA donde sean necesarios (role="banner", role="contentinfo")
  [ ] <nav> tiene aria-label para diferenciarse de otras navegaciones
  [ ] Solo hay UN <main> por pagina
  [ ] El contraste de color entre texto y fondo es suficiente (4.5:1 minimo)
  [ ] Los enlaces son claramente identificables (color, subrayado)
  [ ] El sitio es navegable con teclado (Tab, Enter, Escape)
  [ ] El orden de tabulacion es logico (sigue el flujo visual)
```

### Checklist responsive

```
  [ ] Tiene <meta name="viewport" content="width=device-width, initial-scale=1.0">
  [ ] Los estilos base son MOBILE-FIRST (sin media query = movil)
  [ ] Las imagenes usan width en porcentaje o max-width: 100%
  [ ] No hay scroll horizontal en ninguna resolucion
  [ ] El texto es legible sin hacer zoom (minimo ~16px en movil)
  [ ] Los botones y enlaces tienen area de toque suficiente (44x44px minimo)
  [ ] Se probaron al menos 3 anchos: ~375px, ~768px, ~1200px
  [ ] Los media queries no se solapan (ver Bug 1 de este ejercicio)
  [ ] El contenido no se desborda de su contenedor en ninguna resolucion
  [ ] Las tarjetas cambian de 1 columna (movil) a 2 (tablet) a 4 (desktop)
```

### Checklist de rendimiento

```
  [ ] Las imagenes estan optimizadas (comprimidas, tamanio correcto)
  [ ] Los formatos de imagen son apropiados (PNG, JPG, WebP)
  [ ] El CSS no tiene propiedades duplicadas innecesarias
  [ ] No hay archivos CSS o JS que no se usen
  [ ] Las imagenes fuera del viewport tienen loading="lazy"
  [ ] El archivo CSS esta organizado logicamente
  [ ] Los selectores CSS son simples y eficientes
```

### Checklist de SEO basico

```
  [ ] El <title> es descriptivo y unico para la pagina
  [ ] Hay un <meta name="description"> con resumen del contenido
  [ ] Se usa la jerarquia correcta de headings (h1 → h2 → h3, sin saltar)
  [ ] Solo hay UN <h1> por pagina (o uno por <article>/<section>)
  [ ] Los enlaces tienen texto descriptivo (no "clic aqui")
  [ ] Las imagenes tienen alt text (Google lo usa para indexar imagenes)
  [ ] La URL es descriptiva y legible
  [ ] El sitio carga rapido (las senales de rendimiento afectan el SEO)
  [ ] El sitio es responsivo (Google prioriza sitios mobile-friendly)
```

### Aplicando las checklists a NUESTRO proyecto

**Lo que nuestro proyecto hace bien:**

```
  ✓ Imagenes con alt descriptivo ("Logo de WebB2B", "Icono de...")
  ✓ Estructura semantica (header, nav, main, footer, article)
  ✓ Roles ARIA (role="banner", role="contentinfo", aria-label)
  ✓ Idioma declarado (lang="es")
  ✓ Viewport meta tag presente
  ✓ Enfoque mobile-first (estilos base = movil)
  ✓ Variables CSS para colores reutilizables
  ✓ Gradientes profesionales para las tarjetas
```

**Lo que se podria mejorar:**

```
  ✗ Falta <meta name="description">
  ✗ Bugs de CSS (flex con comas, justify-content: left, orden de queries)
  ✗ Imagenes sin width/height en HTML (puede causar layout shift)
  ✗ No hay loading="lazy" en imagenes
  ✗ align-items duplicado en nav (lineas 108 y 112 de styles.css)
  ✗ No hay un <h1> visible en la pagina (solo h2 en tarjetas)
  ✗ Los enlaces de navegacion no llevan a ninguna parte (href="#")
```

---

## 9. Ejercicios de practica

Los siguientes ejercicios estan pensados para practicar con los archivos
`index.html` y `styles.css` de esta misma carpeta (modulo 08).

### Ejercicio 1 — Corregir los tres bugs del CSS

**Objetivo:** Depurar CSS leyendo el codigo y entendiendo las especificaciones.

Abre `styles.css` y corrige estos tres bugs:

1. **Bug de orden** (lineas 305 y 346): Reorganiza las media queries o ajusta
   los rangos para que no se solapen.

2. **Bug de comas** (linea 143): Cambia `flex: 1, 1, 25%` por `flex: 1 1 25%`.

3. **Bug de justify-content** (linea 316): Cambia `justify-content: left` por
   `justify-content: flex-start`.

Despues de cada correccion, recarga la pagina y observa la diferencia. Usa
DevTools para verificar que los valores se aplican correctamente (en el panel
Computed, los valores invalidos aparecen tachados).

---

### Ejercicio 2 — Agregar una quinta tarjeta

**Objetivo:** Entender como Flexbox redistribuye el espacio.

1. En `index.html`, agrega un nuevo `<article>` dentro de `.contenedor`:
   ```html
   <article class="cajita soporte">
       <h2 class="titulo-cajita">SOPORTE TECNICO</h2>
       <img src="images/ico_consultoria.png" alt="Icono de soporte tecnico">
       <p>Ofrecemos soporte tecnico 24/7 para todos nuestros clientes...</p>
   </article>
   ```

2. En `styles.css`, agrega el gradiente:
   ```css
   .soporte {
     background: linear-gradient(180deg, #ffd700, #ffffff);
   }
   ```

3. Observa:
   - ¿Que pasa en desktop con `flex: 1 1 calc(100% / 4)` y 5 tarjetas?
   - ¿Como lo arreglarias para que quepan 5 en una fila?
   - ¿Que pasa en tablet con 5 tarjetas? (2+2+1 o 3+2?)

---

### Ejercicio 3 — Agregar un breakpoint intermedio

**Objetivo:** Practicar el diseno de breakpoints basado en contenido.

Agrega un breakpoint para pantallas grandes (> 1200px) que muestre las
tarjetas con mayor padding y fuente mas grande:

```css
@media screen and (min-width: 1200px) {
  .cajita {
    padding: 2rem;
    font-size: 1.1rem;
  }
  .titulo-cajita {
    font-size: 1.6em;
  }
  .logo {
    width: 200px;
  }
}
```

Experimenta con los valores hasta que el resultado se vea proporcionado.

---

### Ejercicio 4 — Convertir a CSS Grid

**Objetivo:** Comparar Flexbox vs Grid para el mismo layout.

Reescribe `.contenedor` usando CSS Grid en lugar de Flexbox:

```css
/* MOVIL (base): */
.contenedor {
  display: grid;
  grid-template-columns: 1fr;
  gap: 20px;
}

/* TABLET: */
@media screen and (min-width: 560px) and (max-width: 767px) {
  .contenedor {
    grid-template-columns: 1fr 1fr;
  }
}

/* DESKTOP: */
@media screen and (min-width: 768px) {
  .contenedor {
    grid-template-columns: repeat(4, 1fr);
  }
}
```

Compara: ¿Cuantas lineas de CSS necesitaste con Grid vs Flexbox?
¿Cual te parece mas claro?

---

### Ejercicio 5 — Eliminar la propiedad duplicada

**Objetivo:** Identificar y limpiar codigo CSS redundante.

1. Abre `styles.css` y busca la regla `nav` (lineas 105-113)
2. Identifica la propiedad que aparece DOS VECES
3. Elimina la declaracion duplicada
4. Verifica que el comportamiento visual no cambia

---

### Ejercicio 6 — Agregar hover a las tarjetas

**Objetivo:** Practicar transiciones CSS y estados interactivos.

Agrega un efecto hover a las tarjetas que las "levante" visualmente:

```css
.cajita {
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.cajita:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15);
}
```

Luego experimenta:
- Cambia `translateY(-5px)` por `scale(1.02)`. ¿Que efecto prefieres?
- Agrega `cursor: pointer` para indicar interactividad
- ¿Como harias que la transicion sea mas lenta al salir del hover?

---

### Ejercicio 7 — Agregar un h1 a la pagina

**Objetivo:** Mejorar la semantica y el SEO.

La pagina actual no tiene un `<h1>`. Agrega uno dentro de `<main>`, antes
de `.contenedor`:

```html
<main>
    <h1>Nuestros Servicios</h1>
    <div class="contenedor">
        ...
    </div>
</main>
```

Aplica estilos al `h1`:
```css
main > h1 {
  text-align: center;
  color: var(--azulmarino);
  font-size: 2rem;
  margin: 1.5rem 0;
}
```

---

### Ejercicio 8 — Auditoria completa del proyecto

**Objetivo:** Aplicar las checklists de la seccion 8 al proyecto real.

1. Abre `index.html` y `styles.css`
2. Revisa cada punto de las 4 checklists (accesibilidad, responsive,
   rendimiento, SEO)
3. Anota todo lo que falta o esta mal
4. Implementa al menos 3 mejoras de tu lista
5. Verifica que el sitio sigue funcionando correctamente despues de los cambios

---

### Ejercicio 9 — Investigacion: formatos de imagen modernos

**Objetivo:** Investigar alternativas a PNG para los iconos.

1. Abre cada archivo de `images/` y observa su peso (usa DevTools > Network)
2. Investiga: ¿Cuanto pesarian en formato WebP? ¿Y en SVG?
3. Busca una herramienta online para convertir PNG a WebP (ejemplo: Squoosh)
4. Convierte un icono y compara la calidad visual y el peso
5. Reflexiona: ¿Tiene sentido convertir iconos pequenos a WebP, o seria
   mejor pasarlos a SVG directamente?

---

**Modulo anterior:** [07 - CSS Grid](../07-responsive-css-grid/)
**Siguiente modulo:** [09 - Portfolio Profesional](../09-portfolio-profesional/)
donde construiremos un portfolio completo aplicando todos los conceptos
aprendidos en los modulos 01-08.

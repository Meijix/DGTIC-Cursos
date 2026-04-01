# Modulo 06 — Diseno Responsive: Fundamentos

> **Archivos de referencia:** `index.html` y `styles.css` en esta misma carpeta.
> **Prerequisitos:** Modulos 01-05 (HTML, CSS, Flexbox, componentes).

---

## Indice

1. [Que es Responsive Web Design](#1-que-es-responsive-web-design)
2. [Mobile-First vs Desktop-First](#2-mobile-first-vs-desktop-first)
3. [Media Queries en profundidad](#3-media-queries-en-profundidad)
4. [Unidades fluidas](#4-unidades-fluidas)
5. [Flexbox para layouts de pagina](#5-flexbox-para-layouts-de-pagina)
6. [El viewport meta tag](#6-el-viewport-meta-tag)
7. [Imagenes responsivas](#7-imagenes-responsivas)
8. [Errores comunes](#8-errores-comunes)
9. [Ejercicios de practica](#9-ejercicios-de-practica)

---

## 1. Que es Responsive Web Design

En 2010, Ethan Marcotte publico el articulo "Responsive Web Design" en
A List Apart, definiendo tres pilares fundamentales:

```
  +==================================================================+
  |                                                                  |
  |                    RESPONSIVE WEB DESIGN                         |
  |                                                                  |
  |  +------------------+  +------------------+  +------------------+|
  |  |                  |  |                  |  |                  ||
  |  |  1. CUADRICULAS  |  |  2. IMAGENES     |  |  3. MEDIA        ||
  |  |     FLUIDAS      |  |     FLEXIBLES    |  |     QUERIES      ||
  |  |  (Fluid Grids)   |  |  (Flexible       |  |  (Consultas      ||
  |  |                  |  |   Images)        |  |   de medios)     ||
  |  |  Anchos en %     |  |  max-width:100%  |  |  @media (...)    ||
  |  |  en vez de px    |  |  Las imagenes    |  |  Adaptan el      ||
  |  |  fijos           |  |  se adaptan      |  |  CSS segun el    ||
  |  |                  |  |  a su contenedor |  |  tamano de       ||
  |  |                  |  |                  |  |  pantalla         ||
  |  +------------------+  +------------------+  +------------------+|
  |                                                                  |
  +==================================================================+
```

### Por que importa el diseno responsive

```
  ESTADISTICAS GLOBALES (datos aproximados):
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  - ~60% del trafico web mundial viene de dispositivos moviles
  - Google usa Mobile-First Indexing desde 2019:
    evalua primero la VERSION MOVIL de tu sitio para el ranking
  - Un sitio no responsive pierde ~50% de sus visitantes potenciales

  CONSECUENCIAS:
  ~~~~~~~~~~~~~~
  - SEO: Google penaliza sitios no responsive
  - UX: usuarios frustrados abandonan el sitio
  - Accesibilidad: personas con pantallas pequenas no pueden navegar
  - Negocio: menos conversiones, menos ventas
```

### Responsive vs Adaptive vs Fluid

Estos tres terminos se confunden frecuentemente:

```
  TERMINO      | DEFINICION                        | COMO FUNCIONA
  -------------|-----------------------------------|-------------------------------
  RESPONSIVE   | Se adapta CONTINUAMENTE a          | Usa %, viewport units,
               | cualquier tamano de pantalla       | media queries. El layout
               |                                   | cambia de forma fluida.
               |                                   |
               |    [====]                          |
               |    [========]                      |
               |    [==============]                |
               |    (se estira suavemente)          |
  -------------|-----------------------------------|-------------------------------
  ADAPTIVE     | Tiene LAYOUTS FIJOS               | Se define un layout especifico
               | predefinidos para ciertos          | para cada breakpoint. Entre
               | tamanos de pantalla               | breakpoints, NO cambia.
               |                                   |
               |    [====]                          |
               |    [====]                          |
               |    [=========]     <-- salta       |
               |    [=========]                     |
               |    [================]  <-- salta   |
  -------------|-----------------------------------|-------------------------------
  FLUID        | Usa solo anchos en %              | El contenido se estira o
               | sin breakpoints                    | encoge proporcionalmente.
               |                                   | NO reorganiza el layout.
               |                                   |
               |    [ A  ][ B  ]                    |
               |    [ A    ][ B    ]                |
               |    [ A        ][ B        ]        |
               |    (siempre la misma estructura)   |
```

**Responsive** combina lo mejor de ambos: es **fluido** entre breakpoints
y **se adapta** en los breakpoints cambiando el layout.

---

## 2. Mobile-First vs Desktop-First

### Comparacion directa de codigo

```css
/* =================================================
   DESKTOP-FIRST (NO recomendado)
   =================================================
   Los estilos BASE son para escritorio.
   Las media queries "deshacen" la complejidad.
*/

.sidebar {
    width: 300px;               /* escritorio: ancho fijo */
    float: left;                /* escritorio: al lado del contenido */
    margin-right: 20px;
}

.content {
    margin-left: 320px;         /* escritorio: deja espacio para sidebar */
}

@media (max-width: 768px) {
    .sidebar {
        width: 100%;            /* movil: HAY QUE DESHACER todo */
        float: none;            /* movil: quitar el float */
        margin-right: 0;        /* movil: quitar el margen */
    }
    .content {
        margin-left: 0;         /* movil: quitar el margen */
    }
}

/* Total: 12 declaraciones CSS. 4 solo para "deshacer". */


/* =================================================
   MOBILE-FIRST (RECOMENDADO)
   =================================================
   Los estilos BASE son para movil.
   Las media queries AGREGAN complejidad.
*/

.sidebar {
    /* Movil: nada. Los bloques ya ocupan 100% y se apilan solos. */
}

.content {
    /* Movil: nada. Ya ocupa 100%. */
}

@media (min-width: 768px) {
    .contenedor {
        display: flex;          /* escritorio: activa layout lado a lado */
    }
    .sidebar {
        flex: 0 0 300px;        /* escritorio: 300px fijo */
    }
    .content {
        flex: 1;                /* escritorio: ocupa el resto */
    }
}

/* Total: 5 declaraciones CSS. 0 para "deshacer". MAS LIMPIO. */
```

### El modelo mental

```
  DESKTOP-FIRST:                    MOBILE-FIRST:

  Empiezas con TODO                 Empiezas con lo MINIMO
  y luego QUITAS                    y luego AGREGAS

  +=======================+        +======+
  |  Layout complejo      |        | Base |
  |  con sidebar, grid,   |        | solo |
  |  multiples columnas   |        | una  |
  +=======================+        | col  |
          |                        +======+
          | @media (max-width)           |
          v                              | @media (min-width)
  +===========+                          v
  | Deshaces  |                    +==============+
  | sidebar,  |                    | Agregas      |
  | quitas    |                    | sidebar,     |
  | columnas  |                    | columnas     |
  +===========+                    +==============+
                                         |
                                         | @media (min-width: mas grande)
                                         v
                                   +=======================+
                                   | Agregas mas           |
                                   | complejidad           |
                                   +=======================+
```

### Por que mobile-first es mejor

```
  RAZON                              | EXPLICACION
  -----------------------------------|--------------------------------------------
  1. Menos CSS total                 | Los bloques HTML ya se apilan solos en
                                     | movil. No necesitas escribir codigo para
                                     | eso. Solo escribes CSS para las pantallas
                                     | que necesitan layouts complejos.
  -----------------------------------|--------------------------------------------
  2. Mejora progresiva               | La experiencia base funciona en TODOS los
     (Progressive Enhancement)       | dispositivos, incluso los mas limitados.
                                     | Los mas capaces reciben mejoras.
  -----------------------------------|--------------------------------------------
  3. Rendimiento movil               | Los dispositivos moviles (con conexiones
                                     | mas lentas) descargan y procesan MENOS CSS
                                     | porque las reglas complejas estan dentro
                                     | de media queries que no les aplican.
  -----------------------------------|--------------------------------------------
  4. Fuerza simplicidad              | Empezar con restricciones te obliga a
                                     | priorizar el contenido esencial.
  -----------------------------------|--------------------------------------------
  5. Google Mobile-First Indexing    | Google evalua primero la version movil.
                                     | Si tu CSS base es para movil, Google ve
                                     | la mejor version de tu sitio.
```

### Progresion visual

```
  MOVIL (< 768px)          TABLET (768px-1024px)      ESCRITORIO (> 1024px)
  ~~~~~~~~~~~~~~~~~~       ~~~~~~~~~~~~~~~~~~         ~~~~~~~~~~~~~~~~~~

  +================+       +========================+  +================================+
  | [  HEADER    ] |       | [       HEADER       ] |  | [          HEADER             ] |
  +================+       +========================+  +================================+
  | [    NAV     ] |       | [        NAV         ] |  | [           NAV               ] |
  +================+       +========================+  +================================+
  | [            ] |       | [             ] [     ]|  | [              ] [             ]|
  | [  SECTION   ] |       | [   SECTION   ] [ASIDE]|  | [   SECTION    ] [   ASIDE    ]|
  | [            ] |       | [             ] [     ]|  | [              ] [             ]|
  +================+       | [             ] [     ]|  | [              ] [             ]|
  | [   ASIDE   ] |       +========================+  +================================+
  +================+       | [       FOOTER       ] |  | [          FOOTER             ] |
  | [  FOOTER   ] |       +========================+  +================================+
  +================+

  Estilos BASE               @media (min-width:798px)   Podria haber otro @media
  (sin media query)           section: 60%               para ajustes de escritorio
  Todo apilado en             aside: 33%                 grande si fuera necesario
  una columna.                Lado a lado.
```

---

## 3. Media Queries en profundidad

### Sintaxis completa

```
  @media <tipo> and (<caracteristica>: <valor>) {
      /* Reglas CSS que solo aplican cuando la condicion es verdadera */
  }
```

### Tipos de media

```
  TIPO     | SE APLICA A                        | USO COMUN
  ---------|------------------------------------|---------------------------------
  all      | Todos los dispositivos (defecto)   | Si no pones tipo, es "all"
  screen   | Pantallas (monitores, moviles,     | La gran mayoria de tus estilos
           | tablets)                           |
  print    | Cuando se imprime la pagina        | Ocultar nav, fondo blanco,
           | o se genera PDF                    | texto negro, quitar sombras
  speech   | Lectores de pantalla / sintesis    | Raro; casi nunca se usa
           | de voz                             | directamente
```

### Caracteristicas de media (media features)

```
  CARACTERISTICA          | VALORES              | QUE DETECTA
  ------------------------|----------------------|------------------------------------
  width / min-width /     | Longitud (px, em)    | Ancho del VIEWPORT
  max-width               |                      | (area visible del navegador)
  ------------------------|----------------------|------------------------------------
  height / min-height /   | Longitud             | Alto del viewport
  max-height              |                      |
  ------------------------|----------------------|------------------------------------
  orientation             | portrait |           | portrait = alto > ancho
                          | landscape            | landscape = ancho > alto
  ------------------------|----------------------|------------------------------------
  prefers-color-scheme    | light | dark         | Preferencia de tema oscuro/claro
                          |                      | del sistema operativo del usuario
  ------------------------|----------------------|------------------------------------
  prefers-reduced-motion  | no-preference |      | Si el usuario pidio reducir
                          | reduce               | animaciones (accesibilidad)
  ------------------------|----------------------|------------------------------------
  prefers-contrast        | no-preference |      | Si el usuario pidio alto contraste
                          | more | less |        |
                          | custom               |
  ------------------------|----------------------|------------------------------------
  aspect-ratio            | <ancho>/<alto>       | Relacion de aspecto del viewport
                          | Ej: 16/9             |
  ------------------------|----------------------|------------------------------------
  resolution              | <dpi> | <dppx>       | Densidad de pixeles (pantallas
                          |                      | Retina/HiDPI)
  ------------------------|----------------------|------------------------------------
  hover                   | none | hover         | Si el dispositivo tiene cursor
                          |                      | que puede hacer hover (raton vs
                          |                      | pantalla tactil)
  ------------------------|----------------------|------------------------------------
  pointer                 | none | coarse | fine | Precision del dispositivo
                          |                      | apuntador (dedo vs raton)
```

### Operadores logicos

```css
/* AND: ambas condiciones deben cumplirse */
@media screen and (min-width: 768px) and (max-width: 1024px) {
    /* Solo tablets en modo landscape (aproximadamente) */
}

/* OR (coma): al menos UNA condicion debe cumplirse */
@media (max-width: 600px), (orientation: portrait) {
    /* Pantallas pequenas O en modo vertical */
}

/* NOT: niega toda la consulta */
@media not print {
    /* Todo EXCEPTO cuando se imprime */
}

/* ONLY: para navegadores antiguos que no entienden media queries */
@media only screen and (min-width: 768px) {
    /* Navegadores modernos lo interpretan igual que sin "only" */
}
```

### Tabla de breakpoints comunes

```
  BREAKPOINT   | DISPOSITIVOS TIPICOS                | USO
  -------------|-------------------------------------|---------------------------
  320px        | iPhone SE, telefonos muy pequenos    | Raro como breakpoint;
               |                                     | mejor disenar para 360+
  -------------|-------------------------------------|---------------------------
  480px        | Smartphones en modo vertical         | Ajustes menores para
               | (landscape de los mas pequenos)     | moviles grandes
  -------------|-------------------------------------|---------------------------
  768px        | iPad portrait, tablets               | BREAKPOINT CLASICO.
               |                                     | Paso de movil a tablet.
               |                                     | Primer layout de 2 columnas.
  -------------|-------------------------------------|---------------------------
  1024px       | iPad landscape, laptops pequenas     | Layout completo de
               |                                     | escritorio con sidebar
  -------------|-------------------------------------|---------------------------
  1200px       | Escritorios estandar                 | Contenedor max-width
               |                                     | para limitar ancho de lectura
  -------------|-------------------------------------|---------------------------
  1440px       | Escritorios grandes                  | Ajustes para pantallas
               |                                     | anchas (monitores 2K)
  -------------|-------------------------------------|---------------------------
  1920px       | Monitores Full HD y mayores          | Raro; solo para layouts
               |                                     | que necesitan aprovecharlo
```

### En el ejercicio (`styles.css`)

```css
@media (min-width: 798px) {
    section { flex: 1 1 60%; }
    aside   { flex: 1 1 33.33%; }
}
```

Se usa `min-width` (mobile-first) con un breakpoint de 798px,
cercano al clasico 768px del iPad portrait.

**Buena practica:** Elige breakpoints segun **donde tu diseno necesita
cambiar**, no segun dispositivos especificos. Los dispositivos cambian
constantemente, pero los principios del diseno permanecen.

---

## 4. Unidades fluidas

### Porcentajes vs viewport units

```
  UNIDAD   | RELATIVA A                        | EJEMPLO
  ---------|-----------------------------------|----------------------------------
  %        | El PADRE del elemento             | width: 50% = mitad del padre
  vw       | El VIEWPORT (ventana completa)    | width: 50vw = mitad de la ventana
  vh       | El VIEWPORT (alto)                | height: 100vh = toda la altura
  vmin     | El lado MAS PEQUENO del viewport  | Util para cuadrados responsivos
  vmax     | El lado MAS GRANDE del viewport   | Menos comun
```

```
  Diferencia entre % y vw:

  +-- viewport (1000px) -----------------------------------------------+
  |                                                                    |
  |  +-- padre (600px) ------------------------------------+           |
  |  |                                                     |           |
  |  |  +-- width: 50% (300px = 50% de 600px) --+         |           |
  |  |  |                                        |         |           |
  |  |  +----------------------------------------+         |           |
  |  |                                                     |           |
  |  |  +-- width: 50vw (500px = 50% de 1000px) ----------+--+        |
  |  |  |                                                  |  |        |
  |  |  +--------------------------------------------------+--+       |
  |  |                                                     |           |
  |  +-----------------------------------------------------+           |
  +--------------------------------------------------------------------+
```

### La formula: target / context = result

Para convertir un diseno de pixeles fijos a porcentajes:

```
  FORMULA:  resultado = (medida objetivo / medida del contexto) * 100%

  Ejemplo:
  - El diseno muestra una sidebar de 300px en un contenedor de 960px.
  - Porcentaje: (300 / 960) * 100% = 31.25%

  CSS: .sidebar { width: 31.25%; }

  Ahora, si el contenedor cambia de tamano (ej. 768px):
  .sidebar sera: 768 * 0.3125 = 240px  (se adapta proporcionalmente)
```

### Funciones modernas: clamp(), min(), max()

Estas funciones de CSS permiten crear valores responsivos **sin media queries**:

```css
/* clamp(minimo, ideal, maximo) */
font-size: clamp(1rem, 2.5vw, 2rem);
/*
   - Nunca sera menor que 1rem (16px)
   - Idealmente sera 2.5vw (2.5% del ancho del viewport)
   - Nunca sera mayor que 2rem (32px)
*/

/* min(): el MENOR de los valores */
width: min(90%, 1200px);
/*
   - En pantallas pequenas: 90% (porque 90% < 1200px)
   - En pantallas grandes: 1200px (porque 1200px < 90% de, digamos, 1920px)
   - Equivale a: width: 90%; max-width: 1200px;
*/

/* max(): el MAYOR de los valores */
padding: max(2rem, 5vw);
/*
   - En pantallas pequenas: 2rem (porque 2rem > 5vw cuando vw es chico)
   - En pantallas grandes: 5vw (porque 5vw > 2rem cuando vw es grande)
*/
```

### Visualizacion de clamp()

```
  font-size: clamp(1rem, 2.5vw, 2rem)

  Ancho del viewport:
  |   320px   |   640px   |   960px   |   1280px  |
  |           |           |           |           |
  |  1rem     |  1rem     |  1.5rem   |  2rem     |
  |  (minimo) | (2.5vw =  | (2.5vw = | (maximo)  |
  |           |  1rem,    |  1.5rem)  |           |
  |           |  pero min |           |           |
  |           |  es 1rem) |           |           |

  Grafico:

  tamano
  de fuente
    2rem |- - - - - - - - - - - -+===============
         |                      /
  1.5rem |                    /
         |                  /
    1rem |================+
         |
         +-------|--------|--------|--------|-------> viewport
               320px    640px    960px   1280px
```

### Por que usar em en media queries

```css
/* Mejor practica: em en vez de px para media queries */
@media (min-width: 48em) {    /* 48 * 16 = 768px */
    /* ... */
}

/* En vez de */
@media (min-width: 768px) {
    /* ... */
}
```

**Por que:** Cuando el usuario cambia el tamano base de la fuente en su
navegador (ej. de 16px a 20px), las media queries en `em` se ajustan
proporcionalmente. Con `px`, el layout puede romper porque el texto
crece pero los breakpoints quedan fijos.

```
  Tamano base: 16px (defecto)     Tamano base: 20px (usuario)
  48em = 768px                     48em = 960px
  ^^^^^^^^                         ^^^^^^^^
  El breakpoint se adapta al       Con px fijos (768px), el layout
  tamano de texto del usuario.     tablet apareceria en una pantalla
                                   donde el texto ya es muy grande.
```

---

## 5. Flexbox para layouts de pagina

### El patron del ejercicio

En `styles.css`, el layout principal usa Flexbox para organizar
`<section>` y `<aside>`:

```
  MOVIL (estilos base, sin media query):

  .contenedor {
      display: flex;
      flex-wrap: wrap;
  }
  section, aside {
      flex: 1 1 100%;     <-- Ambos ocupan 100% -> se APILAN
  }

  +====================================+
  |          .contenedor               |
  |  +---------------------------------+
  |  |         <h1> y <p>             |
  |  +---------------------------------+
  |  |                                |
  |  |         SECTION                |  <- flex: 1 1 100%
  |  |         (todo el ancho)        |
  |  |                                |
  |  +---------------------------------+
  |  |                                |
  |  |         ASIDE                  |  <- flex: 1 1 100%
  |  |         (todo el ancho)        |
  |  |                                |
  |  +---------------------------------+
  +====================================+


  ESCRITORIO (@media min-width: 798px):

  section { flex: 1 1 60%; }
  aside   { flex: 1 1 33.33%; }

  +========================================================+
  |                    .contenedor                          |
  |  +-----------------------------------------------------+
  |  |              <h1> y <p>                             |
  |  +--------------------------------------+--------------+
  |  |                                      |              |
  |  |         SECTION                      |    ASIDE     |
  |  |         flex: 1 1 60%                |  flex: 1 1   |
  |  |                                      |  33.33%      |
  |  |         (~63% final con grow)        | (~37% final) |
  |  |                                      |              |
  |  +--------------------------------------+--------------+
  +========================================================+
```

### Como funciona la matematica

```
  Contenedor: 100% del ancho disponible (digamos 1000px despues de padding)

  section: flex-basis 60%  = 600px
  aside:   flex-basis 33%  = 330px
  Total:                   = 930px
  Sobrante:                = 70px

  Ambos tienen flex-grow: 1, asi que se reparten los 70px:
  section: 600 + 35 = 635px (~63.5%)
  aside:   330 + 35 = 365px (~36.5%)
```

### flex-basis en contextos responsivos

```
  flex-basis: 100%   ->  Fuerza apilamiento (un item por linea)
  flex-basis: 50%    ->  Dos items por linea (si caben)
  flex-basis: 33.33% ->  Tres items por linea (si caben)
  flex-basis: 200px  ->  Tamano fijo; con flex-wrap, salta de linea
                         cuando no cabe

  Patron tipico mobile-first:
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~
  .item {
      flex: 1 1 100%;           /* Movil: apilado */
  }

  @media (min-width: 768px) {
      .item {
          flex: 1 1 45%;        /* Tablet: 2 por fila */
      }
  }

  @media (min-width: 1200px) {
      .item {
          flex: 1 1 30%;        /* Escritorio: 3 por fila */
      }
  }
```

---

## 6. El viewport meta tag

### Que es y por que es OBLIGATORIO

```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

Este tag le dice al navegador movil como renderizar la pagina.

### Que hace cada parte

```
  ATRIBUTO              | VALOR              | SIGNIFICADO
  ----------------------|--------------------|--------------------------------------
  width                 | device-width       | El ancho del viewport = el ancho
                        |                    | real del dispositivo. Sin esto,
                        |                    | los moviles simulan 980px.
  ----------------------|--------------------|--------------------------------------
  initial-scale         | 1.0                | El nivel de zoom inicial es 1:1
                        |                    | (sin zoom). 0.5 = 50% zoom out.
  ----------------------|--------------------|--------------------------------------
  maximum-scale         | (no recomendado)   | Limita cuanto puede hacer zoom
                        |                    | el usuario.
  ----------------------|--------------------|--------------------------------------
  user-scalable         | yes | no           | Permite/impide el zoom del usuario.
                        | (NO usar "no")     |
```

### Que pasa SIN el viewport meta tag

```
  CON viewport meta tag:             SIN viewport meta tag:

  Movil (375px de ancho real)        Movil (375px, pero simula 980px)

  +====================+            +=======================================...
  |  [Encabezado]      |            |  [Encabezado super pequeno           ...
  +====================+            +=======================================...
  |  [Nav] [Nav] [Nav] |            |  [N] [N] [N] [N]   (texto diminuto) ...
  +====================+            +=======================================...
  |  Lorem ipsum dolor  |            |  Lorem ipsum dolor sit amet, consecte...
  |  sit amet, consec-  |            |  tur adipisicing elit. Todo el texto ...
  |  tetur adipisicing  |            |  se ve MINUSCULO porque el navegador ...
  |  elit.              |            |  cree que la pantalla tiene 980px y  ...
  |                    |            |  escala todo para que quepa.          ...
  +====================+            +=======================================...

  Texto legible.                     Texto ILEGIBLE. El usuario debe
  Layout adaptado al                 hacer zoom manualmente.
  ancho real.                        El CSS responsive NO funciona.
```

### Por que user-scalable=no es DANINO

```
  <meta name="viewport" content="width=device-width, initial-scale=1.0,
        maximum-scale=1.0, user-scalable=no">
                                     ^^^^^^^^^^^^^^^^^^^^^^
                                     NUNCA hagas esto.

  Razones:
  1. ACCESIBILIDAD: personas con baja vision NECESITAN hacer zoom
     para leer el texto.
  2. WCAG: el criterio 1.4.4 (Resize text) requiere que el texto
     pueda escalarse al 200% sin perdida de funcionalidad.
  3. Navegadores modernos: Safari en iOS 10+ IGNORA user-scalable=no
     por razones de accesibilidad. Asi que ademas de ser danino,
     no funciona en muchos dispositivos.
```

### En el ejercicio (`index.html`)

```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

Correcto: usa `device-width` y `initial-scale=1.0`, sin restringir
el zoom del usuario.

---

## 7. Imagenes responsivas

### El patron basico: max-width: 100%

```css
img {
    max-width: 100%;
    height: auto;       /* Mantiene la proporcion original */
}
```

```
  Contenedor: 400px                 Contenedor: 200px

  +============================+    +=============+
  |                            |    |             |
  |   +--------------------+   |    |  +-------+  |
  |   |                    |   |    |  |       |  |
  |   |   Imagen 300px     |   |    |  | Imagen|  |
  |   |   (cabe, no cambia)|   |    |  | 200px |  |
  |   +--------------------+   |    |  | (se   |  |
  |                            |    |  | encoge)|  |
  +============================+    |  +-------+  |
                                    +=============+

  max-width: 100% = "Nunca seas mas ancho que tu padre".
  Si la imagen es mas pequena que el padre, mantiene su tamano natural.
  Si es mas grande, se encoge al 100% del padre.
```

### srcset y sizes: multiples resoluciones

```html
<img
    src="imagen-800.jpg"
    srcset="
        imagen-400.jpg   400w,
        imagen-800.jpg   800w,
        imagen-1200.jpg 1200w
    "
    sizes="
        (max-width: 600px) 100vw,
        (max-width: 1200px) 50vw,
        800px
    "
    alt="Descripcion de la imagen"
>
```

```
  QUE HACE CADA PARTE:

  srcset:
  - Lista de archivos de imagen con su ANCHO INTRINSECO (en pixeles).
  - 400w = "esta imagen tiene 400 pixeles de ancho".
  - El navegador ELIGE la mas apropiada segun el tamano de pantalla
    y la densidad de pixeles.

  sizes:
  - Le dice al navegador QUE TAMANO tendra la imagen en la pantalla.
  - "(max-width: 600px) 100vw" = en pantallas < 600px, la imagen
    ocupa el 100% del ancho del viewport.
  - "(max-width: 1200px) 50vw" = en pantallas < 1200px, ocupa el 50%.
  - "800px" = en pantallas mas grandes, la imagen se muestra a 800px.

  El navegador combina sizes + srcset + densidad de pixeles para
  decidir CUAL imagen descargar:

  Pantalla 375px (movil), 2x Retina:
  - sizes dice: 100vw = 375px
  - Necesita: 375 * 2 (Retina) = 750px
  - Elige: imagen-800.jpg (la mas cercana sin ser menor)

  Pantalla 1024px (tablet), 1x:
  - sizes dice: 50vw = 512px
  - Necesita: 512px
  - Elige: imagen-800.jpg

  Pantalla 1920px (escritorio), 1x:
  - sizes dice: 800px
  - Necesita: 800px
  - Elige: imagen-800.jpg
```

### El elemento `<picture>` para art direction

```html
<picture>
    <!-- En moviles: imagen recortada/cuadrada enfocada en el sujeto -->
    <source media="(max-width: 600px)" srcset="foto-movil.jpg">

    <!-- En tablets: imagen horizontal media -->
    <source media="(max-width: 1200px)" srcset="foto-tablet.jpg">

    <!-- Escritorio: imagen panoramica completa -->
    <img src="foto-escritorio.jpg" alt="Paisaje de montana">
</picture>
```

```
  Movil (< 600px):          Tablet (600-1200px):        Escritorio (> 1200px):

  +============+            +==================+        +============================+
  |            |            |                  |        |                            |
  |   [cara]   |            |  [persona en     |        |  [persona en paisaje       |
  |   (close   |            |   paisaje medio] |        |   panoramico completo]     |
  |    up)     |            |                  |        |                            |
  +============+            +==================+        +============================+

  Diferentes RECORTES de la misma foto,
  optimizados para cada tamano de pantalla.
  Esto es "art direction": cambiar la composicion,
  no solo el tamano.
```

### Diferencia entre srcset y picture

```
  srcset:
  - La MISMA imagen en diferentes RESOLUCIONES.
  - El navegador decide cual descargar.
  - Usa cuando la imagen es la misma, solo cambia el tamano.

  <picture>:
  - DIFERENTES imagenes segun condiciones.
  - TU decides cual se muestra en cada caso.
  - Usa cuando quieres cambiar el recorte, el formato,
    o usar una imagen completamente diferente.
```

---

## 8. Errores comunes

### Error 1: Olvidar el viewport meta tag

```html
<!-- MAL: la pagina NO es responsive en moviles -->
<head>
    <meta charset="UTF-8">
    <title>Mi pagina</title>
</head>

<!-- BIEN: el movil usa el ancho real del dispositivo -->
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mi pagina</title>
</head>
```

**Sintoma:** El sitio se ve "como escritorio encogido" en el celular.
Las media queries no se activan en los breakpoints esperados.

---

### Error 2: Usar max-width (desktop-first) cuando quieres mobile-first

```css
/* MAL: desktop-first accidental */
.sidebar {
    width: 300px;
    float: left;
}
@media (max-width: 768px) {     /* <-- max-width = estas deshaciendo */
    .sidebar {
        width: 100%;
        float: none;
    }
}

/* BIEN: mobile-first */
/* .sidebar ya ocupa 100% por defecto (es un bloque) */
@media (min-width: 768px) {     /* <-- min-width = estas agregando */
    .sidebar {
        flex: 0 0 300px;
    }
}
```

---

### Error 3: Breakpoints basados en dispositivos en vez del diseno

```css
/* MAL: breakpoint para "iPhone 12" */
@media (max-width: 390px) { ... }    /* Que pasa con el iPhone 13 Mini? */
@media (max-width: 428px) { ... }    /* Y el Samsung Galaxy S21? */

/* BIEN: breakpoint donde tu diseno NECESITA cambiar */
@media (min-width: 768px) { ... }    /* Donde mi layout de 2 columnas
                                         funciona bien */
```

Los dispositivos cambian cada anio. Tu diseno debe funcionar en
**cualquier** ancho, no en dispositivos especificos.

---

### Error 4: Anchos fijos en pixeles que rompen en movil

```css
/* MAL: se desborda en pantallas menores a 800px */
.contenedor {
    width: 800px;
}

/* BIEN: se adapta pero tiene un maximo */
.contenedor {
    width: 100%;
    max-width: 800px;
    margin: 0 auto;      /* Centra el contenedor */
}
```

---

### Error 5: Imagenes sin max-width que desbordan

```css
/* MAL: una imagen de 2000px se sale del contenedor */
img {
    /* sin restriccion de ancho */
}

/* BIEN */
img {
    max-width: 100%;
    height: auto;        /* IMPORTANTE: mantiene la proporcion */
}
```

**Sintoma:** Aparece scroll horizontal en movil. Una imagen gigante
empuja todo el contenido hacia la derecha.

---

### Error 6: Media queries en orden incorrecto

```css
/* MAL (mobile-first): el segundo @media sobreescribe al primero */
@media (min-width: 768px) {
    .card { flex: 1 1 45%; }
}
@media (min-width: 480px) {     /* <-- Este SIEMPRE aplica cuando
    .card { flex: 1 1 100%; }       el de 768px aplica. Sobreescribe. */
}

/* BIEN (mobile-first): de menor a mayor */
@media (min-width: 480px) {
    .card { flex: 1 1 100%; }
}
@media (min-width: 768px) {     /* Este sobreescribe al anterior
    .card { flex: 1 1 45%; }       cuando aplica. Correcto. */
}
@media (min-width: 1200px) {
    .card { flex: 1 1 30%; }
}
```

**Regla:** En mobile-first (`min-width`), ordena las media queries
de **menor a mayor**. En desktop-first (`max-width`), de **mayor a menor**.

---

### Error 7: No probar en dispositivos reales

```
  Chrome DevTools (responsive mode) es un SIMULADOR, no un emulador.
  No replica:
  - Rendimiento real del dispositivo (CPU/GPU movil)
  - Comportamiento tactil (hover, scroll momentum)
  - Barras de direccion que cambian de tamano
  - Notch / Dynamic Island del iPhone
  - Teclado virtual que reduce el viewport

  SIEMPRE prueba en al menos:
  - Un telefono Android real
  - Un iPhone real (Safari tiene sus propias particularidades)
  - Una tablet si tu audiencia las usa
```

---

## 9. Ejercicios de practica

Todos los ejercicios se basan en los archivos `index.html` y `styles.css`
de esta carpeta. Abre `index.html` en tu navegador y usa las DevTools
(F12) para simular diferentes tamanos de pantalla.

### Ejercicio 1 — Agregar un breakpoint intermedio
Agrega una media query para tablets (min-width: 480px) donde:
- La seccion ocupe el 100% (sigue apilada)
- El aside se muestre con fondo diferente y padding extra
- La navegacion tenga gap mas grande

```css
@media (min-width: 480px) {
    aside {
        background: var(--color-sec-alt);
        padding: 25px;
    }
    ul {
        gap: 3rem;
    }
}
```

**Nota:** Asegurate de poner esta media query ANTES de la de `798px`.

---

### Ejercicio 2 — Layout de tres columnas
Modifica el layout para que en pantallas grandes (min-width: 1200px),
haya tres columnas: un aside izquierdo, la seccion central, y el aside
actual a la derecha.

**Pasos:**
1. Agrega un segundo `<aside>` en el HTML antes de `<section>`.
2. Agrega una media query para 1200px:

```css
@media (min-width: 1200px) {
    section { flex: 1 1 50%; }
    aside   { flex: 1 1 20%; }
}
```

---

### Ejercicio 3 — Tipografia fluida con clamp()
Reemplaza los tamanos de fuente fijos por valores fluidos:

```css
:root {
    --grande: clamp(0.9rem, 2vw, 1.2rem);
    --mediano: clamp(0.75rem, 1.5vw, 1rem);
}
```

Redimensiona el navegador lentamente y observa como el texto se
ajusta suavemente.

---

### Ejercicio 4 — Media query para impresion
Agrega estilos de impresion que:
- Quiten la navegacion
- Pongan fondo blanco y texto negro
- Quiten sombras y bordes decorativos
- Muestren las URLs de los enlaces

```css
@media print {
    nav { display: none; }
    body {
        background: white;
        color: black;
        font-weight: normal;
    }
    section, article, aside {
        background: white;
        color: black;
    }
    a::after {
        content: " (" attr(href) ")";
        font-size: 0.8em;
    }
}
```

Prueba con Ctrl+P (o Cmd+P) para ver la vista previa de impresion.

---

### Ejercicio 5 — Tema oscuro/claro automatico
Usa `prefers-color-scheme` para adaptar los colores segun la
preferencia del sistema operativo del usuario:

```css
@media (prefers-color-scheme: light) {
    :root {
        --fondo: #f5f5f5;
        --color-sec: #2e1955;
        --letras: #1a1a1a;
    }
}
```

**Para probar:** En Chrome DevTools, abre el panel de Rendering
(Ctrl+Shift+P > "Show Rendering") y cambia "Emulate CSS media feature
prefers-color-scheme".

---

### Ejercicio 6 — Reducir animaciones
Si en el futuro agregas animaciones, practica con la media query
de movimiento reducido:

```css
/* Primero, agrega una animacion a los botones de navegacion */
li {
    transition: background-color 0.3s ease, transform 0.2s ease;
}
li:hover {
    transform: scale(1.05);
}

/* Luego, respeta la preferencia del usuario */
@media (prefers-reduced-motion: reduce) {
    li {
        transition: none;
    }
    li:hover {
        transform: none;
    }
}
```

---

### Ejercicio 7 — Contenedor con max-width centrado
Agrega un ancho maximo al `.contenedor` para que en pantallas muy
grandes el contenido no se estire demasiado:

```css
.contenedor {
    max-width: 1200px;
    margin: 0 auto;      /* Centra horizontalmente */
}
```

Redimensiona el navegador a mas de 1200px y observa como el contenido
deja de crecer y se centra.

---

### Ejercicio 8 — Imagen responsiva completa
Agrega una imagen al `<section>` con las siguientes caracteristicas:

1. CSS basico: `max-width: 100%; height: auto;`
2. Atributo `loading="lazy"` para carga diferida
3. (Opcional) Un `srcset` con 2-3 versiones de la imagen si tienes
   acceso a una herramienta de redimensionamiento

```html
<img
    src="assets/foto-800.jpg"
    srcset="assets/foto-400.jpg 400w, assets/foto-800.jpg 800w"
    sizes="(max-width: 798px) 100vw, 60vw"
    alt="Descripcion apropiada"
    loading="lazy"
    style="max-width: 100%; height: auto;"
>
```

---

> **Modulo anterior:** `05-componentes-css/CONCEPTOS.md` — Componentes CSS
> **Siguiente modulo:** `07-responsive-css-grid/` — CSS Grid

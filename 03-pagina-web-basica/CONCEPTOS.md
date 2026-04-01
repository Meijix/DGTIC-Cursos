# Modulo 03 -- Paginas Web Multi-archivo

> **Archivos de referencia:** `index.html`, `pagina2.html`, `styles.css`
> y la carpeta `assets/` en este mismo directorio. Este modulo demuestra
> como se construye un sitio con multiples paginas que comparten estilos.

---

## Indice

1. [Estructura de archivos de un sitio web](#1-estructura-de-archivos-de-un-sitio-web)
2. [Enlaces y navegacion](#2-enlaces-y-navegacion)
3. [Imagenes en la web](#3-imagenes-en-la-web)
4. [El modelo de cajas aplicado](#4-el-modelo-de-cajas-aplicado)
5. [Clases CSS y organizacion](#5-clases-css-y-organizacion)
6. [Errores comunes](#6-errores-comunes)
7. [Ejercicios de practica](#7-ejercicios-de-practica)

---

## 1. Estructura de archivos de un sitio web

### Arbol de directorios tipico

```
  mi-sitio-web/
  │
  ├── index.html              <-- Pagina principal (documento por defecto)
  ├── pagina2.html             <-- Pagina secundaria
  ├── contacto.html            <-- Otra pagina
  │
  ├── styles.css               <-- Hoja de estilos COMPARTIDA
  │
  ├── assets/                  <-- Recursos estaticos
  │   ├── img/                 <-- Imagenes
  │   │   ├── logo.svg
  │   │   ├── hero.webp
  │   │   └── fondo.jpg
  │   ├── fonts/               <-- Fuentes locales (si las hay)
  │   └── icons/               <-- Iconos
  │
  ├── css/                     <-- (alternativa) CSS en subcarpeta
  │   ├── reset.css
  │   └── main.css
  │
  └── js/                      <-- JavaScript
      └── app.js
```

> **Este modulo:** Tiene una estructura mas sencilla pero funcional:
> ```
> 03-pagina-web-basica/
> ├── index.html           <-- Pagina principal
> ├── pagina2.html         <-- Pagina secundaria
> ├── styles.css           <-- Estilos compartidos
> └── assets/
>     ├── fondo3.jpg       <-- Imagen JPG local
>     └── fondo4.avif      <-- Imagen AVIF local
> ```

### Convenciones de nombres

| Regla                        | Ejemplo correcto          | Ejemplo incorrecto         | Por que                              |
|------------------------------|---------------------------|----------------------------|--------------------------------------|
| Todo en minusculas           | `mi-pagina.html`          | `Mi-Pagina.html`           | Linux distingue mayusculas/minusculas|
| Guiones en vez de espacios   | `pagina-contacto.html`    | `pagina contacto.html`     | Los espacios rompen URLs             |
| Guiones en vez de guiones bajos | `mi-estilo.css`        | `mi_estilo.css`            | Convencion web (SEO y legibilidad)   |
| Sin caracteres especiales    | `pagina2.html`            | `pagina#2.html`            | Caracteres especiales rompen URLs    |
| Sin acentos ni enies         | `contacto.html`           | `contacto-espanol.html`     | Evita problemas de codificacion      |
| Nombres descriptivos         | `galeria-fotos.html`      | `p2.html`                  | Claridad para humanos y buscadores   |

### El rol especial de index.html

Cuando un usuario visita `https://misitio.com/`, el servidor busca automaticamente
un archivo llamado `index.html` en la raiz. Es el **documento por defecto**.

```
  El usuario escribe:              El servidor entrega:
  ─────────────────                ────────────────────
  https://misitio.com/             index.html
  https://misitio.com/blog/        blog/index.html
  https://misitio.com/about.html   about.html (ruta explicita)
```

Si no existe `index.html`, el servidor puede:
- Mostrar un error 404 (pagina no encontrada)
- Listar los archivos del directorio (esto es un riesgo de seguridad)
- Buscar `index.htm`, `default.html`, etc. (segun la configuracion)

---

## 2. Enlaces y navegacion

### Rutas absolutas vs relativas

```
  RUTA RELATIVA (recomendada para enlaces internos):
  ──────────────────────────────────────────────────

  Posicion actual: /03-pagina-web-basica/index.html

  href="pagina2.html"           --> /03-pagina-web-basica/pagina2.html
  href="assets/fondo3.jpg"      --> /03-pagina-web-basica/assets/fondo3.jpg
  href="../index.html"          --> /index.html (sube un nivel)
  href="../../otro/pagina.html" --> subiendo dos niveles, luego a "otro/"


  RUTA ABSOLUTA LOCAL (relativa a la raiz del servidor):
  ──────────────────────────────────────────────────────

  href="/about.html"            --> Siempre desde la raiz del sitio
  href="/css/styles.css"        --> Independiente de donde estes


  RUTA ABSOLUTA EXTERNA (URL completa):
  ──────────────────────────────────────

  href="https://www.youtube.com/watch?v=..."  --> Otro sitio web
```

### Diagrama visual de rutas relativas

```
  proyecto/
  ├── index.html             Desde index.html:
  ├── pages/                   href="pages/about.html"     --> OK
  │   ├── about.html           href="pages/blog/post1.html" --> OK
  │   └── blog/
  │       └── post1.html     Desde post1.html:
  └── assets/                  href="../../index.html"      --> Sube 2 niveles
      └── logo.png             href="../../assets/logo.png" --> Sube 2, baja a assets
                               href="../about.html"         --> Sube 1 nivel a pages/

  "../" = "sube un nivel en el arbol de directorios"
  "./"  = "directorio actual" (es opcional, href="./pagina2.html" = href="pagina2.html")
```

> **En `index.html` (linea 171):** `<a href="pagina2.html">Pagina secundaria</a>`
> es una ruta relativa. Funciona porque ambos archivos estan en la misma carpeta.
>
> **En `pagina2.html` (linea 51):** `<a href="index.html">Pagina principal</a>`
> completa la navegacion bidireccional.

### Identificadores de fragmento (#)

```html
  <!-- Enlace a una seccion de la misma pagina -->
  <a href="#seccion-servicios">Ir a servicios</a>

  <!-- Mas abajo en la pagina... -->
  <section id="seccion-servicios">
      <h2>Nuestros servicios</h2>
  </section>

  <!-- El navegador hace scroll automatico hasta el elemento con ese id -->
```

```html
  <!-- Enlace a una seccion de OTRA pagina -->
  <a href="pagina2.html#formulario">Ir al formulario de pagina 2</a>

  <!-- Esto abre pagina2.html y luego hace scroll hasta id="formulario" -->
```

### target="_blank" y seguridad

```html
  <!-- INSEGURO (antiguo) -->
  <a href="https://externo.com" target="_blank">Visitar</a>

  <!-- SEGURO (moderno) -->
  <a href="https://externo.com" target="_blank" rel="noopener noreferrer">Visitar</a>
```

**Por que `rel="noopener noreferrer"`:**

```
  SIN noopener:

  Tu pagina                         Pagina externa
  ┌──────────────┐    target="_blank"   ┌──────────────┐
  │  mi-sitio.com │ ──────────────────> │ externo.com  │
  └──────────────┘                      │              │
                                        │ Tiene acceso │
                                        │ a window.opener │
                                        │ Puede CAMBIAR│
                                        │ la URL de tu │
                                        │ pestania!    │
                                        └──────────────┘

  La pagina externa podria redirigir tu pestania a un sitio de phishing:
  window.opener.location = "https://mi-sitio-falso.com/login"

  CON noopener:

  Tu pagina                         Pagina externa
  ┌──────────────┐    target="_blank"   ┌──────────────┐
  │  mi-sitio.com │ ──────────────────> │ externo.com  │
  └──────────────┘   rel="noopener"     │              │
                                        │ window.opener│
                                        │ es NULL      │
                                        │ No tiene     │
                                        │ acceso a tu  │
                                        │ pestania     │
                                        └──────────────┘
```

> **En `index.html` (linea 251):** El enlace a YouTube NO tiene
> `target="_blank"` ni `rel="noopener noreferrer"`. En un proyecto real,
> deberia tenerlos.

### Estados de enlace (LVHAF)

Los enlaces tienen 5 estados y DEBEN declararse en un orden especifico
en CSS para funcionar correctamente:

```
  Orden recomendado (mnemotecnico: LoVe HAte Focus):

  a:link     { color: blue; }         /* L - Enlace no visitado */
  a:visited  { color: purple; }       /* V - Enlace ya visitado */
  a:hover    { color: red; }          /* H - Cursor encima */
  a:active   { color: orange; }       /* A - Mientras se hace clic */
  a:focus    { outline: 2px solid; }  /* F - Cuando tiene foco (teclado) */
```

**Por que importa el orden:** Si pones `:visited` despues de `:hover`,
`:visited` sobreescribe a `:hover` y el efecto hover no funciona en
enlaces ya visitados (porque tienen la misma especificidad y gana el
ultimo en el codigo).

```
  Estado del enlace en el tiempo:

  [No visitado] ──clic──> [Activo] ──suelta──> [Visitado]
       │                                            │
       └──cursor encima──> [Hover]                  └──cursor encima──> [Hover]
       │                      │                     │                      │
       └──tab (teclado)──> [Focus]                  └──tab (teclado)──> [Focus]
```

---

## 3. Imagenes en la web

### Tabla comparativa de formatos

| Formato  | Extension    | Compresion      | Transparencia | Animacion | Tamano tipico  | Mejor para                        |
|----------|-------------|-----------------|---------------|-----------|----------------|-----------------------------------|
| **JPEG** | `.jpg`      | Con perdida     | No            | No        | Mediano        | Fotografias, imagenes complejas   |
| **PNG**  | `.png`      | Sin perdida     | Si (alfa)     | No        | Grande         | Logos, capturas, transparencia    |
| **GIF**  | `.gif`      | Sin perdida     | Si (1 bit)    | Si        | Variable       | Animaciones simples, memes        |
| **SVG**  | `.svg`      | Vectorial (XML) | Si            | Si (CSS/JS)| Muy pequeno   | Iconos, logos, graficos simples   |
| **WebP** | `.webp`     | Ambas           | Si (alfa)     | Si        | Pequeno        | Reemplazo moderno de JPG y PNG    |
| **AVIF** | `.avif`     | Con perdida     | Si (alfa)     | Si        | Muy pequeno    | Reemplazo futuro de JPG (mejor compresion) |

### Comparacion visual de peso

```
  La misma foto (1920x1080), calidad similar:

  JPEG:  ████████████████████████████████████   350 KB
  PNG:   ████████████████████████████████████████████████████████████   800 KB
  WebP:  ████████████████████████████           250 KB  (30% menos que JPEG)
  AVIF:  █████████████████████                  180 KB  (50% menos que JPEG)
```

> **En este modulo:**
> - `assets/fondo3.jpg` -- Imagen JPG (formato universal)
> - `assets/fondo4.avif` -- Imagen AVIF (formato moderno, excelente compresion)
>
> Observa en `pagina2.html` (lineas 87-119) la tabla comparativa JPG vs AVIF
> incluida en los comentarios del codigo.

### Imagenes responsivas: srcset y sizes

```html
  <!-- Basico: una imagen para todos -->
  <img src="foto.jpg" alt="Descripcion">

  <!-- Responsivo: diferentes imagenes segun el ancho de la pantalla -->
  <img src="foto-800.jpg"
       srcset="foto-400.jpg 400w,
               foto-800.jpg 800w,
               foto-1200.jpg 1200w"
       sizes="(max-width: 600px) 400px,
              (max-width: 1000px) 800px,
              1200px"
       alt="Descripcion">
```

**Como funciona:**
```
  1. El navegador lee "sizes" para saber que ancho NECESITA:
     - Si la pantalla es <= 600px: necesita una imagen de 400px
     - Si la pantalla es <= 1000px: necesita una imagen de 800px
     - Si no: necesita 1200px

  2. Busca en "srcset" la imagen que mejor coincida:
     - 400w = "esta imagen tiene 400px de ancho intriniseco"
     - 800w = "esta imagen tiene 800px de ancho intriniseco"

  3. Descarga SOLO la imagen necesaria (ahorra datos en movil)
```

### La etiqueta `<picture>` para multiples formatos

```html
  <picture>
      <source srcset="foto.avif" type="image/avif">     <!-- Si soporta AVIF -->
      <source srcset="foto.webp" type="image/webp">     <!-- Si soporta WebP -->
      <img src="foto.jpg" alt="Descripcion de la foto">  <!-- Respaldo universal -->
  </picture>
```

El navegador recorre los `<source>` de arriba hacia abajo y usa el primer
formato que soporte. Si no soporta ninguno, usa el `<img>` de respaldo.

### Como escribir buen texto alternativo (alt)

```
  Preguntate: Que informacion transmite esta imagen?
         │
         ▼
  La imagen es puramente DECORATIVA?
  (bordes, fondos, separadores)
         │
    ┌────┴────┐
    │ SI      │ NO
    ▼         ▼
  alt=""    La imagen tiene
  (vacio)  TEXTO dentro?
  El lector      │
  la ignora ┌────┴────┐
            │ SI      │ NO
            ▼         ▼
         Transcribe  Describe QUE MUESTRA
         el texto    (no como se ve
         completo    tecnicamente)
```

**Ejemplos:**

| Imagen                              | alt BUENO                                    | alt MALO                    |
|-------------------------------------|----------------------------------------------|-----------------------------|
| Foto del equipo de trabajo          | `alt="Equipo de desarrollo en la oficina"`   | `alt="foto"`                |
| Logo de la UNAM                     | `alt="Logo de la UNAM"`                      | `alt="imagen"`              |
| Grafica de ventas 2024              | `alt="Grafica: ventas subieron 23% en 2024"` | `alt="grafica.png"`         |
| Linea decorativa entre secciones    | `alt=""`                                     | `alt="linea"`               |
| Boton con icono de flecha derecha   | `alt="Siguiente"`                            | `alt="flecha"`              |
| Banner con texto "50% de descuento" | `alt="Oferta: 50% de descuento en todo"`     | `alt="banner"`              |

> **En `index.html`:** La linea 132 tiene `alt="Logo de la UNAM"` (bueno)
> y la linea 242 tiene `alt="Una imagen de anime"` (aceptable pero podria
> ser mas descriptivo si el contenido de la imagen importa).

### Lazy loading

```html
  <!-- El navegador NO descarga esta imagen hasta que el usuario
       haga scroll y se acerque a ella -->
  <img src="foto-grande.jpg" alt="..." loading="lazy">

  <!-- El navegador la descarga INMEDIATAMENTE (default) -->
  <img src="foto-hero.jpg" alt="..." loading="eager">
```

**Cuando usar `loading="lazy"`:**
- Imagenes debajo del "fold" (la parte de la pagina que no se ve sin scroll)
- Galerias con muchas imagenes
- Listas largas de productos

**Cuando NO usar lazy loading:**
- La imagen principal (hero) de la pagina
- Imagenes que se ven sin hacer scroll
- El logo del sitio

---

## 4. El modelo de cajas aplicado

### Gradientes lineales en profundidad

```css
  /* Estructura basica */
  background: linear-gradient(direccion, color1, color2, ...);
```

```
  DIRECCIONES:

  to top          to top right       to right
      ↑               ↗                  →

  to top left                        to bottom right
      ↖                                  ↘

  to left         to bottom left     to bottom (default)
      ←               ↙                  ↓

  Tambien puedes usar angulos:
  0deg = to top    |  90deg = to right  |  180deg = to bottom  |  270deg = to left
  45deg = diagonal hacia arriba-derecha
```

**Ejemplos visuales:**

```
  linear-gradient(to right, azul, cyan)

  ┌────────────────────────────────────────┐
  │ AZUL ▓▓▓▓▓▓▒▒▒▒▒▒░░░░░░       CYAN   │
  └────────────────────────────────────────┘

  linear-gradient(to bottom, rojo, amarillo, verde)

  ┌───────────────────┐
  │     ROJO          │
  │  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓  │
  │  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒  │
  │    AMARILLO       │
  │  ░░░░░░░░░░░░░░  │
  │                   │
  │     VERDE         │
  └───────────────────┘

  linear-gradient(to right, rojo 0%, amarillo 30%, verde 100%)

  ┌──────────────────────────────────────────────────┐
  │ROJO▓▓AMR▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░VERDE│
  │    30%                                    100%   │
  └──────────────────────────────────────────────────┘
  El amarillo aparece en el 30% del recorrido, no en la mitad.
```

> **En `styles.css` (linea 167):**
> `background: linear-gradient(to right, rgb(120, 120, 225), #b4daf9);`
> Crea un degradado horizontal de azul medio a azul claro en la clase `.box`.

### box-shadow: sombras en capas

```
  Sintaxis: box-shadow: offset-x  offset-y  blur  spread  color;

  ┌──────────────────────────┐
  │                          │  offset-x: desplazamiento horizontal
  │       ELEMENTO           │  offset-y: desplazamiento vertical
  │                          │  blur: difuminado (mayor = mas suave)
  └──────────────────────────┘  spread: expansion (mayor = mas grande)
    ╲░░░░░░░░░░░░░░░░░░░░░░╲   color: color de la sombra
     ░░░░░░ SOMBRA ░░░░░░░░░░
```

**Ejemplos tipicos:**

```css
  /* Sombra sutil (elevacion leve) */
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);

  /* Sombra pronunciada (tarjeta elevada) */
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.2);

  /* Resplandor (glow) */
  box-shadow: 0 0 35px 0 #5d3469;

  /* Sombra interior (inset) */
  box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.2);

  /* Multiples sombras (separadas por coma) */
  box-shadow: 0 2px 4px rgba(0,0,0,0.1),
              0 8px 16px rgba(0,0,0,0.1);
```

> **En `styles.css` (linea 119):**
> `box-shadow: 0 0 35px 0 #5d3469;` -- Crea un resplandor purpura
> alrededor de la clase `.box`. Ambos offsets son 0 (centrado), blur de
> 35px (muy difuso) y spread de 0.

### object-fit: cover vs contain vs fill

```
  Imagen original: 800x400 (ratio 2:1)
  Contenedor: 300x300 (ratio 1:1)

  object-fit: COVER                object-fit: CONTAIN             object-fit: FILL
  ┌───────────────────┐            ┌───────────────────┐           ┌───────────────────┐
  │ ┌─────────────────┤            │                   │           │                   │
  │ │                 │            │ ┌───────────────┐ │           │ ┌───────────────┐ │
  │ │    Se ve la     │            │ │  Se ve TODA   │ │           │ │   La imagen   │ │
  │ │    parte que    │            │ │  la imagen    │ │           │ │   se DEFORMA  │ │
  │ │    cabe. El     │            │ │  pero hay     │ │           │ │   para llenar │ │
  │ │    resto se     │            │ │  barras       │ │           │ │   exactamente │ │
  │ │    RECORTA      │            │ │  vacias       │ │           │ │   el espacio  │ │
  │ │                 │            │ └───────────────┘ │           │ └───────────────┘ │
  │ └─────────────────┤            │                   │           │                   │
  └───────────────────┘            └───────────────────┘           └───────────────────┘

  No se deforma.                   No se deforma.                  Se deforma.
  Se recorta.                      No se recorta.                  No se recorta.
  Llena todo el espacio.           Puede dejar espacio.            Llena todo el espacio.
```

> **En `styles.css` (linea 205):** `object-fit: cover;` en las imagenes.
> Con `max-height: 200px` y `max-width: 100%`, las imagenes se recortan
> para llenar su caja sin deformarse.

### border-radius en profundidad

```
  border-radius: 10px;              Esquinas suavemente redondeadas
  ┌─────────────────────────┐
  │                         │
  │                         │
  └─────────────────────────┘

  border-radius: 50%;               Circulo (si es cuadrado) o elipse
  ┌─────────────────────────┐
  /                          \
  |                          |
  \                          /
  └─────────────────────────┘

  border-radius: 9999px;            Forma de "pastilla" (pill)
  (─────────────────────────)       en elementos rectangulares

  border-radius: 20px 0 20px 0;     Esquinas individuales
  ┌─────────────────────────╮       (top-left, top-right,
  │                         │        bottom-right, bottom-left)
  ╰─────────────────────────┘

  border-radius: 50% 50% 50% 50% / 30% 30% 70% 70%;
                                    Forma organica (dos radios por esquina)
```

> **En `styles.css` (linea 230):** `border-radius: 80%;` en las imagenes
> crea una forma ovalada. Con un valor mayor al 50%, los bordes se curvan
> mas alla del semicirculo.

---

## 5. Clases CSS y organizacion

### Clases vs IDs vs selectores de elemento

```
  SELECTOR DE ELEMENTO          CLASE                        ID
  ──────────────────            ─────                        ──
  p { color: blue; }           .destacado { color: red; }   #titulo { color: green; }

  Selecciona TODOS los <p>     Selecciona todos los          Selecciona EL UNICO
  de la pagina.                elementos con                  elemento con
                               class="destacado".             id="titulo".

  Especificidad: 0,0,0,1      Especificidad: 0,0,1,0        Especificidad: 0,1,0,0

  Uso: estilos base            Uso: estilos reutilizables    Uso: JS y label-for-id
  (reset, tipografia)          (componentes, utilidades)     (EVITAR para CSS)
```

### Convenciones de nombres para clases

| Convencion     | Ejemplo                   | Usado en                          |
|----------------|---------------------------|-----------------------------------|
| **kebab-case** | `.mi-clase-css`           | CSS nativo (la MAS comun)         |
| **BEM**        | `.bloque__elemento--mod`  | Proyectos grandes, componentes    |
| **camelCase**  | `.miClaseCss`             | CSS-in-JS (React, styled-components) |
| **PascalCase** | `.MiClaseCss`             | Componentes en frameworks         |

> **En `styles.css` (linea 275):** La clase `.Elemento-diferente` usa
> PascalCase, lo cual funciona pero rompe la convencion. En un proyecto
> real, seria mejor `.elemento-diferente` (kebab-case).

### Impacto en especificidad

```
  Selector                  Especificidad    Resultado
  ──────────────────────    ─────────────    ──────────
  p                         0,0,0,1          Muy facil de sobreescribir
  .texto                    0,0,1,0          Equilibrado (recomendado)
  p.texto                   0,0,1,1          Un poco mas especifico
  .card .texto              0,0,2,0          Dos clases (buena practica)
  #sidebar .texto           0,1,1,0          Dificil de sobreescribir
  #sidebar p.texto          0,1,1,1          Muy dificil de sobreescribir
  style="color: red"        1,0,0,0          Casi imposible de sobreescribir
```

**Regla practica:** Mantene la especificidad lo mas baja posible.
Usa clases simples (`.boton`, `.tarjeta`, `.activo`). Evita IDs y
selectores profundamente anidados en CSS.

### El patron width + max-width

```css
  .box {
      width: 100%;
      max-width: 400px;
      margin: auto;       /* Centra horizontalmente */
  }
```

```
  Pantalla de 320px (movil):        Pantalla de 1200px (escritorio):
  ┌──────────────────────────┐      ┌─────────────────────────────────────────────┐
  │ ┌──────────────────────┐ │      │          ┌──────────────┐                   │
  │ │     .box (100%)      │ │      │          │ .box (400px) │                   │
  │ │  ocupa toda la       │ │      │          │ centrada con │                   │
  │ │  pantalla            │ │      │          │ margin: auto │                   │
  │ └──────────────────────┘ │      │          └──────────────┘                   │
  └──────────────────────────┘      └─────────────────────────────────────────────┘

  width: 100% hace que sea fluido   max-width: 400px pone un "techo"
  en pantallas pequenas.            en pantallas grandes.
```

> **En `styles.css` (linea 81):** La clase `.box` usa exactamente este patron.
> Y en la media query (linea 387), `main` usa `max-width: 900px; margin: 0 auto;`
> para el mismo efecto a nivel de contenedor principal.

---

## 6. Errores comunes

### Error 1: Imagen que no carga (ruta incorrecta)

```html
  <!-- MAL: ruta incorrecta (el archivo esta en assets/, no en la raiz) -->
  <img src="fondo3.jpg" alt="Fondo">

  <!-- BIEN: ruta relativa correcta -->
  <img src="assets/fondo3.jpg" alt="Fondo">

  <!-- MAL: ruta con barra invertida (solo funciona en Windows) -->
  <img src="assets\fondo3.jpg" alt="Fondo">

  <!-- BIEN: siempre barra normal (funciona en todos los sistemas) -->
  <img src="assets/fondo3.jpg" alt="Fondo">
```

### Error 2: CSS que no se aplica

Checklist de diagnostico:
```
  1. El <link> tiene rel="stylesheet"?
     <link href="styles.css">                    <-- FALTA rel
     <link rel="stylesheet" href="styles.css">   <-- CORRECTO

  2. La ruta del href es correcta?
     Verifica que styles.css esta en la misma carpeta que el HTML.
     Abre styles.css directamente en el navegador para confirmar.

  3. El selector es correcto?
     .mi-clase vs .Mi-Clase   <-- CSS ES sensible a mayusculas en clases
     <div class="mi-clase">   <-- Debe coincidir EXACTAMENTE

  4. Otro selector con mayor especificidad lo sobreescribe?
     Usa DevTools (F12) > Elements > Styles para ver que reglas aplican
     y cuales estan "tachadas" (sobreescritas).

  5. Hay un error de sintaxis ANTES de tu regla?
     Un punto y coma faltante o una llave sin cerrar puede
     invalidar TODO lo que viene despues.
```

### Error 3: Enlace externo sin seguridad

```html
  <!-- MAL: vulnerable a tab-nabbing -->
  <a href="https://otro-sitio.com" target="_blank">Visitar</a>

  <!-- BIEN -->
  <a href="https://otro-sitio.com" target="_blank" rel="noopener noreferrer">Visitar</a>
```

### Error 4: font shorthand invalido

```css
  /* MAL: font shorthand requiere AL MENOS font-size y font-family */
  label { font: tahoma; }     /* El navegador IGNORA toda la linea */

  /* BIEN: usa la propiedad especifica */
  label { font-family: tahoma; }

  /* O el shorthand completo */
  label { font: italic 16px tahoma; }
```

> **En `styles.css` (linea 312):** `font: tahoma;` es exactamente este error.
> El navegador ignora la declaracion por ser invalida. La correccion seria
> `font-family: tahoma;` o `font: 1rem tahoma;`.

### Error 5: Imagenes que desbordan el contenedor

```css
  /* MAL: imagen con ancho fijo que se desborda en moviles */
  img { width: 800px; }

  /* BIEN: imagen responsiva */
  img {
      max-width: 100%;    /* Nunca mas ancha que su contenedor */
      height: auto;       /* Mantiene proporciones */
  }
```

### Error 6: filter: drop-shadow con sintaxis incorrecta

```css
  /* MAL: valores separados con comas (como box-shadow) */
  filter: drop-shadow(0px, 0px, 3px, #000);

  /* BIEN: valores separados con espacios (sin comas) */
  filter: drop-shadow(0px 0px 3px #000);
```

> **En `styles.css` (linea 241):** `filter: drop-shadow(0px,0px,3px, #000)`
> tiene exactamente este error. Los valores de `drop-shadow()` se separan
> con espacios, no con comas. Ademas, `drop-shadow` no tiene parametro
> "spread" (a diferencia de `box-shadow`).

### Error 7: Espacios o caracteres especiales en nombres de archivo

```
  MAL:
  └── assets/
      ├── Mi Foto.jpg          <-- Espacio en el nombre
      ├── foto#1.jpg           <-- Caracter especial
      └── Fondo_Principal.JPG  <-- Mayusculas + extension en mayuscula

  BIEN:
  └── assets/
      ├── mi-foto.jpg
      ├── foto-01.jpg
      └── fondo-principal.jpg
```

---

## 7. Ejercicios de practica

### Ejercicio 1: Sitio de 3 paginas (Principiante)

Crea un sitio web con esta estructura:

```
  mi-sitio/
  ├── index.html          (Pagina de inicio)
  ├── galeria.html        (Galeria de imagenes)
  ├── contacto.html       (Formulario de contacto)
  ├── styles.css          (Estilos compartidos)
  └── assets/
      └── (al menos 3 imagenes)
```

Requisitos:
- Cada pagina debe tener un `<nav>` con enlaces a las otras dos paginas
- Todas deben compartir el mismo `styles.css`
- La galeria debe tener al menos 3 imagenes con `alt` descriptivo
- El formulario debe tener campos con `label` conectado via `for/id`
- Agrega `loading="lazy"` a las imagenes de la galeria

### Ejercicio 2: Formatos de imagen (Intermedio)

1. Toma una foto (o descarga una de https://unsplash.com)
2. Convierte la foto a 4 formatos: JPG, PNG, WebP y AVIF
   (puedes usar https://squoosh.app para convertir)
3. Crea una pagina que muestre las 4 versiones lado a lado
4. Debajo de cada imagen, muestra el peso del archivo
5. Implementa `<picture>` con `<source>` para que el navegador
   elija automaticamente el mejor formato

### Ejercicio 3: Tarjetas con sombras y gradientes (Intermedio)

Crea 3 tarjetas (cards) usando HTML y CSS con estos requisitos:
- Cada tarjeta tiene: imagen (con `object-fit: cover`), titulo y texto
- Usa `linear-gradient` como fondo de al menos una tarjeta
- Aplica `box-shadow` para dar efecto de elevacion
- Usa `border-radius` para esquinas redondeadas
- Implementa un efecto `:hover` que cambie la sombra (elevacion al pasar el cursor)
- El layout debe ser responsive: 1 columna en movil, 3 columnas en escritorio

### Ejercicio 4: Depurar y corregir (Avanzado)

Abre el archivo `styles.css` de este modulo y encuentra los errores:

1. **`filter: drop-shadow(0px,0px,3px, #000)`** (linea 241) -- Corrige la sintaxis
2. **`font: tahoma;`** (linea 312) -- Corrige el shorthand invalido
3. **`sans-serif` duplicado** en el font-family del body (linea 52) -- Elimina la repeticion
4. Agrega `* { box-sizing: border-box; }` al inicio para evitar sorpresas
   con el modelo de caja
5. Agrega `rel="noopener noreferrer"` al enlace externo de YouTube en `index.html`

Despues de cada correccion, verifica en el navegador que el cambio funciona.

---

## Para profundizar

### El protocolo HTTP y como viajan las paginas

```
  Cuando escribes una URL en el navegador:

  1. DNS: "www.ejemplo.com" --> 93.184.216.34 (IP del servidor)

  2. TCP: Se establece una conexion con el servidor

  3. HTTP Request:
     GET /index.html HTTP/1.1
     Host: www.ejemplo.com

  4. HTTP Response:
     HTTP/1.1 200 OK
     Content-Type: text/html
     (contenido del HTML)

  5. El navegador parsea el HTML y encuentra <link>, <img>, <script>

  6. Para CADA recurso externo, repite pasos 3-4:
     GET /styles.css HTTP/1.1      --> recibe el CSS
     GET /assets/fondo3.jpg HTTP/1.1 --> recibe la imagen
     GET /script.js HTTP/1.1       --> recibe el JavaScript

  7. Con todo descargado, renderiza la pagina
```

### Performance: optimizando carga de imagenes

```
  TECNICAS DE OPTIMIZACION:

  1. Formato correcto
     AVIF > WebP > JPEG > PNG (en tamano, para fotos)

  2. Dimensiones correctas
     No sirvas una imagen de 4000px si se muestra a 400px.
     Crea versiones en multiples tamanos (400, 800, 1200).

  3. Compresion
     JPEG al 80% de calidad pierde muy poco detalle visible
     pero puede reducir el tamano en un 60%.

  4. Lazy loading
     loading="lazy" en imagenes debajo del fold.

  5. CDN (Content Delivery Network)
     Servir imagenes desde servidores cerca del usuario.

  6. Cache
     El navegador guarda imagenes localmente para no descargarlas de nuevo.
```

### Accesibilidad en imagenes decorativas vs informativas

```
  IMAGENES INFORMATIVAS:
  Transmiten informacion que no esta disponible en el texto.
  → alt debe describir lo que muestra.

  <img src="grafica.png" alt="Ventas subieron de 100 a 250 unidades entre enero y junio">

  IMAGENES DECORATIVAS:
  Solo embellecen la pagina, no transmiten informacion.
  → alt debe estar vacio (alt=""), NO omitido.

  <img src="separador.svg" alt="">

  IMAGENES DE TEXTO:
  Contienen texto renderizado como imagen.
  → alt debe transcribir el texto completo.

  <img src="banner-oferta.jpg" alt="Oferta especial: 50% de descuento este fin de semana">

  IMAGENES FUNCIONALES:
  Son parte de un enlace o boton.
  → alt debe describir la ACCION, no la imagen.

  <a href="/home"><img src="logo.svg" alt="Ir a la pagina de inicio"></a>
  (No: alt="Logo de la empresa")
```

### Prefetching y preloading de recursos

```html
  <!-- Preload: recurso CRITICO que se necesita YA -->
  <link rel="preload" href="styles.css" as="style">
  <link rel="preload" href="hero.webp" as="image">

  <!-- Prefetch: recurso que se necesitara en la SIGUIENTE pagina -->
  <link rel="prefetch" href="pagina2.html">

  <!-- DNS Prefetch: resolver el DNS de un dominio externo por adelantado -->
  <link rel="dns-prefetch" href="https://fonts.googleapis.com">

  <!-- Preconnect: resolver DNS + establecer conexion TCP/TLS -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
```

Estas tecnicas son avanzadas pero marcan la diferencia en rendimiento real.
El navegador puede empezar a descargar recursos antes de que el parser
HTML los encuentre, reduciendo el tiempo de carga total.

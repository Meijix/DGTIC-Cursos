# Módulo 10 — Landing Page Profesional: Arquitectura CSS Moderna

> **Nivel:** Avanzado
> **Prerequisitos:** Módulos 01–09 (todo el curso anterior)
> **Objetivo:** Construir una landing page profesional aplicando arquitectura CSS,
> design systems, tipografía fluida, efectos modernos, rendimiento, accesibilidad y SEO.

---

## Tabla de contenidos

1. [Arquitectura CSS](#1-arquitectura-css)
2. [Design Systems y Variables CSS](#2-design-systems-y-variables-css)
3. [Tipografía responsive con clamp()](#3-tipografía-responsive-con-clamp)
4. [Efectos CSS modernos](#4-efectos-css-modernos)
5. [Performance web](#5-performance-web)
6. [IntersectionObserver API](#6-intersectionobserver-api)
7. [Seguridad en enlaces externos](#7-seguridad-en-enlaces-externos)
8. [SEO y meta tags](#8-seo-y-meta-tags)
9. [Accesibilidad avanzada](#9-accesibilidad-avanzada)
10. [Errores comunes](#10-errores-comunes)
11. [Ejercicios de práctica](#11-ejercicios-de-práctica)

---

## 1. Arquitectura CSS

A medida que un proyecto crece, la organización del CSS se vuelve crucial. Sin
estructura, terminamos con archivos inmanejables, selectores que se pisan entre sí
y especificidad impredecible.

### ITCSS — Inverted Triangle CSS

ITCSS (creado por Harry Roberts) organiza el CSS en capas, de lo más genérico
a lo más específico:

```
                        ITCSS: Triángulo invertido
                        ==========================

 Alcance (qué tanto afecta)         Especificidad
 ◄────── Más amplio ──────►         ◄── Más baja ──►

 ┌──────────────────────────────────────────────────────┐
 │                                                      │
 │              SETTINGS (Configuración)                │
 │         Variables, tokens de diseño                  │
 │         --color-primario, --fuente-base              │
 │                                                      │
 ├──────────────────────────────────────────────────────┤
 │                                                      │
 │            TOOLS (Herramientas)                      │
 │       Mixins, funciones (en preprocesadores)         │
 │       En CSS puro: custom properties calculadas      │
 │                                                      │
 ├──────────────────────────────────────────────────────┤
 │                                                      │
 │          GENERIC (Genérico)                          │
 │     Reset, Normalize, box-sizing                     │
 │     *, *::before, *::after { box-sizing: ... }       │
 │                                                      │
 ├──────────────────────────────────────────────────────┤
 │                                                      │
 │        ELEMENTS (Elementos base)                     │
 │   Estilos para etiquetas HTML sin clases             │
 │   h1, h2, p, a, img, ul { ... }                     │
 │                                                      │
 ├──────────────────────────────────────────────────────┤
 │                                                      │
 │      OBJECTS (Objetos de layout)                     │
 │  Patrones de estructura reutilizables                │
 │  .container, .grid, .flex-row                        │
 │                                                      │
 ├──────────────────────────────────────────────────────┤
 │                                                      │
 │    COMPONENTS (Componentes)                          │
 │  Piezas de UI específicas                            │
 │  .card, .hero, .nav, .footer, .cta-button            │
 │                                                      │
 ├──────────────────────────────────────────────────────┤
 │                                                      │
 │  UTILITIES (Utilidades)          ← Más específico    │
 │  Clases de ayuda con !important permitido            │
 │  .text-center, .hidden, .mt-2, .sr-only             │
 │                                                      │
 └──────────────────────────────────────────────────────┘

 ◄── Especificidad más alta ──►
```

### Cómo se refleja en un archivo CSS

```css
/* ============================================
   1. SETTINGS — Variables de diseño
   ============================================ */
:root {
  --color-primario: #1a365d;
  --color-acento: #e53e3e;
  --fuente-titulo: 'Georgia', serif;
  --espaciado-base: 1rem;
}

/* ============================================
   2. GENERIC — Reset y reglas globales
   ============================================ */
*, *::before, *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

/* ============================================
   3. ELEMENTS — Estilos base para etiquetas
   ============================================ */
body {
  font-family: var(--fuente-base);
  line-height: 1.6;
}

h1, h2, h3 {
  font-family: var(--fuente-titulo);
  line-height: 1.2;
}

a {
  color: var(--color-acento);
  text-decoration: none;
}

/* ============================================
   4. OBJECTS — Patrones de layout
   ============================================ */
.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 var(--espaciado-base);
}

/* ============================================
   5. COMPONENTS — Componentes de UI
   ============================================ */
.hero { ... }
.card { ... }
.nav  { ... }

/* ============================================
   6. UTILITIES — Clases de ayuda
   ============================================ */
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
}

.text-center { text-align: center !important; }
```

### Convenciones de nomenclatura

```
┌───────────────────────────────────────────────────────────────────┐
│                  CONVENCIONES POPULARES                           │
├──────────────┬────────────────────────────────────────────────────┤
│ BEM          │ .bloque__elemento--modificador                    │
│              │ .card__title--highlighted                         │
│              │ Muy explícito, fácil de entender la relación      │
├──────────────┼────────────────────────────────────────────────────┤
│ Utility-     │ .flex .items-center .gap-4 .text-lg              │
│ First        │ Clases pequeñas, composición en el HTML           │
│              │ (estilo Tailwind CSS)                             │
├──────────────┼────────────────────────────────────────────────────┤
│ SMACSS       │ Categorías: base, layout (l-), module, state     │
│              │ (is-), theme (t-)                                 │
│              │ .l-sidebar, .is-active, .t-dark                  │
├──────────────┼────────────────────────────────────────────────────┤
│ Semántico    │ Nombres descriptivos del contenido                │
│ simple       │ .hero, .nav, .proyectos, .contacto               │
│              │ Ideal para proyectos pequeños-medianos            │
└──────────────┴────────────────────────────────────────────────────┘
```

---

## 2. Design Systems y Variables CSS

### Qué es un Design System

Un design system es un conjunto de decisiones de diseño documentadas y codificadas
que garantizan consistencia visual en todo el proyecto.

```
┌──────────────────────────────────────────────────────────────┐
│                     DESIGN SYSTEM                            │
│                                                              │
│  ┌────────────┐  ┌────────────┐  ┌────────────┐             │
│  │  COLORES   │  │ TIPOGRAFÍA │  │ ESPACIADO  │             │
│  │            │  │            │  │            │             │
│  │  Primario  │  │  Títulos   │  │  4px base  │             │
│  │  Secundario│  │  Cuerpo    │  │  8px       │             │
│  │  Acento    │  │  Código    │  │  16px      │             │
│  │  Neutros   │  │  Tamaños   │  │  24px      │             │
│  │  Éxito     │  │            │  │  32px      │             │
│  │  Error     │  │            │  │  48px      │             │
│  └────────────┘  └────────────┘  └────────────┘             │
│                                                              │
│  ┌────────────┐  ┌────────────┐  ┌────────────┐             │
│  │ SOMBRAS    │  │  BORDES    │  │BREAKPOINTS │             │
│  │            │  │            │  │            │             │
│  │  Pequeña   │  │  Radius    │  │  640px sm  │             │
│  │  Mediana   │  │  Anchos    │  │  768px md  │             │
│  │  Grande    │  │  Estilos   │  │  1024px lg │             │
│  └────────────┘  └────────────┘  └────────────┘             │
│                                                              │
│              Todos codificados como                          │
│              CSS Custom Properties                           │
└──────────────────────────────────────────────────────────────┘
```

### Nombrado semántico vs literal

```
┌──────────────────────────────────────────────────────────────────────┐
│                   NIVELES DE NOMBRADO                                │
│                                                                      │
│  Nivel 1: LITERAL (describe el color)                                │
│  ──────────────────────────────                                      │
│  --navy: #1a365d;                                                    │
│  --red-500: #e53e3e;                                                 │
│  --gray-100: #f7f7f7;                                                │
│                                                                      │
│  Nivel 2: SEMÁNTICO (describe el propósito)                          │
│  ──────────────────────────────────────────                          │
│  --color-primario: var(--navy);                                      │
│  --color-acento: var(--red-500);                                     │
│  --color-fondo: var(--gray-100);                                     │
│                                                                      │
│  Nivel 3: CONTEXTUAL (describe dónde se usa)                         │
│  ─────────────────────────────────────────────                       │
│  --nav-bg: var(--color-primario);                                    │
│  --btn-bg: var(--color-acento);                                      │
│  --body-bg: var(--color-fondo);                                      │
│                                                                      │
│  Recomendación: Usa al menos los niveles 1 y 2.                     │
│  El nivel 3 es útil para proyectos grandes o con temas.             │
└──────────────────────────────────────────────────────────────────────┘
```

### Design Tokens

Los "design tokens" son la unidad más pequeña de un design system. Son los
valores primitivos que definen la identidad visual:

```css
:root {
  /* === TOKENS PRIMITIVOS === */
  /* Colores */
  --navy-900: #1a202c;
  --navy-800: #1a365d;
  --navy-700: #2a4a7f;
  --red-500: #e53e3e;
  --red-600: #c53030;
  --white: #ffffff;
  --gray-50: #fafafa;
  --gray-100: #f5f5f5;
  --gray-800: #2d3748;

  /* Tipografía */
  --font-sans: 'Inter', system-ui, sans-serif;
  --font-serif: 'Georgia', serif;

  /* Espaciado (escala de 4px) */
  --space-1: 0.25rem;   /*  4px */
  --space-2: 0.5rem;    /*  8px */
  --space-4: 1rem;      /* 16px */
  --space-6: 1.5rem;    /* 24px */
  --space-8: 2rem;      /* 32px */
  --space-12: 3rem;     /* 48px */
  --space-16: 4rem;     /* 64px */

  /* === TOKENS SEMÁNTICOS === */
  --color-bg: var(--white);
  --color-text: var(--gray-800);
  --color-primary: var(--navy-800);
  --color-accent: var(--red-500);
  --color-accent-hover: var(--red-600);
}
```

### Temas con CSS Variables (ejemplo: modo oscuro)

```css
/* Tema claro (por defecto) */
:root {
  --color-bg: #ffffff;
  --color-text: #1a202c;
  --color-surface: #f7fafc;
  --color-border: #e2e8f0;
  --color-primary: #2b6cb0;
}

/* Tema oscuro */
[data-theme="dark"] {
  --color-bg: #1a202c;
  --color-text: #e2e8f0;
  --color-surface: #2d3748;
  --color-border: #4a5568;
  --color-primary: #63b3ed;
}

/* Los componentes usan las variables, NO colores directos */
body {
  background-color: var(--color-bg);
  color: var(--color-text);
}

.card {
  background-color: var(--color-surface);
  border: 1px solid var(--color-border);
}
```

```
Tema claro:                          Tema oscuro:
┌─────────────────────────┐          ┌─────────────────────────┐
│ ░░░░░░░░░░░░░░░░░░░░░░ │          │ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ │
│ ░ Texto oscuro        ░ │          │ ▓ Texto claro         ▓ │
│ ░                     ░ │          │ ▓                     ▓ │
│ ░ ┌─────────────────┐ ░ │          │ ▓ ┌─────────────────┐ ▓ │
│ ░ │ Card (gris      │ ░ │          │ ▓ │ Card (gris      │ ▓ │
│ ░ │ muy claro)      │ ░ │          │ ▓ │ oscuro)         │ ▓ │
│ ░ └─────────────────┘ ░ │          │ ▓ └─────────────────┘ ▓ │
│ ░░░░░░░░░░░░░░░░░░░░░░ │          │ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ │
└─────────────────────────┘          └─────────────────────────┘

MISMO CSS, MISMOS COMPONENTES
Solo cambian los valores de las variables.
```

```javascript
// Toggle de tema con JavaScript
const toggle = document.querySelector('.theme-toggle');
toggle.addEventListener('click', () => {
  const actual = document.documentElement.getAttribute('data-theme');
  const nuevo = actual === 'dark' ? 'light' : 'dark';
  document.documentElement.setAttribute('data-theme', nuevo);
});
```

---

## 3. Tipografía responsive con clamp()

### El problema

La tipografía debe ser legible en todos los tamaños de pantalla:

```
Móvil (375px):              Escritorio (1440px):
┌────────────────┐          ┌──────────────────────────────────────────┐
│                │          │                                          │
│  Título muy    │          │  Título muy grande y                     │
│  grande y      │          │  prominente aquí                         │
│  prominente    │          │                                          │
│  aquí          │          │  Texto de párrafo con un tamaño          │
│                │          │  cómodo para leer en pantalla grande.    │
│  Texto de      │          │                                          │
│  párrafo...    │          │                                          │
└────────────────┘          └──────────────────────────────────────────┘

  font-size: 2rem              font-size: 3.5rem
  (32px)                       (56px)
```

### La solución clásica: media queries

```css
/* Funciona pero tiene "saltos" entre breakpoints */
h1 { font-size: 2rem; }

@media (min-width: 768px) {
  h1 { font-size: 2.5rem; }
}

@media (min-width: 1024px) {
  h1 { font-size: 3rem; }
}

@media (min-width: 1440px) {
  h1 { font-size: 3.5rem; }
}
```

```
Tamaño de fuente con media queries:

3.5rem │                              ┌──────────
       │                              │
3.0rem │                    ┌─────────┘    Saltos
       │                    │              abruptos
2.5rem │          ┌─────────┘
       │          │
2.0rem │──────────┘
       │
       └──────────┬──────────┬──────────┬──────────►
               768px      1024px     1440px     Ancho
```

### La solución moderna: `clamp()`

```css
/* Transición FLUIDA entre tamaños */
h1 {
  font-size: clamp(2rem, 5vw, 3.5rem);
}
/*                │      │       │
                  │      │       └─ MÁXIMO: nunca más grande que 3.5rem (56px)
                  │      │
                  │      └── PREFERIDO: 5% del ancho del viewport
                  │          (en 1000px de ancho = 50px)
                  │
                  └─── MÍNIMO: nunca más pequeño que 2rem (32px)
*/
```

```
Tamaño de fuente con clamp():

3.5rem │                              ────────────
       │                           ╱
3.0rem │                        ╱       Transición
       │                     ╱          suave y
2.5rem │                  ╱             continua
       │               ╱
2.0rem │───────────────╱
       │
       └──────────┬──────────┬──────────┬──────────►
               640px      1000px     1440px     Ancho

       │  MÍNIMO  │  CRECE LINEALMENTE  │  MÁXIMO  │
       │  2rem    │  (siguiendo vw)     │  3.5rem  │
```

### Cómo funciona paso a paso

```
font-size: clamp(2rem, 5vw, 3.5rem);

Viewport = 320px  →  5vw = 16px   →  Menor que 2rem (32px) → USA 2rem (32px)
Viewport = 640px  →  5vw = 32px   →  Igual que 2rem (32px) → USA 32px
Viewport = 800px  →  5vw = 40px   →  Entre min y max       → USA 40px (2.5rem)
Viewport = 1000px →  5vw = 50px   →  Entre min y max       → USA 50px (3.125rem)
Viewport = 1120px →  5vw = 56px   →  Igual que 3.5rem      → USA 56px (3.5rem)
Viewport = 1920px →  5vw = 96px   →  Mayor que 3.5rem      → USA 3.5rem (56px)
```

### Escala tipográfica completa con clamp()

```css
:root {
  /* Escala tipográfica fluida */
  --text-sm:   clamp(0.875rem, 0.8rem + 0.2vw, 1rem);
  --text-base: clamp(1rem, 0.9rem + 0.3vw, 1.125rem);
  --text-lg:   clamp(1.125rem, 1rem + 0.5vw, 1.5rem);
  --text-xl:   clamp(1.5rem, 1.2rem + 1vw, 2rem);
  --text-2xl:  clamp(1.75rem, 1.2rem + 2vw, 2.5rem);
  --text-3xl:  clamp(2rem, 1.5rem + 2.5vw, 3rem);
  --text-4xl:  clamp(2.5rem, 1.5rem + 3vw, 3.5rem);
  --text-hero: clamp(3rem, 2rem + 4vw, 5rem);
}

h1 { font-size: var(--text-hero); }
h2 { font-size: var(--text-3xl); }
h3 { font-size: var(--text-2xl); }
p  { font-size: var(--text-base); }
```

### clamp() para espaciado

No solo es para tipografía. Funciona con cualquier propiedad que acepte longitudes:

```css
.seccion {
  padding: clamp(2rem, 5vw, 6rem) clamp(1rem, 3vw, 4rem);
  /*       padding vertical          padding horizontal     */
  gap: clamp(1rem, 2vw, 2rem);
}
```

---

## 4. Efectos CSS modernos

### `backdrop-filter` — Glassmorphism

```css
.tarjeta-glass {
  background: rgba(255, 255, 255, 0.15);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px); /* Safari */
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 16px;
}
```

```
SIN backdrop-filter:               CON backdrop-filter: blur(12px):
┌───────────────────────┐          ┌───────────────────────┐
│  Imagen de fondo      │          │  Imagen de fondo      │
│  ┌─────────────────┐  │          │  ┌─────────────────┐  │
│  │ Tarjeta         │  │          │  │░░░░░░░░░░░░░░░░░│  │
│  │ (fondo          │  │          │  │░ Tarjeta        ░│  │
│  │  semi-          │  │          │  │░ (fondo borroso ░│  │
│  │  transparente)  │  │          │  │░  cristal)      ░│  │
│  │ Se ve el fondo  │  │          │  │░ El fondo se ve ░│  │
│  │ perfectamente   │  │          │  │░ difuminado     ░│  │
│  └─────────────────┘  │          │  └─────────────────┘  │
│                       │          │                       │
└───────────────────────┘          └───────────────────────┘
```

### Pseudo-elementos `::before` y `::after`

Los pseudo-elementos crean "sub-elementos" virtuales que no existen en el HTML,
ideales para efectos decorativos.

```css
/* Línea decorativa debajo de un título */
.titulo::after {
  content: '';              /* OBLIGATORIO: sin esto no se renderiza */
  display: block;
  width: 60px;
  height: 4px;
  background-color: var(--color-acento);
  margin-top: 0.5rem;
  border-radius: 2px;
}
```

```
DOM real:                        Lo que se renderiza:
┌────────────────────┐           ┌────────────────────┐
│  <h2 class="titulo">          │  Mis Proyectos      │
│    Mis Proyectos   │           │  ════                │ ← ::after
│  </h2>             │           │  (línea roja)       │
│                    │           │                     │
│  (no hay más       │           │  (el ::after se     │
│   elementos en     │           │   genera en CSS,    │
│   el HTML)         │           │   no en el HTML)    │
└────────────────────┘           └────────────────────┘
```

**Ejemplo avanzado: overlay oscuro sobre una imagen hero:**

```css
.hero {
  position: relative;
  background-image: url('hero.jpg');
  background-size: cover;
}

.hero::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(
    to bottom,
    rgba(0, 0, 0, 0.6),
    rgba(0, 0, 0, 0.3)
  );
  z-index: 1;
}

.hero__contenido {
  position: relative;
  z-index: 2;  /* Encima del overlay */
  color: white;
}
```

```
Capas del hero:
┌──────────────────────────────────┐
│  z-index: 2  CONTENIDO (texto)  │  ← Encima de todo
├──────────────────────────────────┤
│  z-index: 1  ::before (overlay) │  ← Oscurece la imagen
├──────────────────────────────────┤
│  z-index: auto  IMAGEN DE FONDO │  ← La imagen hero
└──────────────────────────────────┘
```

### CSS Filters

```css
/* Escala de grises */
img { filter: grayscale(100%); }
img:hover { filter: grayscale(0%); transition: filter 0.5s; }

/* Otros filtros disponibles */
filter: blur(5px);           /* Desenfoque */
filter: brightness(1.2);     /* Brillo (1 = normal) */
filter: contrast(1.5);       /* Contraste */
filter: saturate(2);         /* Saturación */
filter: sepia(100%);         /* Efecto sepia */
filter: hue-rotate(90deg);   /* Rotar tono */
filter: invert(100%);        /* Invertir colores */
filter: drop-shadow(2px 4px 6px rgba(0,0,0,0.3));

/* Combinación de filtros */
filter: grayscale(50%) brightness(1.1) contrast(1.2);
```

```
ORIGINAL          grayscale(100%)    sepia(100%)
┌──────────┐      ┌──────────┐      ┌──────────┐
│ ████████ │      │ ▓▓▓▓▓▓▓▓ │      │ ░▒▓▒░▒▓▒ │
│ ██FOTO██ │      │ ▓▓FOTO▓▓ │      │ ░▒FOTO▒░ │
│ ██COLOR█ │      │ ▓▓GRIS▓▓ │      │ ░▒SEPIA▒ │
│ ████████ │      │ ▓▓▓▓▓▓▓▓ │      │ ░▒▓▒░▒▓▒ │
└──────────┘      └──────────┘      └──────────┘

blur(5px)          brightness(1.5)   hue-rotate(90deg)
┌──────────┐      ┌──────────┐      ┌──────────┐
│ ░░░░░░░░ │      │ ████████ │      │ ████████ │
│ ░░DESFO░ │      │ ██MÁS ██ │      │ ██COLORE│
│ ░░CADO░░ │      │ ██CLARO█ │      │ ██ROTADO│
│ ░░░░░░░░ │      │ ████████ │      │ ████████ │
└──────────┘      └──────────┘      └──────────┘
```

### mix-blend-mode

Controla cómo se mezcla un elemento con su fondo, similar a los modos de
mezcla de Photoshop:

```css
.texto-blend {
  color: white;
  mix-blend-mode: difference;  /* Invierte colores donde se superpone */
}

.imagen-blend {
  mix-blend-mode: multiply;    /* Oscurece: mezcla multiplicativa */
}
```

| Modo         | Efecto                                               |
|-------------|------------------------------------------------------|
| `normal`    | Sin mezcla (por defecto)                             |
| `multiply`  | Oscurece: mezcla multiplicativa de colores           |
| `screen`    | Aclara: inverso de multiply                          |
| `overlay`   | Combina multiply y screen según luminosidad          |
| `difference`| Resta colores (crea efecto de inversión)             |
| `exclusion` | Similar a difference pero más suave                  |

---

## 5. Performance web

### El pipeline de renderizado del navegador

```
 Cuando el navegador recibe HTML y CSS, sigue estos pasos:

 ┌──────┐    ┌───────┐    ┌────────────┐    ┌────────┐    ┌───────┐    ┌───────────┐
 │ HTML │    │ CSSOM │    │  Render    │    │ Layout │    │ Paint │    │ Composite │
 │ DOM  │───►│       │───►│  Tree      │───►│        │───►│       │───►│           │
 │      │    │       │    │            │    │        │    │       │    │           │
 └──────┘    └───────┘    └────────────┘    └────────┘    └───────┘    └───────────┘
   │            │              │                │             │              │
   │            │              │                │             │              │
   Parsea el    Parsea el     Combina DOM      Calcula       Rellena       Combina
   HTML en un   CSS en un     y CSSOM.         posición y    los píxeles   las capas
   árbol de     árbol de      Solo incluye     tamaño de     de cada       pintadas
   objetos      estilos       elementos        cada          elemento      en la
                              visibles         elemento                    pantalla
                              (no display:
                               none)

COSTO:
  Layout > Paint > Composite

  Si cambias WIDTH    → se ejecuta Layout + Paint + Composite (lento)
  Si cambias COLOR    → se ejecuta Paint + Composite (medio)
  Si cambias TRANSFORM → se ejecuta solo Composite (rápido)
```

### Por qué `transform` y `opacity` son baratas

```
┌─────────────────────────────────────────────────────────┐
│  Cuando animas transform u opacity:                      │
│                                                         │
│  1. El navegador promueve el elemento a su propia       │
│     "capa" (layer) en la GPU                            │
│                                                         │
│  2. La GPU mueve/transforma esa capa sin tocar          │
│     el resto del documento                              │
│                                                         │
│  3. El hilo principal de JavaScript queda LIBRE          │
│     (no hay janks ni bloqueos)                          │
│                                                         │
│  Resultado: 60fps consistentes                          │
└─────────────────────────────────────────────────────────┘
```

### `loading="lazy"` para imágenes

```html
<!-- El navegador NO carga esta imagen hasta que esté cerca del viewport -->
<img src="proyecto-3.jpg"
     alt="Captura del proyecto 3"
     width="800"
     height="600"
     loading="lazy">

<!-- Las imágenes "above the fold" NO deben tener lazy loading -->
<img src="hero.jpg"
     alt="Imagen principal"
     width="1920"
     height="1080"
     loading="eager">  <!-- O simplemente no poner loading -->
```

```
Página con 20 imágenes:

SIN lazy loading:                    CON lazy loading:
┌─────────────────────┐             ┌─────────────────────┐
│ Viewport            │             │ Viewport            │
│ ┌─────┐ ┌─────┐    │             │ ┌─────┐ ┌─────┐    │
│ │IMG 1│ │IMG 2│    │             │ │IMG 1│ │IMG 2│    │  Cargadas
│ └─────┘ └─────┘    │             │ └─────┘ └─────┘    │
│ ┌─────┐ ┌─────┐    │             │ ┌─────┐ ┌─────┐    │
│ │IMG 3│ │IMG 4│    │             │ │IMG 3│ │IMG 4│    │
│ └─────┘ └─────┘    │             │ └─────┘ └─────┘    │
└─────────────────────┘             └─────────────────────┘
  ┌─────┐ ┌─────┐                    ┌─────┐ ┌─────┐
  │IMG 5│ │IMG 6│ Cargadas           │ --- │ │ --- │  NO cargadas
  └─────┘ └─────┘ aunque no          └─────┘ └─────┘  (se cargan
  ... (16 más)     se ven             ... (16 más)     al acercarse)

  Carga inicial:                     Carga inicial:
  20 imágenes = lento                4 imágenes = rápido
```

### CLS (Cumulative Layout Shift)

```
SIN width/height en <img>:            CON width/height en <img>:

Antes de cargar:                      Antes de cargar:
┌──────────────────────┐              ┌──────────────────────┐
│ Título del artículo  │              │ Título del artículo  │
│ Párrafo de texto     │              │ ┌──────────────────┐ │
│ que el usuario       │              │ │                  │ │
│ está leyendo...      │              │ │  Espacio         │ │
└──────────────────────┘              │ │  reservado       │ │
                                      │ │  (300x200)       │ │
Después de cargar imagen:             │ └──────────────────┘ │
┌──────────────────────┐              │ Párrafo de texto     │
│ Título del artículo  │              │ que el usuario       │
│ ┌──────────────────┐ │              │ está leyendo...      │
│ │                  │ │              └──────────────────────┘
│ │  IMAGEN CARGADA  │ │
│ │                  │ │              Después de cargar imagen:
│ └──────────────────┘ │              ┌──────────────────────┐
│ Párrafo de texto ↓↓↓ │ ← ¡SALTO!   │ Título del artículo  │
│ que el usuario   ↓↓↓ │              │ ┌──────────────────┐ │
│ está leyendo...  ↓↓↓ │              │ │  IMAGEN CARGADA  │ │
└──────────────────────┘              │ └──────────────────┘ │
                                      │ Párrafo de texto     │ ← Sin salto
                                      │ que el usuario       │
                                      │ está leyendo...      │
                                      └──────────────────────┘
```

```html
<!-- SIEMPRE incluir width y height para evitar CLS -->
<img src="foto.jpg" alt="Descripción" width="800" height="600">
```

### `<link rel="preload">`

```html
<head>
  <!-- Precarga recursos críticos que el navegador descubrirá tarde -->
  <link rel="preload" href="fuente-titulo.woff2" as="font"
        type="font/woff2" crossorigin>
  <link rel="preload" href="hero.jpg" as="image">
</head>
```

```
SIN preload:
HTML ──► CSS ──► CSS descubre @font-face ──► Descarga fuente ──► Renderiza texto
                                              (TARDE)

CON preload:
HTML ──► Empieza descarga de fuente (en paralelo con CSS)
     └─► CSS ──► La fuente ya está lista ──► Renderiza texto
                                              (ANTES)
```

---

## 6. IntersectionObserver API

### Constructor y opciones

```javascript
const observer = new IntersectionObserver(callback, opciones);
```

```javascript
// Las opciones
const opciones = {
  root: null,          // null = viewport; o un elemento contenedor
  rootMargin: '0px',   // Margen alrededor del root (como CSS margin)
  threshold: 0.1       // 0 a 1: qué porcentaje debe ser visible
                       // 0 = apenas 1px visible
                       // 0.5 = 50% visible
                       // 1 = 100% visible
                       // [0, 0.25, 0.5, 0.75, 1] = múltiples umbrales
};
```

### rootMargin visualizado

```
rootMargin: '0px'                    rootMargin: '-100px 0px'
(zona de detección = viewport)       (zona de detección reducida)

┌─ Viewport ──────────────┐          ┌─ Viewport ──────────────┐
│                          │          │                          │
│  Zona de detección       │          │  (100px ignorados)       │
│  ┌────────────────────┐  │          │  ┌ ─ ─ ─ ─ ─ ─ ─ ─ ─┐  │
│  │                    │  │          │                          │
│  │                    │  │          │  │ Zona de detección  │  │
│  │                    │  │          │     (más pequeña)        │
│  └────────────────────┘  │          │  │                    │  │
│                          │          │                          │
│                          │          │  └ ─ ─ ─ ─ ─ ─ ─ ─ ─┘  │
│                          │          │  (100px ignorados)       │
└──────────────────────────┘          └──────────────────────────┘


rootMargin: '200px 0px'
(zona de detección EXPANDIDA — detecta elementos ANTES de ser visibles)

          ┌ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─┐
          │ 200px extra arriba     │
┌─ Viewport ──────────────┐
│         │                │       │
│                          │
│         │                │       │
│                          │
│         │                │       │
└─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─┘
          │ 200px extra abajo      │
          └ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─┘

Útil para empezar animaciones o lazy loading ANTES
de que el elemento entre al viewport.
```

### El callback y las entries

```javascript
const observer = new IntersectionObserver((entries, observer) => {
  entries.forEach(entry => {
    // entry.target            → El elemento observado (DOM node)
    // entry.isIntersecting    → Boolean: ¿está intersectando?
    // entry.intersectionRatio → 0 a 1: qué tanto se ve
    // entry.boundingClientRect→ Rectángulo del elemento
    // entry.rootBounds        → Rectángulo del root
    // entry.time              → Timestamp del evento

    if (entry.isIntersecting) {
      console.log(`${entry.target.id} es visible al ${
        Math.round(entry.intersectionRatio * 100)
      }%`);
    }
  });
});
```

### Ejemplo completo del ejercicio

```javascript
// ═══════════════════════════════════════════════════════════
// Animación de revelado al hacer scroll (Scroll Reveal)
// ═══════════════════════════════════════════════════════════

// 1. Seleccionar todos los elementos que queremos animar
const elementosAnimados = document.querySelectorAll('.animar-al-scroll');

// 2. Crear el observer con opciones
const observerOpciones = {
  root: null,            // Usar el viewport
  rootMargin: '0px 0px -50px 0px',  // Activar 50px antes del borde inferior
  threshold: 0.1         // Cuando el 10% sea visible
};

// 3. Definir el callback
function manejarInterseccion(entries, observer) {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      // Agregar clase que activa la animación CSS
      entry.target.classList.add('visible');

      // Dejar de observar (la animación solo ocurre una vez)
      observer.unobserve(entry.target);
    }
  });
}

// 4. Crear el observer
const miObserver = new IntersectionObserver(manejarInterseccion, observerOpciones);

// 5. Observar cada elemento
elementosAnimados.forEach(elemento => {
  miObserver.observe(elemento);
});
```

```css
/* CSS correspondiente */
.animar-al-scroll {
  opacity: 0;
  transform: translateY(30px);
  transition: opacity 0.6s ease-out, transform 0.6s ease-out;
}

.animar-al-scroll.visible {
  opacity: 1;
  transform: translateY(0);
}
```

### Casos de uso más allá de animaciones

```
┌───────────────────────────────────────────────────────────────┐
│            CASOS DE USO DE IntersectionObserver               │
├───────────────────┬───────────────────────────────────────────┤
│ Lazy Loading      │ Cargar imágenes solo cuando estén cerca   │
│ de imágenes       │ del viewport (reemplazar src placeholder) │
├───────────────────┼───────────────────────────────────────────┤
│ Infinite Scroll   │ Observar un "sentinel" al final de la     │
│                   │ lista. Cuando es visible, cargar más.     │
├───────────────────┼───────────────────────────────────────────┤
│ Analytics         │ Registrar qué secciones vio el usuario    │
│ (tracking)        │ y por cuánto tiempo.                      │
├───────────────────┼───────────────────────────────────────────┤
│ Video autoplay    │ Pausar videos cuando salen del viewport.  │
│                   │ Reproducir cuando vuelven.                │
├───────────────────┼───────────────────────────────────────────┤
│ Nav tracking      │ Destacar el enlace de navegación de la    │
│                   │ sección actualmente visible.              │
├───────────────────┼───────────────────────────────────────────┤
│ Sticky headers    │ Cambiar estilo del header cuando el       │
│ dinámicos         │ hero deja de ser visible.                 │
└───────────────────┴───────────────────────────────────────────┘
```

---

## 7. Seguridad en enlaces externos

### La vulnerabilidad de `target="_blank"`

```
Cuando usas target="_blank" SIN protección:

1. Tu página abre un enlace en una nueva pestaña
2. La nueva pestaña tiene acceso a window.opener
3. La nueva pestaña puede CAMBIAR la URL de tu página original

                    Tu página                     Página maliciosa
                  ┌─────────────┐               ┌──────────────────┐
                  │ portfolio   │  target=       │ Recurso externo  │
   Usuario ──►   │ .com        │  "_blank"  ──► │                  │
                  │             │               │ window.opener     │
                  │             │   ◄────────── │ .location =      │
                  │ ¡REDIRIGIDO!│               │ 'phishing.com'   │
                  └─────────────┘               └──────────────────┘

El usuario regresa a la pestaña original y encuentra
una página de phishing que parece tu sitio.
Esto se llama TABNABBING.
```

### La solución: `rel="noopener noreferrer"`

```html
<!-- VULNERABLE -->
<a href="https://externo.com" target="_blank">Visitar</a>

<!-- SEGURO -->
<a href="https://externo.com" target="_blank" rel="noopener noreferrer">Visitar</a>
```

| Atributo     | Qué hace                                                     |
|-------------|--------------------------------------------------------------|
| `noopener`  | La nueva pestaña NO tiene acceso a `window.opener`.          |
|             | Elimina la vulnerabilidad de tabnabbing.                     |
| `noreferrer`| No envía la cabecera `Referer` al sitio destino.             |
|             | El sitio destino no sabe DESDE DÓNDE llegó el usuario.      |
|             | También implica `noopener` (doble protección).              |

### Cuándo usar `target="_blank"`

```
USAR target="_blank":                 NO USAR target="_blank":
─────────────────────                 ─────────────────────────
✓ Enlaces a sitios externos          ✗ Navegación interna del sitio
✓ Documentos PDF que el              ✗ Enlaces entre secciones de
  usuario querrá descargar             la misma página (#anclas)
✓ Enlaces en formularios             ✗ Pasos de un proceso
  (para no perder datos)               (checkout, registro)
```

> **Nota:** Los navegadores modernos (Chrome 88+, Firefox 79+) ya aplican
> `noopener` automáticamente a `target="_blank"`. Sin embargo, agregar
> `rel="noopener noreferrer"` explícitamente es buena práctica para
> compatibilidad con navegadores más antiguos.

---

## 8. SEO y meta tags

### Meta description

```html
<head>
  <meta name="description"
        content="Portfolio de Juan Pérez, desarrollador web frontend.
                 Proyectos en HTML, CSS y JavaScript.">
</head>
```

```
En los resultados de búsqueda de Google:

┌──────────────────────────────────────────────────────┐
│  Juan Pérez | Desarrollador Web Frontend             │  ← <title>
│  www.juanperez.dev                                   │  ← URL
│  Portfolio de Juan Pérez, desarrollador web          │
│  frontend. Proyectos en HTML, CSS y JavaScript.      │  ← meta description
└──────────────────────────────────────────────────────┘

REGLAS:
  - Máximo 155-160 caracteres (Google trunca el resto)
  - Debe ser único para cada página
  - Debe incluir palabras clave relevantes de forma NATURAL
  - Debe motivar el clic (es tu "anuncio" gratuito)
```

### Open Graph (og:) para redes sociales

```html
<head>
  <!-- Open Graph: controla cómo se ve al compartir en Facebook/LinkedIn/etc -->
  <meta property="og:title" content="Juan Pérez | Desarrollador Web">
  <meta property="og:description" content="Portfolio de desarrollo web frontend">
  <meta property="og:image" content="https://juanperez.dev/preview.jpg">
  <meta property="og:url" content="https://juanperez.dev">
  <meta property="og:type" content="website">

  <!-- Twitter Card: controla cómo se ve al compartir en Twitter/X -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Juan Pérez | Desarrollador Web">
  <meta name="twitter:description" content="Portfolio de desarrollo web frontend">
  <meta name="twitter:image" content="https://juanperez.dev/preview.jpg">
</head>
```

```
Al compartir en redes sociales:

SIN Open Graph:                     CON Open Graph:
┌──────────────────────┐            ┌──────────────────────┐
│                      │            │ ┌──────────────────┐ │
│  juanperez.dev       │            │ │                  │ │
│  (solo la URL)       │            │ │  IMAGEN PREVIEW  │ │
│                      │            │ │  (og:image)      │ │
│                      │            │ └──────────────────┘ │
│                      │            │ Juan Pérez | Dev Web │
│                      │            │ Portfolio de         │
│                      │            │ desarrollo web...    │
└──────────────────────┘            └──────────────────────┘
```

### La fórmula del `<title>`

```html
<!-- Formato recomendado -->
<title>Página — Marca</title>
<title>Proyectos | Juan Pérez</title>
<title>Sobre Mí — Portfolio de Juan Pérez</title>

<!-- Para la página principal -->
<title>Juan Pérez | Desarrollador Web Frontend</title>
```

```
REGLAS para el <title>:
─────────────────────
  - Máximo 60 caracteres (Google trunca el resto)
  - La palabra clave más importante va PRIMERO
  - Separador: | o — o : (consistente en todo el sitio)
  - Cada página debe tener un título ÚNICO
  - NO repetir la marca en exceso: "Mi Portfolio | Mi Portfolio Web"
```

### Datos estructurados (Schema.org) — básicos

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Person",
  "name": "Juan Pérez",
  "jobTitle": "Desarrollador Web Frontend",
  "url": "https://juanperez.dev",
  "sameAs": [
    "https://github.com/juanperez",
    "https://linkedin.com/in/juanperez"
  ]
}
</script>
```

Esto ayuda a Google a entender que tu página es sobre una PERSONA con una
profesión, y puede mostrar información enriquecida en los resultados.

---

## 9. Accesibilidad avanzada

### Skip Links (enlaces de salto)

Los usuarios de teclado y lectores de pantalla deben poder saltar la navegación
repetitiva para ir directamente al contenido principal.

```html
<!-- PRIMER elemento del <body> -->
<a href="#contenido-principal" class="skip-link">
  Saltar al contenido principal
</a>

<nav>...</nav>

<main id="contenido-principal">
  <!-- Contenido aquí -->
</main>
```

```css
.skip-link {
  position: absolute;
  top: -100%;           /* Oculto fuera de pantalla */
  left: 50%;
  transform: translateX(-50%);
  background: var(--color-primary);
  color: white;
  padding: 0.75rem 1.5rem;
  z-index: 10000;
  transition: top 0.2s;
}

.skip-link:focus {
  top: 10px;            /* Aparece al recibir foco con Tab */
}
```

```
Experiencia del usuario con teclado:

1. El usuario llega a la página y presiona Tab
2. El skip link APARECE en la parte superior:

   ┌──────────────────────────────────────────────┐
   │  ┌────────────────────────────────────────┐  │
   │  │  [ Saltar al contenido principal ]     │  │ ← Visible con foco
   │  └────────────────────────────────────────┘  │
   │  ┌────────────────────────────────────────┐  │
   │  │  NAV: Inicio | Proyectos | Contacto   │  │
   │  └────────────────────────────────────────┘  │
   │                                              │
   │  Contenido principal...                      │
   └──────────────────────────────────────────────┘

3. Si presiona Enter, salta directamente al <main>
4. Si presiona Tab de nuevo, el skip link desaparece
   y el foco va al primer enlace del nav
```

### Atributos ARIA: cuándo usar cada uno

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    COMPARACIÓN DE ATRIBUTOS ARIA                        │
├───────────────────┬─────────────────────────────────────────────────────┤
│  aria-label       │  Etiqueta invisible que REEMPLAZA el contenido      │
│                   │  visible para lectores de pantalla.                 │
│                   │                                                     │
│                   │  <button aria-label="Cerrar menú">                  │
│                   │    <svg>...</svg>  <!-- Icono sin texto -->         │
│                   │  </button>                                          │
│                   │                                                     │
│                   │  El lector dice: "Cerrar menú, botón"              │
├───────────────────┼─────────────────────────────────────────────────────┤
│  aria-labelledby  │  Apunta a OTRO elemento cuyo texto sirve como      │
│                   │  etiqueta. Referencia por ID.                      │
│                   │                                                     │
│                   │  <h2 id="titulo-seccion">Mis proyectos</h2>       │
│                   │  <section aria-labelledby="titulo-seccion">        │
│                   │    ...                                              │
│                   │  </section>                                         │
│                   │                                                     │
│                   │  El lector dice: "Mis proyectos, región"           │
├───────────────────┼─────────────────────────────────────────────────────┤
│  aria-describedby │  Apunta a OTRO elemento cuyo texto sirve como      │
│                   │  DESCRIPCIÓN adicional (no etiqueta).              │
│                   │                                                     │
│                   │  <input aria-describedby="ayuda-email">            │
│                   │  <p id="ayuda-email">                              │
│                   │    Ejemplo: usuario@correo.com                     │
│                   │  </p>                                               │
│                   │                                                     │
│                   │  El lector dice: "Email, campo de texto.           │
│                   │  Ejemplo: usuario@correo.com"                      │
└───────────────────┴─────────────────────────────────────────────────────┘
```

**Regla de oro:** Si un elemento HTML nativo ya transmite el significado
(como `<button>` con texto visible, o `<img>` con alt), NO necesitas ARIA.

```
Primera regla de ARIA:
"No uses ARIA si puedes usar HTML semántico nativo"

MAL:  <div role="button" tabindex="0" aria-label="Enviar">Enviar</div>
BIEN: <button>Enviar</button>
```

### Gestión del foco y navegación por teclado

```
Orden de tabulación natural:

  Tab ──► [Skip link] ──► [Logo] ──► [Nav link 1] ──► [Nav link 2]
                                                            │
  ◄──────────────────────────────────────────────────────────┘
     │
     ▼
  [Botón CTA del hero] ──► [Link 1 de proyectos] ──► ...

REGLAS:
  1. NUNCA uses tabindex > 0 (rompe el orden natural)
  2. Usa tabindex="0" para hacer focusable un elemento no interactivo
  3. Usa tabindex="-1" para que JS pueda darle foco pero NO tab
  4. Los elementos interactivos (a, button, input) ya son focusables
```

**Ejemplo de foco con JavaScript:**

```javascript
// Después de una acción, mover el foco al resultado
document.querySelector('#resultado').focus();

// Para que un elemento no interactivo sea focusable por JS:
// <div id="resultado" tabindex="-1">Tu mensaje fue enviado.</div>
```

### WCAG 2.1 — Niveles de conformidad

```
┌─────────────────────────────────────────────────────────────────┐
│                   NIVELES WCAG 2.1                               │
├─────────┬───────────────────────────────────────────────────────┤
│         │                                                       │
│  Nivel  │  Lo MÍNIMO absoluto. Sin esto, el contenido es       │
│    A    │  inaccesible para algunos usuarios.                   │
│         │                                                       │
│         │  Ejemplos:                                            │
│         │  - Texto alternativo en imágenes (alt)                │
│         │  - No depender solo del color para transmitir info    │
│         │  - Contenido navegable con teclado                    │
│         │                                                       │
├─────────┼───────────────────────────────────────────────────────┤
│         │                                                       │
│  Nivel  │  El ESTÁNDAR recomendado. La mayoría de              │
│   AA    │  legislaciones exigen este nivel.                     │
│         │                                                       │
│         │  Ejemplos (adicionales a A):                          │
│         │  - Contraste de color mínimo 4.5:1 (texto normal)    │
│         │  - Contraste mínimo 3:1 (texto grande)               │
│         │  - Texto redimensionable hasta 200%                   │
│         │  - Indicador de foco visible                          │
│         │                                                       │
├─────────┼───────────────────────────────────────────────────────┤
│         │                                                       │
│  Nivel  │  El nivel MÁS ALTO. Difícil de alcanzar              │
│   AAA   │  completamente, pero ideal como meta.                │
│         │                                                       │
│         │  Ejemplos (adicionales a AA):                         │
│         │  - Contraste de color mínimo 7:1                      │
│         │  - Lenguaje de señas para contenido multimedia        │
│         │  - No hay límite de tiempo en interacciones           │
│         │                                                       │
└─────────┴───────────────────────────────────────────────────────┘
```

### Pruebas básicas de accesibilidad

```
PRUEBA RÁPIDA DE 5 MINUTOS:
────────────────────────────

1. TECLADO: Navega tu sitio SOLO con Tab, Shift+Tab y Enter.
   ¿Puedes llegar a todo? ¿Ves dónde está el foco?

2. ZOOM: Haz zoom al 200% (Ctrl/Cmd + +).
   ¿Se lee todo? ¿Algo se rompe?

3. LECTORES: Usa el lector de pantalla integrado:
   - macOS: VoiceOver (Cmd + F5)
   - Windows: Narrador (Win + Ctrl + Enter)
   ¿El contenido tiene sentido cuando se lee en orden?

4. HERRAMIENTAS:
   - Chrome DevTools → Lighthouse → Accessibility
   - Extensión WAVE (wave.webaim.org)
   - Extensión axe DevTools

5. CONTRASTE: Verifica con herramientas online
   - webaim.org/resources/contrastchecker/
```

---

## 10. Errores comunes

### Error 1: Variables CSS sin fallback

```css
/* MAL: Si --color-acento no está definida, no hay color */
.boton {
  background-color: var(--color-acento);
}

/* BIEN: Fallback como segundo argumento */
.boton {
  background-color: var(--color-acento, #e53e3e);
}
```

### Error 2: clamp() con unidades incompatibles

```css
/* MAL: Mezclar unidades de forma que no funcione */
h1 {
  font-size: clamp(32px, 5vw, 3.5rem);
  /* Funciona, pero mezclar px y rem es inconsistente si el
     usuario cambia el tamaño de fuente base del navegador */
}

/* BIEN: Usar rem como base, vw para la parte fluida */
h1 {
  font-size: clamp(2rem, 1.5rem + 2vw, 3.5rem);
  /* Todo respeta la configuración de fuente del usuario */
}
```

### Error 3: backdrop-filter sin prefijo para Safari

```css
/* MAL: No funciona en Safari */
.glass {
  backdrop-filter: blur(10px);
}

/* BIEN: Incluir prefijo webkit */
.glass {
  -webkit-backdrop-filter: blur(10px);
  backdrop-filter: blur(10px);
}
```

### Error 4: Pseudo-elementos sin `content`

```css
/* MAL: El pseudo-elemento NO se renderiza */
.titulo::after {
  display: block;
  width: 60px;
  height: 4px;
  background: red;
}

/* BIEN: content es OBLIGATORIO (aunque sea cadena vacía) */
.titulo::after {
  content: '';      /* Sin esto, nada se muestra */
  display: block;
  width: 60px;
  height: 4px;
  background: red;
}
```

### Error 5: Open Graph sin imagen con dimensiones correctas

```html
<!-- MAL: Imagen muy pequeña o con formato incorrecto -->
<meta property="og:image" content="logo-50x50.png">

<!-- BIEN: Imagen de al menos 1200x630px para buena vista previa -->
<meta property="og:image" content="https://midominio.com/og-image-1200x630.jpg">
```

### Error 6: Accesibilidad olvidada en elementos interactivos

```html
<!-- MAL: Botón con solo un icono, sin texto accesible -->
<button><svg>...</svg></button>

<!-- BIEN: Agregar aria-label -->
<button aria-label="Abrir menú de navegación"><svg>...</svg></button>

<!-- MAL: Enlace vacío -->
<a href="https://github.com/usuario"><i class="icon-github"></i></a>

<!-- BIEN: Texto accesible -->
<a href="https://github.com/usuario" aria-label="Perfil de GitHub">
  <i class="icon-github" aria-hidden="true"></i>
</a>
```

### Error 7: Skip link que no funciona

```html
<!-- MAL: El target no tiene tabindex y no recibe foco en algunos navegadores -->
<a href="#main">Saltar al contenido</a>
...
<main id="main">...</main>

<!-- BIEN: Agregar tabindex="-1" al target -->
<a href="#main">Saltar al contenido</a>
...
<main id="main" tabindex="-1">...</main>
```

### Error 8: Imágenes sin width y height causan CLS

```html
<!-- MAL: El navegador no sabe las dimensiones hasta que carga la imagen -->
<img src="proyecto.jpg" alt="Mi proyecto">

<!-- BIEN: El navegador reserva el espacio inmediatamente -->
<img src="proyecto.jpg" alt="Mi proyecto" width="800" height="600">
```

---

## 11. Ejercicios de práctica

### Ejercicio 1: Design System desde cero

Crea un sistema de variables CSS completo:

1. Define tokens primitivos: 5 colores, 3 fuentes, escala de espaciado (4px base).
2. Define tokens semánticos que referencien a los primitivos.
3. Implementa un tema oscuro usando `[data-theme="dark"]`.
4. Crea un botón JavaScript que alterne entre temas.
5. Verifica que el contraste cumple WCAG AA en ambos temas.

### Ejercicio 2: Tipografía fluida

1. Crea una escala tipográfica de 6 tamaños usando `clamp()`.
2. Aplícala a h1, h2, h3, h4, p, y small.
3. Compara visualmente el resultado en 375px, 768px y 1440px.
4. **Bonus:** Crea un espaciado fluido con `clamp()` para `padding` y `gap`.

### Ejercicio 3: Tarjeta con efecto glassmorphism

1. Crea un fondo con gradiente o imagen.
2. Coloca una tarjeta encima con `backdrop-filter: blur()`.
3. Agrega un borde semi-transparente y border-radius.
4. La tarjeta debe tener un overlay usando `::before`.
5. Al hacer hover, aumenta ligeramente el blur.
6. Verifica que funcione en Safari (prefijo webkit).

### Ejercicio 4: Landing page con IntersectionObserver

1. Crea una página con 5 secciones.
2. Cada sección tiene una animación de entrada diferente:
   - Sección 1: Fade in (opacity).
   - Sección 2: Slide desde la izquierda (translateX).
   - Sección 3: Slide desde la derecha (translateX negativo).
   - Sección 4: Scale up (scale 0.8 a 1).
   - Sección 5: Combinación (opacity + translateY).
3. Usa un solo IntersectionObserver para todas.
4. Implementa `unobserve` y `rootMargin` negativo.

### Ejercicio 5: Auditoría de accesibilidad

1. Toma la landing page del módulo.
2. Navega solo con teclado. Documenta cualquier problema.
3. Ejecuta Lighthouse en modo accesibilidad. Anota la puntuación.
4. Corrige todos los problemas encontrados:
   - Agregar skip link si no existe.
   - Verificar alt text en todas las imágenes.
   - Verificar contraste de colores.
   - Verificar que todos los interactivos son focusables.
   - Agregar aria-label donde sea necesario.
5. Vuelve a ejecutar Lighthouse y compara la puntuación.

### Ejercicio 6: Optimización de SEO

1. Agrega todas las meta tags necesarias a tu landing:
   - `<title>` con fórmula "Página | Marca".
   - `<meta name="description">` con máximo 155 caracteres.
   - Open Graph completo (title, description, image, url, type).
   - Twitter Card (card, title, description, image).
2. Agrega datos estructurados JSON-LD para una Persona.
3. Verifica con la herramienta de prueba de datos estructurados de Google.
4. Verifica la vista previa de Open Graph con opengraph.xyz.

### Ejercicio 7: Performance audit

1. Ejecuta Lighthouse en modo Performance.
2. Identifica las 3 métricas principales: LCP, FID/INP, CLS.
3. Implementa mejoras:
   - `loading="lazy"` en imágenes below the fold.
   - `width` y `height` en todas las `<img>`.
   - `preload` para fuentes y la imagen hero.
   - Verifica que las animaciones usen solo `transform` y `opacity`.
4. Vuelve a ejecutar Lighthouse y compara.

---

> **Felicidades:** Si completaste los 10 módulos de este curso, tienes una base
> sólida en desarrollo web frontend. Consulta la `GUIA_DEL_CURSO.md` en la raíz
> del repositorio para ver el mapa completo y los siguientes pasos recomendados.

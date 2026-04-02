# Guia del Curso: Desarrollo Web y Programación — DGTIC UNAM

> **Cursos:** Desarrollo de Páginas Web (HTML/CSS/JS), Introducción a la Programación (Python), Fundamentos de PHP
> **Institución:** Dirección General de Cómputo y de Tecnologías de Información y
> Comunicación (DGTIC), UNAM
> **Formato:** 13 módulos progresivos en 2 bloques: desarrollo web (01-10) y programación (11-13)

---

## Tabla de contenidos

1. [Sobre este curso](#1-sobre-este-curso)
2. [Mapa de aprendizaje](#2-mapa-de-aprendizaje)
3. [Tabla de conceptos por módulo](#3-tabla-de-conceptos-por-módulo)
4. [Glosario de términos](#4-glosario-de-términos)
5. [Recursos adicionales](#5-recursos-adicionales)
6. [Cómo seguir aprendiendo](#6-cómo-seguir-aprendiendo)

---

## 1. Sobre este curso

### Qué vas a aprender

Al completar este curso serás capaz de:

- Escribir HTML semántico y accesible desde cero.
- Diseñar y maquetar páginas web con CSS moderno (Flexbox, Grid, variables, transiciones).
- Crear sitios responsive que funcionen en cualquier dispositivo.
- Aplicar buenas prácticas de rendimiento, accesibilidad y SEO.
- Construir un portfolio profesional y una landing page como proyectos finales.
- Entender la interactividad básica con JavaScript (DOM, eventos, IntersectionObserver).
- Programar lógica básica con Python (condicionales, ciclos, funciones).
- Manejar JavaScript a nivel intermedio (POO, eventos, consumo de APIs).
- Desarrollar aplicaciones web server-side con PHP (sesiones, formularios, regex).

### Prerequisitos

**Ninguno.** Este curso empieza desde cero. Solo necesitas:

- Una computadora con un navegador moderno (Chrome, Firefox, Edge o Safari).
- Un editor de texto (recomendamos [Visual Studio Code](https://code.visualstudio.com/)).
- Ganas de aprender y experimentar.

### Cómo usar este repositorio

```
DGTIC-Cursos/
│
├── 01-fundamentos-html/        ← Empieza aquí
├── 02-fundamentos-css/
├── 03-pagina-web-basica/
├── 04-flexbox-dados/
├── 05-componentes-css/
├── 06-responsive-fundamentos/
├── 07-responsive-css-grid/
├── 08-proyecto-web-servicios/
├── 09-portfolio-profesional/
├── 10-landing-personal/
│
├── 11-python-programacion/     ← 15 ejercicios de Python
├── 12-javascript-fundamentos/  ← Scripts JS + proyecto final con API
├── 13-php-fundamentos/         ← Ejercicios PHP + proyecto con sesiones
│
├── index.html                  ← Página principal del repositorio
├── GUIA_DEL_CURSO.md           ← Este archivo (guía general)
└── README.md
```

**Para cada módulo:**

1. Lee el archivo `CONCEPTOS.md` del módulo (cuando exista) para entender la teoría.
2. Revisa los archivos HTML y CSS del ejercicio. Los comentarios en el código
   explican cada decisión.
3. Experimenta: modifica valores, rompe cosas, observa qué pasa.
4. Intenta los ejercicios de práctica de `CONCEPTOS.md` antes de pasar al siguiente módulo.

---

## 2. Mapa de aprendizaje

### Progresión del curso

```
                         MAPA DE APRENDIZAJE
  ═══════════════════════════════════════════════════════════

  FASE 1: FUNDAMENTOS
  ─────────────────────
  ┌───────────────────┐     ┌───────────────────┐
  │  01                │     │  02                │
  │  Fundamentos HTML  │────►│  Fundamentos CSS   │
  │                    │     │                    │
  │  Etiquetas, semán- │     │  Selectores, box   │
  │  tica, estructura  │     │  model, colores    │
  └───────────────────┘     └────────┬──────────┘
                                     │
                                     ▼
  FASE 2: CONSTRUCCIÓN         ┌───────────────────┐
  ─────────────────────        │  03                │
                               │  Página web básica │
                               │                    │
                               │  Multi-página,     │
                               │  navegación, links │
                               └────────┬──────────┘
                                        │
                                        ▼
                               ┌───────────────────┐
                               │  04                │
                               │  Flexbox (Dados)   │
                               │                    │
                               │  Ejes, alineación, │
                               │  distribución      │
                               └────────┬──────────┘
                                        │
                                        ▼
                               ┌───────────────────┐
                               │  05                │
                               │  Componentes CSS   │
                               │                    │
                               │  Cards, botones,   │
                               │  formularios       │
                               └────────┬──────────┘
                                        │
                                        ▼
  FASE 3: RESPONSIVE           ┌───────────────────┐
  ───────────────────          │  06                │
                               │  Responsive        │
                               │  Fundamentos       │
                               │                    │
                               │  Media queries,    │
                               │  mobile first      │
                               └────────┬──────────┘
                                        │
                                        ▼
                               ┌───────────────────┐
                               │  07                │
                               │  CSS Grid          │
                               │                    │
                               │  Grid template,    │
                               │  áreas, responsive │
                               └────────┬──────────┘
                                        │
                                        ▼
  FASE 4: INTEGRACIÓN          ┌───────────────────┐
  ────────────────────         │  08                │
                               │  Proyecto Web      │
                               │  de Servicios      │
                               │                    │
                               │  Sitio completo,   │
                               │  multi-sección     │
                               └────────┬──────────┘
                                        │
                                        ▼
  FASE 5: PROYECTOS            ┌───────────────────┐
  PROFESIONALES                │  09                │
  ─────────────────            │  Portfolio         │
                               │  Profesional       │
                               │                    │
                               │  Position, JS,     │
                               │  scroll animations │
                               └────────┬──────────┘
                                        │
                                        ▼
                               ┌───────────────────┐
                               │  10                │
                               │  Landing Page      │
                               │  Profesional       │
                               │                    │
                               │  Arquitectura CSS, │
                               │  clamp(), a11y,    │
                               │  SEO, performance  │
                               └────────┬──────────┘
                                        │
                                        ▼
  FASE 6: PROGRAMACIÓN        ┌───────────────────┐
  ────────────────────        │  11                │
                               │  Python            │
                               │                    │
                               │  Condicionales,    │
                               │  ciclos, funciones │
                               └────────┬──────────┘
                                        │
                                        ▼
                               ┌───────────────────┐
                               │  12                │
                               │  JavaScript        │
                               │                    │
                               │  POO, DOM,         │
                               │  eventos, APIs     │
                               └────────┬──────────┘
                                        │
                                        ▼
  FASE 7: BACKEND             ┌───────────────────┐
  ───────────────             │  13                │
                               │  PHP               │
                               │                    │
                               │  Sesiones, regex,  │
                               │  formularios       │
                               └───────────────────┘
```

### Vista compacta

```
01 HTML ──► 02 CSS ──► 03 Multi-page ──► 04 Flexbox ──► 05 Componentes
                                                              │
         ┌────────────────────────────────────────────────────┘
         ▼
06 Responsive ──► 07 CSS Grid ──► 08 Integración ──► 09 Portfolio ──► 10 Landing
                                                                          │
         ┌────────────────────────────────────────────────────────────────┘
         ▼
11 Python ──► 12 JavaScript ──► 13 PHP
```

### Qué construye cada módulo

```
Módulo  Qué construyes                         Habilidad principal
──────  ──────────────────────────────────────  ─────────────────────────
  01    Tu primer documento HTML                Estructura y semántica
  02    Página con estilos básicos              CSS: selectores, box model
  03    Sitio de varias páginas con navegación  Enlaces, rutas, estructura
  04    Dados con caras usando Flexbox          Alineación con Flexbox
  05    Componentes reutilizables (cards, etc.) Pensamiento modular
  06    Sitio adaptable a móvil                 Media queries, mobile first
  07    Layouts complejos con Grid              CSS Grid, áreas, responsive
  08    Sitio web de servicios completo         Integración de todo
  09    Portfolio profesional de una página     Position, JS, animaciones
  10    Landing page con efectos modernos       Arquitectura, a11y, SEO
  11    15 ejercicios de Python                Lógica de programación
  12    Scripts JS + proyecto con API          JavaScript, DOM, fetch
  13    Ejercicios PHP + app de usuarios       Backend, sesiones, regex
```

---

## 3. Tabla de conceptos por módulo

| Módulo | Conceptos principales | Archivos clave | Construye sobre |
|--------|----------------------|----------------|-----------------|
| **01** Fundamentos HTML | Etiquetas HTML, semántica, `<head>`, `<body>`, headings, párrafos, listas, enlaces, imágenes, estructura de documento | `index.html` | — |
| **02** Fundamentos CSS | Selectores (tipo, clase, ID), propiedades de texto, colores, box model (margin, padding, border), display, unidades | `index.html`, `style.css` | 01 |
| **03** Página web básica | Multi-página, navegación con `<nav>`, rutas relativas, `<a>` entre páginas, estructura de carpetas, `<footer>` | `index.html`, páginas internas | 01, 02 |
| **04** Flexbox (Dados) | `display: flex`, `flex-direction`, `justify-content`, `align-items`, `flex-wrap`, `gap`, `align-self` | `index.html`, `style.css` | 01, 02 |
| **05** Componentes CSS | Cards, botones, formularios, pseudo-clases (`:hover`, `:focus`), `border-radius`, `box-shadow`, transiciones básicas | Archivos de componentes | 01–04 |
| **06** Responsive | `<meta viewport>`, media queries, `min-width` vs `max-width`, mobile first, unidades relativas (`rem`, `em`, `%`, `vw`) | `style.css` con media queries | 01–05 |
| **07** CSS Grid | `display: grid`, `grid-template-columns`, `grid-template-rows`, `grid-template-areas`, `fr`, `repeat()`, `minmax()`, `auto-fit` | `style.css` con grid | 01–06 |
| **08** Proyecto Web | Integración de Flexbox + Grid, secciones hero, servicios, testimonios, footer complejo, Variables CSS (`--custom-property`) | Sitio completo | 01–07 |
| **09** Portfolio | `position` (relative, absolute, fixed, sticky), `z-index`, transiciones CSS, JavaScript DOM, `classList`, `addEventListener`, IntersectionObserver, scroll animations | `index.html`, `style.css`, `script.js` | 01–08 |
| **10** Landing Page | Arquitectura CSS (ITCSS), design systems, `clamp()`, `backdrop-filter`, `::before`/`::after`, performance (CLS, lazy loading, preload), SEO (meta tags, Open Graph), accesibilidad (ARIA, skip links, WCAG) | `index.html`, `style.css`, `script.js` | 01–09 |
| **11** Python | Variables, condicionales (`if`/`elif`/`else`), ciclos (`for`/`while`), funciones, `input()`, `try`/`except`, `random`, lógica de juegos | 15 carpetas con `.py` + `.md` | — |
| **12** JavaScript | Variables, ciclos, funciones (arrow, anonymous), clases, herencia, DOM (`getElementById`, `querySelector`), eventos (`onclick`, `DOMContentLoaded`), `fetch()` + API REST | `script00-02.js`, `Eventos1/`, `PracticaFinalNat/` | 09, 10 |
| **13** PHP | Variables, funciones, ciclos, `str_repeat()`, expresiones regulares (`preg_match`), sesiones (`$_SESSION`), formularios (`$_POST`), autenticación, `htmlspecialchars()` | `.php` files, `TareaFormulario_NEMB/` | 12 |

---

## 4. Glosario de términos

Los términos están ordenados alfabéticamente. La columna "Módulo" indica dónde
aparece por primera vez en el curso.

| Término | Definición | Módulo | Ejemplo |
|---------|-----------|--------|---------|
| **Accesibilidad (a11y)** | Prácticas para que el contenido web sea utilizable por todas las personas, incluyendo quienes usan tecnologías asistivas. | 05 | `alt="Foto del proyecto"` |
| **Ancestro posicionado** | El elemento más cercano en el árbol DOM que tiene `position` distinto de `static`. Es la referencia para `position: absolute`. | 09 | Un `div` con `position: relative` |
| **ARIA** | Accessible Rich Internet Applications. Atributos HTML que mejoran la accesibilidad cuando el HTML semántico no es suficiente. | 10 | `aria-label="Cerrar menú"` |
| **Backdrop-filter** | Propiedad CSS que aplica efectos gráficos (como desenfoque) al área detrás de un elemento. | 10 | `backdrop-filter: blur(10px)` |
| **Bloque (block)** | Elemento que ocupa todo el ancho disponible y empieza en una nueva línea. | 01 | `<div>`, `<p>`, `<section>` |
| **Box model** | Modelo que describe cómo se calcula el espacio de un elemento: content + padding + border + margin. | 02 | `box-sizing: border-box` |
| **Box-sizing** | Propiedad que define si width/height incluyen padding y border (`border-box`) o no (`content-box`). | 02 | `box-sizing: border-box` |
| **Breakpoint** | Punto de ancho de pantalla donde cambian los estilos CSS mediante media queries. | 06 | `@media (min-width: 768px)` |
| **Caché** | Almacenamiento temporal del navegador. Guarda archivos descargados para no volver a pedirlos. | 09 | El CSS externo se cachea entre páginas |
| **Cascade (cascada)** | Algoritmo que determina qué regla CSS "gana" cuando varias reglas afectan al mismo elemento. | 02 | Especificidad: ID > clase > tipo |
| **classList** | Propiedad de JavaScript que permite manipular las clases CSS de un elemento. | 09 | `elemento.classList.add('visible')` |
| **Clamp()** | Función CSS que define un valor fluido con mínimo, preferido y máximo. | 10 | `font-size: clamp(1rem, 3vw, 2rem)` |
| **CLS** | Cumulative Layout Shift. Métrica que mide cuánto se mueve el contenido visualmente mientras carga la página. | 10 | Agregar `width` y `height` a `<img>` |
| **Composición (composite)** | Paso del renderizado donde el navegador combina las capas pintadas. Es el paso más eficiente para animaciones. | 09 | Animar `transform` y `opacity` |
| **CSS Grid** | Sistema de layout bidimensional (filas y columnas) para crear diseños complejos. | 07 | `display: grid` |
| **CSS Variables** | Propiedades personalizadas que almacenan valores reutilizables. También llamadas Custom Properties. | 08 | `--color-primario: #1a365d` |
| **Design System** | Conjunto de decisiones de diseño codificadas (colores, tipografía, espaciado, componentes) para mantener consistencia. | 10 | Tokens de diseño en `:root` |
| **Design Tokens** | Valores primitivos de un design system: colores, tamaños, fuentes. | 10 | `--space-4: 1rem` |
| **Display** | Propiedad que define cómo se comporta un elemento en el flujo del documento. | 02 | `block`, `inline`, `flex`, `grid` |
| **DOM** | Document Object Model. Representación en objetos del documento HTML que JavaScript puede manipular. | 09 | `document.querySelector('.nav')` |
| **Em** | Unidad relativa al tamaño de fuente del elemento padre. | 02 | `padding: 1.5em` |
| **Especificidad** | Sistema de puntaje que determina qué regla CSS se aplica cuando hay conflictos. ID (100) > clase (10) > tipo (1). | 02 | `#nav .link` tiene especificidad 110 |
| **Flexbox** | Sistema de layout unidimensional (fila o columna) para distribuir y alinear elementos. | 04 | `display: flex` |
| **Flujo normal** | El comportamiento por defecto del navegador al posicionar elementos: bloques apilados verticalmente, inline horizontalmente. | 01 | Elementos `<p>` uno debajo de otro |
| **Focus** | Estado de un elemento cuando está seleccionado para interacción (teclado). | 05 | `:focus { outline: 2px solid blue; }` |
| **fr** | Unidad fraccional de CSS Grid. Representa una fracción del espacio disponible. | 07 | `grid-template-columns: 1fr 2fr 1fr` |
| **Gap** | Propiedad que define el espacio entre elementos en Flexbox o Grid. | 04 | `gap: 1rem` |
| **Glassmorphism** | Estilo de diseño que simula cristal translúcido usando `backdrop-filter: blur()`. | 10 | Tarjetas con fondo borroso |
| **Inline** | Elemento que no empieza en nueva línea y solo ocupa el ancho de su contenido. | 01 | `<span>`, `<a>`, `<strong>` |
| **IntersectionObserver** | API de JavaScript que detecta cuándo un elemento entra o sale del viewport de forma eficiente. | 09 | Animaciones de scroll reveal |
| **ITCSS** | Inverted Triangle CSS. Metodología de arquitectura CSS que organiza estilos de lo genérico a lo específico. | 10 | Settings → Generic → Elements → Components |
| **Layout (reflow)** | Paso del renderizado donde el navegador calcula posición y tamaño de cada elemento. Es costoso. | 09 | Cambiar `width` causa reflow |
| **Lazy loading** | Técnica que retrasa la carga de recursos (imágenes) hasta que estén cerca de ser visibles. | 10 | `<img loading="lazy">` |
| **Margin** | Espacio exterior de un elemento, entre su borde y los elementos vecinos. | 02 | `margin: 1rem auto` |
| **Media query** | Regla CSS que aplica estilos solo cuando se cumple una condición (ancho, orientación, etc.). | 06 | `@media (min-width: 768px) { }` |
| **Mobile first** | Estrategia de diseño que empieza con la versión móvil y agrega complejidad para pantallas más grandes. | 06 | Usar `min-width` en media queries |
| **Open Graph** | Protocolo de meta tags que controla cómo se ve una página al compartirla en redes sociales. | 10 | `<meta property="og:title">` |
| **Padding** | Espacio interior de un elemento, entre su contenido y su borde. | 02 | `padding: 1rem 2rem` |
| **Paint (repaint)** | Paso del renderizado donde el navegador rellena los píxeles de cada elemento. Costo medio. | 09 | Cambiar `color` causa repaint |
| **Position** | Propiedad CSS que define cómo se calcula la posición de un elemento. | 09 | `static`, `relative`, `absolute`, `fixed`, `sticky` |
| **Preload** | Directiva que indica al navegador que descargue un recurso crítico de forma anticipada. | 10 | `<link rel="preload" href="font.woff2">` |
| **Pseudo-clase** | Selector que aplica estilos según el estado del elemento. | 05 | `:hover`, `:focus`, `:nth-child()` |
| **Pseudo-elemento** | Permite estilizar una parte específica de un elemento o crear contenido virtual. | 10 | `::before`, `::after`, `::first-line` |
| **querySelector** | Método de JavaScript que devuelve el primer elemento que coincide con un selector CSS. | 09 | `document.querySelector('.nav')` |
| **Rem** | Unidad relativa al tamaño de fuente del elemento raíz (`<html>`). | 02 | `font-size: 1.5rem` (24px si base=16px) |
| **Responsive design** | Enfoque de diseño donde el sitio se adapta a diferentes tamaños de pantalla. | 06 | Media queries + unidades relativas |
| **Scroll-behavior** | Propiedad CSS que controla si el desplazamiento es instantáneo o suave. | 09 | `scroll-behavior: smooth` |
| **Selector** | Patrón que identifica a qué elementos HTML se aplican los estilos CSS. | 02 | `.clase`, `#id`, `elemento` |
| **Semántica** | Uso de etiquetas HTML que transmiten significado sobre el contenido, no solo apariencia. | 01 | `<article>` en vez de `<div>` |
| **SEO** | Search Engine Optimization. Prácticas para mejorar la visibilidad de una página en buscadores. | 10 | `<meta name="description">` |
| **Skip link** | Enlace oculto que permite a usuarios de teclado saltar la navegación y llegar al contenido principal. | 10 | `<a href="#main" class="skip-link">` |
| **Stacking context** | Contexto que determina el orden de apilamiento (z-index) de los elementos. | 09 | Un `position: relative` con `z-index` crea uno |
| **Sticky** | Valor de position que actúa como relative hasta un umbral de scroll, luego como fixed. | 09 | `position: sticky; top: 0` |
| **Transition** | Propiedad CSS que anima el cambio de un valor a otro de forma suave. | 05 | `transition: opacity 0.3s ease` |
| **Viewport** | El área visible del navegador donde se muestra el contenido. | 06 | `<meta name="viewport" ...>` |
| **Vw / Vh** | Unidades relativas al ancho (vw) y alto (vh) del viewport. 1vw = 1% del ancho. | 06 | `width: 100vw`, `height: 100vh` |
| **WCAG** | Web Content Accessibility Guidelines. Estándar internacional de accesibilidad web con niveles A, AA y AAA. | 10 | Contraste mínimo 4.5:1 para nivel AA |
| **Z-index** | Propiedad que controla el orden de apilamiento de elementos posicionados en el eje Z. | 09 | `z-index: 100` (solo con position) |

---

## 5. Recursos adicionales

### Documentación de referencia

| Recurso | URL | Para qué usarlo |
|---------|-----|-----------------|
| **MDN Web Docs — HTML** | developer.mozilla.org/es/docs/Web/HTML | Referencia completa de etiquetas HTML |
| **MDN Web Docs — CSS** | developer.mozilla.org/es/docs/Web/CSS | Referencia completa de propiedades CSS |
| **MDN Web Docs — JavaScript** | developer.mozilla.org/es/docs/Web/JavaScript | Referencia del lenguaje y APIs del DOM |
| **W3Schools** | w3schools.com | Tutoriales interactivos para principiantes |

### Guías especializadas

| Recurso | URL | Tema |
|---------|-----|------|
| **A Complete Guide to Flexbox** | css-tricks.com/snippets/css/a-guide-to-flexbox/ | Todo sobre Flexbox con diagramas |
| **A Complete Guide to CSS Grid** | css-tricks.com/snippets/css/complete-guide-grid/ | Todo sobre Grid con diagramas |
| **Learn CSS Layout** | learnlayout.com | Conceptos de layout paso a paso |
| **Flexbox Froggy** | flexboxfroggy.com | Juego para aprender Flexbox |
| **Grid Garden** | cssgridgarden.com | Juego para aprender CSS Grid |

### Compatibilidad de navegadores

| Recurso | URL | Para qué usarlo |
|---------|-----|-----------------|
| **Can I Use** | caniuse.com | Verificar soporte de propiedades CSS y APIs JS en navegadores |
| **Baseline** | web.dev/baseline | Estado de soporte de features web modernas |

### Herramientas de accesibilidad

| Recurso | URL | Para qué usarlo |
|---------|-----|-----------------|
| **WAVE** | wave.webaim.org | Evaluador de accesibilidad web online |
| **axe DevTools** | extensión de Chrome/Firefox | Auditoría de accesibilidad en DevTools |
| **WebAIM Contrast Checker** | webaim.org/resources/contrastchecker/ | Verificar contraste de colores (WCAG) |
| **Lighthouse** | integrado en Chrome DevTools | Auditoría de performance, a11y, SEO |

### Herramientas de desarrollo

| Herramienta | Para qué |
|-------------|----------|
| **Visual Studio Code** | Editor de código recomendado |
| **Extensión: Live Server** | Servidor local con recarga automática |
| **Extensión: Prettier** | Formato automático de código |
| **Extensión: HTMLHint** | Validación de HTML en tiempo real |
| **Chrome DevTools** | Inspeccionar elementos, debuggear CSS, performance |
| **Firefox DevTools** | Excelentes herramientas de Grid y Flexbox |

### Validadores

| Recurso | URL | Para qué |
|---------|-----|----------|
| **W3C HTML Validator** | validator.w3.org | Validar que el HTML sea correcto |
| **W3C CSS Validator** | jigsaw.w3.org/css-validator/ | Validar que el CSS sea correcto |
| **Google Rich Results Test** | search.google.com/test/rich-results | Probar datos estructurados |
| **OpenGraph Preview** | opengraph.xyz | Vista previa de Open Graph |

---

## 6. Cómo seguir aprendiendo

### Siguientes pasos después de este curso

```
                    TU RECORRIDO DE APRENDIZAJE
  ═══════════════════════════════════════════════════════

  ┌─────────────────────────────┐
  │  ESTE CURSO                 │
  │  HTML + CSS + JS básico     │     ← Estás aquí
  └──────────────┬──────────────┘
                 │
         ┌───────┴───────┐
         ▼               ▼
  ┌──────────────┐  ┌──────────────┐
  │ JavaScript   │  │ Profundizar  │
  │ a fondo      │  │ CSS          │
  │              │  │              │
  │ - Variables  │  │ - Animaciones│
  │ - Funciones  │  │   @keyframes │
  │ - Arrays     │  │ - Custom     │
  │ - Objetos    │  │   properties │
  │ - Async      │  │   avanzadas  │
  │ - Fetch API  │  │ - Container  │
  │ - Módulos    │  │   queries    │
  └──────┬───────┘  └──────┬───────┘
         │                 │
         └────────┬────────┘
                  ▼
         ┌──────────────────┐
         │  Frameworks       │
         │                   │
         │  ┌─────┐ ┌─────┐ │
         │  │React│ │ Vue │ │
         │  └─────┘ └─────┘ │
         │  ┌───────┐       │
         │  │Svelte │       │
         │  └───────┘       │
         └────────┬─────────┘
                  │
         ┌────────┴────────┐
         ▼                 ▼
  ┌──────────────┐  ┌──────────────┐
  │  Backend     │  │  Herramientas│
  │              │  │              │
  │  - Node.js   │  │  - Git       │
  │  - Python    │  │  - npm       │
  │  - Bases de  │  │  - Bundlers  │
  │    datos     │  │  - CI/CD     │
  │  - APIs REST │  │  - Testing   │
  └──────────────┘  └──────────────┘
```

### Ruta recomendada

```
SEMANAS 1–4:  JavaScript completo
              - Tipos de datos, funciones, scope
              - Manipulación del DOM avanzada
              - Fetch API y promesas
              - Módulos ES6

SEMANAS 5–8:  Herramientas de desarrollo
              - Git y GitHub (control de versiones)
              - npm (gestión de paquetes)
              - Vite o similar (bundler de desarrollo)

SEMANAS 9–12: Framework frontend (elige uno)
              - React (el más demandado laboralmente)
              - Vue (curva de aprendizaje más suave)
              - Svelte (el más innovador)

SEMANAS 13+:  Especialización
              - Backend (Node.js, Python, etc.)
              - UX/UI Design
              - DevOps
              - Mobile (React Native, Flutter)
```

### Ideas de proyectos para practicar

Después de completar este curso, estos proyectos reforzarán tus habilidades:

| Proyecto | Habilidades que practica | Dificultad |
|----------|------------------------|------------|
| **Blog personal** | HTML semántico, tipografía, multi-página, responsive | Baja |
| **Clon de landing** | Elige un sitio que te guste y replica su diseño | Media |
| **Calculadora** | HTML/CSS + JavaScript (eventos, lógica) | Media |
| **Galería de fotos** | CSS Grid, Flexbox, lazy loading, filtros CSS | Media |
| **Dashboard** | Grid complejo, gráficas (con librería), variables CSS | Alta |
| **Tienda online (maqueta)** | Componentes, responsive, formularios, accesibilidad | Alta |
| **App del clima** | Fetch API, JavaScript, diseño responsive, async/await | Alta |

### Comunidades y recursos en español

| Comunidad / Recurso | Descripción |
|---------------------|-------------|
| **MDN en español** | La documentación de Mozilla traducida al español |
| **FreeCodeCamp (español)** | Cursos gratuitos de desarrollo web con certificaciones |
| **Platzi** | Plataforma de cursos en español (de pago, con comunidad activa) |
| **Código Facilito** | Tutoriales y cursos de programación en español |
| **Dev.to (tag #spanish)** | Artículos técnicos de la comunidad en español |
| **Stack Overflow en español** | Preguntas y respuestas técnicas en español |
| **GitHub** | Busca proyectos open source para contribuir y aprender |
| **Discord / Telegram** | Busca comunidades de desarrollo web en español en tu país |

### Consejos finales

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│  1. PRACTICA TODOS LOS DÍAS                                         │
│     Aunque sean 30 minutos. La consistencia supera a la intensidad. │
│                                                                     │
│  2. CONSTRUYE PROYECTOS REALES                                      │
│     Los tutoriales enseñan, pero los proyectos consolidan.          │
│     Cuando te atores, busca la solución. Ese proceso es aprender.   │
│                                                                     │
│  3. LEE CÓDIGO DE OTROS                                             │
│     Inspecciona sitios web que admires con DevTools.                │
│     Lee código open source en GitHub.                               │
│                                                                     │
│  4. NO MEMORICES, COMPRENDE                                         │
│     No necesitas recordar cada propiedad CSS de memoria.            │
│     Necesitas entender los conceptos para saber qué buscar.        │
│                                                                     │
│  5. COMPARTE LO QUE APRENDES                                       │
│     Escribe un blog, haz un video, ayuda en foros.                  │
│     Enseñar es la mejor forma de aprender.                         │
│                                                                     │
│  6. NO TE COMPARES                                                  │
│     Cada persona tiene su ritmo. Lo importante es seguir avanzando. │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

> **Gracias por tomar este curso.** El desarrollo web es un campo que evoluciona
> constantemente, y lo que has aprendido aquí es una base sólida sobre la que puedes
> construir cualquier cosa. Sigue practicando, sigue construyendo, y sigue aprendiendo.

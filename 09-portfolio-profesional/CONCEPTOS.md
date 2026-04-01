# Módulo 09 — Portfolio Profesional: CSS Avanzado y JavaScript

> **Nivel:** Avanzado
> **Prerequisitos:** Módulos 01–08 (HTML, CSS, Flexbox, Grid, Responsive Design)
> **Objetivo:** Construir un portfolio profesional de una sola página con navegación fija,
> animaciones de scroll y JavaScript para interactividad.

---

## Tabla de contenidos

1. [CSS Embebido vs Externo](#1-css-embebido-vs-externo)
2. [Position: el modelo de posicionamiento](#2-position-el-modelo-de-posicionamiento)
3. [Transiciones CSS](#3-transiciones-css)
4. [JavaScript para interactividad](#4-javascript-para-interactividad)
5. [Animaciones basadas en scroll](#5-animaciones-basadas-en-scroll)
6. [Navegación fija (Fixed Navigation)](#6-navegación-fija-fixed-navigation)
7. [Patrones de diseño para portfolios](#7-patrones-de-diseño-para-portfolios)
8. [Errores comunes](#8-errores-comunes)
9. [Ejercicios de práctica](#9-ejercicios-de-práctica)

---

## 1. CSS Embebido vs Externo

### Las tres formas de incluir CSS

```
┌─────────────────────────────────────────────────────────────────┐
│                    FORMAS DE INCLUIR CSS                        │
├─────────────────┬──────────────────┬────────────────────────────┤
│    INLINE       │    EMBEBIDO      │    EXTERNO                 │
│  style="..."    │    <style>       │    <link rel="stylesheet"> │
│                 │    en <head>     │    archivo .css separado    │
├─────────────────┼──────────────────┼────────────────────────────┤
│  Especificidad  │  Una sola página │  Múltiples páginas         │
│  máxima         │  sin peticiones  │  con caché del navegador   │
│                 │  HTTP extra      │                            │
└─────────────────┴──────────────────┴────────────────────────────┘
```

### Cuándo usar CSS embebido (en `<style>`)

No siempre es mala práctica. Hay casos legítimos:

| Caso de uso                | Razón                                                   |
|----------------------------|---------------------------------------------------------|
| Aplicaciones de una página | No hay otras páginas que reutilicen los estilos         |
| Plantillas de email        | Los clientes de email ignoran archivos CSS externos     |
| CSS Crítico (Critical CSS) | El CSS "above the fold" se embebe para carga más rápida |
| Prototipos rápidos         | Menos archivos que gestionar durante experimentación    |

### La estrategia de CSS Crítico (Critical CSS)

```
CARGA TRADICIONAL:
──────────────────
  Navegador pide HTML ──► Navegador pide CSS ──► Renderiza página
                          (petición extra)        (usuario espera)

CARGA CON CRITICAL CSS:
───────────────────────
  Navegador pide HTML ──► CSS crítico YA ESTÁ en <style> ──► Renderiza
  (el CSS para lo que     inmediatamente lo visible
   se ve primero va
   embebido)

  Mientras tanto: el CSS completo se carga en segundo plano
                  con <link rel="preload">
```

**Ejemplo práctico:**

```html
<head>
  <!-- CSS crítico embebido: solo lo necesario para el "above the fold" -->
  <style>
    body { margin: 0; font-family: sans-serif; }
    .hero { height: 100vh; display: flex; align-items: center; }
    .nav  { position: fixed; top: 0; width: 100%; }
  </style>

  <!-- CSS completo cargado de forma asíncrona -->
  <link rel="preload" href="estilos.css" as="style"
        onload="this.onload=null;this.rel='stylesheet'">
</head>
```

### Comparación de rendimiento

```
                        EMBEBIDO            EXTERNO
                     ┌──────────────┐   ┌──────────────┐
Peticiones HTTP      │  1 (solo HTML)│   │  2 (HTML+CSS)│
                     └──────────────┘   └──────────────┘
Caché del navegador  │  NO se cachea │   │  SÍ se cachea│
                     └──────────────┘   └──────────────┘
Primera visita       │  ✓ Más rápido │   │  Más lento   │
                     └──────────────┘   └──────────────┘
Visitas siguientes   │  Más lento    │   │  ✓ Más rápido│
                     └──────────────┘   └──────────────┘
Mantenibilidad       │  Difícil      │   │  ✓ Fácil     │
                     └──────────────┘   └──────────────┘
```

> **Regla general:** Para un portfolio de una sola página, el CSS embebido es
> perfectamente válido. Para sitios con múltiples páginas, usa archivos externos.

---

## 2. Position: el modelo de posicionamiento

La propiedad `position` es una de las más importantes y más malentendidas de CSS.
Define **cómo se calcula la posición final** de un elemento.

### Resumen de valores

```
┌────────────────────────────────────────────────────────────────────────┐
│                        VALORES DE POSITION                            │
├──────────┬──────────┬───────────┬──────────────────────────────────────┤
│ Valor    │ En flujo │ Referencia│ Notas                               │
├──────────┼──────────┼───────────┼──────────────────────────────────────┤
│ static   │ SÍ       │ N/A       │ Valor por defecto. Ignora           │
│          │          │           │ top/right/bottom/left/z-index        │
├──────────┼──────────┼───────────┼──────────────────────────────────────┤
│ relative │ SÍ       │ Su propia │ Se desplaza visualmente PERO su     │
│          │          │ posición  │ espacio original se conserva         │
├──────────┼──────────┼───────────┼──────────────────────────────────────┤
│ absolute │ NO       │ Ancestro  │ Sale del flujo. Se posiciona        │
│          │          │ posicio-  │ respecto al ancestro más cercano    │
│          │          │ nado      │ con position != static              │
├──────────┼──────────┼───────────┼──────────────────────────────────────┤
│ fixed    │ NO       │ Viewport  │ Siempre visible al hacer scroll.    │
│          │          │           │ Ideal para navegaciones.            │
├──────────┼──────────┼───────────┼──────────────────────────────────────┤
│ sticky   │ SÍ*      │ Ancestro  │ Actúa como relative hasta un        │
│          │          │ de scroll │ umbral, luego como fixed.           │
└──────────┴──────────┴───────────┴──────────────────────────────────────┘
```

### `static` — El flujo normal

```
┌──────────────────────────────┐
│        Contenedor            │
│  ┌────────────────────────┐  │
│  │   Elemento A (static)  │  │   Los elementos se apilan
│  └────────────────────────┘  │   uno debajo del otro en
│  ┌────────────────────────┐  │   el orden del HTML.
│  │   Elemento B (static)  │  │
│  └────────────────────────┘  │   top, left, z-index
│  ┌────────────────────────┐  │   NO tienen efecto.
│  │   Elemento C (static)  │  │
│  └────────────────────────┘  │
└──────────────────────────────┘
```

### `relative` — Desplazamiento desde la posición normal

```
┌──────────────────────────────────────┐
│        Contenedor                    │
│  ┌────────────────────────┐          │
│  │   Elemento A (static)  │          │
│  └────────────────────────┘          │
│  ┌ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─┐          │
│  │ Posición original de B │ ← espacio reservado (no colapsa)
│  └ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─┘          │
│       ┌────────────────────────┐     │
│       │  B (relative)          │     │   position: relative;
│       │  top: 10px;            │     │   top: 10px;
│       │  left: 20px;           │     │   left: 20px;
│       └────────────────────────┘     │
│  ┌────────────────────────┐          │
│  │   Elemento C (static)  │ ← NO se mueve, respeta el espacio original de B
│  └────────────────────────┘          │
└──────────────────────────────────────┘
```

**Clave:** `relative` no saca al elemento del flujo. Los demás elementos actúan
como si B estuviera en su posición original.

### `absolute` — Fuera del flujo

```
┌──────────────────────────────────────┐
│  Contenedor (position: relative)     │  ← Este es el "ancestro posicionado"
│                                      │
│  ┌────────────────────────┐          │
│  │   Elemento A (static)  │          │
│  └────────────────────────┘          │
│  ┌────────────────────────┐          │
│  │   Elemento C (static)  │ ← C sube al lugar de B (B ya no ocupa espacio)
│  └────────────────────────┘          │
│                                      │
│             ┌──────────────┐         │
│             │ B (absolute) │         │   position: absolute;
│             │ top: 50px;   │         │   top: 50px;
│             │ right: 10px; │         │   right: 10px;
│             └──────────────┘         │
└──────────────────────────────────────┘
```

**La búsqueda del ancestro posicionado:**

```
¿El padre tiene position != static?
         │
    ┌────┴────┐
    SÍ       NO
    │         │
    │    ¿El abuelo tiene position != static?
    │              │
    │         ┌────┴────┐
    │         SÍ       NO
    │         │         │
    │         │    ... sigue subiendo ...
    │         │         │
    │         │    ¿Llegó al <html>?
    │         │         │
    │         │         SÍ → Se posiciona respecto al viewport
    │         │
    ▼         ▼
  Se posiciona respecto a ese ancestro
```

> **Truco clásico:** Para posicionar un hijo con `absolute`, el padre debe tener
> `position: relative` (aunque no se desplace). Esto crea un "contexto de posicionamiento".

### `fixed` — Relativo al viewport

```
┌─ Viewport (lo que ves en pantalla) ──────────────────┐
│ ┌──────────────────────────────────────────────────┐  │
│ │  NAV (position: fixed; top: 0)                   │  │ ← Siempre visible
│ └──────────────────────────────────────────────────┘  │
│                                                       │
│  Contenido de la página que se desplaza               │
│  al hacer scroll...                                   │
│                                                       │
│                                                       │
│                              ┌──────┐                 │
│                              │ BTN  │ ← Botón fijo    │
│                              │ ↑Top │    position: fixed;
│                              └──────┘    bottom: 20px;
│                                          right: 20px;  │
└───────────────────────────────────────────────────────┘
  │  El contenido se desplaza DETRÁS de los elementos
  │  fijos. Los elementos fijos NO se mueven.
  ▼
```

### `sticky` — El híbrido

```
ANTES de llegar al umbral (top: 0):
┌─ Viewport ──────────────────────┐
│                                  │
│  Contenido anterior...           │
│                                  │
│  ┌────────────────────────────┐  │
│  │  NAV (sticky, top: 0)     │  │ ← Se comporta como relative
│  └────────────────────────────┘  │    (fluye normalmente)
│                                  │
│  Contenido posterior...          │
│                                  │
└──────────────────────────────────┘

DESPUÉS de llegar al umbral (scroll hacia abajo):
┌─ Viewport ──────────────────────┐
│  ┌────────────────────────────┐  │
│  │  NAV (sticky, top: 0)     │  │ ← Se "pega" al top del viewport
│  └────────────────────────────┘  │    (se comporta como fixed)
│                                  │
│  Contenido posterior...          │
│                                  │
│                                  │
│                                  │
└──────────────────────────────────┘
```

**Requisito:** `sticky` necesita que el contenedor padre tenga suficiente altura
para que el scroll pueda activar el comportamiento. Si el padre no tiene overflow,
sticky no funcionará.

### El contexto de apilamiento (Stacking Context) y z-index

```
z-index SOLO funciona en elementos posicionados (relative, absolute, fixed, sticky).

┌──────────────────────────────────────────────────┐
│                                                   │
│   z-index: 3  ┌──────────┐                       │
│               │ Capa 3   │                        │
│          ┌────┤          │                        │
│          │    └──────────┘                        │
│   z-index: 2                                      │
│          │ Capa 2   │                             │
│     ┌────┤          │                             │
│     │    └──────────┘                             │
│   z-index: 1                                      │
│     │ Capa 1   │                                  │
│     └──────────┘                                  │
│                                                   │
│   z-index: auto (0)                               │
│   ┌──────────────────────────────────────┐        │
│   │  Flujo normal del documento          │        │
│   └──────────────────────────────────────┘        │
│                                                   │
│   z-index: -1                                     │
│   ┌──────────────────────────────────────┐        │
│   │  Detrás del flujo normal             │        │
│   └──────────────────────────────────────┘        │
└──────────────────────────────────────────────────┘

GOTCHA: Un z-index alto DENTRO de un contexto de apilamiento
        NUNCA supera a un contexto de apilamiento hermano con
        z-index mayor.

Ejemplo:
  .padre-A  { position: relative; z-index: 1; }
  .hijo-A   { position: absolute; z-index: 9999; }

  .padre-B  { position: relative; z-index: 2; }
  .hijo-B   { position: absolute; z-index: 1; }

  Resultado: .hijo-B aparece ENCIMA de .hijo-A
             porque .padre-B (z:2) > .padre-A (z:1)
```

---

## 3. Transiciones CSS

Las transiciones permiten animar el cambio de un valor CSS a otro de forma suave.

### Sintaxis

```css
/* Propiedades individuales */
transition-property: background-color;
transition-duration: 0.3s;
transition-timing-function: ease;
transition-delay: 0s;

/* Shorthand (atajo) */
transition: background-color 0.3s ease 0s;
/*          propiedad    duración  timing  delay  */

/* Múltiples transiciones */
transition: background-color 0.3s ease,
            transform 0.5s ease-out,
            opacity 0.3s linear;

/* Todas las propiedades animables */
transition: all 0.3s ease;  /* Cómodo pero menos eficiente */
```

### Funciones de temporización (timing functions)

```
ease (por defecto)          linear                    ease-in
Inicio lento, rápido,      Velocidad constante       Inicio lento,
final lento                                           final rápido

│        ___──────          │       ──────────        │           ────
│      ─╱                   │     ╱                   │         ╱
│    ─╱                     │    ╱                    │       ╱
│   ╱                       │   ╱                     │     ╱
│  ╱                        │  ╱                      │   ╱
│╱                          │ ╱                       │──╱
└──────────────             └──────────────           └──────────────


ease-out                    ease-in-out               cubic-bezier()
Inicio rápido,              Inicio lento,             Curva personalizada
final lento                 final lento

│    ────────               │        ___──            │      _──_
│   ╱                       │      ─╱                 │    ╱     ╲──
│  ╱                        │    ─╱                   │   ╱
│ ╱                         │   ╱                     │  ╱
│╱                          │  ╱                      │ ╱
│╱                          │╱                        │╱
└──────────────             └──────────────           └──────────────
                                                      cubic-bezier(0.68,
                                                       -0.55, 0.27, 1.55)
                                                      (efecto de rebote)
```

### Propiedades animables vs no animables

```
┌─────────────────────────────────────────────────────────────────┐
│              ¿SE PUEDE ANIMAR CON TRANSITION?                   │
├──────────────────────────────┬──────────────────────────────────┤
│    SÍ (animables)            │    NO (no animables)             │
├──────────────────────────────┼──────────────────────────────────┤
│ opacity                      │ display                          │
│ transform                    │ position                         │
│ color / background-color     │ float                            │
│ width / height               │ font-family                      │
│ margin / padding             │ content                          │
│ border-radius                │ grid-template-columns*           │
│ box-shadow                   │ overflow                         │
│ font-size                    │ visibility**                     │
│ top / left / right / bottom  │                                  │
│ gap                          │                                  │
│ filter                       │                                  │
│ clip-path                    │                                  │
└──────────────────────────────┴──────────────────────────────────┘
  * grid-template-columns ya es animable en navegadores modernos
  ** visibility tiene transición pero es binario (visible/hidden),
     no hay estados intermedios
```

### Costo de rendimiento de las animaciones

```
┌────────────────────────────────────────────────────────────────┐
│                  PIPELINE DE RENDERIZADO                       │
│                                                                │
│  Paso 1: LAYOUT (Reflow)              ← MÁS COSTOSO           │
│  ────────────────────────                                      │
│  Propiedades: width, height, margin, padding, top, left,      │
│               font-size, border-width                          │
│  Efecto: Recalcula geometría de TODOS los elementos afectados │
│                                                                │
│  Paso 2: PAINT (Repintado)            ← COSTOSO               │
│  ─────────────────────────                                     │
│  Propiedades: color, background-color, box-shadow,            │
│               border-color, outline, background-image         │
│  Efecto: Rellena los píxeles pero no cambia geometría         │
│                                                                │
│  Paso 3: COMPOSITE (Composición)      ← MÁS BARATO           │
│  ───────────────────────────────                               │
│  Propiedades: transform, opacity                               │
│  Efecto: Solo mueve/transforma capas ya pintadas              │
│          La GPU se encarga, el hilo principal queda libre      │
└────────────────────────────────────────────────────────────────┘

RECOMENDACIÓN: Siempre que puedas, anima solo transform y opacity.

En lugar de:                      Usa:
─────────────                     ────
left: 0 → left: 100px            transform: translateX(100px)
width: 100px → width: 200px      transform: scaleX(2)
margin-top: 0 → margin-top: 20px transform: translateY(20px)
```

### Ejemplo completo

```css
.boton {
  background-color: #2563eb;
  color: white;
  padding: 12px 24px;
  border: none;
  border-radius: 8px;
  cursor: pointer;

  /* Transición suave para hover */
  transition: background-color 0.3s ease,
              transform 0.2s ease;
}

.boton:hover {
  background-color: #1d4ed8;
  transform: translateY(-2px);  /* Se eleva ligeramente */
}

.boton:active {
  transform: translateY(0);     /* Vuelve al hacer clic */
}
```

---

## 4. JavaScript para interactividad

### El DOM (Document Object Model)

```
                       HTML                          DOM (en memoria)
                    ┌──────────┐                   ┌──────────────────┐
<html>              │ <html>   │                   │     document     │
  <head>            │   <head> │                   │        │         │
    <title>         │     ...  │    Navegador      │   ┌────┴────┐   │
  </head>           │   <body> │   ═══════════►    │ <head>   <body>  │
  <body>            │     <nav>│    Parsea HTML     │   │     ┌──┴──┐ │
    <nav>           │     <main│    y construye    │ <title> <nav> <main>
    <main>          │       ...│    el DOM         │          │     │ │
      <section>     │   </body>│                   │        <a>  <section>
    </main>         │ </html>  │                   │               │ │
  </body>           └──────────┘                   │             <h1> │
</html>                                            └──────────────────┘

El DOM es una REPRESENTACIÓN EN OBJETOS del HTML.
JavaScript puede leer y modificar esta representación.
Cuando JS cambia el DOM, el navegador actualiza lo que ves en pantalla.
```

### `querySelector` y `querySelectorAll`

```javascript
// querySelector: devuelve EL PRIMER elemento que coincida
const nav = document.querySelector('.nav-principal');
const hero = document.querySelector('#hero');
const primerLink = document.querySelector('nav a');

// querySelectorAll: devuelve TODOS los elementos (NodeList)
const secciones = document.querySelectorAll('section');
const links = document.querySelectorAll('.nav-link');

// Iterar sobre los resultados
secciones.forEach(seccion => {
  console.log(seccion.id);
});

// CUIDADO: querySelectorAll devuelve un NodeList, no un Array.
// Tiene forEach, pero NO tiene map, filter, reduce.
// Para usar métodos de Array:
const arrayDeSecciones = [...secciones];  // Spread operator
// o
const arrayDeSecciones2 = Array.from(secciones);
```

### `addEventListener`: eventos, callbacks y el objeto event

```javascript
// Sintaxis:
// elemento.addEventListener(tipoDeEvento, funcionCallback);

const boton = document.querySelector('.mi-boton');

boton.addEventListener('click', function(event) {
  // 'event' (o 'e') es el objeto con información del evento

  console.log(event.type);        // "click"
  console.log(event.target);      // El elemento que disparó el evento
  console.log(event.currentTarget); // El elemento al que se le asignó el listener
  console.log(event.clientX);     // Posición X del clic en el viewport
  console.log(event.clientY);     // Posición Y del clic en el viewport

  event.preventDefault();         // Evita el comportamiento por defecto
                                  // (útil en enlaces y formularios)
});
```

**Eventos comunes:**

| Evento       | Se dispara cuando...                                |
|-------------|-----------------------------------------------------|
| `click`     | El usuario hace clic en el elemento                 |
| `scroll`    | Se desplaza el contenido (en window o un contenedor)|
| `resize`    | Se cambia el tamaño de la ventana                   |
| `load`      | La página (o un recurso) termina de cargar          |
| `keydown`   | Se presiona una tecla                               |
| `keyup`     | Se suelta una tecla                                 |
| `submit`    | Se envía un formulario                              |
| `mouseenter`| El cursor entra en el elemento                      |
| `mouseleave`| El cursor sale del elemento                         |
| `focus`     | Un input recibe el foco                             |
| `blur`      | Un input pierde el foco                             |

### `classList`: manipulación de clases CSS

```javascript
const elemento = document.querySelector('.tarjeta');

// Agregar una clase
elemento.classList.add('visible');
// <div class="tarjeta visible">

// Remover una clase
elemento.classList.remove('visible');
// <div class="tarjeta">

// Toggle (alterna): si la tiene, la quita; si no la tiene, la agrega
elemento.classList.toggle('activo');

// Verificar si tiene una clase
if (elemento.classList.contains('activo')) {
  console.log('El elemento está activo');
}

// Reemplazar una clase por otra
elemento.classList.replace('viejo', 'nuevo');
```

**El patrón fundamental de interactividad:**

```
┌─────────────────────────────────────────────────────────┐
│  1. CSS define los ESTADOS (clases con estilos)         │
│                                                         │
│     .menu          { transform: translateX(-100%); }    │
│     .menu.abierto  { transform: translateX(0); }        │
│                                                         │
│  2. JS ALTERNA la clase según la interacción            │
│                                                         │
│     boton.addEventListener('click', () => {             │
│       menu.classList.toggle('abierto');                  │
│     });                                                 │
│                                                         │
│  3. CSS TRANSICIONES manejan la animación               │
│                                                         │
│     .menu { transition: transform 0.3s ease; }          │
└─────────────────────────────────────────────────────────┘
```

### `getBoundingClientRect()` — Posición y dimensiones de un elemento

```javascript
const seccion = document.querySelector('#proyectos');
const rect = seccion.getBoundingClientRect();
```

```
┌─ Viewport ──────────────────────────────────┐
│  ▲                                           │
│  │ rect.top (distancia del borde             │
│  │           superior del viewport           │
│  │           al borde superior del elemento) │
│  ▼                                           │
│  ┌─────────────────────────────────┐         │
│◄►│         #proyectos              │         │
│  │                                 │         │
│ rect.left                rect.right│         │
│  │         rect.width              │         │
│  │                                 │         │
│  │         rect.height             │         │
│  └─────────────────────────────────┘         │
│  ▲                                           │
│  │ rect.bottom                               │
│  ▼                                           │
└──────────────────────────────────────────────┘

NOTA: Los valores son RELATIVOS al viewport, NO al documento.
      Cambian al hacer scroll.
      top puede ser negativo (el elemento está arriba del viewport).
```

---

## 5. Animaciones basadas en scroll

### El patrón: CSS define estados, JS alterna la clase

```css
/* Estado INICIAL: oculto y desplazado hacia abajo */
.seccion {
  opacity: 0;
  transform: translateY(30px);
  transition: opacity 0.6s ease, transform 0.6s ease;
}

/* Estado FINAL: visible y en su posición */
.seccion.visible {
  opacity: 1;
  transform: translateY(0);
}
```

```javascript
// JS detecta cuándo el elemento entra en el viewport
// y agrega la clase 'visible'
```

### Por qué `opacity` + `transform`

```
┌────────────────────────────────────────────────────────┐
│  Esta combinación es la MÁS EFICIENTE porque:          │
│                                                        │
│  1. Ambas propiedades solo necesitan COMPOSICIÓN       │
│     (la GPU las maneja, no el hilo principal de JS)    │
│                                                        │
│  2. No causan reflow (no recalculan geometría)         │
│                                                        │
│  3. No causan repaint (no repintan píxeles)            │
│                                                        │
│  RESULTADO: animaciones de 60fps incluso en            │
│             dispositivos de gama baja                  │
└────────────────────────────────────────────────────────┘
```

### Scroll event vs IntersectionObserver

#### Método antiguo: `scroll` event

```javascript
// PROBLEMA: se ejecuta en CADA píxel de scroll (60+ veces por segundo)
window.addEventListener('scroll', function() {
  const secciones = document.querySelectorAll('.seccion');

  secciones.forEach(seccion => {
    const rect = seccion.getBoundingClientRect();
    const enViewport = rect.top < window.innerHeight && rect.bottom > 0;

    if (enViewport) {
      seccion.classList.add('visible');
    }
  });
});
```

```
Scroll Event:
═════════════
Scroll: ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
        │ │ │ │ │ │ │ │ │ │ │ │ │ │ │ │ │ │ │ │ │ │ │
        ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼
Callbacks ejecutados: 60+ por segundo SIEMPRE
(aunque nada interesante esté pasando)
```

#### Método moderno: `IntersectionObserver`

```javascript
// SOLUCIÓN: solo se ejecuta cuando un elemento ENTRA o SALE del viewport
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
      observer.unobserve(entry.target);  // Deja de observar (ya se mostró)
    }
  });
}, {
  threshold: 0.1  // Se activa cuando el 10% del elemento es visible
});

// Observar cada sección
document.querySelectorAll('.seccion').forEach(seccion => {
  observer.observe(seccion);
});
```

```
IntersectionObserver:
═════════════════════
Scroll: ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
                    │                       │
                    ▼                       ▼
Callbacks ejecutados: SOLO cuando cambia la intersección
(muchas menos ejecuciones, mucho más eficiente)
```

**Comparación detallada:**

```
┌──────────────────────┬──────────────────────────────────────┐
│    scroll event      │    IntersectionObserver               │
├──────────────────────┼──────────────────────────────────────┤
│ Imperativo           │ Declarativo                          │
│ (tú calculas todo)   │ (el navegador te avisa)              │
├──────────────────────┼──────────────────────────────────────┤
│ 60+ callbacks/seg    │ Solo cuando cambia la intersección   │
├──────────────────────┼──────────────────────────────────────┤
│ getBoundingClientRect│ Datos precalculados en el callback   │
│ fuerza un reflow     │ (sin reflow adicional)               │
├──────────────────────┼──────────────────────────────────────┤
│ Necesita throttle/   │ Ya está optimizado internamente      │
│ debounce manual      │                                      │
├──────────────────────┼──────────────────────────────────────┤
│ Funciona en IE       │ IE no lo soporta (pero existe        │
│                      │ polyfill)                            │
├──────────────────────┼──────────────────────────────────────┤
│ Más flexible         │ Más eficiente para casos comunes     │
└──────────────────────┴──────────────────────────────────────┘
```

### Smooth Scrolling

**Con CSS (la forma más simple):**

```css
/* Aplica a todo el documento */
html {
  scroll-behavior: smooth;
}
```

**Con JavaScript (más control):**

```javascript
// Scroll suave a un elemento
document.querySelector('#contacto').scrollIntoView({
  behavior: 'smooth',
  block: 'start'    // 'start', 'center', 'end', 'nearest'
});

// Scroll suave a una posición específica
window.scrollTo({
  top: 500,
  behavior: 'smooth'
});
```

```
scroll-behavior: smooth (CSS)     vs     scrollIntoView (JS)
─────────────────────────────            ──────────────────────
Aplica a TODOS los scrolls               Puedes controlar CUÁNDO
del documento automáticamente             se hace scroll (ej: al
                                          hacer clic en un botón)

No puedes controlar la                   Puedes especificar
velocidad ni el easing                   dónde queda el elemento
                                         (start, center, end)

Más simple                               Más flexible
```

---

## 6. Navegación fija (Fixed Navigation)

### El patrón de header fijo

```css
.nav {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  z-index: 1000;       /* Encima de todo lo demás */
  background: white;
}
```

### El problema del contenido oculto

```
SIN compensación:                CON compensación:
┌─────────────────────┐          ┌─────────────────────┐
│▓▓▓▓ NAV (fixed) ▓▓▓│          │▓▓▓▓ NAV (fixed) ▓▓▓│
│█████████████████████│          │                     │
│█ CONTENIDO OCULTO ██│          │  (padding-top: 70px)│
│█ detrás del nav    ██│          │                     │
│█████████████████████│          │  Contenido visible  │
│                     │          │  que empieza debajo  │
│  Contenido visible  │          │  del nav             │
└─────────────────────┘          └─────────────────────┘
```

**Solución clásica:**

```css
.nav {
  position: fixed;
  top: 0;
  height: 70px;
}

body {
  padding-top: 70px;  /* Igual a la altura del nav */
}
```

### El problema con anchor links

```
Al hacer clic en "Contacto" (#contacto), el navegador
salta a la sección, pero el nav la tapa:

┌──────────────────────────┐
│▓▓▓▓▓ NAV (fixed) ▓▓▓▓▓▓│
│█ Inicio del #contacto ██│ ← ¡TAPADO por el nav!
│█████████████████████████│
│                          │
│  Resto de la sección     │
│  contacto...             │
└──────────────────────────┘
```

**Solución moderna con CSS:**

```css
html {
  scroll-padding-top: 80px;  /* Deja espacio para el nav al hacer scroll a un ancla */
}
```

```
CON scroll-padding-top: 80px
┌──────────────────────────┐
│▓▓▓▓▓ NAV (fixed) ▓▓▓▓▓▓│
│                          │
│  (80px de espacio)       │
│                          │
│  Inicio del #contacto   │ ← ¡VISIBLE correctamente!
│                          │
│  Resto de la sección     │
└──────────────────────────┘
```

---

## 7. Patrones de diseño para portfolios

### Estructura de un portfolio de una sola página

```
┌──────────────────────────────────────────────────────────┐
│  NAV (fixed)                                              │
│  [Logo]    [Inicio] [Sobre mí] [Proyectos] [Contacto]   │
├──────────────────────────────────────────────────────────┤
│                                                          │
│              ┌─────────────────────┐                     │
│              │       HERO          │                     │
│              │  "Soy [Nombre]"     │   id="inicio"       │
│              │  Desarrollador Web  │                     │
│              │  [CTA: Ver trabajo] │                     │
│              └─────────────────────┘                     │
│                                                          │
├──────────────────────────────────────────────────────────┤
│                                                          │
│              SOBRE MÍ                  id="sobre-mi"     │
│              Foto + Biografía                            │
│              Habilidades                                 │
│                                                          │
├──────────────────────────────────────────────────────────┤
│                                                          │
│              PROYECTOS                 id="proyectos"    │
│              ┌──────┐ ┌──────┐ ┌──────┐                  │
│              │Proy 1│ │Proy 2│ │Proy 3│                  │
│              └──────┘ └──────┘ └──────┘                  │
│                                                          │
├──────────────────────────────────────────────────────────┤
│                                                          │
│              CONTACTO                  id="contacto"     │
│              Formulario o información                    │
│                                                          │
├──────────────────────────────────────────────────────────┤
│              FOOTER                                      │
│              Copyright + Redes sociales                  │
└──────────────────────────────────────────────────────────┘
```

### Navegación con anchor links

```html
<!-- En el nav -->
<nav>
  <a href="#inicio">Inicio</a>
  <a href="#sobre-mi">Sobre mí</a>
  <a href="#proyectos">Proyectos</a>
  <a href="#contacto">Contacto</a>
</nav>

<!-- Las secciones con sus IDs -->
<section id="inicio">...</section>
<section id="sobre-mi">...</section>
<section id="proyectos">...</section>
<section id="contacto">...</section>
```

### Tracking del enlace activo con JavaScript

```javascript
// Destaca el enlace de la sección actualmente visible

const secciones = document.querySelectorAll('section[id]');
const navLinks = document.querySelectorAll('.nav-link');

const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      // Quitar 'activo' de todos los links
      navLinks.forEach(link => link.classList.remove('activo'));

      // Agregar 'activo' al link correspondiente
      const id = entry.target.id;
      const linkActivo = document.querySelector(`.nav-link[href="#${id}"]`);
      if (linkActivo) {
        linkActivo.classList.add('activo');
      }
    }
  });
}, {
  threshold: 0.5  // El 50% de la sección debe ser visible
});

secciones.forEach(seccion => observer.observe(seccion));
```

---

## 8. Errores comunes

### Error 1: `z-index` no funciona

```css
/* MAL: z-index sin position */
.modal {
  z-index: 9999;  /* No tiene efecto porque position es static */
}

/* BIEN: z-index CON position */
.modal {
  position: fixed;  /* o relative, absolute, sticky */
  z-index: 9999;
}
```

### Error 2: Animar propiedades costosas

```css
/* MAL: Animar left causa reflow constante */
.animado {
  position: absolute;
  left: 0;
  transition: left 0.5s;
}
.animado:hover {
  left: 200px;
}

/* BIEN: Usar transform (solo composición) */
.animado {
  transition: transform 0.5s;
}
.animado:hover {
  transform: translateX(200px);
}
```

### Error 3: Contenido oculto detrás del nav fijo

```css
/* MAL: Olvidar el padding-top */
.nav { position: fixed; top: 0; height: 70px; }
/* El contenido empieza a 0px y queda detrás del nav */

/* BIEN: Compensar con padding */
.nav { position: fixed; top: 0; height: 70px; }
body { padding-top: 70px; }
html { scroll-padding-top: 80px; }  /* Para anchor links */
```

### Error 4: `transition: all` con efectos no deseados

```css
/* MAL: transition: all anima TODO, incluyendo cosas que no quieres */
.tarjeta {
  transition: all 0.3s;
}
/* Si cambias el layout (display, grid, etc.), también intentará
   transicionar esas propiedades, causando efectos extraños */

/* BIEN: Especificar exactamente qué propiedades animar */
.tarjeta {
  transition: background-color 0.3s ease,
              transform 0.3s ease,
              box-shadow 0.3s ease;
}
```

### Error 5: No usar `unobserve` en el IntersectionObserver

```javascript
// MAL: El observer sigue observando elementos ya animados
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
      // El observer sigue ejecutándose innecesariamente
    }
  });
});

// BIEN: Dejar de observar elementos que ya se animaron
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
      observer.unobserve(entry.target);  // Libera recursos
    }
  });
});
```

### Error 6: Evento `scroll` sin throttle

```javascript
// MAL: Se ejecuta 60+ veces por segundo
window.addEventListener('scroll', miFuncion);

// BIEN: Throttle limita la frecuencia de ejecución
function throttle(func, limit) {
  let enEspera = false;
  return function() {
    if (!enEspera) {
      func.apply(this, arguments);
      enEspera = true;
      setTimeout(() => enEspera = false, limit);
    }
  };
}

window.addEventListener('scroll', throttle(miFuncion, 100));
// Se ejecuta máximo 10 veces por segundo

// MEJOR: Usar IntersectionObserver en lugar de scroll event
```

### Error 7: `position: sticky` que no funciona

```css
/* MAL: El padre tiene overflow: hidden o auto */
.contenedor {
  overflow: hidden;  /* Esto ROMPE sticky en los hijos */
}
.hijo {
  position: sticky;
  top: 0;
}

/* BIEN: El padre no debe limitar el overflow */
.contenedor {
  /* Sin overflow: hidden/auto/scroll */
}
.hijo {
  position: sticky;
  top: 0;
}

/* TAMBIÉN MAL: El padre no tiene suficiente altura */
.contenedor {
  height: 100px;  /* Muy poco espacio para que sticky funcione */
}
```

---

## 9. Ejercicios de práctica

### Ejercicio 1: Sistema de posicionamiento

Crea un contenedor con tres elementos. Sin modificar el HTML, logra este resultado
usando solo CSS:

```
┌───────────────────────────────────────┐
│  Contenedor                           │
│                        ┌──────────┐   │
│                        │  Badge   │   │
│  ┌─────────────────┐   │  (rojo)  │   │
│  │   Tarjeta       │   └──────────┘   │
│  │                 │                   │
│  │                 │                   │
│  └─────────────────┘                   │
│                                        │
│                   ┌──────────────────┐ │
│                   │  Tooltip (abajo) │ │
│                   └──────────────────┘ │
└───────────────────────────────────────┘
```

- El badge debe estar posicionado en la esquina superior derecha de la tarjeta.
- El tooltip debe estar centrado horizontalmente respecto al contenedor.
- Usa `relative`, `absolute` y los offsets adecuados.

### Ejercicio 2: Menú con transiciones

Crea un menú de navegación donde:

1. Los enlaces cambian de color al pasar el mouse (transición de 0.3s).
2. Un subrayado aparece debajo del enlace activo usando `::after` con transición de ancho.
3. Al hacer hover, el subrayado se expande de `width: 0` a `width: 100%`.

```
Estado normal:     Estado hover:
┌─────────────┐    ┌─────────────┐
│  Inicio     │    │  Inicio     │
│  Proyectos  │    │  Proyectos  │
│  Contacto   │    │  Contacto   │
└─────────────┘    │  ══════════ │  ← Subrayado animado
                   └─────────────┘
```

### Ejercicio 3: Scroll reveal con IntersectionObserver

1. Crea 5 secciones con contenido.
2. Cada sección debe empezar invisible (`opacity: 0; transform: translateY(40px)`).
3. Usa `IntersectionObserver` para agregar la clase `visible` cuando la sección entre al viewport.
4. Cada sección debe tener un `transition-delay` diferente para que aparezcan en cascada.
5. Usa `unobserve` para que la animación solo ocurra una vez.

### Ejercicio 4: Navegación fija con tracking activo

1. Crea una página con un nav fijo y 4 secciones.
2. Al hacer scroll, el enlace correspondiente a la sección visible debe destacarse.
3. Al hacer clic en un enlace, el scroll debe ser suave.
4. Resuelve el problema del contenido oculto detrás del nav.
5. **Bonus:** Cambia el fondo del nav cuando el usuario haya scrolleado más de 100px.

### Ejercicio 5: Comparación de rendimiento

1. Crea dos versiones de una animación de desplazamiento:
   - Versión A: Anima `left` con `transition`.
   - Versión B: Anima `transform: translateX()` con `transition`.
2. Abre DevTools > Performance > Graba mientras haces hover en ambos.
3. Compara los fotogramas por segundo (FPS) y las capas de renderizado.
4. Documenta tus hallazgos.

---

> **Siguiente paso:** Con estos conceptos dominados, avanza al Módulo 10 donde
> aplicarás arquitectura CSS moderna, `clamp()`, `backdrop-filter` y estrategias
> avanzadas de rendimiento y accesibilidad.

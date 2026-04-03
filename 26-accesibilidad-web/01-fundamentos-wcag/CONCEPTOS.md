# Fundamentos de Accesibilidad y WCAG

## Indice

1. [HTML semantico vs div soup](#1-html-semantico-vs-div-soup)
2. [Landmarks — regiones de pagina](#2-landmarks--regiones-de-pagina)
3. [Jerarquia de encabezados](#3-jerarquia-de-encabezados)
4. [ARIA basico](#4-aria-basico)
5. [La primera regla de ARIA](#5-la-primera-regla-de-aria)
6. [Criterios WCAG clave de esta seccion](#6-criterios-wcag-clave-de-esta-seccion)

---

## 1. HTML semantico vs div soup

El HTML semantico comunica **significado** al navegador y a las tecnologias de asistencia. Usar `<div>` y `<span>` para todo ("div soup") destruye esa comunicacion.

```
  MAL — "div soup"                 BIEN — HTML semantico
  ====================             =======================

  <div class="header">             <header>
    <div class="nav">                <nav aria-label="Principal">
      <div class="link">Inicio       <a href="/">Inicio</a>
      </div>                         <a href="/blog">Blog</a>
    </div>                           </nav>
  </div>                           </header>
  <div class="content">            <main>
    <div class="title">Hola         <h1>Hola</h1>
    </div>                           <p>Bienvenido al sitio.</p>
    <div class="text">              <button>Enviar</button>
      Bienvenido al sitio.         </main>
    </div>
    <div class="btn"
      onclick="send()">
      Enviar
    </div>
  </div>

  Lector de pantalla ve:           Lector de pantalla ve:
  "texto, texto, texto"            "banner, navigation, link Inicio,
                                    link Blog, main, heading 1 Hola,
                                    paragraph, button Enviar"
```

### Problemas del div soup

- Los lectores de pantalla no pueden identificar regiones
- No hay navegacion por landmarks ni encabezados
- Los elementos `<div onclick>` no son focusables por teclado
- No se comunican roles, estados ni nombres accesibles

---

## 2. Landmarks — regiones de pagina

Los landmarks permiten a los usuarios de lectores de pantalla **saltar directamente** a regiones especificas de la pagina, como un indice automatico.

```
  Estructura de una pagina con landmarks
  =======================================

  ┌─────────────────────────────────────────┐
  │  <header>          role="banner"        │
  │  ┌───────────────────────────────────┐  │
  │  │ <nav>          role="navigation"  │  │
  │  └───────────────────────────────────┘  │
  └─────────────────────────────────────────┘
  ┌─────────────────────────────────────────┐
  │  <main>            role="main"          │
  │                                         │
  │  Contenido principal de la pagina       │
  │  (solo puede haber UN <main>)           │
  │                                         │
  └─────────────────────────────────────────┘
  ┌──────────────────┐ ┌────────────────────┐
  │ <aside>          │ │ <footer>           │
  │ role=            │ │ role=              │
  │ "complementary"  │ │ "contentinfo"      │
  └──────────────────┘ └────────────────────┘
```

### Mapeo HTML a landmarks

| Elemento HTML | Rol ARIA implicito | Uso |
|---------------|-------------------|-----|
| `<header>` (hijo de body) | `banner` | Logo, titulo del sitio |
| `<nav>` | `navigation` | Menus de navegacion |
| `<main>` | `main` | Contenido unico de la pagina |
| `<aside>` | `complementary` | Contenido lateral relacionado |
| `<footer>` (hijo de body) | `contentinfo` | Pie de pagina, copyright |
| `<form>` con `aria-label` | `form` | Formularios con nombre |
| `<section>` con `aria-label` | `region` | Seccion con nombre explicito |

---

## 3. Jerarquia de encabezados

Los encabezados (`<h1>` a `<h6>`) crean un **esquema del documento** que los lectores de pantalla usan para navegar. La jerarquia debe ser logica y sin saltos.

```
  CORRECTO                          INCORRECTO
  ========                          ==========

  h1  Titulo principal              h1  Titulo principal
    h2  Seccion A                     h3  Seccion A (salto de h1 a h3)
      h3  Subseccion A.1               h2  Subseccion A.1
      h3  Subseccion A.2             h4  Seccion B (salto, desorden)
    h2  Seccion B                     h2  Subseccion B.1
      h3  Subseccion B.1
```

### Reglas para encabezados

- Solo **un `<h1>`** por pagina (el titulo principal)
- No saltar niveles (de `<h2>` a `<h4>` sin `<h3>`)
- No usar encabezados solo por su tamano — usa CSS para eso
- Los encabezados deben ser descriptivos del contenido

---

## 4. ARIA basico

ARIA (Accessible Rich Internet Applications) agrega informacion semantica que HTML no puede expresar nativamente. Los tres pilares son:

### role — Que es el elemento

```html
<div role="button">Enviar</div>      <!-- Ahora el lector lo anuncia como boton -->
<div role="alert">Error grave</div>  <!-- Anuncia inmediatamente al lector -->
```

### aria-label — Como se llama

```html
<button aria-label="Cerrar dialogo">X</button>
<!-- Sin aria-label, el lector diria solo "X, boton" -->
<!-- Con aria-label, dice "Cerrar dialogo, boton" -->

<nav aria-label="Principal">...</nav>
<nav aria-label="Pie de pagina">...</nav>
<!-- Diferencia dos <nav> en la misma pagina -->
```

### aria-describedby — Informacion adicional

```html
<input type="password" id="pass" aria-describedby="pass-help">
<p id="pass-help">Minimo 8 caracteres, una mayuscula y un numero.</p>
<!-- El lector anuncia: "password, Minimo 8 caracteres..." -->
```

### aria-hidden — Ocultar del arbol de accesibilidad

```html
<span aria-hidden="true">★</span> Favorito
<!-- El icono decorativo se oculta, el lector solo dice "Favorito" -->
```

---

## 5. La primera regla de ARIA

> "No uses ARIA si puedes usar un elemento HTML nativo."

```
  EVITAR                              PREFERIR
  ======                              ========
  <div role="button" tabindex="0"     <button>Enviar</button>
    onclick="send()">Enviar</div>

  <div role="navigation">             <nav>
    <div role="list">                   <ul>
      <div role="listitem">               <li><a href="/">Inicio</a></li>
        <a href="/">Inicio</a>          </ul>
      </div>                           </nav>
    </div>
  </div>

  <span role="checkbox"               <input type="checkbox"
    aria-checked="false"                 id="acepto">
    tabindex="0">                      <label for="acepto">Acepto</label>
  </span>
```

El HTML nativo ya incluye:
- Rol semantico correcto
- Navegacion por teclado integrada
- Gestion de foco automatica
- Estados comunicados al arbol de accesibilidad

ARIA solo agrega atributos; no agrega **comportamiento**. Si usas `role="button"`, aun necesitas manejar Enter, Espacio, focus y estilos de foco manualmente.

---

## 6. Criterios WCAG clave de esta seccion

| Criterio | Nivel | Relacion |
|----------|-------|----------|
| 1.3.1 Informacion y relaciones | A | La estructura semantica se preserva programaticamente |
| 1.3.6 Identificar proposito | AAA | Landmarks identifican regiones de la pagina |
| 2.4.1 Evitar bloques | A | Mecanismo para saltar bloques repetitivos (skip link) |
| 2.4.6 Encabezados y etiquetas | AA | Encabezados describen el tema o proposito |
| 4.1.2 Nombre, rol, valor | A | Todo componente tiene nombre y rol accesibles |

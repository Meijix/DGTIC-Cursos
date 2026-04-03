# Cheatsheet — Accesibilidad Web (a11y)

## Elementos HTML semanticos

```
┌──────────────────────┬──────────────────────────────────────────────────┐
│ Elemento             │ Proposito                                        │
├──────────────────────┼──────────────────────────────────────────────────┤
│ <header>             │ Encabezado de pagina o seccion (role="banner")   │
│ <nav>                │ Navegacion principal (role="navigation")         │
│ <main>               │ Contenido principal — solo uno (role="main")     │
│ <footer>             │ Pie de pagina (role="contentinfo")               │
│ <aside>              │ Contenido complementario (role="complementary")  │
│ <section>            │ Seccion tematica con encabezado                  │
│ <article>            │ Contenido independiente y reutilizable           │
│ <figure>/<figcaption>│ Imagen con descripcion asociada                  │
│ <button>             │ Accion interactiva (no usar <div onclick>)       │
│ <a href>             │ Enlace de navegacion (no usar <span onclick>)    │
│ <label for="id">     │ Etiqueta asociada a un campo de formulario       │
│ <fieldset>/<legend>  │ Agrupacion de campos relacionados                │
└──────────────────────┴──────────────────────────────────────────────────┘
```

---

## Roles ARIA principales

```
Roles de landmark:    banner, navigation, main, complementary, contentinfo, search
Roles de widget:      button, checkbox, dialog, link, tab, tabpanel, menu, menuitem
Roles de estructura:  heading, list, listitem, table, row, cell, img
Roles de live region: alert, log, status, timer, marquee
```

---

## Estados y propiedades ARIA

```
aria-label="texto"          Nombre accesible cuando no hay texto visible
aria-labelledby="id"        Referencia a otro elemento como nombre
aria-describedby="id"       Descripcion adicional (ej: instrucciones de campo)
aria-hidden="true"          Ocultar del arbol de accesibilidad
aria-expanded="true|false"  Estado de un elemento colapsable
aria-selected="true|false"  Elemento seleccionado en una lista
aria-invalid="true"         Campo con error de validacion
aria-required="true"        Campo obligatorio
aria-live="polite|assertive" Anuncia cambios dinamicos al lector
aria-current="page"         Pagina actual en la navegacion
role="none" / role="presentation"  Elimina la semantica del elemento
```

---

## Navegacion por teclado

```
Tab           → Avanzar al siguiente elemento interactivo
Shift + Tab   → Retroceder al elemento interactivo anterior
Enter         → Activar enlace o boton
Espacio       → Activar boton, checkbox, seleccionar opcion
Escape        → Cerrar dialogo, menu, tooltip
Flechas       → Navegar dentro de widgets (tabs, menus, radios)
Home / End    → Ir al primer/ultimo elemento de una lista
```

---

## Contraste de color (WCAG 2.1)

```
┌───────────────────────────┬──────────────┬───────────────┐
│ Tipo de contenido         │ Nivel AA     │ Nivel AAA     │
├───────────────────────────┼──────────────┼───────────────┤
│ Texto normal (< 18px)     │ 4.5 : 1      │ 7 : 1         │
│ Texto grande (>= 18px     │ 3 : 1        │ 4.5 : 1       │
│   o >= 14px bold)         │              │               │
│ Componentes de UI         │ 3 : 1        │ —             │
│ Iconos informativos       │ 3 : 1        │ —             │
└───────────────────────────┴──────────────┴───────────────┘

Herramientas: WebAIM Contrast Checker, Chrome DevTools, Colour Contrast Analyser
```

---

## Focus management

```html
<!-- Skip link al inicio del body -->
<a href="#main-content" class="skip-link">Saltar al contenido</a>

<!-- tabindex valores -->
tabindex="0"    → Incluir en el orden natural de tabulacion
tabindex="-1"   → Focusable via JS pero no en el tab order
tabindex="1+"   → EVITAR — altera el orden natural (antipatron)

/* Estilos de foco visibles */
:focus-visible {
  outline: 3px solid #0077b6;
  outline-offset: 2px;
}
```

---

## Patrones ARIA comunes

```html
<!-- Boton toggle -->
<button aria-pressed="false">Modo oscuro</button>

<!-- Tabs -->
<div role="tablist">
  <button role="tab" aria-selected="true" aria-controls="panel1">Tab 1</button>
  <button role="tab" aria-selected="false" aria-controls="panel2">Tab 2</button>
</div>
<div role="tabpanel" id="panel1">Contenido 1</div>

<!-- Modal accesible -->
<div role="dialog" aria-modal="true" aria-labelledby="titulo-modal">
  <h2 id="titulo-modal">Confirmar accion</h2>
</div>

<!-- Alerta dinamica -->
<div role="alert">Se guardo correctamente.</div>

<!-- Navegacion con pagina actual -->
<nav aria-label="Principal">
  <a href="/" aria-current="page">Inicio</a>
  <a href="/blog">Blog</a>
</nav>
```

---

## Herramientas de testing

```
Automatizadas:          Manuales:                Lectores de pantalla:
- Lighthouse (Chrome)   - Navegacion con Tab     - NVDA (Windows, gratis)
- axe DevTools          - Zoom al 200%           - JAWS (Windows, pago)
- WAVE                  - Sin raton              - VoiceOver (macOS/iOS)
- pa11y (CLI)           - Sin color              - TalkBack (Android)
- eslint-plugin-jsx-a11y - Con lector pantalla   - Orca (Linux)
```

---

## Regla de oro

```
1. Usa HTML semantico PRIMERO
2. Agrega ARIA solo cuando HTML no es suficiente
3. Primera regla de ARIA: "No uses ARIA si puedes usar HTML nativo"
```

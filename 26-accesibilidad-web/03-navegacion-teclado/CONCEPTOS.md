# Navegacion por Teclado

## Indice

1. [Por que importa la navegacion por teclado](#1-por-que-importa-la-navegacion-por-teclado)
2. [Tab order y tabindex](#2-tab-order-y-tabindex)
3. [Skip links](#3-skip-links)
4. [Focus management](#4-focus-management)
5. [Focus visible](#5-focus-visible)
6. [Trampas de teclado (keyboard traps)](#6-trampas-de-teclado-keyboard-traps)
7. [Focus trap en modales](#7-focus-trap-en-modales)
8. [Roving tabindex para widgets](#8-roving-tabindex-para-widgets)

---

## 1. Por que importa la navegacion por teclado

Muchos usuarios no pueden usar un raton:
- Personas con discapacidad motora
- Usuarios de lectores de pantalla
- Usuarios avanzados que prefieren el teclado
- Usuarios con discapacidad temporal (tendinitis, brazo roto)

WCAG criterio **2.1.1 (Nivel A)**: toda funcionalidad debe ser operable con teclado.

### Teclas fundamentales

```
┌─────────────┬────────────────────────────────────────────┐
│ Tecla       │ Accion                                     │
├─────────────┼────────────────────────────────────────────┤
│ Tab         │ Avanzar al siguiente elemento interactivo  │
│ Shift + Tab │ Retroceder al anterior                     │
│ Enter       │ Activar enlace o boton                     │
│ Espacio     │ Activar boton, toggle checkbox             │
│ Escape      │ Cerrar dialogo, menu, tooltip              │
│ Flechas     │ Navegar dentro de widgets (tabs, menus)    │
│ Home / End  │ Ir al primer/ultimo elemento               │
└─────────────┴────────────────────────────────────────────┘
```

---

## 2. Tab order y tabindex

El **tab order** es el orden en que los elementos reciben foco al presionar Tab. Por defecto, sigue el orden del DOM.

### Valores de tabindex

```
tabindex="0"      → Incluir en el orden natural de tabulacion
                    Util para elementos no interactivos que necesitan foco
                    Ejemplo: <div role="button" tabindex="0">

tabindex="-1"     → Se puede enfocar via JavaScript (element.focus())
                    pero NO se incluye en el tab order natural
                    Util para: titulos que reciben foco despues de navegacion,
                    paneles de un tab widget

tabindex="1+"     → ANTIPATRON — Evitar siempre
                    Altera el orden natural creando confusion
                    Los elementos con tabindex positivo van PRIMERO,
                    antes que todo el contenido normal
```

### Diagrama de tab order

```
  DOM order:           Tab order natural:        Con tabindex="1" (MAL):
  ============         ====================      ========================

  [Logo]               1. Link Inicio            1. Boton Enviar (tabindex=1)
  [Link Inicio]        2. Link Blog              2. Link Inicio
  [Link Blog]          3. Input buscar           3. Link Blog
  [Input buscar]       4. Boton enviar           4. Input buscar
  [Contenido...]       5. Link contacto          5. Link contacto
  [Link contacto]
  [Boton enviar]       Predecible y logico       Confuso e inesperado
```

---

## 3. Skip links

Un **skip link** es un enlace oculto que aparece al inicio de la pagina al recibir foco con Tab. Permite saltar bloques repetitivos (como la navegacion) directamente al contenido principal.

### WCAG 2.4.1 (Nivel A)

"Se proporciona un mecanismo para evitar bloques de contenido que se repiten en multiples paginas."

### Implementacion

```html
<!-- Primer elemento del body -->
<a href="#contenido-principal" class="skip-link">
  Saltar al contenido principal
</a>

<!-- ... navegacion, header, etc ... -->

<main id="contenido-principal" tabindex="-1">
  <!-- tabindex="-1" permite que main reciba foco via el enlace -->
</main>
```

```css
.skip-link {
  position: absolute;
  top: -100%;           /* Oculto visualmente por defecto */
  left: 0;
  background: #0077b6;
  color: #fff;
  padding: 0.75rem 1.5rem;
  z-index: 100;
  font-weight: 600;
  text-decoration: none;
}

.skip-link:focus {
  top: 0;               /* Visible cuando recibe foco con Tab */
}
```

```
  Flujo del skip link:
  ====================

  1. Usuario presiona Tab al cargar la pagina
  2. Skip link aparece en la parte superior
     ┌─────────────────────────────────┐
     │ [Saltar al contenido principal] │  ← visible solo con :focus
     └─────────────────────────────────┘
  3. Si presiona Enter → foco salta a <main>
  4. Si presiona Tab otra vez → skip link desaparece, foco va al primer enlace
```

---

## 4. Focus management

Mover el foco programaticamente es necesario en interacciones dinamicas:

### Cuando mover el foco

| Situacion | Mover foco a |
|-----------|-------------|
| Abrir modal | Primer elemento interactivo del modal |
| Cerrar modal | Elemento que lo abrio |
| Eliminar elemento de lista | Elemento anterior o siguiente |
| Cambiar de pagina (SPA) | Titulo de la nueva pagina |
| Enviar formulario con errores | Primer campo con error |
| Expandir contenido | Inicio del contenido expandido |

### Ejemplo en JavaScript

```javascript
// Abrir modal: mover foco al primer elemento interactivo
function abrirModal() {
  modal.hidden = false;
  const primerFocusable = modal.querySelector('button, [href], input, select');
  primerFocusable.focus();
}

// Cerrar modal: regresar foco al disparador
function cerrarModal() {
  modal.hidden = true;
  botonQueAbrio.focus();  // restaurar contexto del usuario
}
```

---

## 5. Focus visible

El indicador de foco visible es esencial para que los usuarios de teclado sepan donde estan. **Nunca** elimines `outline` sin reemplazarlo.

```
  MAL:                              BIEN:
  ====                              =====

  *:focus { outline: none; }        :focus-visible {
                                      outline: 3px solid #0077b6;
                                      outline-offset: 2px;
                                    }

  El usuario de teclado no sabe     Foco claro y visible, solo cuando
  donde esta el foco.               se usa teclado (no con clic).
```

### :focus vs :focus-visible

- `:focus` — se activa con teclado Y con clic
- `:focus-visible` — se activa solo cuando el navegador determina que el foco debe ser visible (generalmente con teclado)

---

## 6. Trampas de teclado (keyboard traps)

Una **trampa de teclado** ocurre cuando el usuario no puede salir de un componente usando Tab o Escape. Esta prohibido por WCAG 2.1.2 (Nivel A).

```
  Trampa de teclado (MAL):
  ========================

  [Boton A] → Tab → [Widget] → Tab → [Widget] → Tab → [Widget]...
                         ↑___________________________________|
                     El foco nunca sale del widget

  Solucion:
  =========

  [Boton A] → Tab → [Widget] → Tab → [Boton B]
                                        Sale normalmente

  O con Escape:
  [Widget] → Escape → [Elemento que tenia foco antes]
```

### Excepcion: focus trap intencional en modales

Los modales **deben** atrapar el foco intencionalmente, pero con posibilidad de salir con Escape. Esto es un **focus trap**, no una keyboard trap.

---

## 7. Focus trap en modales

Un modal accesible debe:

1. Atrapar el foco dentro del modal (Tab no sale al contenido de atras)
2. Permitir cerrar con Escape
3. Restaurar foco al elemento que lo abrio

```
  Focus trap del modal:
  =====================

  ┌─────────────────────────────┐
  │  [Cerrar X]                 │ ← Tab llega aqui al final
  │                             │    y vuelve al inicio del modal
  │  <h2>Titulo del modal</h2> │
  │                             │
  │  [Input nombre]             │
  │  [Input correo]             │
  │  [Boton Cancelar]           │
  │  [Boton Aceptar]            │ ← Tab vuelve a [Cerrar X]
  │                             │
  └─────────────────────────────┘

  Escape → cierra el modal y regresa foco al boton que lo abrio
```

### Implementacion basica

```javascript
function trapFocus(modal) {
  const focusables = modal.querySelectorAll(
    'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])'
  );
  const primero = focusables[0];
  const ultimo = focusables[focusables.length - 1];

  modal.addEventListener('keydown', (e) => {
    if (e.key === 'Tab') {
      if (e.shiftKey && document.activeElement === primero) {
        e.preventDefault();
        ultimo.focus();     // Shift+Tab en el primero → ir al ultimo
      } else if (!e.shiftKey && document.activeElement === ultimo) {
        e.preventDefault();
        primero.focus();    // Tab en el ultimo → ir al primero
      }
    }
    if (e.key === 'Escape') {
      cerrarModal();
    }
  });
}
```

---

## 8. Roving tabindex para widgets

El patron **roving tabindex** se usa en widgets compuestos (tabs, menus, toolbars) donde un grupo de elementos actua como una sola parada de Tab.

```
  Tab order normal (ineficiente para tabs):
  ==========================================
  [Tab 1] → Tab → [Tab 2] → Tab → [Tab 3] → Tab → [Contenido]
  3 paradas de Tab para pasar los tabs

  Roving tabindex (correcto):
  ============================
  [Tab 1] → Tab → [Contenido]          Solo 1 parada de Tab
     ↕ flechas izq/derecha
  [Tab 2]
     ↕
  [Tab 3]
```

### Como funciona

```html
<!-- Solo el tab activo tiene tabindex="0" -->
<div role="tablist">
  <button role="tab" tabindex="0"  aria-selected="true">Tab 1</button>
  <button role="tab" tabindex="-1" aria-selected="false">Tab 2</button>
  <button role="tab" tabindex="-1" aria-selected="false">Tab 3</button>
</div>
```

- **Tab**: entra al widget (foco en tabindex="0") y sale
- **Flechas**: mueven el foco entre las opciones dentro del widget
- Al cambiar de seleccion: se mueve tabindex="0" al nuevo elemento activo

# Cheatsheet — Navegacion por Teclado

## En una frase

Toda funcionalidad debe ser operable con teclado, con un tab order logico, skip links para saltar bloques y foco siempre visible.

---

## Teclas esenciales

```
Tab           → Siguiente elemento interactivo
Shift + Tab   → Elemento interactivo anterior
Enter         → Activar enlace o boton
Espacio       → Activar boton, toggle checkbox
Escape        → Cerrar dialogo, menu, tooltip
Flechas       → Navegar dentro de widgets
Home / End    → Primer / ultimo elemento
```

---

## Tabindex

```
tabindex="0"      Incluir en tab order natural (para elementos no nativos)
tabindex="-1"     Focusable solo via JS (.focus()), fuera del tab order
tabindex="1+"     ANTIPATRON — nunca usar (rompe el orden natural)
```

---

## Skip link

```html
<!-- Primer elemento del <body> -->
<a href="#main" class="skip-link">Saltar al contenido</a>

<!-- Destino -->
<main id="main" tabindex="-1">...</main>
```

```css
.skip-link {
  position: absolute;
  top: -100%;
  left: 0;
  background: #0077b6;
  color: #fff;
  padding: 0.75rem 1.5rem;
  z-index: 100;
}
.skip-link:focus { top: 0; }
```

---

## Focus visible

```css
/* NUNCA hacer esto: */
*:focus { outline: none; }

/* HACER esto: */
:focus-visible {
  outline: 3px solid #0077b6;
  outline-offset: 2px;
}
```

`:focus-visible` → solo muestra outline con teclado, no con clic.

---

## Focus management — cuando mover el foco

```
Abrir modal         → Primer interactivo del modal
Cerrar modal        → Boton que lo abrio
Error formulario    → Primer campo con error
Eliminar item       → Item anterior o siguiente
Expandir contenido  → Inicio del contenido expandido
SPA cambio pagina   → Titulo de la nueva pagina
```

---

## Focus trap en modal

```javascript
// Obtener todos los focusables dentro del modal
const focusables = modal.querySelectorAll(
  'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])'
);
const primero = focusables[0];
const ultimo  = focusables[focusables.length - 1];

modal.addEventListener('keydown', (e) => {
  if (e.key === 'Tab') {
    if (e.shiftKey && document.activeElement === primero) {
      e.preventDefault(); ultimo.focus();
    } else if (!e.shiftKey && document.activeElement === ultimo) {
      e.preventDefault(); primero.focus();
    }
  }
  if (e.key === 'Escape') cerrarModal();
});
```

---

## Roving tabindex (tabs, menus, toolbars)

```html
<div role="tablist">
  <button role="tab" tabindex="0"  aria-selected="true">A</button>
  <button role="tab" tabindex="-1" aria-selected="false">B</button>
  <button role="tab" tabindex="-1" aria-selected="false">C</button>
</div>
```

- Tab entra/sale del widget (1 parada)
- Flechas navegan entre opciones
- Solo el activo tiene `tabindex="0"`

---

## Errores comunes

| Error | Solucion |
|-------|----------|
| `outline: none` sin reemplazo | Usar `:focus-visible` con outline visible |
| `tabindex="5"` en un boton | Usar `tabindex="0"` o nada |
| Modal sin focus trap | Atrapar Tab dentro del modal |
| Cerrar modal sin restaurar foco | Guardar y restaurar `document.activeElement` |
| Sin skip link | Agregar como primer elemento del body |
| Keyboard trap sin salida | Siempre permitir Escape |

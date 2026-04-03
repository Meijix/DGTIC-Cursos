# Cheatsheet — Testing y Auditoria

## En una frase

Las herramientas automatizadas detectan ~30% de los problemas; el testing manual con teclado y lector de pantalla encuentra el resto.

---

## Herramientas automatizadas

```
┌────────────────────┬──────────────────────────────────────────────┐
│ Herramienta        │ Uso                                          │
├────────────────────┼──────────────────────────────────────────────┤
│ Lighthouse         │ Chrome DevTools → Lighthouse → Accessibility │
│ axe DevTools       │ Extension de Chrome → pestaña axe DevTools   │
│ WAVE               │ Extension de Chrome → activar en pagina      │
│ pa11y              │ CLI: pa11y https://misitio.com               │
│ axe-core           │ npm: integrar en Playwright/Cypress          │
│ eslint-plugin-a11y │ Linting de JSX para React                    │
└────────────────────┴──────────────────────────────────────────────┘
```

---

## axe-core en CI

```javascript
// Playwright + axe-core
const results = await new AxeBuilder({ page })
  .withTags(['wcag2a', 'wcag2aa'])
  .analyze();
expect(results.violations).toEqual([]);
```

---

## Checklist manual rapido

```
Teclado:
  [ ] Tab recorre todo en orden logico
  [ ] Foco siempre visible
  [ ] Sin trampas de teclado
  [ ] Skip link funciona
  [ ] Modales atrapan foco + Escape cierra

Visual:
  [ ] Contraste de texto >= 4.5:1
  [ ] Zoom 200% sin scroll horizontal
  [ ] Info no depende solo del color

Estructura:
  [ ] Un solo <h1>, jerarquia sin saltos
  [ ] Landmarks: header, nav, main, footer
  [ ] lang="es" en <html>
  [ ] Titulo de pagina descriptivo

Formularios:
  [ ] Labels asociados a cada campo
  [ ] Errores descriptivos (no solo color)
  [ ] Foco al primer error al validar

Multimedia:
  [ ] Imagenes info con alt descriptivo
  [ ] Imagenes decorativas con alt=""
  [ ] Videos con subtitulos
```

---

## Lectores de pantalla — comandos clave

```
VoiceOver (macOS):
  Activar:        Cmd + F5
  Siguiente:      VO + →  (VO = Ctrl + Option)
  Rotor:          VO + U  (lista de encabezados, landmarks, links)
  Activar:        VO + Espacio

NVDA (Windows):
  Activar:        Ctrl + Alt + N
  Siguiente:      ↓
  Encabezados:    H
  Landmarks:      D
  Enlaces:        K
  Lista:          Insert + F7
```

---

## ARIA live regions

```html
<!-- Cambios no urgentes (resultados, guardado) -->
<div aria-live="polite">3 resultados encontrados.</div>
<div role="status">Guardado automaticamente.</div>

<!-- Cambios urgentes (errores, alertas) -->
<div aria-live="assertive">Error de conexion.</div>
<div role="alert">La contrasena es incorrecta.</div>
```

Regla: `polite` por defecto, `assertive` solo para errores criticos.

---

## Proceso de auditoria

```
1. Automatizado  → Lighthouse + axe + WAVE
2. Teclado       → Navegar sin raton (Tab, Enter, Escape)
3. Lector        → VoiceOver o NVDA
4. Visual        → Zoom 200%, simular daltonismo, verificar contraste
5. Documentar    → Clasificar: critico > serio > moderado > menor
```

---

## Clasificacion de problemas

```
CRITICO  → Bloquea el uso (sin teclado, sin labels, keyboard trap)
SERIO    → Dificulta mucho (bajo contraste, alt faltante, sin subtitulos)
MODERADO → Molesto (orden de Tab raro, sin landmarks)
MENOR    → Mejora posible (live region faltante)
```

---

## Errores mas frecuentes

| Error | Deteccion |
|-------|-----------|
| `<img>` sin alt | Automatica (Lighthouse/axe) |
| `<input>` sin label | Automatica (Lighthouse/axe) |
| Contraste insuficiente | Automatica + manual |
| Foco invisible | Manual (teclado) |
| Keyboard trap | Manual (teclado) |
| Contenido sin landmarks | Automatica + manual |
| Video sin subtitulos | Manual |
| Solo color para estados | Manual |

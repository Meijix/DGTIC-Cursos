# Testing y Auditoria de Accesibilidad

## Indice

1. [Testing automatizado vs manual](#1-testing-automatizado-vs-manual)
2. [Herramientas automatizadas](#2-herramientas-automatizadas)
3. [Checklist de testing manual](#3-checklist-de-testing-manual)
4. [Lectores de pantalla — uso basico](#4-lectores-de-pantalla--uso-basico)
5. [ARIA live regions](#5-aria-live-regions)
6. [Proceso de auditoria completa](#6-proceso-de-auditoria-completa)
7. [Errores comunes y como encontrarlos](#7-errores-comunes-y-como-encontrarlos)

---

## 1. Testing automatizado vs manual

Ninguna herramienta automatizada puede detectar todos los problemas de accesibilidad. Se necesitan ambos enfoques.

```
  Testing automatizado              Testing manual
  ====================              ==============

  Detecta ~30-40% de                Detecta el 60-70% restante
  los problemas WCAG

  Rapido y repetible                Lento pero profundo
  Integrable en CI/CD               Requiere conocimiento humano

  Bueno para:                       Bueno para:
  - Alt text faltante               - Alt text con SIGNIFICADO
  - Contraste insuficiente          - Orden logico de lectura
  - Labels faltantes                - Navegacion con sentido
  - Roles ARIA incorrectos          - Experiencia con teclado
  - Estructura HTML                 - Comprensibilidad del contenido
  - IDs duplicados                  - Focus management correcto

  NO puede verificar:               PUEDE verificar:
  - Si el alt es descriptivo        - Si la experiencia es buena
  - Si el tab order es logico       - Si el contenido tiene sentido
  - Si los errores son claros       - Si es usable con lector pantalla
  - Si el contenido es entendible   - Si el video tiene subtitulos utiles
```

### La regla del 30/70

```
  ┌──────────────────────────────────────────────────────────────┐
  │ Problemas de accesibilidad en un sitio tipico               │
  │                                                              │
  │ ███████████░░░░░░░░░░░░░░░░░░░░  30% automatizado           │
  │ ░░░░░░░░░░░████████████████████  70% solo detectable manual  │
  │                                                              │
  │ El testing automatizado es el INICIO, no el FIN              │
  └──────────────────────────────────────────────────────────────┘
```

---

## 2. Herramientas automatizadas

### Lighthouse (integrado en Chrome)

```
  Como usar:
  1. Chrome DevTools → pestaña "Lighthouse"
  2. Seleccionar "Accessibility"
  3. Ejecutar auditoria
  4. Revisar puntuacion y lista de problemas

  Ventajas:
  - Integrado en Chrome, sin instalar nada
  - Puntuacion de 0-100 facil de entender
  - Sugerencias con enlaces a documentacion
  - Disponible en CI con lighthouse-ci

  Limitaciones:
  - Solo detecta problemas detectables por DOM
  - No navega la pagina ni interactua
```

### axe DevTools (extension de navegador)

```
  Como usar:
  1. Instalar extension axe DevTools
  2. Chrome DevTools → pestaña "axe DevTools"
  3. Escanear la pagina completa o un componente
  4. Revisar problemas agrupados por severidad

  Ventajas:
  - Muy pocos falsos positivos
  - Motor axe-core usado por muchas herramientas
  - Agrupa por impacto: critico, serio, moderado, menor
  - Disponible como libreria npm para testing automatizado
```

### WAVE (extension de navegador)

```
  Como usar:
  1. Instalar extension WAVE
  2. Activar en cualquier pagina
  3. Muestra iconos en la pagina sobre los elementos con problemas

  Ventajas:
  - Visualizacion in-situ (los errores se muestran sobre la pagina)
  - Muestra la estructura de encabezados
  - Detecta problemas de contraste visualmente
  - Muestra el orden de tabulacion
```

### axe-core en testing automatizado

```javascript
// Con Playwright
const { test, expect } = require('@playwright/test');
const AxeBuilder = require('@axe-core/playwright').default;

test('pagina principal cumple a11y', async ({ page }) => {
  await page.goto('http://localhost:3000');

  const results = await new AxeBuilder({ page })
    .withTags(['wcag2a', 'wcag2aa'])  // Verificar WCAG 2.x AA
    .analyze();

  expect(results.violations).toEqual([]);
});
```

---

## 3. Checklist de testing manual

### Navegacion por teclado

```
  [ ] Tab recorre todos los elementos interactivos
  [ ] El orden de Tab es logico y sigue el flujo visual
  [ ] Shift+Tab funciona correctamente en reversa
  [ ] Enter activa enlaces y botones
  [ ] Espacio activa botones y toggles
  [ ] Escape cierra modales y menus
  [ ] No hay trampas de teclado
  [ ] El foco nunca se pierde o desaparece
  [ ] El foco es siempre visible
  [ ] Skip link funciona correctamente
```

### Contenido visual

```
  [ ] Todas las imagenes informativas tienen alt descriptivo
  [ ] Las imagenes decorativas tienen alt=""
  [ ] El contraste de texto cumple 4.5:1 (AA)
  [ ] La pagina es legible al hacer zoom al 200%
  [ ] La informacion no depende solo del color
  [ ] Los videos tienen subtitulos
  [ ] Los enlaces se distinguen del texto (no solo por color)
```

### Formularios

```
  [ ] Todos los campos tienen label asociado
  [ ] Los errores se describen con texto (no solo color)
  [ ] Los campos requeridos estan indicados
  [ ] El foco se mueve al primer error al validar
  [ ] Los grupos de radio/checkbox usan fieldset/legend
```

### Estructura

```
  [ ] Hay un solo <h1> por pagina
  [ ] Los encabezados siguen una jerarquia logica (sin saltos)
  [ ] Se usan landmarks (header, nav, main, footer)
  [ ] El idioma del documento esta declarado (lang="es")
  [ ] El titulo de la pagina es descriptivo
```

---

## 4. Lectores de pantalla — uso basico

### VoiceOver (macOS)

```
  Activar/Desactivar:  Cmd + F5
  Leer siguiente:      VO + Flecha derecha  (VO = Control + Option)
  Leer anterior:       VO + Flecha izquierda
  Activar elemento:    VO + Espacio
  Rotor (navegacion):  VO + U
    → Encabezados, landmarks, enlaces, formularios

  Tip: El Rotor muestra la lista de encabezados, enlaces y landmarks.
       Si tu pagina no tiene encabezados ni landmarks, el Rotor estara vacio.
```

### NVDA (Windows — gratuito)

```
  Activar:             Ctrl + Alt + N
  Detener lectura:     Ctrl
  Leer siguiente:      Flecha abajo
  Leer anterior:       Flecha arriba
  Siguiente encabezado: H
  Siguiente landmark:   D
  Siguiente enlace:     K
  Lista de elementos:   Insert + F7
```

### Que verificar con lector de pantalla

```
  1. El titulo de la pagina se anuncia al cargar
  2. Los landmarks son navegables
  3. Los encabezados forman un esquema logico
  4. Las imagenes se describen o se ignoran (decorativas)
  5. Los formularios anuncian labels y errores
  6. Los botones y enlaces describen su accion
  7. Los cambios dinamicos se anuncian (live regions)
  8. Los modales atrapan el foco correctamente
```

---

## 5. ARIA live regions

Las **live regions** anuncian cambios dinamicos en la pagina sin que el usuario necesite navegar al elemento que cambio.

### aria-live

```html
<!-- polite: espera a que el lector termine lo actual, luego anuncia -->
<div aria-live="polite" id="estado">
  Se guardaron los cambios.
</div>

<!-- assertive: interrumpe lo que el lector esta leyendo -->
<div aria-live="assertive" id="alerta">
  Error: no se pudo conectar al servidor.
</div>
```

### role="alert" (equivalente a aria-live="assertive")

```html
<!-- Se anuncia inmediatamente al lector de pantalla -->
<div role="alert">
  Error: la contrasena es incorrecta.
</div>
```

### role="status" (equivalente a aria-live="polite")

```html
<!-- Se anuncia cuando el lector no esta ocupado -->
<div role="status">
  3 resultados encontrados.
</div>
```

### Cuando usar cada uno

```
  aria-live="polite" / role="status"
  ===================================
  - Resultados de busqueda
  - Guardado automatico exitoso
  - Progreso de carga
  - Notificaciones no urgentes

  aria-live="assertive" / role="alert"
  ======================================
  - Errores de formulario
  - Sesion a punto de expirar
  - Errores de conexion
  - Contenido critico que necesita atencion inmediata
```

### Errores comunes con live regions

```
  MAL: Agregar aria-live al elemento Y cambiar el contenido al mismo tiempo
       (el lector puede no detectar el cambio)

  BIEN: El elemento con aria-live ya existe en el DOM.
        Solo se cambia el contenido de texto.

  MAL: Poner aria-live="assertive" en todo
       (interrumpe constantemente — frustrante)

  BIEN: Usar "polite" por defecto, "assertive" solo para errores criticos
```

---

## 6. Proceso de auditoria completa

```
  Paso 1: Testing automatizado
  =============================
  → Ejecutar Lighthouse, axe y WAVE
  → Documentar todos los problemas encontrados
  → Corregir los problemas criticos primero

  Paso 2: Testing manual — teclado
  ==================================
  → Desconectar el raton
  → Navegar toda la pagina solo con Tab, Enter, Escape
  → Verificar que el foco es visible siempre
  → Verificar modales y widgets interactivos

  Paso 3: Testing manual — lector de pantalla
  =============================================
  → Activar VoiceOver o NVDA
  → Navegar la pagina por landmarks y encabezados
  → Verificar formularios, imagenes, enlaces
  → Verificar cambios dinamicos (live regions)

  Paso 4: Verificacion visual
  =============================
  → Zoom al 200% — todo visible sin scroll horizontal?
  → Simular daltonismo (Chrome DevTools → Rendering)
  → Verificar contraste de todos los textos
  → Verificar que nada depende solo del color

  Paso 5: Documentar y priorizar
  ================================
  → Clasificar por impacto: critico > serio > moderado > menor
  → Critico = bloquea el uso (sin teclado, sin labels)
  → Serio = dificulta mucho (bajo contraste, alt faltante)
  → Moderado = molesto (orden de Tab raro)
  → Menor = mejora posible (live region faltante)
```

---

## 7. Errores comunes y como encontrarlos

| Error | Herramienta para detectarlo | Impacto |
|-------|----------------------------|---------|
| Imagenes sin alt | Lighthouse, axe, WAVE | Critico |
| Inputs sin label | Lighthouse, axe | Critico |
| Contraste insuficiente | Lighthouse, WAVE, DevTools | Serio |
| Falta skip link | Testing manual con teclado | Serio |
| Encabezados sin jerarquia | WAVE, testing manual | Moderado |
| Sin landmarks | WAVE, lector de pantalla | Moderado |
| Foco no visible | Testing manual con teclado | Critico |
| Keyboard trap | Testing manual con teclado | Critico |
| Videos sin subtitulos | Testing manual | Serio |
| Errores sin descripcion | Testing manual, lector | Serio |
| lang faltante en html | Lighthouse, axe | Moderado |
| IDs duplicados | axe, Lighthouse | Moderado |

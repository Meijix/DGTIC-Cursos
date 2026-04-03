# Cheatsheet — Color y Contraste

## En una frase

El texto necesita un ratio de contraste minimo de 4.5:1 (AA) y el color nunca debe ser el unico indicador de informacion.

---

## Ratios WCAG

```
┌───────────────────────────┬──────────────┬───────────────┐
│ Tipo                      │ Nivel AA     │ Nivel AAA     │
├───────────────────────────┼──────────────┼───────────────┤
│ Texto normal (< 18px)     │ 4.5 : 1      │ 7 : 1         │
│ Texto grande (>= 18px     │ 3 : 1        │ 4.5 : 1       │
│   o >= 14px bold)         │              │               │
│ Componentes de UI/iconos  │ 3 : 1        │ —             │
└───────────────────────────┴──────────────┴───────────────┘
```

---

## Regla rapida de minimos

```
Negro sobre blanco:    21:1   (maximo)
#767676 sobre blanco:  4.54:1 (minimo AA texto normal)
#949494 sobre blanco:  3.03:1 (minimo para texto grande)
Blanco sobre blanco:   1:1    (invisible)
```

---

## No depender solo del color

```
MAL:  Borde rojo = error, borde verde = correcto
BIEN: Borde rojo + icono ✗ + texto "Error: campo invalido"
      Borde verde + icono ✓ + texto "Correcto"

MAL:  Enlace diferenciado solo por color azul
BIEN: Enlace azul + subrayado

MAL:  Grafico con solo colores distintos
BIEN: Colores + patrones + etiquetas
```

---

## Daltonismo — combinaciones a evitar

```
Rojo + Verde         → Deuteranopia/Protanopia (8% hombres)
Verde + Marron       → Deuteranopia
Azul + Purpura       → Tritanopia
Verde + Gris         → Varios tipos
Rojo + Negro         → Protanopia severa
```

---

## Herramientas

```
Online:
  - WebAIM Contrast Checker    (webaim.org/resources/contrastchecker)
  - Coolors Contrast Checker   (coolors.co/contrast-checker)
  - Colour Contrast Analyser   (app de escritorio)

Navegador:
  - Chrome DevTools → Inspeccionar → ratio de contraste en colores CSS
  - Chrome → Rendering → "Emulate vision deficiencies"
  - Firefox → Inspector de accesibilidad
```

---

## Modo oscuro — errores comunes

```
1. #FFF sobre #000          → Fatiga visual. Usar #e8e8e8 sobre #1a1a2e
2. Gris insuficiente        → #999 sobre #333 = 3.79:1 FALLA AA
3. Mismo acento ambos modos → #0077B6 puede fallar sobre fondo oscuro
```

---

## Paleta accesible rapida

```
Modo claro (#FFFFFF):              Modo oscuro (#1a1a2e):
  Texto:    #1a1a1a (15.9:1)         Texto:    #e8e8e8 (13.5:1)
  Muted:    #555555 (7.46:1)         Muted:    #a0a0b8 (5.7:1)
  Link:     #0055AA (7.24:1)         Link:     #4da8da (5.91:1)
  Error:    #C7254E (5.64:1)         Error:    #ff6b6b (5.4:1)
  Exito:    #1B7A3D (5.11:1)         Exito:    #52b788 (5.8:1)
```

---

## CSS: respetar preferencias

```css
@media (prefers-color-scheme: dark) {
  :root { --bg: #1a1a2e; --text: #e8e8e8; }
}

@media (prefers-reduced-motion: reduce) {
  * { animation: none !important; transition: none !important; }
}

@media (prefers-contrast: more) {
  :root { --text: #000; --bg: #fff; }
}
```

---

## Errores comunes

| Error | Solucion |
|-------|----------|
| Texto gris claro sobre blanco | Verificar que supere 4.5:1 |
| Solo color para estados | Agregar texto, icono o patron |
| No verificar modo oscuro | Recalcular ratios para fondo oscuro |
| Placeholder gris demasiado claro | Minimo 4.5:1 (o mejor, no depender de placeholder) |
| Focus ring de bajo contraste | Outline de minimo 3:1 contra fondo |

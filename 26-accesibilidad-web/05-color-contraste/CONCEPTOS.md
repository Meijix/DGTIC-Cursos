# Color y Contraste

## Indice

1. [Ratios de contraste WCAG](#1-ratios-de-contraste-wcag)
2. [Como se calcula el contraste](#2-como-se-calcula-el-contraste)
3. [Tipos de daltonismo](#3-tipos-de-daltonismo)
4. [No depender solo del color](#4-no-depender-solo-del-color)
5. [Herramientas de verificacion](#5-herramientas-de-verificacion)
6. [Modo oscuro y accesibilidad](#6-modo-oscuro-y-accesibilidad)
7. [Colores accesibles en la practica](#7-colores-accesibles-en-la-practica)

---

## 1. Ratios de contraste WCAG

WCAG define ratios minimos de contraste entre el texto y su fondo para asegurar legibilidad. El ratio va de 1:1 (sin contraste) a 21:1 (maximo contraste, negro sobre blanco).

```
┌────────────────────────────┬──────────────────┬───────────────────┐
│ Tipo de contenido          │ Nivel AA         │ Nivel AAA         │
│                            │ (recomendado)    │ (optimo)          │
├────────────────────────────┼──────────────────┼───────────────────┤
│ Texto normal               │ 4.5 : 1          │ 7 : 1             │
│ (< 18px o < 14px bold)    │                  │                   │
├────────────────────────────┼──────────────────┼───────────────────┤
│ Texto grande               │ 3 : 1            │ 4.5 : 1           │
│ (>= 18px o >= 14px bold)  │                  │                   │
├────────────────────────────┼──────────────────┼───────────────────┤
│ Componentes de UI          │ 3 : 1            │ —                 │
│ (bordes, iconos, focus)    │                  │                   │
├────────────────────────────┼──────────────────┼───────────────────┤
│ Elementos graficos         │ 3 : 1            │ —                 │
│ (iconos informativos)      │                  │                   │
└────────────────────────────┴──────────────────┴───────────────────┘
```

### Ejemplos visuales de ratios

```
  21:1   #000000 sobre #FFFFFF  ← Maximo contraste (negro/blanco)
   7:1   #595959 sobre #FFFFFF  ← Cumple AAA para texto normal
  4.5:1  #767676 sobre #FFFFFF  ← Minimo AA para texto normal
   3:1   #949494 sobre #FFFFFF  ← Minimo para texto grande y UI
   2:1   #B0B0B0 sobre #FFFFFF  ← INSUFICIENTE para todo
   1:1   #FFFFFF sobre #FFFFFF  ← Sin contraste (invisible)
```

---

## 2. Como se calcula el contraste

El ratio se calcula a partir de la **luminancia relativa** de los dos colores:

```
  Ratio = (L1 + 0.05) / (L2 + 0.05)

  Donde L1 = luminancia del color mas claro
        L2 = luminancia del color mas oscuro

  La luminancia relativa es un valor de 0 (negro) a 1 (blanco)
  calculado a partir de los componentes R, G, B del color.
```

No necesitas calcularlo manualmente — las herramientas lo hacen automaticamente. Pero es util entender que:

- **Colores muy similares** → ratio cercano a 1:1 (malo)
- **Colores muy distintos en luminosidad** → ratio alto (bueno)
- El **tono** (hue) no importa tanto como la **luminosidad**

```
  Mismo tono, diferente contraste:
  ================================

  #0077B6 sobre #FFFFFF  →  4.56:1  ← Cumple AA (apenas)
  #005F8A sobre #FFFFFF  →  6.42:1  ← Cumple AA holgadamente
  #003D5C sobre #FFFFFF  →  9.87:1  ← Cumple AAA

  Diferente tono, mismo problema:
  ================================

  Rojo #FF0000 sobre verde #00FF00  →  Solo 1.28:1  ← FALLA
  (alto contraste de tono pero baja diferencia de luminosidad)
```

---

## 3. Tipos de daltonismo

El daltonismo afecta aproximadamente al 8% de los hombres y al 0.5% de las mujeres. Existen varios tipos:

```
  Tipo              Prevalencia    Afecta a             Vision
  ===============   ===========    ==================   ========================
  Deuteranopia      ~5% hombres    Conos verdes         Rojo y verde similares
  Protanopia        ~1% hombres    Conos rojos          Rojo oscuro, verde similar
  Tritanopia        ~0.01%         Conos azules         Azul y amarillo similares
  Acromatopsia      Muy rara       Todos los conos      Solo grises

  Vision normal:     ● Rojo   ● Verde   ● Azul    ● Amarillo
  Deuteranopia:      ● Marron ● Marron  ● Azul    ● Amarillo
  Protanopia:        ● Oscuro ● Marron  ● Azul    ● Amarillo
  Tritanopia:        ● Rojo   ● Verde   ● Gris    ● Rosa
```

### Combinaciones problematicas

```
  EVITAR estas combinaciones como unico diferenciador:
  ====================================================

  Rojo + Verde        → Indistinguible para deuteranopes y protanopes
  Verde + Marron      → Indistinguible para deuteranopes
  Azul + Purpura      → Dificil para tritanopes
  Verde + Gris        → Problematico para varios tipos
  Rojo + Negro        → Dificil en protanopia severa
```

---

## 4. No depender solo del color

WCAG 1.4.1 (Nivel A): "El color no se usa como unico medio visual para transmitir informacion."

### Ejemplo: estados de formulario

```
  MAL — Solo color:
  ==================

  Campo correcto:  [___________]  (borde verde)
  Campo con error: [___________]  (borde rojo)

  Un usuario daltonico no ve diferencia entre los bordes.

  BIEN — Color + icono + texto:
  ==============================

  Campo correcto:  [___________] ✓ Correcto
  Campo con error: [___________] ✗ Ingresa un correo valido

  Triple indicador: color + icono + mensaje de texto.
```

### Ejemplo: enlaces en texto

```
  MAL — Solo color:
  ==================

  "Visita nuestra pagina para mas informacion."
  (la palabra "pagina" es un enlace pero solo se diferencia por color azul)

  BIEN — Color + subrayado:
  ==========================

  "Visita nuestra pagina para mas informacion."
                    ------
  El subrayado es un indicador visual adicional al color.
```

### Ejemplo: graficos y datos

```
  MAL — Solo color en grafico de barras:
  ========================================

  ████  Ventas    ████  Gastos    ████  Beneficio
  (rojo)          (verde)         (azul)

  BIEN — Color + patron + etiqueta:
  ==================================

  ████  Ventas    ░░░░  Gastos    ////  Beneficio
  (rojo+solido)   (verde+puntos)  (azul+lineas)

  Cada barra tiene: color distinto + patron unico + etiqueta de texto.
```

---

## 5. Herramientas de verificacion

### Herramientas online

| Herramienta | URL | Uso |
|-------------|-----|-----|
| WebAIM Contrast Checker | webaim.org/resources/contrastchecker | Verificar ratio entre dos colores |
| Coolors Contrast Checker | coolors.co/contrast-checker | Interfaz visual atractiva |
| Colour Contrast Analyser | tpgi.com/color-contrast-checker | App de escritorio completa |

### Herramientas en navegador

```
  Chrome DevTools:
  ================
  1. Inspeccionar elemento
  2. En la seccion de color del CSS, aparece el ratio de contraste
  3. El circulo indica si cumple AA/AAA
  4. Pestaña "Rendering" → Emulate vision deficiencies
     → Simula deuteranopia, protanopia, tritanopia, etc.

  Firefox:
  ========
  1. Inspector de accesibilidad
  2. Herramientas de color con ratio integrado
  3. Simulacion de daltonismo en la barra de accesibilidad
```

### En CSS con prefers-color-scheme

```css
/* Respetar la preferencia del sistema operativo */
@media (prefers-color-scheme: dark) {
  :root {
    --bg: #1a1a2e;
    --text: #e8e8e8;      /* 13.5:1 sobre #1a1a2e — cumple AAA */
    --text-muted: #a0a0b8; /* 5.7:1  sobre #1a1a2e — cumple AA */
  }
}
```

---

## 6. Modo oscuro y accesibilidad

El modo oscuro presenta desafios unicos de contraste:

```
  Errores comunes en modo oscuro:
  ===============================

  1. Texto blanco puro (#FFF) sobre negro puro (#000)
     → Ratio 21:1 — tecnicamennte perfecto pero causa fatiga visual
     → Mejor usar: #e8e8e8 sobre #1a1a2e (suavizado)

  2. Texto gris claro sobre fondo gris oscuro
     → Verificar que el ratio no baje de 4.5:1
     → Ejemplo: #999 sobre #333 = 3.79:1 ← FALLA AA

  3. Colores de acento que cumplen en modo claro pero no en oscuro
     → Ejemplo: #0077B6 sobre #FFFFFF = 4.56:1 ← cumple AA
     → Pero:    #0077B6 sobre #1a1a2e = 3.45:1 ← FALLA AA
     → Solucion: ajustar el acento para modo oscuro (#4da8da)
```

### Buenas practicas

- No usar negro puro (#000) ni blanco puro (#FFF) — usar tonos suavizados
- Verificar TODOS los pares de color en ambos modos
- Los bordes y separadores deben mantener 3:1 de contraste
- Los iconos informativos tambien necesitan 3:1

---

## 7. Colores accesibles en la practica

### Paleta base que cumple AA en ambos modos

```
  Modo claro (fondo #FFFFFF):
  ===========================
  Texto principal:    #1a1a1a  (15.9:1) ← AAA
  Texto secundario:   #555555  (7.46:1) ← AAA
  Texto deshabilitado:#767676  (4.54:1) ← AA (minimo aceptable)
  Enlace:             #0055AA  (7.24:1) ← AAA
  Error:              #C7254E  (5.64:1) ← AA
  Exito:              #1B7A3D  (5.11:1) ← AA

  Modo oscuro (fondo #1a1a2e):
  ============================
  Texto principal:    #e8e8e8  (13.5:1) ← AAA
  Texto secundario:   #a0a0b8  (5.7:1)  ← AA
  Texto deshabilitado:#6b6b80  (3.1:1)  ← Solo texto grande
  Enlace:             #4da8da  (5.91:1) ← AA
  Error:              #ff6b6b  (5.4:1)  ← AA
  Exito:              #52b788  (5.8:1)  ← AA
```

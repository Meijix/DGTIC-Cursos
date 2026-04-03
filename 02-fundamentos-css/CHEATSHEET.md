# Cheatsheet — Fundamentos de CSS (Modulo 02)

## Selectores: referencia rapida

| Selector              | Sintaxis       | Ejemplo            | Especificidad |
|-----------------------|----------------|--------------------|---------------|
| Elemento              | `elem`         | `p`                | 0,0,0,1       |
| Clase                 | `.clase`       | `.menu`            | 0,0,1,0       |
| ID                    | `#id`          | `#header`          | 0,1,0,0       |
| Universal             | `*`            | `*`                | 0,0,0,0       |
| Descendiente          | `A B`          | `nav li`           | Suma          |
| Hijo directo          | `A > B`        | `ul > li`          | Suma          |
| Hermano adyacente     | `A + B`        | `h2 + p`           | Suma          |
| Pseudo-clase          | `:pseudo`      | `a:hover`          | 0,0,1,0       |
| Atributo              | `[attr]`       | `[type="email"]`   | 0,0,1,0       |
| Grupo                 | `A, B`         | `h1, h2, h3`       | Independiente |

### Pseudo-clases mas usadas

`:hover` `:focus` `:active` `:first-child` `:last-child` `:nth-child(n)` `:not()` `:root`

---

## Modelo de caja (Box Model)

```
+------------------ MARGIN -------------------+
|             (espacio exterior)               |
|  +------------- BORDER ---------------+     |
|  |           (linea visible)           |     |
|  |  +---------- PADDING ---------+    |     |
|  |  |      (espacio interior)     |    |     |
|  |  |  +------ CONTENT ------+   |    |     |
|  |  |  |   width x height    |   |    |     |
|  |  |  +---------------------+   |    |     |
|  |  +----------------------------+    |     |
|  +------------------------------------+     |
+----------------------------------------------+
```

### content-box vs border-box

```
content-box (default):   width: 300 + padding 40 + border 10 = 350px  (sorpresa!)
border-box (recomendado): width: 300px total, content se ajusta         (predecible)
```

Recomendacion universal:
```css
*, *::before, *::after { box-sizing: border-box; }
```

---

## Especificidad -- como se resuelven conflictos

```
Formato: (inline, IDs, clases, elementos)

  p                    0,0,0,1
  .card                0,0,1,0
  #main .card p        0,1,1,1
  style="..."          1,0,0,0

Un solo ID (0,1,0,0) siempre gana a 99 clases (0,0,99,0).
En empate: la ultima regla en el codigo gana.
```

---

## Variables CSS (Custom Properties)

```css
:root {
    --color-primario: #7ee8fd;    /* Global */
    --espaciado: 1rem;
}
.tarjeta {
    background: var(--color-primario);
    padding: var(--espaciado);
    color: var(--color-texto, black);  /* fallback: black */
}
```

Se pueden cambiar con JS y reaccionan a media queries (a diferencia de Sass).

---

## Unidades CSS

| Unidad | Relativa a                  | Mejor para                     |
|--------|-----------------------------|--------------------------------|
| `px`   | Nada (fija)                 | Bordes, sombras, detalles      |
| `rem`  | font-size de `<html>`       | Fuentes, padding, margin       |
| `em`   | font-size del PADRE         | Espaciado relativo al texto    |
| `%`    | Propiedad del padre         | Anchos fluidos                 |
| `vw`   | 1% del ancho del viewport   | Elementos full-width           |
| `vh`   | 1% del alto del viewport    | Secciones full-height          |
| `ch`   | Ancho del caracter "0"      | Ancho max de texto (60-80ch)   |
| `fr`   | Fraccion del espacio libre  | Columnas en CSS Grid           |

**Cuidado con `em`:** se compone al anidar (1.2em * 1.2em * 1.2em...). Usar `rem` para evitarlo.

---

## Colores

| Formato       | Ejemplo                     | Transparencia |
|---------------|-----------------------------|---------------|
| Hex           | `#001f3f`                   | `#001f3f80`   |
| RGB           | `rgb(0, 31, 63)`            | No            |
| RGBA          | `rgba(0, 31, 63, 0.5)`     | Si (0-1)      |
| HSL           | `hsl(210, 100%, 12%)`       | No            |
| HSLA          | `hsla(210, 100%, 12%, 0.5)` | Si (0-1)     |
| RGB moderno   | `rgb(0 31 63 / 50%)`        | Si            |

**HSL es el mas intuitivo:** H = color (0-360), S = viveza (0-100%), L = claridad (0-100%).

---

## Tipografia

```css
font-family: 'Arial', sans-serif;  /* siempre terminar con familia generica */
font-size: 1rem;                    /* usar rem para accesibilidad */
line-height: 1.5;                   /* 1.5-1.7 para cuerpo de texto */
```

| Familia       | Aspecto                | Ejemplo de fuentes         |
|---------------|------------------------|----------------------------|
| `sans-serif`  | Moderna, limpia        | Arial, Helvetica, Verdana  |
| `serif`       | Clasica, formal        | Times New Roman, Georgia   |
| `monospace`   | Ancho fijo por caracter| Courier New, Consolas      |
| `system-ui`   | Nativa del SO          | San Francisco, Segoe UI    |

---

## Herencia

| Se heredan (texto)   | NO se heredan (caja)  |
|----------------------|-----------------------|
| `color`              | `margin`, `padding`   |
| `font-family`        | `border`              |
| `font-size`          | `background`          |
| `line-height`        | `width`, `height`     |
| `text-align`         | `display`, `position` |

---

## Errores comunes

| Error                                 | Solucion                                       |
|---------------------------------------|-------------------------------------------------|
| `!important` para todo               | Arreglar la especificidad en vez de forzar       |
| `em` anidados que crecen sin control | Usar `rem` en lugar de `em`                      |
| Olvidar familia generica de respaldo | `font-family: 'Arial', sans-serif;`             |
| `font: tahoma;` (shorthand invalido) | Usar `font-family: tahoma;`                     |
| content-box: el ancho no es el real   | Usar `box-sizing: border-box;`                  |
| Margenes verticales que no se suman   | Colapso de margenes: gana el mayor, no se suman |

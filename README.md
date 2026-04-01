# DGTIC - Curso de HTML y CSS

Ejercicios y proyectos del curso de HTML y CSS impartido por la DGTIC (UNAM), complementados con proyectos propios para reforzar los conceptos aprendidos.

**Autora:** Natalia Edith Mejia Bautista

> **Punto de entrada:** abre [`index.html`](index.html) en tu navegador para ver la tabla de contenidos interactiva con enlaces a cada ejercicio.

---

## Contenido del curso

El repositorio esta organizado en modulos progresivos, desde los fundamentos hasta proyectos completos:

| # | Modulo | Temas principales | Archivo principal |
|---|--------|-------------------|-------------------|
| 01 | [Fundamentos HTML](01-fundamentos-html/) | Estructura semantica HTML5, formularios, listas de definicion | `index.html` |
| 02 | [Fundamentos CSS](02-fundamentos-css/) | Variables CSS, box model, colores, tipografia | `index.html` |
| 03 | [Pagina web basica](03-pagina-web-basica/) | Sitio multi-pagina, enlaces, imagenes, formularios | `index.html` |
| 04 | [Flexbox - Dados](04-flexbox-dados/) | Display flex, justify-content, align-items, flex-direction | `dados.html` |
| 05 | [Componentes CSS](05-componentes-css/) | Tarjetas con gradientes, box-shadow, diseno de componentes | `index.html` |
| 06 | [Responsive - Fundamentos](06-responsive-fundamentos/) | Media queries, mobile-first, anchos flexibles con Flexbox | `index.html` |
| 07 | [Responsive - CSS Grid](07-responsive-css-grid/) | CSS Grid, grid-template-columns, layouts multi-columna | `index.html` |
| 08 | [Proyecto: Sitio de servicios](08-proyecto-web-servicios/) | Proyecto integrador con gradientes, cards responsivas, multiples breakpoints | `index.html` |
| 09 | [Portfolio profesional](09-portfolio-profesional/) | Portfolio completo con animaciones scroll, navegacion suave, JavaScript | `portfolioYo.html` |
| 10 | [Landing personal](10-landing-personal/) | Landing page con hero, about, proyectos y contacto. Mobile-first, IntersectionObserver | `index.html` |

---

## Material de aprendizaje

Cada modulo incluye material educativo ademas del codigo:

- **Comentarios en el codigo:** cada archivo HTML y CSS contiene explicaciones detalladas sobre como, por que, y que alternativas se consideraron para cada decision.
- **`CONCEPTOS.md`:** cada carpeta contiene una guia en Markdown con teoria profunda, diagramas ASCII, tablas de referencia, errores comunes y ejercicios de practica.
- **[`GUIA_DEL_CURSO.md`](GUIA_DEL_CURSO.md):** guia general del curso con mapa de aprendizaje, glosario de terminos y recursos adicionales.

### Mapa de progresion

```
01 HTML ──► 02 CSS ──► 03 Multi-pagina
                            │
                            ▼
06 Responsive ◄── 05 Componentes ◄── 04 Flexbox
     │
     ▼
07 CSS Grid ──► 08 Integracion ──► 09 Portfolio ──► 10 Landing
```

---

## Tecnologias

- HTML5 (estructura semantica, formularios, accesibilidad)
- CSS3 (Flexbox, Grid, variables, media queries, gradientes, transiciones)
- JavaScript (IntersectionObserver, scroll animations, navegacion interactiva)

## Como usar

1. Abre [`index.html`](index.html) en tu navegador para ver la tabla de contenidos.
2. Cada carpeta es un modulo independiente — puedes abrir el archivo principal directamente.
3. Lee el `CONCEPTOS.md` de cada modulo para entender la teoria antes o despues de revisar el codigo.

```bash
# Abrir la tabla de contenidos
open index.html

# Abrir un modulo especifico
open 04-flexbox-dados/dados.html

# Leer la guia de un modulo
cat 04-flexbox-dados/CONCEPTOS.md
```

# Cheatsheet — Landing Page Profesional: Arquitectura CSS Moderna (Modulo 10)

## Arquitectura CSS (ITCSS)

```
Organizar el CSS de lo mas generico a lo mas especifico:

  SETTINGS -----> Variables, tokens de diseno (:root)
  GENERIC ------> Reset, box-sizing (*, *::before)
  ELEMENTS -----> Estilos base sin clases (h1, p, a, img)
  OBJECTS ------> Layout reutilizable (.container, .grid)
  COMPONENTS ---> Piezas de UI (.hero, .card, .nav)
  UTILITIES ----> Clases de ayuda (.sr-only, .text-center)

  Especificidad crece hacia abajo -->
```

## Design System con CSS Custom Properties

```css
:root {
  /* Tokens primitivos (Nivel 1: literal) */
  --navy-800: #1a365d;
  --red-500: #e53e3e;
  --gray-100: #f5f5f5;

  /* Tokens semanticos (Nivel 2: proposito) */
  --color-primary: var(--navy-800);
  --color-accent: var(--red-500);
  --color-bg: var(--gray-100);

  /* Espaciado (escala de 4px) */
  --space-2: 0.5rem;    /*  8px */
  --space-4: 1rem;      /* 16px */
  --space-8: 2rem;      /* 32px */
}
```

### Temas con variables (modo oscuro)

```css
:root              { --color-bg: #fff; --color-text: #1a202c; }
[data-theme="dark"]{ --color-bg: #1a202c; --color-text: #e2e8f0; }

/* Componentes usan variables, NUNCA colores directos */
body { background: var(--color-bg); color: var(--color-text); }
```

```javascript
// Toggle de tema
toggle.addEventListener('click', () => {
  const actual = document.documentElement.getAttribute('data-theme');
  document.documentElement.setAttribute('data-theme',
    actual === 'dark' ? 'light' : 'dark');
});
```

## Tipografia fluida con clamp()

```css
font-size: clamp(MINIMO, PREFERIDO, MAXIMO);
font-size: clamp(2rem,   5vw,       3.5rem);
```

```
  Con media queries:        Con clamp():
  3.5rem │       ┌─────     3.5rem │            ──────
         │   ┌───┘                 │          /
  2.0rem │───┘              2.0rem │─────────/
         └───────►ancho            └────────►ancho
         Saltos abruptos           Transicion suave
```

### Escala tipografica completa

```css
:root {
  --text-sm:   clamp(0.875rem, 0.8rem + 0.2vw, 1rem);
  --text-base: clamp(1rem, 0.9rem + 0.3vw, 1.125rem);
  --text-xl:   clamp(1.5rem, 1.2rem + 1vw, 2rem);
  --text-hero: clamp(3rem, 2rem + 4vw, 5rem);
}
```

`clamp()` tambien sirve para padding, gap, margin.

## Patron Hero con overlay

```css
.hero {
  position: relative;
  background: url('hero.jpg') center/cover;
}
.hero::before {
  content: '';
  position: absolute;
  inset: 0;  /* top:0 right:0 bottom:0 left:0 */
  background: linear-gradient(to bottom,
    rgba(0,0,0,0.6), rgba(0,0,0,0.3));
  z-index: 1;
}
.hero__contenido {
  position: relative;
  z-index: 2;  /* Encima del overlay */
}
```

```
Capas:  z:2 TEXTO ──> z:1 ::before (overlay) ──> IMAGEN FONDO
```

## Efectos CSS modernos

```css
/* Glassmorphism */
.glass {
  background: rgba(255,255,255,0.15);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border: 1px solid rgba(255,255,255,0.2);
}

/* Pseudo-elemento decorativo */
.titulo::after {
  content: '';  /* OBLIGATORIO */
  display: block;
  width: 60px; height: 4px;
  background: var(--color-accent);
}

/* Filtros de imagen */
filter: grayscale(100%);       /* Escala de grises */
filter: blur(5px);             /* Desenfoque */
filter: brightness(1.2);       /* Brillo */
filter: drop-shadow(2px 4px 6px rgba(0,0,0,0.3));
```

## IntersectionObserver (completo)

```javascript
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
      observer.unobserve(entry.target);
    }
  });
}, {
  root: null,            // null = viewport
  rootMargin: '0px',     // Expandir/reducir zona de deteccion
  threshold: 0.1         // 0-1: porcentaje visible para activar
});

document.querySelectorAll('.seccion').forEach(s => observer.observe(s));
```

### rootMargin

```
'0px'          = zona = viewport
'-100px 0px'   = zona reducida (activa mas tarde)
'200px 0px'    = zona expandida (activa ANTES de ser visible)
```

## Performance web

```
Pipeline de renderizado:
  DOM -> CSSOM -> Render Tree -> Layout -> Paint -> Composite

  Cambiar WIDTH     -> Layout + Paint + Composite  (LENTO)
  Cambiar COLOR     -> Paint + Composite           (MEDIO)
  Cambiar TRANSFORM -> Solo Composite              (RAPIDO)
```

```html
<!-- Lazy loading: no carga hasta estar cerca del viewport -->
<img src="foto.jpg" loading="lazy" width="800" height="600" alt="...">

<!-- SIEMPRE incluir width y height para evitar layout shift (CLS) -->

<!-- Precargar recursos criticos -->
<link rel="preload" href="fuente.woff2" as="font" crossorigin>
```

## Nomenclatura CSS

| Convencion   | Ejemplo                          | Ideal para         |
|-------------|----------------------------------|---------------------|
| BEM          | `.card__title--highlighted`      | Proyectos grandes   |
| Utility-first| `.flex .items-center .gap-4`    | Tailwind-style      |
| Semantico    | `.hero`, `.nav`, `.contacto`     | Proyectos medianos  |

## Referencia rapida

| Patron                     | Implementacion                           |
|----------------------------|------------------------------------------|
| Hero con overlay           | `::before` + `z-index`                   |
| Tipografia responsiva      | `clamp(min, preferido, max)`             |
| Temas claro/oscuro         | CSS variables + `[data-theme]`           |
| Animacion al scroll        | IntersectionObserver + CSS transitions   |
| Lazy loading imagenes      | `loading="lazy"` en `<img>`              |
| Evitar layout shift        | Siempre incluir `width` y `height`       |
| Seguridad en enlaces ext.  | `rel="noopener noreferrer"` en `<a>`     |

## Errores comunes

| Error                                  | Solucion                             |
|----------------------------------------|--------------------------------------|
| `::before` no aparece                  | Falta `content: ''` (obligatorio)    |
| Colores directos en componentes        | Usar CSS custom properties           |
| `backdrop-filter` no funciona Safari   | Agregar `-webkit-backdrop-filter`    |
| Tipografia con saltos en breakpoints   | Usar `clamp()` en vez de media queries|
| Imagenes sin `width`/`height`          | Provoca layout shift (CLS)          |
| Lazy loading en imagen hero            | Usar `loading="eager"` (o nada)      |
| Variables CSS en selectores incorrectos| `:root` para globales, scoped para temas |
| `z-index` sin `position`              | Agregar `position: relative`         |

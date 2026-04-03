# Cheatsheet — Modulo 06: Diseno Responsive

## Los 3 pilares del Responsive Web Design

```
  +------------------+  +------------------+  +------------------+
  |  CUADRICULAS     |  |  IMAGENES        |  |  MEDIA           |
  |  FLUIDAS         |  |  FLEXIBLES       |  |  QUERIES         |
  |                  |  |                  |  |                  |
  |  Anchos en %     |  |  max-width:100%  |  |  @media (...)    |
  |  en vez de px    |  |  se adaptan al   |  |  adaptan CSS     |
  |  fijos           |  |  contenedor      |  |  segun pantalla  |
  +------------------+  +------------------+  +------------------+
```

## Mobile-First vs Desktop-First

```
  MOBILE-FIRST (recomendado)         DESKTOP-FIRST (no recomendado)
  Estilos base = movil               Estilos base = escritorio
  @media (min-width) AGREGA          @media (max-width) DESHACE
  Menos CSS, 0 parches.              Mas CSS, mas "parches".
```

## Sintaxis de Media Queries

```css
@media <tipo> and (<caracteristica>: <valor>) {
    /* Reglas CSS condicionales */
}

/* Mobile-first: estilos se AGREGAN en pantallas grandes */
@media (min-width: 768px) { ... }

/* Desktop-first: estilos se QUITAN en pantallas pequenas */
@media (max-width: 768px) { ... }

/* Rango combinado */
@media screen and (min-width: 768px) and (max-width: 1024px) { ... }

/* OR con coma */
@media (max-width: 600px), (orientation: portrait) { ... }

/* Preferencias del usuario */
@media (prefers-color-scheme: dark) { ... }
@media (prefers-reduced-motion: reduce) { ... }
```

## Breakpoints comunes

| Breakpoint | Dispositivos tipicos              | Uso principal                     |
|------------|-----------------------------------|-----------------------------------|
| 480px      | Smartphones                       | Ajustes menores para movil grande |
| 768px      | Tablets (iPad portrait)           | Primer layout de 2 columnas       |
| 1024px     | Laptops, iPad landscape           | Layout completo con sidebar       |
| 1200px     | Escritorios estandar              | `max-width` del contenedor        |
| 1440px     | Monitores grandes                 | Ajustes para pantallas anchas     |

Buena practica: elegir breakpoints segun **donde el diseno lo necesita**, no segun dispositivos.

## Viewport meta tag (obligatorio)

```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

Sin esta etiqueta, el navegador movil simula una pantalla de ~980px y las media queries NO funcionan correctamente.

## Unidades fluidas

| Unidad  | Relativa a                  | Ejemplo                           |
|---------|-----------------------------|-----------------------------------|
| `%`     | El PADRE del elemento       | `width: 50%` = mitad del padre    |
| `vw`    | Ancho del VIEWPORT          | `width: 50vw` = mitad de ventana  |
| `vh`    | Alto del VIEWPORT           | `height: 100vh` = toda la altura  |
| `vmin`  | Lado mas pequeno del viewport | Util para cuadrados responsivos |
| `rem`   | Tamano base del `<html>`    | `1rem` = 16px por defecto         |

Formula para convertir px a %: `resultado = (objetivo / contexto) * 100%`

## Funciones CSS modernas (sin media queries)

```css
/* clamp(minimo, ideal, maximo) */
font-size: clamp(1rem, 2.5vw, 2rem);

/* min(): el MENOR de los valores (equivale a width + max-width) */
width: min(90%, 1200px);

/* max(): el MAYOR de los valores */
padding: max(2rem, 5vw);
```

## Imagenes responsivas

```css
img { max-width: 100%; height: auto; }  /* Nunca desborda, mantiene proporcion */
```

## Errores comunes

| Error | Problema | Solucion |
|-------|----------|----------|
| Olvidar el viewport meta tag | Media queries no funcionan en movil | Agregar `<meta name="viewport" ...>` |
| Usar `max-width` en mobile-first | Logica invertida, se deshacen estilos | Usar `min-width` para mobile-first |
| Anchos fijos en px para contenedores | No se adaptan a pantallas pequenas | Usar `%`, `vw`, o `max-width` |
| Breakpoints por dispositivo | Se rompe con nuevos dispositivos | Elegir breakpoints por el diseno |
| Imagenes sin `max-width: 100%` | Desbordan en pantallas pequenas | Agregar `max-width: 100%` a las imagenes |
| Texto con tamano fijo en px | No escala en movil | Usar `rem`, `em`, o `clamp()` |

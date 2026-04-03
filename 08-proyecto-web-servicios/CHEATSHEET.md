# Cheatsheet — Proyecto Web de Servicios (Modulo 08)

## Flujo de un proyecto web

```
  BRIEF ──> WIREFRAME ──> MOCKUP ──> CODIGO
  (que)     (cajas)       (visual)   (HTML+CSS)
```

## Estructura semantica tipica

```
<body>
├── <header>         Logo de la empresa
├── <nav>            Navegacion principal (<ul> + <li> + <a>)
├── <main>           Contenido principal (UNICO por pagina)
│   └── <div>        Wrapper de layout (sin semantica)
│       ├── <article>  Tarjeta de servicio (autocontenida)
│       ├── <article>  ...
│       └── <article>  ...
└── <footer>         Pie de pagina, copyright
```

### Cuando usar cada elemento

| Elemento    | Criterio                                        |
|-------------|-------------------------------------------------|
| `<article>` | Tiene sentido fuera de contexto (post, tarjeta) |
| `<section>` | Agrupa contenido tematico relacionado            |
| `<div>`     | Solo para layout, sin significado semantico      |

## Organizacion de archivos

```
proyecto-pequeno/            proyecto-grande/
├── index.html               ├── index.html
├── styles.css               ├── css/
└── images/                  │   ├── reset.css
    ├── logo.png             │   ├── variables.css
    └── ico_*.png            │   ├── components.css
                             │   └── responsive.css
                             ├── images/
                             ├── fonts/
                             └── js/
```

## Patron de tarjetas (Card Grid)

```
┌─────────────────────┐
│   TITULO  (<h2>)    │
│   ICONO   (<img>)   │
│   Texto   (<p>)     │
│   [Accion] (opc.)   │
└─────────────────────┘
  <article class="cajita">
```

## Breakpoints responsivos (contenido, NO dispositivo)

```
  < 560px (Movil)     560-768px (Tablet)    > 768px (Desktop)
  1 columna           2 columnas            4 columnas

  ┌──────────┐        ┌─────┬─────┐        ┌────┬────┬────┬────┐
  │ Tarjeta  │        │ T1  │ T2  │        │ T1 │ T2 │ T3 │ T4 │
  ├──────────┤        ├─────┼─────┤        └────┴────┴────┴────┘
  │ Tarjeta  │        │ T3  │ T4  │
  └──────────┘        └─────┴─────┘
```

```css
/* MOVIL — base, sin media query */
.contenedor { display: flex; flex-direction: column; }
.cajita     { flex: 1 1 100%; }

/* TABLET */
@media (min-width: 560px) and (max-width: 767px) {
  .contenedor { flex-direction: row; flex-wrap: wrap; }
  .cajita     { flex: 1 1 45%; }
}

/* DESKTOP */
@media (min-width: 768px) {
  .contenedor { flex-direction: row; flex-wrap: nowrap; }
  .cajita     { flex: 1 1 calc(100% / 4); }
}
```

## Anatomia del shorthand `flex`

```
flex: flex-grow  flex-shrink  flex-basis;
      |          |            |
      Crece?     Encoge?      Tamanio base
      0=no 1=si  0=no 1=si    100%, 45%, 200px...

Ejemplos:
  flex: 1 1 100%   --> 1 por fila (ocupa todo)
  flex: 1 1 45%    --> 2 por fila (con margen)
  flex: 0 0 200px  --> Fijo, siempre 200px
```

## Gradientes

```css
background: linear-gradient(180deg, #azulclaro, #ffffff);
```

```
  0deg (abajo>arriba)   90deg (izq>der)   180deg (arriba>abajo)
  ┌──── blanco ────┐    ┌──── color >──┐   ┌──── color ────┐
  │                │    │              │   │               │
  └──── color ─────┘    └──── blanco ──┘   └──── blanco ───┘
```

| Angulo  | Equivalente   | Direccion             |
|---------|---------------|-----------------------|
| 0deg    | to top        | Abajo hacia arriba    |
| 90deg   | to right      | Izquierda a derecha   |
| 180deg  | to bottom     | Arriba hacia abajo    |
| 270deg  | to left       | Derecha a izquierda   |

## Referencia rapida

| Concepto            | Sintaxis / Valor                         |
|---------------------|------------------------------------------|
| Copyright           | `&copy;`                                 |
| Trademark           | `&trade;`  /  `&reg;`                    |
| Espacio no-break    | `&nbsp;`                                 |
| justify-content     | `flex-start` `center` `space-between`    |
| Shorthand separador | **Espacios** (nunca comas)               |

## Errores comunes

| Error                          | Solucion                                    |
|--------------------------------|---------------------------------------------|
| Comas en `flex: 1, 1, 25%`    | Usar espacios: `flex: 1 1 25%`              |
| `justify-content: left`       | Usar `flex-start` (valor estandar)          |
| Media queries se solapan       | Evitar rangos que coincidan (767px vs 768px) |
| Orden de media queries         | Tablet primero, desktop despues (cascada)   |
| Breakpoints por dispositivo    | Definir donde el CONTENIDO lo necesita      |
| `<div>` para todo              | Usar `<article>`, `<section>`, `<nav>`      |

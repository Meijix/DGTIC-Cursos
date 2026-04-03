# Cheatsheet — Modulo 05: Componentes CSS

## Que es un componente CSS

```
  AUTOCONTENIDO          REUTILIZABLE           INDEPENDIENTE
  Tiene todo lo que      Se copia y pega        Cambiar uno no
  necesita (HTML+CSS)    tantas veces como      afecta a los
  para funcionar.        se quiera.             demas.
```

Tres categorias de CSS:

| Tipo        | Proposito                         | Ejemplo                        |
|-------------|-----------------------------------|--------------------------------|
| Componente  | Pieza de UI reutilizable          | `.card`, `.button`, `.navbar`  |
| Layout      | Organiza DONDE van los componentes| `.cards-container`, `.grid`    |
| Utilidad    | Una sola propiedad reutilizable   | `.text-center`, `.mt-10`       |

## Patron: clase base + clase modificadora

```
  HTML:  class="card red-card"
                ^       ^
                |       +---- Modificadora: solo cambia el gradiente
                +------------ Base: tamano, sombra, bordes, tipografia

  CSS:
  .card      { border-radius: 10px; padding: 20px; box-shadow: 0 0 25px #000; }
  .red-card  { background: linear-gradient(#000, #d84242); }
  .blue-card { background: linear-gradient(#000, #242a92); }
```

Para agregar una variante nueva, solo se escribe UNA regla nueva.

## Anatomia de una tarjeta (Card)

```
  +==========================================+
  |              .card .red-card              |  <article>
  |          +------------------+            |
  |          |    .card_img     |            |  <img> con border-radius: 50%
  |          +------------------+            |
  |          Nombre Completo                 |  .card_title <h2>
  |          Subtitulo                       |  .card_subtitle <p>
  |   Texto descriptivo del contenido...     |  .card_content <p>
  +==========================================+
         | box-shadow: 0 0 25px 0 #000
```

## BEM: Block Element Modifier

```
  BLOQUE:       .card                 El componente principal
  ELEMENTO:     .card__title          Parte DENTRO del bloque (separador: __)
  MODIFICADOR:  .card--red            Variante del bloque (separador: --)
```

## Gradientes CSS

```css
/* LINEAR */
background: linear-gradient(#000, #d84242);             /* defecto: to bottom */
background: linear-gradient(90deg, #000, #d84242);      /* izquierda a derecha */

/* RADIAL */
background: radial-gradient(circle, #fff, #000);

/* CONICO */
background: conic-gradient(#d84242, #242a92, #287346, #d84242);
```

| Direccion         | Efecto                  | Grados  |
|-------------------|-------------------------|---------|
| `to bottom`       | Arriba hacia abajo      | 180deg  |
| `to right`        | Izquierda a derecha     | 90deg   |
| `to top`          | Abajo hacia arriba      | 0deg    |
| `to bottom right` | Diagonal                | ~135deg |

## box-shadow y border-radius

```
  box-shadow: <offset-x> <offset-y> <blur> <spread> <color>;
              (+der/-izq)  (+abajo/-arriba) (difuso) (expansion)
```

```css
box-shadow: 0 0 25px 0 #000;                 /* Resplandor uniforme */
box-shadow: 0 4px 6px -1px rgba(0,0,0,0.3);  /* Sutil tipo Material Design */
box-shadow: inset 0 0 10px #000;              /* Sombra interior */

border-radius: 10px;           /* Esquinas redondeadas */
border-radius: 50%;            /* Circulo (si width = height) */
```

## Errores comunes

| Error | Problema | Solucion |
|-------|----------|----------|
| Duplicar estilos base en cada variante | CSS inflado y dificil de mantener | Usar patron base + modificadora |
| `border-radius: 50%` sin ancho=alto | Forma de ovalo, no circulo | Asegurar `width` = `height` |
| Gradiente sin direccion | No es error pero puede confundir | El defecto es `to bottom` (180deg) |
| Sombras con colores solidos | Se ven poco naturales | Usar `rgba()` con transparencia |
| Usar IDs para estilos de componente | No se puede reutilizar | Usar clases (.card, no #card) |
| Olvidar `max-width` en tarjetas | Se estiran en pantallas grandes | Agregar `max-width` al componente |

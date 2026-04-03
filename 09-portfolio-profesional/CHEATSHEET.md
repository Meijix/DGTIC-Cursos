# Cheatsheet — Portfolio Profesional: CSS Avanzado y JavaScript (Modulo 09)

## Position CSS

| Valor      | En flujo | Referencia           | Uso tipico                 |
|------------|----------|----------------------|----------------------------|
| `static`   | Si       | N/A                  | Por defecto, flujo normal  |
| `relative` | Si       | Su posicion original | Contexto para hijos `absolute` |
| `absolute` | No       | Ancestro posicionado | Badges, overlays, tooltips |
| `fixed`    | No       | Viewport             | Navegacion fija            |
| `sticky`   | Si*      | Ancestro de scroll   | Header que se "pega"       |

```
  fixed:                            sticky:
  ┌─ Viewport ──────────┐          Antes del umbral: fluye normal
  │ ▓▓▓ NAV (siempre) ▓▓│          Despues del umbral: se pega
  │                      │
  │  Contenido scroll    │          Requisito: padre con altura
  │  pasa DETRAS del nav │          suficiente para permitir scroll
  └──────────────────────┘
```

**Truco clasico:** padre `position: relative` + hijo `position: absolute`.

## Transiciones CSS

```css
transition: propiedad  duracion  timing  delay;
transition: background-color 0.3s ease 0s;

/* Multiples */
transition: background-color 0.3s ease,
            transform 0.5s ease-out;
```

### Timing functions

| Funcion       | Comportamiento                        |
|---------------|---------------------------------------|
| `ease`        | Lento-rapido-lento (por defecto)      |
| `linear`      | Velocidad constante                   |
| `ease-in`     | Inicio lento, final rapido            |
| `ease-out`    | Inicio rapido, final lento            |
| `ease-in-out` | Lento en ambos extremos               |

### Rendimiento de animaciones

```
  MAS COSTOSO                         MAS BARATO
  Layout (width, margin)  >  Paint (color, shadow)  >  Composite (transform, opacity)

  REGLA: Animar solo transform y opacity siempre que sea posible.

  En lugar de:              Usa:
  left: 100px               transform: translateX(100px)
  width: 200px              transform: scaleX(2)
  margin-top: 20px          transform: translateY(20px)
```

## JavaScript DOM basico

```javascript
// Seleccionar elementos
document.querySelector('.clase');          // Primero que coincida
document.querySelectorAll('section');      // Todos (NodeList)

// NodeList a Array (para map, filter, reduce)
const arr = [...document.querySelectorAll('section')];

// Eventos
elemento.addEventListener('click', (event) => {
  event.preventDefault();     // Evitar comportamiento default
  event.target;               // Elemento que disparo el evento
});

// Manipular clases
elemento.classList.add('visible');
elemento.classList.remove('visible');
elemento.classList.toggle('activo');
elemento.classList.contains('activo');  // true/false
```

### Eventos comunes

| Evento       | Cuando se dispara                   |
|-------------|--------------------------------------|
| `click`     | Clic del usuario                     |
| `scroll`    | Desplazamiento del contenido         |
| `resize`    | Cambio de tamanio de ventana         |
| `keydown`   | Tecla presionada                     |
| `submit`    | Envio de formulario                  |
| `mouseenter`| Cursor entra al elemento             |

## Patron fundamental de interactividad

```
1. CSS define ESTADOS (clases con estilos)
   .menu          { transform: translateX(-100%); }
   .menu.abierto  { transform: translateX(0); }

2. JS ALTERNA la clase
   boton.addEventListener('click', () => {
     menu.classList.toggle('abierto');
   });

3. CSS TRANSICIONES animan el cambio
   .menu { transition: transform 0.3s ease; }
```

## IntersectionObserver (animaciones de scroll)

```javascript
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
      observer.unobserve(entry.target);  // Solo una vez
    }
  });
}, { threshold: 0.1 });  // 10% visible

document.querySelectorAll('.seccion').forEach(s => observer.observe(s));
```

```css
/* Estado inicial: oculto */
.seccion { opacity: 0; transform: translateY(30px);
           transition: opacity 0.6s ease, transform 0.6s ease; }

/* Estado final: visible */
.seccion.visible { opacity: 1; transform: translateY(0); }
```

## Navegacion fija + Smooth Scroll

```css
/* Nav fija */
.nav {
  position: fixed; top: 0; left: 0;
  width: 100%; z-index: 1000;
}

/* Compensar contenido oculto */
body { padding-top: 70px; }

/* Smooth scroll + compensacion de anclas */
html {
  scroll-behavior: smooth;
  scroll-padding-top: 80px;
}
```

```javascript
// Smooth scroll con JS (mas control)
document.querySelector('#contacto').scrollIntoView({
  behavior: 'smooth',
  block: 'start'  // 'start', 'center', 'end'
});
```

## z-index

```
  Solo funciona en elementos posicionados (relative, absolute, fixed, sticky).

  GOTCHA: z-index alto dentro de un contexto de apilamiento
  NUNCA supera a un contexto hermano con z-index mayor.
```

## Referencia rapida

| Patron                  | Solucion                                   |
|-------------------------|--------------------------------------------|
| Header fijo             | `position: fixed` + `padding-top` en body  |
| Header pegajoso         | `position: sticky; top: 0`                 |
| Ancla tapada por nav    | `scroll-padding-top: 80px` en html         |
| Animacion al scroll     | IntersectionObserver + classList.add        |
| Scroll suave            | `scroll-behavior: smooth` en html          |

## Errores comunes

| Error                              | Solucion                                |
|------------------------------------|-----------------------------------------|
| `sticky` no funciona               | Padre necesita altura suficiente        |
| Animar `width`/`margin` (lento)    | Usar `transform` y `opacity`            |
| `scroll` event (60+ calls/seg)     | Usar IntersectionObserver               |
| Contenido oculto bajo nav fijo     | `padding-top` igual a altura del nav    |
| `transition: all` en produccion    | Especificar propiedades individualmente |
| `z-index` sin `position`           | Agregar `position: relative` al menos   |
| Olvidar `event.preventDefault()`   | Usarlo en enlaces con `href="#"`        |

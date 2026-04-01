# Modulo 05 — Componentes CSS: Diseno Modular

> **Archivos de referencia:** `index.html` y `styles.css` en esta misma carpeta.
> **Prerequisitos:** Modulos 01-04 (HTML, CSS basico, pagina web, Flexbox).

---

## Indice

1. [Que es un componente](#1-que-es-un-componente)
2. [Anatomia de una tarjeta (Card)](#2-anatomia-de-una-tarjeta-card)
3. [Nomenclatura: BEM y alternativas](#3-nomenclatura-bem-y-alternativas)
4. [Gradientes CSS](#4-gradientes-css)
5. [Sombras: box-shadow y text-shadow](#5-sombras-box-shadow-y-text-shadow)
6. [Contraste y accesibilidad de color](#6-contraste-y-accesibilidad-de-color)
7. [Errores comunes](#7-errores-comunes)
8. [Ejercicios de practica](#8-ejercicios-de-practica)

---

## 1. Que es un componente

Un **componente** en CSS es una pieza de interfaz que cumple tres requisitos:

```
  +---------------------------------------------------------------+
  |                                                               |
  |  AUTOCONTENIDO     REUTILIZABLE       INDEPENDIENTE           |
  |  ~~~~~~~~~~~~~~    ~~~~~~~~~~~~~      ~~~~~~~~~~~~~~          |
  |  Tiene todo lo     Puedes copiarlo    Cambiar un              |
  |  que necesita      y pegarlo tantas   componente no           |
  |  (HTML + CSS)      veces como         afecta a los            |
  |  para funcionar.   quieras.           demas.                  |
  |                                                               |
  +---------------------------------------------------------------+
```

### Analogias del mundo real

```
  PIEZA DE LEGO                      COMPONENTE CSS
  ~~~~~~~~~~~~~~~~                   ~~~~~~~~~~~~~~~
  - Forma predefinida                - Estructura HTML fija
  - Se conecta con otras piezas      - Se combina con otros componentes
  - Puedes usar la misma pieza       - Puedes reutilizar la misma clase
    muchas veces                       muchas veces
  - Cambiar una pieza no rompe       - Cambiar .card no afecta a .navbar
    las demas

  PARTE DE UN CARRO                  COMPONENTE CSS
  ~~~~~~~~~~~~~~~~~                  ~~~~~~~~~~~~~~~
  - La llanta funciona sola          - El .card funciona solo
  - Puedes reemplazarla por otra     - Puedes cambiar la variante (.red-card
    compatible                          por .blue-card)
  - Tiene interfaz estandar           - Tiene clases CSS estandar
    (tornillos, diametro)               (.card_title, .card_img)
```

### Tres tipos de CSS

No todo el CSS es "componente". Hay tres categorias:

```
  TIPO          | PROPOSITO                      | EJEMPLO
  --------------|--------------------------------|---------------------------
  COMPONENTE    | Define una pieza de UI          | .card, .card_title,
                | reutilizable e independiente    | .navbar, .modal, .button
  --------------|--------------------------------|---------------------------
  LAYOUT        | Organiza DONDE van los          | .cards-container,
                | componentes en la pagina        | .sidebar-layout,
                |                                | .grid-2-cols
  --------------|--------------------------------|---------------------------
  UTILIDAD      | Una sola propiedad CSS          | .text-center,
                | reutilizable                    | .mt-10 (margin-top: 10px),
                |                                | .hidden
```

En el ejercicio 05:
- **Componente:** `.card`, `.card_img`, `.card_title`, `.card_subtitle`, `.card_content`
- **Layout:** `.cards-container` (Flexbox que organiza las tarjetas)
- **Modificadores:** `.red-card`, `.blue-card`, `.green-card` (variantes)

---

## 2. Anatomia de una tarjeta (Card)

### Estructura visual

```
  +==========================================+
  |              .card .red-card              |   <-- <article>
  |                                          |       Dos clases: base + modificador
  |          +------------------+            |
  |          |                  |            |
  |          |    .card_img     |            |   <-- <img> circular
  |          |   (border-       |            |
  |          |    radius: 50%)  |            |
  |          +------------------+            |
  |                                          |
  |          Natalia Edith Mejia             |   <-- .card_title <h2>
  |                                          |
  |       Estudiante de Matematicas          |   <-- .card_subtitle <p>
  |                                          |
  |   Lorem ipsum dolor sit amet             |
  |   consectetur adipisicing elit.          |   <-- .card_content <p>
  |   Odit porro animi, necessitatibus       |
  |   amet laborum fuga maxime...            |
  |                                          |
  +==========================================+
         |
         |  box-shadow: 0 0 25px 0 #000
         |  (efecto de resplandor)
         v
```

### Estructura HTML

```html
<article class="card red-card">
    <img class="card_img" src="..." alt="...">
    <h2 class="card_title">Nombre</h2>
    <p class="card_subtitle">Rol</p>
    <p class="card_content">Descripcion...</p>
</article>
```

### Patron: clase base + clase modificadora

```
  HTML:     class="card red-card"
                    ^      ^
                    |      +---- Clase MODIFICADORA: solo el gradiente rojo
                    +----------- Clase BASE: tamano, sombra, bordes, tipografia

  CSS:
  .card {                              .red-card {
      text-align: center;                 background: linear-gradient(
      border-radius: 10px;                    #000000, #d84242);
      width: 100%;                     }
      max-width: 400px;
      padding: 20px 10px;              .blue-card {
      box-shadow: 0 0 25px 0 #000;        background: linear-gradient(
      color: #f0f0f0;                         #000000, #242a92);
  }                                    }

  La clase BASE contiene todo lo       Las clases MODIFICADORAS solo
  que es COMUN a todas las             contienen lo que VARIA entre
  variantes.                           variantes.
```

**Ventaja:** Si necesitas una nueva variante (ej. tarjeta amarilla),
solo escribes UNA regla CSS nueva:

```css
.yellow-card {
    background: linear-gradient(#000000, #d4a842);
}
```

Sin este patron, tendrias que DUPLICAR todos los estilos de `.card`
en cada variante.

---

## 3. Nomenclatura: BEM y alternativas

### BEM: Block Element Modifier

BEM es una convencion de nombres para clases CSS inventada por Yandex:

```
  BLOQUE:      .card                  El componente principal
  ELEMENTO:    .card__title           Una parte DENTRO del bloque
  MODIFICADOR: .card--red             Una VARIANTE del bloque

  Separadores:
  __  (doble guion bajo)  = elemento dentro del bloque
  --  (doble guion medio) = modificador/variante
```

### Diagrama BEM aplicado a la tarjeta

```
  BLOQUE: .card
  +============================================+
  |                                            |
  |  ELEMENTO: .card__img                      |
  |  +------------------+                      |
  |  |     (imagen)     |                      |
  |  +------------------+                      |
  |                                            |
  |  ELEMENTO: .card__title                    |
  |  "Natalia Edith Mejia"                     |
  |                                            |
  |  ELEMENTO: .card__subtitle                 |
  |  "Estudiante de Matematicas"               |
  |                                            |
  |  ELEMENTO: .card__content                  |
  |  "Lorem ipsum dolor sit amet..."           |
  |                                            |
  +============================================+

  MODIFICADORES del BLOQUE:
  .card--red     -> fondo con gradiente rojo
  .card--blue    -> fondo con gradiente azul
  .card--green   -> fondo con gradiente verde
```

### BEM estricto vs. version del ejercicio

```
  BEM ESTRICTO                    | EN NUESTRO EJERCICIO (simplificado)
  --------------------------------|--------------------------------------
  .card                           | .card
  .card__img                      | .card_img        (un solo guion bajo)
  .card__title                    | .card_title
  .card__subtitle                 | .card_subtitle
  .card__content                  | .card_content
  .card--red                      | .red-card         (clase separada)
  .card--blue                     | .blue-card
  .card--green                    | .green-card
```

Ambos enfoques funcionan. BEM estricto es mas explicito sobre las
relaciones; el enfoque simplificado es mas facil de leer y escribir.

### Comparacion de convenciones CSS

```
  CONVENCION     | FILOSOFIA                    | EJEMPLO               | PROS/CONTRAS
  ---------------|------------------------------|-----------------------|--------------------
  BEM            | Bloques, elementos y         | .card__title--large   | (+) Muy claro
                 | modificadores con            |                       | (+) Predecible
                 | separadores explicitos       |                       | (-) Nombres largos
  ---------------|------------------------------|-----------------------|--------------------
  OOCSS          | Separar ESTRUCTURA           | .card + .skin-red     | (+) Muy reutilizable
  (Object-       | de APARIENCIA.               | .media + .media-body  | (-) Muchas clases
  Oriented CSS)  | Objetos CSS reutilizables    |                       |     en el HTML
  ---------------|------------------------------|-----------------------|--------------------
  SMACSS         | Categorizar CSS en 5         | .l-sidebar            | (+) Buena organizacion
  (Scalable &    | tipos: Base, Layout,         | .is-active            |     para proyectos
  Modular)       | Module, State, Theme         | .theme-dark           |     grandes
                 |                              |                       | (-) Mas complejo
  ---------------|------------------------------|-----------------------|--------------------
  Utility-First  | Clases pequenas de una       | class="flex items-    | (+) Rapido de escribir
  (Tailwind CSS) | sola propiedad que se        | center gap-4 p-2     | (+) No inventa nombres
                 | combinan en el HTML          | bg-red-500 rounded"   | (-) HTML muy cargado
                 |                              |                       | (-) Curva de aprendizaje
  ---------------|------------------------------|-----------------------|--------------------
  CSS Modules /  | Cada componente tiene su     | .title (automatico:   | (+) Cero conflictos
  Scoped CSS     | propio archivo CSS aislado.  |  .card_a3f2_title)    | (-) Requiere tooling
                 | Las clases se transforman    |                       |     (webpack, Vite)
                 | automaticamente para ser     |                       |
                 | unicas.                      |                       |
```

### Cuando usar cual

```
  Proyecto personal / pequeno  -->  Cualquiera funciona, BEM simplificado es buena opcion
  Proyecto mediano (equipo)    -->  BEM estricto o SMACSS
  Aplicacion grande (empresa)  -->  CSS Modules, CSS-in-JS, o Utility-First (Tailwind)
  Prototipo rapido             -->  Utility-First (Tailwind)
```

---

## 4. Gradientes CSS

### linear-gradient: degradado lineal

Un degradado lineal crea una transicion suave entre dos o mas colores
a lo largo de una linea recta.

```
  Sintaxis:
  background: linear-gradient( <direccion>, <color1> <parada1>, <color2> <parada2>, ... );
```

### Direcciones

```
  VALOR              | EFECTO                  | EQUIVALENTE
  -------------------|-------------------------|------------------
  to bottom          | De arriba hacia abajo   | 180deg (defecto)
  to top             | De abajo hacia arriba   | 0deg
  to right           | De izquierda a derecha  | 90deg
  to left            | De derecha a izquierda  | 270deg
  to bottom right    | Diagonal                | ~135deg
  to top left        | Diagonal inversa        | ~315deg
  45deg              | A 45 grados             | 45deg
  135deg             | A 135 grados            | to bottom right
```

### Visualizacion de direcciones

```
  to bottom (180deg)     to right (90deg)      45deg
  (defecto)

  +-----------+          +-----------+         +-----------+
  | ######### |          | ##        |         | ####      |
  | ######### |          | ####      |         |  #####    |
  | ......... |          | ######    |         |   ######  |
  | ......... |          | ########  |         |    ###### |
  |           |          | ########## |        |     ######|
  +-----------+          +-----------+         +-----------+
  # = color1              # = color1            # = color1
  . = transicion          (izq a der)           (diagonal)
    = color2
```

### Color stops (paradas de color)

```css
/* Dos colores, distribucion automatica (50/50) */
background: linear-gradient(#000000, #d84242);

/* Tres colores con posiciones explicitas */
background: linear-gradient(#000 0%, #d84242 50%, #000 100%);

/* Color concentrado en una zona especifica */
background: linear-gradient(#000 0%, #000 40%, #d84242 60%, #d84242 100%);
```

Visualizacion de las paradas de color:

```
  linear-gradient(#000 0%, #d84242 50%, #fff 100%)

  0%   ████████████████  #000000 (negro)
       ████████████████
  25%  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  transicion negro -> rojo
       ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
  50%  ░░░░░░░░░░░░░░░░  #d84242 (rojo)
       ░░░░░░░░░░░░░░░░
  75%  ................  transicion rojo -> blanco
       ................
  100%                    #ffffff (blanco)


  linear-gradient(#000 0%, #000 40%, #d84242 60%, #d84242 100%)

  0%   ████████████████  #000000 (negro solido)
  20%  ████████████████
  40%  ████████████████
       ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  transicion rapida (solo 20% del espacio)
  60%  ░░░░░░░░░░░░░░░░  #d84242 (rojo solido)
  80%  ░░░░░░░░░░░░░░░░
  100% ░░░░░░░░░░░░░░░░
```

### En el ejercicio (`styles.css`)

```css
.red-card   { background: linear-gradient(#000000, #d84242); }  /* negro -> rojo */
.blue-card  { background: linear-gradient(#000000, #242a92); }  /* negro -> azul */
.green-card { background: linear-gradient(#000000, #287346); }  /* negro -> verde */
```

Todas van de arriba (negro) hacia abajo (color), porque no se especifica
direccion (defecto: `to bottom` = `180deg`).

### radial-gradient: degradado radial

Crea una transicion que se expande desde un punto central hacia afuera.

```css
/* Basico: del centro hacia afuera */
background: radial-gradient(#d84242, #000000);

/* Con forma y posicion */
background: radial-gradient(circle at top left, #d84242, #000000);
background: radial-gradient(ellipse at 30% 70%, #d84242 20%, #000 80%);
```

```
  radial-gradient(circle, #fff, #000)

  +-------------------+
  |     .........     |
  |   ...........     |
  |  .....*****....   |
  | ....**     **...  |
  | ...*         *..  |
  | ...*         *..  |
  | ....**     **...  |
  |  .....*****....   |
  |   ...........     |
  |     .........     |
  +-------------------+
  * = blanco (centro)
  . = transicion
    = negro (bordes)
```

### conic-gradient: degradado conico

Crea una transicion que rota alrededor de un punto central (como un reloj).

```css
/* Degradado conico simple */
background: conic-gradient(#d84242, #242a92, #287346, #d84242);

/* Grafico de pastel */
background: conic-gradient(
    #d84242 0deg 120deg,      /* rojo: 0 a 120 grados */
    #242a92 120deg 240deg,    /* azul: 120 a 240 grados */
    #287346 240deg 360deg     /* verde: 240 a 360 grados */
);
```

```
  conic-gradient(red, blue, green, red)

  +-------------------+
  |  verde   |  rojo  |
  |     \    |   /    |
  |      \   |  /     |
  |-------***---------|
  |      /   |  \     |
  |     /    |   \    |
  |  verde   |  azul  |
  +-------------------+
  (la transicion gira como las agujas del reloj)
```

### Degradados repetidos

```css
/* Rayas diagonales */
background: repeating-linear-gradient(
    45deg,
    #d84242 0px,
    #d84242 10px,
    #000000 10px,
    #000000 20px
);

/* Circulos concentricos */
background: repeating-radial-gradient(
    circle,
    #d84242 0px,
    #d84242 10px,
    #000000 10px,
    #000000 20px
);
```

---

## 5. Sombras: box-shadow y text-shadow

### box-shadow: sombra de caja

```
  Sintaxis:
  box-shadow: <offset-x> <offset-y> <blur> <spread> <color>;
  box-shadow: <inset> <offset-x> <offset-y> <blur> <spread> <color>;

  +---offset-x---->
  |
  offset-y    +===========+
  |           |           |
  v           |  ELEMENTO |
              |           |
              +===========+
                   ............
                   . SOMBRA   .
                   ............
```

### Desglose de cada valor

```
  VALOR      | QUE HACE                                   | EN EL EJERCICIO
  -----------|--------------------------------------------|-----------------
  offset-x   | Desplazamiento horizontal de la sombra     | 0 (sin desplazar)
             | (+) derecha, (-) izquierda                 |
  -----------|--------------------------------------------|-----------------
  offset-y   | Desplazamiento vertical de la sombra       | 0 (sin desplazar)
             | (+) abajo, (-) arriba                      |
  -----------|--------------------------------------------|-----------------
  blur       | Radio de desenfoque. Mayor = mas difusa    | 25px (muy difusa)
             | 0 = borde duro                             |
  -----------|--------------------------------------------|-----------------
  spread     | Expansion de la sombra antes del blur      | 0 (sin expansion)
             | (+) sombra mas grande, (-) mas pequena     |
  -----------|--------------------------------------------|-----------------
  color      | Color de la sombra                         | #000000 (negro)
  -----------|--------------------------------------------|-----------------
  inset      | (opcional) La sombra va DENTRO del         | (no usado)
             | elemento en vez de fuera                   |
```

### Ejemplos visuales

```
  box-shadow: 5px 5px 0 0 #000;        box-shadow: 0 0 25px 0 #000;
  (Sombra solida, abajo-derecha)        (Resplandor uniforme, como en el ejercicio)

  +===========+                         ....+===========+....
  |           |                         .   |           |   .
  |  ELEMENTO |                         .   |  ELEMENTO |   .
  |           |                         .   |           |   .
  +===========+####                     ....+===========+....
       ############                     .........................
                                        (sombra en TODOS los lados)


  box-shadow: 0 4px 6px -1px rgba(0,0,0,0.3);
  (Sombra sutil tipo Material Design)

  +===========+
  |           |
  |  ELEMENTO |
  |           |
  +===========+
     ..........
  (solo abajo, sutil y semitransparente)


  box-shadow: inset 0 0 10px #000;
  (Sombra interior)

  +===========+
  |###       #|
  |#         #|
  |#         #|
  |###       #|
  +===========+
  # = sombra DENTRO del elemento
```

### Sombras multiples

Puedes apilar multiples sombras separadas por comas. Se renderizan
de la primera (arriba) a la ultima (abajo):

```css
box-shadow:
    0 1px 3px rgba(0,0,0,0.12),     /* Sombra sutil cercana */
    0 4px 6px rgba(0,0,0,0.08),     /* Sombra media */
    0 10px 20px rgba(0,0,0,0.04);   /* Sombra difusa lejana */
```

Este patron de multiples sombras crea un efecto de **elevacion realista**
(las sombras en la vida real son complejas, no un solo tono uniforme).

### text-shadow: sombra de texto

```
  Sintaxis:
  text-shadow: <offset-x> <offset-y> <blur> <color>;

  (No tiene "spread" ni "inset" como box-shadow.)
```

```css
/* Sombra basica en texto */
text-shadow: 2px 2px 4px rgba(0,0,0,0.5);

/* Efecto de resplandor en texto (neon) */
text-shadow: 0 0 10px #d84242, 0 0 20px #d84242, 0 0 40px #d84242;

/* Texto grabado (incrustado) */
text-shadow: 0 -1px 0 rgba(0,0,0,0.5);  /* sombra arriba = parece hundido */

/* Texto en relieve (elevado) */
text-shadow: 0 1px 0 rgba(255,255,255,0.5);  /* sombra abajo = parece elevado */
```

### Rendimiento

Las sombras con `blur` grande son costosas de renderizar. Considera:

```
  RECOMENDACION                           | POR QUE
  ----------------------------------------|------------------------------------
  Usa blur razonable (< 30px)             | Blur grande = calculo complejo
                                          | por cada pixel de la sombra
  ----------------------------------------|------------------------------------
  Evita sombras en elementos que          | Cada fotograma recalcula la sombra
  se animan frecuentemente                |
  ----------------------------------------|------------------------------------
  Usa will-change: transform en           | Le dice al navegador que prepare
  elementos animados con sombra           | la sombra en la GPU
  ----------------------------------------|------------------------------------
  En listas largas, usa sombras simples   | 100 tarjetas x sombra compleja =
  o un solo color sin blur                | impacto notable en scroll
```

---

## 6. Contraste y accesibilidad de color

### Por que importa el contraste

```
  Texto con BUEN contraste:           Texto con MAL contraste:

  +---------------------------+       +---------------------------+
  | ######################## |       |                           |
  | ## Texto negro sobre   # |       |   Texto gris claro sobre |
  | ## fondo blanco        # |       |   fondo blanco           |
  | ######################## |       |                           |
  +---------------------------+       +---------------------------+
  Ratio: ~21:1 (EXCELENTE)           Ratio: ~1.5:1 (ILEGIBLE
                                      para muchas personas)
```

### Requisitos WCAG 2.1

Las Web Content Accessibility Guidelines (WCAG) definen niveles minimos
de contraste entre texto y fondo:

```
  NIVEL | TEXTO NORMAL          | TEXTO GRANDE              | QUE SIGNIFICA
        | (< 18pt / < 14pt     | (>= 18pt / >= 14pt       |
        |  bold)                |  bold)                    |
  ------|------------------------|---------------------------|-------------------
  AA    | 4.5 : 1 minimo        | 3 : 1 minimo              | Requisito MINIMO
        |                        |                           | aceptable. La
        |                        |                           | mayoria de sitios
        |                        |                           | deben cumplir esto.
  ------|------------------------|---------------------------|-------------------
  AAA   | 7 : 1 minimo          | 4.5 : 1 minimo            | Nivel OPTIMO.
        |                        |                           | Recomendado para
        |                        |                           | texto cuerpo.
```

**Texto grande:** 18pt (24px) normal o 14pt (18.67px) en negritas.

### Como se calcula el ratio de contraste

El ratio se calcula comparando la **luminancia relativa** de dos colores:

```
  Ratio = (L1 + 0.05) / (L2 + 0.05)

  Donde:
  L1 = luminancia del color mas claro
  L2 = luminancia del color mas oscuro

  La luminancia se calcula a partir de los valores RGB:
  1. Convertir R, G, B de 0-255 a 0-1: valor / 255
  2. Aplicar correccion gamma:
     Si valor <= 0.03928: valor / 12.92
     Si valor >  0.03928: ((valor + 0.055) / 1.055) ^ 2.4
  3. Luminancia = 0.2126 * R + 0.7152 * G + 0.0722 * B
```

**No necesitas calcular esto a mano.** Usa herramientas:

### Herramientas para verificar contraste

```
  HERRAMIENTA                              | URL / COMO USARLA
  -----------------------------------------|-------------------------------------
  WebAIM Contrast Checker                  | https://webaim.org/resources/
                                           | contrastchecker/
                                           | Ingresa color de texto y fondo.
  -----------------------------------------|-------------------------------------
  Chrome DevTools                          | Inspeccionar elemento > color >
                                           | Muestra el ratio automaticamente
                                           | con indicador AA/AAA.
  -----------------------------------------|-------------------------------------
  Firefox Accessibility Inspector          | Herramientas > Accesibilidad >
                                           | Verificar problemas de contraste
  -----------------------------------------|-------------------------------------
  Lighthouse (Chrome)                      | DevTools > Lighthouse > Accesibilidad
                                           | Genera un reporte completo.
  -----------------------------------------|-------------------------------------
  axe DevTools (extension)                 | Extension para Chrome/Firefox
                                           | Analiza la pagina completa.
```

### Ejemplo del ejercicio (`styles.css`)

En el `body` del ejercicio 05:

```css
body {
    background-color: beige;    /* #F5F5DC */
    color: #1a1a1a;             /* Casi negro */
}
```

```
  beige (#F5F5DC)  como fondo
  #1a1a1a          como texto

  Luminancia beige:   0.854
  Luminancia #1a1a1a: 0.012

  Ratio = (0.854 + 0.05) / (0.012 + 0.05) = 0.904 / 0.062 = ~14.6:1

  Resultado: PASA AA (4.5:1) y AAA (7:1) con amplio margen.
```

Compara con el error original que se menciona en el CSS:

```
  aliceblue (#F0F8FF) como TEXT sobre beige (#F5F5DC) como fondo:

  Ambos colores son MUY claros.
  Ratio aproximado: ~1.1:1 = FALLA completamente.
  Seria practicamente invisible.
```

### Errores de contraste comunes y soluciones

```
  ERROR                              | RATIO  | SOLUCION
  -----------------------------------|--------|----------------------------
  Gris claro (#999) sobre blanco     | ~2.8:1 | Oscurecer a #767676 (4.5:1)
  Gris claro (#999) sobre blanco     |        | o a #595959 (7:1)
  -----------------------------------|--------|----------------------------
  Texto blanco sobre amarillo        | ~1.1:1 | Usar texto negro o fondo
  (#fff sobre #ffff00)               |        | mas oscuro
  -----------------------------------|--------|----------------------------
  Texto azul claro sobre fondo azul  | ~2:1   | Aumentar la diferencia
  (#66f sobre #009)                  |        | de luminosidad
  -----------------------------------|--------|----------------------------
  Texto sobre imagen de fondo        | Varia  | Agregar overlay oscuro
                                     |        | semitransparente sobre
                                     |        | la imagen
  -----------------------------------|--------|----------------------------
  Placeholder gris claro en inputs   | ~2:1   | Oscurecer placeholder o
  (#ccc en input)                    |        | usar patron diferente
```

### Daltonismo y colores

El contraste de luminosidad es importante, pero tambien considera:

```
  NO confies solo en el COLOR para transmitir informacion.

  MAL:   "Los campos en rojo tienen error"
         (las personas con daltonismo no ven el rojo)

  BIEN:  "Los campos con error tienen borde rojo + icono de advertencia
          + texto 'Este campo es obligatorio'"
         (multiples senales: color + forma + texto)
```

---

## 7. Errores comunes

### Error 1: Repetir estilos en lugar de usar clase base + modificador

```css
/* MAL: duplicacion masiva */
.red-card {
    text-align: center;
    border-radius: 10px;
    width: 100%;
    max-width: 400px;
    box-shadow: 0 0 25px 0 #000;
    background: linear-gradient(#000, #d84242);
}
.blue-card {
    text-align: center;           /* DUPLICADO */
    border-radius: 10px;         /* DUPLICADO */
    width: 100%;                 /* DUPLICADO */
    max-width: 400px;            /* DUPLICADO */
    box-shadow: 0 0 25px 0 #000; /* DUPLICADO */
    background: linear-gradient(#000, #242a92);
}

/* BIEN: clase base + modificador */
.card {
    text-align: center;
    border-radius: 10px;
    width: 100%;
    max-width: 400px;
    box-shadow: 0 0 25px 0 #000;
}
.red-card  { background: linear-gradient(#000, #d84242); }
.blue-card { background: linear-gradient(#000, #242a92); }
```

---

### Error 2: Gradiente como `background-color` en vez de `background`

```css
/* MAL: no funciona */
.card {
    background-color: linear-gradient(#000, #d84242);
}
/* linear-gradient() genera una IMAGEN, no un color.
   background-color solo acepta colores solidos. */

/* BIEN */
.card {
    background: linear-gradient(#000, #d84242);
}
/* "background" es el shorthand que acepta imagenes. */
```

---

### Error 3: Olvidar que border-radius: 50% necesita un cuadrado para ser circulo

```css
/* La imagen es 200x100px (rectangular) */
.card_img {
    border-radius: 50%;    /* Esto crea un OVALO, no un circulo */
}

/* Solucion: forzar dimensiones iguales */
.card_img {
    width: 100px;
    height: 100px;
    object-fit: cover;     /* Recorta la imagen para llenar el cuadrado */
    border-radius: 50%;    /* Ahora SI es un circulo perfecto */
}
```

---

### Error 4: box-shadow con color solido negro en lugar de semitransparente

```css
/* Funciona pero es agresivo */
.card {
    box-shadow: 0 4px 10px #000000;   /* Negro puro, opaco */
}

/* Mejor: usar rgba para suavizar */
.card {
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);   /* Negro al 30% */
}
```

En el ejercicio se usa `#000000` con un blur de `25px`, lo que crea un
efecto de resplandor intenso. Para sombras mas sutiles, usa `rgba()`.

---

### Error 5: Nombres de clase que describen apariencia en vez de funcion

```css
/* MAL: si cambias el color, el nombre pierde sentido */
.red-background-card { ... }
.small-text-12px { ... }
.float-left-box { ... }

/* MEJOR: nombres que describen FUNCION */
.card--danger { ... }      /* "peligro" = rojo, pero el nombre no depende del color */
.card__caption { ... }     /* "caption" describe el ROL del texto */
.sidebar { ... }           /* "lateral" describe la POSICION semantica */
```

Nota: en el ejercicio usamos `.red-card`, `.blue-card`, etc. por simplicidad
didactica. En un proyecto real, nombres como `.card--primary`,
`.card--secondary`, `.card--success` son mas mantenibles.

---

## 8. Ejercicios de practica

Todos los ejercicios se basan en los archivos `index.html` y `styles.css`
de esta carpeta. Abre `index.html` en tu navegador y edita `styles.css`.

### Ejercicio 1 — Nueva variante de color
Crea una cuarta tarjeta con clase `.yellow-card` que tenga un gradiente
de negro a amarillo dorado (`#d4a842`).

**Pasos:**
1. Copia un `<article>` existente en `index.html` y cambia la clase.
2. Agrega la regla `.yellow-card` en `styles.css`.
3. Verifica que el texto sea legible sobre el nuevo fondo (contraste).

---

### Ejercicio 2 — Sombra al hacer hover
Agrega un efecto donde la sombra de las tarjetas AUMENTE cuando el
usuario pase el cursor sobre ellas (hover).

```css
.card:hover {
    box-shadow: 0 0 40px 5px rgba(0, 0, 0, 0.8);
    /* Agrega tambien una transicion suave: */
    transition: box-shadow 0.3s ease;
}
/* Pon la transition tambien en .card (no solo en :hover)
   para que la animacion funcione en ambas direcciones. */
```

---

### Ejercicio 3 — Gradiente diagonal
Cambia el gradiente de `.red-card` para que vaya en diagonal
(de la esquina superior izquierda a la inferior derecha):

```css
.red-card {
    background: linear-gradient(to bottom right, #000000, #d84242);
}
```

Experimenta con otros angulos: `45deg`, `135deg`, `to right`.

---

### Ejercicio 4 — Gradiente de tres colores
Modifica `.blue-card` para que tenga un gradiente con tres paradas
de color: negro arriba, azul en el medio, y negro abajo.

**Pista:** `linear-gradient(#000 0%, #242a92 50%, #000 100%)`

---

### Ejercicio 5 — Tarjeta horizontal
Redisena la tarjeta para que en pantallas grandes (min-width: 768px),
la imagen este a la IZQUIERDA y el texto a la DERECHA, en una fila.

**Pistas:**
- Agrega `display: flex` a `.card` dentro de una media query.
- Usa `flex-direction: row` y `align-items: center`.
- La imagen necesitara un ancho fijo y el texto `flex: 1`.

---

### Ejercicio 6 — Verificar contrastes
Usando la herramienta de WebAIM (https://webaim.org/resources/contrastchecker/):

1. Verifica el contraste de `.card` (color: `#f0f0f0` sobre fondo
   gradiente `#d84242`). Pasa AA?
2. Verifica el contraste de `body` (color: `#1a1a1a` sobre `beige`).
3. Si alguno falla, propone un color alternativo que pase.

---

### Ejercicio 7 — Sombra inset
Agrega una sombra **interior** (inset) a las tarjetas que cree un efecto
de profundidad como si el borde superior estuviera iluminado:

```css
.card {
    box-shadow:
        0 0 25px 0 #000000,                    /* sombra exterior original */
        inset 0 2px 4px rgba(255,255,255,0.2);  /* luz interior arriba */
}
```

---

### Ejercicio 8 — Nomenclatura BEM estricta
Renombra todas las clases del ejercicio para seguir BEM estricto:

```
  ACTUAL            ->  BEM ESTRICTO
  .card                 .card
  .card_img             .card__img
  .card_title           .card__title
  .card_subtitle        .card__subtitle
  .card_content         .card__content
  .red-card             .card--red
  .blue-card            .card--blue
  .green-card           .card--green
  .cards-container      .cards-container (este ya esta bien)
```

Actualiza tanto el HTML como el CSS. Verifica que todo siga funcionando.

---

> **Modulo anterior:** `04-flexbox-dados/CONCEPTOS.md` — Flexbox
> **Siguiente modulo:** `06-responsive-fundamentos/CONCEPTOS.md` — Diseno Responsive

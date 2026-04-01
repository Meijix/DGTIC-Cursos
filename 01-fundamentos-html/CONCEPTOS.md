# Modulo 01 -- Fundamentos de HTML

> **Archivo de referencia:** `index.html` en esta misma carpeta.
> Abre ese archivo en tu navegador y en tu editor de texto simultaneamente
> para ver como cada concepto se aplica en la practica.

---

## Indice

1. [Que es HTML](#1-que-es-html)
2. [Anatomia de un documento HTML](#2-anatomia-de-un-documento-html)
3. [Elementos semanticos vs presentacionales](#3-elementos-semanticos-vs-presentacionales)
4. [Formularios: la puerta de entrada de datos](#4-formularios-la-puerta-de-entrada-de-datos)
5. [Jerarquia de encabezados](#5-jerarquia-de-encabezados)
6. [Listas en HTML](#6-listas-en-html)
7. [Accesibilidad (a11y) fundamentals](#7-accesibilidad-a11y)
8. [Errores comunes](#8-errores-comunes)
9. [Ejercicios de practica](#9-ejercicios-de-practica)

---

## 1. Que es HTML

### HTML es un lenguaje de MARCADO, no de programacion

Esta distincion es fundamental y aparece constantemente en entrevistas tecnicas.

| Caracteristica              | Lenguaje de marcado (HTML)       | Lenguaje de programacion (JS, Python) |
|-----------------------------|----------------------------------|---------------------------------------|
| Define estructura           | Si                               | No directamente                       |
| Tiene logica (if/else)      | No                               | Si                                    |
| Tiene bucles (for/while)    | No                               | Si                                    |
| Manipula datos              | No                               | Si                                    |
| Puede tomar decisiones      | No                               | Si                                    |
| Se "ejecuta"                | No, se interpreta/renderiza      | Si, se ejecuta paso a paso            |

HTML **describe** contenido. Le dice al navegador "esto es un parrafo", "esto es un enlace",
"esto es una imagen". Pero no puede decir "si el usuario tiene mas de 18 anios, muestra esto".

### La analogia del cuerpo humano

```
  HTML = El esqueleto           CSS = La piel y la ropa        JS = Los musculos
  (estructura)                  (presentacion)                 (comportamiento)

  ┌──────────┐                  ┌──────────┐                   ┌──────────┐
  │  <head>  │                  │ colores  │                   │ onclick  │
  │  <body>  │                  │ fuentes  │                   │ fetch()  │
  │  <h1>    │                  │ layout   │                   │ if/else  │
  │  <p>     │                  │ animacion│                   │ loops    │
  │  <img>   │                  │ sombras  │                   │ eventos  │
  └──────────┘                  └──────────┘                   └──────────┘
  Sin CSS ni JS, el HTML        Sin HTML, CSS no tiene          Sin HTML, JS no tiene
  sigue siendo funcional        nada que estilizar              nada que manipular
  (se ve feo pero FUNCIONA)
```

> **Punto clave:** El archivo `index.html` de este modulo no tiene CSS a proposito.
> Lo que ves en el navegador son los **estilos por defecto** del navegador (llamados
> "user-agent stylesheet"). Esto demuestra que HTML es funcional por si solo.

### Breve historia: de HTML 1.0 a HTML5

```
  1991        1995        1997        1999        2014        Hoy
   │           │           │           │           │           │
   ▼           ▼           ▼           ▼           ▼           ▼
  HTML 1.0    HTML 2.0    HTML 3.2    HTML 4.01   HTML5       HTML
  (Tim         (RFC        (Tablas,    (CSS se     (Video,     (Living
  Berners-     oficial)    frames)     separa)     audio,      Standard)
  Lee)                                             canvas,
                                                   semantica)
```

**Por que HTML5 importa:**

- Antes de HTML5, para poner un video necesitabas Flash (un plugin externo
  que era lento, inseguro y no funcionaba en moviles).
- HTML5 introdujo `<video>`, `<audio>`, `<canvas>` de forma nativa.
- Agrego elementos semanticos: `<header>`, `<nav>`, `<main>`, `<footer>`,
  `<section>`, `<article>`, `<aside>`. Antes todo era `<div>`.
- Nuevos tipos de input: `email`, `date`, `color`, `range`, etc.
- API de geolocalizacion, almacenamiento local, web workers.

**HTML ya no tiene "versiones":** Desde 2019, la especificacion se llama
simplemente "HTML" y es un **Living Standard** (estandar vivo) mantenido
por WHATWG. Se actualiza continuamente sin numeros de version.

---

## 2. Anatomia de un documento HTML

### Estructura minima obligatoria

```html
<!doctype html>                 <!-- 1. Instruccion para el navegador -->
<html lang="es">                <!-- 2. Elemento raiz -->
  <head>                        <!-- 3. Metadatos (no visibles) -->
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mi pagina</title>
  </head>
  <body>                        <!-- 4. Contenido visible -->
    <h1>Hola mundo</h1>
    <p>Mi primer parrafo.</p>
  </body>
</html>
```

### El arbol DOM (Document Object Model)

Cuando el navegador lee tu HTML, construye en memoria una estructura de arbol
llamada **DOM**. Cada etiqueta se convierte en un **nodo** del arbol:

```
                        document
                           │
                       <!doctype html>
                           │
                        <html>
                       ┌───┴───┐
                    <head>   <body>
                   ┌──┼──┐     ┌──────┼──────────┐
                <meta> <meta> <title>  │          │
                              │     <header>   <main>
                          "Mi pagina"   │      ┌──┼──┐
                                  "HeaderNat" <h1> <section> <aside>
                                                     │         │
                                                  <article>   <dl>
                                                     │
                                                   <form>
```

> **Asi se ve el DOM del archivo `index.html`** de este modulo (simplificado).
> Puedes verlo tu mismo abriendo las DevTools del navegador (F12) > pestania Elements.

### Relaciones en el arbol DOM

```
  <html>                          TERMINOLOGIA:
    ├── <head>                    ─────────────
    │     ├── <meta>              <html> es PADRE de <head> y <body>
    │     ├── <meta>              <head> y <body> son HIJOS de <html>
    │     └── <title>             <head> y <body> son HERMANOS entre si
    └── <body>                    <meta> es DESCENDIENTE de <html>
          ├── <header>            <html> es ANCESTRO de <meta>
          ├── <nav>
          │     └── <ul>
          │           ├── <li>
          │           ├── <li>
          │           ├── <li>
          │           └── <li>
          ├── <main>
          │     ├── <h1>
          │     ├── <section>
          │     └── <aside>
          └── <footer>
```

Estas relaciones importan para:
- **CSS:** Los selectores descendientes (`nav li`) dependen de esta jerarquia.
- **JavaScript:** `parentNode`, `children`, `querySelector` navegan el arbol.
- **Accesibilidad:** Los lectores de pantalla recorren el arbol en orden.

### head vs body

```
  ┌─────────────────────────────────────────────────────────────┐
  │  <head> -- Metadatos (NO se ven en pantalla)                │
  │                                                             │
  │  Lo que va aqui:                   Lo que NO va aqui:       │
  │  ✓ <meta charset>                  ✗ Textos visibles        │
  │  ✓ <meta viewport>                 ✗ Imagenes               │
  │  ✓ <meta description>              ✗ Formularios            │
  │  ✓ <title>                         ✗ Enlaces de navegacion  │
  │  ✓ <link> (CSS, favicon)           ✗ Encabezados (h1-h6)   │
  │  ✓ <script> (JavaScript)                                    │
  │  ✓ Open Graph tags (redes sociales)                         │
  ├─────────────────────────────────────────────────────────────┤
  │  <body> -- Contenido visible (lo que el usuario VE)         │
  │                                                             │
  │  Lo que va aqui:                   Lo que NO va aqui:       │
  │  ✓ Textos, parrafos               ✗ <meta> tags            │
  │  ✓ Imagenes, videos               ✗ <title>                │
  │  ✓ Formularios                     ✗ <link rel="stylesheet">│
  │  ✓ Enlaces y navegacion                                     │
  │  ✓ Toda la estructura semantica                             │
  └─────────────────────────────────────────────────────────────┘
```

### Meta tags esenciales

| Meta tag                  | Que hace                                              | Que pasa si falta                                      |
|---------------------------|-------------------------------------------------------|--------------------------------------------------------|
| `<meta charset="UTF-8">`  | Define la codificacion de caracteres                  | Caracteres rotos: "Ã±" en lugar de "n"                 |
| `<meta name="viewport">` | Controla el zoom en moviles                           | Todo se ve diminuto en celulares                       |
| `<meta name="description">` | Texto que Google muestra en resultados             | Google inventa un snippet (puede ser malo)             |
| `<title>`                 | Texto en la pestania del navegador                    | Pestania dice la URL del archivo (feo)                 |

> **Revisa en `index.html`:** las lineas 158, 188, 203 y 235 muestran cada uno
> de estos meta tags con comentarios detallados sobre su funcionamiento.

---

## 3. Elementos semanticos vs presentacionales

### El gran diagrama: layout con elementos semanticos

```
  ┌──────────────────────────────────────────────────────────────┐
  │                        <header>                              │
  │  Logo del sitio, titulo, subtitulo                           │
  │  Rol implicito: "banner"                                     │
  ├──────────────────────────────────────────────────────────────┤
  │                         <nav>                                │
  │  Inicio | Nosotros | Servicios | Contacto                   │
  │  Rol implicito: "navigation"                                 │
  ├───────────────────────────────────┬──────────────────────────┤
  │                                   │                          │
  │             <main>                │        <aside>           │
  │  Rol implicito: "main"           │  Rol: "complementary"    │
  │                                   │                          │
  │  ┌─── <section> ──────────────┐  │  Contenido lateral:      │
  │  │  Rol: "region"             │  │  - Glosario              │
  │  │  (con aria-labelledby)     │  │  - Enlaces relacionados  │
  │  │                            │  │  - Publicidad            │
  │  │  ┌── <article> ─────────┐ │  │                          │
  │  │  │  Contenido            │ │  │                          │
  │  │  │  independiente        │ │  │                          │
  │  │  │  (post, producto,    │ │  │                          │
  │  │  │   comentario)        │ │  │                          │
  │  │  └──────────────────────┘ │  │                          │
  │  └────────────────────────────┘  │                          │
  │                                   │                          │
  ├───────────────────────────────────┴──────────────────────────┤
  │                        <footer>                              │
  │  Copyright, enlaces legales, contacto, redes sociales        │
  │  Rol implicito: "contentinfo"                                │
  └──────────────────────────────────────────────────────────────┘
```

### Tabla completa de elementos semanticos

| Elemento      | Proposito                                      | Rol ARIA implicito          | Puede haber multiples? |
|---------------|------------------------------------------------|-----------------------------|------------------------|
| `<header>`    | Encabezado del sitio o de una seccion          | `banner` (solo en `<body>`) | Si                     |
| `<nav>`       | Bloque principal de navegacion                 | `navigation`                | Si                     |
| `<main>`      | Contenido principal y unico de la pagina       | `main`                      | No (solo 1 visible)    |
| `<section>`   | Agrupacion tematica de contenido               | `region` (con etiqueta)     | Si                     |
| `<article>`   | Contenido independiente y auto-contenido       | `article`                   | Si                     |
| `<aside>`     | Contenido tangencialmente relacionado          | `complementary`             | Si                     |
| `<footer>`    | Pie de pagina del sitio o de una seccion       | `contentinfo` (en `<body>`) | Si                     |
| `<figure>`    | Contenido ilustrativo (imagen + pie de imagen) | `figure`                    | Si                     |
| `<figcaption>`| Pie de un `<figure>`                           | (ninguno)                   | 1 por `<figure>`       |
| `<details>`   | Contenido expandible/colapsable                | `group`                     | Si                     |
| `<summary>`   | Titulo visible de un `<details>`               | (ninguno)                   | 1 por `<details>`      |
| `<time>`      | Fecha/hora legible por maquinas                | `time`                      | Si                     |
| `<address>`   | Informacion de contacto                        | `group`                     | Si                     |
| `<mark>`      | Texto resaltado/marcado                        | (ninguno)                   | Si                     |

### Diagrama de decision: section vs article vs div

```
  Quieres agrupar contenido?
         │
         ▼
  Tiene sentido por si solo,
  fuera de la pagina?
  (Si lo pegaras en otro sitio,
  se entenderia?)
         │
    ┌────┴────┐
    │ SI      │ NO
    ▼         ▼
  <article>   Tiene un TEMA
              comun con un
              encabezado?
                  │
             ┌────┴────┐
             │ SI      │ NO
             ▼         ▼
          <section>   <div>
```

**Ejemplos practicos:**

| Contenido                        | Elemento correcto | Por que                                       |
|----------------------------------|-------------------|-----------------------------------------------|
| Un post de blog completo         | `<article>`       | Se entiende solo, se podria publicar aparte    |
| Un comentario de usuario         | `<article>`       | Es una unidad independiente de contenido       |
| "Capitulo 3: Variables"          | `<section>`       | Es parte de algo mas grande (un tutorial)      |
| Un grupo de cards para CSS Grid  | `<div>`           | Solo necesitas un contenedor, sin significado  |
| Una barra lateral con anuncios   | `<aside>`         | Contenido tangencial, removible sin afectar    |

---

## 4. Formularios: la puerta de entrada de datos

### Como funciona un formulario (flujo completo)

```
  NAVEGADOR (cliente)                          SERVIDOR
  ┌───────────────────┐                        ┌───────────────┐
  │                   │   1. Usuario llena      │               │
  │  ┌─────────────┐  │      los campos         │               │
  │  │ Nombre: Ana │  │                        │               │
  │  │ Email: a@b  │  │   2. Clic en "Enviar"  │               │
  │  │ [Enviar]    │  │ ─────────────────────> │  3. Recibe    │
  │  └─────────────┘  │                        │  los datos:   │
  │                   │   HTTP POST /procesar   │  nombre=Ana   │
  │                   │   nombre=Ana&email=a@b  │  email=a@b    │
  │                   │                        │               │
  │                   │ <───────────────────── │  4. Responde  │
  │  5. Muestra       │   200 OK               │  (exito/error)│
  │     resultado     │   "Datos guardados"    │               │
  └───────────────────┘                        └───────────────┘
```

### Tabla de tipos de input

| type         | Que valida automaticamente        | Teclado en movil                | Ejemplo de uso             |
|-------------|-----------------------------------|---------------------------------|----------------------------|
| `text`      | Nada                              | Teclado completo                | Nombre, ciudad             |
| `email`     | Debe tener @ y dominio            | Teclado con @ y .com            | Correo electronico         |
| `password`  | Nada (oculta caracteres)          | Teclado completo                | Contrasenas                |
| `number`    | Solo numeros                      | Teclado numerico                | Edad, cantidad             |
| `tel`       | Nada (formatos varian)            | Teclado telefonico (0-9, +, #) | Numero de telefono         |
| `url`       | Debe tener protocolo (http://)    | Teclado con / y .com            | Sitio web                  |
| `date`      | Fecha valida                      | Selector de fecha nativo        | Fecha de nacimiento        |
| `time`      | Hora valida                       | Selector de hora                | Hora de cita               |
| `color`     | Color hexadecimal                 | Selector de color nativo        | Color favorito             |
| `range`     | Valor dentro de min-max           | Slider deslizable               | Volumen, brillo            |
| `search`    | Nada (icono de limpiar)           | Teclado con "Buscar"            | Barra de busqueda          |
| `checkbox`  | Booleano (si/no)                  | Casilla de verificacion         | Acepto terminos            |
| `radio`     | Una opcion del grupo              | Boton circular                  | Genero, procedencia        |
| `file`      | Tipo de archivo (con accept)      | Selector de archivos            | Subir foto                 |
| `hidden`    | Nada (invisible)                  | (no se muestra)                 | Token CSRF, IDs            |
| `submit`    | (es boton, no campo)              | (es boton)                      | Enviar formulario          |

### La conexion label-for-id

```
        <label for="nombre">Nombre:</label>
                    │
                    │  El valor de "for"
                    │  debe ser IDENTICO
                    │  al valor de "id"
                    │
                    ▼
        <input type="text" id="nombre" name="nombre">
                           │            │
                           │            └── name: clave que se envia al servidor
                           │                      (nombre=valor_que_escribio_el_usuario)
                           │
                           └── id: identificador unico en TODO el documento
                                   (conecta con el "for" del label)
```

**Tres beneficios de esta conexion:**

1. **Lectores de pantalla:** Al llegar al input, anuncian "Nombre, campo de texto"
   en lugar de solo "campo de texto".
2. **Area de clic ampliada:** Hacer clic en el texto "Nombre:" activa el campo.
   Crucial en dispositivos tactiles.
3. **Pruebas de accesibilidad:** Herramientas como Lighthouse y axe marcan inputs
   sin label conectado como error critico.

### Fieldset y legend: agrupacion accesible

```
  ┌─── <fieldset> ─────────────────────────────────────────┐
  │ Proporciona tus datos         <-- <legend>             │
  │                                                        │
  │  Nombre:  [_______________]                            │
  │  Email:   [_______________]                            │
  │                                                        │
  │  ┌─── <fieldset> (anidado) ─────────────────────────┐  │
  │  │ Procedencia:              <-- <legend>           │  │
  │  │  ( ) Mexicano                                    │  │
  │  │  ( ) Extranjero                                  │  │
  │  └──────────────────────────────────────────────────┘  │
  │                                                        │
  │  Sabor favorito: [▼ Elija una opcion ]                 │
  └────────────────────────────────────────────────────────┘
```

> **En `index.html`:** Observa como el fieldset de "Procedencia" (linea 604)
> esta anidado dentro del fieldset principal (linea 506). El lector de pantalla
> anuncia el legend ANTES de cada campo dentro del fieldset.

### Radio buttons vs checkboxes

```
  RADIO BUTTONS                        CHECKBOXES
  (seleccion UNICA)                    (seleccion MULTIPLE)

  Procedencia:                         Idiomas que hablas:
  (●) Mexicano                         [✓] Espaniol
  ( ) Extranjero                       [✓] Ingles
                                       [ ] Frances
  Solo UNO puede estar                 VARIOS pueden estar
  seleccionado.                        seleccionados.

  Se agrupan por NAME:                 Cada uno tiene NAME diferente
  name="procedencia" en ambos          (o name="idiomas[]" en arrays)

  Al seleccionar uno,                  Seleccionar uno NO afecta
  el otro se DESELECCIONA              a los demas
```

---

## 5. Jerarquia de encabezados

### El "indice" del documento

Los encabezados h1-h6 crean una jerarquia similar al indice de un libro.
Los lectores de pantalla permiten navegar saltando entre encabezados,
por eso el orden importa.

```
  CORRECTO                              INCORRECTO
  ─────────                             ──────────

  h1: Mi sitio web                      h1: Mi sitio web
  ├── h2: Servicios                     ├── h3: Servicios      ← Salto h1 a h3!
  │   ├── h3: Diseno web                │   ├── h5: Diseno web ← Salto h3 a h5!
  │   └── h3: Marketing                 │   └── h2: Marketing  ← h2 dentro de h3?
  ├── h2: Equipo                        ├── h4: Equipo         ← Desorden total
  │   └── h3: Directivos                └── h1: Contacto       ← Dos h1!
  └── h2: Contacto
```

### Reglas de encabezados

| Regla                                    | Explicacion                                                       |
|------------------------------------------|-------------------------------------------------------------------|
| Solo un `<h1>` por pagina                | Es el titulo principal, el tema general de la pagina              |
| No saltar niveles                        | Despues de h1 viene h2, no h3 ni h4                               |
| h2 para secciones principales            | Los grandes bloques de contenido                                  |
| h3 para sub-secciones                    | Detalles dentro de una seccion h2                                 |
| h4-h6 para sub-sub-secciones             | Rara vez necesarios; si llegas a h5 o h6, replantea la estructura |
| Los encabezados no son para "texto grande"| Si quieres texto grande, usa CSS. Un h3 no es "un parrafo grande" |

> **En `index.html`:** Observa la jerarquia en el `<main>` (linea 413):
> h1 > h2 (seccion 1) > h3 (articulo 1). El h3 en el aside (linea 660)
> es discutible -- si el aside es un bloque independiente al mismo nivel
> que section, podria ser h2.

---

## 6. Listas en HTML

### Tres tipos de lista, tres propositos

```
  <ul> Lista desordenada             <ol> Lista ordenada              <dl> Lista de definicion
  ───────────────────                ──────────────────               ────────────────────────

  * Leche                            1. Precalentar horno             Termino 1
  * Huevos                           2. Mezclar ingredientes            La definicion 1
  * Harina                           3. Hornear 30 min                Termino 2
                                                                       La definicion 2
  El ORDEN no importa.               El ORDEN importa.                Pares termino-definicion.
  Si reordenas, el                   Si reordenas, la receta          Glosarios, FAQs,
  significado no cambia.             sale MAL.                        metadatos clave-valor.
```

### Guia de decision

```
  Necesitas una lista?
         │
         ▼
  Los items son PARES de
  termino + definicion?
  (glosario, FAQ, metadatos)
         │
    ┌────┴────┐
    │ SI      │ NO
    ▼         ▼
   <dl>    Importa el ORDEN
           de los items?
               │
          ┌────┴────┐
          │ SI      │ NO
          ▼         ▼
         <ol>      <ul>
```

### Ejemplo de dl/dt/dd (como en `index.html` linea 694)

```html
<dl>
  <dt>HTML</dt>
  <dd>Lenguaje de marcado para estructurar contenido web.</dd>

  <dt>CSS</dt>
  <dd>Lenguaje de estilos para la presentacion visual.</dd>

  <dt>JavaScript</dt>
  <dd>Lenguaje de programacion para interactividad.</dd>
  <dd>Tambien se usa en el servidor con Node.js.</dd>   <!-- Un termino, DOS definiciones -->
</dl>
```

> **Dato avanzado:** Un `<dt>` puede tener multiples `<dd>` (varias definiciones
> para un mismo termino), y varios `<dt>` pueden compartir un mismo `<dd>`.

---

## 7. Accesibilidad (a11y)

> "a11y" es la abreviacion de "accessibility" (a + 11 letras + y).

### La primera regla de ARIA

> "La primera regla de ARIA es: **NO uses ARIA** si puedes usar
> HTML semantico nativo." -- W3C WAI-ARIA Authoring Practices

**Que significa esto:** Antes de agregar `role="banner"` a un `<div>`,
preguntate si puedes usar `<header>` directamente. El elemento semantico
ya tiene el rol integrado.

### Roles implicitos de los elementos semanticos

| Elemento HTML          | Rol ARIA implicito | Condicion                              |
|------------------------|--------------------|----------------------------------------|
| `<header>`             | `banner`           | Solo cuando es hijo directo de `<body>` |
| `<nav>`                | `navigation`       | Siempre                                |
| `<main>`               | `main`             | Siempre                                |
| `<footer>`             | `contentinfo`      | Solo cuando es hijo directo de `<body>` |
| `<aside>`              | `complementary`    | Siempre                                |
| `<section>`            | `region`           | Solo con `aria-label` o `aria-labelledby` |
| `<article>`            | `article`          | Siempre                                |
| `<form>`               | `form`             | Solo con nombre accesible               |
| `<a href="...">`       | `link`             | Solo cuando tiene href                 |
| `<button>`             | `button`           | Siempre                                |
| `<input type="text">`  | `textbox`          | Siempre                                |
| `<input type="checkbox">` | `checkbox`      | Siempre                                |
| `<input type="radio">` | `radio`            | Siempre                                |
| `<select>`             | `combobox`         | Siempre                                |
| `<img alt="...">`      | `img`              | Cuando tiene alt con texto             |
| `<img alt="">`         | `presentation`     | Cuando alt esta vacio                  |
| `<ul>`, `<ol>`         | `list`             | Siempre                                |
| `<li>`                 | `listitem`         | Siempre                                |
| `<h1>` - `<h6>`        | `heading`          | Siempre (con aria-level correspondiente)|

### Por que el HTML semantico ES accesibilidad

```
  CON HTML semantico:                   CON <div> para todo:
  ──────────────────                    ────────────────────

  <nav>                                 <div class="nav">
    <ul>                                  <div>
      <li><a href="#">Inicio</a></li>       <span onclick="go()">Inicio</span>
    </ul>                                 </div>
  </nav>                                </div>

  Lector de pantalla dice:              Lector de pantalla dice:
  "Navegacion, lista, 4 elementos,     "Inicio"
   Inicio, enlace"                      (Y nada mas. No sabe que es nav,
                                         no sabe que hay 4 opciones,
  El usuario SABE:                       no sabe que es un enlace.)
  - Que es una navegacion
  - Que hay 4 opciones                  El usuario esta PERDIDO.
  - Que "Inicio" es un enlace
  - Puede saltar con atajos
```

### Cuando SI se necesita ARIA

1. **Multiples `<nav>`:** Usa `aria-label` para distinguirlos.
   ```html
   <nav aria-label="Navegacion principal">...</nav>
   <nav aria-label="Navegacion del pie de pagina">...</nav>
   ```

2. **`<section>` sin nombre:** Agrega `aria-labelledby` apuntando a su encabezado.
   ```html
   <section aria-labelledby="sec1-heading">
     <h2 id="sec1-heading">Mis servicios</h2>
   </section>
   ```

3. **Widgets complejos:** Tabs, carruseles, modales -- cosas que HTML nativo
   no tiene. Ahi si necesitas ARIA roles, states y properties.

---

## 8. Errores comunes

### Error 1: Olvidar cerrar etiquetas

```html
  <!-- MAL -->
  <p>Primer parrafo
  <p>Segundo parrafo

  <!-- BIEN -->
  <p>Primer parrafo</p>
  <p>Segundo parrafo</p>
```

El navegador "adivina" donde cerrar, pero puede adivinar mal y romper tu layout.

### Error 2: Usar `<br>` para espaciado

```html
  <!-- MAL: Usar <br> como si fuera margin -->
  <p>Parrafo 1</p>
  <br><br><br>
  <p>Parrafo 2</p>

  <!-- BIEN: Usar CSS para espaciado -->
  <p class="con-margen">Parrafo 1</p>
  <p>Parrafo 2</p>
  <!-- En CSS: .con-margen { margin-bottom: 2rem; } -->
```

`<br>` es para saltos de linea DENTRO de texto (como una direccion o un poema),
no para crear espacio entre elementos.

### Error 3: Usar `<div>` para todo (la "divitis")

```html
  <!-- MAL: Divitis -->
  <div class="header">
    <div class="nav">
      <div class="nav-item"><a href="#">Inicio</a></div>
    </div>
  </div>

  <!-- BIEN: HTML semantico -->
  <header>
    <nav>
      <ul>
        <li><a href="#">Inicio</a></li>
      </ul>
    </nav>
  </header>
```

### Error 4: Omitir el alt en imagenes

```html
  <!-- MAL -->
  <img src="foto.jpg">

  <!-- MAL (alt vacio cuando la imagen SI tiene contenido informativo) -->
  <img src="grafica-ventas.jpg" alt="">

  <!-- BIEN -->
  <img src="foto.jpg" alt="Equipo de trabajo en la oficina central">

  <!-- BIEN (imagen decorativa que no aporta informacion) -->
  <img src="linea-decorativa.svg" alt="">
```

### Error 5: Saltar niveles de encabezado

```html
  <!-- MAL -->
  <h1>Mi sitio</h1>
  <h3>Servicios</h3>    <!-- Salto de h1 a h3! Donde esta h2? -->
  <h5>Diseno web</h5>   <!-- Salto de h3 a h5! -->

  <!-- BIEN -->
  <h1>Mi sitio</h1>
  <h2>Servicios</h2>
  <h3>Diseno web</h3>
```

### Error 6: Confundir id y class

```html
  <!-- MAL: id repetido (id DEBE ser unico en todo el documento) -->
  <p id="destacado">Parrafo 1</p>
  <p id="destacado">Parrafo 2</p>

  <!-- BIEN: class puede repetirse -->
  <p class="destacado">Parrafo 1</p>
  <p class="destacado">Parrafo 2</p>
```

### Error 7: Usar placeholder en lugar de label

```html
  <!-- MAL: Sin label, solo placeholder -->
  <input type="text" placeholder="Nombre">

  <!-- BIEN: Label conectado + placeholder complementario -->
  <label for="nombre">Nombre:</label>
  <input type="text" id="nombre" placeholder="Ej: Maria Lopez">
```

---

## 9. Ejercicios de practica

### Ejercicio 1: Estructura basica (Principiante)

Crea un documento HTML desde cero (sin copiar) que tenga:
- DOCTYPE, html con lang, head con charset/viewport/title, body
- Un `<header>` con el nombre de tu sitio
- Un `<nav>` con 3 enlaces (pueden apuntar a "#")
- Un `<main>` con un h1 y dos parrafos
- Un `<footer>` con texto de copyright

**Validacion:** Abre tu archivo en https://validator.w3.org/ y corrige todos los errores.

### Ejercicio 2: Formulario accesible (Intermedio)

Crea un formulario de registro con:
- Un `<fieldset>` con `<legend>` "Datos personales"
- Campos: nombre (text), email (email), telefono (tel), fecha de nacimiento (date)
- Cada campo DEBE tener `<label>` conectado con for/id
- Un `<fieldset>` anidado con `<legend>` "Genero" y radio buttons (masculino/femenino/otro)
- Un `<select>` para pais con al menos 5 opciones
- Un boton de envio

**Verificacion:** Con el navegador, haz clic en cada label y verifica que activa su campo.

### Ejercicio 3: Pagina semantica completa (Avanzado)

Recrea la estructura del archivo `index.html` de este modulo **desde cero, sin mirar el original**.
Tu pagina debe tener:
- Todos los elementos semanticos: header, nav, main, section, article, aside, footer
- Una lista de definicion (`<dl>`) en el aside
- Un formulario con fieldset, radio buttons y select
- Jerarquia correcta de encabezados (h1 > h2 > h3)
- `aria-label` en el nav y `aria-labelledby` en la section

**Despues de terminar:** Compara tu version con `index.html`. Identifica las diferencias
y reflexiona sobre las decisiones que tomaste.

### Ejercicio 4: Auditoria de accesibilidad (Investigacion)

1. Abre el archivo `index.html` en Chrome
2. Abre DevTools (F12) > pestania Lighthouse
3. Ejecuta una auditoria de "Accessibility"
4. Documenta: Que puntaje obtuviste? Que mejoras sugiere?
5. Implementa las correcciones sugeridas y vuelve a ejecutar la auditoria

---

## Para profundizar

### El algoritmo de parsing de HTML

El navegador no ejecuta HTML linea por linea como un programa. En cambio:

1. **Tokenizacion:** Convierte el texto en tokens (`<`, `div`, `>`, texto, `</`, `div`, `>`).
2. **Construccion del arbol:** Los tokens se insertan en el arbol DOM siguiendo
   reglas complejas. Por ejemplo, si encuentras un `<p>` dentro de otro `<p>`,
   el parser automaticamente cierra el primer `<p>` antes de abrir el segundo.
3. **Correccion de errores:** HTML es MUY tolerante. Si olvidas cerrar un `<div>`,
   el parser intenta corregirlo. Esto es intencional (a diferencia de XML, que
   rechaza el documento si tiene un solo error).

### Content categories (categorias de contenido)

HTML5 reemplazo las categorias "block" e "inline" con un sistema mas complejo:

| Categoria         | Que incluye                              | Ejemplo                     |
|-------------------|------------------------------------------|-----------------------------|
| Flow content      | La mayoria de elementos en `<body>`      | `<div>`, `<p>`, `<table>`   |
| Phrasing content  | Texto y elementos que van dentro de texto| `<span>`, `<a>`, `<strong>` |
| Heading content   | Encabezados                              | `<h1>` - `<h6>`             |
| Sectioning content| Crean secciones en el outline            | `<article>`, `<section>`, `<nav>`, `<aside>` |
| Embedded content  | Contenido externo embebido               | `<img>`, `<video>`, `<iframe>` |
| Interactive content| Elementos con los que el usuario interactua| `<a>`, `<button>`, `<input>` |
| Metadata content  | Metadatos del documento                  | `<meta>`, `<link>`, `<title>` |

Estas categorias determinan que elementos pueden contener a otros. Por ejemplo,
`<p>` solo puede contener "phrasing content", por eso no puedes meter un `<div>`
dentro de un `<p>` (el parser automaticamente cierra el `<p>`).

### Void elements (elementos vacios)

Algunos elementos HTML **nunca** tienen contenido ni etiqueta de cierre:

```
  <meta>     <link>     <br>       <hr>
  <img>      <input>    <source>   <track>
  <area>     <base>     <col>      <embed>
  <wbr>
```

Escribir `<br />` con la barra es valido pero innecesario en HTML5.
Es un vestigio de XHTML donde era obligatorio.

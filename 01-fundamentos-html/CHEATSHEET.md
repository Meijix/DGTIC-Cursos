# Cheatsheet — Fundamentos de HTML (Modulo 01)

## Estructura minima de un documento HTML

```html
<!doctype html>
<html lang="es">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mi pagina</title>
  </head>
  <body>
    <!-- contenido visible -->
  </body>
</html>
```

---

## Elementos semanticos -- layout tipico

```
+---------------------------------------------------------+
|                      <header>                           |
|  Logo, titulo del sitio          (banner)               |
+---------------------------------------------------------+
|                       <nav>                             |
|  Inicio | Nosotros | Contacto    (navigation)           |
+--------------------------------------+------------------+
|              <main>                  |    <aside>       |
|  (unico por pagina)                 | Contenido lateral|
|                                      | (complementary)  |
|  +--- <section> ---------+          |                  |
|  | Tema con encabezado    |          |                  |
|  |  +--- <article> ----+ |          |                  |
|  |  | Contenido         | |          |                  |
|  |  | independiente     | |          |                  |
|  |  +-------------------+ |          |                  |
|  +------------------------+          |                  |
+--------------------------------------+------------------+
|                     <footer>                            |
|  Copyright, enlaces legales          (contentinfo)      |
+---------------------------------------------------------+
```

---

## Referencia rapida de elementos semanticos

| Elemento      | Proposito                          | Multiples? |
|---------------|------------------------------------|------------|
| `<header>`    | Encabezado del sitio o seccion     | Si         |
| `<nav>`       | Navegacion principal               | Si         |
| `<main>`      | Contenido principal de la pagina   | No (1)     |
| `<section>`   | Agrupacion tematica                | Si         |
| `<article>`   | Contenido independiente            | Si         |
| `<aside>`     | Contenido complementario           | Si         |
| `<footer>`    | Pie de pagina                      | Si         |
| `<figure>`    | Imagen + pie de imagen             | Si         |

### Decision rapida: section vs article vs div

- Se entiende SOLO fuera de la pagina? -> `<article>`
- Tiene un TEMA comun con encabezado?  -> `<section>`
- Solo necesitas un contenedor?        -> `<div>`

---

## Formularios

```html
<form action="/procesar" method="POST">
  <fieldset>
    <legend>Datos personales</legend>

    <label for="nombre">Nombre:</label>
    <input type="text" id="nombre" name="nombre" required>

    <label for="email">Email:</label>
    <input type="email" id="email" name="email">

    <button type="submit">Enviar</button>
  </fieldset>
</form>
```

### Tipos de input mas usados

| type       | Valida automaticamente   | Teclado movil      |
|------------|--------------------------|---------------------|
| `text`     | Nada                     | Completo            |
| `email`    | Requiere @ y dominio     | Con @ y .com        |
| `password` | Oculta caracteres        | Completo            |
| `number`   | Solo numeros             | Numerico            |
| `date`     | Fecha valida             | Selector de fecha   |
| `checkbox` | Booleano (si/no)         | Casilla             |
| `radio`    | Una opcion del grupo     | Boton circular      |

### Conexion label-for-id

```
<label for="nombre">       <-- for="nombre"
         |                       debe ser IDENTICO
         v                       al id del input
<input id="nombre" name="nombre">
         |                  |
         id: conecta        name: clave que se
         con el label       envia al servidor
```

---

## Listas

```html
<!-- Desordenada -->        <!-- Ordenada -->         <!-- Definicion -->
<ul>                        <ol>                      <dl>
  <li>Item</li>               <li>Primero</li>          <dt>Termino</dt>
  <li>Item</li>               <li>Segundo</li>          <dd>Definicion</dd>
</ul>                       </ol>                     </dl>
```

---

## Meta tags esenciales

| Meta tag                     | Que pasa si falta                  |
|------------------------------|------------------------------------|
| `<meta charset="UTF-8">`    | Caracteres rotos (acentos, enies)  |
| `<meta name="viewport" ...>`| Todo diminuto en celulares         |
| `<title>`                    | Pestana muestra la URL             |
| `<meta name="description">` | Google inventa un snippet           |

---

## Jerarquia de encabezados

Solo **un** `<h1>` por pagina. Nunca saltar niveles (h1 -> h3 sin h2).

```
h1  Titulo principal
 h2  Subtema A
  h3  Detalle de A
 h2  Subtema B
```

---

## Errores comunes

| Error                               | Solucion                                        |
|--------------------------------------|-------------------------------------------------|
| `<div>` para TODO                   | Usar elementos semanticos                        |
| Input sin `<label>` conectado       | Agregar `<label for="id-del-input">`             |
| `<h1>` -> `<h3>` (saltar nivel)    | Respetar la jerarquia: h1 > h2 > h3             |
| Olvidar `alt` en imagenes           | Siempre poner `alt=""` (decorativa) o descriptivo|
| Olvidar `charset="UTF-8"`          | Caracteres especiales se rompen                  |
| No cerrar etiquetas                  | Verificar que toda etiqueta abierta tenga cierre |

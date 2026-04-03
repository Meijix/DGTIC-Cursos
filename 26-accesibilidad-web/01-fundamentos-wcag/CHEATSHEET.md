# Cheatsheet — Fundamentos y WCAG

## En una frase

Usa HTML semantico para comunicar estructura, landmarks para crear regiones navegables y ARIA solo cuando HTML nativo no es suficiente.

---

## Elementos semanticos esenciales

```
<header>       → Banner del sitio (logo, titulo)
<nav>          → Bloque de navegacion
<main>         → Contenido unico de la pagina (solo 1)
<footer>       → Pie de pagina
<aside>        → Contenido complementario
<section>      → Seccion tematica (con encabezado)
<article>      → Contenido independiente
<h1> a <h6>    → Jerarquia de encabezados (sin saltos)
<button>       → Accion interactiva
<a href="..."> → Enlace de navegacion
```

---

## Landmarks y sus roles

```
┌────────────────┬──────────────────────┬────────────────────────────────┐
│ HTML           │ Rol ARIA             │ Cuantos por pagina             │
├────────────────┼──────────────────────┼────────────────────────────────┤
│ <header>       │ banner               │ 1 (hijo directo de body)       │
│ <nav>          │ navigation           │ Multiples (usar aria-label)    │
│ <main>         │ main                 │ 1                              │
│ <aside>        │ complementary        │ Multiples                      │
│ <footer>       │ contentinfo          │ 1 (hijo directo de body)       │
│ <form> +label  │ form                 │ Multiples                      │
└────────────────┴──────────────────────┴────────────────────────────────┘
```

---

## Encabezados — reglas rapidas

```
1. Solo un <h1> por pagina
2. No saltar niveles: h1 → h2 → h3 (nunca h1 → h3)
3. Cada seccion relevante debe tener un encabezado
4. No usar encabezados para estilizar — usa CSS
5. El <h1> describe el contenido principal de la pagina
```

---

## ARIA en 4 atributos

```html
role="button"              → Define QUE es el elemento
aria-label="Cerrar"        → Nombre accesible (cuando no hay texto visible)
aria-describedby="id"      → Descripcion adicional vinculada
aria-hidden="true"         → Oculta del arbol de accesibilidad
```

---

## Div soup → HTML semantico (regla rapida)

```
<div class="header">     → <header>
<div class="nav">        → <nav>
<div class="content">    → <main>
<div class="sidebar">    → <aside>
<div class="footer">     → <footer>
<div class="btn">        → <button>
<div class="link">       → <a href="...">
<div class="title">      → <h1>, <h2>, etc.
<div class="list">       → <ul> o <ol>
<div class="input-wrap"> → <fieldset>
```

---

## Errores comunes

| Error | Solucion |
|-------|----------|
| Usar `<div onclick>` como boton | Usa `<button>` nativo |
| Multiples `<h1>` en la pagina | Solo uno — el titulo principal |
| Saltar de `<h2>` a `<h4>` | Respetar la jerarquia secuencial |
| `<nav>` sin `aria-label` cuando hay multiples | Diferenciar con `aria-label="Principal"` |
| Poner `role="button"` sin teclado | ARIA no agrega comportamiento — mejor usa `<button>` |
| Ocultar contenido importante con `aria-hidden` | Solo ocultar decorativo |

---

## Regla de oro

```
1. Usa HTML semantico PRIMERO
2. Agrega ARIA solo cuando HTML no alcanza
3. Nunca uses ARIA para reemplazar un elemento nativo
```

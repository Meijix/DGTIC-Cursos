# Cheatsheet — Formularios Accesibles

## En una frase

Todo campo necesita un label asociado, los errores deben describirse y vincularse, y los campos relacionados se agrupan con fieldset/legend.

---

## Label — tres formas

```html
<!-- 1. Explicita (preferida) -->
<label for="email">Correo</label>
<input type="email" id="email">

<!-- 2. Implicita (envolvente) -->
<label>Correo <input type="email"></label>

<!-- 3. aria-label (cuando no hay label visible) -->
<input type="search" aria-label="Buscar en el sitio">
```

---

## Fieldset + Legend

```html
<fieldset>
  <legend>Genero</legend>
  <label><input type="radio" name="gen" value="m"> Masculino</label>
  <label><input type="radio" name="gen" value="f"> Femenino</label>
  <label><input type="radio" name="gen" value="o"> Otro</label>
</fieldset>
```

Usar para: grupos de radio buttons, checkboxes relacionados, secciones logicas del formulario.

---

## Errores accesibles

```html
<label for="pass">Contrasena</label>
<input type="password" id="pass"
       aria-invalid="true"
       aria-describedby="pass-err">
<p id="pass-err" role="alert">Minimo 8 caracteres.</p>
```

```
Checklist de errores:
  [x] aria-invalid="true" en el campo con error
  [x] Mensaje vinculado con aria-describedby
  [x] role="alert" para anuncio inmediato
  [x] Texto descriptivo (no solo "Error")
  [x] No depender solo del color rojo
  [x] Foco al primer campo con error
```

---

## Campos requeridos

```html
<label for="nombre">Nombre <span aria-hidden="true">*</span></label>
<input type="text" id="nombre" required aria-required="true">
```

Indicar al inicio: "Los campos con * son obligatorios."

---

## Tipos de input para movil

```
email       → Teclado con @ y .com
tel         → Teclado numerico
url         → Teclado con / y .com
number      → Teclado numerico
search      → Incluye boton buscar
date        → Selector de fecha nativo
password    → Oculta caracteres
```

---

## Autocomplete

```
given-name       → Nombre
family-name      → Apellido
email            → Correo
tel              → Telefono
street-address   → Direccion
postal-code      → Codigo postal
cc-number        → Numero de tarjeta
country-name     → Pais
bday             → Fecha de nacimiento
```

---

## Patron completo de un campo

```html
<label for="campo">Nombre del campo <span aria-hidden="true">*</span></label>
<p id="campo-ayuda">Instrucciones del campo.</p>
<input type="text" id="campo"
       required
       aria-required="true"
       aria-describedby="campo-ayuda"
       autocomplete="name">
<p id="campo-error" role="alert" hidden>Mensaje de error descriptivo.</p>
```

---

## Errores comunes

| Error | Solucion |
|-------|----------|
| Placeholder como unica etiqueta | Siempre usar `<label>` visible |
| `<label>` sin `for` ni input hijo | Asociar con `for="id-del-input"` |
| Error: solo borde rojo | Agregar texto + icono descriptivo |
| Radio buttons sin fieldset | Agrupar con `<fieldset>/<legend>` |
| Sin `autocomplete` en datos personales | Agregar autocomplete apropiado (WCAG 1.3.5) |
| Error dice "Invalido" sin explicar | Describir que se espera: "Ingresa un correo valido" |

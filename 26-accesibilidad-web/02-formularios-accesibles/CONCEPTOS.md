# Formularios Accesibles

## Indice

1. [Labels — la base de todo formulario accesible](#1-labels--la-base-de-todo-formulario-accesible)
2. [Agrupacion con fieldset y legend](#2-agrupacion-con-fieldset-y-legend)
3. [Mensajes de error accesibles](#3-mensajes-de-error-accesibles)
4. [Campos requeridos](#4-campos-requeridos)
5. [Tipos de input para movil](#5-tipos-de-input-para-movil)
6. [Autocomplete — ayuda al navegador](#6-autocomplete--ayuda-al-navegador)
7. [Patron completo de un campo accesible](#7-patron-completo-de-un-campo-accesible)

---

## 1. Labels — la base de todo formulario accesible

Cada campo de formulario **debe** tener un label asociado. Sin label, los lectores de pantalla anuncian el campo como "edit text" sin contexto.

### Asociacion explicita con for/id

```html
<label for="email">Correo electronico</label>
<input type="email" id="email" name="email">
```

El atributo `for` del `<label>` apunta al `id` del `<input>`. Al hacer clic en el label, el campo recibe el foco (beneficio tambien para usuarios con discapacidad motora).

### Asociacion implicita (label envolvente)

```html
<label>
  Correo electronico
  <input type="email" name="email">
</label>
```

Funciona pero la asociacion explicita es preferida por su mayor compatibilidad.

### Lo que NUNCA hacer

```
  MAL                                        POR QUE
  ===                                        =======
  <input placeholder="Correo...">            Placeholder NO es label. Desaparece al escribir.
  <span>Correo</span> <input>               Sin asociacion programatica.
  <div>Correo</div> <input>                 El lector no sabe que el div y el input estan
                                             relacionados.
```

```
  Arbol de accesibilidad:

  SIN label:    textbox (sin nombre)      ← El usuario no sabe que escribir
  CON label:    textbox "Correo electronico"  ← Claro y descriptivo
```

---

## 2. Agrupacion con fieldset y legend

Cuando varios campos estan relacionados (como opciones de radio o secciones de un formulario), se deben agrupar con `<fieldset>` y `<legend>`.

```html
<fieldset>
  <legend>Metodo de pago</legend>

  <label>
    <input type="radio" name="pago" value="tarjeta">
    Tarjeta de credito
  </label>

  <label>
    <input type="radio" name="pago" value="paypal">
    PayPal
  </label>

  <label>
    <input type="radio" name="pago" value="transferencia">
    Transferencia bancaria
  </label>
</fieldset>
```

```
  Lo que el lector de pantalla anuncia:
  ====================================

  "Metodo de pago, grupo"
  "Tarjeta de credito, radio button, 1 de 3"
  "PayPal, radio button, 2 de 3"
  "Transferencia bancaria, radio button, 3 de 3"

  Sin fieldset/legend, cada radio diria solo su label sin contexto del grupo.
```

---

## 3. Mensajes de error accesibles

Los errores deben ser **visibles**, **descriptivos** y **asociados programaticamente** al campo.

### Patron con aria-invalid y aria-describedby

```html
<label for="pass">Contrasena</label>
<input
  type="password"
  id="pass"
  aria-invalid="true"
  aria-describedby="pass-error"
  required
>
<p id="pass-error" role="alert" style="color: #d32f2f;">
  La contrasena debe tener al menos 8 caracteres.
</p>
```

### Flujo de error accesible

```
  1. Usuario envia formulario
  2. Se valida y se detectan errores
  3. aria-invalid="true" se agrega a campos con error
  4. Mensaje de error se muestra y se vincula con aria-describedby
  5. El foco se mueve al PRIMER campo con error
  6. role="alert" hace que el lector anuncie el error inmediatamente
  7. Al corregir: aria-invalid="false" y se oculta el mensaje
```

### No depender solo del color

```
  MAL:  Campo con borde rojo (un usuario daltonico no lo ve)

  BIEN: Campo con borde rojo + icono de error + texto descriptivo
        ┌─────────────────────────────────────┐
        │ [!] La contrasena es muy corta       │
        └─────────────────────────────────────┘
```

---

## 4. Campos requeridos

Hay varias formas de indicar que un campo es obligatorio, y deben combinarse:

```html
<!-- Opcion 1: atributo required nativo + indicador visual -->
<label for="nombre">
  Nombre <span aria-hidden="true">*</span>
</label>
<input type="text" id="nombre" required aria-required="true">

<!-- Indicar al inicio del formulario -->
<p>Los campos marcados con <span aria-hidden="true">*</span>
   (<span class="sr-only">asterisco</span>) son obligatorios.</p>
```

### Por que ambos required y aria-required?

- `required`: activa la validacion nativa del navegador
- `aria-required="true"`: asegura que todos los lectores de pantalla lo anuncien

---

## 5. Tipos de input para movil

El tipo de input correcto muestra el **teclado adecuado** en dispositivos moviles, mejorando la experiencia para todos:

```
┌──────────────────────┬──────────────────────────────────────────────┐
│ type=""              │ Teclado movil                                │
├──────────────────────┼──────────────────────────────────────────────┤
│ text                 │ Teclado alfanumerico general                 │
│ email                │ Incluye @ y .com                             │
│ tel                  │ Teclado numerico para telefonos              │
│ url                  │ Incluye / .com                               │
│ number               │ Teclado numerico                             │
│ search               │ Incluye boton de busqueda                    │
│ password             │ Oculta caracteres                            │
│ date                 │ Selector de fecha nativo                     │
└──────────────────────┴──────────────────────────────────────────────┘
```

---

## 6. Autocomplete — ayuda al navegador

El atributo `autocomplete` permite que el navegador pre-llene campos con datos guardados del usuario.

```html
<input type="text"    name="nombre"   autocomplete="given-name">
<input type="text"    name="apellido" autocomplete="family-name">
<input type="email"   name="email"    autocomplete="email">
<input type="tel"     name="tel"      autocomplete="tel">
<input type="text"    name="calle"    autocomplete="street-address">
<input type="text"    name="cp"       autocomplete="postal-code">
<input type="text"    name="tarjeta"  autocomplete="cc-number">
```

### Beneficios de accesibilidad

- Usuarios con discapacidad motora escriben menos
- Usuarios con discapacidad cognitiva tienen menos que recordar
- WCAG 1.3.5 (AA) requiere autocomplete en campos de datos personales

---

## 7. Patron completo de un campo accesible

```html
<div class="campo">
  <!-- 1. Label visible y asociado -->
  <label for="correo">
    Correo electronico
    <span aria-hidden="true">*</span>
  </label>

  <!-- 2. Instrucciones antes del campo -->
  <p id="correo-instrucciones" class="instrucciones">
    Usaremos este correo para enviar tu confirmacion.
  </p>

  <!-- 3. Input con todos los atributos necesarios -->
  <input
    type="email"
    id="correo"
    name="correo"
    required
    aria-required="true"
    aria-describedby="correo-instrucciones"
    autocomplete="email"
  >

  <!-- 4. Mensaje de error (oculto inicialmente) -->
  <p id="correo-error" role="alert" hidden>
    Ingresa un correo valido (ejemplo: usuario@dominio.com).
  </p>
</div>
```

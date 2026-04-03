# Multimedia Accesible

## Indice

1. [Texto alternativo — cuando y como](#1-texto-alternativo--cuando-y-como)
2. [Imagenes decorativas](#2-imagenes-decorativas)
3. [Figure y figcaption](#3-figure-y-figcaption)
4. [Subtitulos en video — el elemento track](#4-subtitulos-en-video--el-elemento-track)
5. [Audiodescripciones](#5-audiodescripciones)
6. [Transcripciones](#6-transcripciones)
7. [Arbol de decision para imagenes](#7-arbol-de-decision-para-imagenes)

---

## 1. Texto alternativo — cuando y como

El atributo `alt` en imagenes es **obligatorio** segun WCAG 1.1.1 (Nivel A). Describe el contenido o la funcion de la imagen para quienes no pueden verla.

### Reglas para escribir buen alt text

```
  INFORMATIVA                         FUNCIONAL
  ===========                         =========
  La imagen transmite informacion     La imagen es un enlace o boton

  <img src="grafica.png"              <a href="/inicio">
    alt="Grafico de barras               <img src="logo.png"
    mostrando ventas 2025:                  alt="Inicio — MiSitio">
    Q1: 30%, Q2: 45%, Q3: 60%">      </a>

  Describe QUE muestra la imagen      Describe A DONDE lleva o QUE HACE
```

### Buenas practicas

```
┌─────────────────────────────────────────────────────────────────────────┐
│ Hacer                              │ No hacer                          │
├─────────────────────────────────────┼───────────────────────────────────┤
│ Describir el contenido esencial    │ "imagen de..." (redundante)       │
│ Ser conciso (maximo ~125 chars)    │ "foto.jpg" (nombre de archivo)    │
│ Incluir texto de la imagen         │ Dejar alt vacio en img informativa│
│ Describir la funcion si es enlace  │ Repetir el texto adyacente       │
│ Usar contexto relevante            │ Descripciones excesivamente largas│
└─────────────────────────────────────┴───────────────────────────────────┘
```

### Ejemplos comparados

```
  MAL:  <img alt="imagen">
  MAL:  <img alt="foto-equipo-2025.jpg">
  MAL:  <img alt="Imagen de una foto de nuestro equipo de trabajo posando
                   para la foto grupal en la oficina central">

  BIEN: <img alt="Equipo de desarrollo celebrando el lanzamiento de v2.0">
  BIEN: <img alt=""> (si es decorativa — ver seccion 2)
```

---

## 2. Imagenes decorativas

Las imagenes que no transmiten informacion (bordes, separadores, fondos, iconos redundantes) deben tener `alt=""` vacio para que los lectores de pantalla las ignoren.

```html
<!-- Decorativa: icono junto a texto que ya lo describe -->
<button>
  <img src="lupa.svg" alt="">
  Buscar
</button>
<!-- El lector dice: "Buscar, boton" — sin decir "lupa" redundantemente -->

<!-- Decorativa: separador visual -->
<img src="separador.png" alt="">

<!-- Decorativa: imagen de fondo decorativa -->
<img src="patron-abstracto.svg" alt="">
```

### Si no pones alt="" el lector leera el nombre del archivo

```
  Sin alt:     "imagen foto-equipo-2025-final-v2.jpg"  ← ilegible
  Con alt="":  (silencio)                               ← correcto para decorativa
  Con alt:     "Equipo de desarrollo"                   ← correcto para informativa
```

### Alternativa CSS para decorativas

```css
/* Mejor opcion para imagenes puramente decorativas */
.hero {
  background-image: url('patron.svg');
}
```

Las imagenes de fondo CSS son **invisibles** para los lectores de pantalla por naturaleza.

---

## 3. Figure y figcaption

El elemento `<figure>` agrupa una imagen con su descripcion (`<figcaption>`), creando una relacion semantica que los lectores de pantalla entienden.

```html
<figure>
  <img
    src="arquitectura-red.png"
    alt="Diagrama de la arquitectura de red mostrando tres capas:
         cliente, servidor y base de datos"
  >
  <figcaption>
    Figura 1: Arquitectura de red del sistema. Los clientes se conectan
    al servidor a traves de HTTPS, y el servidor consulta la base de datos
    mediante conexiones cifradas.
  </figcaption>
</figure>
```

### Diferencia entre alt y figcaption

```
  alt           → Para lectores de pantalla (reemplaza la imagen)
                  No es visible en pantalla
                  Debe ser conciso

  figcaption    → Para todos los usuarios (complementa la imagen)
                  Visible en pantalla
                  Puede ser mas detallado
```

Ambos pueden coexistir. El `alt` describe la imagen; el `figcaption` da contexto adicional.

---

## 4. Subtitulos en video — el elemento track

Los subtitulos permiten que personas sordas o con dificultad auditiva accedan al contenido de video. WCAG 1.2.2 (Nivel A) los requiere para todo contenido pregrabado.

### Implementacion con el elemento track

```html
<video controls width="640">
  <source src="tutorial.mp4" type="video/mp4">

  <!-- Subtitulos en espanol (captions incluyen sonidos ambientales) -->
  <track
    kind="captions"
    src="tutorial-es.vtt"
    srclang="es"
    label="Espanol"
    default
  >

  <!-- Subtitulos en ingles -->
  <track
    kind="subtitles"
    src="tutorial-en.vtt"
    srclang="en"
    label="English"
  >

  <!-- Fallback para navegadores sin soporte de video -->
  Tu navegador no soporta video HTML5.
  <a href="tutorial.mp4">Descarga el video</a>.
</video>
```

### Formato WebVTT (.vtt)

```
WEBVTT

00:00:01.000 --> 00:00:04.000
Bienvenidos al tutorial de accesibilidad web.

00:00:04.500 --> 00:00:08.000
Hoy aprenderemos a crear sitios
inclusivos para todos los usuarios.

00:00:08.500 --> 00:00:12.000
[Musica de fondo suena]
Empecemos con los fundamentos.
```

### Tipos de track

```
┌──────────────┬──────────────────────────────────────────────┐
│ kind         │ Proposito                                     │
├──────────────┼──────────────────────────────────────────────┤
│ captions     │ Subtitulos + sonidos ambientales (para sordos)│
│ subtitles    │ Traduccion del dialogo (para otro idioma)     │
│ descriptions │ Audiodescripcion textual (para ciegos)        │
│ chapters     │ Titulos de capitulos para navegacion          │
│ metadata     │ Datos para scripts (no visible)               │
└──────────────┴──────────────────────────────────────────────┘
```

---

## 5. Audiodescripciones

Las audiodescripciones narran los elementos visuales importantes de un video durante las pausas del dialogo. Son esenciales para usuarios ciegos.

```
  Video normal:              Con audiodescripcion:
  ============               =====================

  [Narrador habla]           [Narrador habla]
  [Escena de paisaje]        [Voz: "Un campo verde se extiende
                              hacia montanas cubiertas de nieve"]
  [Narrador habla]           [Narrador habla]
  [Grafico en pantalla]      [Voz: "El grafico muestra un incremento
                              del 45% en las ventas del ultimo trimestre"]
```

### WCAG niveles

- **1.2.3 (A)**: Audiodescripcion O texto alternativo para video pregrabado
- **1.2.5 (AA)**: Audiodescripcion para video pregrabado
- **1.2.7 (AAA)**: Audiodescripcion extendida (se pausa el video)

---

## 6. Transcripciones

Una transcripcion es una **version texto completa** del contenido multimedia: dialogo, sonidos ambientales y descripcion de elementos visuales.

### Beneficios

- Accesible para personas sordociegas (con linea braille)
- Buscable por motores de busqueda
- Util en ambientes ruidosos o silenciosos
- Permite copiar/pegar citas

### Ejemplo de transcripcion

```html
<details>
  <summary>Transcripcion del video: Introduccion a la accesibilidad</summary>
  <div>
    <p><strong>[00:00]</strong> Bienvenidos al tutorial. [Musica de fondo]</p>
    <p><strong>[00:05]</strong> La accesibilidad web asegura que todas
       las personas puedan usar los sitios web.</p>
    <p><strong>[00:12]</strong> [Se muestra un grafico con estadisticas]
       Segun la OMS, el 16% de la poblacion mundial tiene alguna
       discapacidad.</p>
  </div>
</details>
```

---

## 7. Arbol de decision para imagenes

```
  La imagen transmite informacion?
  |
  +-- NO → Es puramente decorativa
  |        → alt=""
  |        → O usa CSS background-image
  |
  +-- SI
      |
      +-- Es un enlace o boton?
      |   → alt describe la ACCION o DESTINO, no la imagen
      |   → Ejemplo: alt="Ir al inicio" (no "Logo azul")
      |
      +-- Contiene texto?
      |   → alt incluye el texto de la imagen
      |   → Ejemplo: alt="Oferta: 50% de descuento este fin de semana"
      |
      +-- Es un grafico o diagrama complejo?
      |   → alt breve + descripcion larga
      |   → Usar figcaption o enlace a descripcion detallada
      |   → Ejemplo: alt="Grafico de ventas 2025"
      |     + figcaption con datos completos
      |
      +-- Es una foto informativa?
          → alt describe lo relevante en contexto
          → Ejemplo: alt="Maria Garcia, nueva directora de tecnologia"
```

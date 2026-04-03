# Cheatsheet — Multimedia Accesible

## En una frase

Toda imagen necesita alt text (o alt="" si es decorativa), todo video necesita subtitulos, y todo audio necesita transcripcion.

---

## Alt text — reglas rapidas

```
Informativa    → alt="Descripcion del contenido esencial"
Funcional      → alt="Accion o destino" (si es enlace/boton)
Decorativa     → alt="" (vacio, no omitir el atributo)
Compleja       → alt breve + figcaption o descripcion larga
Con texto      → alt incluye el texto de la imagen
```

---

## Arbol de decision

```
Transmite informacion?
├── NO → alt=""
└── SI
    ├── Es enlace/boton? → alt = destino/accion
    ├── Tiene texto?     → alt = texto de la imagen
    ├── Es compleja?     → alt breve + figcaption detallado
    └── Es foto?         → alt = descripcion contextual
```

---

## Figure + figcaption

```html
<figure>
  <img src="grafico.png"
       alt="Grafico de barras: ventas Q1-Q4 2025">
  <figcaption>
    Figura 1: Las ventas crecieron 45% entre Q1 y Q4 de 2025.
  </figcaption>
</figure>
```

`alt` = reemplaza la imagen (lectores). `figcaption` = complementa (todos).

---

## Video con subtitulos

```html
<video controls>
  <source src="video.mp4" type="video/mp4">
  <track kind="captions" src="subs-es.vtt" srclang="es" label="Espanol" default>
  <track kind="subtitles" src="subs-en.vtt" srclang="en" label="English">
</video>
```

---

## Formato WebVTT

```
WEBVTT

00:00:01.000 --> 00:00:04.000
Bienvenidos al tutorial.

00:00:04.500 --> 00:00:08.000
[Musica de fondo]
Hoy aprenderemos accesibilidad.
```

---

## Tipos de track

```
captions      → Subtitulos + sonidos (para sordos)
subtitles     → Traduccion de dialogo
descriptions  → Audiodescripcion textual (para ciegos)
chapters      → Titulos de capitulos
metadata      → Datos para scripts
```

---

## Transcripcion

```html
<details>
  <summary>Transcripcion del video</summary>
  <p>[00:00] Bienvenidos. [Musica de fondo]</p>
  <p>[00:05] La accesibilidad web es fundamental...</p>
</details>
```

---

## Criterios WCAG relevantes

```
1.1.1 (A)    → Todo contenido no textual tiene alt text
1.2.1 (A)    → Audio/video pregrabado tiene alternativa
1.2.2 (A)    → Video pregrabado tiene subtitulos
1.2.3 (A)    → Video pregrabado tiene audiodescripcion o texto alt
1.2.5 (AA)   → Video pregrabado tiene audiodescripcion
1.4.5 (AA)   → Texto en imagenes solo si es esencial
```

---

## Errores comunes

| Error | Solucion |
|-------|----------|
| Omitir alt en `<img>` | Siempre incluir alt (o alt="" si decorativa) |
| alt="imagen" o alt="foto.jpg" | Describir el contenido, no el formato |
| alt excesivamente largo | Maximo ~125 chars, usar figcaption para mas |
| Video sin subtitulos | Agregar `<track kind="captions">` |
| Icono junto a texto con alt repetido | Usar alt="" en el icono |
| Imagen de fondo informativa en CSS | Mover a `<img>` con alt, o usar aria-label |

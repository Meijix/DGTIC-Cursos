# Cheatsheet — Pagina Web Multi-archivo (Modulo 03)

## Estructura de archivos tipica

```
mi-sitio-web/
|
+-- index.html            <-- Pagina por defecto (el servidor la entrega automaticamente)
+-- pagina2.html           <-- Pagina secundaria
+-- styles.css             <-- Hoja de estilos COMPARTIDA por todas las paginas
|
+-- assets/
    +-- img/               <-- Imagenes locales
    +-- fonts/             <-- Fuentes locales
    +-- icons/             <-- Iconos
```

### Convenciones de nombres

| Regla                         | Correcto            | Incorrecto           |
|-------------------------------|----------------------|----------------------|
| Todo en minusculas            | `mi-pagina.html`     | `Mi-Pagina.html`     |
| Guiones en vez de espacios    | `pagina-contacto.html`| `pagina contacto.html`|
| Sin acentos ni caracteres esp.| `contacto.html`      | `pagina#2.html`      |
| Nombres descriptivos          | `galeria-fotos.html` | `p2.html`            |

---

## Rutas relativas vs absolutas

```
RELATIVA (recomendada para enlaces internos):
  href="pagina2.html"            --> mismo directorio
  href="assets/fondo3.jpg"       --> baja a subcarpeta
  href="../index.html"           --> sube un nivel

ABSOLUTA LOCAL (desde la raiz del servidor):
  href="/about.html"

ABSOLUTA EXTERNA (URL completa):
  href="https://www.ejemplo.com"
```

### Diagrama de rutas relativas

```
proyecto/
+-- index.html                Desde index.html:
+-- pages/                      href="pages/about.html"       OK
|   +-- about.html
|   +-- blog/                 Desde post1.html:
|       +-- post1.html          href="../../index.html"       sube 2 niveles
+-- assets/                     href="../../assets/logo.png"  sube 2, baja a assets
    +-- logo.png                href="../about.html"           sube 1 a pages/

"../" = sube un nivel      "./" = directorio actual (opcional)
```

---

## Imagenes: formatos y comparacion

| Formato | Transparencia | Animacion | Peso     | Mejor para                  |
|---------|---------------|-----------|----------|-----------------------------|
| JPEG    | No            | No        | Mediano  | Fotografias                 |
| PNG     | Si (alfa)     | No        | Grande   | Logos, capturas, transparencia|
| SVG     | Si            | Si (CSS)  | Pequeno  | Iconos, logos vectoriales   |
| WebP    | Si (alfa)     | Si        | Pequeno  | Reemplazo moderno de JPG/PNG|
| AVIF    | Si (alfa)     | Si        | Muy peq. | Mejor compresion disponible |

### Imagen con fallback de formatos

```html
<picture>
    <source srcset="foto.avif" type="image/avif">
    <source srcset="foto.webp" type="image/webp">
    <img src="foto.jpg" alt="Descripcion de la foto">
</picture>
```

### Texto alternativo (alt)

```
La imagen es decorativa? --SI--> alt=""  (vacio, el lector la ignora)
                         --NO--> Describe QUE MUESTRA, no como se ve
```

| Imagen                    | alt bueno                               | alt malo       |
|---------------------------|-----------------------------------------|----------------|
| Foto del equipo           | `"Equipo de desarrollo en la oficina"`  | `"foto"`       |
| Logo de la UNAM           | `"Logo de la UNAM"`                     | `"imagen"`     |
| Linea decorativa          | `""`                                    | `"linea"`      |

---

## Enlaces: atributos importantes

```html
<!-- Enlace interno (misma pestana) -->
<a href="pagina2.html">Ir a pagina 2</a>

<!-- Enlace externo (nueva pestana, con seguridad) -->
<a href="https://ejemplo.com" target="_blank" rel="noopener noreferrer">Visitar</a>

<!-- Enlace a seccion de la misma pagina -->
<a href="#servicios">Ir a servicios</a>
<section id="servicios">...</section>

<!-- Enlace a seccion de otra pagina -->
<a href="pagina2.html#formulario">Ir al formulario</a>
```

**Siempre** usar `rel="noopener noreferrer"` con `target="_blank"` para evitar ataques de tab-nabbing.

---

## Clases CSS y organizacion de estilos

```
SELECTOR DE ELEMENTO        CLASE                      ID
p { color: blue; }          .destacado { color: red; } #titulo { ... }
Todos los <p>               Reutilizable (N elementos) Unico (1 elemento)
Especificidad: 0,0,0,1     Especificidad: 0,0,1,0    Especificidad: 0,1,0,0
Uso: estilos base           Uso: componentes           Uso: JS, label-for-id
```

### Patron width + max-width (responsivo)

```css
.contenedor {
    width: 100%;            /* fluido en moviles */
    max-width: 400px;       /* techo en pantallas grandes */
    margin: auto;           /* centrado horizontal */
}
```

```
Movil (320px):                    Escritorio (1200px):
+------------------------+       +------------------------------------------+
| .contenedor (100%)     |       |        +----------------+               |
| ocupa toda la pantalla |       |        | .contenedor    |               |
+------------------------+       |        | (400px, centrado)|             |
                                 +------------------------------------------+
```

---

## Entidades HTML

| Entidad     | Caracter | Cuando usarla                     |
|-------------|----------|-----------------------------------|
| `&lt;`      | <        | Mostrar etiquetas HTML como texto |
| `&gt;`      | >        | Mostrar etiquetas HTML como texto |
| `&amp;`     | &        | Siempre que necesites un &        |
| `&nbsp;`    | (espacio)| Espacio que no se rompe           |
| `&copy;`    | (c)      | Simbolo de copyright              |

---

## Errores comunes

| Error                                | Solucion                                         |
|--------------------------------------|--------------------------------------------------|
| Imagen no carga (ruta incorrecta)    | Verificar ruta relativa: `assets/foto.jpg`       |
| Barra invertida en rutas             | Usar `/` (normal), nunca `\`                     |
| CSS no se aplica                     | Verificar `rel="stylesheet"` en el `<link>`      |
| Clase CSS no coincide                | CSS distingue mayusculas: `.mi-clase` != `.Mi-Clase`|
| Enlace externo sin `rel="noopener"`  | Agregar `rel="noopener noreferrer"` con `_blank` |
| `font: tahoma;` (shorthand invalido)| Usar `font-family: tahoma;`                      |
| Imagen se desborda del contenedor    | `img { max-width: 100%; height: auto; }`        |

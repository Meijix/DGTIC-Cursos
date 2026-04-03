# DGTIC - Cursos de Desarrollo Web y Programación

Ejercicios y proyectos de los cursos impartidos por la DGTIC (UNAM): desarrollo web (HTML, CSS, JavaScript), introducción a la programación (Python) y fundamentos de PHP.

**Autora:** Natalia Edith Mejia Bautista

> **Punto de entrada:** abre [`index.html`](index.html) en tu navegador para ver la tabla de contenidos interactiva con enlaces a cada ejercicio.

---

## Contenido del curso

El repositorio esta organizado en modulos progresivos, desde los fundamentos hasta proyectos completos:

### Bloque 1 — HTML y CSS (Desarrollo Web)

| # | Modulo | Temas principales | Archivo principal |
|---|--------|-------------------|-------------------|
| 01 | [Fundamentos HTML](01-fundamentos-html/) | Estructura semantica HTML5, formularios, listas de definicion | `index.html` |
| 02 | [Fundamentos CSS](02-fundamentos-css/) | Variables CSS, box model, colores, tipografia | `index.html` |
| 03 | [Pagina web basica](03-pagina-web-basica/) | Sitio multi-pagina, enlaces, imagenes, formularios | `index.html` |
| 04 | [Flexbox - Dados](04-flexbox-dados/) | Display flex, justify-content, align-items, flex-direction | `dados.html` |
| 05 | [Componentes CSS](05-componentes-css/) | Tarjetas con gradientes, box-shadow, diseno de componentes | `index.html` |
| 06 | [Responsive - Fundamentos](06-responsive-fundamentos/) | Media queries, mobile-first, anchos flexibles con Flexbox | `index.html` |
| 07 | [Responsive - CSS Grid](07-responsive-css-grid/) | CSS Grid, grid-template-columns, layouts multi-columna | `index.html` |
| 08 | [Proyecto: Sitio de servicios](08-proyecto-web-servicios/) | Proyecto integrador con gradientes, cards responsivas, multiples breakpoints | `index.html` |
| 09 | [Portfolio profesional](09-portfolio-profesional/) | Portfolio completo con animaciones scroll, navegacion suave, JavaScript | `portfolioYo.html` |
| 10 | [Landing personal](10-landing-personal/) | Landing page con hero, about, proyectos y contacto. Mobile-first, IntersectionObserver | `index.html` |

### Bloque 2 — Programación

| # | Modulo | Temas principales | Contenido |
|---|--------|-------------------|-----------|
| 00 | [Ejercicios de programación](00-ejercicios-programacion/) | Condicionales, ciclos, funciones, validacion, logica de juegos | 15 ejercicios `.py` (prerequisito) |
| 11 | [Python - Fundamentos](11-python-fundamentos/) | Tipos, estructuras de datos, POO, decoradores, testing, proyectos | 10 secciones con 55 archivos |
| 12 | [JavaScript - Fundamentos](12-javascript-fundamentos/) | Variables, ciclos, funciones, POO, eventos DOM, consumo de API | Scripts progresivos + proyecto final (TMDB API) |
| 13 | [PHP - Fundamentos](13-php-fundamentos/) | Funciones, regex, sesiones, formularios, gestion de usuarios | Ejercicios + proyecto con autenticacion |

### Bloque 3 — Backend y Frameworks

| # | Modulo | Temas principales | Contenido |
|---|--------|-------------------|-----------|
| 14 | [PHP - Orientado a Objetos](14-php-orientado-a-objetos/) | Clases, metodos, acceso privado/protegido, constructores, herencia | 7 ejercicios progresivos de POO |
| 15 | [Laravel - CRUD](15-laravel-crud/) | Controladores REST, Blade, validacion, paginacion, email | App de gestion de cursos |
| 16 | [Laravel - Livewire](16-laravel-livewire/) | Componentes reactivos, Livewire 3, Tailwind CSS | CRUD reactivo sin JS |
| 17 | [Laravel - Evaluación](17-laravel-evaluacion/) | Livewire avanzado, model binding, factories, testing | Proyecto evaluado de clientes |
| 18 | [Node.js - Introducción](18-nodejs-intro/) | Express, AWS DynamoDB/Lambda/API Gateway, OpenAI SDK | Arquitectura serverless |
| 19 | [Node.js - Challenge API](19-nodejs-challenge-api/) | CLI + Express, consumo de API OpenAI, async/await | Mini-proyecto de integracion |
| 20 | [GitHub Actions](20-github-actions/) | CI/CD, workflows, testing, deploy, acciones personalizadas, seguridad | 6 secciones con 34 archivos |

### Bloque 4 — Ciencias de la Computacion

| # | Modulo | Temas principales | Contenido |
|---|--------|-------------------|-----------|
| 21 | [Estructuras de Datos](21-estructuras-de-datos/) | Arrays, listas enlazadas, pilas, colas, tablas hash, arboles, heaps, grafos | 8 secciones con diagramas y ejemplos Python |
| 22 | [Algoritmos de Ordenacion](22-algoritmos-ordenacion/) | Bubble, Selection, Insertion, Merge, Quick, Counting, Radix Sort | 7 secciones con visualizaciones y analisis Big O |

---

## Material de aprendizaje

Los modulos 01-10 incluyen material educativo adicional:

- **Comentarios en el codigo:** cada archivo HTML y CSS contiene explicaciones detalladas sobre como, por que, y que alternativas se consideraron para cada decision.
- **`CONCEPTOS.md`:** cada carpeta (01-10) contiene una guia en Markdown con teoria profunda, diagramas ASCII, tablas de referencia, errores comunes y ejercicios de practica.
- **[`GUIA_DEL_CURSO.md`](GUIA_DEL_CURSO.md):** guia general del curso con mapa de aprendizaje, glosario de terminos y recursos adicionales.

Los modulos 11-13 incluyen sus propios enunciados y documentacion dentro de cada ejercicio.

### Mapa de progresion

```
                    BLOQUE 1: Desarrollo Web
┌─────────────────────────────────────────────────────────┐
│                                                         │
│  01 HTML ──► 02 CSS ──► 03 Multi-pagina                 │
│                              │                          │
│                              ▼                          │
│  06 Responsive ◄── 05 Componentes ◄── 04 Flexbox       │
│       │                                                 │
│       ▼                                                 │
│  07 CSS Grid ──► 08 Integracion ──► 09 Portfolio        │
│                                         │               │
│                                         ▼               │
│                                    10 Landing           │
└─────────────────────────────────────────────────────────┘
                         │
                         ▼
                 BLOQUE 2: Programación
┌─────────────────────────────────────────────────────────┐
│                                                         │
│  00 Ejercicios ──► 11 Python ──► 12 JavaScript           │
│                              │                          │
│                              ▼                          │
│                         13 PHP (backend)                │
└─────────────────────────────────────────────────────────┘
                         │
                         ▼
             BLOQUE 3: Backend y Frameworks
┌─────────────────────────────────────────────────────────┐
│                                                         │
│  14 PHP POO ──► 15 Laravel CRUD ──► 16 Livewire        │
│                                         │               │
│                                         ▼               │
│                                    17 Evaluación        │
│                                                         │
│  18 Node.js Intro ──► 19 Node.js Challenge (API)       │
│                                                         │
│  20 GitHub Actions (CI/CD)                              │
└─────────────────────────────────────────────────────────┘
                         │
                         ▼
          BLOQUE 4: Ciencias de la Computación
┌───────��─────────────────────────────────────────────────┐
│                                                         │
│  21 Estructuras de Datos ──► 22 Algoritmos Ordenacion   │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

---

## Tecnologias

- **HTML5** — estructura semantica, formularios, accesibilidad
- **CSS3** — Flexbox, Grid, variables, media queries, gradientes, transiciones
- **JavaScript** — DOM, eventos, clases, fetch/API, IntersectionObserver
- **Python** — logica de programacion, funciones, manejo de errores
- **PHP** — funciones, regex, sesiones, POO, formularios server-side
- **Laravel** — MVC, Eloquent ORM, Blade, Livewire, validacion, email
- **Node.js** — Express, async/await, AWS (DynamoDB, Lambda), OpenAI API
- **GitHub Actions** — CI/CD, workflows, testing automatizado, deploy, seguridad
- **Estructuras de datos** — arrays, listas enlazadas, pilas, colas, tablas hash, arboles, heaps, grafos
- **Algoritmos de ordenacion** — bubble, selection, insertion, merge, quick, counting, radix sort

## Como usar

1. Abre [`index.html`](index.html) en tu navegador para ver la tabla de contenidos.
2. Cada carpeta es un modulo independiente — puedes abrir el archivo principal directamente.
3. Lee el `CONCEPTOS.md` de cada modulo (01-10) para entender la teoria.
4. Los ejercicios de Python (11) se ejecutan con `python3 ejercicioNN.py`.
5. Los archivos PHP (13-14) requieren un servidor local (`php -S localhost:8000`).
6. Los proyectos Laravel (15-17) tienen instrucciones detalladas en su `SETUP.md`.
7. Los proyectos Node.js (18-19) necesitan `npm install` y `node index.js`.

```bash
# Abrir la tabla de contenidos
open index.html

# Abrir un modulo especifico
open 04-flexbox-dados/dados.html

# Ejecutar un ejercicio de Python
python3 11-python-programacion/Ejercicio-01_Numeros_pares/ejercicio01.py

# Levantar servidor PHP local
cd 13-php-fundamentos/TareaFormulario_NEMB && php -S localhost:8000

# Levantar un proyecto Laravel (ver SETUP.md de cada uno)
cd 15-laravel-crud && composer install && cp .env.example .env && php artisan key:generate
touch database/database.sqlite && php artisan migrate && php artisan serve
```

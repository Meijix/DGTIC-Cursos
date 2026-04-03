# Guia del Curso: Desarrollo Web y Programacion — DGTIC UNAM

> **Cursos:** Ejercicios de Programacion (Python), Desarrollo de Paginas Web (HTML/CSS/JS), Fundamentos de Python, JavaScript, PHP, Laravel, Node.js, CI/CD con GitHub Actions, Estructuras de Datos y Algoritmos de Ordenacion, TypeScript, React, SQL y Bases de Datos, Accesibilidad Web, Docker
> **Institucion:** Direccion General de Computo y de Tecnologias de Informacion y
> Comunicacion (DGTIC), UNAM
> **Formato:** 28 modulos progresivos (00-27) en 7 bloques: prerequisito (00), desarrollo web (01-10), programacion y backend (11-19), DevOps (20), ciencias de la computacion (21-22), frontend avanzado (23-24), y bases de datos, accesibilidad y DevOps (25-27)

---

## Tabla de contenidos

1. [Sobre este curso](#1-sobre-este-curso)
2. [Mapa de aprendizaje](#2-mapa-de-aprendizaje)
3. [Tabla de conceptos por modulo](#3-tabla-de-conceptos-por-modulo)
4. [Glosario de terminos](#4-glosario-de-terminos)
5. [Recursos adicionales](#5-recursos-adicionales)
6. [Como seguir aprendiendo](#6-como-seguir-aprendiendo)

---

## 1. Sobre este curso

### Que vas a aprender

Al completar este curso seras capaz de:

- Resolver ejercicios de logica de programacion con Python (prerequisito).
- Escribir HTML semantico y accesible desde cero.
- Disenar y maquetar paginas web con CSS moderno (Flexbox, Grid, variables, transiciones).
- Crear sitios responsive que funcionen en cualquier dispositivo.
- Aplicar buenas practicas de rendimiento, accesibilidad y SEO.
- Construir un portfolio profesional y una landing page como proyectos finales.
- Entender la interactividad basica con JavaScript (DOM, eventos, IntersectionObserver).
- Programar con Python a nivel intermedio (POO, decoradores, generadores, testing con pytest).
- Manejar JavaScript a nivel intermedio (POO, eventos, consumo de APIs).
- Desarrollar aplicaciones web server-side con PHP (sesiones, formularios, regex).
- Aplicar Programacion Orientada a Objetos en PHP (clases, herencia, polimorfismo).
- Construir aplicaciones web con Laravel (CRUD, Blade, Livewire, Eloquent).
- Crear APIs y servicios con Node.js, Express y servicios cloud (AWS, OpenAI).
- Automatizar pruebas y despliegues con GitHub Actions (CI/CD, workflows, Docker).
- Comprender estructuras de datos fundamentales (arrays, listas enlazadas, pilas, colas, tablas hash, arboles, heaps, grafos).
- Implementar y analizar algoritmos de ordenacion clasicos (bubble, selection, insertion, merge, quick, counting, radix sort).
- Programar con TypeScript (tipos, interfaces, genericos, clases, utility types, configuracion).
- Construir aplicaciones con React (JSX, componentes, hooks, React Router, formularios).
- Disenar y consultar bases de datos con SQL (SELECT, JOINs, normalizacion, indices, transacciones).
- Aplicar principios de accesibilidad web (WCAG, ARIA, navegacion por teclado, contraste, testing).
- Containerizar aplicaciones con Docker (Dockerfile, Compose, desarrollo, produccion).

### Prerequisitos

**Ninguno.** Este curso empieza desde cero. Solo necesitas:

- Una computadora con un navegador moderno (Chrome, Firefox, Edge o Safari).
- Un editor de texto (recomendamos [Visual Studio Code](https://code.visualstudio.com/)).
- Ganas de aprender y experimentar.

### Como usar este repositorio

```
DGTIC-Cursos/
│
├── 00-ejercicios-programacion/    ← Prerequisito: 15 ejercicios Python
│
├── 01-fundamentos-html/           ← Bloque 1: Desarrollo Web
├── 02-fundamentos-css/
├── 03-pagina-web-basica/
├── 04-flexbox-dados/
├── 05-componentes-css/
├── 06-responsive-fundamentos/
├── 07-responsive-css-grid/
├── 08-proyecto-web-servicios/
├── 09-portfolio-profesional/
├── 10-landing-personal/
│
├── 11-python-fundamentos/         ← Bloque 2: Programacion y Backend
├── 12-javascript-fundamentos/
├── 13-php-fundamentos/
├── 14-php-orientado-a-objetos/
├── 15-laravel-crud/
├── 16-laravel-livewire/
├── 17-laravel-evaluacion/
├── 18-nodejs-intro/
├── 19-nodejs-challenge-api/
│
├── 20-github-actions/             ← Bloque 3: DevOps / CI/CD
│
├── 21-estructuras-de-datos/       ← Bloque 4: Ciencias de la Computacion
├── 22-algoritmos-de-ordenacion/
│
├── 23-typescript/                 ← Bloque 5: Frontend Avanzado
├── 24-react-fundamentos/
│
├── 25-sql-bases-de-datos/         ← Bloque 6: Bases de Datos, Accesibilidad y DevOps
├── 26-accesibilidad-web/
├── 27-docker/
│
├── index.html                     ← Pagina principal del repositorio
├── GUIA_DEL_CURSO.md              ← Este archivo (guia general)
└── README.md
```

**Para cada modulo:**

1. Lee el archivo `CONCEPTOS.md` del modulo (cuando exista) para entender la teoria.
2. Revisa los archivos de codigo del ejercicio. Los comentarios en el codigo
   explican cada decision.
3. Experimenta: modifica valores, rompe cosas, observa que pasa.
4. Intenta los ejercicios de practica de `CONCEPTOS.md` antes de pasar al siguiente modulo.

### Estructura detallada de los modulos

| Bloque | Modulos | Descripcion |
|--------|---------|-------------|
| **Prerequisito** | 00 | 15 ejercicios de logica en Python (numeros, ciclos, condicionales, juegos) |
| **Desarrollo Web** | 01-10 | HTML semantico, CSS moderno, Flexbox, Grid, responsive, portfolio y landing page |
| **Programacion y Backend** | 11-19 | Python completo (10 secciones, 55 archivos), JavaScript, PHP, Laravel, Node.js |
| **DevOps** | 20 | GitHub Actions: CI/CD completo (6 secciones, 34 archivos YAML) |
| **Ciencias de la Computacion** | 21-22 | Estructuras de datos y algoritmos de ordenacion |
| **Frontend Avanzado** | 23-24 | TypeScript y React fundamentos |
| **Bases de Datos, Accesibilidad y DevOps** | 25-27 | SQL, accesibilidad web (WCAG/ARIA) y Docker |

---

## 2. Mapa de aprendizaje

### Progresion del curso

```
                         MAPA DE APRENDIZAJE
  ═══════════════════════════════════════════════════════════

  FASE 0: PREREQUISITO
  ─────────────────────
  ┌───────────────────┐
  │  00                │
  │  Ejercicios de     │
  │  Programacion      │
  │                    │
  │  15 ejercicios     │
  │  Python: logica,   │
  │  ciclos, juegos    │
  └────────┬──────────┘
           │
           ▼
  FASE 1: FUNDAMENTOS WEB
  ─────────────────────
  ┌───────────────────┐     ┌───────────────────┐
  │  01                │     │  02                │
  │  Fundamentos HTML  │────►│  Fundamentos CSS   │
  │                    │     │                    │
  │  Etiquetas, seman- │     │  Selectores, box   │
  │  tica, estructura  │     │  model, colores    │
  └───────────────────┘     └────────┬──────────┘
                                     │
                                     ▼
  FASE 2: CONSTRUCCION          ┌───────────────────┐
  ─────────────────────         │  03                │
                                │  Pagina web basica │
                                │                    │
                                │  Multi-pagina,     │
                                │  navegacion, links │
                                └────────┬──────────┘
                                         │
                                         ▼
                                ┌───────────────────┐
                                │  04                │
                                │  Flexbox (Dados)   │
                                │                    │
                                │  Ejes, alineacion, │
                                │  distribucion      │
                                └────────┬──────────┘
                                         │
                                         ▼
                                ┌───────────────────┐
                                │  05                │
                                │  Componentes CSS   │
                                │                    │
                                │  Cards, botones,   │
                                │  formularios       │
                                └────────┬──────────┘
                                         │
                                         ▼
  FASE 3: RESPONSIVE            ┌───────────────────┐
  ───────────────────           │  06                │
                                │  Responsive        │
                                │  Fundamentos       │
                                │                    │
                                │  Media queries,    │
                                │  mobile first      │
                                └────────┬──────────┘
                                         │
                                         ▼
                                ┌───────────────────┐
                                │  07                │
                                │  CSS Grid          │
                                │                    │
                                │  Grid template,    │
                                │  areas, responsive │
                                └────────┬──────────┘
                                         │
                                         ▼
  FASE 4: INTEGRACION           ┌───────────────────┐
  ────────────────────          │  08                │
                                │  Proyecto Web      │
                                │  de Servicios      │
                                │                    │
                                │  Sitio completo,   │
                                │  multi-seccion     │
                                └────────┬──────────┘
                                         │
                                         ▼
  FASE 5: PROYECTOS             ┌───────────────────┐
  PROFESIONALES                 │  09                │
  ─────────────────             │  Portfolio         │
                                │  Profesional       │
                                │                    │
                                │  Position, JS,     │
                                │  scroll animations │
                                └────────┬──────────┘
                                         │
                                         ▼
                                ┌───────────────────┐
                                │  10                │
                                │  Landing Page      │
                                │  Profesional       │
                                │                    │
                                │  Arquitectura CSS, │
                                │  clamp(), a11y,    │
                                │  SEO, performance  │
                                └────────┬──────────┘
                                         │
                                         ▼
  FASE 6: PYTHON COMPLETO      ┌───────────────────┐
  ────────────────────          │  11                │
                                │  Python            │
                                │  Fundamentos       │
                                │                    │
                                │  POO, decoradores, │
                                │  generadores,      │
                                │  testing, archivos │
                                └────────┬──────────┘
                                         │
                                         ▼
  FASE 7: JS + PHP              ┌───────────────────┐
  ─────────────                 │  12                │
                                │  JavaScript        │
                                │                    │
                                │  POO, DOM,         │
                                │  eventos, APIs     │
                                └────────┬──────────┘
                                         │
                                         ▼
                                ┌───────────────────┐
                                │  13                │
                                │  PHP               │
                                │                    │
                                │  Sesiones, regex,  │
                                │  formularios       │
                                └────────┬──────────┘
                                         │
                                         ▼
  FASE 8: POO + FRAMEWORKS     ┌───────────────────┐
  ────────────────────          │  14                │
                                │  PHP POO           │
                                │                    │
                                │  Clases, herencia, │
                                │  encapsulamiento   │
                                └────────┬──────────┘
                                         │
                                         ▼
                                ┌───────────────────┐
                                │  15                │
                                │  Laravel CRUD      │
                                │                    │
                                │  MVC, Eloquent,    │
                                │  Blade, email      │
                                └────────┬──────────┘
                                         │
                                         ▼
                                ┌───────────────────┐
                                │  16                │
                                │  Laravel Livewire  │
                                │                    │
                                │  Componentes       │
                                │  reactivos         │
                                └────────┬──────────┘
                                         │
                                         ▼
  FASE 9: EVALUACION            ┌───────────────────┐
  ──────────────────            │  17                │
                                │  Laravel Eval      │
                                │                    │
                                │  Proyecto evaluado │
                                │  Livewire avanzado │
                                └───────────────────┘

  FASE 10: NODE.js              ┌───────────────────┐
  ────────────────              │  18                │
                                │  Node.js Intro     │
                                │                    │
                                │  Express, AWS,     │
                                │  DynamoDB, Lambda  │
                                └────────┬──────────┘
                                         │
                                         ▼
                                ┌───────────────────┐
                                │  19                │
                                │  Node.js Challenge │
                                │                    │
                                │  CLI + API,        │
                                │  OpenAI, JSON      │
                                └────────┬──────────┘
                                         │
                                         ▼
  FASE 11: DEVOPS               ┌───────────────────┐
  ───────────────               │  20                │
                                │  GitHub Actions    │
                                │                    │
                                │  CI/CD, workflows, │
                                │  testing, deploy,  │
                                │  Docker, seguridad │
                                └────────┬──────────┘
                                         │
                                         ▼
  FASE 12: CIENCIAS DE          ┌───────────────────┐
  LA COMPUTACION                │  21                │
  ──────────────────            │  Estructuras de    │
                                │  Datos             │
                                │                    │
                                │  Arrays, listas,   │
                                │  pilas, colas,     │
                                │  hash, arboles,    │
                                │  heaps, grafos     │
                                └────────┬──────────┘
                                         │
                                         ▼
                                ┌───────────────────┐
                                │  22                │
                                │  Algoritmos de     │
                                │  Ordenacion        │
                                │                    │
                                │  Bubble, selection,│
                                │  insertion, merge, │
                                │  quick, counting,  │
                                │  radix sort        │
                                └────────┬──────────┘
                                         │
                                         ▼
  FASE 13: FRONTEND            ┌───────────────────┐
  AVANZADO                     │  23                │
  ────────────────             │  TypeScript        │
                               │                    │
                               │  Tipos, interfaces,│
                               │  genericos, clases,│
                               │  utility types     │
                               └────────┬──────────┘
                                        │
                                        ▼
                               ┌───────────────────┐
                               │  24                │
                               │  React             │
                               │  Fundamentos       │
                               │                    │
                               │  JSX, componentes, │
                               │  hooks, Router,    │
                               │  formularios       │
                               └────────┬──────────┘
                                        │
                                        ▼
  FASE 14: BD, A11Y Y         ┌───────────────────┐
  DEVOPS                       │  25                │
  ────────────────             │  SQL y Bases de    │
                               │  Datos             │
                               │                    │
                               │  SELECT, JOINs,    │
                               │  normalizacion,    │
                               │  indices, trans.   │
                               └────────┬──────────┘
                                        │
                                        ▼
                               ┌───────────────────┐
                               │  26                │
                               │  Accesibilidad Web │
                               │                    │
                               │  WCAG, ARIA,       │
                               │  teclado, contraste│
                               │  testing           │
                               └────────┬──────────┘
                                        │
                                        ▼
                               ┌───────────────────┐
                               │  27                │
                               │  Docker            │
                               │                    │
                               │  Contenedores,     │
                               │  Dockerfile,       │
                               │  Compose, deploy   │
                               └───────────────────┘
```

### Vista compacta

```
00 Prerequisito (Python)
    │
    ▼
01 HTML ──► 02 CSS ──► 03 Multi-page ──► 04 Flexbox ──► 05 Componentes
                                                              │
         ┌────────────────────────────────────────────────────┘
         ▼
06 Responsive ──► 07 CSS Grid ──► 08 Integracion ──► 09 Portfolio ──► 10 Landing
                                                                          │
         ┌────────────────────────────────────────────────────────────────┘
         ▼
11 Python ──► 12 JavaScript ──► 13 PHP ──► 14 PHP POO ──► 15 Laravel ──► 16 Livewire ──► 17 Eval
                    │
                    └──► 18 Node.js ──► 19 Challenge API
                                              │
                                              └──► 20 GitHub Actions (CI/CD)
                                                          │
                                                          └──► 21 Estructuras de Datos ──► 22 Algoritmos de Ordenacion
                                                                                                    │
                              ┌──────────────────────────────────────────────────────────────────────┘
                              ▼
23 TypeScript ──► 24 React Fundamentos ──► 25 SQL y Bases de Datos ──► 26 Accesibilidad Web ──► 27 Docker
```

### Que construye cada modulo

```
Modulo  Que construyes                         Habilidad principal
──────  ──────────────────────────────────────  ─────────────────────────
  00    15 ejercicios de logica en Python      Pensamiento algoritmico
  01    Tu primer documento HTML                Estructura y semantica
  02    Pagina con estilos basicos              CSS: selectores, box model
  03    Sitio de varias paginas con navegacion  Enlaces, rutas, estructura
  04    Dados con caras usando Flexbox          Alineacion con Flexbox
  05    Componentes reutilizables (cards, etc.) Pensamiento modular
  06    Sitio adaptable a movil                 Media queries, mobile first
  07    Layouts complejos con Grid              CSS Grid, areas, responsive
  08    Sitio web de servicios completo         Integracion de todo
  09    Portfolio profesional de una pagina     Position, JS, animaciones
  10    Landing page con efectos modernos       Arquitectura, a11y, SEO
  11    Curso completo Python (10 secciones)    POO, decoradores, testing
  12    Scripts JS + proyecto con API           JavaScript, DOM, fetch
  13    Ejercicios PHP + app de usuarios        Backend, sesiones, regex
  14    7 ejercicios de POO en PHP              Clases, herencia, polimorfismo
  15    App CRUD de cursos con Laravel          MVC, Eloquent, Blade, email
  16    CRUD reactivo con Livewire              Componentes sin JS, reactivo
  17    Proyecto evaluado de clientes           Livewire avanzado, testing
  18    Node.js con Express y AWS               Serverless, DynamoDB, Lambda
  19    Challenge: CLI + API OpenAI             Integracion de APIs, JSON
  20    Pipelines CI/CD con GitHub Actions      Workflows, testing, deploy
  21    Estructuras de datos fundamentales     Arrays, listas, pilas, colas, hash, arboles
  22    Algoritmos de ordenacion clasicos      Bubble, selection, merge, quick sort
  23    Proyecto con TypeScript                Tipos, interfaces, genericos, clases
  24    Aplicacion con React                   JSX, componentes, hooks, Router
  25    Consultas y diseno de bases de datos   SELECT, JOINs, normalizacion, indices
  26    Auditoria y mejoras de accesibilidad   WCAG, ARIA, teclado, contraste
  27    Aplicacion containerizada con Docker   Dockerfile, Compose, dev y prod
```

---

## 3. Tabla de conceptos por modulo

| Modulo | Conceptos principales | Archivos clave | Construye sobre |
|--------|----------------------|----------------|-----------------|
| **00** Ejercicios Programacion | Variables, `input()`, condicionales (`if`/`elif`/`else`), ciclos (`for`/`while`), operadores aritmeticos, logica de juegos, `random`, diagramas de flujo | 15 carpetas con `.py` + `.md` + diagramas | -- |
| **01** Fundamentos HTML | Etiquetas HTML, semantica, `<head>`, `<body>`, headings, parrafos, listas, enlaces, imagenes, estructura de documento | `index.html` | -- |
| **02** Fundamentos CSS | Selectores (tipo, clase, ID), propiedades de texto, colores, box model (margin, padding, border), display, unidades | `index.html`, `style.css` | 01 |
| **03** Pagina web basica | Multi-pagina, navegacion con `<nav>`, rutas relativas, `<a>` entre paginas, estructura de carpetas, `<footer>` | `index.html`, paginas internas | 01, 02 |
| **04** Flexbox (Dados) | `display: flex`, `flex-direction`, `justify-content`, `align-items`, `flex-wrap`, `gap`, `align-self` | `index.html`, `style.css` | 01, 02 |
| **05** Componentes CSS | Cards, botones, formularios, pseudo-clases (`:hover`, `:focus`), `border-radius`, `box-shadow`, transiciones basicas | Archivos de componentes | 01-04 |
| **06** Responsive | `<meta viewport>`, media queries, `min-width` vs `max-width`, mobile first, unidades relativas (`rem`, `em`, `%`, `vw`) | `style.css` con media queries | 01-05 |
| **07** CSS Grid | `display: grid`, `grid-template-columns`, `grid-template-rows`, `grid-template-areas`, `fr`, `repeat()`, `minmax()`, `auto-fit` | `style.css` con grid | 01-06 |
| **08** Proyecto Web | Integracion de Flexbox + Grid, secciones hero, servicios, testimonios, footer complejo, Variables CSS (`--custom-property`) | Sitio completo | 01-07 |
| **09** Portfolio | `position` (relative, absolute, fixed, sticky), `z-index`, transiciones CSS, JavaScript DOM, `classList`, `addEventListener`, IntersectionObserver, scroll animations | `index.html`, `style.css`, `script.js` | 01-08 |
| **10** Landing Page | Arquitectura CSS (ITCSS), design systems, `clamp()`, `backdrop-filter`, `::before`/`::after`, performance (CLS, lazy loading, preload), SEO (meta tags, Open Graph), accesibilidad (ARIA, skip links, WCAG) | `index.html`, `style.css`, `script.js` | 01-09 |
| **11** Python Fundamentos | Tipos de datos, listas, tuplas, diccionarios, sets, comprehensions, funciones de orden superior, lambdas, `*args`/`**kwargs`, type hints, POO (clases, herencia, polimorfismo, magic methods, dataclasses), modulos/paquetes, archivos (CSV, JSON, pathlib), decoradores, generadores, iteradores, manejo de errores, context managers, logging, pytest (fixtures, mocking, parametrize), proyectos integradores | 10 secciones, 55 archivos `.py` + `.md` | 00 |
| **12** JavaScript | Variables, ciclos, funciones (arrow, anonymous), clases, herencia, DOM (`getElementById`, `querySelector`), eventos (`onclick`, `DOMContentLoaded`), `fetch()` + API REST | `script00-02.js`, `Eventos1/`, `PracticaFinalNat/` | 09, 10 |
| **13** PHP | Variables, funciones, ciclos, `str_repeat()`, expresiones regulares (`preg_match`), sesiones (`$_SESSION`), formularios (`$_POST`), autenticacion, `htmlspecialchars()` | `.php` files, `TareaFormulario_NEMB/` | 12 |
| **14** PHP POO | Clases, objetos, propiedades (public/private/protected), metodos, constructores/destructores, herencia, polimorfismo | `Clases/`, `Vistas/`, `index.php` | 13 |
| **15** Laravel CRUD | Controladores REST (index/create/store/edit/update/destroy), Blade templates, Eloquent ORM, validacion, paginacion, Mailable, rutas con nombre, middleware | `app/Http/Controllers/`, `resources/views/`, `routes/web.php` | 14 |
| **16** Laravel Livewire | Componentes Livewire 3, propiedades reactivas, validacion en tiempo real, Tailwind CSS, Vite | `app/Livewire/`, `resources/views/livewire/` | 15 |
| **17** Laravel Evaluacion | Multiples componentes Livewire, model binding en rutas, CustomerFactory, composicion de componentes, proyecto evaluado | `app/Http/Livewire/`, `database/factories/` | 16 |
| **18** Node.js Intro | `require`/modulos, Express (rutas, middleware, JSON), AWS SDK (DynamoDB DocumentClient), Lambda functions, API Gateway, OpenAI SDK, `dotenv` | `index.js`, `modules.js` | 12 |
| **19** Node.js Challenge | `readline` (CLI interactivo), `axios` (HTTP client), async/await, Express POST endpoint, integracion OpenAI chat completions | `index.js`, `server.js` | 18 |
| **20** GitHub Actions | Workflows YAML, eventos (push, PR, schedule, dispatch), jobs y steps, runners, variables y secretos, matrices de estrategia, cache, CI (pytest, Node, PHP, lint), CD (GitHub Pages, Vercel, Docker), releases, acciones compuestas, workflows reutilizables, concurrencia, seguridad, proyectos fullstack y monorepo | 6 secciones, 34 archivos `.yml` + `.md` | 11, 18, 19 |
| **21** Estructuras de Datos | Arrays, listas enlazadas (simples, dobles, circulares), pilas (stack), colas (queue, deque, priority queue), tablas hash (colisiones, encadenamiento, direccionamiento abierto), arboles (binarios, BST, AVL), heaps (min-heap, max-heap), grafos (dirigidos, no dirigidos, BFS, DFS) | Implementaciones y ejercicios por estructura | 00, 11 |
| **22** Algoritmos de Ordenacion | Bubble sort, selection sort, insertion sort, merge sort, quick sort, counting sort, radix sort, analisis de complejidad (Big O), estabilidad de algoritmos, comparacion de rendimiento | Implementaciones y visualizaciones por algoritmo | 21 |
| **23** TypeScript | Tipos primitivos, type annotations, interfaces, types, genericos, clases tipadas, utility types (`Partial`, `Pick`, `Omit`, `Record`), enums, union/intersection types, type guards, modulos, configuracion (`tsconfig.json`) | Archivos `.ts` y configuracion | 12 |
| **24** React Fundamentos | JSX, componentes funcionales, props, state (`useState`), efectos (`useEffect`), hooks (`useContext`, `useRef`, `useMemo`), React Router (rutas, `Link`, parametros), formularios controlados, eventos, renderizado condicional, listas y keys | Componentes `.jsx`/`.tsx`, `App.jsx` | 23 |
| **25** SQL y Bases de Datos | `SELECT`, `WHERE`, `ORDER BY`, `GROUP BY`, `HAVING`, JOINs (`INNER`, `LEFT`, `RIGHT`, `FULL`), subconsultas, normalizacion (1NF, 2NF, 3NF), indices, claves primarias y foraneas, transacciones (`BEGIN`, `COMMIT`, `ROLLBACK`), vistas | Archivos `.sql`, diagramas ER | 11 |
| **26** Accesibilidad Web | WCAG 2.1 (niveles A, AA, AAA), principios POUR (Perceptible, Operable, Comprensible, Robusto), roles y atributos ARIA, navegacion por teclado, focus management, contraste de colores, lectores de pantalla, testing de accesibilidad (axe, WAVE, Lighthouse) | Auditorias y ejemplos HTML accesibles | 10 |
| **27** Docker | Contenedores vs maquinas virtuales, imagenes, `Dockerfile` (instrucciones `FROM`, `COPY`, `RUN`, `CMD`, `EXPOSE`), Docker Compose (`docker-compose.yml`, servicios, volumenes, redes), multi-stage builds, entorno de desarrollo, entorno de produccion, Docker Hub | `Dockerfile`, `docker-compose.yml` | 20 |

---

## 4. Glosario de terminos

Los terminos estan ordenados alfabeticamente. La columna "Modulo" indica donde
aparece por primera vez en el curso.

| Termino | Definicion | Modulo | Ejemplo |
|---------|-----------|--------|---------|
| **Accesibilidad (a11y)** | Practicas para que el contenido web sea utilizable por todas las personas, incluyendo quienes usan tecnologias asistivas. | 05 | `alt="Foto del proyecto"` |
| **Action (GitHub Actions)** | Unidad reutilizable de codigo que realiza una tarea dentro de un workflow. Puede ser oficial, de la comunidad o personalizada. | 20 | `uses: actions/checkout@v4` |
| **ARIA (roles y atributos)** | Atributos que definen roles, estados y propiedades para hacer contenido web accesible a tecnologias asistivas cuando HTML semantico no es suficiente. | 26 | `role="alert"`, `aria-expanded="false"` |
| **Ancestro posicionado** | El elemento mas cercano en el arbol DOM que tiene `position` distinto de `static`. Es la referencia para `position: absolute`. | 09 | Un `div` con `position: relative` |
| **ARIA** | Accessible Rich Internet Applications. Atributos HTML que mejoran la accesibilidad cuando el HTML semantico no es suficiente. | 10 | `aria-label="Cerrar menu"` |
| **Backdrop-filter** | Propiedad CSS que aplica efectos graficos (como desenfoque) al area detras de un elemento. | 10 | `backdrop-filter: blur(10px)` |
| **Blade** | Motor de plantillas de Laravel. Permite escribir vistas con sintaxis limpia que mezcla HTML con directivas PHP especiales. | 15 | `{{ $variable }}`, `@foreach`, `@if` |
| **Bloque (block)** | Elemento que ocupa todo el ancho disponible y empieza en una nueva linea. | 01 | `<div>`, `<p>`, `<section>` |
| **Box model** | Modelo que describe como se calcula el espacio de un elemento: content + padding + border + margin. | 02 | `box-sizing: border-box` |
| **Box-sizing** | Propiedad que define si width/height incluyen padding y border (`border-box`) o no (`content-box`). | 02 | `box-sizing: border-box` |
| **Breakpoint** | Punto de ancho de pantalla donde cambian los estilos CSS mediante media queries. | 06 | `@media (min-width: 768px)` |
| **Cache** | Almacenamiento temporal del navegador. Guarda archivos descargados para no volver a pedirlos. | 09 | El CSS externo se cachea entre paginas |
| **Cascade (cascada)** | Algoritmo que determina que regla CSS "gana" cuando varias reglas afectan al mismo elemento. | 02 | Especificidad: ID > clase > tipo |
| **CI/CD** | Continuous Integration / Continuous Deployment. Practica de automatizar la compilacion, pruebas y despliegue del codigo cada vez que se hace un cambio. | 20 | Un workflow que ejecuta tests y despliega al hacer push |
| **classList** | Propiedad de JavaScript que permite manipular las clases CSS de un elemento. | 09 | `elemento.classList.add('visible')` |
| **Clamp()** | Funcion CSS que define un valor fluido con minimo, preferido y maximo. | 10 | `font-size: clamp(1rem, 3vw, 2rem)` |
| **CLS** | Cumulative Layout Shift. Metrica que mide cuanto se mueve el contenido visualmente mientras carga la pagina. | 10 | Agregar `width` y `height` a `<img>` |
| **Componente (React)** | Funcion que retorna JSX y representa una parte reutilizable de la interfaz. Puede recibir props y manejar estado propio. | 24 | `function Button({ label }) { return <button>{label}</button> }` |
| **Composicion (composite)** | Paso del renderizado donde el navegador combina las capas pintadas. Es el paso mas eficiente para animaciones. | 09 | Animar `transform` y `opacity` |
| **Contenedor (Docker)** | Instancia ejecutable de una imagen Docker. Aislado del sistema host, con su propio filesystem, red y procesos. | 27 | `docker run -p 3000:3000 mi-app` |
| **CSS Grid** | Sistema de layout bidimensional (filas y columnas) para crear disenos complejos. | 07 | `display: grid` |
| **CSS Variables** | Propiedades personalizadas que almacenan valores reutilizables. Tambien llamadas Custom Properties. | 08 | `--color-primario: #1a365d` |
| **Decorator (decorador)** | Funcion de Python que envuelve otra funcion para extender su comportamiento sin modificar su codigo. Usa la sintaxis `@nombre`. | 11 | `@login_required` sobre una funcion |
| **Design System** | Conjunto de decisiones de diseno codificadas (colores, tipografia, espaciado, componentes) para mantener consistencia. | 10 | Tokens de diseno en `:root` |
| **Design Tokens** | Valores primitivos de un design system: colores, tamanos, fuentes. | 10 | `--space-4: 1rem` |
| **Display** | Propiedad que define como se comporta un elemento en el flujo del documento. | 02 | `block`, `inline`, `flex`, `grid` |
| **Docker Compose** | Herramienta para definir y ejecutar aplicaciones Docker multi-contenedor mediante un archivo YAML. | 27 | `docker-compose up -d` con `docker-compose.yml` |
| **Dockerfile** | Archivo de texto con instrucciones para construir una imagen Docker. Define el entorno, dependencias y comandos de la aplicacion. | 27 | `FROM node:20`, `COPY . .`, `RUN npm install` |
| **DOM** | Document Object Model. Representacion en objetos del documento HTML que JavaScript puede manipular. | 09 | `document.querySelector('.nav')` |
| **Eloquent** | ORM de Laravel. Permite interactuar con la base de datos usando modelos PHP en lugar de SQL directo. Cada modelo representa una tabla. | 15 | `Curso::where('activo', true)->get()` |
| **Em** | Unidad relativa al tamano de fuente del elemento padre. | 02 | `padding: 1.5em` |
| **Especificidad** | Sistema de puntaje que determina que regla CSS se aplica cuando hay conflictos. ID (100) > clase (10) > tipo (1). | 02 | `#nav .link` tiene especificidad 110 |
| **Fixture (pytest)** | Funcion que prepara datos o estado necesario antes de ejecutar un test. Permite reutilizar configuraciones entre pruebas. | 11 | `@pytest.fixture` que retorna una conexion a BD |
| **Flexbox** | Sistema de layout unidimensional (fila o columna) para distribuir y alinear elementos. | 04 | `display: flex` |
| **Flujo normal** | El comportamiento por defecto del navegador al posicionar elementos: bloques apilados verticalmente, inline horizontalmente. | 01 | Elementos `<p>` uno debajo de otro |
| **Focus** | Estado de un elemento cuando esta seleccionado para interaccion (teclado). | 05 | `:focus { outline: 2px solid blue; }` |
| **fr** | Unidad fraccional de CSS Grid. Representa una fraccion del espacio disponible. | 07 | `grid-template-columns: 1fr 2fr 1fr` |
| **Gap** | Propiedad que define el espacio entre elementos en Flexbox o Grid. | 04 | `gap: 1rem` |
| **Generico (TypeScript)** | Parametro de tipo que permite crear funciones, clases e interfaces reutilizables que trabajan con multiples tipos manteniendo type safety. | 23 | `function identity<T>(arg: T): T { return arg; }` |
| **Generator (generador)** | Funcion de Python que usa `yield` para producir valores bajo demanda en lugar de retornar una lista completa. Ahorra memoria con grandes conjuntos de datos. | 11 | `def contar(): yield 1; yield 2` |
| **Glassmorphism** | Estilo de diseno que simula cristal translucido usando `backdrop-filter: blur()`. | 10 | Tarjetas con fondo borroso |
| **Hook (React)** | Funcion especial de React que permite usar estado y otras caracteristicas en componentes funcionales. | 24 | `const [count, setCount] = useState(0)` |
| **Imagen (Docker)** | Plantilla de solo lectura con instrucciones para crear un contenedor. Incluye el codigo, runtime, librerias y configuracion. | 27 | `docker build -t mi-app .` |
| **Indice (SQL)** | Estructura de datos que mejora la velocidad de consultas en una tabla a cambio de espacio en disco y tiempo de escritura. | 25 | `CREATE INDEX idx_email ON usuarios(email)` |
| **Inline** | Elemento que no empieza en nueva linea y solo ocupa el ancho de su contenido. | 01 | `<span>`, `<a>`, `<strong>` |
| **Interface (TypeScript)** | Contrato que define la forma de un objeto, especificando los nombres y tipos de sus propiedades y metodos. | 23 | `interface User { name: string; age: number; }` |
| **IntersectionObserver** | API de JavaScript que detecta cuando un elemento entra o sale del viewport de forma eficiente. | 09 | Animaciones de scroll reveal |
| **Iterator (iterador)** | Objeto de Python que implementa los metodos `__iter__()` y `__next__()` para recorrer una secuencia elemento por elemento. | 11 | `iter([1, 2, 3])` retorna un iterador |
| **ITCSS** | Inverted Triangle CSS. Metodologia de arquitectura CSS que organiza estilos de lo generico a lo especifico. | 10 | Settings -> Generic -> Elements -> Components |
| **JOIN (SQL)** | Operacion que combina filas de dos o mas tablas basandose en una columna relacionada. | 25 | `SELECT * FROM pedidos INNER JOIN clientes ON pedidos.cliente_id = clientes.id` |
| **JSX** | Extension de sintaxis de JavaScript que permite escribir estructura similar a HTML dentro de codigo JavaScript. Es la base de los componentes React. | 24 | `return <h1>Hola {nombre}</h1>` |
| **Layout (reflow)** | Paso del renderizado donde el navegador calcula posicion y tamano de cada elemento. Es costoso. | 09 | Cambiar `width` causa reflow |
| **Lazy loading** | Tecnica que retrasa la carga de recursos (imagenes) hasta que esten cerca de ser visibles. | 10 | `<img loading="lazy">` |
| **Livewire** | Framework de Laravel para crear interfaces reactivas usando componentes PHP del lado del servidor, sin escribir JavaScript manualmente. | 16 | `<livewire:counter />` renderiza un componente reactivo |
| **Margin** | Espacio exterior de un elemento, entre su borde y los elementos vecinos. | 02 | `margin: 1rem auto` |
| **Normalizacion (SQL)** | Proceso de organizar tablas para reducir redundancia y mejorar integridad de datos. Se aplica en formas normales (1NF, 2NF, 3NF). | 25 | Separar direcciones en su propia tabla en lugar de repetirlas |
| **Media query** | Regla CSS que aplica estilos solo cuando se cumple una condicion (ancho, orientacion, etc.). | 06 | `@media (min-width: 768px) { }` |
| **Middleware** | Capa de codigo que intercepta y filtra las peticiones HTTP antes de que lleguen al controlador. Usado para autenticacion, logging, CORS, etc. | 15 | `Route::middleware('auth')->group(...)` |
| **Mobile first** | Estrategia de diseno que empieza con la version movil y agrega complejidad para pantallas mas grandes. | 06 | Usar `min-width` en media queries |
| **Mock (mocking)** | Tecnica de testing que reemplaza dependencias reales (APIs, bases de datos) con objetos simulados para aislar la unidad bajo prueba. | 11 | `@patch('modulo.requests.get')` |
| **Open Graph** | Protocolo de meta tags que controla como se ve una pagina al compartirla en redes sociales. | 10 | `<meta property="og:title">` |
| **ORM** | Object-Relational Mapping. Tecnica que permite interactuar con bases de datos usando objetos del lenguaje en lugar de SQL directo. | 15 | Eloquent en Laravel, SQLAlchemy en Python |
| **Padding** | Espacio interior de un elemento, entre su contenido y su borde. | 02 | `padding: 1rem 2rem` |
| **Paint (repaint)** | Paso del renderizado donde el navegador rellena los pixeles de cada elemento. Costo medio. | 09 | Cambiar `color` causa repaint |
| **Position** | Propiedad CSS que define como se calcula la posicion de un elemento. | 09 | `static`, `relative`, `absolute`, `fixed`, `sticky` |
| **Preload** | Directiva que indica al navegador que descargue un recurso critico de forma anticipada. | 10 | `<link rel="preload" href="font.woff2">` |
| **Pseudo-clase** | Selector que aplica estilos segun el estado del elemento. | 05 | `:hover`, `:focus`, `:nth-child()` |
| **Pseudo-elemento** | Permite estilizar una parte especifica de un elemento o crear contenido virtual. | 10 | `::before`, `::after`, `::first-line` |
| **POUR (principios)** | Los cuatro principios de accesibilidad WCAG: Perceptible, Operable, Comprensible (Understandable) y Robusto. | 26 | Todo contenido debe ser perceptible por al menos un sentido |
| **Pytest** | Framework de testing para Python. Mas simple y potente que `unittest`, con soporte para fixtures, parametrizacion y plugins. | 11 | `def test_suma(): assert suma(2,3) == 5` |
| **querySelector** | Metodo de JavaScript que devuelve el primer elemento que coincide con un selector CSS. | 09 | `document.querySelector('.nav')` |
| **React Router** | Libreria de enrutamiento para React que permite navegacion entre vistas sin recargar la pagina. | 24 | `<Route path="/about" element={<About />} />` |
| **Rem** | Unidad relativa al tamano de fuente del elemento raiz (`<html>`). | 02 | `font-size: 1.5rem` (24px si base=16px) |
| **Responsive design** | Enfoque de diseno donde el sitio se adapta a diferentes tamanos de pantalla. | 06 | Media queries + unidades relativas |
| **Runner (GitHub Actions)** | Servidor (maquina virtual) que ejecuta los jobs de un workflow. Puede ser hospedado por GitHub o auto-hospedado. | 20 | `runs-on: ubuntu-latest` |
| **Scroll-behavior** | Propiedad CSS que controla si el desplazamiento es instantaneo o suave. | 09 | `scroll-behavior: smooth` |
| **Selector** | Patron que identifica a que elementos HTML se aplican los estilos CSS. | 02 | `.clase`, `#id`, `elemento` |
| **Semantica** | Uso de etiquetas HTML que transmiten significado sobre el contenido, no solo apariencia. | 01 | `<article>` en vez de `<div>` |
| **SEO** | Search Engine Optimization. Practicas para mejorar la visibilidad de una pagina en buscadores. | 10 | `<meta name="description">` |
| **Skip link** | Enlace oculto que permite a usuarios de teclado saltar la navegacion y llegar al contenido principal. | 10 | `<a href="#main" class="skip-link">` |
| **Stacking context** | Contexto que determina el orden de apilamiento (z-index) de los elementos. | 09 | Un `position: relative` con `z-index` crea uno |
| **Sticky** | Valor de position que actua como relative hasta un umbral de scroll, luego como fixed. | 09 | `position: sticky; top: 0` |
| **Transaccion (SQL)** | Secuencia de operaciones SQL que se ejecutan como una unidad atomica. Si una falla, todas se deshacen (rollback). | 25 | `BEGIN; UPDATE cuentas SET saldo = saldo - 100; COMMIT;` |
| **Transition** | Propiedad CSS que anima el cambio de un valor a otro de forma suave. | 05 | `transition: opacity 0.3s ease` |
| **TypeScript** | Superconjunto de JavaScript que agrega tipado estatico opcional. Se compila a JavaScript y permite detectar errores en tiempo de desarrollo. | 23 | `let name: string = "Ana"` |
| **Viewport** | El area visible del navegador donde se muestra el contenido. | 06 | `<meta name="viewport" ...>` |
| **Utility Types (TypeScript)** | Tipos predefinidos de TypeScript que transforman otros tipos para crear nuevas variantes. | 23 | `Partial<User>`, `Pick<User, 'name'>`, `Omit<User, 'id'>` |
| **Volumen (Docker)** | Mecanismo para persistir datos generados por contenedores Docker. Los datos sobreviven al reinicio o eliminacion del contenedor. | 27 | `volumes: - ./data:/var/lib/mysql` |
| **Vw / Vh** | Unidades relativas al ancho (vw) y alto (vh) del viewport. 1vw = 1% del ancho. | 06 | `width: 100vw`, `height: 100vh` |
| **WCAG** | Web Content Accessibility Guidelines. Estandar internacional de accesibilidad web con niveles A, AA y AAA. | 10 | Contraste minimo 4.5:1 para nivel AA |
| **Workflow (GitHub Actions)** | Proceso automatizado definido en un archivo YAML dentro de `.github/workflows/`. Se activa por eventos como push, pull request o un horario. | 20 | Un archivo `ci.yml` que corre tests en cada push |
| **Z-index** | Propiedad que controla el orden de apilamiento de elementos posicionados en el eje Z. | 09 | `z-index: 100` (solo con position) |

---

## 5. Recursos adicionales

### Documentacion de referencia

| Recurso | URL | Para que usarlo |
|---------|-----|-----------------|
| **MDN Web Docs -- HTML** | developer.mozilla.org/es/docs/Web/HTML | Referencia completa de etiquetas HTML |
| **MDN Web Docs -- CSS** | developer.mozilla.org/es/docs/Web/CSS | Referencia completa de propiedades CSS |
| **MDN Web Docs -- JavaScript** | developer.mozilla.org/es/docs/Web/JavaScript | Referencia del lenguaje y APIs del DOM |
| **Python -- Documentacion oficial** | docs.python.org/es/3/ | Tutorial, referencia de la biblioteca estandar y guias |
| **Laravel -- Documentacion oficial** | laravel.com/docs | Guia completa del framework: Eloquent, Blade, Livewire, rutas, middleware |
| **Node.js -- Documentacion oficial** | nodejs.org/docs/latest/api/ | Referencia de modulos core: fs, http, path, events |
| **Express -- Documentacion oficial** | expressjs.com/es/ | Guia del framework web para Node.js |
| **PHP -- Manual oficial** | php.net/manual/es/ | Referencia completa del lenguaje PHP |
| **GitHub Actions -- Documentacion** | docs.github.com/es/actions | Guia completa de workflows, sintaxis YAML, acciones y runners |
| **TypeScript -- Documentacion oficial** | typescriptlang.org/docs/ | Manual del lenguaje, handbook y referencia de tipos |
| **React -- Documentacion oficial** | react.dev | Tutorial, referencia de API, hooks y patrones |
| **Docker -- Documentacion oficial** | docs.docker.com | Guia de Dockerfile, Compose, redes y volumenes |
| **W3Schools** | w3schools.com | Tutoriales interactivos para principiantes |

### Guias especializadas

| Recurso | URL | Tema |
|---------|-----|------|
| **A Complete Guide to Flexbox** | css-tricks.com/snippets/css/a-guide-to-flexbox/ | Todo sobre Flexbox con diagramas |
| **A Complete Guide to CSS Grid** | css-tricks.com/snippets/css/complete-guide-grid/ | Todo sobre Grid con diagramas |
| **Learn CSS Layout** | learnlayout.com | Conceptos de layout paso a paso |
| **Flexbox Froggy** | flexboxfroggy.com | Juego para aprender Flexbox |
| **Grid Garden** | cssgridgarden.com | Juego para aprender CSS Grid |
| **Real Python** | realpython.com | Tutoriales y articulos de Python con profundidad |
| **Pytest -- Documentacion** | docs.pytest.org | Guia oficial del framework de testing para Python |
| **Laracasts** | laracasts.com | Video tutoriales de Laravel y PHP moderno |
| **TypeScript Playground** | typescriptlang.org/play | Editor en linea para experimentar con TypeScript |
| **React Tutorial** | react.dev/learn | Tutorial oficial interactivo de React |
| **SQLBolt** | sqlbolt.com | Ejercicios interactivos para aprender SQL |
| **WebAIM -- Intro to Accessibility** | webaim.org/intro/ | Introduccion completa a la accesibilidad web |
| **Docker -- Get Started** | docs.docker.com/get-started/ | Tutorial oficial paso a paso de Docker |

### Compatibilidad de navegadores

| Recurso | URL | Para que usarlo |
|---------|-----|-----------------|
| **Can I Use** | caniuse.com | Verificar soporte de propiedades CSS y APIs JS en navegadores |
| **Baseline** | web.dev/baseline | Estado de soporte de features web modernas |

### Herramientas de accesibilidad

| Recurso | URL | Para que usarlo |
|---------|-----|-----------------|
| **WAVE** | wave.webaim.org | Evaluador de accesibilidad web online |
| **axe DevTools** | extension de Chrome/Firefox | Auditoria de accesibilidad en DevTools |
| **WebAIM Contrast Checker** | webaim.org/resources/contrastchecker/ | Verificar contraste de colores (WCAG) |
| **Lighthouse** | integrado en Chrome DevTools | Auditoria de performance, a11y, SEO |

### Herramientas de desarrollo

| Herramienta | Para que |
|-------------|----------|
| **Visual Studio Code** | Editor de codigo recomendado |
| **Extension: Live Server** | Servidor local con recarga automatica |
| **Extension: Prettier** | Formato automatico de codigo |
| **Extension: HTMLHint** | Validacion de HTML en tiempo real |
| **Extension: PHP Intelephense** | Autocompletado y analisis para PHP |
| **Extension: Python** | Soporte para Python (linting, debugging, IntelliSense) |
| **Chrome DevTools** | Inspeccionar elementos, debuggear CSS, performance |
| **Firefox DevTools** | Excelentes herramientas de Grid y Flexbox |
| **Postman** | Probar y documentar APIs REST |
| **Docker Desktop** | Contenedores para desarrollo local y CI/CD |

### Validadores

| Recurso | URL | Para que |
|---------|-----|----------|
| **W3C HTML Validator** | validator.w3.org | Validar que el HTML sea correcto |
| **W3C CSS Validator** | jigsaw.w3.org/css-validator/ | Validar que el CSS sea correcto |
| **Google Rich Results Test** | search.google.com/test/rich-results | Probar datos estructurados |
| **OpenGraph Preview** | opengraph.xyz | Vista previa de Open Graph |

---

## 6. Como seguir aprendiendo

### Siguientes pasos despues de este curso

```
                    TU RECORRIDO DE APRENDIZAJE
  ═══════════════════════════════════════════════════════

  ┌─────────────────────────────────┐
  │  ESTE CURSO                     │
  │  00-27: Web + Python + PHP +    │     ← Estas aqui
  │  Laravel + Node.js + CI/CD +    │
  │  Estructuras de datos + Algos + │
  │  TypeScript + React + SQL +     │
  │  Accesibilidad + Docker         │
  └──────────────┬──────────────────┘
                 │
         ┌───────┴───────┐
         ▼               ▼
  ┌──────────────┐  ┌──────────────┐
  │ Profundizar  │  │ Profundizar  │
  │ Frontend     │  │ Backend      │
  │              │  │              │
  │ - React      │  │ - Django /   │
  │   avanzado / │  │   FastAPI    │
  │   Next.js    │  │ - Bases de   │
  │ - Vue /      │  │   datos      │
  │   Svelte     │  │   avanzadas  │
  │ - Animaciones│  │ - GraphQL    │
  │   @keyframes │  │ - Microserv. │
  │ - SSR / SSG  │  │              │
  └──────┬───────┘  └──────┬───────┘
         │                 │
         └────────┬────────┘
                  ▼
         ┌──────────────────┐
         │  DevOps y Cloud   │
         │                   │
         │  - Kubernetes     │
         │  - AWS / GCP /    │
         │    Azure          │
         │  - Terraform      │
         │  - Monitoreo      │
         └────────┬─────────┘
                  │
                  ▼
         ┌──────────────────┐
         │  Especializacion  │
         │                   │
         │  - Data Science   │
         │  - Machine Learn. │
         │  - Mobile (React  │
         │    Native/Flutter)│
         │  - Seguridad web  │
         │  - Arquitectura   │
         │    de software    │
         └──────────────────┘
```

### Ruta recomendada

```
SEMANAS 1-4:   Profundizar lo aprendido
               - JavaScript avanzado (ES6+, async/await, modulos)
               - Python: librerias populares (requests, pandas, Flask)
               - Practicar con proyectos propios

SEMANAS 5-8:   Framework frontend (elige uno)
               - React (el mas demandado laboralmente)
               - Vue (curva de aprendizaje mas suave)
               - Svelte (el mas innovador)

SEMANAS 9-12:  DevOps y herramientas avanzadas
               - Docker (contenedores, docker-compose)
               - Cloud (AWS, GCP o Azure — nivel basico)
               - Bases de datos avanzadas (PostgreSQL, MongoDB, Redis)

SEMANAS 13-16: Especializacion
               - Backend avanzado (Django, FastAPI, NestJS)
               - Testing E2E (Cypress, Playwright)
               - Arquitectura de software (clean code, patrones)

SEMANAS 17+:   Mundo profesional
               - Contribuir a proyectos open source
               - Construir un portfolio completo
               - Preparar entrevistas tecnicas
```

### Ideas de proyectos para practicar

Despues de completar este curso, estos proyectos reforzaran tus habilidades:

| Proyecto | Habilidades que practica | Dificultad |
|----------|------------------------|------------|
| **Blog personal** | HTML semantico, tipografia, multi-pagina, responsive | Baja |
| **Clon de landing** | Elige un sitio que te guste y replica su diseno | Media |
| **Calculadora** | HTML/CSS + JavaScript (eventos, logica) | Media |
| **Galeria de fotos** | CSS Grid, Flexbox, lazy loading, filtros CSS | Media |
| **API REST con Express** | Node.js, Express, JSON, validacion, middleware | Media |
| **App de tareas con Laravel** | CRUD, Eloquent, Blade, Livewire, autenticacion | Media |
| **Dashboard** | Grid complejo, graficas (con libreria), variables CSS | Alta |
| **Tienda online (maqueta)** | Componentes, responsive, formularios, accesibilidad | Alta |
| **App del clima** | Fetch API, JavaScript, diseno responsive, async/await | Alta |
| **CLI de productividad** | Python, archivos, JSON, decoradores, testing con pytest | Alta |
| **Pipeline CI/CD propio** | GitHub Actions, Docker, tests automatizados, deploy | Alta |

### Comunidades y recursos en espanol

| Comunidad / Recurso | Descripcion |
|---------------------|-------------|
| **MDN en espanol** | La documentacion de Mozilla traducida al espanol |
| **FreeCodeCamp (espanol)** | Cursos gratuitos de desarrollo web con certificaciones |
| **Platzi** | Plataforma de cursos en espanol (de pago, con comunidad activa) |
| **Codigo Facilito** | Tutoriales y cursos de programacion en espanol |
| **Dev.to (tag #spanish)** | Articulos tecnicos de la comunidad en espanol |
| **Stack Overflow en espanol** | Preguntas y respuestas tecnicas en espanol |
| **GitHub** | Busca proyectos open source para contribuir y aprender |
| **Discord / Telegram** | Busca comunidades de desarrollo web en espanol en tu pais |

### Consejos finales

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│  1. PRACTICA TODOS LOS DIAS                                         │
│     Aunque sean 30 minutos. La consistencia supera a la intensidad. │
│                                                                     │
│  2. CONSTRUYE PROYECTOS REALES                                      │
│     Los tutoriales ensenan, pero los proyectos consolidan.          │
│     Cuando te atores, busca la solucion. Ese proceso es aprender.   │
│                                                                     │
│  3. LEE CODIGO DE OTROS                                             │
│     Inspecciona sitios web que admires con DevTools.                │
│     Lee codigo open source en GitHub.                               │
│                                                                     │
│  4. NO MEMORICES, COMPRENDE                                         │
│     No necesitas recordar cada propiedad CSS de memoria.            │
│     Necesitas entender los conceptos para saber que buscar.         │
│                                                                     │
│  5. COMPARTE LO QUE APRENDES                                       │
│     Escribe un blog, haz un video, ayuda en foros.                  │
│     Ensenar es la mejor forma de aprender.                          │
│                                                                     │
│  6. NO TE COMPARES                                                  │
│     Cada persona tiene su ritmo. Lo importante es seguir avanzando. │
│                                                                     │
│  7. AUTOMATIZA DESDE EL INICIO                                     │
│     Usa CI/CD, linters y tests desde tu primer proyecto.            │
│     Los buenos habitos se forman temprano.                          │
│                                                                     │
│  8. EXPLORA DEVOPS Y CLOUD                                         │
│     Docker, GitHub Actions y servicios cloud son habilidades        │
│     cada vez mas valoradas en la industria.                         │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

> **Gracias por tomar este curso.** El desarrollo web y la programacion son campos que evolucionan
> constantemente, y lo que has aprendido aqui — desde HTML basico hasta CI/CD con GitHub Actions,
> estructuras de datos, algoritmos de ordenacion, TypeScript, React, SQL, accesibilidad web
> y Docker — es una base solida sobre la que puedes construir cualquier cosa. Sigue practicando,
> sigue construyendo, y sigue aprendiendo.

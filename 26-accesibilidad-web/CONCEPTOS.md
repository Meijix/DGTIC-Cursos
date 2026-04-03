# Modulo 26: Accesibilidad Web (a11y)

## Indice de contenidos

1. [Que es la accesibilidad web?](#1-que-es-la-accesibilidad-web)
2. [Por que importa](#2-por-que-importa)
3. [WCAG 2.1 — Niveles de conformidad](#3-wcag-21--niveles-de-conformidad)
4. [Principios POUR](#4-principios-pour)
5. [El arbol de accesibilidad](#5-el-arbol-de-accesibilidad)
6. [Estadisticas sobre discapacidad](#6-estadisticas-sobre-discapacidad)
7. [Tecnologias de asistencia](#7-tecnologias-de-asistencia)
8. [Mapa del modulo](#8-mapa-del-modulo)

---

## 1. Que es la accesibilidad web?

La accesibilidad web (abreviada **a11y** — la "a", 11 letras, la "y") es la practica de disenar y desarrollar sitios web que puedan ser utilizados por **todas las personas**, incluyendo aquellas con discapacidades visuales, auditivas, motoras o cognitivas.

No se trata de crear una version "especial" del sitio, sino de construir desde el inicio de forma inclusiva. Un sitio accesible beneficia a todos: usuarios con discapacidades permanentes, temporales (brazo roto) o situacionales (sol en la pantalla).

---

## 2. Por que importa

### Argumento moral
Toda persona tiene derecho a acceder a la informacion y servicios en linea. Excluir usuarios con discapacidades es equivalente a construir un edificio sin rampa.

### Argumento legal
- **Europa:** Directiva de Accesibilidad Web (EN 301 549)
- **EE.UU.:** ADA (Americans with Disabilities Act), Seccion 508
- **Mexico:** NOM-035, Ley Federal para Prevenir la Discriminacion
- Las demandas por inaccesibilidad web aumentan cada anio

### Argumento de negocio
- El 15-20% de la poblacion mundial tiene alguna discapacidad
- Mejor SEO: Google favorece sitios accesibles
- Mayor audiencia y alcance de mercado
- Mejor experiencia de usuario para todos

---

## 3. WCAG 2.1 — Niveles de conformidad

Las **Web Content Accessibility Guidelines** (WCAG) son el estandar internacional de accesibilidad web, publicado por el W3C.

```
Nivel A         Nivel AA           Nivel AAA
=========       ==========         ===========
Minimo          Recomendado        Optimo
indispensable   objetivo comun     aspiracional

- Alt text       - Contraste 4.5:1   - Contraste 7:1
- Navegacion     - Redimensionar      - Lenguaje de signos
  por teclado      texto 200%        - Audiodescripcion
- Labels en      - Consistencia en     extendida
  formularios      navegacion        - Identificacion
                 - Identificacion       de proposito
                   de errores        - Sin limites de
                                       tiempo
```

### Criterios de exito

WCAG define criterios de exito medibles. Ejemplo:

| Criterio | Nivel | Descripcion |
|----------|-------|-------------|
| 1.1.1 Contenido no textual | A | Todo contenido no textual tiene alternativa |
| 1.4.3 Contraste minimo | AA | Texto normal 4.5:1, texto grande 3:1 |
| 2.1.1 Teclado | A | Toda funcionalidad accesible por teclado |
| 2.4.7 Foco visible | AA | El foco del teclado es visible |
| 3.3.1 Identificacion de errores | A | Los errores se describen al usuario |
| 4.1.2 Nombre, rol, valor | A | Los componentes tienen nombre y rol accesibles |

---

## 4. Principios POUR

WCAG se organiza en 4 principios fundamentales:

```
  P.O.U.R. — Los 4 pilares de la accesibilidad web

  ┌─────────────────────────────────────────────────────────────────────┐
  │                                                                     │
  │   PERCEIVABLE          OPERABLE           UNDERSTANDABLE            │
  │   (Perceptible)        (Operable)         (Comprensible)           │
  │                                                                     │
  │   La informacion       Los componentes    La informacion y         │
  │   debe poder ser       de la interfaz     la operacion de la       │
  │   percibida por        deben poder ser    interfaz deben ser       │
  │   al menos un          operados por       comprensibles            │
  │   sentido              el usuario                                   │
  │                                                                     │
  │   - Alt text           - Navegacion       - Lenguaje claro         │
  │   - Subtitulos           por teclado      - Comportamiento         │
  │   - Contraste          - Tiempo              predecible            │
  │   - No solo color        suficiente       - Ayuda con errores      │
  │                        - Sin destellos                              │
  │                                                                     │
  │   ─────────────────────────────────────────────────────────────     │
  │                                                                     │
  │   ROBUST (Robusto)                                                  │
  │                                                                     │
  │   El contenido debe ser lo suficientemente robusto para ser         │
  │   interpretado por una amplia variedad de agentes de usuario,       │
  │   incluyendo tecnologias de asistencia.                             │
  │                                                                     │
  │   - HTML semantico valido                                           │
  │   - ARIA correctamente implementado                                 │
  │   - Compatibilidad con lectores de pantalla                         │
  │                                                                     │
  └─────────────────────────────────────────────────────────────────────┘
```

---

## 5. El arbol de accesibilidad

El navegador construye un **arbol de accesibilidad** a partir del DOM. Este arbol es lo que los lectores de pantalla y otras tecnologias de asistencia utilizan para presentar el contenido.

```
  DOM (lo que escribes)          Arbol de accesibilidad (lo que el lector ve)
  ====================           ============================================

  <header>                       banner
    <nav>                          navigation
      <ul>                           list (3 items)
        <li><a>Inicio</a></li>        link "Inicio"
        <li><a>Blog</a></li>          link "Blog"
        <li><a>Contacto</a></li>      link "Contacto"
      </ul>
    </nav>
  </header>
  <main>                         main
    <h1>Bienvenido</h1>            heading level 1 "Bienvenido"
    <p>Texto...</p>                text "Texto..."
    <button>Enviar</button>        button "Enviar"
    <img alt="Logo">               img "Logo"
    <img alt="">                   (ignorada — decorativa)
  </main>
  <footer>                       contentinfo
    <p>2026 Mi Sitio</p>            text "2026 Mi Sitio"
  </footer>
```

### Lo que incluye cada nodo del arbol

```
  Nodo del arbol de accesibilidad
  ┌──────────────────────────────┐
  │ Rol:    button               │  ← Que tipo de elemento es
  │ Nombre: "Enviar formulario"  │  ← Texto accesible (label)
  │ Estado: disabled             │  ← Estados actuales (ARIA)
  │ Valor:  —                    │  ← Valor actual (si aplica)
  └──────────────────────────────┘
```

Si usas `<div onclick="...">` en lugar de `<button>`, el arbol de accesibilidad no sabra que es un boton. Por eso el HTML semantico es fundamental.

---

## 6. Estadisticas sobre discapacidad

```
  Tipo de discapacidad          Prevalencia mundial       Ejemplo web
  ========================      ====================      ==========================
  Visual (baja vision, ceguera)    ~2.2 mil millones       Lectores de pantalla, zoom
  Auditiva (sordera, hipoacusia)   ~430 millones            Subtitulos, transcripciones
  Motora (movilidad reducida)      ~200 millones            Navegacion por teclado
  Cognitiva (dislexia, TDAH)       ~200 millones            Lenguaje simple, estructura
  Situacional (temporal)           Todos en algun momento   Sol, ruido, un brazo ocupado

  Total: ~1,300 millones de personas viven con alguna discapacidad significativa
         (16% de la poblacion mundial — OMS, 2023)
```

### Discapacidades temporales y situacionales

No solo las discapacidades permanentes importan:

- **Permanente:** persona ciega → lector de pantalla
- **Temporal:** cirugia ocular → necesita alto contraste
- **Situacional:** sol directo en pantalla → necesita alto contraste

La accesibilidad beneficia a todos.

---

## 7. Tecnologias de asistencia

| Tecnologia | Usuarios | Interaccion con la web |
|------------|----------|------------------------|
| Lector de pantalla (NVDA, JAWS, VoiceOver) | Usuarios ciegos | Lee el arbol de accesibilidad en voz alta |
| Magnificador de pantalla (ZoomText) | Baja vision | Amplifica zonas de la pantalla |
| Navegacion por teclado | Usuarios con discapacidad motora | Tab, Enter, flechas, Escape |
| Switch / pulsador | Movilidad muy reducida | Un solo boton para navegar |
| Software de reconocimiento de voz | Movilidad reducida | Comandos de voz para interactuar |
| Lineas braille | Usuarios ciegos | Muestra texto en braille en tiempo real |

---

## 8. Mapa del modulo

| Seccion | Tema | Enfoque |
|---------|------|---------|
| 01-fundamentos-wcag | Fundamentos y WCAG | HTML semantico, landmarks, ARIA basico |
| 02-formularios-accesibles | Formularios accesibles | Labels, errores, validacion accesible |
| 03-navegacion-teclado | Navegacion por teclado | Tab order, skip links, focus management |
| 04-multimedia | Multimedia accesible | Alt text, subtitulos, transcripciones |
| 05-color-contraste | Color y contraste | Ratios WCAG, daltonismo, indicadores |
| 06-testing-auditoria | Testing y auditoria | Herramientas, checklists, screen readers |

# React Fundamentos — Conceptos Generales

## Que es React?

React es una **biblioteca de JavaScript** para construir interfaces de usuario,
creada por Facebook (Meta) en 2013. Se centra en la capa de vista y utiliza un
modelo declarativo basado en **componentes reutilizables**.

---

## Modelo de Componentes

En React, toda la interfaz se construye con componentes: piezas independientes
y reutilizables que encapsulan su propia logica, estado y presentacion.

```
  Arbol de Componentes — Aplicacion de Tareas
  =============================================

         <App>
        /     \
  <Header>   <Main>
              /    \
        <TaskForm>  <TaskList>
                     /   |   \
                <Task> <Task> <Task>
```

Cada componente:
- Recibe datos via **props** (solo lectura)
- Puede tener **estado** interno (useState)
- Retorna **JSX** que describe la interfaz

---

## Virtual DOM

React no manipula el DOM directamente. Usa un **Virtual DOM** (representacion
en memoria del DOM real) para calcular los cambios minimos necesarios.

```
  Estado anterior          Estado nuevo
  +-----------+           +-----------+
  | VDOM v1   |           | VDOM v2   |
  +-----------+           +-----------+
        \                      /
         \    Diffing Alg.    /
          +--------+---------+
                   |
           Cambios minimos
                   |
                   v
          +----------------+
          |   DOM Real     |
          | (solo patches) |
          +----------------+
```

Ventajas:
- Rendimiento optimizado (batch updates)
- API declarativa (describes QUE quieres, no COMO)
- Reconciliacion eficiente

---

## JSX — JavaScript XML

JSX es una extension de sintaxis que permite escribir HTML dentro de JavaScript.
No es obligatorio, pero es el estandar en React.

```jsx
// JSX se transforma a llamadas React.createElement()
const elemento = <h1 className="titulo">Hola Mundo</h1>;

// Equivalente sin JSX:
const elemento = React.createElement('h1', { className: 'titulo' }, 'Hola Mundo');
```

Reglas clave de JSX:
- Usar `className` en vez de `class`
- Expresiones JS dentro de `{llaves}`
- Todo debe tener un solo elemento raiz (o usar `<Fragment>`)
- Los componentes se nombran en PascalCase

---

## Flujo de Datos Unidireccional

React sigue un flujo de datos de **arriba hacia abajo** (one-way data flow).
Los datos fluyen de padres a hijos via props, nunca al reves.

```
  Flujo de Datos en React
  ========================

  [Estado en App]
        |
        | props
        v
  [Componente Padre]
      /         \
     | props     | props
     v           v
  [Hijo A]    [Hijo B]

  Para comunicar hijo -> padre:
  Se pasan funciones callback como props

  App (estado + callback) --props--> Hijo
  Hijo --ejecuta callback--> App actualiza estado
  App --re-render con nuevo estado--> Hijo
```

---

## React vs Vue — Comparativa Breve

| Aspecto             | React                    | Vue                       |
|---------------------|--------------------------|---------------------------|
| Tipo                | Biblioteca (vista)       | Framework progresivo      |
| Sintaxis plantillas | JSX (JS + HTML)          | Templates HTML + directivas|
| Estado              | Hooks (useState, etc.)   | Composition API / Options |
| Reactividad         | Inmutable (setState)     | Reactiva (proxy)          |
| Ecosistema          | Amplio, muchas opciones  | Mas integrado, opinado    |
| Curva aprendizaje   | Requiere mas JS puro     | Mas accesible inicialmente|
| Comunidad           | Muy grande (Meta)        | Grande (comunidad indie)  |
| Ideal para          | Apps grandes, flexibles  | Apps rapidas, prototipado |

---

## Ecosistema React

```
  React Core
    |
    +-- React DOM (renderizado web)
    +-- React Native (apps moviles)
    |
  Librerias complementarias:
    +-- React Router (navegacion SPA)
    +-- Redux / Zustand (estado global)
    +-- React Query / SWR (fetching datos)
    +-- React Hook Form (formularios)
    +-- Styled Components / Tailwind (estilos)
    +-- Vite / Next.js (tooling / SSR)
```

---

## Requisitos Previos

Para aprovechar este modulo necesitas:
- JavaScript moderno (ES6+): arrow functions, destructuring, modules, promises
- HTML y CSS basico
- Familiaridad con la terminal y npm/npx
- Node.js instalado (v18+)

## Crear un Proyecto

```bash
# Con Vite (recomendado)
npm create vite@latest mi-app -- --template react
cd mi-app
npm install
npm run dev
```

---

> **Navegacion**: Cada seccion (01-07) contiene su propio `CONCEPTOS.md`,
> `CHEATSHEET.md` y `ejemplos.jsx` con codigo ejecutable.

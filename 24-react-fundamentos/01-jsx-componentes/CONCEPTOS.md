# 01 — JSX y Componentes

## Que es JSX?

JSX (JavaScript XML) es una extension de sintaxis para JavaScript que permite
escribir estructuras similares a HTML dentro del codigo JS. React lo utiliza
para describir como debe verse la interfaz.

```
  Transformacion JSX
  ===================

  Codigo JSX                  React.createElement()
  +------------------+        +---------------------------+
  | <h1>Hola</h1>   |  --->  | createElement('h1',       |
  +------------------+        |   null, 'Hola')           |
                              +---------------------------+
                                        |
                                        v
                              +---------------------------+
                              | { type: 'h1',             |
                              |   props: {                |
                              |     children: 'Hola'      |
                              |   }                       |
                              | }                         |
                              +---------------------------+
```

JSX NO es HTML. Es azucar sintactico que se transpila a llamadas de funciones.

---

## Expresiones en JSX

Dentro de JSX se pueden insertar expresiones JavaScript usando `{llaves}`:

```jsx
const nombre = "Maria";
const edad = 28;

return (
  <div>
    <p>Nombre: {nombre}</p>
    <p>Edad: {edad}</p>
    <p>Mayor de edad: {edad >= 18 ? 'Si' : 'No'}</p>
    <p>Doble: {edad * 2}</p>
    <p>Fecha: {new Date().toLocaleDateString()}</p>
  </div>
);
```

Solo se permiten **expresiones** (retornan un valor), no sentencias como `if` o `for`.

---

## Componentes Funcionales

Un componente es una funcion que retorna JSX. Se nombra en **PascalCase**.

```
  Anatomia de un Componente
  ==========================

  function MiComponente(props) {    <-- funcion con PascalCase
    |                                    recibe props como argumento
    |  // logica, hooks, variables
    |
    return (                         <-- retorna JSX
      <div>
        <h1>{props.titulo}</h1>
      </div>
    );
  }

  // Uso:
  <MiComponente titulo="Hola" />     <-- se usa como etiqueta HTML
```

---

## Composicion de Componentes

React se basa en componer componentes pequenos para formar interfaces complejas.

```
  Arbol de Composicion
  =====================

          <App>
         /     \
   <Navbar>    <Main>
    /    \      /    \
 <Logo> <Nav> <Hero> <Cards>
                      / | \
              <Card> <Card> <Card>
```

Cada componente es independiente, reutilizable y testeable por separado.

---

## Fragments

Cuando necesitas retornar multiples elementos sin un contenedor extra en el DOM:

```jsx
// Con Fragment completo
import { Fragment } from 'react';

function Lista() {
  return (
    <Fragment>
      <li>Elemento 1</li>
      <li>Elemento 2</li>
    </Fragment>
  );
}

// Con sintaxis corta (recomendado)
function Lista() {
  return (
    <>
      <li>Elemento 1</li>
      <li>Elemento 2</li>
    </>
  );
}
```

---

## Children Prop

Todo lo que se coloca entre las etiquetas de un componente se pasa como `children`:

```jsx
function Tarjeta({ children, titulo }) {
  return (
    <div className="tarjeta">
      <h2>{titulo}</h2>
      <div className="contenido">
        {children}
      </div>
    </div>
  );
}

// Uso:
<Tarjeta titulo="Perfil">
  <img src="foto.jpg" alt="Perfil" />
  <p>Descripcion del usuario</p>
</Tarjeta>
```

```
  Flujo de children
  ==================

  <Tarjeta titulo="Perfil">      props.titulo = "Perfil"
    <img ... />                   props.children = [<img>, <p>]
    <p>Descripcion</p>
  </Tarjeta>

  Renderizado final:
  +------------------+
  | Perfil           |   <-- titulo
  |  [img]           |   <-- children[0]
  |  Descripcion     |   <-- children[1]
  +------------------+
```

---

## Reglas Clave de JSX

| HTML              | JSX                    | Razon                         |
|-------------------|------------------------|-------------------------------|
| `class`           | `className`            | class es palabra reservada JS |
| `for`             | `htmlFor`              | for es palabra reservada JS   |
| `onclick`         | `onClick`              | camelCase para eventos        |
| `style="color:r"` | `style={{color:'r'}}`  | objeto JS, no string          |
| `tabindex`        | `tabIndex`             | camelCase para atributos      |

- Todo componente debe retornar un **solo elemento raiz**
- Las etiquetas vacias se auto-cierran: `<img />`, `<input />`, `<br />`
- Los componentes propios usan PascalCase: `<MiComponente />`
- Los elementos HTML usan minusculas: `<div>`, `<span>`

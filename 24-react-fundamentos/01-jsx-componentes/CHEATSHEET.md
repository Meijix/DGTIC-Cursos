# 01 — JSX y Componentes — Cheatsheet

## Sintaxis JSX Basica

```jsx
// Expresiones en llaves
<p>{variable}</p>
<p>{2 + 2}</p>
<p>{condicion ? 'si' : 'no'}</p>
<p>{arreglo.length}</p>

// Atributos
<div className="contenedor">          // class -> className
<label htmlFor="email">               // for -> htmlFor
<img src={urlVariable} alt="foto" />  // auto-cierre obligatorio
<div style={{ color: 'blue', fontSize: '16px' }}>  // objeto JS
```

## Componente Funcional

```jsx
// Declaracion basica
function Saludo() {
  return <h1>Hola Mundo</h1>;
}

// Arrow function
const Saludo = () => <h1>Hola Mundo</h1>;

// Con props
function Saludo({ nombre, edad }) {
  return <p>Soy {nombre}, tengo {edad} anios</p>;
}

// Uso
<Saludo nombre="Ana" edad={25} />
```

## Fragments

```jsx
// Sintaxis corta (preferida)
<>
  <h1>Titulo</h1>
  <p>Parrafo</p>
</>

// Con key (necesario en listas)
<Fragment key={id}>
  <dt>{termino}</dt>
  <dd>{definicion}</dd>
</Fragment>
```

## Children

```jsx
// Definir componente contenedor
function Caja({ children }) {
  return <div className="caja">{children}</div>;
}

// Usar con contenido
<Caja>
  <p>Cualquier contenido aqui</p>
  <button>Click</button>
</Caja>
```

## Composicion

```jsx
// Componentes pequenos componen grandes
function App() {
  return (
    <>
      <Header />
      <main>
        <Sidebar />
        <Contenido />
      </main>
      <Footer />
    </>
  );
}
```

## Renderizado Condicional en JSX

```jsx
// Ternario
{logueado ? <Dashboard /> : <Login />}

// AND logico
{error && <MensajeError texto={error} />}

// Variable JSX
let contenido;
if (cargando) contenido = <Spinner />;
else contenido = <Datos />;
return <div>{contenido}</div>;
```

## Listas

```jsx
{items.map(item => (
  <Elemento key={item.id} dato={item} />
))}
```

## Reglas Rapidas

- PascalCase para componentes: `<MiComponente />`
- minusculas para HTML: `<div>`, `<span>`
- Un solo elemento raiz por return
- `className` en vez de `class`
- Eventos en camelCase: `onClick`, `onChange`
- Cerrar todas las etiquetas: `<br />`, `<input />`

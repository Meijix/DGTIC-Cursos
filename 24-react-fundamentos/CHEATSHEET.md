# React Fundamentos — Cheatsheet

## JSX Rapido

```jsx
// Expresiones en JSX
<p>{nombre.toUpperCase()}</p>
<p>{edad >= 18 ? 'Adulto' : 'Menor'}</p>
<p>{items.length > 0 && <Lista items={items} />}</p>

// Atributos dinamicos
<img src={urlImagen} alt={descripcion} />
<div className={activo ? 'activo' : 'inactivo'}>...</div>
<input style={{ color: 'red', fontSize: '14px' }} />
```

## Hooks Esenciales

```jsx
// useState — Estado local
const [valor, setValor] = useState(valorInicial);
setValor(nuevoValor);
setValor(prev => prev + 1);  // actualizacion funcional

// useEffect — Efectos secundarios
useEffect(() => {
  // efecto al montar y cuando cambian dependencias
  return () => { /* cleanup al desmontar */ };
}, [dependencia1, dependencia2]);

useEffect(() => { /* solo al montar */ }, []);
useEffect(() => { /* en cada render */ });

// useContext — Consumir contexto
const valor = useContext(MiContexto);

// useReducer — Estado complejo
const [state, dispatch] = useReducer(reducer, estadoInicial);
dispatch({ type: 'ACCION', payload: datos });

// useMemo — Valor memoizado
const resultado = useMemo(() => calculoCostoso(a, b), [a, b]);

// useCallback — Funcion memoizada
const handleClick = useCallback(() => {
  hacerAlgo(id);
}, [id]);

// useRef — Referencia mutable / acceso DOM
const inputRef = useRef(null);
inputRef.current.focus();
```

## Manejo de Eventos

```jsx
<button onClick={handleClick}>Click</button>
<button onClick={() => handleDelete(id)}>Borrar</button>
<input onChange={(e) => setNombre(e.target.value)} />
<form onSubmit={(e) => { e.preventDefault(); enviar(); }}>
```

## Renderizado Condicional

```jsx
// Ternario
{condicion ? <CompA /> : <CompB />}

// AND logico (solo renderizar si true)
{mostrar && <Componente />}

// Early return
if (cargando) return <Spinner />;
if (error) return <Error mensaje={error} />;
return <Contenido datos={datos} />;
```

## Listas y Keys

```jsx
{items.map(item => (
  <li key={item.id}>{item.nombre}</li>
))}

// NUNCA usar indice como key si la lista cambia
// SIEMPRE usar un identificador unico y estable
```

## Props

```jsx
// Pasar props
<Hijo nombre="Ana" edad={25} activo={true} />
<Hijo {...objetoProps} />

// Recibir y destructurar
function Hijo({ nombre, edad, activo = false }) { ... }

// Children
<Contenedor>
  <p>Contenido hijo</p>
</Contenedor>
function Contenedor({ children }) {
  return <div className="caja">{children}</div>;
}
```

## Formularios Controlados

```jsx
const [email, setEmail] = useState('');
<input
  type="email"
  value={email}
  onChange={(e) => setEmail(e.target.value)}
/>
```

## React Router v6

```jsx
import { BrowserRouter, Routes, Route, Link, useParams } from 'react-router-dom';

<BrowserRouter>
  <nav><Link to="/inicio">Inicio</Link></nav>
  <Routes>
    <Route path="/" element={<Home />} />
    <Route path="/usuario/:id" element={<Usuario />} />
    <Route path="*" element={<NoEncontrado />} />
  </Routes>
</BrowserRouter>

// Leer parametros
const { id } = useParams();

// Navegacion programatica
const navigate = useNavigate();
navigate('/inicio');
```

## Custom Hooks

```jsx
// Extraer logica reutilizable
function useLocalStorage(key, valorInicial) {
  const [valor, setValor] = useState(
    () => JSON.parse(localStorage.getItem(key)) ?? valorInicial
  );
  useEffect(() => {
    localStorage.setItem(key, JSON.stringify(valor));
  }, [key, valor]);
  return [valor, setValor];
}
```

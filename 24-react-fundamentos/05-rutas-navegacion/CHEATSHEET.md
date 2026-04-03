# 05 — Rutas y Navegacion — Cheatsheet

## Instalacion

```bash
npm install react-router-dom
```

## Setup Basico

```jsx
import { BrowserRouter, Routes, Route } from 'react-router-dom';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/acerca" element={<Acerca />} />
        <Route path="*" element={<NotFound />} />
      </Routes>
    </BrowserRouter>
  );
}
```

## Link y NavLink

```jsx
import { Link, NavLink } from 'react-router-dom';

// Link simple
<Link to="/acerca">Acerca</Link>

// NavLink con clase activa
<NavLink
  to="/acerca"
  className={({ isActive }) => isActive ? "nav-activo" : ""}
>
  Acerca
</NavLink>

// NavLink con estilo activo
<NavLink
  to="/acerca"
  style={({ isActive }) => ({ fontWeight: isActive ? "bold" : "normal" })}
>
  Acerca
</NavLink>
```

## Parametros Dinamicos

```jsx
// Definir ruta
<Route path="/usuario/:id" element={<Usuario />} />
<Route path="/post/:categoria/:slug" element={<Post />} />

// Leer parametros
import { useParams } from 'react-router-dom';
const { id } = useParams();
const { categoria, slug } = useParams();
```

## Navegacion Programatica

```jsx
import { useNavigate } from 'react-router-dom';

const navigate = useNavigate();
navigate("/ruta");              // ir a ruta
navigate(-1);                   // ir atras
navigate("/ruta", { replace: true });  // sin historial
navigate("/ruta", { state: { datos: "algo" } });  // pasar datos
```

## Rutas Anidadas

```jsx
import { Outlet } from 'react-router-dom';

<Route path="/dashboard" element={<Dashboard />}>
  <Route index element={<Resumen />} />
  <Route path="perfil" element={<Perfil />} />
  <Route path="config" element={<Config />} />
</Route>

function Dashboard() {
  return (
    <div>
      <h1>Dashboard</h1>
      <Outlet /> {/* Renderiza la ruta hija activa */}
    </div>
  );
}
```

## Ruta Protegida

```jsx
import { Navigate } from 'react-router-dom';

function RutaProtegida({ children }) {
  const autenticado = useAuth();
  if (!autenticado) return <Navigate to="/login" replace />;
  return children;
}

<Route path="/admin" element={
  <RutaProtegida>
    <Admin />
  </RutaProtegida>
} />
```

## useLocation y useSearchParams

```jsx
import { useLocation, useSearchParams } from 'react-router-dom';

// Leer location actual
const location = useLocation();
// location.pathname = "/usuario/42"
// location.state   = datos pasados con navigate

// Query params: /buscar?q=react&page=2
const [searchParams, setSearchParams] = useSearchParams();
const query = searchParams.get("q");     // "react"
const page = searchParams.get("page");   // "2"
setSearchParams({ q: "vue", page: "1" });
```

## Hooks de React Router v6

```
Hook              | Retorna                       | Uso
------------------|-------------------------------|---------------------------
useParams()       | { param: valor }              | Leer parametros de ruta
useNavigate()     | funcion navigate              | Navegar programaticamente
useLocation()     | { pathname, search, state }   | Info de la URL actual
useSearchParams() | [params, setParams]           | Query string (?key=val)
useOutletContext() | valor del contexto            | Datos entre padre-hijo
```

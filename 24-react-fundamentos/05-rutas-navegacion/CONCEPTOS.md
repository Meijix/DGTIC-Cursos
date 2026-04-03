# 05 — Rutas y Navegacion

## SPA y Enrutamiento

En una **Single Page Application** (SPA), el navegador carga una sola pagina HTML.
La navegacion entre "paginas" se maneja con JavaScript, sin recargar el documento.

```
  Aplicacion Tradicional (MPA):     SPA con React Router:

  /inicio   --> servidor --> HTML    /inicio   --> React cambia componente
  /acerca   --> servidor --> HTML    /acerca   --> React cambia componente
  /contacto --> servidor --> HTML    /contacto --> React cambia componente

  (recarga completa cada vez)        (una sola carga, cambio instantaneo)
```

---

## React Router v6 — Instalacion

```bash
npm install react-router-dom
```

---

## Estructura Basica

```
  Arbol de Rutas
  ===============

  <BrowserRouter>               <-- Habilita enrutamiento
    <App>
      <Navbar />                <-- Siempre visible (con <Link>)
      <Routes>                  <-- Contenedor de rutas
        <Route path="/" element={<Home />} />
        <Route path="/acerca" element={<Acerca />} />
        <Route path="/contacto" element={<Contacto />} />
        <Route path="*" element={<NoEncontrado />} />
      </Routes>
    </App>
  </BrowserRouter>
```

---

## Componentes Principales

### BrowserRouter
Envuelve toda la aplicacion. Usa la History API del navegador.

### Routes y Route
`<Routes>` contiene las rutas. `<Route>` define la relacion path -> componente.

### Link y NavLink
Navegacion sin recargar la pagina. `NavLink` agrega clase activa automaticamente.

```jsx
import { Link, NavLink } from 'react-router-dom';

// Link basico
<Link to="/acerca">Acerca</Link>

// NavLink — agrega clase/estilo cuando la ruta esta activa
<NavLink
  to="/acerca"
  className={({ isActive }) => isActive ? "activo" : ""}
>
  Acerca
</NavLink>
```

---

## Parametros Dinamicos

Rutas con segmentos variables usando `:parametro`.

```
  Ruta con parametro
  ====================

  Definicion:   /usuario/:id
  URL real:     /usuario/42     --> useParams() = { id: "42" }
  URL real:     /usuario/abc    --> useParams() = { id: "abc" }
```

```jsx
// Definir ruta con parametro
<Route path="/usuario/:id" element={<PerfilUsuario />} />

// Leer parametro en el componente
import { useParams } from 'react-router-dom';

function PerfilUsuario() {
  const { id } = useParams(); // "42"
  return <h1>Usuario #{id}</h1>;
}
```

---

## Navegacion Programatica

Navegar desde codigo (no desde un click en `<Link>`).

```jsx
import { useNavigate } from 'react-router-dom';

function FormularioLogin() {
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    await iniciarSesion(datos);
    navigate("/dashboard");       // navegar a otra ruta
    navigate(-1);                 // ir atras (como boton atras)
    navigate("/login", { replace: true }); // sin agregar al historial
  };
}
```

---

## Rutas Anidadas (Nested Routes)

Rutas dentro de rutas, con `<Outlet>` para renderizar las hijas.

```
  Rutas Anidadas
  ===============

  /dashboard              --> <Dashboard> con <Outlet>
  /dashboard/perfil       --> <Outlet> muestra <Perfil>
  /dashboard/ajustes      --> <Outlet> muestra <Ajustes>

  <Route path="/dashboard" element={<Dashboard />}>
    <Route index element={<Resumen />} />      // /dashboard
    <Route path="perfil" element={<Perfil />} />
    <Route path="ajustes" element={<Ajustes />} />
  </Route>
```

```jsx
import { Outlet } from 'react-router-dom';

function Dashboard() {
  return (
    <div>
      <h1>Dashboard</h1>
      <nav>
        <Link to="/dashboard/perfil">Perfil</Link>
        <Link to="/dashboard/ajustes">Ajustes</Link>
      </nav>
      <Outlet />  {/* Aqui se renderizan las rutas hijas */}
    </div>
  );
}
```

---

## Rutas Protegidas

Patron para restringir acceso a rutas que requieren autenticacion.

```
  Flujo de Ruta Protegida
  =========================

  Usuario no autenticado:
  /dashboard --> <RutaProtegida> --> redirige a /login

  Usuario autenticado:
  /dashboard --> <RutaProtegida> --> muestra <Dashboard>
```

```jsx
import { Navigate } from 'react-router-dom';

function RutaProtegida({ children }) {
  const { usuario } = useContext(AuthContexto);

  if (!usuario) {
    return <Navigate to="/login" replace />;
  }

  return children;
}

// Uso en las rutas:
<Route
  path="/dashboard"
  element={
    <RutaProtegida>
      <Dashboard />
    </RutaProtegida>
  }
/>
```

---

## Ruta 404

Capturar rutas no definidas con el path `*` (wildcard).

```jsx
<Routes>
  <Route path="/" element={<Home />} />
  <Route path="/acerca" element={<Acerca />} />
  <Route path="*" element={<NoEncontrado />} />
</Routes>

function NoEncontrado() {
  return (
    <div>
      <h1>404 — Pagina no encontrada</h1>
      <Link to="/">Volver al inicio</Link>
    </div>
  );
}
```

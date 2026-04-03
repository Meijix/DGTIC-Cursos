// =============================================================
// 05 — Rutas y Navegacion: Ejemplo de SPA Multi-pagina
// =============================================================
// Requiere: npm install react-router-dom
// Copiar en App.jsx de un proyecto Vite + React
// =============================================================

import { useState, createContext, useContext } from 'react';
import {
  BrowserRouter,
  Routes,
  Route,
  Link,
  NavLink,
  Navigate,
  Outlet,
  useParams,
  useNavigate,
  useLocation,
} from 'react-router-dom';

// =============================================================
// Contexto de autenticacion (simulado)
// =============================================================

const AuthContexto = createContext();

function AuthProvider({ children }) {
  const [usuario, setUsuario] = useState(null);

  const login = (nombre) => setUsuario({ nombre, id: Date.now() });
  const logout = () => setUsuario(null);

  return (
    <AuthContexto.Provider value={{ usuario, login, logout }}>
      {children}
    </AuthContexto.Provider>
  );
}

function useAuth() {
  return useContext(AuthContexto);
}

// =============================================================
// Componente de Ruta Protegida
// =============================================================

function RutaProtegida({ children }) {
  const { usuario } = useAuth();
  const location = useLocation();

  if (!usuario) {
    // Guardar la ruta intentada para redirigir despues del login
    return <Navigate to="/login" state={{ from: location }} replace />;
  }

  return children;
}

// =============================================================
// Barra de navegacion con NavLink
// =============================================================

function Navbar() {
  const { usuario, logout } = useAuth();

  const estiloActivo = ({ isActive }) => ({
    color: isActive ? "#61dafb" : "#a0a0b8",
    fontWeight: isActive ? "bold" : "normal",
    textDecoration: "none",
    padding: "8px 12px",
  });

  return (
    <nav style={{
      display: "flex",
      alignItems: "center",
      gap: "4px",
      padding: "8px 16px",
      backgroundColor: "#16213e",
      borderBottom: "2px solid #61dafb",
      flexWrap: "wrap",
    }}>
      <NavLink to="/" style={estiloActivo}>Inicio</NavLink>
      <NavLink to="/acerca" style={estiloActivo}>Acerca</NavLink>
      <NavLink to="/usuarios" style={estiloActivo}>Usuarios</NavLink>
      <NavLink to="/dashboard" style={estiloActivo}>Dashboard</NavLink>

      <div style={{ marginLeft: "auto", display: "flex", alignItems: "center", gap: "8px" }}>
        {usuario ? (
          <>
            <span style={{ color: "#61dafb" }}>Hola, {usuario.nombre}</span>
            <button onClick={logout} style={{ padding: "4px 8px" }}>Salir</button>
          </>
        ) : (
          <NavLink to="/login" style={estiloActivo}>Login</NavLink>
        )}
      </div>
    </nav>
  );
}

// =============================================================
// Paginas
// =============================================================

function Inicio() {
  return (
    <div>
      <h1>Pagina de Inicio</h1>
      <p>Bienvenido a la SPA de ejemplo con React Router v6.</p>
      <p>Navega usando los enlaces de arriba.</p>
      <ul>
        <li><Link to="/usuarios">Ver lista de usuarios</Link></li>
        <li><Link to="/usuarios/1">Ver usuario #1</Link></li>
        <li><Link to="/dashboard">Ir al Dashboard (requiere login)</Link></li>
      </ul>
    </div>
  );
}

function Acerca() {
  return (
    <div>
      <h1>Acerca de</h1>
      <p>Esta aplicacion demuestra:</p>
      <ul>
        <li>Rutas basicas con Routes y Route</li>
        <li>Navegacion con Link y NavLink</li>
        <li>Parametros dinamicos con useParams</li>
        <li>Rutas anidadas con Outlet</li>
        <li>Rutas protegidas con Navigate</li>
        <li>Navegacion programatica con useNavigate</li>
      </ul>
    </div>
  );
}

// =============================================================
// Usuarios — Parametros dinamicos
// =============================================================

const datosUsuarios = [
  { id: 1, nombre: "Ana Lopez", rol: "Admin", email: "ana@ejemplo.com" },
  { id: 2, nombre: "Pedro Garcia", rol: "Editor", email: "pedro@ejemplo.com" },
  { id: 3, nombre: "Maria Torres", rol: "Viewer", email: "maria@ejemplo.com" },
  { id: 4, nombre: "Carlos Ruiz", rol: "Editor", email: "carlos@ejemplo.com" },
];

function ListaUsuarios() {
  return (
    <div>
      <h1>Usuarios</h1>
      <ul>
        {datosUsuarios.map((u) => (
          <li key={u.id} style={{ marginBottom: "8px" }}>
            <Link to={`/usuarios/${u.id}`}>{u.nombre}</Link> — {u.rol}
          </li>
        ))}
      </ul>
    </div>
  );
}

function DetalleUsuario() {
  const { id } = useParams(); // Leer parametro :id de la URL
  const navigate = useNavigate();

  const usuario = datosUsuarios.find((u) => u.id === Number(id));

  if (!usuario) {
    return (
      <div>
        <h2>Usuario no encontrado</h2>
        <button onClick={() => navigate("/usuarios")}>Volver a la lista</button>
      </div>
    );
  }

  return (
    <div>
      <button onClick={() => navigate(-1)}>Volver atras</button>
      <h1>{usuario.nombre}</h1>
      <p><strong>Rol:</strong> {usuario.rol}</p>
      <p><strong>Email:</strong> {usuario.email}</p>
      <p><strong>ID:</strong> {usuario.id}</p>
    </div>
  );
}

// =============================================================
// Login — Navegacion programatica
// =============================================================

function Login() {
  const [nombre, setNombre] = useState("");
  const { login } = useAuth();
  const navigate = useNavigate();
  const location = useLocation();

  // Ruta de donde venia el usuario (si fue redirigido)
  const from = location.state?.from?.pathname || "/dashboard";

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!nombre.trim()) return;
    login(nombre.trim());
    navigate(from, { replace: true }); // Redirigir al destino original
  };

  return (
    <div>
      <h1>Iniciar Sesion</h1>
      <form onSubmit={handleSubmit} style={{ display: "flex", gap: "8px" }}>
        <input
          value={nombre}
          onChange={(e) => setNombre(e.target.value)}
          placeholder="Tu nombre..."
        />
        <button type="submit">Entrar</button>
      </form>
      <p style={{ color: "#666", marginTop: "8px" }}>
        (Escribe cualquier nombre para simular login)
      </p>
    </div>
  );
}

// =============================================================
// Dashboard — Rutas anidadas con Outlet
// =============================================================

function Dashboard() {
  return (
    <div>
      <h1>Dashboard</h1>
      <nav style={{ display: "flex", gap: "8px", marginBottom: "16px" }}>
        <Link to="/dashboard" style={{ color: "#61dafb" }}>Resumen</Link>
        <Link to="/dashboard/perfil" style={{ color: "#61dafb" }}>Mi Perfil</Link>
        <Link to="/dashboard/ajustes" style={{ color: "#61dafb" }}>Ajustes</Link>
      </nav>
      <div style={{ padding: "16px", border: "1px solid #ddd", borderRadius: "8px" }}>
        <Outlet /> {/* Aqui se renderizan las rutas hijas */}
      </div>
    </div>
  );
}

function DashboardResumen() {
  const { usuario } = useAuth();
  return <p>Bienvenido al dashboard, {usuario?.nombre}. Selecciona una seccion.</p>;
}

function DashboardPerfil() {
  const { usuario } = useAuth();
  return (
    <div>
      <h2>Mi Perfil</h2>
      <p>Nombre: {usuario?.nombre}</p>
      <p>ID: {usuario?.id}</p>
    </div>
  );
}

function DashboardAjustes() {
  return (
    <div>
      <h2>Ajustes</h2>
      <p>Aqui irian las configuraciones de la cuenta.</p>
    </div>
  );
}

// =============================================================
// 404 — Pagina no encontrada
// =============================================================

function NoEncontrado() {
  return (
    <div style={{ textAlign: "center", padding: "40px" }}>
      <h1 style={{ fontSize: "48px", color: "#e63946" }}>404</h1>
      <p>Pagina no encontrada</p>
      <Link to="/" style={{ color: "#61dafb" }}>Volver al inicio</Link>
    </div>
  );
}

// =============================================================
// App principal — Definicion de todas las rutas
// =============================================================

export default function App() {
  return (
    <BrowserRouter>
      <AuthProvider>
        <div style={{ minHeight: "100vh", backgroundColor: "#1a1a2e", color: "#e8e8e8" }}>
          <Navbar />
          <main style={{ maxWidth: "700px", margin: "0 auto", padding: "20px" }}>
            <Routes>
              {/* Rutas publicas */}
              <Route path="/" element={<Inicio />} />
              <Route path="/acerca" element={<Acerca />} />
              <Route path="/login" element={<Login />} />
              <Route path="/usuarios" element={<ListaUsuarios />} />
              <Route path="/usuarios/:id" element={<DetalleUsuario />} />

              {/* Rutas protegidas con layout anidado */}
              <Route
                path="/dashboard"
                element={
                  <RutaProtegida>
                    <Dashboard />
                  </RutaProtegida>
                }
              >
                <Route index element={<DashboardResumen />} />
                <Route path="perfil" element={<DashboardPerfil />} />
                <Route path="ajustes" element={<DashboardAjustes />} />
              </Route>

              {/* 404 — captura todas las rutas no definidas */}
              <Route path="*" element={<NoEncontrado />} />
            </Routes>
          </main>
        </div>
      </AuthProvider>
    </BrowserRouter>
  );
}

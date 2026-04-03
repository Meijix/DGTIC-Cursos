// =============================================================
// 07 — Proyecto Integrador: Gestor de Tareas SPA
// =============================================================
// Aplicacion completa que integra todos los conceptos:
// - JSX y Componentes (seccion 01)
// - Props y Estado (seccion 02)
// - useEffect y ciclo de vida (seccion 03)
// - Hooks avanzados: useContext, useReducer, custom hooks (seccion 04)
// - React Router: rutas, protegidas, navegacion (seccion 05)
// - Formularios controlados con validacion (seccion 06)
//
// Instalacion:
//   npm create vite@latest gestor-tareas -- --template react
//   cd gestor-tareas
//   npm install react-router-dom
//   # Copiar este archivo como src/App.jsx
//   npm run dev
// =============================================================

import {
  useState,
  useEffect,
  useContext,
  useReducer,
  createContext,
  useCallback,
} from 'react';
import {
  BrowserRouter,
  Routes,
  Route,
  Link,
  NavLink,
  Navigate,
  useNavigate,
} from 'react-router-dom';

// =============================================================
// Custom Hook: useLocalStorage (seccion 04)
// =============================================================
function useLocalStorage(key, valorInicial) {
  const [valor, setValor] = useState(() => {
    try {
      const guardado = localStorage.getItem(key);
      return guardado !== null ? JSON.parse(guardado) : valorInicial;
    } catch {
      return valorInicial;
    }
  });

  useEffect(() => {
    localStorage.setItem(key, JSON.stringify(valor));
  }, [key, valor]);

  return [valor, setValor];
}

// =============================================================
// Contexto de Autenticacion (seccion 04 + 05)
// =============================================================
const AuthContexto = createContext();

function AuthProvider({ children }) {
  const [usuario, setUsuario] = useLocalStorage("gestor-auth", null);

  const login = useCallback((nombre) => {
    setUsuario({ nombre, id: Date.now() });
  }, [setUsuario]);

  const logout = useCallback(() => {
    setUsuario(null);
  }, [setUsuario]);

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
// Reducer de Tareas (seccion 04)
// =============================================================
function tareasReducer(state, action) {
  switch (action.type) {
    case "AGREGAR":
      return [
        ...state,
        {
          id: Date.now(),
          texto: action.payload,
          completada: false,
          fecha: new Date().toLocaleDateString("es-MX"),
        },
      ];
    case "TOGGLE":
      return state.map((t) =>
        t.id === action.payload ? { ...t, completada: !t.completada } : t
      );
    case "ELIMINAR":
      return state.filter((t) => t.id !== action.payload);
    case "EDITAR":
      return state.map((t) =>
        t.id === action.payload.id
          ? { ...t, texto: action.payload.texto }
          : t
      );
    case "LIMPIAR_HECHAS":
      return state.filter((t) => !t.completada);
    case "CARGAR":
      return action.payload;
    default:
      return state;
  }
}

// =============================================================
// Contexto de Tareas (seccion 04)
// =============================================================
const TareasContexto = createContext();

function TareasProvider({ children }) {
  const [tareasGuardadas, setTareasGuardadas] = useLocalStorage("gestor-tareas", []);
  const [tareas, dispatch] = useReducer(tareasReducer, tareasGuardadas);

  // Sincronizar reducer con localStorage (seccion 03)
  useEffect(() => {
    setTareasGuardadas(tareas);
  }, [tareas, setTareasGuardadas]);

  return (
    <TareasContexto.Provider value={{ tareas, dispatch }}>
      {children}
    </TareasContexto.Provider>
  );
}

function useTareas() {
  return useContext(TareasContexto);
}

// =============================================================
// Ruta Protegida (seccion 05)
// =============================================================
function RutaProtegida({ children }) {
  const { usuario } = useAuth();
  if (!usuario) {
    return <Navigate to="/login" replace />;
  }
  return children;
}

// =============================================================
// Estilos compartidos
// =============================================================
const estilos = {
  pagina: { maxWidth: "700px", margin: "0 auto", padding: "20px" },
  botonPrimario: {
    padding: "8px 20px", backgroundColor: "#61dafb", color: "#1a1a2e",
    border: "none", borderRadius: "6px", fontWeight: "bold", cursor: "pointer",
  },
  botonSecundario: {
    padding: "6px 12px", backgroundColor: "#333", color: "#e8e8e8",
    border: "1px solid #555", borderRadius: "4px", cursor: "pointer",
  },
  botonPeligro: {
    padding: "6px 12px", backgroundColor: "#e63946", color: "#fff",
    border: "none", borderRadius: "4px", cursor: "pointer",
  },
  tarjeta: {
    backgroundColor: "#16213e", borderRadius: "8px", padding: "16px",
    marginBottom: "8px", border: "1px solid rgba(255,255,255,0.08)",
  },
};

// =============================================================
// Navbar (seccion 01 + 05)
// =============================================================
function Navbar() {
  const { usuario, logout } = useAuth();

  const estiloLink = ({ isActive }) => ({
    color: isActive ? "#61dafb" : "#a0a0b8",
    fontWeight: isActive ? "bold" : "normal",
    textDecoration: "none",
    padding: "8px 12px",
  });

  return (
    <nav style={{
      display: "flex", alignItems: "center", flexWrap: "wrap",
      gap: "4px", padding: "8px 16px",
      backgroundColor: "#0f3460", borderBottom: "3px solid #61dafb",
    }}>
      <NavLink to="/" style={estiloLink}>Inicio</NavLink>
      {usuario && (
        <NavLink to="/tareas" style={estiloLink}>Mis Tareas</NavLink>
      )}

      <div style={{ marginLeft: "auto", display: "flex", alignItems: "center", gap: "8px" }}>
        {usuario ? (
          <>
            <span style={{ color: "#61dafb", fontSize: "14px" }}>
              {usuario.nombre}
            </span>
            <button onClick={logout} style={estilos.botonSecundario}>
              Salir
            </button>
          </>
        ) : (
          <NavLink to="/login" style={estiloLink}>Entrar</NavLink>
        )}
      </div>
    </nav>
  );
}

// =============================================================
// Pagina: Inicio (seccion 01)
// =============================================================
function Inicio() {
  const { usuario } = useAuth();

  return (
    <div style={estilos.pagina}>
      <h1 style={{ color: "#61dafb" }}>Gestor de Tareas</h1>
      <p style={{ color: "#a0a0b8", marginBottom: "16px" }}>
        Aplicacion SPA completa con React Router, Context API y persistencia local.
      </p>
      {usuario ? (
        <Link to="/tareas" style={{ ...estilos.botonPrimario, textDecoration: "none" }}>
          Ver mis tareas
        </Link>
      ) : (
        <Link to="/login" style={{ ...estilos.botonPrimario, textDecoration: "none" }}>
          Iniciar sesion
        </Link>
      )}
    </div>
  );
}

// =============================================================
// Pagina: Login (seccion 05 + 06)
// =============================================================
function Login() {
  const [nombre, setNombre] = useState("");
  const [error, setError] = useState("");
  const { login, usuario } = useAuth();
  const navigate = useNavigate();

  // Si ya esta autenticado, redirigir
  if (usuario) {
    return <Navigate to="/tareas" replace />;
  }

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!nombre.trim()) {
      setError("Ingresa tu nombre para continuar");
      return;
    }
    login(nombre.trim());
    navigate("/tareas");
  };

  return (
    <div style={estilos.pagina}>
      <h1>Iniciar Sesion</h1>
      <p style={{ color: "#a0a0b8" }}>Ingresa tu nombre para acceder al gestor.</p>
      <form onSubmit={handleSubmit} style={{ marginTop: "16px" }}>
        <input
          type="text"
          value={nombre}
          onChange={(e) => { setNombre(e.target.value); setError(""); }}
          placeholder="Tu nombre..."
          style={{
            padding: "10px", borderRadius: "6px", width: "100%",
            border: error ? "2px solid #e63946" : "1px solid #555",
            backgroundColor: "#16213e", color: "#e8e8e8",
            marginBottom: "4px",
          }}
        />
        {error && <p style={{ color: "#e63946", fontSize: "13px" }}>{error}</p>}
        <button type="submit" style={{ ...estilos.botonPrimario, marginTop: "8px" }}>
          Entrar
        </button>
      </form>
    </div>
  );
}

// =============================================================
// Pagina: Lista de Tareas (seccion 02 + 04)
// =============================================================
function ListaTareas() {
  const { tareas, dispatch } = useTareas();
  const { usuario } = useAuth();
  const [filtro, setFiltro] = useState("todas");

  const tareasFiltradas = tareas.filter((t) => {
    if (filtro === "pendientes") return !t.completada;
    if (filtro === "completadas") return t.completada;
    return true;
  });

  const total = tareas.length;
  const completadas = tareas.filter((t) => t.completada).length;
  const pendientes = total - completadas;
  const porcentaje = total > 0 ? Math.round((completadas / total) * 100) : 0;

  return (
    <div style={estilos.pagina}>
      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", flexWrap: "wrap", gap: "8px" }}>
        <h1>Mis Tareas</h1>
        <Link to="/tareas/nueva" style={{ ...estilos.botonPrimario, textDecoration: "none" }}>
          + Nueva Tarea
        </Link>
      </div>

      {/* Estadisticas */}
      <div style={{ ...estilos.tarjeta, marginTop: "16px" }}>
        <div style={{ display: "flex", justifyContent: "space-around", textAlign: "center" }}>
          <div>
            <div style={{ fontSize: "24px", fontWeight: "bold", color: "#61dafb" }}>{total}</div>
            <div style={{ fontSize: "12px", color: "#a0a0b8" }}>Total</div>
          </div>
          <div>
            <div style={{ fontSize: "24px", fontWeight: "bold", color: "#4caf50" }}>{completadas}</div>
            <div style={{ fontSize: "12px", color: "#a0a0b8" }}>Hechas</div>
          </div>
          <div>
            <div style={{ fontSize: "24px", fontWeight: "bold", color: "#ff9800" }}>{pendientes}</div>
            <div style={{ fontSize: "12px", color: "#a0a0b8" }}>Pendientes</div>
          </div>
          <div>
            <div style={{ fontSize: "24px", fontWeight: "bold", color: "#61dafb" }}>{porcentaje}%</div>
            <div style={{ fontSize: "12px", color: "#a0a0b8" }}>Progreso</div>
          </div>
        </div>
        {/* Barra de progreso */}
        <div style={{ marginTop: "8px", backgroundColor: "#333", borderRadius: "4px", height: "6px" }}>
          <div style={{
            width: `${porcentaje}%`, height: "100%",
            backgroundColor: "#4caf50", borderRadius: "4px",
            transition: "width 0.3s",
          }} />
        </div>
      </div>

      {/* Filtros */}
      <div style={{ display: "flex", gap: "4px", margin: "16px 0 8px" }}>
        {["todas", "pendientes", "completadas"].map((f) => (
          <button
            key={f}
            onClick={() => setFiltro(f)}
            style={{
              padding: "4px 12px", borderRadius: "4px", border: "none",
              cursor: "pointer", textTransform: "capitalize",
              backgroundColor: filtro === f ? "#61dafb" : "#333",
              color: filtro === f ? "#1a1a2e" : "#a0a0b8",
              fontWeight: filtro === f ? "bold" : "normal",
            }}
          >
            {f}
          </button>
        ))}
        {completadas > 0 && (
          <button
            onClick={() => dispatch({ type: "LIMPIAR_HECHAS" })}
            style={{ ...estilos.botonPeligro, marginLeft: "auto", fontSize: "12px" }}
          >
            Limpiar completadas
          </button>
        )}
      </div>

      {/* Lista de tareas */}
      {tareasFiltradas.length === 0 ? (
        <div style={{ ...estilos.tarjeta, textAlign: "center", color: "#a0a0b8" }}>
          {total === 0
            ? "No hay tareas. Crea una nueva!"
            : "No hay tareas con este filtro."}
        </div>
      ) : (
        tareasFiltradas.map((tarea) => (
          <TareaItem key={tarea.id} tarea={tarea} dispatch={dispatch} />
        ))
      )}
    </div>
  );
}

// Componente individual de tarea (seccion 01 + 02)
function TareaItem({ tarea, dispatch }) {
  const [editando, setEditando] = useState(false);
  const [textoEdit, setTextoEdit] = useState(tarea.texto);

  const guardarEdicion = () => {
    if (textoEdit.trim()) {
      dispatch({ type: "EDITAR", payload: { id: tarea.id, texto: textoEdit.trim() } });
    }
    setEditando(false);
  };

  return (
    <div style={{
      ...estilos.tarjeta,
      display: "flex", alignItems: "center", gap: "12px",
      opacity: tarea.completada ? 0.6 : 1,
    }}>
      <input
        type="checkbox"
        checked={tarea.completada}
        onChange={() => dispatch({ type: "TOGGLE", payload: tarea.id })}
        style={{ width: "18px", height: "18px", cursor: "pointer" }}
      />

      <div style={{ flex: 1 }}>
        {editando ? (
          <input
            value={textoEdit}
            onChange={(e) => setTextoEdit(e.target.value)}
            onKeyDown={(e) => e.key === "Enter" && guardarEdicion()}
            onBlur={guardarEdicion}
            autoFocus
            style={{
              width: "100%", padding: "4px 8px",
              backgroundColor: "#0f3460", color: "#e8e8e8",
              border: "1px solid #61dafb", borderRadius: "4px",
            }}
          />
        ) : (
          <span
            style={{ textDecoration: tarea.completada ? "line-through" : "none", cursor: "pointer" }}
            onDoubleClick={() => { setEditando(true); setTextoEdit(tarea.texto); }}
          >
            {tarea.texto}
          </span>
        )}
        <div style={{ fontSize: "11px", color: "#6b6b80", marginTop: "2px" }}>
          {tarea.fecha}
        </div>
      </div>

      <button
        onClick={() => dispatch({ type: "ELIMINAR", payload: tarea.id })}
        style={{ ...estilos.botonPeligro, padding: "4px 8px", fontSize: "12px" }}
        title="Eliminar tarea"
      >
        X
      </button>
    </div>
  );
}

// =============================================================
// Pagina: Formulario de Nueva Tarea (seccion 06)
// =============================================================
function FormularioTarea() {
  const [texto, setTexto] = useState("");
  const [error, setError] = useState("");
  const { dispatch } = useTareas();
  const navigate = useNavigate();

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!texto.trim()) {
      setError("La tarea no puede estar vacia");
      return;
    }
    if (texto.trim().length < 3) {
      setError("Minimo 3 caracteres");
      return;
    }
    dispatch({ type: "AGREGAR", payload: texto.trim() });
    setTexto("");
    setError("");
    navigate("/tareas");
  };

  return (
    <div style={estilos.pagina}>
      <h1>Nueva Tarea</h1>
      <form onSubmit={handleSubmit} style={{ marginTop: "16px" }}>
        <input
          type="text"
          value={texto}
          onChange={(e) => { setTexto(e.target.value); setError(""); }}
          placeholder="Que necesitas hacer?"
          autoFocus
          style={{
            width: "100%", padding: "12px", borderRadius: "6px",
            border: error ? "2px solid #e63946" : "1px solid #555",
            backgroundColor: "#16213e", color: "#e8e8e8",
            fontSize: "16px",
          }}
        />
        {error && <p style={{ color: "#e63946", fontSize: "13px", marginTop: "4px" }}>{error}</p>}

        <div style={{ display: "flex", gap: "8px", marginTop: "12px" }}>
          <button type="submit" style={estilos.botonPrimario}>
            Crear Tarea
          </button>
          <button
            type="button"
            onClick={() => navigate("/tareas")}
            style={estilos.botonSecundario}
          >
            Cancelar
          </button>
        </div>
      </form>
    </div>
  );
}

// =============================================================
// Pagina: 404
// =============================================================
function NoEncontrado() {
  return (
    <div style={{ ...estilos.pagina, textAlign: "center", paddingTop: "60px" }}>
      <h1 style={{ fontSize: "64px", color: "#e63946" }}>404</h1>
      <p style={{ color: "#a0a0b8" }}>Pagina no encontrada</p>
      <Link to="/" style={{ color: "#61dafb" }}>Volver al inicio</Link>
    </div>
  );
}

// =============================================================
// App Principal — Composicion de todo (seccion 01 + 05)
// =============================================================
export default function App() {
  return (
    <BrowserRouter>
      <AuthProvider>
        <TareasProvider>
          <div style={{ minHeight: "100vh", backgroundColor: "#1a1a2e", color: "#e8e8e8" }}>
            <Navbar />
            <Routes>
              <Route path="/" element={<Inicio />} />
              <Route path="/login" element={<Login />} />
              <Route path="/tareas" element={
                <RutaProtegida><ListaTareas /></RutaProtegida>
              } />
              <Route path="/tareas/nueva" element={
                <RutaProtegida><FormularioTarea /></RutaProtegida>
              } />
              <Route path="*" element={<NoEncontrado />} />
            </Routes>
          </div>
        </TareasProvider>
      </AuthProvider>
    </BrowserRouter>
  );
}

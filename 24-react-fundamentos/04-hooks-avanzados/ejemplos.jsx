// =============================================================
// 04 — Hooks Avanzados: Ejemplos Practicos
// =============================================================

import {
  useState,
  useEffect,
  useContext,
  useReducer,
  useMemo,
  useCallback,
  useRef,
  createContext,
} from 'react';

// =============================================================
// 1. useContext — Tema oscuro/claro global
// =============================================================

// Crear contexto para el tema
const TemaContexto = createContext();

function TemaProvider({ children }) {
  const [tema, setTema] = useState("claro");
  const toggleTema = () => setTema((prev) => (prev === "claro" ? "oscuro" : "claro"));

  const estilos = {
    claro: { background: "#ffffff", color: "#1a1a2e", border: "1px solid #ddd" },
    oscuro: { background: "#1a1a2e", color: "#e8e8e8", border: "1px solid #444" },
  };

  return (
    <TemaContexto.Provider value={{ tema, toggleTema, estilos: estilos[tema] }}>
      {children}
    </TemaContexto.Provider>
  );
}

// Componente que consume el contexto (sin importar profundidad)
function BotonTema() {
  const { tema, toggleTema } = useContext(TemaContexto);
  return (
    <button onClick={toggleTema}>
      Tema actual: {tema} (click para cambiar)
    </button>
  );
}

function TarjetaTema({ titulo, contenido }) {
  const { estilos } = useContext(TemaContexto);
  return (
    <div style={{ ...estilos, padding: "16px", borderRadius: "8px", marginTop: "8px" }}>
      <h4>{titulo}</h4>
      <p>{contenido}</p>
    </div>
  );
}

function EjemploContext() {
  return (
    <TemaProvider>
      <BotonTema />
      <TarjetaTema
        titulo="Tarjeta con Tema"
        contenido="Este componente lee el tema del contexto directamente."
      />
    </TemaProvider>
  );
}

// =============================================================
// 2. useReducer — Gestor de tareas con acciones
// =============================================================

const estadoInicial = {
  tareas: [
    { id: 1, texto: "Aprender useReducer", completada: false },
    { id: 2, texto: "Crear un custom hook", completada: false },
  ],
  filtro: "todas", // "todas" | "pendientes" | "completadas"
};

function tareasReducer(state, action) {
  switch (action.type) {
    case "AGREGAR":
      return {
        ...state,
        tareas: [
          ...state.tareas,
          { id: Date.now(), texto: action.payload, completada: false },
        ],
      };
    case "TOGGLE":
      return {
        ...state,
        tareas: state.tareas.map((t) =>
          t.id === action.payload ? { ...t, completada: !t.completada } : t
        ),
      };
    case "ELIMINAR":
      return {
        ...state,
        tareas: state.tareas.filter((t) => t.id !== action.payload),
      };
    case "FILTRAR":
      return { ...state, filtro: action.payload };
    case "LIMPIAR_COMPLETADAS":
      return { ...state, tareas: state.tareas.filter((t) => !t.completada) };
    default:
      return state;
  }
}

function EjemploReducer() {
  const [state, dispatch] = useReducer(tareasReducer, estadoInicial);
  const [nuevoTexto, setNuevoTexto] = useState("");

  const tareasFiltradas = state.tareas.filter((t) => {
    if (state.filtro === "pendientes") return !t.completada;
    if (state.filtro === "completadas") return t.completada;
    return true;
  });

  const agregar = () => {
    if (!nuevoTexto.trim()) return;
    dispatch({ type: "AGREGAR", payload: nuevoTexto.trim() });
    setNuevoTexto("");
  };

  return (
    <div>
      <div style={{ display: "flex", gap: "8px", marginBottom: "12px" }}>
        <input
          value={nuevoTexto}
          onChange={(e) => setNuevoTexto(e.target.value)}
          onKeyDown={(e) => e.key === "Enter" && agregar()}
          placeholder="Nueva tarea..."
        />
        <button onClick={agregar}>Agregar</button>
      </div>

      <div style={{ display: "flex", gap: "4px", marginBottom: "8px" }}>
        {["todas", "pendientes", "completadas"].map((f) => (
          <button
            key={f}
            onClick={() => dispatch({ type: "FILTRAR", payload: f })}
            style={{ fontWeight: state.filtro === f ? "bold" : "normal" }}
          >
            {f}
          </button>
        ))}
        <button
          onClick={() => dispatch({ type: "LIMPIAR_COMPLETADAS" })}
          style={{ marginLeft: "auto", color: "red" }}
        >
          Limpiar completadas
        </button>
      </div>

      <ul style={{ listStyle: "none", padding: 0 }}>
        {tareasFiltradas.map((t) => (
          <li key={t.id} style={{ display: "flex", gap: "8px", padding: "4px 0" }}>
            <input
              type="checkbox"
              checked={t.completada}
              onChange={() => dispatch({ type: "TOGGLE", payload: t.id })}
            />
            <span style={{ flex: 1, textDecoration: t.completada ? "line-through" : "none" }}>
              {t.texto}
            </span>
            <button onClick={() => dispatch({ type: "ELIMINAR", payload: t.id })}>X</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

// =============================================================
// 3. useMemo y useCallback — Optimizacion de rendimiento
// =============================================================

function EjemploMemo() {
  const [numeros] = useState(() =>
    Array.from({ length: 10000 }, (_, i) => Math.floor(Math.random() * 100))
  );
  const [filtroMin, setFiltroMin] = useState(50);
  const [contador, setContador] = useState(0);

  // useMemo: solo recalcula cuando numeros o filtroMin cambian
  // (no cuando contador cambia y causa un re-render)
  const filtrados = useMemo(() => {
    console.log("Recalculando filtro...");
    return numeros.filter((n) => n >= filtroMin);
  }, [numeros, filtroMin]);

  const promedio = useMemo(() => {
    if (filtrados.length === 0) return 0;
    return (filtrados.reduce((sum, n) => sum + n, 0) / filtrados.length).toFixed(1);
  }, [filtrados]);

  // useCallback: la referencia de la funcion no cambia entre renders
  const incrementar = useCallback(() => {
    setContador((prev) => prev + 1);
  }, []);

  return (
    <div>
      <p>
        Filtro minimo:{" "}
        <input
          type="range"
          min={0}
          max={100}
          value={filtroMin}
          onChange={(e) => setFiltroMin(Number(e.target.value))}
        />{" "}
        {filtroMin}
      </p>
      <p>
        {filtrados.length} numeros de {numeros.length} | Promedio: {promedio}
      </p>
      <p>
        Contador (no afecta el calculo): {contador}{" "}
        <button onClick={incrementar}>+1</button>
      </p>
    </div>
  );
}

// =============================================================
// 4. useRef — Acceso al DOM y valores mutables
// =============================================================

function EjemploRef() {
  const inputRef = useRef(null);
  const renderCount = useRef(0);
  const [texto, setTexto] = useState("");

  // Contar renders sin causar re-render adicional
  renderCount.current += 1;

  const enfocar = () => {
    inputRef.current.focus();
    inputRef.current.select();
  };

  return (
    <div>
      <div style={{ display: "flex", gap: "8px" }}>
        <input
          ref={inputRef}
          value={texto}
          onChange={(e) => setTexto(e.target.value)}
          placeholder="Escribe algo..."
        />
        <button onClick={enfocar}>Enfocar y seleccionar</button>
      </div>
      <p style={{ color: "#666" }}>
        Renders del componente: {renderCount.current} (useRef no causa re-render)
      </p>
    </div>
  );
}

// =============================================================
// 5. Custom Hook — useLocalStorage
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

function EjemploCustomHook() {
  const [nombre, setNombre] = useLocalStorage("demo-nombre", "");
  const [color, setColor] = useLocalStorage("demo-color", "#61dafb");

  return (
    <div>
      <p>Estos valores se guardan en localStorage y persisten entre recargas:</p>
      <label>
        Nombre:{" "}
        <input value={nombre} onChange={(e) => setNombre(e.target.value)} />
      </label>
      <br />
      <label>
        Color:{" "}
        <input type="color" value={color} onChange={(e) => setColor(e.target.value)} />
      </label>
      <p style={{ color }}>
        Hola, {nombre || "anonimo"}! (guardado en localStorage)
      </p>
    </div>
  );
}

// =============================================================
// App principal
// =============================================================

export default function App() {
  return (
    <div style={{ maxWidth: "700px", margin: "0 auto", padding: "20px" }}>
      <h1>React: Hooks Avanzados</h1>

      <section style={{ marginBottom: "24px" }}>
        <h2>1. useContext — Tema Global</h2>
        <EjemploContext />
      </section>

      <section style={{ marginBottom: "24px" }}>
        <h2>2. useReducer — Gestor de Tareas</h2>
        <EjemploReducer />
      </section>

      <section style={{ marginBottom: "24px" }}>
        <h2>3. useMemo / useCallback — Rendimiento</h2>
        <EjemploMemo />
      </section>

      <section style={{ marginBottom: "24px" }}>
        <h2>4. useRef — DOM y Valores Mutables</h2>
        <EjemploRef />
      </section>

      <section style={{ marginBottom: "24px" }}>
        <h2>5. Custom Hook — useLocalStorage</h2>
        <EjemploCustomHook />
      </section>
    </div>
  );
}

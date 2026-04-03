// =============================================================
// 03 — Efectos y Ciclo de Vida: Ejemplos Practicos
// =============================================================

import { useState, useEffect } from 'react';

// -------------------------------------------------------------
// 1. useEffect basico — ejecutar al montar
// -------------------------------------------------------------
function MensajeBienvenida() {
  const [mostrar, setMostrar] = useState(false);

  useEffect(() => {
    // Se ejecuta una vez al montar el componente
    console.log("Componente MensajeBienvenida montado");
    setMostrar(true);

    // Cleanup al desmontar
    return () => {
      console.log("Componente MensajeBienvenida desmontado");
    };
  }, []); // [] = solo al montar

  return mostrar ? <p>Bienvenido a la aplicacion!</p> : null;
}

// -------------------------------------------------------------
// 2. Fetch de datos — cargar usuarios de una API
// -------------------------------------------------------------
function ListaUsuarios() {
  const [usuarios, setUsuarios] = useState([]);
  const [cargando, setCargando] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    // AbortController para cancelar si el componente se desmonta
    const controller = new AbortController();

    const cargarUsuarios = async () => {
      try {
        const respuesta = await fetch(
          "https://jsonplaceholder.typicode.com/users",
          { signal: controller.signal }
        );

        if (!respuesta.ok) {
          throw new Error(`HTTP ${respuesta.status}`);
        }

        const datos = await respuesta.json();
        setUsuarios(datos);
      } catch (err) {
        // Ignorar errores de cancelacion
        if (err.name !== "AbortError") {
          setError(err.message);
        }
      } finally {
        setCargando(false);
      }
    };

    cargarUsuarios();

    // Cleanup: cancelar fetch si el componente se desmonta
    return () => controller.abort();
  }, []);

  if (cargando) return <p>Cargando usuarios...</p>;
  if (error) return <p style={{ color: "red" }}>Error: {error}</p>;

  return (
    <ul>
      {usuarios.slice(0, 5).map((usuario) => (
        <li key={usuario.id}>
          <strong>{usuario.name}</strong> — {usuario.email}
        </li>
      ))}
    </ul>
  );
}

// -------------------------------------------------------------
// 3. Temporizador — setInterval con cleanup
// -------------------------------------------------------------
function Cronometro() {
  const [segundos, setSegundos] = useState(0);
  const [activo, setActivo] = useState(false);

  useEffect(() => {
    // Solo crear intervalo si esta activo
    if (!activo) return;

    const intervaloId = setInterval(() => {
      setSegundos((prev) => prev + 1);
    }, 1000);

    // Cleanup: limpiar intervalo al pausar o desmontar
    return () => clearInterval(intervaloId);
  }, [activo]); // Se re-ejecuta cuando activo cambia

  const formatear = (s) => {
    const min = Math.floor(s / 60).toString().padStart(2, "0");
    const seg = (s % 60).toString().padStart(2, "0");
    return `${min}:${seg}`;
  };

  return (
    <div>
      <p style={{ fontSize: "32px", fontFamily: "monospace", fontWeight: "bold" }}>
        {formatear(segundos)}
      </p>
      <div style={{ display: "flex", gap: "8px" }}>
        <button onClick={() => setActivo(true)} disabled={activo}>
          Iniciar
        </button>
        <button onClick={() => setActivo(false)} disabled={!activo}>
          Pausar
        </button>
        <button onClick={() => { setActivo(false); setSegundos(0); }}>
          Reiniciar
        </button>
      </div>
    </div>
  );
}

// -------------------------------------------------------------
// 4. Event listener — detectar tamano de ventana
// -------------------------------------------------------------
function TamanoVentana() {
  const [dimensiones, setDimensiones] = useState({
    ancho: window.innerWidth,
    alto: window.innerHeight,
  });

  useEffect(() => {
    const manejarResize = () => {
      setDimensiones({
        ancho: window.innerWidth,
        alto: window.innerHeight,
      });
    };

    // Suscribirse al evento
    window.addEventListener("resize", manejarResize);

    // Cleanup: desuscribirse
    return () => window.removeEventListener("resize", manejarResize);
  }, []);

  return (
    <p>
      Ventana: <strong>{dimensiones.ancho}</strong> x{" "}
      <strong>{dimensiones.alto}</strong> px
      {dimensiones.ancho < 768 ? " (movil)" : " (escritorio)"}
    </p>
  );
}

// -------------------------------------------------------------
// 5. Efecto con dependencias — busqueda en tiempo real
// -------------------------------------------------------------
function BuscadorPosts() {
  const [busqueda, setBusqueda] = useState("");
  const [resultados, setResultados] = useState([]);
  const [buscando, setBuscando] = useState(false);

  useEffect(() => {
    // No buscar si el texto es muy corto
    if (busqueda.length < 3) {
      setResultados([]);
      return;
    }

    setBuscando(true);
    const controller = new AbortController();

    // Debounce: esperar 500ms antes de buscar
    const timerId = setTimeout(async () => {
      try {
        const res = await fetch(
          `https://jsonplaceholder.typicode.com/posts?_limit=5&title_like=${busqueda}`,
          { signal: controller.signal }
        );
        const data = await res.json();
        setResultados(data);
      } catch (err) {
        if (err.name !== "AbortError") {
          console.error("Error buscando:", err);
        }
      } finally {
        setBuscando(false);
      }
    }, 500);

    // Cleanup: cancelar timer y fetch pendientes
    return () => {
      clearTimeout(timerId);
      controller.abort();
    };
  }, [busqueda]); // Se ejecuta cuando busqueda cambia

  return (
    <div>
      <input
        type="text"
        value={busqueda}
        onChange={(e) => setBusqueda(e.target.value)}
        placeholder="Buscar posts (min 3 caracteres)..."
        style={{ width: "100%", padding: "8px" }}
      />
      {buscando && <p>Buscando...</p>}
      {resultados.length > 0 && (
        <ul>
          {resultados.map((post) => (
            <li key={post.id}>{post.title}</li>
          ))}
        </ul>
      )}
      {busqueda.length >= 3 && !buscando && resultados.length === 0 && (
        <p style={{ color: "#999" }}>Sin resultados para "{busqueda}"</p>
      )}
    </div>
  );
}

// -------------------------------------------------------------
// 6. localStorage — persistir estado entre recargas
// -------------------------------------------------------------
function NotaPersistente() {
  const [nota, setNota] = useState(() => {
    // Inicializacion perezosa: leer de localStorage
    return localStorage.getItem("mi-nota") || "";
  });

  // Guardar en localStorage cada vez que nota cambia
  useEffect(() => {
    localStorage.setItem("mi-nota", nota);
  }, [nota]);

  return (
    <div>
      <textarea
        value={nota}
        onChange={(e) => setNota(e.target.value)}
        placeholder="Escribe una nota (se guarda automaticamente)..."
        rows={4}
        style={{ width: "100%", padding: "8px" }}
      />
      <p style={{ color: "#666" }}>
        {nota.length} caracteres — guardado en localStorage
      </p>
    </div>
  );
}

// -------------------------------------------------------------
// App principal
// -------------------------------------------------------------
export default function App() {
  const [seccion, setSeccion] = useState("todos");

  const secciones = [
    { id: "todos", label: "Todos" },
    { id: "fetch", label: "Fetch API" },
    { id: "timer", label: "Cronometro" },
    { id: "resize", label: "Ventana" },
    { id: "buscar", label: "Busqueda" },
    { id: "storage", label: "localStorage" },
  ];

  return (
    <div style={{ maxWidth: "700px", margin: "0 auto", padding: "20px" }}>
      <h1>React: Efectos y Ciclo de Vida</h1>

      <nav style={{ display: "flex", gap: "8px", flexWrap: "wrap", marginBottom: "20px" }}>
        {secciones.map((s) => (
          <button
            key={s.id}
            onClick={() => setSeccion(s.id)}
            style={{
              padding: "6px 12px",
              backgroundColor: seccion === s.id ? "#61dafb" : "#eee",
              color: seccion === s.id ? "#1a1a2e" : "#333",
              border: "none",
              borderRadius: "4px",
              cursor: "pointer",
              fontWeight: seccion === s.id ? "bold" : "normal",
            }}
          >
            {s.label}
          </button>
        ))}
      </nav>

      <MensajeBienvenida />

      {(seccion === "todos" || seccion === "fetch") && (
        <section style={{ marginBottom: "20px" }}>
          <h2>Fetch de Datos (API)</h2>
          <ListaUsuarios />
        </section>
      )}

      {(seccion === "todos" || seccion === "timer") && (
        <section style={{ marginBottom: "20px" }}>
          <h2>Cronometro (setInterval)</h2>
          <Cronometro />
        </section>
      )}

      {(seccion === "todos" || seccion === "resize") && (
        <section style={{ marginBottom: "20px" }}>
          <h2>Tamano de Ventana (addEventListener)</h2>
          <TamanoVentana />
        </section>
      )}

      {(seccion === "todos" || seccion === "buscar") && (
        <section style={{ marginBottom: "20px" }}>
          <h2>Busqueda en Tiempo Real</h2>
          <BuscadorPosts />
        </section>
      )}

      {(seccion === "todos" || seccion === "storage") && (
        <section style={{ marginBottom: "20px" }}>
          <h2>Nota Persistente (localStorage)</h2>
          <NotaPersistente />
        </section>
      )}
    </div>
  );
}

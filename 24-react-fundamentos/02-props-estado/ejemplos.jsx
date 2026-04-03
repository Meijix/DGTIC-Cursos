// =============================================================
// 02 — Props y Estado: Ejemplos Practicos
// =============================================================

import { useState } from 'react';

// -------------------------------------------------------------
// 1. Props basicas — pasar datos de padre a hijo
// -------------------------------------------------------------
function Saludo({ nombre, emoji = "👋" }) {
  return <p>{emoji} Hola, {nombre}!</p>;
}

function TarjetaPerfil({ nombre, rol, avatar }) {
  return (
    <div style={{
      display: "flex", alignItems: "center", gap: "12px",
      padding: "12px", border: "1px solid #ddd", borderRadius: "8px",
    }}>
      <img
        src={avatar}
        alt={nombre}
        style={{ width: 50, height: 50, borderRadius: "50%" }}
      />
      <div>
        <strong>{nombre}</strong>
        <p style={{ color: "#666", margin: 0 }}>{rol}</p>
      </div>
    </div>
  );
}

// -------------------------------------------------------------
// 2. Children prop — componente contenedor
// -------------------------------------------------------------
function Panel({ titulo, children, color = "#61dafb" }) {
  return (
    <section style={{
      border: `2px solid ${color}`,
      borderRadius: "8px",
      marginBottom: "16px",
    }}>
      <h3 style={{
        backgroundColor: color,
        color: "#1a1a2e",
        padding: "8px 16px",
        margin: 0,
      }}>
        {titulo}
      </h3>
      <div style={{ padding: "16px" }}>
        {children}
      </div>
    </section>
  );
}

// -------------------------------------------------------------
// 3. Contador — useState basico
// -------------------------------------------------------------
function Contador() {
  const [cuenta, setCuenta] = useState(0);

  return (
    <div style={{ display: "flex", alignItems: "center", gap: "12px" }}>
      <button onClick={() => setCuenta(prev => prev - 1)}>-</button>
      <span style={{ fontSize: "24px", fontWeight: "bold", minWidth: "40px", textAlign: "center" }}>
        {cuenta}
      </span>
      <button onClick={() => setCuenta(prev => prev + 1)}>+</button>
      <button onClick={() => setCuenta(0)} style={{ marginLeft: "12px" }}>
        Reiniciar
      </button>
    </div>
  );
}

// -------------------------------------------------------------
// 4. Toggle — estado booleano
// -------------------------------------------------------------
function ToggleTexto() {
  const [visible, setVisible] = useState(true);

  return (
    <div>
      <button onClick={() => setVisible(prev => !prev)}>
        {visible ? "Ocultar" : "Mostrar"} mensaje
      </button>
      {visible && (
        <p style={{ marginTop: "8px", padding: "8px", backgroundColor: "#e3f2fd" }}>
          Este texto se puede ocultar y mostrar con el boton.
        </p>
      )}
    </div>
  );
}

// -------------------------------------------------------------
// 5. Input controlado — estado sincronizado con input
// -------------------------------------------------------------
function InputNombre() {
  const [nombre, setNombre] = useState("");

  return (
    <div>
      <label>
        Tu nombre:{" "}
        <input
          type="text"
          value={nombre}
          onChange={(e) => setNombre(e.target.value)}
          placeholder="Escribe tu nombre..."
        />
      </label>
      <p>
        {nombre
          ? `Hola, ${nombre}! (${nombre.length} caracteres)`
          : "Escribe algo para ver el resultado."}
      </p>
    </div>
  );
}

// -------------------------------------------------------------
// 6. Estado con objetos — formulario de perfil
// -------------------------------------------------------------
function FormularioPerfil() {
  const [perfil, setPerfil] = useState({
    nombre: "",
    email: "",
    bio: "",
  });

  // Manejador generico para todos los campos
  const handleChange = (e) => {
    const { name, value } = e.target;
    setPerfil(prev => ({ ...prev, [name]: value }));
  };

  return (
    <div>
      <div style={{ display: "flex", flexDirection: "column", gap: "8px" }}>
        <input
          name="nombre"
          placeholder="Nombre"
          value={perfil.nombre}
          onChange={handleChange}
        />
        <input
          name="email"
          placeholder="Email"
          type="email"
          value={perfil.email}
          onChange={handleChange}
        />
        <textarea
          name="bio"
          placeholder="Biografia"
          value={perfil.bio}
          onChange={handleChange}
          rows={3}
        />
      </div>
      <pre style={{ marginTop: "12px", backgroundColor: "#f5f5f5", padding: "8px" }}>
        {JSON.stringify(perfil, null, 2)}
      </pre>
    </div>
  );
}

// -------------------------------------------------------------
// 7. Elevacion de estado — dos hermanos comparten datos
// -------------------------------------------------------------
function ConvertidorTemperatura() {
  // Estado elevado: celsius es la fuente de verdad
  const [celsius, setCelsius] = useState(0);

  const fahrenheit = (celsius * 9) / 5 + 32;

  return (
    <div>
      <div style={{ display: "flex", gap: "16px", flexWrap: "wrap" }}>
        <label>
          Celsius:{" "}
          <input
            type="number"
            value={celsius}
            onChange={(e) => setCelsius(Number(e.target.value))}
            style={{ width: "80px" }}
          />
        </label>
        <p>
          = <strong>{fahrenheit.toFixed(1)}</strong> Fahrenheit
        </p>
      </div>
      <p style={{ color: "#666", marginTop: "8px" }}>
        {celsius > 100 ? "Agua hirviendo!" :
         celsius > 30 ? "Hace calor" :
         celsius > 15 ? "Temperatura agradable" :
         celsius > 0 ? "Hace frio" : "Bajo cero!"}
      </p>
    </div>
  );
}

// -------------------------------------------------------------
// 8. Lista con estado — agregar y eliminar items
// -------------------------------------------------------------
function ListaCompras() {
  const [items, setItems] = useState([
    { id: 1, texto: "Leche", comprado: false },
    { id: 2, texto: "Pan", comprado: false },
  ]);
  const [nuevoItem, setNuevoItem] = useState("");

  const agregar = () => {
    if (!nuevoItem.trim()) return;
    setItems(prev => [
      ...prev,
      { id: Date.now(), texto: nuevoItem.trim(), comprado: false },
    ]);
    setNuevoItem("");
  };

  const toggleComprado = (id) => {
    setItems(prev =>
      prev.map(item =>
        item.id === id ? { ...item, comprado: !item.comprado } : item
      )
    );
  };

  const eliminar = (id) => {
    setItems(prev => prev.filter(item => item.id !== id));
  };

  return (
    <div>
      <div style={{ display: "flex", gap: "8px", marginBottom: "12px" }}>
        <input
          value={nuevoItem}
          onChange={(e) => setNuevoItem(e.target.value)}
          onKeyDown={(e) => e.key === "Enter" && agregar()}
          placeholder="Nuevo item..."
        />
        <button onClick={agregar}>Agregar</button>
      </div>
      <ul style={{ listStyle: "none", padding: 0 }}>
        {items.map((item) => (
          <li
            key={item.id}
            style={{
              display: "flex", alignItems: "center", gap: "8px",
              padding: "4px 0",
              textDecoration: item.comprado ? "line-through" : "none",
              color: item.comprado ? "#999" : "inherit",
            }}
          >
            <input
              type="checkbox"
              checked={item.comprado}
              onChange={() => toggleComprado(item.id)}
            />
            <span style={{ flex: 1 }}>{item.texto}</span>
            <button onClick={() => eliminar(item.id)} style={{ color: "red" }}>
              X
            </button>
          </li>
        ))}
      </ul>
      <p style={{ color: "#666" }}>
        {items.filter(i => !i.comprado).length} pendientes de {items.length} totales
      </p>
    </div>
  );
}

// -------------------------------------------------------------
// App principal — composicion de todos los ejemplos
// -------------------------------------------------------------
export default function App() {
  return (
    <div style={{ maxWidth: "700px", margin: "0 auto", padding: "20px" }}>
      <h1>React: Props y Estado</h1>

      <Panel titulo="Props Basicas">
        <Saludo nombre="Maria" />
        <Saludo nombre="Carlos" emoji="🎉" />
        <TarjetaPerfil
          nombre="Ana Lopez"
          rol="Desarrolladora Frontend"
          avatar="https://i.pravatar.cc/50?img=1"
        />
      </Panel>

      <Panel titulo="Contador (useState)" color="#4caf50">
        <Contador />
      </Panel>

      <Panel titulo="Toggle" color="#ff9800">
        <ToggleTexto />
      </Panel>

      <Panel titulo="Input Controlado" color="#9c27b0">
        <InputNombre />
      </Panel>

      <Panel titulo="Estado con Objetos" color="#e91e63">
        <FormularioPerfil />
      </Panel>

      <Panel titulo="Elevacion de Estado" color="#00bcd4">
        <ConvertidorTemperatura />
      </Panel>

      <Panel titulo="Lista con Estado (CRUD)" color="#ff5722">
        <ListaCompras />
      </Panel>
    </div>
  );
}

// =============================================================
// 01 — JSX y Componentes: Ejemplos Practicos
// =============================================================
// Para ejecutar: crear proyecto con Vite y copiar en App.jsx
//   npm create vite@latest demo -- --template react
//   cd demo && npm install && npm run dev
// =============================================================

import { Fragment } from 'react';

// -------------------------------------------------------------
// 1. Componente basico — funcion que retorna JSX
// -------------------------------------------------------------
function Saludo() {
  const mensaje = "Bienvenido a React";
  return <h1>{mensaje}</h1>;
}

// -------------------------------------------------------------
// 2. Expresiones en JSX — todo dentro de {llaves}
// -------------------------------------------------------------
function InfoUsuario() {
  const nombre = "Carlos";
  const edad = 30;
  const hobbies = ["leer", "programar", "cocinar"];

  return (
    <div>
      <h2>Perfil de {nombre}</h2>
      <p>Edad: {edad} anios</p>
      <p>Mayor de edad: {edad >= 18 ? "Si" : "No"}</p>
      <p>Hobbies: {hobbies.join(", ")}</p>
      <p>Fecha actual: {new Date().toLocaleDateString("es-MX")}</p>
    </div>
  );
}

// -------------------------------------------------------------
// 3. Componente con props — recibir datos del padre
// -------------------------------------------------------------
function TarjetaProducto({ nombre, precio, disponible = true }) {
  return (
    <div className="tarjeta-producto">
      <h3>{nombre}</h3>
      <p className="precio">${precio.toFixed(2)} MXN</p>
      <p className={disponible ? "disponible" : "agotado"}>
        {disponible ? "En stock" : "Agotado"}
      </p>
    </div>
  );
}

// -------------------------------------------------------------
// 4. Composicion — componentes dentro de componentes
// -------------------------------------------------------------
function Encabezado({ titulo, subtitulo }) {
  return (
    <header>
      <h1>{titulo}</h1>
      {subtitulo && <p>{subtitulo}</p>}
    </header>
  );
}

function Navegacion() {
  const enlaces = ["Inicio", "Productos", "Contacto"];
  return (
    <nav>
      <ul>
        {enlaces.map((enlace) => (
          <li key={enlace}>
            <a href={`#${enlace.toLowerCase()}`}>{enlace}</a>
          </li>
        ))}
      </ul>
    </nav>
  );
}

function PiePagina({ anio }) {
  return (
    <footer>
      <p>Derechos reservados {anio}</p>
    </footer>
  );
}

// -------------------------------------------------------------
// 5. Fragments — retornar multiples elementos sin wrapper
// -------------------------------------------------------------
function ListaDefiniciones() {
  const terminos = [
    { id: 1, termino: "JSX", definicion: "Extension de sintaxis para JavaScript" },
    { id: 2, termino: "Props", definicion: "Datos pasados de padre a hijo" },
    { id: 3, termino: "Estado", definicion: "Datos internos del componente" },
  ];

  return (
    <dl>
      {terminos.map(({ id, termino, definicion }) => (
        // Fragment con key — necesario dentro de .map()
        <Fragment key={id}>
          <dt><strong>{termino}</strong></dt>
          <dd>{definicion}</dd>
        </Fragment>
      ))}
    </dl>
  );
}

// -------------------------------------------------------------
// 6. Children prop — componente contenedor reutilizable
// -------------------------------------------------------------
function Tarjeta({ children, titulo, color = "#61dafb" }) {
  return (
    <div
      style={{
        border: `2px solid ${color}`,
        borderRadius: "8px",
        padding: "16px",
        marginBottom: "12px",
      }}
    >
      {titulo && <h3 style={{ color }}>{titulo}</h3>}
      <div>{children}</div>
    </div>
  );
}

function AlertaInfo({ children }) {
  return (
    <div style={{
      backgroundColor: "#e3f2fd",
      color: "#1565c0",
      padding: "12px",
      borderLeft: "4px solid #1565c0",
      borderRadius: "4px",
    }}>
      <strong>Info: </strong>
      {children}
    </div>
  );
}

// -------------------------------------------------------------
// 7. Renderizado condicional — multiples patrones
// -------------------------------------------------------------
function EstadoPedido({ estado }) {
  // Early return para casos especiales
  if (!estado) return <p>Sin informacion</p>;

  // Map de estados a colores
  const colores = {
    pendiente: "#ff9800",
    enviado: "#2196f3",
    entregado: "#4caf50",
    cancelado: "#f44336",
  };

  return (
    <span style={{
      color: colores[estado] || "#999",
      fontWeight: "bold",
      textTransform: "uppercase",
    }}>
      {estado}
    </span>
  );
}

// -------------------------------------------------------------
// 8. Listas con key — renderizar arreglos
// -------------------------------------------------------------
function ListaUsuarios() {
  const usuarios = [
    { id: 1, nombre: "Ana Lopez", rol: "Admin" },
    { id: 2, nombre: "Pedro Garcia", rol: "Editor" },
    { id: 3, nombre: "Maria Torres", rol: "Viewer" },
  ];

  return (
    <ul>
      {usuarios.map((usuario) => (
        <li key={usuario.id}>
          <strong>{usuario.nombre}</strong> — {usuario.rol}
        </li>
      ))}
    </ul>
  );
}

// -------------------------------------------------------------
// App principal — composicion de todos los ejemplos
// -------------------------------------------------------------
export default function App() {
  return (
    <div style={{ maxWidth: "700px", margin: "0 auto", padding: "20px" }}>
      <Encabezado
        titulo="React: JSX y Componentes"
        subtitulo="Ejemplos practicos de la seccion 01"
      />
      <Navegacion />

      <Tarjeta titulo="Saludo Basico">
        <Saludo />
      </Tarjeta>

      <Tarjeta titulo="Info Usuario" color="#4caf50">
        <InfoUsuario />
      </Tarjeta>

      <Tarjeta titulo="Productos">
        <TarjetaProducto nombre="Laptop Pro" precio={24999.99} />
        <TarjetaProducto nombre="Mouse Inalambrico" precio={599} />
        <TarjetaProducto nombre="Monitor 4K" precio={8999} disponible={false} />
      </Tarjeta>

      <Tarjeta titulo="Glosario React">
        <ListaDefiniciones />
      </Tarjeta>

      <AlertaInfo>
        Este es un ejemplo del patron <strong>children</strong> en React.
      </AlertaInfo>

      <Tarjeta titulo="Estados de Pedido" color="#ff9800">
        <p>Pedido #001: <EstadoPedido estado="pendiente" /></p>
        <p>Pedido #002: <EstadoPedido estado="enviado" /></p>
        <p>Pedido #003: <EstadoPedido estado="entregado" /></p>
        <p>Pedido #004: <EstadoPedido estado="cancelado" /></p>
        <p>Pedido #005: <EstadoPedido estado={null} /></p>
      </Tarjeta>

      <Tarjeta titulo="Lista de Usuarios" color="#9c27b0">
        <ListaUsuarios />
      </Tarjeta>

      <PiePagina anio={new Date().getFullYear()} />
    </div>
  );
}

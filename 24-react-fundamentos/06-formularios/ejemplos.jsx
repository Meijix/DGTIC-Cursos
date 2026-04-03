// =============================================================
// 06 — Formularios: Ejemplos Practicos
// =============================================================
// Formulario de registro completo con validacion
// =============================================================

import { useState } from 'react';

// -------------------------------------------------------------
// 1. Input controlado basico
// -------------------------------------------------------------
function InputBasico() {
  const [texto, setTexto] = useState("");

  return (
    <div>
      <label>
        Escribe algo:{" "}
        <input
          type="text"
          value={texto}
          onChange={(e) => setTexto(e.target.value)}
          placeholder="Texto controlado..."
        />
      </label>
      <p>Valor actual: <strong>{texto || "(vacio)"}</strong></p>
      <p>Caracteres: {texto.length}</p>
    </div>
  );
}

// -------------------------------------------------------------
// 2. Formulario de registro completo con validacion
// -------------------------------------------------------------

const ESTADO_INICIAL = {
  nombre: "",
  email: "",
  password: "",
  confirmPassword: "",
  pais: "",
  genero: "",
  intereses: [],
  aceptaTerminos: false,
  bio: "",
};

const PAISES = [
  { value: "", label: "Selecciona un pais..." },
  { value: "mx", label: "Mexico" },
  { value: "co", label: "Colombia" },
  { value: "ar", label: "Argentina" },
  { value: "es", label: "Espana" },
  { value: "cl", label: "Chile" },
];

const INTERESES = ["Desarrollo Web", "Mobile", "DevOps", "IA/ML", "Diseno UX"];

function FormularioRegistro() {
  const [form, setForm] = useState(ESTADO_INICIAL);
  const [errores, setErrores] = useState({});
  const [enviado, setEnviado] = useState(false);

  // Manejador generico para text, email, password, textarea, select, radio
  const handleChange = (e) => {
    const { name, value } = e.target;
    setForm((prev) => ({ ...prev, [name]: value }));

    // Limpiar error del campo al editar
    if (errores[name]) {
      setErrores((prev) => {
        const copia = { ...prev };
        delete copia[name];
        return copia;
      });
    }
  };

  // Manejador para checkbox de terminos
  const handleCheckTerminos = (e) => {
    setForm((prev) => ({ ...prev, aceptaTerminos: e.target.checked }));
  };

  // Manejador para checkboxes multiples (intereses)
  const handleIntereses = (interes) => {
    setForm((prev) => ({
      ...prev,
      intereses: prev.intereses.includes(interes)
        ? prev.intereses.filter((i) => i !== interes)
        : [...prev.intereses, interes],
    }));
  };

  // Validacion completa
  const validar = () => {
    const e = {};

    if (!form.nombre.trim()) {
      e.nombre = "El nombre es obligatorio";
    } else if (form.nombre.trim().length < 2) {
      e.nombre = "Minimo 2 caracteres";
    }

    if (!form.email.trim()) {
      e.email = "El email es obligatorio";
    } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(form.email)) {
      e.email = "Email no valido";
    }

    if (!form.password) {
      e.password = "La contrasena es obligatoria";
    } else if (form.password.length < 6) {
      e.password = "Minimo 6 caracteres";
    }

    if (form.password !== form.confirmPassword) {
      e.confirmPassword = "Las contrasenas no coinciden";
    }

    if (!form.pais) {
      e.pais = "Selecciona un pais";
    }

    if (!form.genero) {
      e.genero = "Selecciona un genero";
    }

    if (form.intereses.length === 0) {
      e.intereses = "Selecciona al menos un interes";
    }

    if (!form.aceptaTerminos) {
      e.aceptaTerminos = "Debes aceptar los terminos";
    }

    setErrores(e);
    return Object.keys(e).length === 0;
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (validar()) {
      setEnviado(true);
      console.log("Datos del formulario:", form);
    }
  };

  const handleReset = () => {
    setForm(ESTADO_INICIAL);
    setErrores({});
    setEnviado(false);
  };

  // Mostrar resultado si fue enviado
  if (enviado) {
    return (
      <div style={{ padding: "16px", border: "2px solid #4caf50", borderRadius: "8px" }}>
        <h3 style={{ color: "#4caf50" }}>Registro exitoso!</h3>
        <pre style={{ background: "#f5f5f5", padding: "12px", borderRadius: "4px", color: "#333" }}>
          {JSON.stringify(form, null, 2)}
        </pre>
        <button onClick={handleReset} style={{ marginTop: "8px" }}>
          Nuevo registro
        </button>
      </div>
    );
  }

  // Componente para mostrar errores
  const ErrorMsg = ({ campo }) =>
    errores[campo] ? (
      <span style={{ color: "#e63946", fontSize: "12px", display: "block", marginTop: "2px" }}>
        {errores[campo]}
      </span>
    ) : null;

  const estiloInput = (campo) => ({
    width: "100%",
    padding: "8px",
    borderRadius: "4px",
    border: errores[campo] ? "2px solid #e63946" : "1px solid #ccc",
  });

  return (
    <form onSubmit={handleSubmit} style={{ display: "flex", flexDirection: "column", gap: "12px" }}>

      {/* Nombre */}
      <div>
        <label><strong>Nombre completo *</strong></label>
        <input
          name="nombre"
          type="text"
          value={form.nombre}
          onChange={handleChange}
          placeholder="Tu nombre..."
          style={estiloInput("nombre")}
        />
        <ErrorMsg campo="nombre" />
      </div>

      {/* Email */}
      <div>
        <label><strong>Email *</strong></label>
        <input
          name="email"
          type="email"
          value={form.email}
          onChange={handleChange}
          placeholder="tu@email.com"
          style={estiloInput("email")}
        />
        <ErrorMsg campo="email" />
      </div>

      {/* Password */}
      <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: "8px" }}>
        <div>
          <label><strong>Contrasena *</strong></label>
          <input
            name="password"
            type="password"
            value={form.password}
            onChange={handleChange}
            style={estiloInput("password")}
          />
          <ErrorMsg campo="password" />
        </div>
        <div>
          <label><strong>Confirmar *</strong></label>
          <input
            name="confirmPassword"
            type="password"
            value={form.confirmPassword}
            onChange={handleChange}
            style={estiloInput("confirmPassword")}
          />
          <ErrorMsg campo="confirmPassword" />
        </div>
      </div>

      {/* Select — Pais */}
      <div>
        <label><strong>Pais *</strong></label>
        <select
          name="pais"
          value={form.pais}
          onChange={handleChange}
          style={estiloInput("pais")}
        >
          {PAISES.map((p) => (
            <option key={p.value} value={p.value}>{p.label}</option>
          ))}
        </select>
        <ErrorMsg campo="pais" />
      </div>

      {/* Radio — Genero */}
      <div>
        <label><strong>Genero *</strong></label>
        <div style={{ display: "flex", gap: "16px", marginTop: "4px" }}>
          {["Masculino", "Femenino", "Otro"].map((g) => (
            <label key={g} style={{ display: "flex", alignItems: "center", gap: "4px" }}>
              <input
                type="radio"
                name="genero"
                value={g.toLowerCase()}
                checked={form.genero === g.toLowerCase()}
                onChange={handleChange}
              />
              {g}
            </label>
          ))}
        </div>
        <ErrorMsg campo="genero" />
      </div>

      {/* Checkboxes multiples — Intereses */}
      <div>
        <label><strong>Intereses * (selecciona al menos uno)</strong></label>
        <div style={{ display: "flex", flexWrap: "wrap", gap: "12px", marginTop: "4px" }}>
          {INTERESES.map((interes) => (
            <label key={interes} style={{ display: "flex", alignItems: "center", gap: "4px" }}>
              <input
                type="checkbox"
                checked={form.intereses.includes(interes)}
                onChange={() => handleIntereses(interes)}
              />
              {interes}
            </label>
          ))}
        </div>
        <ErrorMsg campo="intereses" />
      </div>

      {/* Textarea — Bio */}
      <div>
        <label><strong>Biografia (opcional)</strong></label>
        <textarea
          name="bio"
          value={form.bio}
          onChange={handleChange}
          rows={3}
          placeholder="Cuentanos sobre ti..."
          style={{ ...estiloInput("bio"), resize: "vertical" }}
        />
      </div>

      {/* Checkbox — Terminos */}
      <div>
        <label style={{ display: "flex", alignItems: "center", gap: "8px" }}>
          <input
            type="checkbox"
            checked={form.aceptaTerminos}
            onChange={handleCheckTerminos}
          />
          <span>Acepto los terminos y condiciones *</span>
        </label>
        <ErrorMsg campo="aceptaTerminos" />
      </div>

      {/* Botones */}
      <div style={{ display: "flex", gap: "8px" }}>
        <button type="submit" style={{
          padding: "10px 24px", backgroundColor: "#61dafb",
          color: "#1a1a2e", border: "none", borderRadius: "4px",
          fontWeight: "bold", cursor: "pointer",
        }}>
          Registrarse
        </button>
        <button type="button" onClick={handleReset} style={{
          padding: "10px 24px", backgroundColor: "#eee",
          color: "#333", border: "none", borderRadius: "4px",
          cursor: "pointer",
        }}>
          Limpiar
        </button>
      </div>

      {/* Resumen de errores */}
      {Object.keys(errores).length > 0 && (
        <p style={{ color: "#e63946" }}>
          Hay {Object.keys(errores).length} error(es) en el formulario.
        </p>
      )}
    </form>
  );
}

// -------------------------------------------------------------
// App principal
// -------------------------------------------------------------
export default function App() {
  return (
    <div style={{ maxWidth: "600px", margin: "0 auto", padding: "20px" }}>
      <h1>React: Formularios</h1>

      <section style={{ marginBottom: "24px" }}>
        <h2>1. Input Controlado Basico</h2>
        <InputBasico />
      </section>

      <section>
        <h2>2. Formulario de Registro Completo</h2>
        <p style={{ color: "#666", marginBottom: "12px" }}>
          Con validacion, multiples tipos de input y manejo de errores.
        </p>
        <FormularioRegistro />
      </section>
    </div>
  );
}

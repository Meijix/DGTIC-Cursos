# 06 — Formularios

## Componentes Controlados

En React, los inputs del formulario se controlan con estado. El valor del
input siempre refleja el estado de React (single source of truth).

```
  Flujo de Componente Controlado
  ================================

  [Estado React]
       |
       | value={estado}
       v
  +----------+
  |  <input> |  --> usuario escribe
  +----------+
       |
       | onChange --> e.target.value
       v
  setEstado(nuevoValor)
       |
       | re-render
       v
  [Estado React actualizado]
       |
       | value={nuevoEstado}
       v
  +----------+
  |  <input> |  --> muestra nuevo valor
  +----------+
```

---

## Input Basico Controlado

```jsx
function InputControlado() {
  const [nombre, setNombre] = useState("");

  return (
    <input
      type="text"
      value={nombre}                              // controlado por estado
      onChange={(e) => setNombre(e.target.value)}   // actualizar estado
    />
  );
}
```

La diferencia clave: React es quien decide que valor tiene el input,
no el DOM del navegador.

---

## Formulario Multi-campo

Patron para manejar multiples inputs con un solo manejador:

```jsx
function Formulario() {
  const [datos, setDatos] = useState({
    nombre: "",
    email: "",
    mensaje: "",
  });

  // Manejador generico — usa el atributo name del input
  const handleChange = (e) => {
    const { name, value } = e.target;
    setDatos(prev => ({ ...prev, [name]: value }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log("Datos:", datos);
  };

  return (
    <form onSubmit={handleSubmit}>
      <input name="nombre" value={datos.nombre} onChange={handleChange} />
      <input name="email"  value={datos.email}  onChange={handleChange} />
      <textarea name="mensaje" value={datos.mensaje} onChange={handleChange} />
      <button type="submit">Enviar</button>
    </form>
  );
}
```

```
  Flujo del manejador generico
  ==============================

  <input name="email" value={datos.email} onChange={handleChange} />
                |                                     |
                v                                     v
  e.target.name = "email"              setDatos(prev => ({
  e.target.value = "ana@mail.com"        ...prev,
                                         [name]: value  <-- computed property
                                       }))
```

---

## Tipos de Input

### Select

```jsx
const [pais, setPais] = useState("mx");

<select value={pais} onChange={(e) => setPais(e.target.value)}>
  <option value="mx">Mexico</option>
  <option value="co">Colombia</option>
  <option value="ar">Argentina</option>
</select>
```

### Checkbox

```jsx
const [acepta, setAcepta] = useState(false);

<input
  type="checkbox"
  checked={acepta}                     // checked, no value
  onChange={(e) => setAcepta(e.target.checked)}  // .checked, no .value
/>
```

### Radio Buttons

```jsx
const [genero, setGenero] = useState("otro");

<label>
  <input type="radio" name="genero" value="m"
    checked={genero === "m"} onChange={(e) => setGenero(e.target.value)} />
  Masculino
</label>
<label>
  <input type="radio" name="genero" value="f"
    checked={genero === "f"} onChange={(e) => setGenero(e.target.value)} />
  Femenino
</label>
```

---

## Validacion de Formularios

```
  Estrategias de Validacion
  ===========================

  1. Al enviar (onSubmit)     <-- Mas comun
     - Validar todos los campos
     - Mostrar errores
     - Prevenir envio si hay errores

  2. Al cambiar (onChange)    <-- Feedback inmediato
     - Validar campo actual
     - Mostrar error mientras escribe

  3. Al perder foco (onBlur)  <-- Balance
     - Validar cuando sale del campo
     - No interrumpe mientras escribe
```

```jsx
function validar(datos) {
  const errores = {};
  if (!datos.nombre.trim()) errores.nombre = "Nombre requerido";
  if (!datos.email.includes("@")) errores.email = "Email invalido";
  if (datos.password.length < 6) errores.password = "Minimo 6 caracteres";
  return errores;
}
```

---

## Librerias de Formularios

Para formularios complejos, las librerias simplifican la validacion y el manejo:

| Libreria         | Caracteristica principal        |
|------------------|---------------------------------|
| React Hook Form  | Rendimiento (minimal re-renders)|
| Formik           | API declarativa completa        |
| Zod + RHF        | Validacion con TypeScript       |

```jsx
// React Hook Form — ejemplo basico
import { useForm } from 'react-hook-form';

function MiForm() {
  const { register, handleSubmit, formState: { errors } } = useForm();

  const onSubmit = (data) => console.log(data);

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <input {...register("nombre", { required: "Campo requerido" })} />
      {errors.nombre && <span>{errors.nombre.message}</span>}
      <button type="submit">Enviar</button>
    </form>
  );
}
```

---

## Componentes No Controlados

Alternativa donde el DOM maneja el valor. Se usa `useRef` para leer el valor.
Menos comun en React, pero util para integraciones con librerias externas.

```jsx
function FormNoControlado() {
  const inputRef = useRef(null);

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log(inputRef.current.value); // leer directamente del DOM
  };

  return (
    <form onSubmit={handleSubmit}>
      <input ref={inputRef} defaultValue="texto inicial" />
      <button type="submit">Enviar</button>
    </form>
  );
}
```

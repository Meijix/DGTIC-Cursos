# 06 — Formularios — Cheatsheet

## Input Controlado

```jsx
const [valor, setValor] = useState("");
<input value={valor} onChange={(e) => setValor(e.target.value)} />
```

## Manejador Generico Multi-campo

```jsx
const [form, setForm] = useState({ nombre: "", email: "" });

const handleChange = (e) => {
  const { name, value } = e.target;
  setForm(prev => ({ ...prev, [name]: value }));
};

<input name="nombre" value={form.nombre} onChange={handleChange} />
<input name="email"  value={form.email}  onChange={handleChange} />
```

## Tipos de Input

```jsx
// Text / Email / Password
<input type="text" value={val} onChange={e => set(e.target.value)} />

// Textarea
<textarea value={val} onChange={e => set(e.target.value)} rows={4} />

// Select
<select value={val} onChange={e => set(e.target.value)}>
  <option value="">Selecciona...</option>
  <option value="a">Opcion A</option>
</select>

// Checkbox (usa checked, no value)
<input type="checkbox"
  checked={bool}
  onChange={e => set(e.target.checked)}
/>

// Radio (grupo con mismo name)
<input type="radio" name="grupo" value="a"
  checked={val === "a"}
  onChange={e => set(e.target.value)}
/>

// Number
<input type="number" value={num}
  onChange={e => set(Number(e.target.value))}
/>
```

## Submit del Formulario

```jsx
const handleSubmit = (e) => {
  e.preventDefault();  // evitar recarga de pagina
  // validar y procesar datos
  console.log(formData);
};

<form onSubmit={handleSubmit}>
  {/* inputs */}
  <button type="submit">Enviar</button>
</form>
```

## Validacion Basica

```jsx
const [errores, setErrores] = useState({});

const validar = () => {
  const e = {};
  if (!form.nombre.trim()) e.nombre = "Requerido";
  if (!form.email.includes("@")) e.email = "Email invalido";
  if (form.password.length < 6) e.password = "Min 6 caracteres";
  setErrores(e);
  return Object.keys(e).length === 0; // true si no hay errores
};

const handleSubmit = (e) => {
  e.preventDefault();
  if (validar()) {
    // enviar datos
  }
};

// Mostrar error
{errores.nombre && <span className="error">{errores.nombre}</span>}
```

## Reset del Formulario

```jsx
const estadoInicial = { nombre: "", email: "" };
const [form, setForm] = useState(estadoInicial);

const resetear = () => setForm(estadoInicial);
```

## Checkbox Multiple

```jsx
const [seleccionados, setSeleccionados] = useState([]);

const toggleItem = (item) => {
  setSeleccionados(prev =>
    prev.includes(item)
      ? prev.filter(i => i !== item)
      : [...prev, item]
  );
};

{opciones.map(op => (
  <label key={op}>
    <input
      type="checkbox"
      checked={seleccionados.includes(op)}
      onChange={() => toggleItem(op)}
    />
    {op}
  </label>
))}
```

## React Hook Form (basico)

```jsx
import { useForm } from 'react-hook-form';

const { register, handleSubmit, formState: { errors }, reset } = useForm();

<form onSubmit={handleSubmit(onSubmit)}>
  <input {...register("nombre", { required: "Campo obligatorio" })} />
  {errors.nombre && <span>{errors.nombre.message}</span>}

  <input {...register("email", {
    required: "Requerido",
    pattern: { value: /^\S+@\S+$/, message: "Email invalido" }
  })} />

  <button type="submit">Enviar</button>
  <button type="button" onClick={() => reset()}>Limpiar</button>
</form>
```

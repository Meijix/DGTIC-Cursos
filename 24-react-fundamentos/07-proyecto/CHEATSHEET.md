# 07 — Proyecto Integrador — Cheatsheet

## Estructura del Proyecto

```
gestor-tareas/
  src/
    App.jsx          <-- Todo el codigo (single-file para este ejemplo)
  package.json
```

## Dependencias

```bash
npm install react-router-dom
```

## Patrones Usados

### Context + Provider

```jsx
const MiContexto = createContext();

function MiProvider({ children }) {
  const [estado, setEstado] = useState(valorInicial);
  return (
    <MiContexto.Provider value={{ estado, setEstado }}>
      {children}
    </MiContexto.Provider>
  );
}

const useMiContexto = () => useContext(MiContexto);
```

### useReducer para CRUD

```jsx
function reducer(state, action) {
  switch (action.type) {
    case "AGREGAR":
      return [...state, { id: Date.now(), ...action.payload }];
    case "ELIMINAR":
      return state.filter(item => item.id !== action.payload);
    case "TOGGLE":
      return state.map(item =>
        item.id === action.payload
          ? { ...item, completada: !item.completada }
          : item
      );
    default:
      return state;
  }
}
```

### Ruta Protegida

```jsx
function RutaProtegida({ children }) {
  const { usuario } = useAuth();
  if (!usuario) return <Navigate to="/login" replace />;
  return children;
}
```

### Custom Hook para localStorage

```jsx
function useLocalStorage(key, inicial) {
  const [val, setVal] = useState(() =>
    JSON.parse(localStorage.getItem(key)) ?? inicial
  );
  useEffect(() => {
    localStorage.setItem(key, JSON.stringify(val));
  }, [key, val]);
  return [val, setVal];
}
```

### Formulario Controlado con Validacion

```jsx
const [texto, setTexto] = useState("");
const [error, setError] = useState("");

const handleSubmit = (e) => {
  e.preventDefault();
  if (!texto.trim()) {
    setError("Campo requerido");
    return;
  }
  dispatch({ type: "AGREGAR", payload: texto.trim() });
  setTexto("");
  setError("");
  navigate("/tareas");
};
```

### Filtrado de Lista

```jsx
const [filtro, setFiltro] = useState("todas");

const tareasFiltradas = tareas.filter(t => {
  if (filtro === "pendientes") return !t.completada;
  if (filtro === "completadas") return t.completada;
  return true;
});
```

## Estructura de Rutas

```jsx
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
```

## Estadisticas de Tareas

```jsx
const total = tareas.length;
const completadas = tareas.filter(t => t.completada).length;
const pendientes = total - completadas;
const porcentaje = total > 0 ? Math.round((completadas / total) * 100) : 0;
```

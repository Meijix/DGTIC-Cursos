# 04 — Hooks Avanzados

## Panorama de Hooks

```
  Hooks de React
  ===============

  Basicos:                  Avanzados:
  +-------------+           +------------------+
  | useState    |           | useContext       |  <-- compartir datos
  | useEffect   |           | useReducer      |  <-- estado complejo
  +-------------+           | useMemo         |  <-- memoizar valores
                            | useCallback     |  <-- memoizar funciones
                            | useRef          |  <-- refs mutables / DOM
                            +------------------+

  Custom Hooks:
  +-----------------------------------+
  | useLocalStorage, useFetch, etc.   |  <-- logica reutilizable
  +-----------------------------------+
```

---

## useContext — Estado Global sin Prop Drilling

El problema del **prop drilling**: pasar datos a traves de muchos niveles.

```
  SIN Context (prop drilling):       CON Context:

  <App tema="oscuro">                <App>
    <Layout tema="oscuro">             <ThemeProvider>  <-- provee
      <Sidebar tema="oscuro">            <Layout>
        <Boton tema="oscuro" />            <Sidebar>
                                              <Boton />  <-- consume
  (tema pasa por 4 niveles               directamente
   aunque Layout y Sidebar
   no lo usan)
```

### Crear y Usar Contexto

```jsx
// 1. Crear el contexto
const TemaContexto = createContext("claro");

// 2. Proveer en un componente alto
function App() {
  const [tema, setTema] = useState("oscuro");
  return (
    <TemaContexto.Provider value={{ tema, setTema }}>
      <Layout />
    </TemaContexto.Provider>
  );
}

// 3. Consumir en cualquier hijo (sin importar profundidad)
function Boton() {
  const { tema, setTema } = useContext(TemaContexto);
  return <button className={tema}>Toggle Tema</button>;
}
```

---

## useReducer — Estado Complejo

Ideal cuando el estado tiene multiples sub-valores o transiciones complejas.

```
  Flujo de useReducer
  =====================

  Componente                       Reducer
  +----------+   dispatch(accion)  +-------------------+
  | UI       | ------------------> | switch(type)      |
  |          |                     |   case 'AGREGAR': |
  |          | <------------------ |     return nuevo  |
  +----------+   nuevo estado      |   case 'BORRAR':  |
                                   |     return nuevo  |
                                   +-------------------+

  const [state, dispatch] = useReducer(reducer, estadoInicial);
  dispatch({ type: 'AGREGAR', payload: item });
```

El reducer es una funcion pura: `(estadoActual, accion) => nuevoEstado`

---

## useMemo — Memoizar Valores Calculados

Evita recalcular valores costosos en cada render si las dependencias no cambiaron.

```jsx
const resultado = useMemo(() => {
  return calculoCostoso(datos);
}, [datos]); // Solo recalcula si datos cambia
```

```
  Sin useMemo:                   Con useMemo:

  Render 1: calcular(datos)      Render 1: calcular(datos) + cache
  Render 2: calcular(datos)      Render 2: leer de cache (rapido)
  Render 3: calcular(datos)      Render 3: leer de cache (rapido)
  (recalcula cada vez)           Render 4: datos cambio -> recalcular
```

Usar solo cuando el calculo es realmente costoso. No memoizar todo.

---

## useCallback — Memoizar Funciones

Similar a useMemo pero para funciones. Evita crear nuevas instancias en cada render.

```jsx
// Sin useCallback: nueva funcion en cada render
const handleClick = () => hacerAlgo(id);

// Con useCallback: misma referencia si id no cambia
const handleClick = useCallback(() => {
  hacerAlgo(id);
}, [id]);
```

Util cuando se pasa como prop a componentes hijos memoizados con `React.memo`.

---

## useRef — Referencias Mutables

Dos usos principales:
1. **Acceder al DOM** directamente
2. **Almacenar valores mutables** que no causan re-render

```
  useRef vs useState
  ====================

  useRef:                          useState:
  - .current mutable               - Inmutable (via setter)
  - NO causa re-render             - SI causa re-render
  - Persistente entre renders      - Persistente entre renders
  - Para DOM, timers, valores      - Para datos de UI
    que no afectan la UI
```

```jsx
// Acceso al DOM
const inputRef = useRef(null);
<input ref={inputRef} />
inputRef.current.focus(); // enfocar el input

// Valor mutable sin re-render
const contadorRenders = useRef(0);
useEffect(() => {
  contadorRenders.current += 1; // no causa re-render
});
```

---

## Custom Hooks — Logica Reutilizable

Un custom hook es una funcion que empieza con `use` y puede usar otros hooks.

```
  Patron Custom Hook
  ====================

  Componente A ----\
                    +---> useMiHook()  <--- logica compartida
  Componente B ----/         |
                             +---> useState, useEffect, etc.
```

```jsx
// Hook reutilizable para fetch
function useFetch(url) {
  const [datos, setDatos] = useState(null);
  const [cargando, setCargando] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const controller = new AbortController();
    fetch(url, { signal: controller.signal })
      .then(res => res.json())
      .then(data => setDatos(data))
      .catch(err => {
        if (err.name !== 'AbortError') setError(err.message);
      })
      .finally(() => setCargando(false));
    return () => controller.abort();
  }, [url]);

  return { datos, cargando, error };
}

// Uso en cualquier componente
function MiComponente() {
  const { datos, cargando, error } = useFetch("/api/datos");
  // ...
}
```

---

## Reglas de Hooks

1. Solo llamar hooks en el **nivel superior** (no en if, for, funciones anidadas)
2. Solo llamar hooks en **componentes funcionales** o **custom hooks**
3. Los custom hooks deben empezar con `use`

```jsx
// CORRECTO
function MiComponente() {
  const [valor, setValor] = useState(0);
  useEffect(() => { ... }, []);
}

// INCORRECTO
function MiComponente() {
  if (condicion) {
    const [valor, setValor] = useState(0); // ERROR
  }
}
```

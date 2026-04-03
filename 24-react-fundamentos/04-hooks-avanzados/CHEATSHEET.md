# 04 — Hooks Avanzados — Cheatsheet

## useContext

```jsx
import { createContext, useContext, useState } from 'react';

// 1. Crear contexto
const MiContexto = createContext(valorPorDefecto);

// 2. Proveer
function App() {
  const [dato, setDato] = useState("hola");
  return (
    <MiContexto.Provider value={{ dato, setDato }}>
      <Hijos />
    </MiContexto.Provider>
  );
}

// 3. Consumir (en cualquier nivel de profundidad)
function ComponenteHijo() {
  const { dato, setDato } = useContext(MiContexto);
  return <p>{dato}</p>;
}
```

## useReducer

```jsx
import { useReducer } from 'react';

// Reducer: funcion pura (estado, accion) => nuevoEstado
function reducer(state, action) {
  switch (action.type) {
    case 'incrementar':
      return { ...state, contador: state.contador + 1 };
    case 'decrementar':
      return { ...state, contador: state.contador - 1 };
    case 'reset':
      return { ...state, contador: 0 };
    default:
      return state;
  }
}

// Uso
const [state, dispatch] = useReducer(reducer, { contador: 0 });
dispatch({ type: 'incrementar' });
dispatch({ type: 'reset' });
```

## useMemo

```jsx
import { useMemo } from 'react';

// Memoizar valor costoso de calcular
const resultado = useMemo(() => {
  return lista.filter(item => item.activo).sort((a, b) => a.nombre.localeCompare(b.nombre));
}, [lista]); // Solo recalcula si lista cambia

// NO usar para todo — solo para calculos costosos
```

## useCallback

```jsx
import { useCallback } from 'react';

// Memoizar funcion (misma referencia entre renders)
const handleSubmit = useCallback((datos) => {
  enviar(datos, userId);
}, [userId]); // Nueva funcion solo si userId cambia

// Util al pasar callbacks a hijos memoizados con React.memo
```

## useRef

```jsx
import { useRef } from 'react';

// Referencia al DOM
const inputRef = useRef(null);
<input ref={inputRef} />
inputRef.current.focus();

// Valor mutable sin re-render
const renderCount = useRef(0);
renderCount.current += 1; // NO causa re-render

// Guardar valor previo
const prevValor = useRef(valor);
useEffect(() => {
  prevValor.current = valor;
}, [valor]);
```

## Custom Hooks

```jsx
// Hook para localStorage
function useLocalStorage(key, valorInicial) {
  const [valor, setValor] = useState(() =>
    JSON.parse(localStorage.getItem(key)) ?? valorInicial
  );
  useEffect(() => {
    localStorage.setItem(key, JSON.stringify(valor));
  }, [key, valor]);
  return [valor, setValor];
}

// Hook para toggle booleano
function useToggle(inicial = false) {
  const [valor, setValor] = useState(inicial);
  const toggle = useCallback(() => setValor(v => !v), []);
  return [valor, toggle];
}

// Hook para fetch
function useFetch(url) {
  const [state, setState] = useState({ datos: null, cargando: true, error: null });
  useEffect(() => {
    const ctrl = new AbortController();
    fetch(url, { signal: ctrl.signal })
      .then(r => r.json())
      .then(datos => setState({ datos, cargando: false, error: null }))
      .catch(err => {
        if (err.name !== 'AbortError')
          setState({ datos: null, cargando: false, error: err.message });
      });
    return () => ctrl.abort();
  }, [url]);
  return state;
}
```

## Comparativa Rapida

```
Hook          | Para que                    | Causa re-render?
--------------|-----------------------------|------------------
useContext    | Datos globales sin drilling  | Si (al cambiar)
useReducer   | Estado complejo/transiciones | Si
useMemo      | Memoizar calculos costosos   | No (optimizacion)
useCallback  | Memoizar funciones           | No (optimizacion)
useRef       | DOM / valores mutables       | No
```

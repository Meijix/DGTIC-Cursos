# 02 — Props y Estado — Cheatsheet

## Props

```jsx
// Pasar props
<Hijo nombre="Ana" edad={25} activo lista={[1,2,3]} />

// Recibir con destructuring
function Hijo({ nombre, edad, activo = false, lista = [] }) { ... }

// Spread de props
const datos = { nombre: "Ana", edad: 25 };
<Hijo {...datos} />

// Children
<Contenedor>
  <p>Contenido hijo</p>
</Contenedor>
function Contenedor({ children }) {
  return <div>{children}</div>;
}
```

## useState

```jsx
import { useState } from 'react';

// Declarar estado
const [valor, setValor] = useState(valorInicial);

// Actualizar directamente
setValor("nuevo valor");
setValor(42);
setValor(true);

// Actualizar basandose en el anterior (RECOMENDADO)
setContador(prev => prev + 1);
setNombre(prev => prev.toUpperCase());
```

## Estado con Objetos

```jsx
const [usuario, setUsuario] = useState({ nombre: "", edad: 0 });

// Actualizar una propiedad (crear copia nueva)
setUsuario(prev => ({ ...prev, nombre: "Ana" }));

// NUNCA mutar directamente
// usuario.nombre = "Ana";  // MAL
```

## Estado con Arreglos

```jsx
const [items, setItems] = useState([]);

// Agregar
setItems(prev => [...prev, nuevoItem]);

// Eliminar por id
setItems(prev => prev.filter(item => item.id !== id));

// Modificar un elemento
setItems(prev => prev.map(item =>
  item.id === id ? { ...item, hecho: true } : item
));

// Reemplazar todo
setItems(nuevaLista);
```

## Inicializacion Perezosa

```jsx
// Si el valor inicial es costoso de calcular
const [datos, setDatos] = useState(() => {
  return JSON.parse(localStorage.getItem('datos')) ?? [];
});
```

## Elevacion de Estado

```jsx
// Padre posee el estado
function Padre() {
  const [valor, setValor] = useState("");
  return (
    <>
      <HijoInput valor={valor} onCambio={setValor} />
      <HijoDisplay texto={valor} />
    </>
  );
}

// Hijo con input — usa callback del padre
function HijoInput({ valor, onCambio }) {
  return <input value={valor} onChange={e => onCambio(e.target.value)} />;
}

// Hijo display — solo lee
function HijoDisplay({ texto }) {
  return <p>{texto}</p>;
}
```

## Patrones Comunes

```jsx
// Toggle booleano
const [activo, setActivo] = useState(false);
<button onClick={() => setActivo(prev => !prev)}>Toggle</button>

// Input controlado
const [nombre, setNombre] = useState("");
<input value={nombre} onChange={e => setNombre(e.target.value)} />

// Contador
const [n, setN] = useState(0);
<button onClick={() => setN(prev => prev + 1)}>+</button>
<button onClick={() => setN(prev => prev - 1)}>-</button>
```

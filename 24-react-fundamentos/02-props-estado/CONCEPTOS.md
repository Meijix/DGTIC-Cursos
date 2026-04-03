# 02 — Props y Estado

## Props (Propiedades)

Las props son el mecanismo para pasar datos de un componente padre a un hijo.
Son **de solo lectura** — un componente nunca debe modificar sus propias props.

```
  Flujo de Props
  ===============

  <App>                         Estado vive aqui
    |
    | nombre="Ana" edad={25}    Props fluyen hacia abajo
    v
  <Perfil>                      Recibe y usa props
    |
    | texto="Hola Ana"          Puede pasar a sus hijos
    v
  <Saludo>
```

---

## Pasar y Recibir Props

```jsx
// PADRE — pasa datos como atributos
<TarjetaUsuario
  nombre="Ana"
  edad={25}
  activo={true}
  hobbies={["leer", "correr"]}
  onSaludar={() => alert("Hola")}
/>

// HIJO — recibe via destructuring (recomendado)
function TarjetaUsuario({ nombre, edad, activo, hobbies, onSaludar }) {
  return (
    <div>
      <h2>{nombre}</h2>
      <p>Edad: {edad}</p>
    </div>
  );
}
```

---

## Valores por Defecto

```jsx
function Boton({ texto = "Click", color = "blue", tamano = "md" }) {
  return <button className={`btn btn-${tamano}`}>{texto}</button>;
}

// Si no se pasa la prop, usa el valor por defecto
<Boton />                    // texto="Click", color="blue"
<Boton texto="Enviar" />     // texto="Enviar", color="blue"
```

---

## Spread de Props

```jsx
const datosUsuario = { nombre: "Pedro", edad: 30, rol: "Admin" };

// Pasar todas las propiedades de un objeto
<Perfil {...datosUsuario} />

// Equivalente a:
<Perfil nombre="Pedro" edad={30} rol="Admin" />
```

---

## useState — Estado Local

El estado es informacion que un componente **posee y puede modificar**.
Cuando el estado cambia, React re-renderiza el componente.

```
  Ciclo del Estado
  =================

  1. Estado inicial
     const [contador, setContador] = useState(0);
                                              ^
                                        valor inicial

  2. Renderizado
     return <p>{contador}</p>;   // muestra 0

  3. Evento del usuario
     <button onClick={() => setContador(contador + 1)}>

  4. Actualizacion
     setContador(1)  -->  React agenda re-render

  5. Re-renderizado
     return <p>{contador}</p>;   // muestra 1

  [Render] --> [Evento] --> [setState] --> [Re-render]
      ^                                        |
      +----------------------------------------+
```

---

## Reglas de useState

```jsx
import { useState } from 'react';

function Ejemplo() {
  // Siempre en el nivel superior del componente
  const [nombre, setNombre] = useState("");
  const [edad, setEdad] = useState(0);
  const [items, setItems] = useState([]);

  // NUNCA dentro de if, for, o funciones anidadas
  // NUNCA llamar hooks condicionalmente
}
```

---

## Actualizacion Funcional

Cuando el nuevo estado depende del anterior, usar la forma funcional:

```jsx
// INCORRECTO — puede fallar con multiples actualizaciones rapidas
setContador(contador + 1);

// CORRECTO — siempre recibe el estado mas reciente
setContador(prev => prev + 1);

// Con arreglos
setItems(prev => [...prev, nuevoItem]);

// Con objetos
setUsuario(prev => ({ ...prev, nombre: "Nuevo" }));
```

---

## Elevacion de Estado (Lifting State Up)

Cuando dos componentes hermanos necesitan compartir estado, se eleva al padre comun.

```
  ANTES (estado duplicado):        DESPUES (estado elevado):

  <App>                            <App>
   / \                              estado: valor
  A   B                             / \
  |   |                            A   B
  estado  estado                   |   |
  (duplicado)                      usa props

  Problema: A y B no se            Solucion: App tiene el estado
  pueden sincronizar               y lo pasa como props
```

```jsx
function App() {
  // Estado elevado al padre comun
  const [texto, setTexto] = useState("");

  return (
    <>
      <InputTexto valor={texto} onChange={setTexto} />
      <VistaPrevia texto={texto} />
    </>
  );
}

function InputTexto({ valor, onChange }) {
  return <input value={valor} onChange={e => onChange(e.target.value)} />;
}

function VistaPrevia({ texto }) {
  return <p>Vista previa: {texto}</p>;
}
```

---

## Estado Inmutable

React detecta cambios comparando referencias. Siempre crear nuevas copias:

```jsx
// Objetos — spread + sobrescribir
setUsuario(prev => ({ ...prev, nombre: "Nuevo" }));

// Arreglos — crear nuevo arreglo
setItems(prev => [...prev, nuevoItem]);              // agregar
setItems(prev => prev.filter(i => i.id !== id));      // eliminar
setItems(prev => prev.map(i =>                        // modificar
  i.id === id ? { ...i, completado: true } : i
));
```

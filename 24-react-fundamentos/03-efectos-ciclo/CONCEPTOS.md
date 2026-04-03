# 03 — Efectos y Ciclo de Vida

## Que es un Efecto?

Un **efecto secundario** (side effect) es cualquier operacion que interactua
con el mundo fuera del componente: llamadas a APIs, suscripciones, temporizadores,
manipulacion directa del DOM, o sincronizacion con sistemas externos.

```
  Componente React
  =================

  Render puro:              Efectos:
  +-----------------+       +--------------------+
  | - Calcular JSX  |       | - Fetch de API     |
  | - Leer props    |       | - setInterval      |
  | - Leer estado   |       | - addEventListener |
  | - Retornar UI   |       | - localStorage     |
  +-----------------+       +--------------------+
        |                          |
        v                          v
  Se ejecuta en                Se ejecuta DESPUES
  cada render                  del render (useEffect)
```

---

## useEffect — Sintaxis

```jsx
import { useEffect } from 'react';

useEffect(() => {
  // Codigo del efecto (se ejecuta despues del render)

  return () => {
    // Cleanup (opcional — se ejecuta antes del proximo efecto
    // y al desmontar el componente)
  };
}, [dependencia1, dependencia2]); // Arreglo de dependencias
```

---

## Arreglo de Dependencias

El arreglo de dependencias controla CUANDO se ejecuta el efecto:

```
  Variantes de useEffect
  ========================

  useEffect(() => { ... });           Sin arreglo
  --> Se ejecuta en CADA render       (raramente deseado)

  useEffect(() => { ... }, []);       Arreglo vacio
  --> Solo al MONTAR (1 vez)          (equivale a componentDidMount)

  useEffect(() => { ... }, [a, b]);   Con dependencias
  --> Al montar Y cuando a o b        (equivale a componentDidUpdate
      cambien                          para esas dependencias)
```

---

## Ciclo de Vida: Clases vs Hooks

```
  Componente de Clase          Hooks Funcionales
  ========================     ========================

  constructor()                useState(valorInicial)
  componentDidMount()          useEffect(() => {}, [])
  componentDidUpdate()         useEffect(() => {}, [deps])
  componentWillUnmount()       useEffect(() => {
                                 return () => { cleanup };
                               }, []);

  Flujo temporal:
  ===============

  [Montar]
     |
     v
  Render --> useEffect(() => {...}, [])
     |
  [Actualizar estado/props]
     |
     v
  Re-render --> cleanup anterior --> useEffect(() => {...}, [deps])
     |
  [Desmontar]
     |
     v
  cleanup final
```

---

## Fetch de Datos

Patron comun: cargar datos al montar el componente.

```jsx
function ListaUsuarios() {
  const [usuarios, setUsuarios] = useState([]);
  const [cargando, setCargando] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch("https://jsonplaceholder.typicode.com/users")
      .then(res => {
        if (!res.ok) throw new Error("Error en la peticion");
        return res.json();
      })
      .then(data => setUsuarios(data))
      .catch(err => setError(err.message))
      .finally(() => setCargando(false));
  }, []); // [] = solo al montar

  if (cargando) return <p>Cargando...</p>;
  if (error) return <p>Error: {error}</p>;
  return <ul>{usuarios.map(u => <li key={u.id}>{u.name}</li>)}</ul>;
}
```

---

## Cleanup — Limpiar Efectos

Los efectos que crean suscripciones, timers o event listeners deben
limpiarse para evitar memory leaks.

```
  Ciclo de Cleanup
  =================

  Montar:   efecto() se ejecuta
  Update:   cleanup() --> efecto() se ejecuta de nuevo
  Desmontar: cleanup() final

  Ejemplo con timer:

  useEffect(() => {
    const id = setInterval(tick, 1000);  // crear
    return () => clearInterval(id);       // limpiar
  }, []);

  Ejemplo con evento:

  useEffect(() => {
    window.addEventListener('resize', handler);   // suscribir
    return () => window.removeEventListener('resize', handler);  // desuscribir
  }, []);
```

---

## Fetch con async/await

useEffect no puede ser async directamente. Se define una funcion interna:

```jsx
useEffect(() => {
  const cargarDatos = async () => {
    try {
      setCargando(true);
      const res = await fetch(url);
      const data = await res.json();
      setDatos(data);
    } catch (err) {
      setError(err.message);
    } finally {
      setCargando(false);
    }
  };

  cargarDatos();
}, [url]); // Se re-ejecuta si url cambia
```

---

## Errores Comunes

| Error                          | Problema                              | Solucion                     |
|--------------------------------|---------------------------------------|------------------------------|
| Loop infinito                  | Falta arreglo de dependencias         | Agregar `[]` o `[deps]`     |
| Estado desactualizado          | Closure sobre valor viejo             | Usar actualizacion funcional |
| Efecto no se limpia            | No retornar cleanup                   | Return funcion de limpieza   |
| Fetch en componente desmontado | setState despues de desmontar         | Flag `isMounted` o AbortController |
| useEffect async                | No se puede hacer useEffect async     | Funcion async interna        |

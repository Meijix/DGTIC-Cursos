# 03 — Efectos y Ciclo de Vida — Cheatsheet

## useEffect — Variantes

```jsx
import { useState, useEffect } from 'react';

// Ejecutar en cada render (raramente necesario)
useEffect(() => {
  console.log("Render completado");
});

// Solo al montar (equivale a componentDidMount)
useEffect(() => {
  console.log("Componente montado");
}, []);

// Al montar y cuando cambian dependencias
useEffect(() => {
  console.log(`El valor cambio a: ${valor}`);
}, [valor]);

// Con cleanup (equivale a componentWillUnmount)
useEffect(() => {
  const id = setInterval(() => tick(), 1000);
  return () => clearInterval(id); // cleanup
}, []);
```

## Fetch de Datos

```jsx
// Patron basico con .then()
useEffect(() => {
  fetch(url)
    .then(res => res.json())
    .then(data => setDatos(data))
    .catch(err => setError(err.message))
    .finally(() => setCargando(false));
}, []);

// Con async/await (funcion interna)
useEffect(() => {
  const cargar = async () => {
    try {
      const res = await fetch(url);
      const data = await res.json();
      setDatos(data);
    } catch (err) {
      setError(err.message);
    }
  };
  cargar();
}, [url]);

// Con AbortController (cancelar si desmonta)
useEffect(() => {
  const controller = new AbortController();
  fetch(url, { signal: controller.signal })
    .then(res => res.json())
    .then(data => setDatos(data))
    .catch(err => {
      if (err.name !== 'AbortError') setError(err.message);
    });
  return () => controller.abort();
}, [url]);
```

## Suscripciones y Event Listeners

```jsx
// Escuchar resize de ventana
useEffect(() => {
  const handler = () => setAncho(window.innerWidth);
  window.addEventListener('resize', handler);
  return () => window.removeEventListener('resize', handler);
}, []);

// Escuchar teclas
useEffect(() => {
  const handler = (e) => {
    if (e.key === 'Escape') cerrarModal();
  };
  document.addEventListener('keydown', handler);
  return () => document.removeEventListener('keydown', handler);
}, []);
```

## Temporizadores

```jsx
// setInterval con cleanup
useEffect(() => {
  const id = setInterval(() => {
    setSegundos(prev => prev + 1);
  }, 1000);
  return () => clearInterval(id);
}, []);

// setTimeout
useEffect(() => {
  const id = setTimeout(() => setMostrar(true), 3000);
  return () => clearTimeout(id);
}, []);
```

## Sincronizar con localStorage

```jsx
// Leer al montar
useEffect(() => {
  const guardado = localStorage.getItem('datos');
  if (guardado) setDatos(JSON.parse(guardado));
}, []);

// Guardar cuando cambia
useEffect(() => {
  localStorage.setItem('datos', JSON.stringify(datos));
}, [datos]);
```

## Equivalencias Clase vs Hooks

```
componentDidMount()       -->  useEffect(() => {}, [])
componentDidUpdate(prev)  -->  useEffect(() => {}, [dep])
componentWillUnmount()    -->  useEffect(() => { return () => {} }, [])
```

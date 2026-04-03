# 07 — Proyecto Integrador: Gestor de Tareas

## Vision General

Este proyecto integra todos los conceptos del modulo en una aplicacion SPA
completa: un **gestor de tareas** con multiples vistas, autenticacion simulada,
manejo de estado global y persistencia local.

---

## Arquitectura de la Aplicacion

```
  Estructura de Componentes
  ===========================

  <BrowserRouter>
    <AuthProvider>              <-- Context: autenticacion
      <TareasProvider>          <-- Context: estado de tareas (useReducer)
        <App>
          <Navbar />
          <Routes>
            /            --> <Inicio />
            /login       --> <Login />
            /tareas      --> <ListaTareas />      (protegida)
            /tareas/nueva --> <FormularioTarea />  (protegida)
            *            --> <NoEncontrado />
          </Routes>
        </App>
      </TareasProvider>
    </AuthProvider>
  </BrowserRouter>
```

---

## Conceptos Aplicados por Seccion

```
  Seccion del Modulo        Donde se Aplica en el Proyecto
  ========================  ==========================================

  01 JSX y Componentes      Toda la UI: Navbar, Tarjeta, Layout
  02 Props y Estado          Props en componentes, useState en forms
  03 Efectos y Ciclo         useEffect para localStorage, cargar datos
  04 Hooks Avanzados         useContext (auth, tareas), useReducer,
                             custom hooks (useLocalStorage)
  05 Rutas y Navegacion      React Router: rutas, protegidas, params
  06 Formularios             FormularioTarea: validacion, controlados
```

---

## Flujo de Datos

```
  Flujo de Estado Global
  ========================

  AuthContext                    TareasContext
  +-----------+                  +-------------------+
  | usuario   |                  | tareas: []        |
  | login()   |                  | dispatch(accion)  |
  | logout()  |                  +-------------------+
  +-----------+                         |
       |                                |
       v                                v
  <RutaProtegida>               <ListaTareas>
  Verifica si usuario            Lee tareas del context
  existe antes de                Dispatch para CRUD
  renderizar rutas

  Persistencia:
  +-------------------+
  | localStorage      |  <-- useEffect sincroniza tareas
  | "tareas-app"      |      al cambiar el estado
  +-------------------+
```

---

## Reducer de Tareas

```
  Acciones del Reducer
  ======================

  dispatch({ type, payload })

  AGREGAR        --> Crea nueva tarea con id, texto, completada, fecha
  TOGGLE         --> Cambia completada de una tarea por id
  ELIMINAR       --> Remueve tarea por id
  EDITAR         --> Actualiza texto de una tarea por id
  LIMPIAR_HECHAS --> Elimina todas las tareas completadas
```

```jsx
function tareasReducer(state, action) {
  switch (action.type) {
    case "AGREGAR":
      return [...state, {
        id: Date.now(),
        texto: action.payload,
        completada: false,
        fecha: new Date().toLocaleDateString(),
      }];
    case "TOGGLE":
      return state.map(t =>
        t.id === action.payload ? { ...t, completada: !t.completada } : t
      );
    case "ELIMINAR":
      return state.filter(t => t.id !== action.payload);
    case "EDITAR":
      return state.map(t =>
        t.id === action.payload.id ? { ...t, texto: action.payload.texto } : t
      );
    case "LIMPIAR_HECHAS":
      return state.filter(t => !t.completada);
    default:
      return state;
  }
}
```

---

## Custom Hook: useLocalStorage

```jsx
function useLocalStorage(key, valorInicial) {
  const [valor, setValor] = useState(() => {
    const guardado = localStorage.getItem(key);
    return guardado ? JSON.parse(guardado) : valorInicial;
  });

  useEffect(() => {
    localStorage.setItem(key, JSON.stringify(valor));
  }, [key, valor]);

  return [valor, setValor];
}
```

---

## Rutas Protegidas

```
  Flujo de Proteccion
  =====================

  Usuario NO autenticado:
  /tareas --> <RutaProtegida> --> <Navigate to="/login" />

  Usuario SI autenticado:
  /tareas --> <RutaProtegida> --> <ListaTareas />
```

---

## Formulario con Validacion

El formulario de nueva tarea implementa:
- Componente controlado con useState
- Validacion al enviar (onSubmit)
- Prevencion de envio vacio
- Reset despues de envio exitoso
- Navegacion programatica post-envio

---

## Como Ejecutar

```bash
# 1. Crear proyecto
npm create vite@latest gestor-tareas -- --template react

# 2. Instalar dependencias
cd gestor-tareas
npm install react-router-dom

# 3. Copiar el contenido de ejemplos.jsx en src/App.jsx

# 4. Ejecutar
npm run dev
```

---

## Posibles Extensiones

- Agregar prioridad (alta/media/baja) a las tareas
- Filtros por estado y busqueda por texto
- Edicion inline de tareas
- Backend real con API REST
- Animaciones con Framer Motion
- Testing con Vitest + React Testing Library

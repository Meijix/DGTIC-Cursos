# 07 — Proyecto Integrador — Cheatsheet

## Resumen de Conceptos Usados

```
┌─────────────────────┬─────────────────────────────────────────┐
│ Concepto            │ Donde se usa en el proyecto             │
├─────────────────────┼─────────────────────────────────────────┤
│ interface           │ Tarea, FiltroTareas, Estadisticas       │
│ type alias          │ Resultado<T>, CrearTareaDTO             │
│ enum                │ Estado, Prioridad                       │
│ readonly            │ Tarea.id, Tarea.creadaEn                │
│ opcional (?)        │ descripcion, fechaLimite                │
│ Generics <T>        │ Resultado<T>                            │
│ Partial<T>          │ actualizarTarea(id, Partial<Tarea>)     │
│ Pick<T,K>           │ ResumenTarea                            │
│ Omit<T,K>           │ CrearTareaDTO (sin id ni fechas)        │
│ Record<K,V>         │ Estadisticas por estado                 │
│ Readonly<T>         │ Tarea devuelta al exterior              │
│ Type guard          │ esExito() para Resultado                │
│ Clase               │ GestorTareas                            │
│ private             │ _tareas, _generarId                     │
│ Union discriminada  │ Resultado = Exito | Fallo               │
└─────────────────────┴─────────────────────────────────────────┘
```

## Tipos Clave del Proyecto

```typescript
// Enums
enum Estado { Pendiente, EnProgreso, Completada, Cancelada }
enum Prioridad { Baja, Media, Alta, Urgente }

// Interface principal
interface Tarea {
  readonly id: string;
  titulo: string;
  descripcion?: string;
  estado: Estado;
  prioridad: Prioridad;
  etiquetas: string[];
  creadaEn: Date;
  actualizadaEn: Date;
  fechaLimite?: Date;
}

// Tipo resultado generico
type Resultado<T> =
  | { exito: true; datos: T }
  | { exito: false; error: string };
```

## Operaciones del Gestor

```typescript
class GestorTareas {
  crear(datos: CrearTareaDTO): Resultado<Tarea>
  actualizar(id: string, cambios: Partial<Tarea>): Resultado<Tarea>
  eliminar(id: string): Resultado<void>
  buscarPorId(id: string): Resultado<Tarea>
  filtrar(filtro: FiltroTareas): Tarea[]
  estadisticas(): EstadisticasTareas
}
```

## Type Guard del Proyecto

```typescript
function esExito<T>(resultado: Resultado<T>): resultado is { exito: true; datos: T } {
  return resultado.exito === true;
}

// Uso:
const r = gestor.crear({ titulo: "Test", ... });
if (esExito(r)) {
  console.log(r.datos.titulo);  // TypeScript sabe que r.datos existe
}
```

## DTOs con Utility Types

```typescript
// Para crear: sin id ni timestamps
type CrearTareaDTO = Omit<Tarea, "id" | "creadaEn" | "actualizadaEn">;

// Para actualizar: todo opcional excepto id
type ActualizarTareaDTO = Partial<Omit<Tarea, "id" | "creadaEn">>;

// Para resumen: solo campos clave
type ResumenTarea = Pick<Tarea, "id" | "titulo" | "estado" | "prioridad">;
```

## Estadisticas con Record

```typescript
interface EstadisticasTareas {
  total: number;
  porEstado: Record<Estado, number>;
  porPrioridad: Record<Prioridad, number>;
  completadas: number;
  pendientes: number;
}
```

## Flujo de Ejecucion

```
Crear gestor
    │
    ├── crear(dto) ──▶ valida ──▶ Resultado<Tarea>
    │
    ├── actualizar(id, cambios) ──▶ busca + merge ──▶ Resultado<Tarea>
    │
    ├── filtrar(filtro) ──▶ aplica predicados ──▶ Tarea[]
    │
    └── estadisticas() ──▶ reduce sobre tareas ──▶ EstadisticasTareas
```

## Patron Completo: Crear y Verificar

```typescript
const gestor = new GestorTareas();

const resultado = gestor.crear({
  titulo: "Aprender TypeScript",
  prioridad: Prioridad.Alta,
  etiquetas: ["estudio"],
  estado: Estado.Pendiente
});

if (esExito(resultado)) {
  console.log(`Tarea creada: ${resultado.datos.titulo}`);
  console.log(`ID: ${resultado.datos.id}`);
} else {
  console.error(`Error: ${resultado.error}`);
}
```

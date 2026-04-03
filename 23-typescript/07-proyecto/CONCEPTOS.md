# 07 — Proyecto Integrador: Gestor de Tareas Tipado

## Descripcion del Proyecto

Un **gestor de tareas** (todo-list manager) que aplica todos los conceptos
de TypeScript vistos en las secciones anteriores:

- Interfaces y type aliases para modelar datos
- Genericos para estructuras reutilizables
- Utility types para transformar tipos
- Clases con modificadores de acceso
- Type guards para validaciones
- Enums para estados

## Arquitectura

```
  ┌───────────────────────────────────────────────────┐
  │                GESTOR DE TAREAS                   │
  ├───────────────────────────────────────────────────┤
  │                                                   │
  │  Tipos e Interfaces (contratos de datos)          │
  │  ├── Tarea, Prioridad, Estado                     │
  │  ├── FiltroTareas, EstadisticasTareas             │
  │  └── Resultado<T> (generico para operaciones)     │
  │                                                   │
  │  Clase GestorTareas (logica principal)            │
  │  ├── crear, actualizar, eliminar                  │
  │  ├── buscar, filtrar, ordenar                     │
  │  ├── estadisticas, exportar                       │
  │  └── private: validar, generarId                  │
  │                                                   │
  │  Funciones utilitarias                            │
  │  ├── validadores con type guards                  │
  │  ├── formateadores de salida                      │
  │  └── helpers con utility types                    │
  │                                                   │
  └───────────────────────────────────────────────────┘
```

## Conceptos Aplicados por Seccion

```
┌───────────────────────────────────────────────────────────────┐
│ Seccion              │ Concepto aplicado en el proyecto       │
├──────────────────────┼────────────────────────────────────────┤
│ 01 Tipos basicos     │ string, number, boolean, enums, void  │
│ 02 Interfaces/types  │ Tarea, FiltroTareas, union types      │
│ 03 Funciones/generic │ Resultado<T>, funciones de busqueda   │
│ 04 Clases/POO        │ GestorTareas con private/readonly     │
│ 05 Modulos/config    │ Estructura modular (simulada)         │
│ 06 Tipos avanzados   │ Partial, Pick, Omit, type guards     │
└──────────────────────┴────────────────────────────────────────┘
```

## Modelo de Datos

```
  interface Tarea {
    readonly id: string;           <-- readonly (no cambia)
    titulo: string;                <-- string basico
    descripcion?: string;          <-- opcional
    estado: Estado;                <-- enum
    prioridad: Prioridad;          <-- enum
    etiquetas: string[];           <-- array
    creadaEn: Date;                <-- Date
    actualizadaEn: Date;
    fechaLimite?: Date;            <-- opcional
  }

  Estado:
  ┌─────────────┐   ┌──────────────┐   ┌──────────────┐
  │  Pendiente  │──▶│ En Progreso  │──▶│  Completada  │
  └─────────────┘   └──────────────┘   └──────────────┘
                                              │
                                        ┌─────┴──────┐
                                        │  Cancelada  │
                                        └────────────┘
```

## Patron Resultado<T>

Se usa para manejar errores de forma tipada, sin excepciones.

```
  type Resultado<T> =
    | { exito: true; datos: T }
    | { exito: false; error: string }

  Ejemplo:
  ┌────────────────────────────────────────────┐
  │ crear("Tarea 1")                           │
  │   → { exito: true, datos: { id: "...", ...}} │
  │                                            │
  │ crear("")  // titulo vacio                 │
  │   → { exito: false, error: "Titulo req." }│
  └────────────────────────────────────────────┘
```

## Utility Types en el Proyecto

```
  Partial<Tarea>    — Para actualizar (solo enviar lo que cambia)
  Pick<Tarea, ...>  — Para el resumen de una tarea
  Omit<Tarea, "id"> — Para crear (el id se genera internamente)
  Record<Estado, n> — Para las estadisticas por estado
  Readonly<Tarea>   — Para la tarea devuelta (no modificable desde fuera)
```

## Flujo de Uso

```
  1. Crear gestor
     const gestor = new GestorTareas();

  2. Agregar tarea
     const resultado = gestor.crear({
       titulo: "Aprender TypeScript",
       prioridad: Prioridad.Alta,
       etiquetas: ["estudio", "programacion"]
     });

  3. Actualizar tarea
     gestor.actualizar(id, { estado: Estado.EnProgreso });

  4. Filtrar tareas
     const urgentes = gestor.filtrar({
       estado: Estado.Pendiente,
       prioridad: Prioridad.Alta
     });

  5. Obtener estadisticas
     const stats = gestor.estadisticas();
     // { total: 5, porEstado: { pendiente: 2, ... }, ... }
```

## Puntos de Aprendizaje

1. **Modelado de datos** — Definir interfaces antes de escribir logica
2. **Seguridad de tipos** — El compilador detecta errores de uso
3. **Genericos** — Resultado<T> funciona con cualquier tipo de datos
4. **Utility types** — Evitar duplicar interfaces similares
5. **Type guards** — Verificar el tipo de Resultado antes de usar .datos
6. **Enums** — Estados y prioridades como conjuntos cerrados
7. **Readonly** — Prevenir modificaciones accidentales de datos

## Como Ejecutar

```bash
# Compilar
tsc ejemplos.ts

# Ejecutar
node ejemplos.js

# O con ts-node (sin compilar)
npx ts-node ejemplos.ts
```

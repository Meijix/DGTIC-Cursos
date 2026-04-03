// ============================================================================
// 07 — PROYECTO INTEGRADOR: Gestor de Tareas Tipado
// ============================================================================
// Un mini-proyecto que combina TODOS los conceptos de TypeScript:
// - Interfaces, types, enums (secciones 01-02)
// - Genericos, funciones tipadas (seccion 03)
// - Clases con modificadores de acceso (seccion 04)
// - Estructura modular (seccion 05)
// - Utility types, mapped types, type guards (seccion 06)
//
// Compilar: tsc ejemplos.ts
// Ejecutar: node ejemplos.js
// ============================================================================


// ============================================================================
// TIPOS E INTERFACES
// ============================================================================

// --- Enums: conjuntos cerrados de valores ---

enum Estado {
  Pendiente = "PENDIENTE",
  EnProgreso = "EN_PROGRESO",
  Completada = "COMPLETADA",
  Cancelada = "CANCELADA"
}

enum Prioridad {
  Baja = "BAJA",
  Media = "MEDIA",
  Alta = "ALTA",
  Urgente = "URGENTE"
}

// --- Interface principal ---

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

// --- DTOs con Utility Types ---

// Para crear: sin id ni timestamps (se generan internamente)
type CrearTareaDTO = Omit<Tarea, "id" | "creadaEn" | "actualizadaEn"> & {
  descripcion?: string;
  fechaLimite?: Date;
};

// Para actualizar: todo opcional excepto id y fecha de creacion
type ActualizarTareaDTO = Partial<Omit<Tarea, "id" | "creadaEn">>;

// Para mostrar resumen
type ResumenTarea = Pick<Tarea, "id" | "titulo" | "estado" | "prioridad">;

// --- Tipo generico para resultados ---

type Resultado<T> =
  | { exito: true; datos: T }
  | { exito: false; error: string };

// --- Filtros ---

interface FiltroTareas {
  estado?: Estado;
  prioridad?: Prioridad;
  etiqueta?: string;
  busqueda?: string;
}

// --- Estadisticas ---

interface EstadisticasTareas {
  total: number;
  porEstado: Record<Estado, number>;
  porPrioridad: Record<Prioridad, number>;
  completadas: number;
  pendientes: number;
  tasaCompletado: string;
}


// ============================================================================
// TYPE GUARDS
// ============================================================================

function esExito<T>(resultado: Resultado<T>): resultado is { exito: true; datos: T } {
  return resultado.exito === true;
}

function esFallo<T>(resultado: Resultado<T>): resultado is { exito: false; error: string } {
  return resultado.exito === false;
}


// ============================================================================
// CLASE PRINCIPAL: GestorTareas
// ============================================================================

class GestorTareas {
  private _tareas: Map<string, Tarea> = new Map();
  private _contadorId: number = 0;

  // --- Metodo privado: generar ID unico ---
  private _generarId(): string {
    this._contadorId++;
    return `tarea-${this._contadorId.toString().padStart(4, "0")}`;
  }

  // --- Metodo privado: validar datos de creacion ---
  private _validarCreacion(datos: CrearTareaDTO): string[] {
    const errores: string[] = [];

    if (!datos.titulo || datos.titulo.trim().length < 3) {
      errores.push("El titulo debe tener al menos 3 caracteres");
    }

    if (datos.titulo && datos.titulo.length > 100) {
      errores.push("El titulo no puede exceder 100 caracteres");
    }

    if (datos.fechaLimite && datos.fechaLimite < new Date()) {
      errores.push("La fecha limite no puede ser en el pasado");
    }

    if (!Object.values(Estado).includes(datos.estado)) {
      errores.push("Estado invalido");
    }

    if (!Object.values(Prioridad).includes(datos.prioridad)) {
      errores.push("Prioridad invalida");
    }

    return errores;
  }

  // --- CREAR tarea ---
  crear(datos: CrearTareaDTO): Resultado<Readonly<Tarea>> {
    const errores = this._validarCreacion(datos);
    if (errores.length > 0) {
      return { exito: false, error: errores.join("; ") };
    }

    const ahora = new Date();
    const tarea: Tarea = {
      id: this._generarId(),
      titulo: datos.titulo.trim(),
      descripcion: datos.descripcion?.trim(),
      estado: datos.estado,
      prioridad: datos.prioridad,
      etiquetas: [...datos.etiquetas],
      creadaEn: ahora,
      actualizadaEn: ahora,
      fechaLimite: datos.fechaLimite
    };

    this._tareas.set(tarea.id, tarea);
    return { exito: true, datos: tarea };
  }

  // --- ACTUALIZAR tarea (Partial) ---
  actualizar(id: string, cambios: ActualizarTareaDTO): Resultado<Readonly<Tarea>> {
    const tarea = this._tareas.get(id);
    if (!tarea) {
      return { exito: false, error: `Tarea con ID '${id}' no encontrada` };
    }

    const tareaActualizada: Tarea = {
      ...tarea,
      ...cambios,
      id: tarea.id,             // readonly: no se puede cambiar
      creadaEn: tarea.creadaEn, // readonly: no se puede cambiar
      actualizadaEn: new Date()
    };

    this._tareas.set(id, tareaActualizada);
    return { exito: true, datos: tareaActualizada };
  }

  // --- ELIMINAR tarea ---
  eliminar(id: string): Resultado<void> {
    if (!this._tareas.has(id)) {
      return { exito: false, error: `Tarea con ID '${id}' no encontrada` };
    }
    this._tareas.delete(id);
    return { exito: true, datos: undefined };
  }

  // --- BUSCAR por ID ---
  buscarPorId(id: string): Resultado<Readonly<Tarea>> {
    const tarea = this._tareas.get(id);
    if (!tarea) {
      return { exito: false, error: `Tarea con ID '${id}' no encontrada` };
    }
    return { exito: true, datos: tarea };
  }

  // --- FILTRAR tareas ---
  filtrar(filtro: FiltroTareas): Readonly<Tarea>[] {
    let resultado = Array.from(this._tareas.values());

    if (filtro.estado) {
      resultado = resultado.filter(t => t.estado === filtro.estado);
    }

    if (filtro.prioridad) {
      resultado = resultado.filter(t => t.prioridad === filtro.prioridad);
    }

    if (filtro.etiqueta) {
      resultado = resultado.filter(t =>
        t.etiquetas.includes(filtro.etiqueta!)
      );
    }

    if (filtro.busqueda) {
      const termino = filtro.busqueda.toLowerCase();
      resultado = resultado.filter(t =>
        t.titulo.toLowerCase().includes(termino) ||
        (t.descripcion?.toLowerCase().includes(termino) ?? false)
      );
    }

    return resultado;
  }

  // --- LISTAR todas ---
  listar(): Readonly<Tarea>[] {
    return Array.from(this._tareas.values());
  }

  // --- RESUMEN (Pick) ---
  resumenes(): ResumenTarea[] {
    return Array.from(this._tareas.values()).map(t => ({
      id: t.id,
      titulo: t.titulo,
      estado: t.estado,
      prioridad: t.prioridad
    }));
  }

  // --- ESTADISTICAS (Record) ---
  estadisticas(): EstadisticasTareas {
    const tareas = Array.from(this._tareas.values());
    const total = tareas.length;

    // Conteo por estado usando Record
    const porEstado: Record<Estado, number> = {
      [Estado.Pendiente]: 0,
      [Estado.EnProgreso]: 0,
      [Estado.Completada]: 0,
      [Estado.Cancelada]: 0
    };

    // Conteo por prioridad usando Record
    const porPrioridad: Record<Prioridad, number> = {
      [Prioridad.Baja]: 0,
      [Prioridad.Media]: 0,
      [Prioridad.Alta]: 0,
      [Prioridad.Urgente]: 0
    };

    tareas.forEach(t => {
      porEstado[t.estado]++;
      porPrioridad[t.prioridad]++;
    });

    const completadas = porEstado[Estado.Completada];
    const pendientes = porEstado[Estado.Pendiente];
    const tasaCompletado = total > 0
      ? ((completadas / total) * 100).toFixed(1) + "%"
      : "0%";

    return { total, porEstado, porPrioridad, completadas, pendientes, tasaCompletado };
  }

  // --- EXPORTAR como JSON ---
  exportar(): string {
    const datos = {
      exportadoEn: new Date().toISOString(),
      totalTareas: this._tareas.size,
      tareas: Array.from(this._tareas.values())
    };
    return JSON.stringify(datos, null, 2);
  }
}


// ============================================================================
// FUNCIONES UTILITARIAS
// ============================================================================

function formatearTarea(tarea: Readonly<Tarea>): string {
  const prioridadEmoji: Record<Prioridad, string> = {
    [Prioridad.Baja]: "[BAJA]",
    [Prioridad.Media]: "[MEDIA]",
    [Prioridad.Alta]: "[ALTA]",
    [Prioridad.Urgente]: "[URGENTE]"
  };

  const partes = [
    `  ${prioridadEmoji[tarea.prioridad]} ${tarea.titulo}`,
    `    ID: ${tarea.id} | Estado: ${tarea.estado}`,
    `    Etiquetas: ${tarea.etiquetas.join(", ") || "ninguna"}`
  ];

  if (tarea.descripcion) {
    partes.push(`    Descripcion: ${tarea.descripcion}`);
  }

  return partes.join("\n");
}

function formatearEstadisticas(stats: EstadisticasTareas): string {
  return [
    `  Total: ${stats.total} tareas`,
    `  Pendientes: ${stats.pendientes} | Completadas: ${stats.completadas}`,
    `  Tasa de completado: ${stats.tasaCompletado}`,
    `  Por estado:`,
    ...Object.entries(stats.porEstado).map(
      ([estado, n]) => `    ${estado}: ${n}`
    ),
    `  Por prioridad:`,
    ...Object.entries(stats.porPrioridad).map(
      ([prio, n]) => `    ${prio}: ${n}`
    )
  ].join("\n");
}


// ============================================================================
// EJECUCION DEL PROYECTO
// ============================================================================

console.log("=============================================");
console.log("  GESTOR DE TAREAS — TypeScript Integrador   ");
console.log("=============================================\n");

const gestor = new GestorTareas();

// --- 1. Crear tareas ---
console.log("--- Creando tareas ---\n");

const tareas: CrearTareaDTO[] = [
  {
    titulo: "Aprender tipos basicos de TypeScript",
    descripcion: "Estudiar string, number, boolean, enums y tuplas",
    estado: Estado.Completada,
    prioridad: Prioridad.Alta,
    etiquetas: ["estudio", "typescript"]
  },
  {
    titulo: "Practicar interfaces y types",
    descripcion: "Crear interfaces para un proyecto real",
    estado: Estado.EnProgreso,
    prioridad: Prioridad.Alta,
    etiquetas: ["estudio", "typescript", "practica"]
  },
  {
    titulo: "Implementar genericos en proyecto personal",
    estado: Estado.Pendiente,
    prioridad: Prioridad.Media,
    etiquetas: ["proyecto", "typescript"]
  },
  {
    titulo: "Revisar documentacion de utility types",
    estado: Estado.Pendiente,
    prioridad: Prioridad.Baja,
    etiquetas: ["estudio", "documentacion"]
  },
  {
    titulo: "Configurar tsconfig.json para proyecto nuevo",
    estado: Estado.Pendiente,
    prioridad: Prioridad.Urgente,
    etiquetas: ["config", "proyecto"]
  },
  {
    titulo: "Escribir tests con tipos para API",
    estado: Estado.Cancelada,
    prioridad: Prioridad.Media,
    etiquetas: ["testing", "api"]
  }
];

const idsCreados: string[] = [];

tareas.forEach(datos => {
  const resultado = gestor.crear(datos);
  if (esExito(resultado)) {
    idsCreados.push(resultado.datos.id);
    console.log(`  Creada: "${resultado.datos.titulo}" (${resultado.datos.id})`);
  } else {
    console.log(`  Error: ${resultado.error}`);
  }
});

// --- 2. Intentar crear tarea invalida ---
console.log("\n--- Validacion ---\n");

const invalida = gestor.crear({
  titulo: "AB",  // muy corto
  estado: Estado.Pendiente,
  prioridad: Prioridad.Alta,
  etiquetas: []
});

if (esFallo(invalida)) {
  console.log(`  Validacion correcta: "${invalida.error}"`);
}

// --- 3. Actualizar tarea (Partial) ---
console.log("\n--- Actualizando tareas ---\n");

const actualizacion = gestor.actualizar(idsCreados[2], {
  estado: Estado.EnProgreso,
  descripcion: "Implementando cola generica y tipo Resultado<T>"
});

if (esExito(actualizacion)) {
  console.log(`  Actualizada: "${actualizacion.datos.titulo}"`);
  console.log(`    Nuevo estado: ${actualizacion.datos.estado}`);
  console.log(`    Descripcion: ${actualizacion.datos.descripcion}`);
}

// --- 4. Buscar por ID ---
console.log("\n--- Busqueda por ID ---\n");

const buscada = gestor.buscarPorId(idsCreados[0]);
if (esExito(buscada)) {
  console.log(formatearTarea(buscada.datos));
}

// Buscar ID inexistente
const noExiste = gestor.buscarPorId("tarea-9999");
if (esFallo(noExiste)) {
  console.log(`\n  Busqueda fallida: ${noExiste.error}`);
}

// --- 5. Filtrar tareas ---
console.log("\n--- Filtrar: Pendientes ---\n");

const pendientes = gestor.filtrar({ estado: Estado.Pendiente });
pendientes.forEach(t => console.log(formatearTarea(t)));

console.log("\n--- Filtrar: Etiqueta 'typescript' ---\n");

const deTypeScript = gestor.filtrar({ etiqueta: "typescript" });
deTypeScript.forEach(t => console.log(formatearTarea(t)));

console.log("\n--- Filtrar: Busqueda 'genericos' ---\n");

const busqueda = gestor.filtrar({ busqueda: "genericos" });
busqueda.forEach(t => console.log(formatearTarea(t)));

// --- 6. Resumenes (Pick) ---
console.log("\n--- Resumenes (Pick<Tarea, ...>) ---\n");

const resumenes = gestor.resumenes();
resumenes.forEach(r => {
  console.log(`  [${r.id}] ${r.titulo} — ${r.estado} (${r.prioridad})`);
});

// --- 7. Estadisticas (Record) ---
console.log("\n--- Estadisticas ---\n");

const stats = gestor.estadisticas();
console.log(formatearEstadisticas(stats));

// --- 8. Eliminar tarea ---
console.log("\n--- Eliminando tarea cancelada ---\n");

const eliminada = gestor.eliminar(idsCreados[5]);
if (esExito(eliminada)) {
  console.log(`  Tarea eliminada exitosamente`);
  console.log(`  Tareas restantes: ${gestor.listar().length}`);
}

// --- 9. Estadisticas finales ---
console.log("\n--- Estadisticas finales ---\n");

const statsFinal = gestor.estadisticas();
console.log(formatearEstadisticas(statsFinal));

console.log("\n=============================================");
console.log("  Proyecto completado — todos los conceptos  ");
console.log("  de TypeScript aplicados en un solo archivo  ");
console.log("=============================================");

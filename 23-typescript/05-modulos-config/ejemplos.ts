// ============================================================================
// 05 — MODULOS Y CONFIGURACION
// ============================================================================
// Este archivo muestra patrones de modulos ES en TypeScript.
// En un proyecto real, cada seccion estaria en su propio archivo.
//
// Compilar: tsc ejemplos.ts
// Ejecutar: node ejemplos.js
// ============================================================================


// ----------------------------------------------------------------------------
// 1. SIMULACION DE MODULOS
// En un proyecto real, cada bloque seria un archivo .ts separado
// con import/export. Aqui lo simulamos con namespaces y comentarios.
// ----------------------------------------------------------------------------

// ── archivo: tipos.ts ──
// export interface Usuario { ... }
// export type Rol = "admin" | "editor" | "lector";

interface Usuario {
  id: number;
  nombre: string;
  email: string;
  rol: Rol;
}

type Rol = "admin" | "editor" | "lector";

interface Config {
  host: string;
  puerto: number;
  debug: boolean;
  entorno: "desarrollo" | "produccion" | "pruebas";
}


// ── archivo: constantes.ts ──
// export const CONFIG_DEFAULT: Config = { ... }

const CONFIG_DEFAULT: Config = {
  host: "localhost",
  puerto: 3000,
  debug: true,
  entorno: "desarrollo"
};

const ROLES_PERMITIDOS: readonly Rol[] = ["admin", "editor", "lector"];


// ── archivo: validadores.ts ──
// export function validarEmail(email: string): boolean { ... }

function validarEmail(email: string): boolean {
  const patron = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return patron.test(email);
}

function validarUsuario(usuario: Partial<Usuario>): string[] {
  const errores: string[] = [];

  if (!usuario.nombre || usuario.nombre.trim().length < 2) {
    errores.push("Nombre debe tener al menos 2 caracteres");
  }

  if (!usuario.email || !validarEmail(usuario.email)) {
    errores.push("Email invalido");
  }

  if (usuario.rol && !ROLES_PERMITIDOS.includes(usuario.rol)) {
    errores.push(`Rol invalido. Opciones: ${ROLES_PERMITIDOS.join(", ")}`);
  }

  return errores;
}


// ── archivo: servicios.ts ──
// import { Usuario, Config } from "./tipos.js";
// import { validarUsuario } from "./validadores.js";

class ServicioUsuarios {
  private usuarios: Usuario[] = [];
  private siguienteId: number = 1;

  constructor(private config: Config) {}

  crear(datos: Omit<Usuario, "id">): Usuario {
    const errores = validarUsuario(datos);
    if (errores.length > 0) {
      throw new Error(`Validacion fallida: ${errores.join("; ")}`);
    }

    const usuario: Usuario = {
      id: this.siguienteId++,
      ...datos
    };
    this.usuarios.push(usuario);

    if (this.config.debug) {
      console.log(`  [DEBUG] Usuario creado: ${usuario.nombre} (ID: ${usuario.id})`);
    }

    return usuario;
  }

  buscarPorId(id: number): Usuario | undefined {
    return this.usuarios.find(u => u.id === id);
  }

  buscarPorRol(rol: Rol): Usuario[] {
    return this.usuarios.filter(u => u.rol === rol);
  }

  listar(): Usuario[] {
    return [...this.usuarios];
  }

  eliminar(id: number): boolean {
    const indice = this.usuarios.findIndex(u => u.id === id);
    if (indice === -1) return false;
    this.usuarios.splice(indice, 1);
    return true;
  }
}


// ----------------------------------------------------------------------------
// 2. EJEMPLO DE tsconfig.json COMENTADO
// (Mostrado como objeto para referencia)
// ----------------------------------------------------------------------------

const tsconfigEjemplo = {
  compilerOptions: {
    // -- Salida --
    target: "ES2020",            // Version de JS generado
    module: "ESNext",            // Sistema de modulos
    outDir: "./dist",            // Donde van los .js compilados
    rootDir: "./src",            // Donde esta el codigo fuente

    // -- Verificacion estricta --
    strict: true,                // Activa TODAS las verificaciones estrictas
    // Equivale a activar: noImplicitAny, strictNullChecks,
    // strictFunctionTypes, strictBindCallApply,
    // strictPropertyInitialization, noImplicitThis, alwaysStrict

    // -- Calidad de codigo --
    noUnusedLocals: true,        // Error en variables locales sin usar
    noUnusedParameters: true,    // Error en parametros sin usar
    noImplicitReturns: true,     // Error si una rama no retorna

    // -- Resolucion de modulos --
    moduleResolution: "bundler", // Para Vite/webpack. Usar "node16" para Node
    esModuleInterop: true,       // Compatibilidad CJS <-> ESM
    resolveJsonModule: true,     // Permite import de .json

    // -- Generacion --
    declaration: true,           // Genera archivos .d.ts
    sourceMap: true,             // Genera .js.map para debug
    skipLibCheck: true           // Omite verificar .d.ts (acelera compilacion)
  },
  include: ["src/**/*"],
  exclude: ["node_modules", "dist", "**/*.test.ts"]
};


// ----------------------------------------------------------------------------
// 3. PATRONES DE IMPORT/EXPORT (como referencia)
// ----------------------------------------------------------------------------

/*
  === NAMED EXPORTS (multiples por archivo) ===

  // math.ts
  export function sumar(a: number, b: number): number { return a + b; }
  export function restar(a: number, b: number): number { return a - b; }
  export const PI = 3.14159;

  // main.ts
  import { sumar, restar, PI } from "./math.js";
  import { sumar as add } from "./math.js";  // renombrar
  import * as Math from "./math.js";          // importar todo


  === DEFAULT EXPORT (uno por archivo) ===

  // logger.ts
  export default class Logger {
    log(msg: string): void { console.log(msg); }
  }

  // main.ts
  import Logger from "./logger.js";
  import MiLogger from "./logger.js";  // cualquier nombre


  === EXPORT SOLO DE TIPOS ===

  // tipos.ts
  export type ID = string | number;
  export interface Config { host: string; }

  // main.ts
  import type { ID, Config } from "./tipos.js";
  // 'type' indica que se elimina en compilacion


  === RE-EXPORTS (barrel files) ===

  // index.ts (barrel file)
  export { sumar, restar } from "./math.js";
  export { default as Logger } from "./logger.js";
  export * from "./utils.js";
  export type { Config } from "./tipos.js";
*/


// ----------------------------------------------------------------------------
// 4. DECLARATION FILES (.d.ts) — Referencia
// ----------------------------------------------------------------------------

/*
  Los archivos .d.ts contienen solo tipos, sin codigo ejecutable.
  Se usan para describir librerias JavaScript sin tipos.

  // mi-libreria.d.ts
  declare module "mi-libreria" {
    export function procesar(datos: string): number;
    export const VERSION: string;

    export interface Opciones {
      verbose?: boolean;
      timeout?: number;
    }

    export default class Cliente {
      constructor(opciones?: Opciones);
      conectar(): Promise<void>;
      desconectar(): void;
    }
  }

  // Ampliar tipos globales
  // global.d.ts
  declare global {
    interface Window {
      __APP_VERSION__: string;
    }

    // Declarar modulos para assets
    declare module "*.css" {
      const content: string;
      export default content;
    }

    declare module "*.png" {
      const src: string;
      export default src;
    }
  }
*/


// ----------------------------------------------------------------------------
// 5. EJECUCION — Usar los servicios definidos arriba
// ----------------------------------------------------------------------------

console.log("=== Modulos y Configuracion — Demo ===\n");

// Crear servicio con configuracion
const servicio = new ServicioUsuarios(CONFIG_DEFAULT);

// Crear usuarios
console.log("--- Creando usuarios ---");
servicio.crear({ nombre: "Ana Garcia", email: "ana@ejemplo.com", rol: "admin" });
servicio.crear({ nombre: "Carlos Lopez", email: "carlos@ejemplo.com", rol: "editor" });
servicio.crear({ nombre: "Maria Torres", email: "maria@ejemplo.com", rol: "lector" });
servicio.crear({ nombre: "Pedro Ruiz", email: "pedro@ejemplo.com", rol: "editor" });

// Buscar
console.log("\n--- Buscar por ID ---");
const usuario = servicio.buscarPorId(1);
console.log(`  ID 1: ${usuario?.nombre} (${usuario?.rol})`);

// Filtrar por rol
console.log("\n--- Editores ---");
const editores = servicio.buscarPorRol("editor");
editores.forEach(e => console.log(`  ${e.nombre}`));

// Validacion fallida
console.log("\n--- Validacion fallida ---");
try {
  servicio.crear({ nombre: "", email: "invalido", rol: "admin" });
} catch (e) {
  console.log(`  Error: ${(e as Error).message}`);
}

// Listar todos
console.log("\n--- Todos los usuarios ---");
servicio.listar().forEach(u => {
  console.log(`  [${u.id}] ${u.nombre} — ${u.email} (${u.rol})`);
});

// Mostrar config usada
console.log("\n--- Configuracion activa ---");
console.log(`  Host: ${CONFIG_DEFAULT.host}:${CONFIG_DEFAULT.puerto}`);
console.log(`  Entorno: ${CONFIG_DEFAULT.entorno}`);
console.log(`  Debug: ${CONFIG_DEFAULT.debug}`);

// Referencia al tsconfig
console.log("\n--- tsconfig.json de referencia ---");
console.log(`  Target: ${tsconfigEjemplo.compilerOptions.target}`);
console.log(`  Module: ${tsconfigEjemplo.compilerOptions.module}`);
console.log(`  Strict: ${tsconfigEjemplo.compilerOptions.strict}`);

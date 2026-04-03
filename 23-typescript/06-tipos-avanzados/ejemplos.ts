// ============================================================================
// 06 — TIPOS AVANZADOS
// ============================================================================
// Compilar: tsc ejemplos.ts
// Ejecutar: node ejemplos.js
// ============================================================================


// ----------------------------------------------------------------------------
// 1. UTILITY TYPES: Partial, Required, Readonly
// ----------------------------------------------------------------------------

interface Usuario {
  id: number;
  nombre: string;
  email: string;
  edad: number;
  activo: boolean;
}

// Partial — todas las propiedades opcionales
function actualizarUsuario(id: number, cambios: Partial<Usuario>): void {
  console.log(`  Actualizando usuario ${id} con:`, cambios);
}

// Required — todas las propiedades obligatorias
type UsuarioCompleto = Required<Partial<Usuario>>;

// Readonly — ninguna propiedad se puede modificar
type UsuarioInmutable = Readonly<Usuario>;

console.log("=== Partial, Required, Readonly ===");
actualizarUsuario(1, { nombre: "Nuevo nombre" });          // solo nombre
actualizarUsuario(1, { email: "nuevo@mail.com", edad: 30 }); // email y edad

const inmutable: UsuarioInmutable = {
  id: 1, nombre: "Ana", email: "ana@mail.com", edad: 28, activo: true
};
// inmutable.nombre = "otro";  // ERROR: Cannot assign to 'nombre'
console.log("Inmutable:", inmutable);


// ----------------------------------------------------------------------------
// 2. UTILITY TYPES: Pick y Omit
// ----------------------------------------------------------------------------

// Pick — seleccionar propiedades especificas
type UsuarioPublico = Pick<Usuario, "id" | "nombre">;

// Omit — excluir propiedades
type UsuarioSinId = Omit<Usuario, "id">;

interface UsuarioConPassword extends Usuario {
  password: string;
}
type UsuarioSeguro = Omit<UsuarioConPassword, "password">;

const publico: UsuarioPublico = { id: 1, nombre: "Ana" };
const sinId: UsuarioSinId = { nombre: "Ana", email: "a@b.com", edad: 28, activo: true };

console.log("\n=== Pick y Omit ===");
console.log("Publico (Pick):", publico);
console.log("Sin ID (Omit):", sinId);


// ----------------------------------------------------------------------------
// 3. UTILITY TYPES: Record
// ----------------------------------------------------------------------------

type Rol = "admin" | "editor" | "lector";

// Crear un mapa de permisos por rol
const permisos: Record<Rol, string[]> = {
  admin: ["crear", "leer", "editar", "eliminar"],
  editor: ["crear", "leer", "editar"],
  lector: ["leer"]
};

// Record con string keys
const contadorPalabras: Record<string, number> = {};
const texto = "hola mundo hola typescript hola";
texto.split(" ").forEach(palabra => {
  contadorPalabras[palabra] = (contadorPalabras[palabra] || 0) + 1;
});

console.log("\n=== Record ===");
console.log("Permisos:", permisos);
console.log("Contador:", contadorPalabras);


// ----------------------------------------------------------------------------
// 4. UTILITY TYPES: Exclude, Extract, NonNullable
// ----------------------------------------------------------------------------

type TodosTipos = string | number | boolean | null | undefined;

type SoloValores = NonNullable<TodosTipos>;          // string | number | boolean
type SoloTextoNum = Exclude<TodosTipos, boolean | null | undefined>; // string | number
type SoloPrimitivos = Extract<TodosTipos, string | number>; // string | number

console.log("\n=== Exclude, Extract, NonNullable ===");
// Estos son tipos, no valores. Los usamos para demostrar:
const valor1: SoloValores = "hola";        // OK
// const valor2: SoloValores = null;        // ERROR
const valor3: SoloTextoNum = 42;           // OK
// const valor4: SoloTextoNum = true;       // ERROR
console.log("SoloValores ejemplo:", valor1);
console.log("SoloTextoNum ejemplo:", valor3);


// ----------------------------------------------------------------------------
// 5. UTILITY TYPES: ReturnType y Parameters
// ----------------------------------------------------------------------------

function crearUsuario(nombre: string, edad: number, email: string) {
  return { id: Math.random(), nombre, edad, email, creado: new Date() };
}

type UsuarioCreado = ReturnType<typeof crearUsuario>;
type ParamsCrear = Parameters<typeof crearUsuario>;

console.log("\n=== ReturnType y Parameters ===");
const params: ParamsCrear = ["Ana", 28, "ana@mail.com"];
const resultado: UsuarioCreado = crearUsuario(...params);
console.log("Creado:", resultado);


// ----------------------------------------------------------------------------
// 6. MAPPED TYPES — Transformaciones personalizadas
// ----------------------------------------------------------------------------

// Hacer todas las propiedades nullable
type Nullable<T> = {
  [K in keyof T]: T[K] | null;
};

// Hacer getters automaticos
type Getters<T> = {
  [K in keyof T as `get${Capitalize<string & K>}`]: () => T[K];
};

interface Punto { x: number; y: number; }

type PuntoNullable = Nullable<Punto>;
// { x: number | null; y: number | null }

type PuntoGetters = Getters<Punto>;
// { getX: () => number; getY: () => number }

const puntoNull: PuntoNullable = { x: 10, y: null };
const puntoGet: PuntoGetters = {
  getX: () => 10,
  getY: () => 20
};

console.log("\n=== Mapped Types ===");
console.log("Nullable:", puntoNull);
console.log("Getters:", puntoGet.getX(), puntoGet.getY());


// ----------------------------------------------------------------------------
// 7. CONDITIONAL TYPES
// ----------------------------------------------------------------------------

// Tipo que verifica si algo es un array
type EsArray<T> = T extends any[] ? true : false;

type Test1 = EsArray<string[]>;    // true
type Test2 = EsArray<number>;      // false

// Extraer tipo de elemento de un array
type ElementoDe<T> = T extends (infer E)[] ? E : never;

type Elem1 = ElementoDe<string[]>;    // string
type Elem2 = ElementoDe<number[]>;    // number

// Extraer tipo de retorno (reimplementacion de ReturnType)
type MiReturnType<T> = T extends (...args: any[]) => infer R ? R : never;

type R1 = MiReturnType<() => string>;           // string
type R2 = MiReturnType<(x: number) => boolean>; // boolean

// Tipo condicional practico: aplanar promesas
type Aplanar<T> = T extends Promise<infer U> ? Aplanar<U> : T;

type A1 = Aplanar<Promise<string>>;             // string
type A2 = Aplanar<Promise<Promise<number>>>;    // number

console.log("\n=== Conditional Types ===");
console.log("(Los conditional types son verificados en compilacion)");
console.log("EsArray<string[]> = true, EsArray<number> = false");


// ----------------------------------------------------------------------------
// 8. TEMPLATE LITERAL TYPES
// ----------------------------------------------------------------------------

type Color = "rojo" | "verde" | "azul";
type Tamano = "sm" | "md" | "lg";

// Genera todas las combinaciones
type ClaseCSS = `${Tamano}-${Color}`;
// "sm-rojo"|"sm-verde"|"sm-azul"|"md-rojo"|"md-verde"|"md-azul"|...

type MetodoHTTP = "GET" | "POST" | "PUT" | "DELETE";
type Recurso = "users" | "posts" | "comments";
type Endpoint = `${MetodoHTTP} /api/${Recurso}`;

const clase: ClaseCSS = "lg-azul";
const endpoint: Endpoint = "GET /api/users";

console.log("\n=== Template Literal Types ===");
console.log(`Clase CSS: ${clase}`);
console.log(`Endpoint: ${endpoint}`);

// Tipos de eventos del DOM con template literals
type EventoBase = "click" | "focus" | "blur" | "change";
type HandlerName = `on${Capitalize<EventoBase>}`;
// "onClick" | "onFocus" | "onBlur" | "onChange"

const handler: HandlerName = "onClick";
console.log(`Handler: ${handler}`);


// ----------------------------------------------------------------------------
// 9. TYPE GUARDS — Todas las formas
// ----------------------------------------------------------------------------

// --- typeof ---
function procesarValor(valor: string | number | boolean): string {
  if (typeof valor === "string") return `Texto: ${valor.toUpperCase()}`;
  if (typeof valor === "number") return `Numero: ${valor.toFixed(2)}`;
  return `Booleano: ${valor ? "verdadero" : "falso"}`;
}

// --- instanceof ---
class ApiError extends Error {
  constructor(public statusCode: number, message: string) {
    super(message);
  }
}

function manejarError(error: Error): string {
  if (error instanceof ApiError) {
    return `Error API [${error.statusCode}]: ${error.message}`;
  }
  return `Error general: ${error.message}`;
}

// --- in ---
interface Coche { conducir(): void; ruedas: number; }
interface Bicicleta { pedalear(): void; ruedas: number; }

function describir(vehiculo: Coche | Bicicleta): string {
  if ("conducir" in vehiculo) {
    return "Es un coche";
  }
  return "Es una bicicleta";
}

// --- Custom type guard ---
interface Exito { ok: true; datos: string }
interface Fallo { ok: false; error: string }
type Resultado = Exito | Fallo;

function esExito(r: Resultado): r is Exito {
  return r.ok === true;
}

console.log("\n=== Type Guards ===");
console.log(procesarValor("hola"));
console.log(procesarValor(3.14159));
console.log(procesarValor(true));

console.log(manejarError(new ApiError(404, "No encontrado")));
console.log(manejarError(new Error("Algo fallo")));

const resultado: Resultado = { ok: true, datos: "Informacion cargada" };
if (esExito(resultado)) {
  console.log(`Custom guard — Datos: ${resultado.datos}`);
}


// ----------------------------------------------------------------------------
// 10. EJEMPLO INTEGRADOR: Sistema de formularios tipado
// Combina mapped types, conditional types, utility types y generics
// ----------------------------------------------------------------------------

// Tipo base de un campo de formulario
interface CampoFormulario<T> {
  valor: T;
  error: string | null;
  tocado: boolean;
  valido: boolean;
}

// Convertir interface a formulario (mapped type)
type Formulario<T> = {
  [K in keyof T]: CampoFormulario<T[K]>;
};

// Extraer solo los valores del formulario
type ValoresFormulario<T> = {
  [K in keyof T]: T[K] extends CampoFormulario<infer V> ? V : never;
};

// Interface del modelo
interface DatosRegistro {
  nombre: string;
  email: string;
  edad: number;
  aceptaTerminos: boolean;
}

// Crear formulario tipado
type FormRegistro = Formulario<DatosRegistro>;

const formulario: FormRegistro = {
  nombre: { valor: "Ana Garcia", error: null, tocado: true, valido: true },
  email: { valor: "ana@mail.com", error: null, tocado: true, valido: true },
  edad: { valor: 28, error: null, tocado: false, valido: true },
  aceptaTerminos: { valor: true, error: null, tocado: true, valido: true }
};

// Funcion para extraer valores del formulario
function extraerValores<T>(form: Formulario<T>): T {
  const resultado = {} as T;
  for (const key in form) {
    resultado[key] = form[key].valor;
  }
  return resultado;
}

// Funcion para verificar si el formulario es valido
function esFormularioValido<T>(form: Formulario<T>): boolean {
  return Object.values(form).every(
    (campo) => (campo as CampoFormulario<unknown>).valido
  );
}

console.log("\n=== Ejemplo Integrador: Formulario Tipado ===");
console.log("Valores:", extraerValores(formulario));
console.log("Valido:", esFormularioValido(formulario));

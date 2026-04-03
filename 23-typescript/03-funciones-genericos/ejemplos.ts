// ============================================================================
// 03 — FUNCIONES Y GENERICOS
// ============================================================================
// Compilar: tsc ejemplos.ts
// Ejecutar: node ejemplos.js
// ============================================================================


// ----------------------------------------------------------------------------
// 1. FUNCIONES CON TIPOS
// ----------------------------------------------------------------------------

function sumar(a: number, b: number): number {
  return a + b;
}

const multiplicar = (a: number, b: number): number => a * b;

// Tipo de funcion como variable
type OperacionMatematica = (a: number, b: number) => number;

const restar: OperacionMatematica = (a, b) => a - b;
const dividir: OperacionMatematica = (a, b) => {
  if (b === 0) throw new Error("Division por cero");
  return a / b;
};

console.log("=== Funciones Tipadas ===");
console.log(`Sumar: ${sumar(10, 5)}`);
console.log(`Multiplicar: ${multiplicar(10, 5)}`);
console.log(`Restar: ${restar(10, 5)}`);
console.log(`Dividir: ${dividir(10, 5)}`);


// ----------------------------------------------------------------------------
// 2. PARAMETROS OPCIONALES Y DEFAULT
// ----------------------------------------------------------------------------

function crearSaludo(
  nombre: string,
  saludo: string = "Hola",
  titulo?: string
): string {
  const tituloStr = titulo ? `${titulo} ` : "";
  return `${saludo}, ${tituloStr}${nombre}!`;
}

console.log("\n=== Opcionales y Default ===");
console.log(crearSaludo("Ana"));                       // Hola, Ana!
console.log(crearSaludo("Carlos", "Buenos dias"));     // Buenos dias, Carlos!
console.log(crearSaludo("Lopez", "Estimado", "Dr."));  // Estimado, Dr. Lopez!


// ----------------------------------------------------------------------------
// 3. REST PARAMETERS
// ----------------------------------------------------------------------------

function sumarTodos(...numeros: number[]): number {
  return numeros.reduce((acc, n) => acc + n, 0);
}

function concatenar(separador: string, ...partes: string[]): string {
  return partes.join(separador);
}

console.log("\n=== Rest Parameters ===");
console.log(`Suma total: ${sumarTodos(1, 2, 3, 4, 5)}`);
console.log(`Concatenar: ${concatenar(" - ", "uno", "dos", "tres")}`);


// ----------------------------------------------------------------------------
// 4. FUNCTION OVERLOADS
// Diferentes firmas para la misma funcion
// ----------------------------------------------------------------------------

// Firmas de overload
function formatear(valor: string): string;
function formatear(valor: number): string;
function formatear(valor: Date): string;

// Implementacion
function formatear(valor: string | number | Date): string {
  if (typeof valor === "string") {
    return valor.toUpperCase();
  }
  if (typeof valor === "number") {
    return valor.toFixed(2);
  }
  return valor.toISOString().split("T")[0];
}

console.log("\n=== Overloads ===");
console.log(formatear("hola mundo"));     // HOLA MUNDO
console.log(formatear(3.14159));           // 3.14
console.log(formatear(new Date()));        // 2024-01-01 (fecha actual)


// ----------------------------------------------------------------------------
// 5. GENERICOS BASICOS
// Funciones que trabajan con cualquier tipo
// ----------------------------------------------------------------------------

function identidad<T>(valor: T): T {
  return valor;
}

function primero<T>(arr: T[]): T | undefined {
  return arr[0];
}

function ultimo<T>(arr: T[]): T | undefined {
  return arr[arr.length - 1];
}

console.log("\n=== Genericos Basicos ===");
console.log(identidad<string>("TypeScript"));  // explicito
console.log(identidad(42));                     // inferido: number
console.log(primero([10, 20, 30]));            // 10 (number)
console.log(primero(["a", "b", "c"]));         // "a" (string)
console.log(ultimo([1, 2, 3, 4, 5]));          // 5


// ----------------------------------------------------------------------------
// 6. GENERICOS CON MULTIPLES PARAMETROS
// ----------------------------------------------------------------------------

function crearPar<K, V>(clave: K, valor: V): [K, V] {
  return [clave, valor];
}

function mapear<T, U>(arr: T[], transformar: (item: T) => U): U[] {
  return arr.map(transformar);
}

console.log("\n=== Multiples Parametros de Tipo ===");
console.log(crearPar("nombre", "Ana"));      // ["nombre", "Ana"]
console.log(crearPar(1, true));               // [1, true]

const numeros = [1, 2, 3, 4, 5];
const textos = mapear(numeros, n => `#${n}`);
console.log("Mapeado:", textos);               // ["#1", "#2", "#3", "#4", "#5"]


// ----------------------------------------------------------------------------
// 7. RESTRICCIONES (CONSTRAINTS)
// Limitar los tipos que acepta un generico
// ----------------------------------------------------------------------------

// T debe tener .length
function mostrarLargo<T extends { length: number }>(item: T): string {
  return `Largo: ${item.length}`;
}

console.log("\n=== Constraints ===");
console.log(mostrarLargo("Hola TypeScript"));  // Largo: 15
console.log(mostrarLargo([1, 2, 3]));          // Largo: 3
// mostrarLargo(42);  // ERROR: number no tiene .length

// Restriccion con keyof
function obtenerPropiedad<T, K extends keyof T>(obj: T, clave: K): T[K] {
  return obj[clave];
}

const persona = { nombre: "Ana", edad: 25, ciudad: "CDMX" };
console.log(obtenerPropiedad(persona, "nombre"));  // "Ana"
console.log(obtenerPropiedad(persona, "edad"));     // 25
// obtenerPropiedad(persona, "telefono");  // ERROR: no existe esa clave


// ----------------------------------------------------------------------------
// 8. INTERFACES GENERICAS
// ----------------------------------------------------------------------------

interface Respuesta<T> {
  datos: T;
  exito: boolean;
  mensaje: string;
  timestamp: number;
}

interface Paginado<T> {
  items: T[];
  pagina: number;
  porPagina: number;
  total: number;
}

// Usar las interfaces
const respUsuarios: Respuesta<string[]> = {
  datos: ["Ana", "Carlos", "Maria"],
  exito: true,
  mensaje: "Usuarios cargados",
  timestamp: Date.now()
};

const listaPaginada: Paginado<{ id: number; nombre: string }> = {
  items: [
    { id: 1, nombre: "Producto A" },
    { id: 2, nombre: "Producto B" }
  ],
  pagina: 1,
  porPagina: 10,
  total: 50
};

console.log("\n=== Interfaces Genericas ===");
console.log("Respuesta:", respUsuarios);
console.log("Paginado:", listaPaginada);


// ----------------------------------------------------------------------------
// 9. TYPE GENERICO: RESULTADO (OK / ERROR)
// Patron muy util para manejar errores de forma tipada
// ----------------------------------------------------------------------------

type Resultado<T> =
  | { ok: true; valor: T }
  | { ok: false; error: string };

function dividirSeguro(a: number, b: number): Resultado<number> {
  if (b === 0) {
    return { ok: false, error: "Division por cero" };
  }
  return { ok: true, valor: a / b };
}

function parsearJSON<T>(texto: string): Resultado<T> {
  try {
    const datos = JSON.parse(texto) as T;
    return { ok: true, valor: datos };
  } catch {
    return { ok: false, error: "JSON invalido" };
  }
}

console.log("\n=== Tipo Resultado ===");

const div1 = dividirSeguro(10, 3);
if (div1.ok) {
  console.log(`10/3 = ${div1.valor.toFixed(4)}`);
}

const div2 = dividirSeguro(10, 0);
if (!div2.ok) {
  console.log(`Error: ${div2.error}`);
}

const json1 = parsearJSON<{ nombre: string }>('{"nombre": "Ana"}');
if (json1.ok) {
  console.log(`Parseado: ${json1.valor.nombre}`);
}


// ----------------------------------------------------------------------------
// 10. EJEMPLO PRACTICO: Cola generica (Queue)
// Estructura de datos reutilizable con genericos
// ----------------------------------------------------------------------------

interface Cola<T> {
  encolar(item: T): void;
  desencolar(): T | undefined;
  frente(): T | undefined;
  estaVacia(): boolean;
  tamano(): number;
}

function crearCola<T>(): Cola<T> {
  const items: T[] = [];

  return {
    encolar(item: T): void {
      items.push(item);
    },
    desencolar(): T | undefined {
      return items.shift();
    },
    frente(): T | undefined {
      return items[0];
    },
    estaVacia(): boolean {
      return items.length === 0;
    },
    tamano(): number {
      return items.length;
    }
  };
}

console.log("\n=== Cola Generica ===");

// Cola de strings
const colaMensajes = crearCola<string>();
colaMensajes.encolar("Primer mensaje");
colaMensajes.encolar("Segundo mensaje");
colaMensajes.encolar("Tercer mensaje");

console.log(`Frente: ${colaMensajes.frente()}`);
console.log(`Tamano: ${colaMensajes.tamano()}`);
console.log(`Desencolado: ${colaMensajes.desencolar()}`);
console.log(`Nuevo frente: ${colaMensajes.frente()}`);

// Cola de numeros — misma implementacion, diferente tipo
const colaNumeros = crearCola<number>();
colaNumeros.encolar(100);
colaNumeros.encolar(200);
console.log(`\nCola numeros — frente: ${colaNumeros.frente()}`);

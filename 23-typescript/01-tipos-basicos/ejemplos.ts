// ============================================================================
// 01 — TIPOS BASICOS EN TYPESCRIPT
// ============================================================================
// Compilar: tsc ejemplos.ts
// Ejecutar: node ejemplos.js  (o usar ts-node ejemplos.ts)
// ============================================================================


// ----------------------------------------------------------------------------
// 1. TIPOS PRIMITIVOS
// ----------------------------------------------------------------------------

let nombre: string = "Maria";
let edad: number = 28;
let esEstudiante: boolean = true;
let sinValor: null = null;
let sinDefinir: undefined = undefined;

console.log("=== Tipos Primitivos ===");
console.log(`Nombre: ${nombre} (tipo: ${typeof nombre})`);
console.log(`Edad: ${edad} (tipo: ${typeof edad})`);
console.log(`Estudiante: ${esEstudiante} (tipo: ${typeof esEstudiante})`);


// ----------------------------------------------------------------------------
// 2. INFERENCIA DE TIPOS
// TypeScript deduce el tipo automaticamente cuando hay un valor inicial
// ----------------------------------------------------------------------------

let ciudad = "CDMX";          // TS infiere: string
let temperatura = 22.5;       // TS infiere: number
let conectado = false;        // TS infiere: boolean
const PI = 3.14159;           // TS infiere: 3.14159 (tipo literal con const)

console.log("\n=== Inferencia ===");
console.log(`Ciudad: ${ciudad} — PI: ${PI}`);


// ----------------------------------------------------------------------------
// 3. ARRAYS
// ----------------------------------------------------------------------------

let numeros: number[] = [10, 20, 30, 40, 50];
let frutas: Array<string> = ["manzana", "pera", "uva"];
let mixto: (string | number)[] = ["hola", 42, "mundo", 7];

// Array readonly — no se puede modificar despues de crear
let constantes: readonly number[] = [1, 1, 2, 3, 5, 8];
// constantes.push(13);  // ERROR: Property 'push' does not exist

console.log("\n=== Arrays ===");
console.log("Numeros:", numeros);
console.log("Frutas:", frutas);
console.log("Mixto:", mixto);
console.log("Constantes (readonly):", constantes);


// ----------------------------------------------------------------------------
// 4. TUPLAS
// Arrays con longitud y tipos fijos por posicion
// ----------------------------------------------------------------------------

let coordenada: [number, number] = [19.4326, -99.1332];
let usuario: [string, number, boolean] = ["Ana", 25, true];
let etiquetada: [nombre: string, edad: number] = ["Carlos", 30];

console.log("\n=== Tuplas ===");
console.log(`Coordenada: lat=${coordenada[0]}, lng=${coordenada[1]}`);
console.log(`Usuario: ${usuario[0]}, ${usuario[1]} anios, activo: ${usuario[2]}`);


// ----------------------------------------------------------------------------
// 5. ENUMS
// Conjuntos de constantes con nombre
// ----------------------------------------------------------------------------

// Enum numerico (auto-incremental desde 0)
enum Direccion {
  Norte,    // 0
  Sur,      // 1
  Este,     // 2
  Oeste     // 3
}

// Enum string (cada valor es explicito)
enum EstadoPedido {
  Pendiente = "PENDIENTE",
  Enviado = "ENVIADO",
  Entregado = "ENTREGADO",
  Cancelado = "CANCELADO"
}

// Uso de enums
let rumbo: Direccion = Direccion.Norte;
let pedido: EstadoPedido = EstadoPedido.Enviado;

console.log("\n=== Enums ===");
console.log(`Direccion Norte = ${rumbo}`);
console.log(`Nombre de Direccion[0] = ${Direccion[0]}`);
console.log(`Estado del pedido: ${pedido}`);


// ----------------------------------------------------------------------------
// 6. ANY — Desactiva la verificacion (usar con precaucion)
// ----------------------------------------------------------------------------

let flexible: any = "soy string";
flexible = 42;            // OK: any permite reasignar a cualquier tipo
flexible = { x: 1 };     // OK
// flexible.metodoInventado(); // No da error en compilacion, pero falla en ejecucion

console.log("\n=== any ===");
console.log("Flexible ahora es:", flexible);


// ----------------------------------------------------------------------------
// 7. UNKNOWN — Tipo seguro para valores desconocidos
// ----------------------------------------------------------------------------

let dato: unknown = "Hola TypeScript";

// dato.toUpperCase();  // ERROR: Object is of type 'unknown'

// Hay que verificar el tipo antes de usar
if (typeof dato === "string") {
  console.log("\n=== unknown ===");
  console.log("Dato en mayusculas:", dato.toUpperCase());
}

// Otro ejemplo con verificacion
function procesarDato(valor: unknown): string {
  if (typeof valor === "string") return `String: ${valor}`;
  if (typeof valor === "number") return `Number: ${valor.toFixed(2)}`;
  if (typeof valor === "boolean") return `Boolean: ${valor}`;
  return "Tipo no reconocido";
}

console.log(procesarDato("test"));
console.log(procesarDato(3.14159));
console.log(procesarDato(true));


// ----------------------------------------------------------------------------
// 8. VOID — Funciones sin retorno significativo
// ----------------------------------------------------------------------------

function saludar(nombre: string): void {
  console.log(`\n=== void ===`);
  console.log(`Hola, ${nombre}!`);
  // No tiene return (o return sin valor)
}

saludar("Mundo");


// ----------------------------------------------------------------------------
// 9. NEVER — Funciones que NUNCA retornan
// ----------------------------------------------------------------------------

function lanzarError(mensaje: string): never {
  throw new Error(mensaje);
}

// Uso de never para exhaustividad en switch
type Semaforo = "rojo" | "amarillo" | "verde";

function accion(color: Semaforo): string {
  switch (color) {
    case "rojo":     return "Detenerse";
    case "amarillo": return "Precaucion";
    case "verde":    return "Avanzar";
    default:
      // Si alguien agrega un color nuevo y no lo maneja,
      // TypeScript dara un error aqui
      const _exhaustivo: never = color;
      return _exhaustivo;
  }
}

console.log("\n=== never (exhaustividad) ===");
console.log(`Rojo: ${accion("rojo")}`);
console.log(`Verde: ${accion("verde")}`);


// ----------------------------------------------------------------------------
// 10. ASERCIONES DE TIPO
// Le dices a TypeScript "yo se que este valor es de este tipo"
// ----------------------------------------------------------------------------

let valorDesconocido: unknown = "Hola Mundo";

// Forma 1: as
let longitud1: number = (valorDesconocido as string).length;

// Forma 2: angulos (no funciona en archivos .tsx)
let longitud2: number = (<string>valorDesconocido).length;

console.log("\n=== Aserciones ===");
console.log(`Longitud con 'as': ${longitud1}`);
console.log(`Longitud con '<>': ${longitud2}`);


// ----------------------------------------------------------------------------
// 11. TYPE NARROWING — Reducir tipos con verificaciones
// ----------------------------------------------------------------------------

function describir(valor: string | number | boolean): string {
  if (typeof valor === "string") {
    // Aqui TypeScript sabe que es string
    return `Texto de ${valor.length} caracteres: "${valor}"`;
  }
  if (typeof valor === "number") {
    // Aqui TypeScript sabe que es number
    return `Numero: ${valor.toFixed(2)}`;
  }
  // Aqui TypeScript sabe que es boolean
  return `Booleano: ${valor ? "verdadero" : "falso"}`;
}

console.log("\n=== Type Narrowing ===");
console.log(describir("TypeScript"));
console.log(describir(42.567));
console.log(describir(true));

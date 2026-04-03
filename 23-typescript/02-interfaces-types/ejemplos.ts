// ============================================================================
// 02 — INTERFACES Y TYPE ALIASES
// ============================================================================
// Compilar: tsc ejemplos.ts
// Ejecutar: node ejemplos.js
// ============================================================================


// ----------------------------------------------------------------------------
// 1. INTERFACES BASICAS
// Definen la forma de un objeto
// ----------------------------------------------------------------------------

interface Usuario {
  nombre: string;
  edad: number;
  email: string;
}

const usuario1: Usuario = {
  nombre: "Maria Garcia",
  edad: 28,
  email: "maria@ejemplo.com"
};

console.log("=== Interface Basica ===");
console.log(usuario1);


// ----------------------------------------------------------------------------
// 2. PROPIEDADES OPCIONALES Y READONLY
// ----------------------------------------------------------------------------

interface Producto {
  readonly id: number;       // no se puede cambiar despues de crear
  nombre: string;
  precio: number;
  descripcion?: string;      // puede no existir
  descuento?: number;        // puede no existir
}

const laptop: Producto = {
  id: 1,
  nombre: "Laptop Pro",
  precio: 25000,
  descripcion: "Laptop de alto rendimiento"
  // descuento omitido — es opcional
};

// laptop.id = 2;  // ERROR: Cannot assign to 'id' because it is read-only

console.log("\n=== Opcionales y Readonly ===");
console.log(laptop);
console.log(`Descuento: ${laptop.descuento ?? "Sin descuento"}`);


// ----------------------------------------------------------------------------
// 3. TYPE ALIASES
// Crean nombres para cualquier tipo
// ----------------------------------------------------------------------------

type Punto = { x: number; y: number };
type ID = string | number;
type Color = "rojo" | "verde" | "azul";
type Coordenadas = [number, number];

const punto: Punto = { x: 10, y: 20 };
const miId: ID = "abc-123";
const color: Color = "verde";
const coords: Coordenadas = [19.43, -99.13];

console.log("\n=== Type Aliases ===");
console.log("Punto:", punto);
console.log("ID:", miId);
console.log("Color:", color);
console.log("Coordenadas:", coords);


// ----------------------------------------------------------------------------
// 4. EXTENDER INTERFACES
// Las interfaces pueden heredar de otras
// ----------------------------------------------------------------------------

interface Animal {
  nombre: string;
  edad: number;
}

interface Mascota extends Animal {
  duenio: string;
  vacunado: boolean;
}

interface Perro extends Mascota {
  raza: string;
}

const miPerro: Perro = {
  nombre: "Max",
  edad: 3,
  duenio: "Carlos",
  vacunado: true,
  raza: "Labrador"
};

console.log("\n=== Extender Interfaces ===");
console.log(miPerro);


// ----------------------------------------------------------------------------
// 5. INTERSECCION DE TYPES (&)
// Combina multiples types en uno
// ----------------------------------------------------------------------------

type ConNombre = { nombre: string };
type ConEdad = { edad: number };
type ConEmail = { email: string };

type PersonaCompleta = ConNombre & ConEdad & ConEmail;

const persona: PersonaCompleta = {
  nombre: "Ana Lopez",
  edad: 32,
  email: "ana@ejemplo.com"
};

console.log("\n=== Interseccion de Types ===");
console.log(persona);


// ----------------------------------------------------------------------------
// 6. UNION TYPES (|)
// Un valor puede ser de uno u otro tipo
// ----------------------------------------------------------------------------

type Resultado = string | number;
type Estado = "pendiente" | "procesando" | "completado" | "error";

function formatearId(id: string | number): string {
  if (typeof id === "string") {
    return `ID-${id.toUpperCase()}`;
  }
  return `ID-${id.toString().padStart(5, "0")}`;
}

console.log("\n=== Union Types ===");
console.log(formatearId("abc"));     // ID-ABC
console.log(formatearId(42));        // ID-00042

// Tipos literales como union
let estado: Estado = "pendiente";
console.log(`Estado: ${estado}`);
estado = "completado";
console.log(`Estado: ${estado}`);
// estado = "desconocido";  // ERROR: no es un valor valido


// ----------------------------------------------------------------------------
// 7. UNION DISCRIMINADA
// Patron poderoso para manejar diferentes variantes de un tipo
// ----------------------------------------------------------------------------

type Exito = {
  tipo: "exito";
  datos: string[];
  totalResultados: number;
};

type ErrorRespuesta = {
  tipo: "error";
  codigo: number;
  mensaje: string;
};

type Cargando = {
  tipo: "cargando";
  progreso: number;
};

type RespuestaAPI = Exito | ErrorRespuesta | Cargando;

function manejarRespuesta(respuesta: RespuestaAPI): string {
  switch (respuesta.tipo) {
    case "exito":
      return `OK: ${respuesta.totalResultados} resultados encontrados`;
    case "error":
      return `Error ${respuesta.codigo}: ${respuesta.mensaje}`;
    case "cargando":
      return `Cargando... ${respuesta.progreso}%`;
  }
}

console.log("\n=== Union Discriminada ===");
console.log(manejarRespuesta({ tipo: "exito", datos: ["a", "b"], totalResultados: 2 }));
console.log(manejarRespuesta({ tipo: "error", codigo: 404, mensaje: "No encontrado" }));
console.log(manejarRespuesta({ tipo: "cargando", progreso: 75 }));


// ----------------------------------------------------------------------------
// 8. INDEX SIGNATURES
// Objetos con claves dinamicas
// ----------------------------------------------------------------------------

interface Diccionario {
  [palabra: string]: string;
}

const traducciones: Diccionario = {
  hola: "hello",
  mundo: "world",
  casa: "house"
};

// Agregar claves dinamicamente
traducciones["gato"] = "cat";

console.log("\n=== Index Signatures ===");
console.log(traducciones);

// Combinar propiedades fijas con index signature
interface ConfigApp {
  nombre: string;                    // obligatorio
  version: string;                   // obligatorio
  [opcion: string]: string;          // cualquier otra clave string
}

const config: ConfigApp = {
  nombre: "MiApp",
  version: "1.0.0",
  tema: "oscuro",
  idioma: "es"
};

console.log("Config:", config);


// ----------------------------------------------------------------------------
// 9. DECLARATION MERGING (solo interfaces)
// Declarar la misma interface dos veces las fusiona
// ----------------------------------------------------------------------------

interface Ventana {
  titulo: string;
  ancho: number;
}

interface Ventana {
  alto: number;
  visible: boolean;
}

// Ahora Ventana tiene las 4 propiedades
const ventana: Ventana = {
  titulo: "Principal",
  ancho: 800,
  alto: 600,
  visible: true
};

console.log("\n=== Declaration Merging ===");
console.log(ventana);


// ----------------------------------------------------------------------------
// 10. EJEMPLO PRACTICO: Sistema de formas geometricas
// Combina interfaces, types, unions y readonly
// ----------------------------------------------------------------------------

interface FormaBase {
  readonly tipo: string;
  color: Color;
}

interface Circulo extends FormaBase {
  readonly tipo: "circulo";
  radio: number;
}

interface Rectangulo extends FormaBase {
  readonly tipo: "rectangulo";
  ancho: number;
  alto: number;
}

interface Triangulo extends FormaBase {
  readonly tipo: "triangulo";
  base: number;
  altura: number;
}

type Forma = Circulo | Rectangulo | Triangulo;

function calcularArea(forma: Forma): number {
  switch (forma.tipo) {
    case "circulo":
      return Math.PI * forma.radio ** 2;
    case "rectangulo":
      return forma.ancho * forma.alto;
    case "triangulo":
      return (forma.base * forma.altura) / 2;
  }
}

function describirForma(forma: Forma): string {
  const area = calcularArea(forma).toFixed(2);
  return `${forma.tipo} (${forma.color}) — area: ${area}`;
}

const formas: Forma[] = [
  { tipo: "circulo", color: "rojo", radio: 5 },
  { tipo: "rectangulo", color: "azul", ancho: 10, alto: 4 },
  { tipo: "triangulo", color: "verde", base: 6, altura: 8 }
];

console.log("\n=== Ejemplo Practico: Formas ===");
formas.forEach(f => console.log(describirForma(f)));

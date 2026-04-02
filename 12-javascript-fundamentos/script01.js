// =============================================================================
// MODULO 12 - JAVASCRIPT FUNDAMENTOS: FUNCIONES
// =============================================================================
//
// NIVEL: Basico-Intermedio
// TEMA: Funciones tradicionales, funciones flecha (arrow), funciones anonimas
//
// CONCEPTOS CLAVE DE ESTE ARCHIVO:
// ---------------------------------
// En JavaScript existen TRES formas principales de declarar funciones.
// Todas hacen lo mismo, pero tienen diferencias sutiles e importantes:
//
// 1. FUNCION TRADICIONAL (Function Declaration):
//    function nombre(parametros) { ... }
//    - Se puede llamar ANTES de declararla (hoisting).
//    - Tiene su propio contexto 'this'.
//    - Es la forma mas antigua y compatible.
//
// 2. FUNCION FLECHA (Arrow Function) - ES6/2015:
//    const nombre = (parametros) => { ... }
//    - NO tiene hoisting (debe declararse antes de usarse).
//    - NO tiene su propio 'this' (hereda el del contexto padre).
//    - Sintaxis mas corta y moderna.
//    - Si tiene UNA sola expresion, se puede omitir {} y return:
//      const doble = x => x * 2
//
// 3. FUNCION ANONIMA (Function Expression):
//    const nombre = function(parametros) { ... }
//    - Similar a la flecha pero con sintaxis clasica.
//    - NO tiene hoisting.
//    - Tiene su propio 'this'.
//    - Util para callbacks y funciones que se pasan como argumento.
//
// HOISTING (ELEVACION):
// ---------------------
// JavaScript "eleva" las declaraciones de funciones tradicionales al inicio
// del archivo. Por eso se pueden llamar antes de donde estan escritas.
// Las funciones flecha y anonimas NO se elevan porque se asignan a
// variables (const/let), y las variables no se elevan de la misma forma.
//
// Ejemplo de hoisting:
//   saludar();  // Funciona! -> "Hola"
//   function saludar() { console.log("Hola"); }
//
//   despedir();  // ERROR! -> Cannot access 'despedir' before initialization
//   const despedir = () => { console.log("Adios"); }
//
// COMPARACION CON PYTHON (para quienes vienen del modulo 11):
// -----------------------------------------------------------
// Python:  def power_(base, exponent):     JS: function power_(base, exponent) { }
// Python:  potencia = lambda b, e: b**e    JS: const potencia = (b, e) => b**e
// Python no tiene funcion anonima con function, pero si tiene lambda.
// En Python NO existe hoisting; todo debe definirse antes de usarse.
//
// NOTA: Python tiene ** para potencia (2**3 = 8).
//       JavaScript NO tiene **, se usa Math.pow(2, 3) o el operador ** (ES7+).
//       En este ejercicio se calcula manualmente con un bucle.
// =============================================================================

/* Natalia Edith Mejia Bautista */

// ---- FORMA 1: FUNCION TRADICIONAL (Function Declaration) ----
//
// 'function' es la palabra reservada para declarar funciones.
// 'power_' es el nombre de la funcion (se usa guion bajo para no confundir
// con Math.pow que es la funcion nativa de JavaScript para potencias).
//
// Parametros: base y exponent (se reciben por valor para tipos primitivos).
//
// LOGICA: Se inicializa ans con base, y se multiplica por base
// (exponent - 1) veces mas. Ejemplo: power_(2, 3) -> 2 * 2 * 2 = 8
//
// NOTA: El bucle empieza en i = 2 porque ans ya tiene el valor de base (1 vez).
// Si exponent = 1, el bucle no se ejecuta y retorna base directamente.
// CUIDADO: Esta implementacion no maneja exponent = 0 (deberia retornar 1).
function power_(base, exponent){
    let ans = base
    for (let i = 2; i<= exponent; i++)
        ans *= base
    return ans
}

// ---- FORMA 2: FUNCION FLECHA (Arrow Function) ----
//
// Sintaxis: const nombre = (parametros) => { cuerpo }
//
// La flecha => es lo que le da el nombre. Se lee como "va a" o "produce".
// const potenciaFlecha = (base, exponent) => { ... }
// Se lee: "potenciaFlecha recibe base y exponent, y produce..."
//
// Se asigna a una constante (const) porque la referencia a la funcion
// no deberia cambiar. Si usaramos let, alguien podria reasignar:
//   potenciaFlecha = "hola"  // Esto seria un bug dificil de encontrar.
// Con const, esto lanza un error y nos protege.
//
// CUANDO USAR FUNCIONES FLECHA:
// - Callbacks cortos: array.map(x => x * 2)
// - Cuando NO necesitas tu propio 'this'
// - Cuando quieres sintaxis concisa

//Convertir a función flecha
const potenciaFlecha = (base, exponent) => {
    let ans = base
    for (let i = 2; i <= exponent; i++)
        ans *= base
    return ans
}

// ---- FORMA 3: FUNCION ANONIMA (Function Expression) ----
//
// Se llama "anonima" porque la funcion en si NO tiene nombre.
// Lo que tiene nombre es la VARIABLE que la almacena (potenciaAnon).
//
// Sintaxis: const nombre = function(parametros) { cuerpo }
//
// La diferencia con la declaracion tradicional es sutil pero importante:
// - function power_(...)  -> Declaration: se eleva (hoisting)
// - const potenciaAnon = function(...) -> Expression: NO se eleva
//
// USO COMUN: Como callbacks (funciones que se pasan a otras funciones):
//   setTimeout(function() { console.log("Hola"); }, 1000);
//   boton.addEventListener("click", function() { ... });
//
// En la practica moderna, las funciones flecha han reemplazado en gran
// parte a las funciones anonimas para callbacks, pero es importante
// conocer ambas formas porque hay mucho codigo existente que las usa.

//Convertir a función anonima
const potenciaAnon = function(base, exponent){
    let ans = base
    for (let i = 2; i <= exponent; i++)
        ans *= base
    return ans
}

// ---- USO DE LAS TRES FUNCIONES ----
//
// Las tres producen el mismo resultado: 2^3 = 8
// Esto demuestra que las tres formas son funcionalmente equivalentes
// para este caso de uso.
//
// console.log() puede recibir multiples argumentos separados por coma.
// El primer argumento es un string descriptivo, el segundo es el resultado.
// En la consola se mostraran separados por un espacio.

//uTILIZAR LA FUNCIÓN
console.log("Funcion", power_(2, 3))
console.log("Funcion Flecha", potenciaFlecha(2, 3))
console.log("Funcion Anonima", potenciaAnon(2, 3))

// =============================================================================
// RESUMEN DE DIFERENCIAS:
//
// | Caracteristica          | Tradicional | Flecha     | Anonima    |
// |------------------------|-------------|------------|------------|
// | Hoisting               | SI          | NO         | NO         |
// | Propio 'this'          | SI          | NO         | SI         |
// | Puede ser constructor  | SI          | NO         | SI         |
// | Sintaxis corta         | NO          | SI         | NO         |
// | Uso moderno preferido  | Metodos     | Callbacks  | Legacy     |
//
// EJERCICIOS SUGERIDOS:
// 1. Reescribe potenciaFlecha en una sola linea (sin llaves ni return).
//    Pista: solo funciona si el cuerpo es UNA sola expresion.
// 2. Intenta llamar a potenciaFlecha ANTES de su declaracion. Que pasa?
// 3. Crea una funcion flecha que reciba un arreglo y retorne la suma.
// 4. Agrega manejo del caso exponent = 0 (deberia retornar 1).
// =============================================================================

// =============================================================================
// MODULO 12 - JAVASCRIPT FUNDAMENTOS: BUCLES Y SALIDA POR CONSOLA
// =============================================================================
//
// NIVEL: Basico
// TEMA: Bucles (for, while), concatenacion de strings, template literals
//
// CONCEPTOS CLAVE DE ESTE ARCHIVO:
// ---------------------------------
// 1. BUCLE FOR: Se usa cuando sabemos cuantas veces queremos repetir algo.
//    Sintaxis: for (inicializacion; condicion; incremento) { ... }
//    - Inicializacion: se ejecuta UNA sola vez al inicio (ej: let i = 1)
//    - Condicion: se evalua ANTES de cada iteracion (ej: i <= 10)
//    - Incremento: se ejecuta DESPUES de cada iteracion (ej: i++)
//
// 2. BUCLE WHILE: Se usa cuando NO sabemos cuantas veces repetir, solo la condicion.
//    Sintaxis: while (condicion) { ... }
//    CUIDADO: Si la condicion nunca se vuelve falsa, tendremos un bucle infinito.
//
// 3. TEMPLATE LITERALS (backticks): Las comillas invertidas `` permiten
//    insertar variables dentro de un string usando ${variable}.
//    Es mucho mas legible que concatenar con +.
//    Ejemplo: `Hola ${nombre}` vs "Hola " + nombre
//
// 4. console.log(): Es la forma principal de depurar en JavaScript.
//    Imprime mensajes en la consola del navegador (F12) o en la terminal de Node.js.
//
// 5. DECLARACION DE VARIABLES:
//    - const: valor que NO cambia (constante). Usar siempre que sea posible.
//    - let: valor que SI puede cambiar. Tiene alcance de bloque {}.
//    - var: la forma antigua. Tiene alcance de funcion, NO de bloque.
//      RECOMENDACION: Evitar var, usar const por defecto y let cuando necesites reasignar.
//
// COMPARACION CON PYTHON (para quienes vienen del modulo 11):
// -----------------------------------------------------------
// Python:  for i in range(1, 11):           JS: for (let i = 1; i <= 10; i++)
// Python:  while j <= maxim:                JS: while (j <= maxim)
// Python:  print(f"8 x {i} = {8*i}")       JS: console.log(`8 x ${i} = ${8*i}`)
// Python:  asteriscos += '*'                JS: asteriscos += '*'  (igual!)
//
// NOTA: En Python los bloques se definen por indentacion.
//       En JavaScript los bloques se definen por llaves {}.
// =============================================================================

/* Natalia Edith Mejia Bautista
Ejercicio 1: Utiliza un bucle for para imprimir en consola la tabla de multiplicar del 8:
*/

// ---- EJERCICIO 1: TABLA DE MULTIPLICAR CON BUCLE FOR ----
//
// Se declara 'tabla' como const porque su valor nunca cambiara.
// Si intentaramos hacer tabla = 9, JavaScript lanzaria un error:
// TypeError: Assignment to constant variable.
const tabla = 8;

// console.log() con template literal (backticks ``)
// ${tabla} se reemplaza por el valor de la variable 'tabla' (8).
// Esto es equivalente a: console.log("Tabla de multiplicar del " + tabla)
// pero mucho mas legible, especialmente con multiples variables.
console.log(`Tabla de multiplicar del ${tabla}`);

// BUCLE FOR:
// - let i = 1       -> Se inicializa i en 1 (usamos let porque i cambiara)
// - i <= 10         -> Continua mientras i sea menor o igual a 10
// - (sin incremento en la declaracion del for, se hace dentro del cuerpo)
//
// NOTA IMPORTANTE: Este for NO tiene la tercera parte (incremento) en su declaracion.
// Normalmente se escribe: for (let i = 1; i <= 10; i++)
// Aqui el i++ esta dentro del cuerpo del bucle, lo cual funciona igual
// pero es una practica menos comun. Ambas formas son validas.
//
// OPERADOR *: Multiplicacion. ${tabla * i} calcula 8 * i directamente
// dentro del template literal. Se pueden poner expresiones completas dentro de ${}.
for (let i = 1; i <= 10;) {
    console.log(`${tabla} x ${i} = ${tabla * i}`);
    i++
}

// ---- EJERCICIO 2: TRIANGULO DE ASTERISCOS CON BUCLE WHILE ----
//
// Este ejercicio demuestra:
// - Concatenacion de strings (asteriscos += '*')
// - Bucle while para repeticion condicional
// - Construccion progresiva de un patron visual

/*
Ejercicio 2: Elabora un script que "pinte" un triángulo como el de la imagen, haciendo uso del bucle while */

// 'let' porque estas variables cambiaran de valor durante la ejecucion.
// Si usaramos 'const', obtendriamos un error al intentar reasignar.
let j = 1 // incremento

// Se inicializa como string vacio ''. En cada iteracion se le agrega un '*'.
// Asi se construye el triangulo linea por linea:
// Iteracion 1: '*'
// Iteracion 2: '**'
// Iteracion 3: '***'
// ... y asi sucesivamente hasta 7 asteriscos.
//
// OPERADOR +=: Es un atajo para asteriscos = asteriscos + '*'
// Funciona tanto con numeros (suma) como con strings (concatenacion).
let asteriscos = '' // variable de los asteriscos

// 'maxim' podria ser const ya que no se reasigna, pero let tambien funciona.
// BUENA PRACTICA: Usar const aqui seria mas apropiado -> const maxim = 7
let maxim = 7

console.log('Triángulo de asteriscos')

// BUCLE WHILE:
// Se ejecuta mientras j sea menor o igual a maxim (7).
// En cada iteracion:
// 1. Se concatena un '*' a la cadena 'asteriscos'
// 2. Se imprime la cadena actual
// 3. Se incrementa j en 1
//
// CUIDADO: Si olvidaramos j++, el bucle seria INFINITO porque
// j siempre seria 1 y la condicion 1 <= 7 siempre seria verdadera.
// Esto congelaria el navegador o la terminal.
while (j <= maxim) {
    asteriscos += '*'
    console.log(asteriscos)
    j++
}

// =============================================================================
// PARA EJECUTAR ESTE ARCHIVO:
// - En terminal: node script00.js
// - En navegador: incluir con <script src="script00.js"></script> y ver la consola (F12)
//
// EJERCICIOS SUGERIDOS:
// 1. Modifica el primer ejercicio para que el usuario elija la tabla (usa prompt())
// 2. Modifica el triangulo para que sea invertido (de 7 asteriscos a 1)
// 3. Crea un triangulo centrado (con espacios a la izquierda)
// 4. Intenta reescribir el bucle while como un bucle for y viceversa
// =============================================================================

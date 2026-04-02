// =============================================================================
// MODULO 12 - JAVASCRIPT FUNDAMENTOS: PROGRAMACION ORIENTADA A OBJETOS (POO)
// =============================================================================
//
// NIVEL: Intermedio
// TEMA: Clases, herencia, metodos, instanciacion con 'new'
//
// CONCEPTOS CLAVE DE ESTE ARCHIVO:
// ---------------------------------
//
// 1. CLASES EN JAVASCRIPT (ES6/2015):
//    Las clases son "plantillas" para crear objetos. Definen que propiedades
//    y metodos tendran los objetos creados a partir de ellas.
//
//    Sintaxis:
//    class NombreClase {
//        constructor(parametros) { ... }   // Se ejecuta al crear el objeto
//        metodo() { ... }                  // Metodo de la clase
//    }
//
//    NOTA TECNICA: Las clases en JavaScript son "azucar sintactico" (syntactic sugar)
//    sobre el sistema de prototipos. Internamente, JavaScript NO tiene clases reales
//    como Java o C++. Es un lenguaje basado en PROTOTIPOS. La palabra 'class'
//    simplemente hace mas facil escribir el patron de prototipos.
//
// 2. HERENCIA CON 'extends':
//    Una clase hija puede heredar todos los metodos y propiedades de una clase padre.
//    class Hija extends Padre { ... }
//    - La clase hija tiene acceso a TODO lo que tiene la clase padre.
//    - La clase hija puede agregar sus propios metodos adicionales.
//    - La clase hija puede SOBREESCRIBIR (override) metodos del padre.
//    - Si la hija define un constructor, DEBE llamar a super() primero.
//
// 3. INSTANCIACION CON 'new':
//    const objeto = new NombreClase(argumentos);
//    'new' hace tres cosas:
//    a) Crea un objeto vacio {}
//    b) Ejecuta el constructor con ese objeto como 'this'
//    c) Retorna el objeto creado
//
// 4. METODOS:
//    Son funciones definidas dentro de una clase. Se llaman con:
//    objeto.metodo(argumentos)
//    No necesitan la palabra 'function' dentro de la clase.
//
// COMPARACION CON PYTHON (para quienes vienen del modulo 11):
// -----------------------------------------------------------
// Python:                              JavaScript:
// class Calculadora:                   class Calculadora {
//     def sumar(self, a, b):               sumar(a, b) {
//         return a + b                         return a + b
//                                          }
// class CalcAvanzada(Calculadora):     class CalcAvanzada extends Calculadora {
//     def multiplicar(self, a, b):         multiplicar(a, b) {
//         return a * b                         return a * b
//                                          }
// calc = Calculadora()                 const calc = new Calculadora()
//
// DIFERENCIAS IMPORTANTES:
// - Python usa 'self' como primer parametro; JS usa 'this' implicitamente.
// - Python hereda con parentesis: class Hija(Padre)
//   JS hereda con extends: class Hija extends Padre
// - Python NO requiere 'new'; JS SI lo requiere.
// =============================================================================

//Natalia Edith Mejia Bautista

// ---- EJERCICIO 1: CLASE BASE - CALCULADORA ----
//
// Esta clase NO tiene constructor. Cuando no defines un constructor,
// JavaScript crea uno vacio automaticamente: constructor() {}
// Esto significa que se puede instanciar sin argumentos: new Calculadora()
//
// La clase define dos metodos: sumar y restar.
// Cada metodo recibe dos parametros (a, b) y retorna el resultado.
//
// NOTA: Los metodos dentro de una clase no usan la palabra 'function'.
// Esto es una simplificacion de la sintaxis de clases ES6.
// Antes de ES6, se hacia asi:
//   Calculadora.prototype.sumar = function(a, b) { return a + b; }

/* Escribe el código JS que implemente una clase Calculadora con los siguientes métodos:
● sumar
● restar */
class Calculadora {
    // Metodo sumar: recibe dos numeros y retorna su suma.
    // En JavaScript, + funciona tanto para numeros como para strings:
    //   5 + 5 = 10  (suma numerica)
    //   "5" + "5" = "55"  (concatenacion de strings!)
    // CUIDADO: Si a o b fueran strings, el resultado seria inesperado.
    sumar(a, b) {
        return a + b
    }
    // Metodo restar: recibe dos numeros y retorna la diferencia.
    restar(a, b) {
        return a - b
    }
}


// ---- EJERCICIO 2: CLASE HIJA - CALCULADORA AVANZADA CON HERENCIA ----
//
// 'extends' es la palabra clave para herencia en JavaScript.
// CalcAvanzada hereda TODOS los metodos de Calculadora (sumar, restar)
// y agrega dos nuevos (multiplicar, dividir).
//
// CADENA DE PROTOTIPOS (Prototype Chain):
// Cuando llamas calcAvanzada.sumar(5, 5), JavaScript busca:
// 1. Tiene CalcAvanzada un metodo 'sumar'? NO
// 2. Tiene su padre (Calculadora) un metodo 'sumar'? SI -> lo ejecuta
// Esta busqueda hacia arriba en la cadena se llama "prototype chain".
//
// NOTA: CalcAvanzada tampoco tiene constructor, asi que hereda el
// constructor vacio de Calculadora automaticamente.

/*2. Escribe el código JS que implemente una clase CalcAvanzada con los métodos "multiplicar" y
"dividir", además de los métodos de la clase Calculadora, utilizando herencia. */

class CalcAvanzada extends Calculadora {
    multiplicar(a, b) {
        return a * b
    }
    // CUIDADO con dividir: Si b es 0, retorna Infinity (no lanza error).
    // En Python, dividir por 0 lanza ZeroDivisionError.
    // En JavaScript, 5 / 0 = Infinity, -5 / 0 = -Infinity, 0 / 0 = NaN.
    // Una buena practica seria validar: if (b === 0) throw new Error("...")
    dividir(a, b) {
        return a / b
    }
}

// ---- USO DE LAS CLASES ----
//
// 'new' es OBLIGATORIO para crear instancias de clases.
// Sin 'new', obtenemos: TypeError: Cannot call a class as a function
//
// const vs let: Usamos const porque la referencia al objeto no cambiara.
// NOTA: Aunque sea const, las PROPIEDADES del objeto SI pueden cambiar.
// const impide reasignar la variable, no modificar el contenido.
//   const calc = new Calculadora();
//   calc = new Calculadora();  // ERROR: reasignacion prohibida
//   calc.nuevoMetodo = () => {};  // OK: se puede modificar el objeto

//uso de las clases
const calc = new Calculadora()
const calcAvanzada = new CalcAvanzada()

// calc solo puede usar sumar y restar
console.log(calc.sumar(5, 5)) //10
console.log(calc.restar(5, 5)) //0

// calcAvanzada puede usar sumar (heredado) Y multiplicar (propio)
// Esto demuestra la herencia: sumar viene de Calculadora, multiplicar es de CalcAvanzada
console.log(calcAvanzada.sumar(5, 5)) //10
console.log(calcAvanzada.multiplicar(5, 5)) //25

// =============================================================================
// CONCEPTOS AVANZADOS RELACIONADOS:
//
// INSTANCEOF: Verifica si un objeto es instancia de una clase.
//   calc instanceof Calculadora           // true
//   calcAvanzada instanceof Calculadora   // true (por herencia!)
//   calcAvanzada instanceof CalcAvanzada  // true
//   calc instanceof CalcAvanzada          // false (el padre no es instancia del hijo)
//
// SUPER: Si CalcAvanzada tuviera constructor, deberia llamar a super():
//   class CalcAvanzada extends Calculadora {
//       constructor(precision) {
//           super();  // OBLIGATORIO: llama al constructor del padre
//           this.precision = precision;
//       }
//   }
//
// GETTERS Y SETTERS:
//   class Temperatura {
//       constructor(celsius) { this._celsius = celsius; }
//       get fahrenheit() { return this._celsius * 9/5 + 32; }
//       set fahrenheit(f) { this._celsius = (f - 32) * 5/9; }
//   }
//   const t = new Temperatura(0);
//   console.log(t.fahrenheit);  // 32 (se llama como propiedad, no como metodo)
//
// METODOS ESTATICOS:
//   class MathUtil {
//       static doble(x) { return x * 2; }
//   }
//   MathUtil.doble(5);  // 10 (se llama en la clase, no en instancias)
//
// EJERCICIOS SUGERIDOS:
// 1. Agrega un metodo 'potencia(base, exp)' a CalcAvanzada.
// 2. Crea una clase CalcCientifica que herede de CalcAvanzada y
//    agregue metodos para raiz cuadrada y logaritmo.
// 3. Agrega validacion en dividir para evitar division por cero.
// 4. Agrega un constructor que reciba una precision (decimales).
// =============================================================================

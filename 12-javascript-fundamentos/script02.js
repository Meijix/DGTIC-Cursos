//Natalia Edith Mejia Bautista

/* Escribe el código JS que implemente una clase Calculadora con los siguientes métodos:
● sumar
● restar */
class Calculadora {
    sumar(a, b) {
        return a + b
    }
    restar(a, b) {
        return a - b
    }
}


/*2. Escribe el código JS que implemente una clase CalcAvanzada con los métodos “multiplicar” y
“dividir”, además de los métodos de la clase Calculadora, utilizando herencia. */

class CalcAvanzada extends Calculadora {
    multiplicar(a, b) {
        return a * b
    }
    dividir(a, b) {
        return a / b
    }
}

//uso de las clases
const calc = new Calculadora()
const calcAvanzada = new CalcAvanzada()
console.log(calc.sumar(5, 5)) //10
console.log(calc.restar(5, 5)) //0
console.log(calcAvanzada.sumar(5, 5)) //10
console.log(calcAvanzada.multiplicar(5, 5)) //25

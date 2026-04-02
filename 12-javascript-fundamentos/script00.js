/* Natalia Edith Mejia Bautista
Ejercicio 1: Utiliza un bucle for para imprimir en consola la tabla de multiplicar del 8:
*/
const tabla = 8;
console.log(`Tabla de multiplicar del ${tabla}`);
for (let i = 1; i <= 10;) {
    console.log(`${tabla} x ${i} = ${tabla * i}`);
    i++
}
/* 
Ejercicio 2: Elabora un script que “pinte” un triángulo como el de la imagen, haciendo uso del bucle while */
let j = 1 // incremento
let asteriscos = '' // variable de los asteriscos
let maxim = 7

console.log('Triángulo de asteriscos')
while (j <= maxim) {
    asteriscos += '*'
    console.log(asteriscos)
    j++
}
/* Natalia Edith Mejia Bautista */

function power_(base, exponent){
    let ans = base
    for (let i = 2; i<= exponent; i++)
        ans *= base
    return ans
}

//Convertir a función flecha
const potenciaFlecha = (base, exponent) => {
    let ans = base
    for (let i = 2; i <= exponent; i++)
        ans *= base
    return ans
}

//Convertir a función anonima
const potenciaAnon = function(base, exponent){
    let ans = base
    for (let i = 2; i <= exponent; i++)
        ans *= base
    return ans
}

//uTILIZAR LA FUNCIÓN
console.log("Funcion", power_(2, 3))
console.log("Funcion Flecha", potenciaFlecha(2, 3))
console.log("Funcion Anonima", potenciaAnon(2, 3))
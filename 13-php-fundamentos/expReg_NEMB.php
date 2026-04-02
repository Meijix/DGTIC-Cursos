<!-- Expresiones Regulares con PHP
INSTRUCCIONES
Realizar una expresión regular que detecte emails correctos.
Realizar una expresión regular que detecte Curps Correctos
es decir que permita usar únicamente estos caracteres: ABCD123456EFGHIJ78.
Realizar una expresión regular que detecte palabras de longitud mayor a 50 formadas solo por letras.
Crea una función para escapar los símbolos especiales.
Crear una expresión regular para detectar números decimales. -->
<?php
// Expresion regular para emails
$email = "      ";
$expRegEmail = "/^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/";
if (preg_match($expRegEmail, $email)) {
    echo "El email es correcto";
} else {
    echo "El email es incorrecto";
}
echo "<br>";
// Expresion regular para Curps
$curp = "ABCD123456EFGHIJ78";
$expRegCurp = "/^[A-Z]{4}[0-9]{6}[A-Z]{6}[0-9]{2}$/";
if (preg_match($expRegCurp, $curp)) {
    echo "La curp es correcta";
} else {
    echo "La curp es incorrecta";
}
echo "<br>";
// Expresion regular para palabras de longitud mayor a 50 formadas solo por letras
$palabra = "    ";
$expRegPalabra = "/^[a-zA-Z]{50,}$/";
if (preg_match($expRegPalabra, $palabra)) {
    echo "La palabra es correcta";
} else {
    echo "La palabra es incorrecta";
}
echo "<br>";
// Funcion para escapar los simbolos especiales
function escaparSimbolos($cadena)
{
    $cadena = htmlspecialchars($cadena);
    return $cadena;
}
// Expresion regular para detectar numeros decimales
$numero = "123.456";
$expRegNumero = "/^[0-9]+(\.[0-9]+)?$/";
if (preg_match($expRegNumero, $numero)) {
    echo "El numero es correcto";
} else {    
    echo "El numero es incorrecto";
}                           
?>
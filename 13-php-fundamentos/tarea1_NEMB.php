<!-- 
Natalia Edith Mejia Bautista
Tarea 1. Script que genere una piramide dado un simbolo y un número de filas -->

<?php

function piramide($filas, $simbolo){
    //recorrer las filas
    for ($i = 1; $i <= $filas; $i++) {
        //repetir el simbolo para la fila
        $piramide = str_repeat($simbolo, $i);
        //centrar la piramide
        $pirCentrada = "<center>" . $piramide . "</center>";
        echo $pirCentrada . " ";
    }
}

function rombo($filas, $simbolo){
    //Parte superior del rombo
    for ($i = 1; $i <= $filas; $i++) {
        //repetir el simbolo para la fila
        $piramide = str_repeat($simbolo, $i);
        //centrar la piramide
        $pirCentrada = "<center>" . $piramide . "</center>";
        echo $pirCentrada;
    }
    //Parte inferior del rombo
    for ($i = $filas - 1; $i >= 1; $i--) {
        //repetir el simbolo para la fila
        $piramide = str_repeat($simbolo, $i);
        //centrar la piramide
        $pirCentrada = "<center>" . $piramide . "</center>";
        echo $pirCentrada;
    }
}

//llamada a las funciones
$filas = 10;
$simbolo = "🌟";
echo "<h2> Natalia Edith Mejia Bautista </h2>";
echo "<h1> Tarea 1 </h1>";
echo "<h3> Piramide </h3>";
piramide($filas, $simbolo);
echo "<h3> Rombo </h3>";
rombo($filas, $simbolo);


?>
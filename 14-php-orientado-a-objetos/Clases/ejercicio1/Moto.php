<?php

//crea aqui la clase Moto junto con dos propiedades public
class Moto{
    //declaracion de propiedades
    public $color;
    public $marca;
}

//crea aqui la instancia o el objeto de la clase Moto
$moto1 = new Moto;

// Verifica si la solicitud es POST
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Obtén los valores de los atributos desde la solicitud POST
    $moto1->color = $_POST['color'];
    $moto1->marca = $_POST['marca'];

    // Construye el mensaje concatenando los valores de los atributos
    $mensaje = "La moto es de color " . $moto1->color . " y de marca " . $moto1->marca . ".";
}
?>


<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Ejercicio Moto</title>
</head>
<body>
	<h1>Moto</h1>
	<p>Ingresa la siguiente informacion de la moto: </p>
    <form method="post" action="">
        <label for="color">Color:</label>
        <input type="text" id="color" name="color" required>
        <br>
        <label for="marca">Marca:</label>
        <input type="text" id="marca" name="marca" required>
        <br>
        <input type="submit" value="Enviar">
    </form>

    <?php
    // Muestra el mensaje si está definido en un inptu de solo lectura
    if (isset($mensaje)) {
        echo '<input type="text" value="' . ($mensaje) . '" readonly>';
    }
    ?>
</body>
</html>
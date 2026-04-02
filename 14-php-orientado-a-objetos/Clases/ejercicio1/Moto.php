<?php
/**
 * ==========================================================================
 * EJERCICIO 1 (PARTE 2): CLASE MOTO - FORMULARIO CON CLASE
 * ==========================================================================
 *
 * CONCEPTOS CLAVE:
 * ----------------
 *
 * 1. CLASE COMO CONTENEDOR DE DATOS:
 *    La clase Moto tiene dos propiedades publicas: $color y $marca.
 *    Funciona como un "contenedor inteligente" para agrupar datos
 *    relacionados. En vez de tener dos variables sueltas, las
 *    encapsulamos en un objeto.
 *
 *    SIN CLASE:
 *    $motoColor = "rojo";
 *    $motoMarca = "Honda";
 *
 *    CON CLASE:
 *    $moto1 = new Moto;
 *    $moto1->color = "rojo";
 *    $moto1->marca = "Honda";
 *
 *    Ventaja: Si tenemos 10 motos, con clases creamos 10 objetos.
 *    Sin clases, necesitariamos 20 variables (2 por moto).
 *
 * 2. $_SERVER["REQUEST_METHOD"]:
 *    Variable superglobal que contiene el metodo HTTP de la peticion.
 *    Puede ser "GET", "POST", "PUT", "DELETE", etc.
 *    Es otra forma de verificar si el formulario fue enviado por POST.
 *
 *    Alternativas equivalentes:
 *    - if ($_SERVER["REQUEST_METHOD"] == "POST")  <- este archivo usa esta
 *    - if (!empty($_POST))                         <- Carro.php usa esta
 *    - if (isset($_POST['campo']))                 <- otra forma comun
 *
 * 3. FORMULARIO action="" (VACIO):
 *    Cuando action="" esta vacio, el formulario se envia A SI MISMO.
 *    Es decir, Moto.php recibe los datos que Moto.php envia.
 *    El mismo archivo actua como formulario Y procesador.
 *
 * 4. MEZCLA PHP + HTML EN UN SOLO ARCHIVO:
 *    Este archivo demuestra el patron comun en PHP:
 *    - ARRIBA: logica PHP (procesar datos, crear objetos)
 *    - ABAJO: HTML (formulario y presentacion)
 *    El PHP se ejecuta primero, luego el HTML se envia al navegador.
 */

//crea aqui la clase Moto junto con dos propiedades public
// Definimos la clase Moto con la misma estructura basica que Carro
// Ambas clases tienen propiedades public, que es el nivel mas basico de OOP
class Moto{
    //declaracion de propiedades
    // public $color y public $marca permiten acceso directo desde fuera:
    // $moto1->color = "rojo";  // Esto funciona porque es public
    public $color;
    public $marca;
}

// INSTANCIACION: Creamos un objeto $moto1 de la clase Moto
// En este punto, ambas propiedades son null (no tienen valor asignado)
//crea aqui la instancia o el objeto de la clase Moto
$moto1 = new Moto;

// Verificamos si la peticion fue POST usando $_SERVER["REQUEST_METHOD"]
// Esta es una alternativa a !empty($_POST) que vimos en Carro.php
// Verifica si la solicitud es POST
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Obtén los valores de los atributos desde la solicitud POST
    // Asignamos los datos del formulario a las propiedades del objeto
    // El operador -> accede a la propiedad del objeto
    $moto1->color = $_POST['color'];
    $moto1->marca = $_POST['marca'];

    // Construye el mensaje concatenando los valores de los atributos
    // Usamos el operador punto (.) para concatenar multiples cadenas
    // $moto1->color accede al valor que acabamos de asignar arriba
    $mensaje = "La moto es de color " . $moto1->color . " y de marca " . $moto1->marca . ".";
}
?>

<!-- =====================================================================
     PARTE HTML - FORMULARIO Y PRESENTACION
     =====================================================================
     Todo lo que esta fuera de <?php ?> es HTML puro.
     El PHP de arriba ya se ejecuto cuando llegamos aqui.
-->
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Ejercicio Moto</title>
</head>
<body>
	<h1>Moto</h1>
	<p>Ingresa la siguiente informacion de la moto: </p>

    <!-- action="" (vacio) significa que el formulario se envia a SI MISMO (Moto.php) -->
    <!-- method="post" envia los datos en el cuerpo HTTP (no en la URL) -->
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
    // MEZCLA PHP DENTRO DE HTML:
    // Este bloque PHP se ejecuta en el servidor y genera HTML condicional.
    // isset($mensaje) verifica si la variable $mensaje fue creada arriba
    // (solo se crea si el formulario fue enviado por POST)
    // Muestra el mensaje si está definido en un inptu de solo lectura
    if (isset($mensaje)) {
        // readonly hace que el input no sea editable por el usuario
        echo '<input type="text" value="' . ($mensaje) . '" readonly>';
    }
    ?>
</body>
</html>

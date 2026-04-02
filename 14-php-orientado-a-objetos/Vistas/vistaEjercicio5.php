<?php
/**
 * ==========================================================================
 * VISTA DEL EJERCICIO 5: CONSTRUCTORES Y DESTRUCTORES
 * ==========================================================================
 *
 * CONCEPTOS CLAVE:
 * ----------------
 *
 * 1. CONSTRUCTOR Y DESTRUCTOR EN ACCION:
 *    Al incluir token.php:
 *    - Si hay POST: se crea el objeto token -> __construct() se ejecuta
 *    - Se llama a mostrar() para obtener el mensaje
 *    - Cuando PHP termina de ejecutar este archivo -> __destruct() se ejecuta
 *    - El destructor imprime "El token ha sido destruido" en la pagina
 *
 * 2. ORDEN DE APARICION EN LA PAGINA:
 *    a) El input readonly muestra $mensaje (resultado de mostrar())
 *    b) El formulario HTML se renderiza
 *    c) Al final, el destructor agrega "El token ha sido destruido"
 *
 *    Esto ocurre porque __destruct() se ejecuta al final del script,
 *    DESPUES de que todo el HTML ha sido procesado.
 *
 * 3. <?= $mensaje ?>:
 *    Si el formulario NO fue enviado, $mensaje = '' (string vacio).
 *    Si fue enviado, $mensaje contiene "Hola [nombre] este es tu token: [numero]".
 */

//comando de inclusion con la ruta de las clases
// Al incluir token.php:
// - Se define la clase token con __construct() y __destruct()
// - Si hay POST: se crea objeto, se genera token, y se guarda $mensaje
// - El destructor se ejecutara al final de ESTE archivo
include_once('../clases/ejercicio5/token.php');
?>
<!DOCTYPE html>
<html>
<head>

	<link rel="stylesheet" href="../css/bootstrap.min.css">
	<link rel="stylesheet" href="../css/bootstrap-grid.css">
	<script type="text/javascript" src="../js/bootstrap.min.js"></script>
	<script type="text/javascript" src="../js/jquery-3.4.1.min.js"></script>
	<title>
		Indice
	</title>
</head>
<body>

	<!-- Input readonly que muestra el mensaje del token -->
	<!-- Si no se envio el formulario: vacio -->
	<!-- Si se envio: "Hola Natalia este es tu token: 1847362950" -->
	<input class='form-control' type='text' value='<?=$mensaje?>' readonly>

	<div class="container" style="margin-top: 4em">

	<header> <h1>Recoge tu token</h1></header><br>

	<!-- Formulario para ingresar el nombre -->
	<form method="post">


					 <div class="form-group">
				 		<label for="CajaTexto1">Escribe tu nombre:</label>
						<input class="form-control" type="text" name="nombre" id="CajaTexto1">
					</div>


		<button class="btn btn-primary" type="submit" >enviar</button>
		<a class="btn btn-link offset-md-8 offset-lg-9 offset-6" href="../index.php">Regresar</a>
	</form>

	</div>

	<!--
	NOTA: Despues de este punto, cuando PHP termine de ejecutar el script,
	el destructor __destruct() de la clase token se ejecutara y mostrara
	"El token ha sido destruido" aqui al final de la pagina.
	-->

</body>
</html>

<?php
/**
 * ==========================================================================
 * VISTA DEL EJERCICIO 4: ATRIBUTOS CON ARREGLOS (RFC)
 * ==========================================================================
 *
 * CONCEPTOS CLAVE:
 * ----------------
 *
 * 1. FORMULARIO CON MULTIPLES CAMPOS:
 *    Este formulario recoge nombre, apellidos y fecha de nacimiento.
 *    Todos estos datos se envian como $_POST y se agrupan en un array
 *    asociativo en Rfc.php antes de pasarlos al objeto.
 *
 * 2. $mensaje:
 *    La variable $mensaje se crea en Rfc.php y contiene el resultado
 *    del metodo construir(). Se muestra en la tabla de resultados.
 *
 * 3. <?= $mensaje ?> (SINTAXIS CORTA):
 *    Inserta el valor de $mensaje directamente en el HTML.
 *    Si $mensaje esta vacio (no se envio el formulario), no muestra nada.
 *    Si se envio el formulario, muestra el RFC generado.
 *
 * 4. FLUJO DEL EJERCICIO:
 *    1. Usuario llena nombre, apellidos y fecha
 *    2. Datos se envian por POST a este mismo archivo
 *    3. include_once carga Rfc.php que:
 *       a) Crea el objeto Rfc
 *       b) Agrupa datos en array asociativo
 *       c) Llama a guardar() y construir()
 *    4. La vista muestra el resultado en la tabla
 */

//comando de inclusion con la ruta de las clases
// Al incluir Rfc.php:
// - Se define la clase Rfc con propiedad private $datos (array)
// - Se crea $Rfc1 y $mensaje
// - Si hay POST, se procesan los datos y se genera el RFC
include_once('../clases/ejercicio4/Rfc.php');
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


	<div class="container" style="margin-top: 4em">

	<header> <h1>RFC sin homoclave</h1></header><br>

	<!-- Formulario con 4 campos para generar el RFC -->
	<form method="post">


					 <div class="form-group">
				 		<label for="CajaTexto1">Nombre:</label>
						<input class="form-control" type="text" name="nombre" id="CajaTexto1">
					</div>

					<div class="form-group">
						<label for="CajaTexto2">Apellido paterno:</label>
						<input class="form-control" type="text" name="paterno" id="CajaTexto2">
					</div>

					<div class="form-group">
						<label for="CajaTexto3">Apellido materno:</label>
						<input class="form-control" type="text" name="materno" id="CajaTexto3">
					</div>
					<div class="form-group">

						<label for="CajaTexto4">Fecha de nacimiento:</label>
						<!-- type="date" genera un selector de fecha nativo del navegador -->
						<!-- El formato enviado es YYYY-MM-DD (ej: 1990-01-15) -->
						<input class="form-control" type="date" name="fecha" id="CajaTexto4">

					</div>



		<button class="btn btn-primary" type="submit" >enviar</button>
		<a class="btn btn-link offset-md-8 offset-lg-9 offset-6" href="../index.php">Regresar</a>
	</form>

	</div>

	<!-- TABLA DE RESULTADOS -->
	<div class="container mt-5">
		<h1>Respuesta del servidor</h1>
		<table class="table">
				<thead>
		      <tr>
		       <th>Tu RFC</th>

		      </tr>
		    </thead>
		    <tbody>
					<tr>
						<td>rfc:</td>

			<!-- Agrega una etiqueta php y llama a al metodo que muestra el rfc -->
						<!-- $mensaje contiene el resultado de construir() -->
						<td><?= $mensaje?></td>


					</tr>



			</tbody>
		</table>

    </div>


</body>
</html>


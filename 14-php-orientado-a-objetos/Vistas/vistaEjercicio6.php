<?php
/**
 * ==========================================================================
 * VISTA DEL EJERCICIO 6: HERENCIA
 * ==========================================================================
 *
 * CONCEPTOS CLAVE:
 * ----------------
 *
 * 1. MULTIPLES INCLUDES:
 *    Se incluyen varios archivos de clases. Cada uno define una clase hija
 *    que hereda de transporte. Carro4.php ya incluye a los demas, pero
 *    los include_once adicionales son seguros (no causan doble inclusion).
 *
 * 2. POLIMORFISMO EN LA TABLA:
 *    <?= $mensaje ?> puede contener HTML generado por CUALQUIERA de las
 *    clases hijas (carro, avion, barco, bicicleta). El HTML tiene la
 *    misma estructura (filas de tabla) pero con contenido diferente.
 *
 *    Dependiendo de la seleccion del usuario:
 *    - "aereo"      -> $mensaje viene de avion::resumenAvion()
 *    - "terrestre"  -> $mensaje viene de carro::resumenCarro()
 *    - "maritimo"   -> $mensaje viene de barco::resumenBarco()
 *    - "bicicleta"  -> $mensaje viene de bicicleta::resumenBicicleta()
 *
 *    Todos los metodos resumenX() retornan HTML de tabla, pero cada uno
 *    agrega sus datos especificos (turbinas, puertas, calado, modelo).
 *
 * 3. SELECT (MENU DESPLEGABLE):
 *    <select name="tipo_transporte"> genera un menu con opciones.
 *    Al enviar el formulario, $_POST['tipo_transporte'] contiene
 *    el value de la opcion seleccionada (ej: 'aereo', 'terrestre').
 *    Este valor se usa en el switch de Carro4.php para crear el objeto apropiado.
 */

// Incluimos los archivos de clases
// Carro4.php ya incluye transporte.php, avion.php, bicicleta.php, barco.php
// Pero include_once asegura que no se carguen dos veces
include_once('../Clases/ejercicio6/Carro4.php');
include_once('../Clases/ejercicio6/avion.php');
include_once('../Clases/ejercicio6/bicicleta.php');
include_once('../Clases/ejercicio6/barco.php');

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

	<header> <h1>Los transportes</h1></header><br>

	<form method="post">


					 <div class="form-group">
				 		<label for="CajaTexto1">Tipo de transporte:</label>
				 		<!-- <select> genera un menu desplegable -->
				 		<!-- name="tipo_transporte" -> $_POST['tipo_transporte'] -->
				 		<!-- Cada <option value="..."> define una opcion -->
				 		<!-- El 'value' es lo que se envia por POST (no el texto visible) -->
						<select class="form-control" name="tipo_transporte" id="CajaTexto1">
							<option value='aereo' >Aereo</option>
							<option value='terrestre' >Terrestre</option>
							<option value='maritimo' >Maritimo</option>
							<option value='bicicleta' >Bicicleta</option>
						</select>
					</div>


		<button class="btn btn-primary" type="submit" >enviar</button>
		<a class="btn btn-link offset-md-8 offset-lg-9 offset-6" href="../index.php">Regresar</a>
	</form>

	</div>

	<!-- TABLA DE RESULTADOS -->
	<!-- $mensaje contiene filas <tr> generadas por la clase hija correspondiente -->
	<!-- El mismo <table> se usa para CUALQUIER tipo de transporte -->
	<!-- Esto es POLIMORFISMO: misma interfaz, diferente comportamiento -->
	<div class="container mt-5">
		<h1>Respuesta del servidor</h1>
		<table class="table">
			<thead>
		      <tr>
		      	 <th>Transporte</th>
		      </tr>
		    </thead>
		    <tbody>
		    <!-- $mensaje contiene las filas HTML generadas por resumenCarro(),
		         resumenAvion(), resumenBarco() o resumenBicicleta() -->
			<?= $mensaje; ?>
			</tbody>
		</table>

    </div>



</body>
</html>

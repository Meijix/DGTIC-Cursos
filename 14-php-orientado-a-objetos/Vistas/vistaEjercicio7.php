<?php
/**
 * ==========================================================================
 * VISTA DEL EJERCICIO 7: HERENCIA MULTINIVEL Y PROTECTED
 * ==========================================================================
 *
 * CONCEPTOS CLAVE:
 * ----------------
 *
 * 1. HERENCIA MULTINIVEL EN ACCION:
 *    Al incluir Hijo.php, este incluye Padre.php, que incluye Abuelo.php.
 *    Asi, las tres clases quedan disponibles automaticamente:
 *
 *    vistaEjercicio7.php
 *        -> include Hijo.php
 *            -> include Padre.php
 *                -> include Abuelo.php
 *
 *    La cadena de includes refleja la cadena de herencia.
 *
 * 2. RESULTADO VISUAL:
 *    Cuando el usuario ingresa su nombre y envia el formulario,
 *    la tabla muestra 3 filas correspondientes a 3 generaciones:
 *
 *    +--------+----------------------------------+
 *    | Abuelo | Nemesio Martinez Dominguez       |  <- De Abuelo::crear_ficha()
 *    | Padre  | Jorge Martinez                   |  <- De Padre::resumenPadre()
 *    | Hijo   | [nombre ingresado] Martinez      |  <- De Hijo::resumenHijo()
 *    +--------+----------------------------------+
 *
 *    El apellido "Martinez" se hereda de Abuelo a traves de todas las
 *    generaciones gracias al modificador PROTECTED.
 *
 * 3. PROTECTED EN ACCION:
 *    $apellido_paterno esta definido como protected en Abuelo.
 *    Esto permite que Hijo lo use directamente ($this->apellido_paterno)
 *    a pesar de estar definido 2 niveles arriba en la jerarquia.
 *    Si fuera private, Hijo NO podria acceder a el.
 */

// Incluimos Hijo.php (que automaticamente incluye Padre.php y Abuelo.php)
include_once('../clases/ejercicio7/Hijo.php');
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

	<header> <h1>Familia</h1></header><br>

	<!-- Formulario simple: solo pide el nombre del "hijo" -->
	<form method="post">


					 <div class="form-group">
				 		<label for="CajaTexto1">Escribe tu nombre y descubre de donde vienes:</label>
						<input class="form-control" type="text" name="nombre" id="CajaTexto1">
					</div>

		<button class="btn btn-primary" type="submit" >enviar</button>
		<a class="btn btn-link offset-md-8 offset-lg-9 offset-6" href="../index.php">Regresar</a>
	</form>

	</div>

	<!-- TABLA DE RESULTADOS -->
	<!-- $mensaje contiene las 3 filas del arbol genealogico -->
	<!-- Generadas por Hijo::resumenHijo() que llama a metodos de Padre y Abuelo -->
	<div class="container mt-5">
		<h1>Respuesta del servidor</h1>
		<table class="table">
			<thead>
		      <tr>
		      	 <th></th>
		      </tr>
		    </thead>
		    <tbody>
			<?= $mensaje; ?>

			</tbody>
		</table>

    </div>

</body>
</html>

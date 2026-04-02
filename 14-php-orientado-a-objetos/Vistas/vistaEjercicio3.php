<?php
/**
 * ==========================================================================
 * VISTA DEL EJERCICIO 3: ENCAPSULAMIENTO CON private
 * ==========================================================================
 *
 * CONCEPTOS CLAVE:
 * ----------------
 *
 * 1. DIFERENCIA CON EJERCICIO 2:
 *    En el Ejercicio 2, se accedia a propiedades publicas directamente:
 *      $Carro1->color  (propiedad public)
 *
 *    En el Ejercicio 3, las placas son private, asi que se accede
 *    a traves de un metodo publico:
 *      $Carro1->mostrar_placas()  (metodo que accede a propiedad private)
 *
 * 2. ENCAPSULAMIENTO EN ACCION:
 *    La vista NO sabe como se almacenan las placas internamente.
 *    Solo sabe que puede llamar a mostrar_placas() para obtenerlas.
 *    Esto es encapsulamiento: ocultar la implementacion interna.
 *
 *    Si manana cambiamos como se almacenan las placas (por ejemplo,
 *    usando un formato diferente), la vista NO necesita cambiar.
 *    Solo Carro3.php necesitaria actualizarse.
 */

//comando de inclusion con la ruta de las clases
// Al incluir Carro3.php:
// - Se define la clase Carro3 con propiedad private $placas
// - Se crea $Carro1 y se procesan datos POST si existen
include_once('../clases/ejercicio3/Carro3.php');
?>


<!DOCTYPE html>
<html>
<head>

	<link rel="stylesheet" href="../css/bootstrap.min.css">
	<link rel="stylesheet" href="../css/bootstrap-grid.css">
	<script type="text/javascript" src="../js/bootstrap.min.js"></script>
	<script type="text/javascript" src="../js/jquery-3.4.1.min.js"></script>
	<title>
		Ejercicio 2
	</title>
</head>
<body>

	<div class="container" style="margin-top: 4em">
	<header> <h1>Registro de placas</h1></header><br>

	<!-- Formulario simple con un solo campo: placas -->
	<form method="post">
		<div class="form-group row">
			 <label class="col-sm-1" for="CajaTexto1">Placas:</label>
			 <div class="col-sm-4">
					<input class="form-control" type="text" name="placas" id="CajaTexto1">
			</div>


		</div>
		<button class="btn btn-primary" type="submit" >enviar</button>
		<a class="btn btn-link offset-md-9 offset-lg-9 offset-7" href="../index.php">Regresar</a>
	</form>


	</div>

	<!-- TABLA DE RESULTADOS -->
	<div class="container mt-5">
		<h1>Respuesta del servidor</h1>
		<table class="table">
				<thead>
		      <tr>
		       <th>Información del vehículo</th>

		      </tr>
		    </thead>
		    <tbody>
					<tr>
						<td><?='Placas:'?></td>
						<!-- AQUI SE VE EL ENCAPSULAMIENTO -->
						<!-- No podemos hacer $Carro1->placas (es private) -->
						<!-- Debemos usar el metodo publico mostrar_placas() -->
						<!-- El metodo internamente hace echo $this->placas -->
						<td><?=$Carro1->mostrar_placas()?></td>

					</tr>



			</tbody>
		</table>

    </div>

</body>
</html>

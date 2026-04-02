<?php
/**
 * ==========================================================================
 * VISTA DEL EJERCICIO 2: METODOS Y ATRIBUTOS
 * ==========================================================================
 *
 * CONCEPTOS CLAVE:
 * ----------------
 *
 * 1. include_once CON RUTA RELATIVA:
 *    '../clases/ejercicio2/Carro2.php' usa .. para subir un directorio.
 *    Desde Vistas/ subimos a la raiz y luego entramos a clases/ejercicio2/
 *
 *    Estructura: Vistas/vistaEjercicio2.php -> incluye -> Clases/ejercicio2/Carro2.php
 *
 * 2. SEPARACION CLASE vs VISTA:
 *    A diferencia del Ejercicio 1 (donde la clase estaba en la vista),
 *    aqui la clase Carro2 esta en su propio archivo.
 *    La vista solo se encarga de la PRESENTACION (HTML).
 *
 * 3. SINTAXIS CORTA <?= ?>:
 *    <?=$Carro1->color?> es equivalente a <?php echo $Carro1->color; ?>
 *    Es una forma mas corta y limpia de insertar valores PHP en HTML.
 *
 * 4. ACCESO A PROPIEDADES PUBLIC vs METODOS GETTER:
 *    - $Carro1->color   -> Acceso DIRECTO a propiedad public
 *    - $Carro1->getVerificado() -> Acceso via METODO a propiedad private
 *
 *    Las propiedades publicas se acceden directamente.
 *    Las propiedades privadas necesitan un metodo getter.
 *
 * 5. TABLA HTML PARA MOSTRAR DATOS:
 *    La tabla muestra las propiedades del objeto Carro2.
 *    Cada fila (<tr>) tiene dos celdas (<td>): etiqueta y valor.
 *    Los valores vienen del objeto PHP creado en Carro2.php.
 */

//comando de inclusion con la ruta de las clases
// Al incluir Carro2.php, se ejecuta su codigo:
// - Se define la clase Carro2
// - Se crea el objeto $Carro1
// - Se procesan datos POST si existen
// - $Carro1 queda disponible para usar aqui
include_once('../clases/ejercicio2/Carro2.php');
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
	<header> <h1>La verificación</h1></header><br>

	<!-- Formulario con tres campos: color, modelo y anio -->
	<form method="post">
		<div class="form-group row">
			 <label class="col-sm-1" for="CajaTexto1">Color:</label>
			 <div class="col-sm-4">
					<input class="form-control" type="color" name="color" id="CajaTexto1">
			</div>

			<label class="col-sm-2 pl-md-5 " for="CajaTexto2">Modelo:</label>
			 <div class="col-sm-4 pl-lg-1" >
					<input class="form-control" type="text" name="modelo" id="CajaTexto2">
			</div>

			<label class="col-sm-2 pl-md-5 " for="CajaTexto3">Año:</label>
			 <div class="col-sm-4 pl-lg-1" >
					<input class="form-control" type="int" name="year" id="CajaTexto3">
		</div>
		<button class="btn btn-primary" type="submit" >enviar</button>
		<a class="btn btn-link offset-md-9 offset-lg-9 offset-7" href="../index.php">Regresar</a>
	</form>


	</div>

	<!-- TABLA DE RESULTADOS -->
	<!-- Muestra los datos del objeto $Carro1 despues de procesar el formulario -->
	<div class="container mt-5">
		<h1>Respuesta del servidor</h1>
		<table class="table">
				<thead>
		      <tr>
		       <th>Caracteristicas de carro</th>

		      </tr>
		    </thead>
		    <tbody>
					<tr>
						<!-- <?='texto'?> es igual a <?php echo 'texto'; ?> -->
						<td><?='Color:'?></td>
						<!-- Acceso DIRECTO a propiedad public -->
						<td><?=$Carro1->color?></td>

					</tr>

					<tr>
						<td><?='Modelo:'?></td>
						<!-- Acceso DIRECTO a propiedad public -->
						<td><?=$Carro1->modelo?></td>

					</tr>

					<tr>
						<td><?='Año:'?></td>
						<td><?=$Carro1->year?></td>
					</tr>

					<tr>
						<td><?='Verificación:'?></td>
						<!-- El resultado de estatus de la verificacion NO ES CORRECTO-->
						<!-- Acceso via GETTER a propiedad private -->
						<!-- getVerificado() es la unica forma de leer $verificado -->
						<!-- porque es private en la clase Carro2 -->
						<td><?=$Carro1->getVerificado()?></td>
					</tr>

			</tbody>
		</table>



</body>
</html>

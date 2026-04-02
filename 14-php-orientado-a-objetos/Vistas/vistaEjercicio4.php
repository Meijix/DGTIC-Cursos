<?php
//comando de inclusion con la ruta de las clases
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
						<input class="form-control" type="date" name="fecha" id="CajaTexto4">
						
					</div>
			

		
		<button class="btn btn-primary" type="submit" >enviar</button>
		<a class="btn btn-link offset-md-8 offset-lg-9 offset-6" href="../index.php">Regresar</a>
	</form>

	</div>
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
						<td><?= $mensaje?></td>

													
					</tr>
				
					
					
			</tbody>
		</table>

    </div>


</body>
</html>


<?php
//comando de inclusion con la ruta de las clases
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
						<td><?='Color:'?></td>
						<td><?=$Carro1->color?></td>
													
					</tr>
				
					<tr>
						<td><?='Modelo:'?></td>
						<td><?=$Carro1->modelo?></td>
												
					</tr>

					<tr>
						<td><?='Año:'?></td>
						<td><?=$Carro1->year?></td>
					</tr>

					<tr>
						<td><?='Verificación:'?></td>
						<!-- El resultado de estatus de la verificacion NO ES CORRECTO-->
						<td><?=$Carro1->getVerificado()?></td>
					</tr>
					
			</tbody>
		</table>

    

</body>
</html>
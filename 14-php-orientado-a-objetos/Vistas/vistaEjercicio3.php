<?php
//comando de inclusion con la ruta de las clases
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
						<td><?=$Carro1->mostrar_placas()?></td>
													
					</tr>
				
					
					
			</tbody>
		</table>

    </div>

</body>
</html>
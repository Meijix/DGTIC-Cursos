<?php 
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
	<form method="post">
		

					 <div class="form-group">
				 		<label for="CajaTexto1">Escribe tu nombre y descubre de donde vienes:</label>
						<input class="form-control" type="text" name="nombre" id="CajaTexto1">
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
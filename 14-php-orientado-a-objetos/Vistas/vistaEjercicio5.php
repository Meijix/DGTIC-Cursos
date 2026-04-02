<?php
//comando de inclusion con la ruta de las clases
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
	
	<input class='form-control' type='text' value='<?=$mensaje?>' readonly>

	<div class="container" style="margin-top: 4em">
	
	<header> <h1>Recoge tu token</h1></header><br>
	<form method="post">
		

					 <div class="form-group">
				 		<label for="CajaTexto1">Escribe tu nombre:</label>
						<input class="form-control" type="text" name="nombre" id="CajaTexto1">
					</div>

					
			
		<button class="btn btn-primary" type="submit" >enviar</button>
		<a class="btn btn-link offset-md-8 offset-lg-9 offset-6" href="../index.php">Regresar</a>
	</form>

	</div>



</body>
</html>
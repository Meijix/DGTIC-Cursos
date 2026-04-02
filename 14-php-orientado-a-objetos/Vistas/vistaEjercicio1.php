<?php

class Carro{
	//declaracion de propiedades
	public $color;
	
}


//crea aqui la clase Moto junto con dos propiedades public


//inicializamos el mensaje que lanzara el servidor con vacio
$mensajeServidor='';


//crea aqui la instancia o el objeto de la clase Moto


$Carro1 = new Carro;

 if ( !empty($_POST)){

 	//almacenamos el valor mandado por POST en el atributo color
 	$Carro1->color=$_POST['color'];
 	//se construye el mensaje que sera lanzado por el servidor
 	$mensajeServidor='el servidor dice que ya escogiste un color: '.$_POST['color'];


 	 // recibe aqui los valores mandados por post 
 }  

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
	
	<input type="text" class="form-control" value="<?php  echo $mensajeServidor; ?>" readonly>

	<!-- aqui puedes insertar el mesaje del servidor para Moto-->


	<div class="container" style="margin-top: 4em">
	
	<header> <h1>Carro y Moto</h1></header><br>
	<form method="post">
		<div class="form-group row">

			 <label class="col-sm-3" for="CajaTexto1">Color del carro:</label>
			 <div class="col-sm-4">
					<input class="form-control" type="color" name="color" id="CajaTexto1">
			</div>
			<div class="col-sm-4">
			</div>

			<!-- inserta aqui los inputs para recibir los atributos del objeto-->
						
		</div>
		<button class="btn btn-primary" type="submit" >enviar</button>
		<a class="btn btn-link offset-md-8 offset-lg-9 offset-6" href="../index.php">Regresar</a>
	</form>

	</div>


</body>
</html>


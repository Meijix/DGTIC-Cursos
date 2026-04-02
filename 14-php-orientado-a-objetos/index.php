<?php
	define('DS',DIRECTORY_SEPARATOR);
	define('ROOT',realpath(dirname(__FILE__)).DS);
	
//	require_once "Config/auto.php";
//	Config\auto::run();
//		new Config\request();

?>


<!DOCTYPE html>
<html>
<head>
	<link rel="stylesheet" href="css/bootstrap.min.css">
	
	<title>
		Indice
	</title>
</head>
<body>
	<div class="container" style="margin-top: 4em">
		<div class="row px-md-4 mb-4">
		<h1>Curso de php orientado a objetos</h1>
		<br>
		<h3>Natalia Edith Mejia Bautista</h3>
		</div>
		<div class="list-group row">
			
				<a class="list-group-item list-group-item-info list-group-item-action" href="Vistas/vistaEjercicio1.php">Ejercicio 1: Clases y objetos</a>
				<a class="list-group-item list-group-item-info list-group-item-action" href="Vistas/vistaEjercicio2.php">Ejercicio 2: Métodos y atributos</a>
				<a class="list-group-item list-group-item-info list-group-item-action" href="Vistas/vistaEjercicio3.php">Ejercicio 3: Modificador de acceso private</a>
				<a class="list-group-item list-group-item-info list-group-item-action" href="Vistas/vistaEjercicio4.php">Ejercicio 4: Atributos con arreglos</a>
				<a class="list-group-item list-group-item-info list-group-item-action" href="Vistas/vistaEjercicio5.php">Ejercicio 5: Constructores y destructores</a>
				<a class="list-group-item list-group-item-info list-group-item-action" href="Vistas/vistaEjercicio6.php">Ejercicio 6: Herencia</a>
				<a class="list-group-item list-group-item-info list-group-item-action" href="Vistas/vistaEjercicio7.php">Ejercicio 7: Herencia y modificador de acceso protected</a>
				
		</div>
	</div>
	<script type="text/javascript" src="js/bootstrap.min.js"></script>
	<script type="text/javascript" src="js/jquery-3.4.1.min.js"></script>
</body>
</html>

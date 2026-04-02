<?php
/**
 * ==========================================================================
 * VISTA DEL EJERCICIO 1: CLASES Y OBJETOS BASICOS
 * ==========================================================================
 *
 * CONCEPTOS CLAVE:
 * ----------------
 *
 * 1. PATRON MVC SIMPLIFICADO:
 *    Este proyecto sigue una version simple del patron MVC:
 *    - Modelo (Clases/):  La logica y datos (clase Carro, Moto)
 *    - Vista (Vistas/):   La presentacion (HTML + formularios)
 *    - Controlador:       En este caso, esta mezclado en la Vista
 *
 *    La Vista incluye la Clase (Modelo) y presenta los datos al usuario.
 *
 * 2. DEFINICION DE CLASE DENTRO DE LA VISTA:
 *    En este archivo, la clase Carro se define DIRECTAMENTE aqui
 *    (no se incluye desde un archivo externo). Esto es un antipatron
 *    en proyectos grandes, pero es valido para ejercicios simples.
 *
 *    En los ejercicios siguientes (2-7), la clase se define en un
 *    archivo separado y se incluye con include_once().
 *
 * 3. FORMULARIO -> PROCESAMIENTO -> RESPUESTA:
 *    Este archivo hace tres cosas:
 *    a) Define la clase Carro y crea un objeto
 *    b) Si hay datos POST, asigna valores al objeto
 *    c) Muestra el formulario HTML con la respuesta del servidor
 *
 *    Todo en un solo archivo (se envia a si mismo con method="post").
 *
 * 4. <?php echo $variable; ?> vs <?= $variable ?>:
 *    Son equivalentes. La sintaxis corta <?= ?> es un atajo para echo.
 *    <?= $mensajeServidor ?> es igual a <?php echo $mensajeServidor; ?>
 */

// Definimos la clase Carro directamente en la vista
class Carro{
	//declaracion de propiedades
	// public: se puede acceder desde fuera con $Carro1->color
	public $color;

}


//crea aqui la clase Moto junto con dos propiedades public


//inicializamos el mensaje que lanzara el servidor con vacio
// String vacio como valor inicial para que no haya error al mostrarlo en HTML
$mensajeServidor='';


//crea aqui la instancia o el objeto de la clase Moto


// Creamos el objeto $Carro1 a partir de la clase Carro
$Carro1 = new Carro;

// Si el formulario fue enviado (hay datos POST)...
 if ( !empty($_POST)){

 	//almacenamos el valor mandado por POST en el atributo color
 	// $Carro1->color accede a la propiedad publica del objeto
 	$Carro1->color=$_POST['color'];
 	//se construye el mensaje que sera lanzado por el servidor
 	// Concatenacion con el operador punto (.)
 	$mensajeServidor='el servidor dice que ya escogiste un color: '.$_POST['color'];


 	 // recibe aqui los valores mandados por post
 }

?>

<!-- =====================================================================
     HTML DE LA VISTA
     =====================================================================
     Bootstrap proporciona clases CSS predefinidas para disenar rapidamente:
     - container: centra el contenido con margenes
     - form-group row: organiza formularios en filas
     - form-control: estiliza inputs
     - btn btn-primary: boton azul
     - btn-link: boton que parece enlace
-->
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

	<!-- Input de solo lectura que muestra la respuesta del servidor -->
	<!-- <?php echo $mensajeServidor; ?> inserta el valor de la variable PHP en el HTML -->
	<!-- 'readonly' impide que el usuario edite este campo -->
	<input type="text" class="form-control" value="<?php  echo $mensajeServidor; ?>" readonly>

	<!-- aqui puedes insertar el mesaje del servidor para Moto-->


	<div class="container" style="margin-top: 4em">

	<header> <h1>Carro y Moto</h1></header><br>

	<!-- method="post": datos van en el cuerpo HTTP (no en la URL) -->
	<!-- Sin action: se envia a SI MISMO (esta misma pagina) -->
	<form method="post">
		<div class="form-group row">

			 <label class="col-sm-3" for="CajaTexto1">Color del carro:</label>
			 <div class="col-sm-4">
			 		<!-- type="color" muestra un selector de color nativo del navegador -->
			 		<!-- name="color" -> se accede como $_POST['color'] -->
					<input class="form-control" type="color" name="color" id="CajaTexto1">
			</div>
			<div class="col-sm-4">
			</div>

			<!-- inserta aqui los inputs para recibir los atributos del objeto-->

		</div>
		<button class="btn btn-primary" type="submit" >enviar</button>
		<!-- Enlace para regresar al indice principal -->
		<a class="btn btn-link offset-md-8 offset-lg-9 offset-6" href="../index.php">Regresar</a>
	</form>

	</div>


</body>
</html>


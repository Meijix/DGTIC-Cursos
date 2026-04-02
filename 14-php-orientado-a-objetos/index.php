<?php
/**
 * ==========================================================================
 * PAGINA PRINCIPAL - INDICE DE EJERCICIOS DE PHP ORIENTADO A OBJETOS
 * ==========================================================================
 *
 * CONCEPTOS CLAVE EN ESTE ARCHIVO:
 * ---------------------------------
 *
 * 1. CONSTANTES CON define():
 *    define() crea una constante: un valor que NO puede cambiar durante
 *    la ejecucion del script. A diferencia de las variables ($), las
 *    constantes NO llevan el signo de dolar y por convencion se escriben
 *    en MAYUSCULAS.
 *
 *    define('NOMBRE', valor);
 *    - El primer argumento es el nombre de la constante (string)
 *    - El segundo argumento es el valor
 *
 * 2. DIRECTORY_SEPARATOR:
 *    Constante predefinida de PHP que contiene el separador de directorios
 *    del sistema operativo:
 *    - En Windows: \  (backslash)
 *    - En Linux/Mac: /  (forward slash)
 *    Usarla hace que el codigo sea PORTABLE entre sistemas operativos.
 *
 * 3. realpath() y dirname():
 *    - dirname(__FILE__) retorna el directorio donde esta este archivo
 *    - __FILE__ es una "constante magica" que contiene la ruta completa del archivo actual
 *    - realpath() convierte una ruta relativa en una ruta ABSOLUTA
 *
 * 4. PROGRESION DE EJERCICIOS:
 *    Los 7 ejercicios estan organizados de menor a mayor complejidad:
 *
 *    Ejercicio 1: Clases y objetos           (lo mas basico)
 *    Ejercicio 2: Metodos y atributos        (agregar comportamiento)
 *    Ejercicio 3: Private (encapsulamiento)  (proteger datos)
 *    Ejercicio 4: Arreglos como atributos    (datos complejos)
 *    Ejercicio 5: Constructores/destructores (ciclo de vida del objeto)
 *    Ejercicio 6: Herencia                   (reutilizar codigo)
 *    Ejercicio 7: Protected + herencia multinivel (acceso controlado)
 *
 *    Esta progresion es intencional: cada ejercicio construye sobre el anterior.
 */

	// DS almacena el separador de directorios del sistema operativo
	define('DS',DIRECTORY_SEPARATOR);

	// ROOT almacena la ruta absoluta del directorio actual + separador
	// Esto permite construir rutas de archivos de forma portable:
	// ROOT . 'Clases' . DS . 'archivo.php'
	define('ROOT',realpath(dirname(__FILE__)).DS);

//	require_once "Config/auto.php";
//	Config\auto::run();
//		new Config\request();

?>


<!DOCTYPE html>
<html>
<head>
	<!-- Bootstrap CSS para estilos predefinidos (clases como list-group, container, etc.) -->
	<link rel="stylesheet" href="css/bootstrap.min.css">

	<title>
		Indice
	</title>
</head>
<body>
	<!-- container: clase de Bootstrap que centra el contenido con margenes laterales -->
	<!-- margin-top: 4em separa el contenido del borde superior -->
	<div class="container" style="margin-top: 4em">
		<div class="row px-md-4 mb-4">
		<h1>Curso de php orientado a objetos</h1>
		<br>
		<h3>Natalia Edith Mejia Bautista</h3>
		</div>

		<!--
		LISTA DE EJERCICIOS:
		Cada enlace <a> lleva a una vista diferente.
		Las vistas estan en la carpeta Vistas/ y cada una incluye
		su clase correspondiente desde Clases/ejercicioN/.

		Las clases de Bootstrap usadas:
		- list-group: convierte una lista en un grupo visual
		- list-group-item: cada elemento del grupo
		- list-group-item-info: color azul claro de fondo
		- list-group-item-action: efecto hover al pasar el raton
		-->
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

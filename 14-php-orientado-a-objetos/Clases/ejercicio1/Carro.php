<?php
/**
 * ==========================================================================
 * EJERCICIO 1: CLASES Y OBJETOS - CLASE CARRO
 * ==========================================================================
 *
 * CONCEPTOS CLAVE:
 * ----------------
 *
 * 1. QUE ES UNA CLASE:
 *    Una clase es un PLANO o MOLDE que define la estructura de un objeto.
 *    Es como el plano arquitectonico de una casa: describe QUE tendra
 *    (habitaciones, banos) pero no es una casa en si misma.
 *
 *    Analogia:
 *    - Clase "Carro"  = El plano de un carro (que propiedades tiene)
 *    - Objeto $Carro1 = Un carro real construido a partir de ese plano
 *
 *    CLASE (plano)              OBJETO (instancia)
 *    +------------------+      +------------------+
 *    | Carro            |      | $Carro1          |
 *    |------------------|      |------------------|
 *    | $color           | ---> | $color = "rojo"  |
 *    | $marca           |      | $marca = "Ford"  |
 *    +------------------+      +------------------+
 *
 * 2. PROPIEDADES (ATRIBUTOS):
 *    Son las variables que pertenecen a una clase. Describen las
 *    CARACTERISTICAS del objeto (que datos tiene).
 *
 * 3. MODIFICADOR DE ACCESO 'public':
 *    public significa que la propiedad es accesible desde CUALQUIER LUGAR:
 *    - Desde dentro de la clase
 *    - Desde fuera de la clase (codigo que usa el objeto)
 *    - Desde clases hijas (herencia)
 *
 *    Es el nivel de acceso MAS PERMISIVO. En ejercicios posteriores
 *    veremos private y protected que restringen el acceso.
 *
 * 4. INSTANCIACION (new):
 *    $Carro1 = new Carro;
 *    Crea un OBJETO (instancia) a partir de la clase.
 *    Es como construir una casa a partir de un plano.
 *    Cada objeto tiene sus propios valores de propiedades.
 *
 * 5. OPERADOR FLECHA (->):
 *    Se usa para acceder a propiedades y metodos de un objeto.
 *    $Carro1->color = "rojo";  // Asignar valor a la propiedad
 *    echo $Carro1->color;       // Leer valor de la propiedad
 *
 *    Equivalencia:
 *    PHP:    $objeto->propiedad
 *    Python: objeto.propiedad
 *    Java:   objeto.propiedad
 *
 * 6. $_POST Y FORMULARIOS:
 *    Este archivo tambien maneja datos del formulario (de la vista).
 *    Cuando el usuario envia el formulario, $_POST contiene los datos.
 *    !empty($_POST) verifica que hay datos enviados.
 */

// Definicion de la clase Carro
// La palabra clave 'class' seguida del nombre inicia la definicion
class Carro{
	//declaracion de propiedades
	// 'public' permite acceder a estas propiedades desde fuera de la clase
	// Ejemplo: $Carro1->color = "rojo";  (esto es posible porque son public)
	public $color;
	public $marca;
}

// ==========================================================================
// CODIGO DE EJECUCION (fuera de la clase)
// ==========================================================================

//inicializamos el mensaje que lanzara el servidor con vacio
// Esta variable almacenara la respuesta que se mostrara en la vista
$mensajeServidor='';

// INSTANCIACION: Creamos un OBJETO a partir de la clase Carro
// $Carro1 es ahora una instancia de Carro con sus propias propiedades
// En este momento, $color y $marca estan vacias (null)
//se instancia la clase Carro
$Carro1 = new Carro;

// Verificamos si el formulario fue enviado (si hay datos POST)
// !empty($_POST) retorna true si $_POST NO esta vacio
//verifica si se ha enviado una petición POST
 if ( !empty($_POST)){

 	// ACCESO A PROPIEDADES CON ->
 	// $Carro1->color accede a la propiedad 'color' del objeto $Carro1
 	// $_POST['color'] contiene el valor enviado desde el formulario
 	//almacenamos el valor mandado por POST en el atributo color
 	$Carro1->color=$_POST['color'];

 	// CONCATENACION DE CADENAS con el operador punto (.)
 	// Construimos un mensaje uniendo texto fijo con el valor dinamico
 	//se construye el mensaje que sera lanzado por el servidor
 	$mensajeServidor='el servidor dice que ya escogiste un color: '.$_POST['color'];
 }


?>

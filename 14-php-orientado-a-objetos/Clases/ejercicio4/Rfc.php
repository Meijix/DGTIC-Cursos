<?php
/**
 * ==========================================================================
 * EJERCICIO 4: ATRIBUTOS CON ARREGLOS (ARRAYS COMO PROPIEDADES)
 * ==========================================================================
 *
 * PROGRESION:
 * Ejercicio 1: Propiedades simples (string)
 * Ejercicio 2: Propiedades simples + metodos
 * Ejercicio 3: Propiedades private simples
 * Ejercicio 4: Propiedades private de tipo ARRAY (datos complejos)
 *
 * CONCEPTOS CLAVE:
 * ----------------
 *
 * 1. ARRAYS COMO PROPIEDADES:
 *    Las propiedades de una clase pueden ser de cualquier tipo, incluyendo
 *    arrays (arreglos). Esto permite almacenar MULTIPLES valores
 *    relacionados en una sola propiedad.
 *
 *    En este caso, $datos es un array asociativo que contiene:
 *    ['nombre' => 'Juan', 'paterno' => 'Perez', 'materno' => 'Lopez', 'fecha' => '1990-01-15']
 *
 *    Es como una "mini base de datos" dentro del objeto.
 *
 * 2. METODOS PRIVATE:
 *    Asi como las propiedades pueden ser private, los metodos tambien.
 *    Un metodo private SOLO puede ser llamado desde DENTRO de la clase.
 *
 *    En este ejemplo, construir() es private porque es un metodo INTERNO
 *    que solo la clase necesita usar. El codigo externo no deberia llamarlo
 *    directamente.
 *
 *    NOTA: En el codigo de ejecucion se llama $Rfc1->construir() desde fuera,
 *    lo cual produciria un error:
 *    "Call to private method Rfc::construir() from scope"
 *    Este es un bug intencional o educativo para mostrar el error.
 *
 * 3. PATRON DE DISENO - SEPARACION DE RESPONSABILIDADES:
 *    - guardar(): Metodo PUBLIC para recibir datos del exterior
 *    - construir(): Metodo PRIVATE para logica interna
 *
 *    El exterior solo necesita saber "guardar datos" y "obtener RFC".
 *    No necesita saber COMO se construye el RFC internamente.
 *
 * 4. INICIALIZACION DE ARRAYS:
 *    private $datos = array();
 *    Esto crea un array VACIO como valor inicial de la propiedad.
 *    array() y [] son equivalentes en PHP moderno:
 *    - $datos = array();   // Sintaxis clasica
 *    - $datos = [];        // Sintaxis moderna (PHP 5.4+)
 */

class Rfc{

	//declara un atributo private de tipo arreglo para los datos
	// Se inicializa como array vacio usando array() (sintaxis clasica)
	// Esto evita errores si se intenta acceder antes de guardar datos
	private $datos=array();

	/**
	 * Metodo PUBLIC para guardar datos en el atributo private.
	 * Este es el "punto de entrada" para los datos del formulario.
	 * Recibe un array asociativo y lo almacena completo en $this->datos.
	 *
	 * @param array $datos Array asociativo con nombre, paterno, materno, fecha
	 */
	//declara un metodo public para guardar los datos en el atributo private
	public function guardar($datos){
		// $this->datos (propiedad del objeto) recibe el array completo
		// Despues de esto, $this->datos['nombre'] contiene el nombre, etc.
		$this->datos=$datos;

	}

	/**
	 * Metodo PRIVATE para construir el RFC con los datos almacenados.
	 * Al ser private, SOLO puede ser llamado desde dentro de esta clase.
	 *
	 * NOTA: Este metodo solo retorna el nombre. En un ejercicio completo,
	 * deberia construir el RFC usando:
	 * - Primeras 2 letras del apellido paterno
	 * - Primera letra del apellido materno
	 * - Primera letra del nombre
	 * - Fecha de nacimiento (AA/MM/DD)
	 *
	 * @return string El RFC construido (incompleto en esta version)
	 */
	//declara un metodo private para generar el rfc con los datos de atributo y retornalo con un return
	private function construir(){
		// Accedemos al array $datos usando la clave 'nombre'
		// $this->datos['nombre'] funciona porque $datos es un array asociativo
		return $this->datos['nombre'];

	}

}

// Variable para almacenar el mensaje de respuesta
$mensaje='';

// Instanciamos la clase Rfc
// NOTA: "new Rfc" sin parentesis funciona igual que "new Rfc()" cuando
// no hay constructor que reciba parametros
//crea un objeto instanciado a la calse Rfc
$Rfc1 = new Rfc;

//si existe solicitudes POST entonces guarda dichos datos en un arreglo que se declare de forma asociativa
if ( !empty($_POST)){

	// Creamos un array asociativo con los datos del formulario
	// Cada clave del array corresponde a un campo del formulario
	$datos_front = [
		'nombre' => $_POST['nombre'],
		'paterno'=> $_POST['paterno'],
		'materno'=> $_POST['materno'],
		'fecha'=> $_POST['fecha']
	];

	//usa el metodo para guardar poniendo al arreglo como parametro
	// Primero guardamos los datos en el objeto
	$Rfc1->guardar($datos_front);

	// Luego intentamos construir el RFC
	// NOTA: construir() es PRIVATE, asi que esta linea produciria un error:
	// "Call to private method Rfc::construir() from global scope"
	// Para que funcione, construir() deberia ser public,
	// o deberia haber un metodo public que llame a construir() internamente
	$mensaje=$Rfc1->construir();

}

?>

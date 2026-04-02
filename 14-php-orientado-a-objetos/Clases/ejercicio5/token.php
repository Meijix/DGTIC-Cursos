<?php
/**
 * ==========================================================================
 * EJERCICIO 5 (PARTE 1): CONSTRUCTOR Y DESTRUCTOR - GENERADOR DE TOKEN
 * ==========================================================================
 *
 * CONCEPTOS CLAVE:
 * ----------------
 *
 * 1. CONSTRUCTOR (__construct):
 *    Se ejecuta automaticamente al crear el objeto con 'new'.
 *    En este caso, recibe un parametro $nombre_front que se almacena
 *    en la propiedad privada $nombre, y genera un token aleatorio.
 *
 *    FLUJO:
 *    $token1 = new token("Natalia");
 *                    |
 *                    v
 *    __construct("Natalia") se ejecuta:
 *      -> $this->nombre = "Natalia"
 *      -> $this->token = rand()   (numero aleatorio)
 *
 * 2. DESTRUCTOR (__destruct):
 *    Se ejecuta cuando el objeto se destruye (al final del script
 *    o cuando se usa unset()).
 *
 *    En este ejemplo, el destructor "invalida" el token asignandole
 *    un mensaje de texto y lo muestra en pantalla.
 *
 *    ORDEN DE EJECUCION EN ESTE ARCHIVO:
 *    1. Se crea el objeto: new token("Natalia") -> __construct()
 *    2. Se llama a mostrar() -> retorna el mensaje con el token
 *    3. El script PHP termina
 *    4. PHP destruye el objeto -> __destruct() se ejecuta
 *    5. Se muestra "El token ha sido destruido" en la pagina
 *
 * 3. rand() - NUMEROS ALEATORIOS:
 *    Genera un numero entero aleatorio.
 *    - rand()        -> numero aleatorio entre 0 y getrandmax()
 *    - rand(1, 100)  -> numero aleatorio entre 1 y 100
 *
 *    NOTA: Para tokens de seguridad reales, se debe usar:
 *    - random_int(min, max)  -> criptograficamente seguro
 *    - bin2hex(random_bytes(16))  -> token hexadecimal seguro
 *
 * 4. return vs echo EN METODOS:
 *    - mostrar() usa RETURN: retorna el valor al codigo que lo llamo
 *      El codigo que llama decide que hacer con el valor
 *    - __destruct() usa ECHO: imprime directamente en la pagina
 *      No hay "codigo que lo llame" porque se ejecuta automaticamente
 *
 *    BUENA PRACTICA: Preferir return en metodos normales.
 *    Esto hace el metodo mas flexible y testeable.
 */

//declaracion de clase token
	class token{
		//declaracion de atributos
		// Ambos son private: solo accesibles desde dentro de la clase
		private $nombre;
		private $token;

		/**
		 * CONSTRUCTOR: Se ejecuta al hacer new token("nombre")
		 * Almacena el nombre y genera un token numerico aleatorio.
		 *
		 * NOTA: El parametro se llama $nombre_front para distinguirlo
		 * de la propiedad $this->nombre. Podrian tener el mismo nombre
		 * sin conflicto gracias a $this->
		 *
		 * @param string $nombre_front Nombre del usuario desde el formulario
		 */
		//declaracion de metodo constructor
		public function __construct($nombre_front){
			$this->nombre=$nombre_front;
			// rand() genera un numero aleatorio, ej: 1847362950
			$this->token=rand();
		}

		/**
		 * Metodo que construye y RETORNA un mensaje con el nombre y token.
		 * Usa RETURN (no echo) para que el codigo externo decida como usarlo.
		 *
		 * @return string Mensaje con formato "Hola [nombre] este es tu token: [numero]"
		 */
		//declaracion del metodo mostrar para armar el mensaje con el nombre y token
		public function mostrar(){
			// Concatenacion con el operador punto (.)
			return 'Hola '.$this->nombre.' este es tu token: '.$this->token;
		}

		/**
		 * DESTRUCTOR: Se ejecuta automaticamente cuando el objeto se destruye.
		 * "Invalida" el token reemplazandolo con un mensaje de texto
		 * y lo muestra directamente en la pagina.
		 *
		 * NOTA: El token original se PIERDE al sobreescribirlo.
		 * Esto simula la "expiracion" de un token de seguridad.
		 */
		//declaracion de metodo destructor
		public function __destruct(){
			//destruye token
			// Sobreescribimos el token numerico con un mensaje de texto
			$this->token='El token ha sido destruido';
			// echo dentro del destructor: se ejecuta al final del script
			echo $this->token;
		}
	}

// Variable para almacenar el mensaje de respuesta
$mensaje='';


if (!empty($_POST)){
	//creacion de objeto de la clase
	// Al hacer new token($_POST['nombre']):
	// 1. __construct() se ejecuta con el nombre del formulario
	// 2. Se genera el token aleatorio
	$token1= new token($_POST['nombre']);

	// mostrar() retorna el mensaje, no lo imprime
	// Guardamos el resultado en $mensaje para usarlo en la vista
	$mensaje=$token1->mostrar();
}

// Cuando PHP termina este archivo:
// Si $token1 existe, __destruct() se ejecuta automaticamente
// y muestra "El token ha sido destruido" en la pagina


?>

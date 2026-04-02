<?php
/**
 * ==========================================================================
 * EJERCICIO 2: METODOS, CONSTRUCTOR Y GETTER/SETTER
 * ==========================================================================
 *
 * PROGRESION DESDE EJERCICIO 1:
 * Ejercicio 1: Solo propiedades publicas (datos sin comportamiento)
 * Ejercicio 2: Agregamos METODOS (comportamiento) y un atributo PRIVATE
 *
 * CONCEPTOS CLAVE:
 * ----------------
 *
 * 1. METODOS:
 *    Son funciones que pertenecen a una clase. Definen el COMPORTAMIENTO
 *    del objeto (que puede HACER).
 *
 *    Analogia con un carro real:
 *    - Propiedades: color, modelo, anio (CARACTERISTICAS - que ES)
 *    - Metodos:     verificacion(), acelerar() (COMPORTAMIENTO - que HACE)
 *
 * 2. __construct() - CONSTRUCTOR:
 *    Metodo especial que se ejecuta AUTOMATICAMENTE cuando se crea un objeto.
 *    Se usa para inicializar las propiedades del objeto con valores por defecto.
 *
 *    $Carro1 = new Carro2();  // __construct() se ejecuta automaticamente aqui
 *
 *    Los metodos que empiezan con __ (doble guion bajo) son "metodos magicos"
 *    de PHP. No los llamas directamente; PHP los ejecuta en momentos especificos.
 *
 * 3. $this:
 *    Palabra clave que se refiere al OBJETO ACTUAL (la instancia que esta
 *    ejecutando el metodo). Permite acceder a las propiedades y metodos
 *    del mismo objeto desde dentro de la clase.
 *
 *    $this->color      accede a la propiedad $color de ESTE objeto
 *    $this->verificar() llama al metodo verificar() de ESTE objeto
 *
 *    Equivalencia:
 *    PHP:    $this->propiedad
 *    Python: self.propiedad
 *    Java:   this.propiedad
 *
 * 4. GETTER y SETTER:
 *    Son metodos que controlan el acceso a propiedades privadas.
 *    - getter (getVerificado): OBTIENE el valor de una propiedad privada
 *    - setter (setVerificado): ESTABLECE el valor de una propiedad privada
 *
 *    Por que usarlos?
 *    - Permiten VALIDAR datos antes de asignarlos
 *    - Permiten agregar logica adicional al leer/escribir
 *    - Son el puente entre el mundo exterior y los datos privados
 *
 *    Sin getter/setter (propiedad publica):
 *    $carro->verificado = "cualquier cosa";  // Sin control
 *
 *    Con getter/setter (propiedad privada):
 *    $carro->setVerificado("valor");  // El setter puede validar
 *
 * 5. MEZCLA DE public Y private:
 *    Este ejercicio introduce la PRIMERA propiedad private ($verificado).
 *    Las propiedades public ($color, $modelo, $year) se acceden directamente.
 *    La propiedad private ($verificado) solo se accede via getter/setter.
 */

//creación de la clase carro
class Carro2{
	//declaracion de propiedades
	// public: accesibles desde fuera de la clase con $objeto->propiedad
	public $color;
	public $modelo;
	public $year;

	// private: SOLO accesible desde DENTRO de esta clase
	// NO se puede hacer $Carro1->verificado desde fuera (daria error)
	// Se accede unicamente a traves de getVerificado() y setVerificado()
	private $verificado;

	/**
	 * CONSTRUCTOR: Se ejecuta automaticamente al hacer new Carro2()
	 * Inicializa todas las propiedades con valores por defecto.
	 * Sin esto, las propiedades serian null hasta que se les asigne valor.
	 */
	public function __construct() {
		// $this-> se refiere al objeto que se esta creando
		$this->color = "";
		$this->modelo = "";
		$this->year = 0;
		$this->verificado = "";
	}

	/**
	 * GETTER: Metodo publico que RETORNA el valor de la propiedad privada.
	 * Es la unica forma de LEER $verificado desde fuera de la clase.
	 * @return string El estado de verificacion del carro
	 */
	public function getVerificado() {
		return $this->verificado;
    }

	/**
	 * SETTER: Metodo publico que ASIGNA un valor a la propiedad privada.
	 * Es la unica forma de ESCRIBIR en $verificado desde fuera de la clase.
	 * Aqui se podria agregar validacion antes de asignar el valor.
	 * @param string $verificado El nuevo estado de verificacion
	 */
	public function setVerificado($verificado) {
		$this->verificado = $verificado;
    }

	/**
	 * METODO verificacion():
	 * Determina si el carro puede circular segun su anio de fabricacion.
	 * Este metodo demuestra como un objeto puede MODIFICAR sus propias
	 * propiedades privadas usando $this-> y el setter.
	 *
	 * Logica:
	 * - Anio >= 2010:          "Circula" (carro relativamente nuevo)
	 * - 1990 <= Anio < 2010:   "Revision" (necesita inspeccion)
	 * - Anio < 1990:           "No circula" (carro muy antiguo)
	 */
	//declaracion del método verificación
	//se verificará mediante el año de fabricación del carro si circula o no guiándose por la tabla.
	public function verificacion() {
		// $this->year accede a la propiedad year de ESTE objeto
		$year = $this->year;
		if ($year >= 2010) {
			// Usa el setter para asignar el valor (buena practica)
			$this->setVerificado("Circula");
		} elseif ($year < 2010 && $year >= 1990) {
			$this->setVerificado("Revision");
		} else {
			$this->setVerificado("No circula");
		}
	}
}

// ==========================================================================
// CODIGO DE EJECUCION (fuera de la clase)
// ==========================================================================

// Creamos una instancia de Carro2 usando new
// El constructor __construct() se ejecuta automaticamente aqui
// Todas las propiedades se inicializan con sus valores por defecto
//creación de instancia a la clase Carro
$Carro1 = new Carro2();

// Llamamos al metodo verificacion() ANTES de tener datos del formulario
// Con year = 0 (valor del constructor), el resultado sera "No circula"
$Carro1->verificacion();

// Procesamos los datos del formulario si fueron enviados
if (!empty($_POST)){
	// Asignamos los datos del POST a las propiedades publicas
	// Esto es posible porque $color, $modelo y $year son public
	$Carro1->color=$_POST['color'];
	$Carro1->modelo=$_POST['modelo'];
	$Carro1->year=$_POST['year'];

	// NOTA: Despues de asignar el year del POST, deberiamos llamar
	// verificacion() de nuevo para actualizar el estado con el year real:
	// $Carro1->verificacion();
}





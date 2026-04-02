<?php
/**
 * ==========================================================================
 * EJERCICIO 3: ENCAPSULAMIENTO CON private
 * ==========================================================================
 *
 * PROGRESION:
 * Ejercicio 1: Propiedades publicas (sin proteccion)
 * Ejercicio 2: Mix de public + private con getter/setter
 * Ejercicio 3: SOLO propiedades private + metodos publicos para acceder
 *
 * CONCEPTOS CLAVE:
 * ----------------
 *
 * 1. ENCAPSULAMIENTO (ENCAPSULATION):
 *    Es el principio de OCULTAR los datos internos de un objeto y
 *    proporcionar metodos publicos para interactuar con ellos.
 *
 *    Analogia: Un cajero automatico
 *    - private: El dinero dentro del cajero (no puedes tocarlo directamente)
 *    - public:  Los botones y pantalla (la interfaz para interactuar)
 *    - No puedes meter la mano y sacar dinero; debes usar los botones (metodos)
 *
 *    SIN encapsulamiento (Ejercicio 1):
 *    $Carro1->placas = "ABC-123";     // Cualquiera puede cambiar las placas!
 *    $Carro1->placas = "";             // Cualquiera puede borrarlas!
 *
 *    CON encapsulamiento (Ejercicio 3):
 *    $Carro1->registrar_placas("ABC-123");  // Pasa por un metodo que puede VALIDAR
 *    // $Carro1->placas = "";  // ERROR: no se puede acceder a propiedad private
 *
 * 2. POR QUE USAR private:
 *    - PROTECCION: Evita que codigo externo modifique datos incorrectamente
 *    - VALIDACION: Los metodos publicos pueden verificar datos antes de guardarlos
 *    - FLEXIBILIDAD: Puedes cambiar la implementacion interna sin afectar al resto
 *    - CONTROL: Sabes exactamente donde se modifican los datos (solo en la clase)
 *
 * 3. EJEMPLO DE POR QUE IMPORTA:
 *    Imagina que las placas deben tener formato "XXX-000".
 *    Con private + metodo, puedes validar:
 *
 *    public function registrar_placas($placas) {
 *        if (preg_match("/^[A-Z]{3}-[0-9]{3}$/", $placas)) {
 *            $this->placas = $placas;  // Solo asigna si es valido
 *        } else {
 *            echo "Formato de placa invalido";
 *        }
 *    }
 *
 *    Con public, no hay forma de prevenir datos invalidos.
 *
 * 4. TABLA DE ACCESO:
 *    +-------------+--------+---------+-----------+
 *    | Modificador | Clase  | Hija    | Exterior  |
 *    +-------------+--------+---------+-----------+
 *    | public      | SI     | SI      | SI        |
 *    | protected   | SI     | SI      | NO        |
 *    | private     | SI     | NO      | NO        |
 *    +-------------+--------+---------+-----------+
 *
 *    private es el nivel MAS RESTRICTIVO: solo la propia clase puede acceder.
 */

//creación de la clase carro
class Carro3{
	//declaracion de propiedades
	// private: SOLO accesible desde dentro de esta clase
	// Intentar $Carro1->placas desde fuera produciria un ERROR FATAL:
	// "Cannot access private property Carro3::$placas"
	private $placas;


	/**
	 * Metodo publico para REGISTRAR (escribir) las placas.
	 * Este es el UNICO camino para asignar un valor a $placas.
	 * Es el "setter" de las placas, aunque no sigue la convencion setPlacas().
	 *
	 * @param string $placas Las placas a registrar
	 */
	//declaracion del método verificación
	public function registrar_placas($placas){
		// $this->placas accede a la propiedad private de ESTE objeto
		// $placas (sin $this->) es el parametro recibido del metodo
		// CUIDADO: No confundir $this->placas (propiedad) con $placas (parametro)
		$this->placas=$placas;
	}

	/**
	 * Metodo publico para MOSTRAR (leer) las placas.
	 * Este es el UNICO camino para leer el valor de $placas.
	 * Es el "getter" de las placas, aunque usa echo en vez de return.
	 *
	 * NOTA: Seria mejor practica usar return en vez de echo:
	 * public function mostrar_placas() { return $this->placas; }
	 * Esto permite al codigo que llama decidir QUE hacer con el valor.
	 */
	public function mostrar_placas(){
		echo $this->placas;
	}
}

// ==========================================================================
// CODIGO DE EJECUCION
// ==========================================================================

//creación de instancia a la clase Carro
$Carro1 = new Carro3();

if (!empty($_POST)){
	// LINEA COMENTADA - Esto causaria un ERROR:
	// $Carro1->placas = $_POST['placas'];
	// Error: "Cannot access private property Carro3::$placas"
	// Porque $placas es private, NO se puede acceder directamente

	// FORMA CORRECTA: Usar el metodo publico registrar_placas()
	// El metodo SI puede acceder a $this->placas porque esta DENTRO de la clase
	//$Carro1->placas=$_POST['placas'];
	$Carro1->registrar_placas($_POST['placas']);
}

?>


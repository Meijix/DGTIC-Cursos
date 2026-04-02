<?php
/**
 * ==========================================================================
 * EJERCICIO 7: HERENCIA MULTINIVEL - CLASE "HIJO" (NIVEL FINAL)
 * ==========================================================================
 *
 * CONCEPTOS CLAVE:
 * ----------------
 *
 * 1. HERENCIA MULTINIVEL COMPLETA:
 *    Hijo extiende Padre, que a su vez extiende Abuelo.
 *    Hijo tiene acceso a TODO lo protected/public de AMBOS ancestros.
 *
 *    Lo que Hijo puede acceder con $this->:
 *    +-------------------+------------------+---------------------+
 *    | De Abuelo         | De Padre         | Propias de Hijo     |
 *    +-------------------+------------------+---------------------+
 *    | $nombreAbuelo     | $nombrePadre     | $nombre             |
 *    | $apellido_paterno | resumenPadre()   | __construct()       |
 *    | $apellido_materno |                  | resumenHijo()       |
 *    | crear_ficha()     |                  |                     |
 *    +-------------------+------------------+---------------------+
 *
 *    Todo esto gracias a que las propiedades son PROTECTED.
 *    Si fueran PRIVATE, Hijo NO podria acceder a nada de Abuelo.
 *
 * 2. parent:: EN HERENCIA MULTINIVEL:
 *    En resumenHijo():
 *    - parent::crear_ficha() busca crear_ficha() en Padre.
 *      Como Padre NO define crear_ficha(), sube a Abuelo donde SI existe.
 *      PHP busca automaticamente en la cadena de herencia.
 *
 *    - $this->resumenPadre() llama al metodo de Padre.
 *      Funciona sin parent:: porque $this-> busca en toda la cadena.
 *
 *    Diferencia:
 *    - parent:: busca SOLO en el padre directo (y su cadena si no lo encuentra)
 *    - $this-> busca en toda la cadena, empezando por la clase actual
 *
 * 3. CONSTRUCTOR PROPIO EN LA CLASE FINAL:
 *    Hijo tiene __construct($nombre) que SOLO inicializa $this->nombre.
 *    Las propiedades de Abuelo y Padre ya tienen valores por defecto
 *    (definidos directamente en la declaracion: protected $nombreAbuelo='Nemesio').
 *
 *    NOTA: Si Abuelo o Padre tuvieran constructores con parametros obligatorios,
 *    Hijo deberia llamar parent::__construct() aqui.
 *
 * 4. COMPOSICION DEL RESUMEN:
 *    resumenHijo() COMBINA informacion de 3 generaciones:
 *    1. parent::crear_ficha()    -> Ficha del abuelo (de Abuelo)
 *    2. $this->resumenPadre()    -> Ficha del padre (de Padre)
 *    3. HTML con $this->nombre   -> Ficha del hijo (propia)
 *
 *    El resultado es un arbol genealogico completo, construido
 *    reutilizando metodos de cada nivel de la herencia.
 */

// Solo necesitamos incluir Padre.php (que a su vez incluye Abuelo.php)
// La cadena de includes sigue la cadena de herencia
include_once('Padre.php');

//declara una clase Hijo que extienda Padres
	class Hijo extends Padre{

		// Propiedad propia de Hijo: su nombre
		// Es protected por si alguien creara una clase Nieto en el futuro
		protected $nombre;

		/**
		 * Constructor que recibe el nombre del hijo.
		 * Las propiedades de Abuelo y Padre ya tienen valores por defecto,
		 * asi que no necesitamos inicializarlas aqui.
		 *
		 * @param string $nombre Nombre del hijo (viene del formulario)
		 */
		public function __construct($nombre){
			$this->nombre=$nombre;
		}

		/**
		 * Genera el resumen COMPLETO de la familia (3 generaciones).
		 * Demuestra como Hijo puede acceder a metodos y propiedades
		 * de TODA la cadena de herencia.
		 *
		 * @return string HTML con filas de tabla: abuelo + padre + hijo
		 */
		public function resumenHijo(){
			// parent::crear_ficha() -> busca en Padre, no lo encuentra,
			// sube a Abuelo -> ejecuta Abuelo::crear_ficha()
			// Genera: "Abuelo: Nemesio Martinez Dominguez"
			$resumen=parent::crear_ficha();

			// $this->resumenPadre() -> llama al metodo de Padre
			// Genera: "Padre: Jorge Martinez"
			// NOTA: resumenPadre() accede a $this->apellido_paterno (de Abuelo)
			$resumen.=$this->resumenPadre();

			// Agrega la fila del hijo con su nombre + apellido heredado
			// $this->nombre: propiedad PROPIA de Hijo
			// $this->apellido_paterno: propiedad HEREDADA de Abuelo (2 niveles arriba!)
			$resumen.='<tr>
						<td>Hijo:</td>
						<td>'. $this->nombre.' '.$this->apellido_paterno.'</td>
					</tr>
					';
			return $resumen;
		}

	}

// ==========================================================================
// LOGICA PRINCIPAL: Procesar formulario y crear objeto Hijo
// ==========================================================================

$mensaje='';

if (!empty($_POST)){
	//creacion de objeto de la clase
	// Al crear new Hijo("Natalia"):
	// 1. PHP reserva memoria
	// 2. Hijo::__construct("Natalia") se ejecuta
	// 3. $this->nombre = "Natalia"
	// 4. Las propiedades de Abuelo y Padre ya tienen valores por defecto
	$hijo1= new Hijo($_POST['nombre']);

	// resumenHijo() genera el HTML con las 3 generaciones:
	// Abuelo: Nemesio Martinez Dominguez
	// Padre: Jorge Martinez
	// Hijo: [nombre del input] Martinez
	$mensaje=$hijo1->resumenHijo();
}


?>

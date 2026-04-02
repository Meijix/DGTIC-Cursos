<?php
/**
 * ==========================================================================
 * EJERCICIO 6: HERENCIA - CLASE HIJA "CARRO" + LOGICA PRINCIPAL
 * ==========================================================================
 *
 * CONCEPTOS CLAVE:
 * ----------------
 *
 * 1. extends - HERENCIA:
 *    "class carro extends transporte" significa:
 *    - carro ES UN tipo de transporte
 *    - carro HEREDA todas las propiedades y metodos publicos de transporte
 *    - carro puede agregar sus PROPIAS propiedades y metodos adicionales
 *
 *    Despues de extends, carro tiene:
 *    - De transporte: nombre, velocidad_max, tipo_combustible, crear_ficha()
 *    - Propias: numero_puertas, resumenCarro()
 *
 * 2. parent::__construct() - LLAMAR AL CONSTRUCTOR PADRE:
 *    Cuando la clase hija tiene su propio constructor, el constructor
 *    del padre NO se ejecuta automaticamente. Hay que llamarlo explicitamente.
 *
 *    parent:: es la forma de acceder a metodos de la clase padre desde la hija.
 *    parent::__construct($nom, $vel, $com) ejecuta el constructor de transporte,
 *    que inicializa las propiedades comunes (nombre, velocidad, combustible).
 *
 *    Sin parent::__construct(), las propiedades heredadas quedarian sin inicializar.
 *
 * 3. parent::crear_ficha() - EXTENDER METODOS DEL PADRE:
 *    En resumenCarro(), se llama a parent::crear_ficha() para obtener
 *    el HTML base (nombre, velocidad, combustible) y luego se le AGREGA
 *    la informacion propia del carro (numero de puertas).
 *
 *    Esto es diferente a SOBREESCRIBIR: no reemplazamos crear_ficha(),
 *    sino que la USAMOS como base y le agregamos mas contenido.
 *
 * 4. OPERADOR .= (CONCATENAR Y ASIGNAR):
 *    $mensaje .= 'texto';  es equivalente a  $mensaje = $mensaje . 'texto';
 *    Agrega texto al final de la cadena existente.
 *
 * 5. switch - SELECCION MULTIPLE:
 *    Evalua una expresion y ejecuta el bloque del case que coincida.
 *    Cada case DEBE terminar con break; o PHP seguira ejecutando
 *    los cases siguientes ("fall-through").
 *
 * 6. POLIMORFISMO (concepto avanzado):
 *    Cada clase hija (carro, avion, barco, bicicleta) tiene su propio
 *    metodo resumen (resumenCarro, resumenAvion, etc.).
 *    Todos hacen algo similar (generar una ficha) pero cada uno lo hace
 *    a su manera, agregando sus propios datos.
 */

// Incluimos las clases necesarias
// include_once asegura que cada archivo se cargue solo una vez
// Esto es necesario porque cada clase hija esta en su propio archivo
include_once('transporte.php');
include_once('bicicleta.php');
include_once('barco.php');
include_once('avion.php');


	//declaracion de la clase hijo o subclase Carro
	// 'extends' es la palabra clave para HEREDAR de otra clase
	// carro hereda TODO lo publico y protegido de transporte
	class carro extends transporte{

		// Propiedad PROPIA de carro (no la tienen avion, barco, etc.)
		private $numero_puertas;

		/**
		 * CONSTRUCTOR de la clase hija.
		 * Recibe 4 parametros: 3 para el padre + 1 propio.
		 *
		 * @param string $nom Nombre (para transporte)
		 * @param string $vel Velocidad maxima (para transporte)
		 * @param string $com Tipo de combustible (para transporte)
		 * @param string $pue Numero de puertas (propio de carro)
		 */
		//declaracion de constructor
		public function __construct($nom,$vel,$com,$pue){
			//sobreescritura de constructor de la clase padre
			// parent::__construct() llama al constructor de transporte
			// para inicializar las 3 propiedades comunes
			parent::__construct($nom,$vel,$com);
			// Inicializamos la propiedad propia de carro
			$this->numero_puertas=$pue;

		}

		/**
		 * Genera el resumen completo del carro en HTML.
		 * COMBINA la ficha del padre con datos propios del carro.
		 *
		 * Flujo:
		 * 1. parent::crear_ficha() genera las filas de nombre, velocidad, combustible
		 * 2. Se agrega una fila adicional con numero_puertas
		 * 3. Se retorna el HTML completo
		 */
		// declaracion de metodo
		public function resumenCarro(){
			// sobreescribitura de metodo crear_ficha en la clse padre
			// Obtenemos la ficha base del padre (3 filas de tabla)
			$mensaje=parent::crear_ficha();
			// .= agrega al final: sumamos la fila de numero de puertas
			$mensaje.='<tr>
						<td>Numero de puertas:</td>
						<td>'. $this->numero_puertas.'</td>
					</tr>';
			return $mensaje;
		}
	}

// ==========================================================================
// LOGICA PRINCIPAL: Procesar el formulario y crear el objeto apropiado
// ==========================================================================

$mensaje='';

if (!empty($_POST)){
	//declaracion de un operador switch
	// switch evalua el valor de $_POST['tipo_transporte'] y ejecuta
	// el case que coincida. Cada case crea un objeto diferente.
	//
	// NOTA: Los datos estan "hardcodeados" (escritos fijo en el codigo).
	// En un proyecto real, vendrian del formulario o de una base de datos.
	switch ($_POST['tipo_transporte']) {
		case 'aereo':
			//creacion del objeto con sus respectivos parametros para el constructor
			// new avion() llama: avion::__construct -> parent::__construct
			$jet1= new avion('jet','400','gasoleo','2');
			$mensaje=$jet1->resumenAvion();
			break;  // IMPORTANTE: sin break, PHP ejecutaria tambien el case 'terrestre'
		case 'terrestre':
			$carro1= new carro('carro','200','gasolina','4');
			$mensaje=$carro1->resumenCarro();
			break;
		case 'maritimo':
			$bergantin1= new barco('bergantin','40','na','15');
			$mensaje=$bergantin1->resumenBarco();
			break;
		case 'bicicleta':
			$bicicleta1= new bicicleta('bicicleta','20','pedales','26');
			$mensaje=$bicicleta1->resumenBicicleta();
	}

}

?>

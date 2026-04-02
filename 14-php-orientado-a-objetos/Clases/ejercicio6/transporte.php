<?php
/**
 * ==========================================================================
 * EJERCICIO 6: HERENCIA - CLASE PADRE "TRANSPORTE"
 * ==========================================================================
 *
 * PROGRESION:
 * Ejercicios 1-5: Clases independientes (cada una con su propia estructura)
 * Ejercicio 6:    HERENCIA - clases que comparten y extienden funcionalidad
 *
 * CONCEPTOS CLAVE:
 * ----------------
 *
 * 1. QUE ES LA HERENCIA:
 *    Es un mecanismo de OOP que permite crear una clase NUEVA basada en
 *    una clase EXISTENTE. La clase nueva (hija) HEREDA las propiedades
 *    y metodos de la clase existente (padre).
 *
 *    Analogia con biologia:
 *    - Un hijo hereda caracteristicas de sus padres (color de ojos, etc.)
 *    - Pero tambien tiene sus propias caracteristicas unicas
 *
 *    JERARQUIA DE ESTE EJERCICIO:
 *
 *                    transporte          <- CLASE PADRE (base)
 *                   /    |    \    \
 *                  /     |     \    \
 *              carro   avion  barco  bicicleta   <- CLASES HIJAS
 *
 *    Todos los transportes tienen: nombre, velocidad_max, tipo_combustible
 *    Cada uno agrega sus propias propiedades:
 *    - carro: numero_puertas
 *    - avion: numero_turbinas
 *    - barco: calado
 *    - bicicleta: rodada, modelo
 *
 * 2. CLASE PADRE (SUPERCLASE / BASE):
 *    Es la clase que contiene las propiedades y metodos COMUNES.
 *    En este caso, 'transporte' tiene lo que TODOS los transportes comparten.
 *    Las clases hijas NO necesitan redefinir estas propiedades comunes.
 *
 * 3. POR QUE USAR HERENCIA:
 *    SIN herencia, cada clase repetiria las mismas propiedades:
 *
 *    class carro {                    class avion {
 *        private $nombre;                 private $nombre;       <- DUPLICADO
 *        private $velocidad_max;          private $velocidad_max; <- DUPLICADO
 *        private $tipo_combustible;       private $tipo_combustible; <- DUPLICADO
 *        private $puertas;                private $turbinas;
 *    }                                }
 *
 *    CON herencia, lo comun va en la clase padre:
 *    class transporte { $nombre, $velocidad_max, $tipo_combustible }
 *    class carro extends transporte { $puertas }  // Hereda las 3 de arriba
 *
 *    Ventajas: codigo DRY (Don't Repeat Yourself), facil mantenimiento,
 *    cambiar algo en transporte afecta a TODAS las clases hijas.
 *
 * 4. CONSTRUCTOR EN LA CLASE PADRE:
 *    El constructor de transporte inicializa las propiedades comunes.
 *    Las clases hijas llamaran a este constructor con parent::__construct()
 *    para no duplicar el codigo de inicializacion.
 */

//declaracion de clase padre transporte
	class transporte{
		//declaracion de atributos
		// Son private: solo accesibles desde ESTA clase (transporte)
		// Las clases hijas NO pueden acceder directamente a estas propiedades
		// (para eso se necesitaria 'protected', que veremos en el ejercicio 7)
		// Sin embargo, las hijas pueden usar el metodo crear_ficha() que SI tiene acceso
		private $nombre;
		private $velocidad_max;
		private $tipo_combustible;

		/**
		 * CONSTRUCTOR de la clase padre.
		 * Recibe los 3 parametros comunes a todo transporte.
		 * Las clases hijas llamaran a este constructor con:
		 *   parent::__construct($nom, $vel, $com)
		 *
		 * @param string $nom Nombre del transporte
		 * @param string $vel Velocidad maxima
		 * @param string $com Tipo de combustible
		 */
		//declaracion de metodo constructor
		public function __construct($nom,$vel,$com){
			$this->nombre=$nom;
			$this->velocidad_max=$vel;
			$this->tipo_combustible=$com;
		}

		/**
		 * Genera una ficha HTML con los datos comunes del transporte.
		 * Este metodo es PUBLIC, asi que las clases hijas pueden llamarlo
		 * usando parent::crear_ficha() para EXTENDER la ficha con sus
		 * propios datos adicionales.
		 *
		 * Retorna HTML (filas de tabla) en vez de imprimirlo directamente,
		 * lo que permite a las hijas agregar mas filas antes de mostrarlo.
		 *
		 * @return string HTML con filas de tabla (<tr>) con los datos comunes
		 */
		//Este metodo genera un ficha en html
		public function crear_ficha(){
			// Construimos HTML usando concatenacion de cadenas
			// Cada <tr> es una fila de tabla con dos columnas: etiqueta y valor
			$ficha='
					<tr>
						<td>Nombre:</td>
						<td>'. $this->nombre.'</td>
					</tr>
					<tr>
						<td>Velocidad máxima:</td>
						<td>'. $this->velocidad_max.'</td>
					</tr>
					<tr>
						<td>Tipo de combustible:</td>
						<td>'. $this->tipo_combustible.'</td>
					</tr>';

			return $ficha;
		}

	}


?>

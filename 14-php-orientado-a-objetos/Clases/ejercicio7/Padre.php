<?php
/**
 * ==========================================================================
 * EJERCICIO 7: HERENCIA MULTINIVEL - CLASE "PADRE" (NIVEL INTERMEDIO)
 * ==========================================================================
 *
 * CONCEPTOS CLAVE:
 * ----------------
 *
 * 1. HERENCIA DE ABUELO:
 *    Padre extiende Abuelo, lo que significa que Padre TIENE:
 *    - De Abuelo (protected): $nombreAbuelo, $apellido_paterno, $apellido_materno
 *    - De Abuelo (protected): crear_ficha()
 *    - Propias: $nombrePadre, resumenPadre()
 *
 * 2. ACCESO A PROPIEDADES HEREDADAS PROTECTED:
 *    Padre puede acceder DIRECTAMENTE a $this->apellido_paterno
 *    aunque esta definida en Abuelo. Esto es posible porque:
 *    - La propiedad es protected (no private)
 *    - Padre hereda de Abuelo (extends)
 *
 *    Si $apellido_paterno fuera private en Abuelo:
 *    $this->apellido_paterno  // ERROR: no accesible desde Padre
 *
 * 3. CADENA DE HERENCIA:
 *    Cuando Hijo herede de Padre, Hijo tendra acceso a:
 *    - Todo lo protected/public de Abuelo (heredado a traves de Padre)
 *    - Todo lo protected/public de Padre (heredado directamente)
 *    - Sus propias propiedades y metodos
 *
 *    Es como una cadena: Abuelo -> Padre -> Hijo
 *    Cada eslabon pasa sus propiedades protected al siguiente.
 *
 * 4. CLASE INTERMEDIA:
 *    Padre es una clase "intermedia" en la cadena:
 *    - Es HIJA de Abuelo (hereda de el)
 *    - Es PADRE de Hijo (le pasa herencia)
 *    - Puede acceder a todo lo de Abuelo via $this->
 *    - Todo lo que defina como protected sera accesible por Hijo
 */

// Incluimos la clase Abuelo para poder heredar de ella
include_once('Abuelo.php');

//declara una clase Padres que extienda Abuelos
	class Padre extends Abuelo{

		// Propiedad propia de Padre, tambien protected para que Hijo pueda accederla
		protected $nombrePadre='Jorge';

		/**
		 * Genera la ficha del padre.
		 * Accede a $this->apellido_paterno que viene de ABUELO (herencia).
		 * Esto demuestra que protected permite el acceso entre generaciones.
		 *
		 * NOTA: $this->apellido_paterno fue definida en Abuelo como protected.
		 * Padre puede usarla como si fuera suya gracias a la herencia.
		 *
		 * @return string HTML con fila de tabla del padre
		 */
		public function resumenPadre(){
			// $this->nombrePadre: propiedad PROPIA de Padre
			// $this->apellido_paterno: propiedad HEREDADA de Abuelo (protected)
			$fichaPadre='<tr>
						<td>Padre:</td>
						<td>'. $this->nombrePadre.' '.$this->apellido_paterno.'</td>
					</tr>
					';
			return $fichaPadre;
		}
	}



?>

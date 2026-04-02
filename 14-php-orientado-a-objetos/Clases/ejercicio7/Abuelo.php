<?php
/**
 * ==========================================================================
 * EJERCICIO 7: HERENCIA MULTINIVEL + PROTECTED - CLASE "ABUELO"
 * ==========================================================================
 *
 * PROGRESION:
 * Ejercicio 6: Herencia simple (padre -> hijo, 1 nivel)
 * Ejercicio 7: Herencia MULTINIVEL (abuelo -> padre -> hijo, 2+ niveles)
 *              + Modificador PROTECTED
 *
 * CONCEPTOS CLAVE:
 * ----------------
 *
 * 1. HERENCIA MULTINIVEL:
 *    Una clase puede heredar de otra que a su vez hereda de otra.
 *    Esto crea una CADENA de herencia:
 *
 *    Abuelo     <- Clase base (raiz de la cadena)
 *      |
 *    Padre      <- Hereda de Abuelo (tiene todo lo de Abuelo + lo suyo)
 *      |
 *    Hijo       <- Hereda de Padre (tiene todo lo de Abuelo + Padre + lo suyo)
 *
 *    Hijo tiene acceso a las propiedades/metodos protected de Abuelo
 *    Y tambien a los de Padre. La herencia es ACUMULATIVA.
 *
 * 2. PROTECTED - EL MODIFICADOR "INTERMEDIO":
 *    protected es el punto medio entre public y private:
 *
 *    +-------------+-------------------+-------------------+-------------------+
 *    | Modificador | Misma clase       | Clase hija        | Codigo externo    |
 *    +-------------+-------------------+-------------------+-------------------+
 *    | public      | SI puede acceder  | SI puede acceder  | SI puede acceder  |
 *    | protected   | SI puede acceder  | SI puede acceder  | NO puede acceder  |
 *    | private     | SI puede acceder  | NO puede acceder  | NO puede acceder  |
 *    +-------------+-------------------+-------------------+-------------------+
 *
 *    ANALOGIA:
 *    - public:    Como la puerta de tu casa (cualquiera puede tocar)
 *    - protected: Como el album familiar (solo familia puede verlo)
 *    - private:   Como tu diario personal (solo tu puedes leerlo)
 *
 * 3. POR QUE PROTECTED Y NO PRIVATE:
 *    En el Ejercicio 6, transporte usaba private, y las clases hijas
 *    no podian acceder directamente a $nombre, $velocidad, etc.
 *    Solo podian acceder a traves de metodos publicos (crear_ficha).
 *
 *    En este Ejercicio 7, Abuelo usa protected, lo que permite que
 *    Padre e Hijo accedan DIRECTAMENTE a $nombreAbuelo, $apellido_paterno, etc.
 *
 *    Usar protected cuando: Las clases hijas NECESITAN acceso directo
 *    Usar private cuando: Solo la propia clase debe manipular los datos
 *
 * 4. VALORES POR DEFECTO EN PROPIEDADES:
 *    protected $nombreAbuelo = 'Nemesio';
 *    Esto asigna un valor inicial a la propiedad SIN necesidad de constructor.
 *    Todos los objetos de esta clase (y sus hijas) empiezan con este valor.
 */

//declaracion de clase Abuelos
	class Abuelo{
		//declaracion de atributos protected
		// protected: accesible desde esta clase Y desde clases hijas (Padre, Hijo)
		// Pero NO accesible desde codigo externo ($abuelo->nombreAbuelo seria ERROR)
		//
		// Se inicializan con valores por defecto directamente en la declaracion
		// No se necesita constructor para asignar estos valores
		protected $nombreAbuelo='Nemesio';
		protected $apellido_paterno='Martinez';
		protected $apellido_materno='Dominguez';

		/**
		 * Metodo PROTECTED para crear la ficha del abuelo.
		 * Es protected porque:
		 * - Las clases hijas (Padre, Hijo) pueden llamarlo
		 * - El codigo externo NO puede llamarlo directamente
		 *
		 * NOTA: En el Ejercicio 6, crear_ficha() era public.
		 * Aqui es protected para demostrar la diferencia.
		 * Hijo::resumenHijo() puede llamar parent::crear_ficha()
		 * pero desde fuera, $abuelo->crear_ficha() daria error.
		 *
		 * @return string HTML con fila de tabla del abuelo
		 */
		protected function crear_ficha(){
			// $this->nombreAbuelo accede a la propiedad protected
			// Concatenamos nombre + apellidos para mostrar el nombre completo
			$fichaAbuelo='
					<tr>
						<td>Abuelo:</td>
						<td>'. $this->nombreAbuelo.' '. $this->apellido_paterno.'
						'. $this->apellido_materno.'</td>
					</tr>';

			return $fichaAbuelo;
		}

	}



?>

<?php  
//declaracion de clase Abuelos
	class Abuelo{
		//declaracion de atributos protected
		protected $nombreAbuelo='Nemesio';
		protected $apellido_paterno='Martinez';
		protected $apellido_materno='Dominguez';

		protected function crear_ficha(){
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

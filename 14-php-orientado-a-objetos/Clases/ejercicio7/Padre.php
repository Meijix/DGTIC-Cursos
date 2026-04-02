<?php  
include_once('Abuelo.php');

//declara una clase Padres que extienda Abuelos
	class Padre extends Abuelo{

		protected $nombrePadre='Jorge';

		public function resumenPadre(){
			$fichaPadre='<tr>
						<td>Padre:</td>
						<td>'. $this->nombrePadre.' '.$this->apellido_paterno.'</td>				
					</tr>
					';
			return $fichaPadre;
		}
	}



?>

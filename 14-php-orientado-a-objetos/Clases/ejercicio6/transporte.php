<?php  
//declaracion de clase padre transporte
	class transporte{
		//declaracion de atributos
		private $nombre;
		private $velocidad_max;
		private $tipo_combustible;

		//declaracion de metodo constructor
		public function __construct($nom,$vel,$com){
			$this->nombre=$nom;
			$this->velocidad_max=$vel;
			$this->tipo_combustible=$com;
		}

		//Este metodo genera un ficha en html
		public function crear_ficha(){
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

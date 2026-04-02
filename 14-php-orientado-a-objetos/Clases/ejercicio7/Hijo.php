<?php  
include_once('Padre.php');

//declara una clase Hijo que extienda Padres
	class Hijo extends Padre{

		protected $nombre;

		public function __construct($nombre){
			$this->nombre=$nombre;
		}

		public function resumenHijo(){
			$resumen=parent::crear_ficha();
			$resumen.=$this->resumenPadre();
			$resumen.='<tr>
						<td>Hijo:</td>
						<td>'. $this->nombre.' '.$this->apellido_paterno.'</td>				
					</tr>
					';
			return $resumen;
		}
	
	}

$mensaje='';

if (!empty($_POST)){
	//creacion de objeto de la clase

	$hijo1= new Hijo($_POST['nombre']);
	$mensaje=$hijo1->resumenHijo();
}


?>

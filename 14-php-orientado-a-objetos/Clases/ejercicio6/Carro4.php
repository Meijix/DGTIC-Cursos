<?php  
include_once('transporte.php');
include_once('bicicleta.php');
include_once('barco.php');
include_once('avion.php');


	//declaracion de la clase hijo o subclase Carro
	class carro extends transporte{

		private $numero_puertas;

		//declaracion de constructor
		public function __construct($nom,$vel,$com,$pue){
			//sobreescritura de constructor de la clase padre
			parent::__construct($nom,$vel,$com);
			$this->numero_puertas=$pue;
				
		}

		// declaracion de metodo
		public function resumenCarro(){
			// sobreescribitura de metodo crear_ficha en la clse padre
			$mensaje=parent::crear_ficha();
			$mensaje.='<tr>
						<td>Numero de puertas:</td>
						<td>'. $this->numero_puertas.'</td>				
					</tr>';
			return $mensaje;
		}
	} 

$mensaje='';


if (!empty($_POST)){
	//declaracion de un operador switch
	switch ($_POST['tipo_transporte']) {
		case 'aereo':
			//creacion del objeto con sus respectivos parametros para el constructor
			$jet1= new avion('jet','400','gasoleo','2');
			$mensaje=$jet1->resumenAvion();
			break;
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

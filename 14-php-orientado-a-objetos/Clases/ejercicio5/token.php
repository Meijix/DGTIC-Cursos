<?php  
//declaracion de clase token
	class token{
		//declaracion de atributos
		private $nombre;
		private $token;
		//declaracion de metodo constructor
		public function __construct($nombre_front){
			$this->nombre=$nombre_front;
			$this->token=rand();
		}

		//declaracion del metodo mostrar para armar el mensaje con el nombre y token
		public function mostrar(){
			return 'Hola '.$this->nombre.' este es tu token: '.$this->token;
		}

		//declaracion de metodo destructor
		public function __destruct(){
			//destruye token
			$this->token='El token ha sido destruido';
			echo $this->token;
		}
	}

$mensaje='';


if (!empty($_POST)){
	//creacion de objeto de la clase
	$token1= new token($_POST['nombre']);
	$mensaje=$token1->mostrar();
}


?>

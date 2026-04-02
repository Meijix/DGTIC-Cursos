<?php

class Rfc{

	//declara un atributo private de tipo arreglo para los datos	
	private $datos=array();

	//declara un metodo public para guardar los datos en el atributo private
	public function guardar($datos){
		
		$this->datos=$datos;
		
	}

	//declara un metodo private para generar el rfc con los datos de atributo y retornalo con un return
	private function construir(){
		
			return $this->datos['nombre'];
		
	}

}
$mensaje='';

//crea un objeto instanciado a la calse Rfc
$Rfc1 = new Rfc;

//si existe solicitudes POST entonces guarda dichos datos en un arreglo que se declare de forma asociativa 
if ( !empty($_POST)){

	$datos_front = [
		'nombre' => $_POST['nombre'],
		'paterno'=> $_POST['paterno'],
		'materno'=> $_POST['materno'],
		'fecha'=> $_POST['fecha']
	];

	//usa el metodo para guardar poniendo al arreglo como parametro
	$Rfc1->guardar($datos_front);
	$mensaje=$Rfc1->construir();

}  

?>

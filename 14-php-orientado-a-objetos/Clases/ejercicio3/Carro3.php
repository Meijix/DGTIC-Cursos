<?php
//creación de la clase carro
class Carro3{
	//declaracion de propiedades
	private $placas;
	

	//declaracion del método verificación
	public function registrar_placas($placas){
		$this->placas=$placas;
	}

	public function mostrar_placas(){
		echo $this->placas;
	}
}

//creación de instancia a la clase Carro
$Carro1 = new Carro3();

if (!empty($_POST)){
	//$Carro1->placas=$_POST['placas'];
	$Carro1->registrar_placas($_POST['placas']);
}

?>


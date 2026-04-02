<?php
//creación de la clase carro
class Carro2{
	//declaracion de propiedades
	public $color;
	public $modelo;
	public $year;
	private $verificado;

	public function __construct() {
		$this->color = "";
		$this->modelo = "";
		$this->year = 0;
		$this->verificado = "";
	}
	
	public function getVerificado() {
		return $this->verificado;
    }
	
	public function setVerificado($verificado) {
		$this->verificado = $verificado;
    }
	//declaracion del método verificación
	//se verificará mediante el año de fabricación del carro si circula o no guiándose por la tabla.
	public function verificacion() {
		$year = $this->year;
		if ($year >= 2010) {
			$this->setVerificado("Circula");
		} elseif ($year < 2010 && $year >= 1990) {
			$this->setVerificado("Revision");
		} else {
			$this->setVerificado("No circula");
		}
	}
}

//creación de instancia a la clase Carro
$Carro1 = new Carro2();
$Carro1->verificacion();

if (!empty($_POST)){
	$Carro1->color=$_POST['color'];
	$Carro1->modelo=$_POST['modelo'];
	$Carro1->year=$_POST['year'];
}





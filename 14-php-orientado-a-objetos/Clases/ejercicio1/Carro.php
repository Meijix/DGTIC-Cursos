<?php

class Carro{
	//declaracion de propiedades
	public $color;
	public $marca;
}

//inicializamos el mensaje que lanzara el servidor con vacio
$mensajeServidor='';

//se instancia la clase Carro
$Carro1 = new Carro;

//verifica si se ha enviado una petición POST
 if ( !empty($_POST)){

 	//almacenamos el valor mandado por POST en el atributo color
 	$Carro1->color=$_POST['color'];
 	//se construye el mensaje que sera lanzado por el servidor
 	$mensajeServidor='el servidor dice que ya escogiste un color: '.$_POST['color'];
 }  


?>

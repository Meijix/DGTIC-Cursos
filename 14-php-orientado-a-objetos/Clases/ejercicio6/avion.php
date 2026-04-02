<?php
include_once('transporte.php');

class avion extends transporte{

private $numero_turbinas;

//sobreescritura de constructor
public function __construct($nom,$vel,$com,$tur){
    parent::__construct($nom,$vel,$com);
    $this->numero_turbinas=$tur;
}

// sobreescritura de metodo
public function resumenAvion(){
    $mensaje=parent::crear_ficha();
    $mensaje.='<tr>
                <td>Numero de turbinas:</td>
                <td>'. $this->numero_turbinas.'</td>				
            </tr>';
    return $mensaje;
}
}
?>
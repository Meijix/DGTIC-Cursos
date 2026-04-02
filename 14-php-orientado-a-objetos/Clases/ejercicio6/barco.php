<?php
include_once('transporte.php');

class barco extends transporte{
    private $calado;

    //sobreescritura de constructor
    public function __construct($nom,$vel,$com,$cal){
        parent::__construct($nom,$vel,$com);
        $this->calado=$cal;
    }

    // sobreescritura de metodo
    public function resumenBarco(){
        $mensaje=parent::crear_ficha();
        $mensaje.='<tr>
                    <td>Calado:</td>
                    <td>'. $this->calado.'</td>				
                </tr>';
        return $mensaje;
    }
}

?>
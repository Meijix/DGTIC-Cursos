<?php
include_once('transporte.php');

class bicicleta extends transporte{

    private $rodada;
    private $modelo;

    //sobreescritura de constructor
    public function __construct($nom,$vel,$com,$tur){
        parent::__construct($nom,$vel,$com);
        $this->modelo=$tur;
        $this->rodada=$com;
    }

    // sobreescritura de metodo
    public function resumenBicicleta(){
        $mensaje=parent::crear_ficha();
        $mensaje.='
                <tr>
                    <td>Modelo:</td>
                    <td>'. $this->modelo.'</td>
                    </tr>
                ';
        return $mensaje;
    }
}
?>
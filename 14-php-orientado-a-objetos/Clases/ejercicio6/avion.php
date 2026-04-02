<?php
/**
 * ==========================================================================
 * EJERCICIO 6: HERENCIA - CLASE HIJA "AVION"
 * ==========================================================================
 *
 * CONCEPTOS CLAVE:
 * ----------------
 *
 * 1. PATRON REPETIDO EN TODAS LAS CLASES HIJAS:
 *    Todas las clases hijas del ejercicio 6 siguen el mismo patron:
 *
 *    a) extends transporte                         -> Heredan de la misma clase padre
 *    b) Propiedad private propia                   -> Dato especifico de esta clase
 *    c) Constructor con parent::__construct()       -> Inicializan padre + propio
 *    d) Metodo resumenX() con parent::crear_ficha() -> Ficha padre + datos propios
 *
 *    Este patron demuestra como la herencia permite REUTILIZAR codigo.
 *    Si transporte tuviera 20 propiedades, no tendriamos que repetirlas
 *    en cada clase hija.
 *
 * 2. ESPECIALIZACION:
 *    avion agrega $numero_turbinas, algo que solo tiene sentido para aviones.
 *    Un carro no tiene turbinas, un barco no tiene turbinas.
 *    Cada clase hija SE ESPECIALIZA en un tipo particular de transporte.
 *
 *    Esto refleja la realidad: un avion ES UN transporte, pero tambien
 *    tiene caracteristicas que otros transportes no tienen.
 */

include_once('transporte.php');

// 'extends transporte' -> avion hereda de transporte
class avion extends transporte{

// Propiedad PROPIA: solo los aviones tienen turbinas
private $numero_turbinas;

/**
 * Constructor: inicializa datos del padre + dato propio.
 *
 * @param string $nom Nombre del avion
 * @param string $vel Velocidad maxima
 * @param string $com Tipo de combustible
 * @param string $tur Numero de turbinas (propio de avion)
 */
//sobreescritura de constructor
public function __construct($nom,$vel,$com,$tur){
    // parent:: accede a la clase padre (transporte)
    // parent::__construct() llama al constructor de transporte
    parent::__construct($nom,$vel,$com);
    $this->numero_turbinas=$tur;
}

/**
 * Genera el resumen del avion: ficha comun + numero de turbinas.
 *
 * @return string HTML con todas las filas de la tabla
 */
// sobreescritura de metodo
public function resumenAvion(){
    // Obtenemos la ficha base (nombre, velocidad, combustible)
    $mensaje=parent::crear_ficha();
    // Agregamos la fila especifica del avion
    $mensaje.='<tr>
                <td>Numero de turbinas:</td>
                <td>'. $this->numero_turbinas.'</td>
            </tr>';
    return $mensaje;
}
}
?>

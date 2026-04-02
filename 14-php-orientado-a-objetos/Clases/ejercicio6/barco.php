<?php
/**
 * ==========================================================================
 * EJERCICIO 6: HERENCIA - CLASE HIJA "BARCO"
 * ==========================================================================
 *
 * CONCEPTOS CLAVE:
 * ----------------
 *
 * 1. MISMA ESTRUCTURA QUE AVION Y BICICLETA:
 *    Todas las clases hijas siguen el mismo patron de herencia.
 *    barco agrega $calado (profundidad que alcanza bajo el agua),
 *    una propiedad que solo tiene sentido para embarcaciones.
 *
 * 2. CALADO:
 *    Es la profundidad a la que se sumerge un barco en el agua.
 *    Mide desde la linea de flotacion hasta la parte mas baja del casco.
 *    Ejemplo: un barco con calado de 15 metros necesita aguas de al menos
 *    15 metros de profundidad para navegar sin tocar el fondo.
 *
 * 3. VENTAJA DE LA HERENCIA EN ESTE EJEMPLO:
 *    Si quisieramos agregar una nueva propiedad a TODOS los transportes
 *    (por ejemplo, $peso), solo la agregariamos en la clase transporte.
 *    Todas las clases hijas (carro, avion, barco, bicicleta) la heredarian
 *    automaticamente sin modificar ningun otro archivo.
 */

include_once('transporte.php');

// barco hereda de transporte: tiene nombre, velocidad, combustible + calado
class barco extends transporte{
    // Propiedad PROPIA: el calado solo aplica a embarcaciones
    private $calado;

    /**
     * Constructor: padre + dato propio.
     *
     * @param string $nom Nombre del barco
     * @param string $vel Velocidad maxima
     * @param string $com Tipo de combustible ("na" = no aplica para veleros)
     * @param string $cal Calado en metros
     */
    //sobreescritura de constructor
    public function __construct($nom,$vel,$com,$cal){
        parent::__construct($nom,$vel,$com);
        $this->calado=$cal;
    }

    /**
     * Genera el resumen del barco: ficha comun + calado.
     *
     * @return string HTML con filas de tabla
     */
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

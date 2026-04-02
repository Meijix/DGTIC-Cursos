<?php
/**
 * ==========================================================================
 * EJERCICIO 6: HERENCIA - CLASE HIJA "BICICLETA"
 * ==========================================================================
 *
 * CONCEPTOS CLAVE:
 * ----------------
 *
 * 1. HERENCIA DE transporte:
 *    bicicleta extiende transporte, asi que hereda:
 *    - Propiedades: nombre, velocidad_max, tipo_combustible
 *    - Metodos: __construct(), crear_ficha()
 *
 *    Y agrega sus propias propiedades: $rodada y $modelo
 *
 * 2. SOBREESCRITURA DE CONSTRUCTOR:
 *    bicicleta tiene su propio __construct() que:
 *    a) Llama a parent::__construct() para inicializar propiedades del padre
 *    b) Inicializa sus propias propiedades ($modelo y $rodada)
 *
 *    Sin parent::__construct(), las propiedades heredadas NO se inicializarian
 *    y crear_ficha() mostraria valores vacios.
 *
 * 3. CADA CLASE HIJA ES INDEPENDIENTE:
 *    bicicleta, avion, barco y carro heredan la misma base pero cada una
 *    agrega su propia especializacion. Este es el poder de la herencia:
 *    codigo comun reutilizado + especializacion por clase.
 *
 *    VISUALIZACION:
 *    transporte:  [nombre] [velocidad] [combustible]
 *    bicicleta:   [nombre] [velocidad] [combustible] + [modelo] [rodada]
 *    avion:       [nombre] [velocidad] [combustible] + [turbinas]
 *    barco:       [nombre] [velocidad] [combustible] + [calado]
 */

// include_once previene doble inclusion de transporte.php
// (Carro4.php tambien lo incluye, pero include_once lo carga solo 1 vez)
include_once('transporte.php');

class bicicleta extends transporte{

    // Propiedades PROPIAS de bicicleta (no las tienen carro, avion, etc.)
    private $rodada;
    private $modelo;

    /**
     * Constructor de bicicleta.
     * Recibe 4 parametros: 3 para el padre + 1 propio.
     *
     * @param string $nom Nombre
     * @param string $vel Velocidad maxima
     * @param string $com Tipo de combustible (en este caso "pedales")
     * @param string $tur Modelo de la bicicleta (parametro reutilizado)
     */
    //sobreescritura de constructor
    public function __construct($nom,$vel,$com,$tur){
        // Llamamos al constructor padre para inicializar nombre, velocidad, combustible
        parent::__construct($nom,$vel,$com);
        $this->modelo=$tur;
        $this->rodada=$com;
    }

    /**
     * Genera el resumen de la bicicleta combinando ficha padre + datos propios.
     * Mismo patron que resumenCarro(), resumenAvion(), etc.
     *
     * @return string HTML con filas de tabla
     */
    // sobreescritura de metodo
    public function resumenBicicleta(){
        // parent::crear_ficha() retorna las filas comunes (nombre, velocidad, combustible)
        $mensaje=parent::crear_ficha();
        // .= agrega la fila del modelo al final
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

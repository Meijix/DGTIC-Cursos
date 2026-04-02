<?php
/**
 * ==========================================================================
 * VISTA DEL EJERCICIO 1: INCLUSION DE CLASES
 * ==========================================================================
 *
 * CONCEPTOS CLAVE:
 * ----------------
 *
 * 1. require_once:
 *    Incluye un archivo PHP externo y ejecuta su codigo.
 *    - require: Si el archivo NO existe, produce un ERROR FATAL (detiene PHP)
 *    - include: Si el archivo NO existe, produce un WARNING (sigue ejecutando)
 *    - _once: Asegura que el archivo se incluya UNA SOLA VEZ
 *             (evita errores de redefinicion de clases)
 *
 *    Cuando hacemos require_once 'Carro.php':
 *    - Se ejecuta TODO el codigo de Carro.php
 *    - La clase Carro queda disponible para usar
 *    - Las variables $Carro1 y $mensajeServidor quedan disponibles
 *    - Es como si el contenido de Carro.php se "pegara" aqui
 *
 * 2. ORGANIZACION DE ARCHIVOS:
 *    Este archivo demuestra la separacion de responsabilidades:
 *    - Carro.php: Define la CLASE y su logica
 *    - Moto.php: Define la CLASE Moto (con su propia vista integrada)
 *    - vista.php: Simplemente incluye ambas clases
 *
 *    Esta separacion facilita el mantenimiento: si necesitas cambiar
 *    la clase Carro, solo editas Carro.php.
 */

// Incluimos los archivos de las clases
// require_once asegura que cada archivo se cargue exactamente una vez
// Al incluir Moto.php, su HTML tambien se renderiza (porque Moto.php tiene HTML)
require_once 'Moto.php';
require_once 'Carro.php';
?>

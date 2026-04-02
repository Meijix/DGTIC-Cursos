<?php
/**
 * ==========================================================================
 * ARCHIVO DE DATOS DE USUARIOS PRECARGADOS
 * ==========================================================================
 *
 * PROPOSITO:
 * Este archivo simula una "base de datos" usando la variable de sesion.
 * En un proyecto real, estos datos estarian en una base de datos (MySQL,
 * PostgreSQL, etc.) y se consultarian con SQL.
 *
 * CONCEPTOS CLAVE:
 * ----------------
 *
 * 1. ARRAYS ASOCIATIVOS EN PHP:
 *    A diferencia de los arrays numericos [0, 1, 2], los arrays asociativos
 *    usan CLAVES CON NOMBRE (como los diccionarios de Python).
 *
 *    Sintaxis: $array = ['clave' => 'valor', 'otra_clave' => 'otro_valor'];
 *    Acceso:   $array['clave'] retorna 'valor'
 *
 *    Equivalencia con Python:
 *    PHP:    $datos = ['nombre' => 'Juan', 'edad' => 20];
 *    Python: datos = {'nombre': 'Juan', 'edad': 20}
 *
 * 2. ARRAYS MULTIDIMENSIONALES:
 *    Un array puede contener otros arrays. Aqui tenemos:
 *    $_SESSION['alumnosRegistrados'] = [
 *        1 => [...],           // Alumno 1 (array asociativo)
 *        317737822 => [...]    // Alumno 2 (array asociativo)
 *    ]
 *
 *    Para acceder al nombre del alumno 1:
 *    $_SESSION['alumnosRegistrados'][1]['nombre'] -> "Admin"
 *
 * 3. CLAVES NUMERICAS COMO IDENTIFICADORES:
 *    Usamos el numero de cuenta como clave del array.
 *    Esto permite buscar un alumno DIRECTAMENTE por su numero de cuenta:
 *    $_SESSION['alumnosRegistrados'][317737822] -> datos de Natalia
 *
 *    Es mas eficiente que recorrer todo el array buscando el numero.
 *
 * 4. $_SESSION:
 *    Variable superglobal que persiste entre peticiones HTTP.
 *    Los datos guardados aqui sobreviven mientras la sesion este activa.
 *    Se almacenan en archivos temporales del servidor (generalmente en /tmp).
 *
 * NOTA DE SEGURIDAD IMPORTANTE:
 * Las contrasenas NUNCA deben almacenarse en texto plano.
 * En produccion se debe usar:
 *   password_hash('admin123', PASSWORD_DEFAULT)  -> para guardar
 *   password_verify($input, $hash)                -> para verificar
 *
 * NOTA: Este archivo se incluye con include_once/require_once en las demas
 * paginas. Cada vez que se carga, SOBREESCRIBE los datos de la sesion con
 * estos valores iniciales. Esto es intencional para fines didacticos.
 */

$_SESSION['alumnosRegistrados'] = [
    // Primer usuario precargado: Administrador
    // La clave 1 es el numero de cuenta
    1 => [
        'num_cta' => 1,
        'nombre' => "Admin",
        "primer_apellido" => "General",
        "segundo_apellido" => "General2",
        "genero" => "O",
        "contrasena" => "admin123",
        "fecha_nac" => "2020-01-01"
    ],
    //Agregar otro usuario precargado
    // La clave 317737822 es el numero de cuenta (permite acceso directo)
    317737822 => [
        'num_cta' => 317737822,
        'nombre' => "Natalia",
        "primer_apellido" => "Mejia",
        "segundo_apellido" => "Bautista",
        "genero" => "O",
        "contrasena" => "naty123",
        "fecha_nac" => "2020-08-30"
    ]
];

/* print_r($_SESSION); */

?>

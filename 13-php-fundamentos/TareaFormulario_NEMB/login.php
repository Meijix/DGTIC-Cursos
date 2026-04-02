<!--
=============================================================================
LOGIN (INICIO DE SESION) CON PHP
=============================================================================

CONCEPTOS CLAVE EN ESTE ARCHIVO:
---------------------------------

1. AUTENTICACION:
   Proceso de verificar la identidad de un usuario. En este caso:
   - El usuario proporciona su numero de cuenta y contrasena
   - El servidor busca esos datos en la sesion
   - Si coinciden, el usuario esta "autenticado" y se le permite acceder

2. FLUJO DE LOGIN:
   Navegador: envia POST con num_cuenta y contrasena
       |
       v
   Servidor: session_start() recupera datos de $_SESSION
       |
       v
   Servidor: busca al alumno por num_cuenta en $_SESSION['alumnosRegistrados']
       |
       +---> Si coinciden: crea $_SESSION['login'] con datos del alumno
       |     y redirige a info.php con header('Location: ...')
       |
       +---> Si NO coinciden: muestra mensaje de error

3. OPERADOR TERNARIO:
   $resultado = (condicion) ? valor_si_true : valor_si_false;
   Es una forma compacta del if/else en una sola linea.

   En este archivo:
   isset($_SESSION['alumnosRegistrados'][$_POST['num_cuenta_ingresada']])
       ? $_SESSION['alumnosRegistrados'][$_POST['num_cuenta_ingresada']]
       : [];
   Equivale a:
   if (isset(...)) { $alumno = $_SESSION[...]; } else { $alumno = []; }

4. header('Location: ...'):
   Envia una cabecera HTTP de redireccion (codigo 302).
   El navegador recibe esta cabecera y automaticamente navega a la URL indicada.
   IMPORTANTE: Despues de header() SIEMPRE se debe poner exit() para detener
   la ejecucion del script. Sin exit(), PHP seguiria ejecutando codigo
   que podria mostrar datos no deseados.

5. exit():
   Detiene completamente la ejecucion del script PHP.
   Se usa despues de header('Location: ...') para asegurar que no se
   ejecute codigo posterior a la redireccion.

NOTA DE SEGURIDAD:
------------------
En un proyecto real:
- Las contrasenas se verifican con password_verify(), NO con comparacion directa
- Se usan tokens CSRF para evitar ataques de falsificacion de peticiones
- Se limita el numero de intentos de login (para evitar fuerza bruta)
- Se usa HTTPS para cifrar la comunicacion
-->

<?php

// include_once carga el archivo de datos de usuarios
// Se ejecuta ANTES de session_start() para que los datos esten disponibles
include_once 'usuario.php'; // Include the file where the user data is stored

// Inicia o reanuda la sesion. El servidor busca la cookie PHPSESSID
// enviada por el navegador y recupera los datos de $_SESSION asociados.
session_start(); // Start the session

/* print_r($_POST);  */
//print_r($_SESSION['alumnosRegistrados']);

// =========================================================================
// LOGICA DE AUTENTICACION
// =========================================================================

// Check if the form has been submitted
// isset($_POST['entrar']) verifica si el boton "Ingresar" fue presionado.
// El boton tiene name="entrar", asi que solo existe en $_POST cuando se envia el form.
if(isset($_POST['entrar'])) {

    // Buscar al alumno en la lista de alumnos registrados
    // Usamos el OPERADOR TERNARIO para buscar al alumno de forma segura:
    // Si el numero de cuenta existe en el array -> devuelve los datos del alumno
    // Si NO existe -> devuelve un array vacio []
    // Esto evita un error "Undefined index" si el num_cuenta no existe.
    $alumno = isset($_SESSION['alumnosRegistrados'][$_POST['num_cuenta_ingresada']]) ? $_SESSION['alumnosRegistrados'][$_POST['num_cuenta_ingresada']] : [];

    /* print_r($alumno); */

    // Verificamos TRES condiciones con el operador && (AND logico):
    // 1. $alumno != [] -> El alumno fue encontrado (no es array vacio)
    // 2. num_cuenta coincide con num_cta del alumno
    // 3. La contrasena ingresada coincide con la almacenada
    //
    // NOTA: En produccion, la comparacion de contrasenas debe usar
    // password_verify($ingresada, $hash_almacenado) en vez de ==
    if ($alumno!=[] && $_POST['num_cuenta_ingresada'] == $alumno['num_cta'] &&  $_POST['contrasena_ingresada'] == $alumno['contrasena']) {

        // CREACION DE LA SESION DE LOGIN:
        // Guardamos los datos del usuario autenticado en $_SESSION['login'].
        // Esta informacion estara disponible en TODAS las paginas que llamen
        // session_start() mientras la sesion siga activa.
        //
        // El operador punto (.) concatena las cadenas del nombre completo
        $_SESSION['login'] = [
            'nombre' => $alumno['nombre'] . ' ' . $alumno['primer_apellido'].' '.$alumno['segundo_apellido'],
            'num_cta' => $alumno['num_cta'],
            'fecha_nac' => $alumno['fecha_nac'],
        ];
        /* print_r($_SESSION['login']); */

        // REDIRECCION HTTP:
        // header('Location: info.php') envia al navegador la cabecera:
        //   HTTP/1.1 302 Found
        //   Location: info.php
        // El navegador automaticamente hace un GET a info.php
        header('Location: info.php');

        // exit() DETIENE la ejecucion del script inmediatamente.
        // Sin esto, PHP seguiria ejecutando el resto del archivo,
        // lo cual podria causar errores o mostrar contenido no deseado.
        exit(); // Ensure no further code is executed after redirection
    } else {
        // If the user is not found, display an error message
        // Se muestra un mensaje con la clase CSS 'error' para estilizarlo en rojo
        echo "<div class='error'> Error: Numero de cuenta no encontrado o contraseña incorrecta </div>";
    }
}
?>

<!-- =====================================================================
     FORMULARIO HTML DE LOGIN
     =====================================================================
     Este formulario permite al usuario ingresar sus credenciales.
     Los datos se envian al mismo archivo (action="login.php") por POST.
-->
<!DOCTYPE html>
<html lang="es">
<!-- Formulario de inicio de sesion -->

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="estilos.css">
    <title>Iniciar sesion</title>
</head>
<body>
    <div class="contenedor">
        <h1>Inicia sesion</h1>
        <p>Ingresa tu numero de cuenta y contraseña</p>

        <!-- method="POST" envia los datos de forma segura (en el cuerpo HTTP) -->
        <!-- action="login.php" envia los datos a este mismo archivo -->
        <form action="login.php" method="POST">

            <div class="contenedor-input">
            <label for="num_cuenta">Numero de cuenta:</label>
            <!-- name="num_cuenta_ingresada" -> se accede como $_POST['num_cuenta_ingresada'] -->
            <input class="caja" type="text" name="num_cuenta_ingresada" id="num_cuenta" placeholder='123123' required>
            </div>

            <div class="contenedor-input">
            <label for="password">Contraseña:</label>
            <!-- type="password" oculta los caracteres escritos -->
            <input class="caja" type="password" name="contrasena_ingresada" id="password" placeholder="Ingrese su contraseña" required>
            </div>

            <div class="contenedor-input">
            <!-- type="submit" con name="entrar" ->
                 Al presionar, se envia el formulario Y se agrega 'entrar' a $_POST.
                 Esto permite al PHP de arriba detectar que el formulario fue enviado. -->
            <center><input class="btn-ingresar" type="submit" value="Ingresar" name="entrar"></center>
            </div>
        </form>

        <!-- Enlace para ir a la pagina de registro si no tiene cuenta -->
        <a href="formulario.php">Registrarse</a>
    </div>
</body>
<footer>
    <p>Desarrollado por Natalia Edith Mejia Bautista</p>
    <p>Curso de PHP DGTIC. Diciembre 2024</p>
</footer>
</html>

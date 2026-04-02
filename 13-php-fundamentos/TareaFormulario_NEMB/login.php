<?php

include_once 'usuario.php'; // Include the file where the user data is stored
session_start(); // Start the session
/* print_r($_POST);  */
//print_r($_SESSION['alumnosRegistrados']);
// Check if the form has been submitted
if(isset($_POST['entrar'])) {
    // Buscar al alumno en la lista de alumnos registrados
    $alumno = isset($_SESSION['alumnosRegistrados'][$_POST['num_cuenta_ingresada']]) ? $_SESSION['alumnosRegistrados'][$_POST['num_cuenta_ingresada']] : [];
    
    /* print_r($alumno); */
    if ($alumno!=[] && $_POST['num_cuenta_ingresada'] == $alumno['num_cta'] &&  $_POST['contrasena_ingresada'] == $alumno['contrasena']) {
        $_SESSION['login'] = [
            'nombre' => $alumno['nombre'] . ' ' . $alumno['primer_apellido'].' '.$alumno['segundo_apellido'], 
            'num_cta' => $alumno['num_cta'], 
            'fecha_nac' => $alumno['fecha_nac'], 
        ];
        /* print_r($_SESSION['login']); */
        header('Location: info.php');
        exit(); // Ensure no further code is executed after redirection
    } else {
        // If the user is not found, display an error message
        echo "<div class='error'> Error: Numero de cuenta no encontrado o contraseña incorrecta </div>";
    }    
}
?>
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
        <form action="login.php" method="POST">

            <div class="contenedor-input">
            <label for="num_cuenta">Numero de cuenta:</label>
            <input class="caja" type="text" name="num_cuenta_ingresada" id="num_cuenta" placeholder='123123' required>
            </div>

            <div class="contenedor-input">
            <label for="password">Contraseña:</label>
            <input class="caja" type="password" name="contrasena_ingresada" id="password" placeholder="Ingrese su contraseña" required>
            </div>

            <div class="contenedor-input">
            <center><input class="btn-ingresar" type="submit" value="Ingresar" name="entrar"></center>
            </div>
        </form>

        <a href="formulario.php">Registrarse</a>
    </div>
</body>
<footer>
    <p>Desarrollado por Natalia Edith Mejia Bautista</p>
    <p>Curso de PHP DGTIC. Diciembre 2024</p>
</footer>
</html>
<!-- http://127.0.0.1/PHP-Naty/CursoDGTIC/BasicosPHP/TareaFormulario_NEMB/formulario.php -->
<?php
session_start();
include_once 'usuario.php';

//print_r($_SESSION);
//Guardar datos del formulario en la variable de sesión
if(isset($_POST['num_cta'])) {
    $_SESSION['alumnosRegistrados'][$_POST['num_cta']] = [
        'num_cta' => $_POST['num_cta'],
        'nombre' => $_POST['nombre'],
        'primer_apellido' => $_POST['primer_apellido'],
        'segundo_apellido' => $_POST['segundo_apellido'],
        'genero' => $_POST['genero'],
        'contrasena' => $_POST['contrasena'],
        'fecha_nac' => $_POST['fec_nac']
    ];
    if (isset($_SESSION['alumnosRegistrados'][$_POST['num_cta']])) {
        echo "<div class='exito'> Datos guardados correctamente </div>";
    } else {
        echo "<div class='error'> Error al guardar los datos </div>";
    }
    //print_r($_SESSION['alumnosRegistrados']);
    //header('Location: login.php');
} 
?>
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="estilos.css">
    <title>Formulario de registro</title>
</head>
<body>
<div class="contenedor">
        <h2>Formulario de registro de alumnos</h2>
        <form action="formulario.php" method="post">
            <div class="contenedor-input">
            <label for="num_cta">Numero de cuenta:</label>
            <input type="text" name="num_cta" placeholder="317737822" required>
            </div>

            <div class="contenedor-input">
            <label for="nombre">Nombre:</label>
            <input type="text" name="nombre" placeholder="Natalia" required>
            </div>

            <div class="contenedor-input">
            <label for="primer_apellido">Primer Apellido:</label>
            <input type="text" name="primer_apellido" placeholder="Mejia" required>
            </div>

            <div class="contenedor-input">
            <label for="segundo_apellido">Segundo Apellido:</label>
            <input type="text" name="segundo_apellido" placeholder="Bautista" required>
            </div>

            <div class="contenedor-input">
            <label for="genero">Género:</label>
            <select name="genero" required>
                <option value="">Seleccione uno</option>
                <option value="M">Hombre</option>
                <option value="F">Mujer</option>
                <option value="O">Otro</option>
            </select>
            </div>

            <div class="contenedor-input">
            <label for="fec_nac">Fecha de Nacimiento:</label>
            <input type="date" name="fec_nac" required>
            </div>

            <div class="contenedor-input">
            <label for="contrasena">Contraseña</label>
            <input type="password" name="contrasena" placeholder="12341234@" required>
            </div>  

            <center><button class="btn-ingresar" type="submit">Registrarme</button></center>
        </form>
        <a href="login.php">Iniciar Sesión</a>
<!--         <a href="info.php">Ver información</a>
        <a href="logout.php">Cerrar Sesión</a> -->
        
    </div>

</body>
<footer>
    <p>Desarrollado por Natalia Edith Mejia Bautista</p>
    <p>Curso de PHP DGTIC. Diciembre 2024</p>
</footer>
</html>
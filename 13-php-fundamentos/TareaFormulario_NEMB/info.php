<!-- http://127.0.0.1/PHP-Naty/CursoDGTIC/BasicosPHP/TareaFormulario_NEMB/info.php -->

<!--
=============================================================================
PAGINA DE INFORMACION DEL ALUMNO (REQUIERE SESION ACTIVA)
=============================================================================

CONCEPTOS CLAVE EN ESTE ARCHIVO:
---------------------------------

1. PAGINA PROTEGIDA:
   Esta pagina muestra datos del alumno que inicio sesion.
   Depende de que $_SESSION['login'] exista (creada en login.php).
   En un proyecto real, se deberia verificar si el usuario esta autenticado
   y redirigir a login.php si no lo esta:

   if (!isset($_SESSION['login'])) {
       header('Location: login.php');
       exit();
   }

2. require_once vs include_once:
   - include_once: Si el archivo no existe, muestra WARNING pero sigue ejecutando
   - require_once: Si el archivo no existe, muestra FATAL ERROR y DETIENE la ejecucion

   Se usa require_once cuando el archivo es INDISPENSABLE para que la pagina funcione.
   Se usa include_once cuando es opcional o complementario.

3. MEZCLA DE PHP Y HTML:
   En este archivo se mezcla PHP dentro del HTML usando la sintaxis corta:
   <?php echo $variable; ?>

   Esto permite insertar valores dinamicos dentro de etiquetas HTML.
   El servidor ejecuta el PHP y envia el HTML resultante al navegador.

4. foreach - RECORRER ARRAYS:
   foreach ($array as $elemento) { ... }
   Recorre cada elemento de un array. En este caso, recorre todos los
   alumnos registrados para mostrarlos en una tabla HTML.

   Equivalencia con Python:
   PHP:    foreach ($array as $elem) { ... }
   Python: for elem in array: ...

5. TABLAS HTML DINAMICAS:
   Se usa PHP dentro de <table> para generar filas (<tr>) dinamicamente.
   Cada iteracion del foreach genera una fila de la tabla.
-->

<?php

// require_once es mas estricto que include_once:
// Si 'usuario.php' no existe, PHP lanza un error FATAL y se detiene.
// Esto es apropiado porque los datos de usuario son ESENCIALES.
require_once('usuario.php');

// Inicia/reanuda la sesion para poder acceder a $_SESSION['login']
// y $_SESSION['alumnosRegistrados'] que fueron creados en formulario.php y login.php
session_start();

// NOTA: En produccion, aqui deberia haber una verificacion:
// if (!isset($_SESSION['login'])) {
//     header('Location: login.php');
//     exit();
// }
// Esto protege la pagina de accesos no autorizados.
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="estilos.css">
    <title>Información alumnos</title>
</head>
<body>
    <!-- ===================================================================
         TARJETA DE INFORMACION DEL USUARIO LOGUEADO
         ===================================================================
         Se accede a los datos del usuario autenticado a traves de
         $_SESSION['login'], que fue creada en login.php
    -->
    <div class="contenedor">
        <h2>Mi informacion</h2>
            <!-- Imagen de perfil aleatoria usando el servicio pravatar.cc -->
            <img src="https://i.pravatar.cc/128" alt="foto de perfil" class="foto_perfil">

            <!-- <?php echo ... ?> inserta valores de PHP dentro del HTML -->
            <!-- $_SESSION['login']['nombre'] contiene el nombre completo del alumno -->
            <p><strong>Nombre completo:</strong> <?php echo $_SESSION['login']['nombre']; ?></p>

            <p><strong>Número de Cuenta:</strong> <?php echo $_SESSION['login']['num_cta']; ?></p>
            <p><strong>Fecha de Nacimiento:</strong> <?php echo $_SESSION['login']['fecha_nac']; ?></p>
    </div>

    <!-- ===================================================================
         TABLA DE TODOS LOS USUARIOS REGISTRADOS
         ===================================================================
         Se recorre $_SESSION['alumnosRegistrados'] con foreach para generar
         una fila de tabla por cada alumno registrado.

         NOTA DE SEGURIDAD: En produccion, NO se mostrarian todos los datos
         de otros usuarios. Esto es solo con fines didacticos.
    -->
    <!--  Tabla de usuarios registrados -->
    <div>
        <h3>Usuarios registrados</h3>
        <table class="tabla_usuarios">
            <!-- Cabecera de la tabla (se muestra UNA sola vez) -->
            <tr>
                <th>Nombre</th>
                <th>Numero de cuenta</th>
                <th>Fecha de nacimiento</th>
            </tr>

            <!--
            foreach recorre el array asociativo $_SESSION['alumnosRegistrados'].
            En cada iteracion, $alumno contiene UN array con los datos de UN alumno:
            $alumno = ['num_cta' => 317737822, 'nombre' => 'Natalia', ...]

            La sintaxis PHP dentro de HTML usa <?php ... ?> para abrir/cerrar bloques.
            El HTML dentro del foreach se repite por cada alumno.
            -->
            <?php foreach ($_SESSION['alumnosRegistrados'] as $alumno) { ?>
                <tr>
                    <!-- Se concatenan nombre + apellidos con el operador punto (.) -->
                    <td><?php echo $alumno['nombre'] . ' ' . $alumno['primer_apellido'] . ' ' . $alumno['segundo_apellido']; ?></td>
                    <td><?php echo $alumno['num_cta']; ?></td>
                    <td><?php echo $alumno['fecha_nac']; ?></td>
                </tr>
            <?php } ?>
        </table>

    <!-- Enlaces de navegacion -->
    <a href="formulario.php">Ir a Formulario</a>
    <a href="logout.php">Cerrar Sesión</a>
    </div>

</body>
<footer>
    <p>Desarrollado por Natalia Edith Mejia Bautista</p>
    <p>Curso de PHP DGTIC. Diciembre 2024</p>
</footer>
</html>

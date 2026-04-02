<!--
=============================================================================
CIERRE DE SESION (LOGOUT)
=============================================================================

CONCEPTOS CLAVE EN ESTE ARCHIVO:
---------------------------------

1. DESTRUCCION DE SESION:
   Para cerrar la sesion de un usuario correctamente, se deben hacer
   TRES pasos:

   a) session_start()    -> Reanudar la sesion activa
   b) session_unset()    -> Eliminar todas las variables de $_SESSION
   c) session_destroy()  -> Destruir la sesion en el servidor

   NOTA: Este archivo no incluye estas llamadas explicitamente,
   lo cual significa que la sesion NO se destruye realmente al visitar
   esta pagina. En un proyecto real, se deberia agregar:

   <?php
   session_start();       // Primero hay que reanudar la sesion
   $_SESSION = [];        // Limpiar todas las variables de sesion
   session_unset();       // Liberar las variables de sesion
   session_destroy();     // Destruir la sesion en el servidor
   ?>

   Sin estos pasos, si el usuario vuelve a info.php, seguira viendo
   sus datos porque la sesion sigue activa.

2. MEZCLA DE JAVASCRIPT Y HTML:
   La etiqueta <script> contiene JavaScript que se ejecuta en el NAVEGADOR.
   alert() muestra una ventana emergente. Esto es codigo del LADO DEL CLIENTE.

   DIFERENCIA IMPORTANTE:
   - PHP se ejecuta en el SERVIDOR (antes de enviar la respuesta)
   - JavaScript se ejecuta en el NAVEGADOR (despues de recibir la respuesta)
   - El servidor envia el HTML con el <script> incluido
   - El navegador ejecuta el alert() al cargar la pagina

3. FLUJO DE LOGOUT IDEAL:
   Usuario hace clic en "Cerrar Sesion"
       |
       v
   Servidor recibe GET /logout.php
       |
       v
   PHP: session_start() + session_destroy()
       |
       v
   Servidor envia HTML de despedida + header para eliminar cookie
       |
       v
   Navegador muestra la pagina de despedida
   (La cookie PHPSESSID se elimina o expira)
-->

<script>
    alert("¡Se ha cerrado sesion!");
</script>
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="estilos.css">
    <title>Sesion cerrada</title>
</head>
<body>
    <h1>¡Hasta luego!</h1>
    <p>¡Gracias por visitarnos!</p>
    <div>
        <!-- Imagen GIF externa para la despedida -->
        <img src="https://media.giphy.com/media/3o7TKz9bX9v6hZ8lIc/giphy.gif" alt="Gif de despedida">
    </div>

    <!-- Enlaces para volver a iniciar sesion o registrarse -->
    <a href="login.php">Iniciar sesion</a>
    <a href="formulario.php">Registrarse</a>
</body>
<footer>
    <p>Desarrollado por Natalia Edith Mejia Bautista</p>
    <p>Curso de PHP DGTIC. Diciembre 2024</p>
</footer>
</html>

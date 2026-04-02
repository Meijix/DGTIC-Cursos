<!-- http://127.0.0.1/PHP-Naty/CursoDGTIC/BasicosPHP/TareaFormulario_NEMB/formulario.php -->

<!--
=============================================================================
FORMULARIO DE REGISTRO DE ALUMNOS CON PHP
=============================================================================

CONCEPTOS CLAVE EN ESTE ARCHIVO:
---------------------------------

1. SESIONES EN PHP (session_start()):
   HTTP es un protocolo SIN ESTADO (stateless). Esto significa que cada
   peticion del navegador es INDEPENDIENTE: el servidor no recuerda nada
   entre una peticion y otra.

   Las sesiones resuelven esto:
   - session_start() crea o reanuda una sesion
   - PHP genera un ID unico (PHPSESSID) y lo envia al navegador como cookie
   - En cada peticion, el navegador envia esa cookie de vuelta
   - PHP usa ese ID para recuperar los datos guardados en $_SESSION

   FLUJO COMPLETO:
   Navegador -> POST /formulario.php -> Servidor PHP
   Servidor: session_start() -> genera ID "abc123"
   Servidor -> Respuesta + Cookie: PHPSESSID=abc123 -> Navegador
   Navegador -> GET /info.php + Cookie: PHPSESSID=abc123 -> Servidor
   Servidor: session_start() -> recupera sesion "abc123" con los datos previos

2. $_POST:
   Variable superglobal de PHP que contiene los datos enviados por un
   formulario HTML con method="POST". Es un array asociativo.
   Ejemplo: $_POST['nombre'] contiene el valor del input con name="nombre"

   DIFERENCIA GET vs POST:
   - GET: datos visibles en la URL (?nombre=Juan&edad=20). Limite de tamano.
          Usar para busquedas y filtros. Los datos quedan en el historial.
   - POST: datos en el cuerpo de la peticion HTTP (no visibles en URL).
           Sin limite practico de tamano. Usar para formularios con datos sensibles.

3. include_once:
   Incluye y ejecuta un archivo PHP externo. El "_once" asegura que solo
   se incluya UNA VEZ aunque se llame multiples veces (evita errores de
   redefinicion de funciones o clases).

4. isset():
   Verifica si una variable existe y no es NULL.
   isset($_POST['num_cta']) retorna true solo si el formulario fue enviado
   con un campo llamado 'num_cta'. Es una buena practica verificar ANTES
   de usar los datos.

5. ARRAYS ASOCIATIVOS:
   En PHP, los arrays pueden tener claves con nombre (como diccionarios en Python).
   $_SESSION['alumnosRegistrados'][$_POST['num_cta']] crea una estructura:
   $_SESSION = [
       'alumnosRegistrados' => [
           317737822 => ['num_cta' => 317737822, 'nombre' => 'Natalia', ...]
       ]
   ]

6. FORMULARIOS HTML + PHP:
   <form action="formulario.php" method="post"> indica:
   - action: a donde se envian los datos (puede ser el mismo archivo)
   - method: como se envian (POST o GET)

   Cada <input name="campo"> genera una entrada en $_POST['campo']
   El atributo 'required' hace validacion del lado del CLIENTE (navegador),
   pero SIEMPRE se debe validar tambien del lado del SERVIDOR (PHP).

FLUJO DE ESTE ARCHIVO:
-----------------------
1. Se inicia la sesion y se cargan usuarios precargados (usuario.php)
2. Si hay datos POST (formulario enviado), se guardan en $_SESSION
3. Se muestra el formulario HTML (siempre, haya o no datos POST)
4. El formulario apunta a si mismo (action="formulario.php")
-->

<?php
// session_start() DEBE ser lo PRIMERO que se ejecuta en el archivo.
// No puede haber NADA antes (ni espacios, ni HTML, ni echo).
// Razon: session_start() envia una cabecera HTTP (Set-Cookie), y las
// cabeceras deben enviarse ANTES de cualquier contenido.
session_start();

// include_once carga el archivo usuario.php que contiene los datos
// precargados de alumnos. Usa "_once" para evitar doble inclusion.
include_once 'usuario.php';

//print_r($_SESSION);

// =========================================================================
// PROCESAMIENTO DEL FORMULARIO (logica del servidor)
// =========================================================================
// isset() verifica si el formulario fue enviado.
// Si alguien accede a esta pagina directamente (sin enviar el form),
// $_POST estara vacio y este bloque NO se ejecuta.
//Guardar datos del formulario en la variable de sesión
if(isset($_POST['num_cta'])) {
    // Guardamos los datos en $_SESSION usando el numero de cuenta como clave.
    // Esto permite buscar rapidamente al alumno por su numero de cuenta.
    //
    // ESTRUCTURA DEL ARRAY:
    // $_SESSION['alumnosRegistrados'][317737822] = [
    //     'num_cta' => 317737822,
    //     'nombre' => 'Natalia',
    //     ...
    // ]
    //
    // NOTA DE SEGURIDAD: En un proyecto real, la contrasena NUNCA se guarda
    // en texto plano. Se debe usar password_hash() para cifrarla:
    // 'contrasena' => password_hash($_POST['contrasena'], PASSWORD_DEFAULT)
    $_SESSION['alumnosRegistrados'][$_POST['num_cta']] = [
        'num_cta' => $_POST['num_cta'],
        'nombre' => $_POST['nombre'],
        'primer_apellido' => $_POST['primer_apellido'],
        'segundo_apellido' => $_POST['segundo_apellido'],
        'genero' => $_POST['genero'],
        'contrasena' => $_POST['contrasena'],
        'fecha_nac' => $_POST['fec_nac']
    ];

    // Verificacion: comprobamos que los datos se guardaron correctamente
    if (isset($_SESSION['alumnosRegistrados'][$_POST['num_cta']])) {
        // Se genera HTML con una clase CSS para estilizar el mensaje
        echo "<div class='exito'> Datos guardados correctamente </div>";
    } else {
        echo "<div class='error'> Error al guardar los datos </div>";
    }
    //print_r($_SESSION['alumnosRegistrados']);
    //header('Location: login.php');
}
?>

<!-- =====================================================================
     PARTE HTML - INTERFAZ DE USUARIO
     =====================================================================
     A partir de aqui, todo es HTML puro que el navegador renderiza.
     PHP ya termino de ejecutarse en el bloque anterior.
-->
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- Enlace a la hoja de estilos CSS externa -->
    <link rel="stylesheet" href="estilos.css">
    <title>Formulario de registro</title>
</head>
<body>
<div class="contenedor">
        <h2>Formulario de registro de alumnos</h2>

        <!--
        FORMULARIO HTML:
        - action="formulario.php" -> al enviar, los datos van a este mismo archivo
        - method="post" -> los datos se envian por POST (no visibles en la URL)

        Cuando el usuario hace clic en "Registrarme":
        1. El navegador recopila todos los valores de los inputs
        2. Crea una peticion HTTP POST con esos datos en el cuerpo
        3. Envia la peticion al servidor (a formulario.php)
        4. El servidor ejecuta el PHP de arriba y procesa los datos
        5. El servidor responde con el HTML del formulario (posiblemente con mensaje de exito)
        -->
        <form action="formulario.php" method="post">
            <!-- Cada input tiene un atributo 'name' que se convierte en la clave de $_POST -->
            <!-- 'required' hace validacion basica en el navegador (HTML5) -->
            <div class="contenedor-input">
            <label for="num_cta">Numero de cuenta:</label>
            <!-- name="num_cta" -> despues se accede como $_POST['num_cta'] -->
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
            <!-- <select> genera un menu desplegable -->
            <!-- Cada <option value="X"> define una opcion; el 'value' es lo que se envia por POST -->
            <select name="genero" required>
                <option value="">Seleccione uno</option>
                <option value="M">Hombre</option>
                <option value="F">Mujer</option>
                <option value="O">Otro</option>
            </select>
            </div>

            <div class="contenedor-input">
            <label for="fec_nac">Fecha de Nacimiento:</label>
            <!-- type="date" muestra un selector de fecha nativo del navegador -->
            <input type="date" name="fec_nac" required>
            </div>

            <div class="contenedor-input">
            <label for="contrasena">Contraseña</label>
            <!-- type="password" oculta los caracteres al escribir (muestra puntos) -->
            <!-- NOTA: Esto solo es visual; los datos viajan sin cifrar a menos que se use HTTPS -->
            <input type="password" name="contrasena" placeholder="12341234@" required>
            </div>

            <!-- type="submit" envia el formulario al servidor -->
            <center><button class="btn-ingresar" type="submit">Registrarme</button></center>
        </form>
        <!-- Enlace para ir a la pagina de login si ya tiene cuenta -->
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

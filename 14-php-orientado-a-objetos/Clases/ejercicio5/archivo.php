<?php
/**
 * ==========================================================================
 * EJERCICIO 5 (PARTE 2): CONSTRUCTOR Y DESTRUCTOR - GENERADOR DE CONTRASENAS
 * ==========================================================================
 *
 * PROGRESION:
 * Ejercicio 1-4: Constructor basico o sin constructor
 * Ejercicio 5:   Constructor con PARAMETROS + Destructor
 *
 * CONCEPTOS CLAVE:
 * ----------------
 *
 * 1. __construct($parametro) - CONSTRUCTOR CON PARAMETROS:
 *    El constructor puede recibir parametros, lo que OBLIGA a proporcionar
 *    datos al momento de crear el objeto.
 *
 *    $password1 = new password("Natalia");
 *    // PHP automaticamente ejecuta: __construct("Natalia")
 *    // No se puede hacer: new password();  -> Error: falta parametro
 *
 *    Esto es util cuando un objeto NO TIENE SENTIDO sin ciertos datos.
 *    Un generador de contrasena sin nombre del usuario no tiene sentido.
 *
 * 2. __destruct() - DESTRUCTOR:
 *    Metodo magico que se ejecuta AUTOMATICAMENTE cuando un objeto
 *    se destruye. Esto ocurre en dos situaciones:
 *
 *    a) Cuando PHP termina de ejecutar el script (fin del archivo)
 *    b) Cuando se usa unset($objeto) explicitamente
 *    c) Cuando la variable sale de su alcance (scope)
 *
 *    IMPORTANTE: El destructor se ejecuta DESPUES de que PHP ha enviado
 *    la mayor parte del HTML al navegador. Por eso el echo dentro del
 *    destructor aparece al final de la pagina.
 *
 *    Uso comun del destructor:
 *    - Cerrar conexiones a bases de datos
 *    - Cerrar archivos abiertos
 *    - Liberar recursos del sistema
 *    - Guardar logs
 *
 * 3. FUNCIONES DE CADENA ENCADENADAS:
 *    substr(strtoupper(uniqid()), -4) combina tres funciones:
 *
 *    uniqid()         -> Genera un ID unico basado en el tiempo, ej: "672f3a1b2c4d5"
 *    strtoupper(...)  -> Convierte a mayusculas: "672F3A1B2C4D5"
 *    substr(..., -4)  -> Toma los ultimos 4 caracteres: "4D5"
 *                        El -4 indica "desde 4 posiciones antes del final"
 *
 *    Resultado: Una "contrasena" de 4 caracteres alfanumericos en mayusculas.
 *    NOTA: Esto NO es criptograficamente seguro. Para contrasenas reales
 *    se debe usar random_bytes() o password_hash().
 *
 * 4. CICLO DE VIDA DE UN OBJETO:
 *
 *    new password("Natalia")     ->  __construct() se ejecuta
 *         |                              |
 *         v                              v
 *    Objeto existe en memoria      Se inicializan propiedades
 *    Se pueden usar sus metodos    Se genera la contrasena
 *         |
 *         v
 *    Script PHP termina (o unset)  ->  __destruct() se ejecuta
 *                                           |
 *                                           v
 *                                      Se muestra mensaje de destruccion
 *                                      Se libera la memoria
 */

// Crear una clase con dichos métodos (__construct y __destruct) pero ahora que al momento de instanciar a la clase te genere una contraseña de solo 4 letras mayúsculas y al momento de destruir el objeto se muestre en pantalla tu contraseña.

class password{
    //declaracion de atributos
    // Todos son private: solo accesibles desde dentro de esta clase
    private $nombre;
    private $password;
    private $salidatexto;

    /**
     * CONSTRUCTOR con parametro obligatorio.
     * Se ejecuta al hacer: $password1 = new password("Natalia");
     * Inicializa el nombre y genera una contrasena aleatoria.
     *
     * @param string $nombre El nombre del usuario
     */
    //declaracion de metodo constructor
    public function __construct($nombre){
        $this->nombre=$nombre;

        //genera contrasena de 4 letras mayusculas
        // Paso a paso:
        // 1. uniqid()     -> genera algo como "672f3a1b2c4d5" (basado en microsegundos)
        // 2. strtoupper() -> "672F3A1B2C4D5"
        // 3. substr(,-4)  -> toma los ultimos 4 caracteres: "4D5" + uno mas
        $this->password=substr(strtoupper(uniqid()),-4);
    }

    /**
     * DESTRUCTOR: Se ejecuta automaticamente cuando el objeto se destruye.
     * En este caso, muestra un mensaje de despedida con la contrasena
     * y luego la "destruye" asignandole null.
     *
     * El destructor se ejecuta:
     * - Al final del script PHP (cuando todas las variables se liberan)
     * - Al hacer unset($password1)
     * - Cuando la variable sale de su alcance (ej: fin de una funcion)
     */
    //declaracion de metodo destructor
    public function __destruct(){
        //Texto de salida de destruccion de contrasena
        $this->salidatexto=$this->nombre.', la contrasena ' . $this->password. ' ha sido destruida';
        //destruye la contrasena
        // Asignar null "borra" el valor, pero la propiedad sigue existiendo
        $this->password=null;
        //muestra el mensaje como parrafo alerta
        // Este echo se ejecuta cuando el objeto se destruye
        // Aparecera al final del HTML porque PHP destruye objetos al terminar el script
        echo '<p style="color: red;">'.$this->salidatexto.'</p>';

    }
}

$mensaje='';

// Solo creamos el objeto si el formulario fue enviado
//instanciar clase con el nombre del usuario
if (!empty($_POST)){
    //creacion de objeto de la clase
    // Al hacer new password($_POST['nombre']):
    // 1. PHP reserva memoria para el objeto
    // 2. Ejecuta __construct($_POST['nombre'])
    // 3. Se genera la contrasena automaticamente
    $password1= new password($_POST['nombre']);
    //$mensaje=$password1->mostrar();

    // Cuando PHP termina de ejecutar este archivo:
    // 1. $password1 sale del alcance
    // 2. PHP ejecuta automaticamente __destruct()
    // 3. Se muestra el mensaje rojo en la pagina
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        input{
            margin: 10px;
        }

        h1{
            text-align: center;
            color: darkblue;
            font-family: sans-serif;
        }

        p, form{
            text-align: center;
        }


    </style>
    <title>Ejercicio Contrasena</title>
</head>
<body>
    <h1>Password</h1>
    <!-- Formulario que se envia a si mismo (action="" vacio) -->
    <form action="" method="post">
        <p>Ingresa tu nombre para generar tu contrasena: </p>
        <!-- name="nombre" -> se accede como $_POST['nombre'] en el PHP de arriba -->
        <input type="text" name="nombre" placeholder="Nombre">
        <input type="submit" value="Generar">
    </form>

</body>
</html>

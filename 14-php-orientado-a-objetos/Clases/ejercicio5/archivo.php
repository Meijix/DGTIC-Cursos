<?php
// Crear una clase con dichos métodos (__construct y __destruct) pero ahora que al momento de instanciar a la clase te genere una contraseña de solo 4 letras mayúsculas y al momento de destruir el objeto se muestre en pantalla tu contraseña.

class password{
    //declaracion de atributos
    private $nombre;
    private $password;
    private $salidatexto;
    //declaracion de metodo constructor
    public function __construct($nombre){
        $this->nombre=$nombre;
        //genera contrasena de 4 letras mayusculas
        $this->password=substr(strtoupper(uniqid()),-4);
    }

    //declaracion de metodo destructor
    public function __destruct(){
        //Texto de salida de destruccion de contrasena 
        $this->salidatexto=$this->nombre.', la contrasena ' . $this->password. ' ha sido destruida';
        //destruye la contrasena
        $this->password=null;
        //muestra el mensaje como parrafo alerta
        echo '<p style="color: red;">'.$this->salidatexto.'</p>';
    
    }
}

$mensaje='';
//instanciar clase con el nombre del usuario
if (!empty($_POST)){
    //creacion de objeto de la clase
    $password1= new password($_POST['nombre']);
    //$mensaje=$password1->mostrar();
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
    <form action="" method="post">
        <p>Ingresa tu nombre para generar tu contrasena: </p>
        <input type="text" name="nombre" placeholder="Nombre">
        <input type="submit" value="Generar">
    </form>

</body>
</html>
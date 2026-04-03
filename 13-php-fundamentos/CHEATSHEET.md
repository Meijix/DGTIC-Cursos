# Cheatsheet — Fundamentos de PHP

## Sintaxis basica

```php
<?php
// Todo el codigo va entre <?php ... ?>
echo "Hola mundo";   // imprime al navegador
// Cada instruccion termina con punto y coma (;)
?>
```

## Variables y tipos

```php
$nombre = "Juan";       // string
$edad = 20;             // int
$promedio = 8.5;        // float
$activo = true;         // bool
$datos = null;          // null
$colores = ["rojo", "azul"];  // array
```

Todas las variables empiezan con `$`. PHP infiere el tipo (tipado dinamico).

| Funcion              | Uso                              |
|----------------------|----------------------------------|
| `gettype($x)`       | Nombre del tipo como string      |
| `var_dump($x)`      | Tipo + valor (debug)             |
| `isset($x)`         | Existe y no es null              |
| `empty($x)`         | Vacio, 0, "", null, false, []    |

## Operadores

```
==   Igual valor (5 == "5" es TRUE)    CUIDADO
===  Igual valor Y tipo                SIEMPRE preferir este
.    Concatenar strings: "Hola" . " mundo"
.=   Concatenar y asignar: $s .= "!"
**   Potencia: $a ** 2
%    Modulo: $a % 2
```

## Strings

```php
"Hola $nombre"         // comillas dobles: interpolan variables
'Hola $nombre'         // comillas simples: texto literal
"Hola" . " " . $nombre // concatenacion con punto
```

| Funcion               | Ejemplo                             | Resultado     |
|-----------------------|-------------------------------------|---------------|
| `strlen($s)`          | `strlen("Hola")`                   | `4`           |
| `strtoupper($s)`      | `strtoupper("hola")`               | `"HOLA"`      |
| `strtolower($s)`      | `strtolower("HOLA")`               | `"hola"`      |
| `substr($s, i, n)`    | `substr("Hola", 1, 2)`            | `"ol"`        |
| `trim($s)`            | `trim(" Hola ")`                   | `"Hola"`      |
| `str_replace(a,b,$s)` | `str_replace("a","o","Hala")`      | `"Holo"`      |
| `explode(sep, $s)`    | `explode(",", "a,b,c")`           | `["a","b","c"]`|
| `implode(sep, $a)`    | `implode("-", [1,2,3])`           | `"1-2-3"`     |

## Arrays

```php
// Indexado
$frutas = ["manzana", "pera", "uva"];
echo $frutas[0];  // "manzana"

// Asociativo (clave => valor)
$alumno = ["nombre" => "Ana", "edad" => 20];
echo $alumno["nombre"];  // "Ana"

// Recorrer
foreach ($frutas as $fruta) { echo $fruta; }
foreach ($alumno as $clave => $valor) { echo "$clave: $valor"; }
```

| Funcion              | Descripcion                        |
|----------------------|------------------------------------|
| `count($arr)`        | Numero de elementos                |
| `array_push($a, v)` | Agrega al final                    |
| `in_array(v, $a)`   | Verifica si existe                 |
| `array_keys($a)`    | Retorna las claves                 |
| `sort($a)`          | Ordena (modifica el original)      |

## Funciones

```php
function saludar($nombre, $saludo = "Hola") {
    return "$saludo, $nombre!";
}
echo saludar("Ana");          // "Hola, Ana!"
echo saludar("Ana", "Buenos dias"); // "Buenos dias, Ana!"
```

Scope: las funciones NO acceden a variables externas salvo con `global $var;`.

## Superglobales

| Variable      | Contenido                                  |
|---------------|--------------------------------------------|
| `$_GET`       | Datos de la URL (`?nombre=Ana`)            |
| `$_POST`      | Datos del cuerpo de un formulario POST     |
| `$_SESSION`   | Datos persistentes entre paginas (sesion)  |
| `$_COOKIE`    | Cookies enviadas por el navegador          |
| `$_SERVER`    | Info del servidor y la peticion HTTP       |
| `$_FILES`     | Archivos subidos por formulario            |

## Formularios

```html
<form action="procesar.php" method="POST">
    <input type="text" name="nombre" required>
    <input type="submit" value="Enviar">
</form>
```

```php
<?php
if (isset($_POST['nombre'])) {
    $nombre = htmlspecialchars($_POST['nombre'], ENT_QUOTES, 'UTF-8');
    echo "Recibido: $nombre";
}
?>
```

## Sesiones

```php
session_start();                  // SIEMPRE al inicio del archivo
$_SESSION['usuario'] = "Ana";    // guardar dato
echo $_SESSION['usuario'];       // leer dato (en otra pagina)

// Cerrar sesion:
session_start();
$_SESSION = [];
session_destroy();
```

## Expresiones regulares

```php
preg_match("/^[0-9]+$/", "123")        // 1 (coincide)
preg_match_all("/[0-9]+/", $str, $m)   // busca todas las coincidencias
preg_replace("/[^a-zA-Z]/", "", $str)  // elimina no-letras
```

Patrones utiles: `/^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/` (email), `/^[0-9]{10}$/` (telefono 10 digitos)

## Include / Require

```php
include 'archivo.php';    // incluye, WARNING si no existe
require 'archivo.php';    // incluye, ERROR FATAL si no existe
include_once 'a.php';     // solo incluye una vez (evita duplicados)
require_once 'a.php';     // solo requiere una vez
```

## Referencia rapida — Seguridad

| Ataque          | Defensa                                            |
|-----------------|----------------------------------------------------|
| XSS             | `htmlspecialchars($dato, ENT_QUOTES, 'UTF-8')`    |
| SQL Injection   | Consultas preparadas con PDO: `$pdo->prepare("SELECT * FROM t WHERE c = ?"); $stmt->execute([$val]);` |
| CSRF            | Tokens ocultos en formularios                      |

**Regla de oro:** NUNCA confiar en datos del usuario. SIEMPRE validar en el servidor.

## Errores comunes

| Error                                  | Causa                                              | Solucion                          |
|----------------------------------------|----------------------------------------------------|-----------------------------------|
| `Undefined variable $x`               | Variable no existe o esta fuera de scope            | Verificar nombre y scope          |
| Headers already sent                   | `echo` antes de `session_start()` o `header()`     | Poner `session_start()` al inicio |
| `==` da resultados inesperados         | `5 == "5"` es TRUE (comparacion debil)             | Usar `===`                        |
| Formulario no envia datos              | Falta atributo `name` en el input HTML             | Agregar `name="campo"`            |
| Comillas simples no interpolan         | `'Hola $nombre'` imprime literal                   | Usar comillas dobles `"Hola $nombre"` |
| Sesion no persiste entre paginas       | Falta `session_start()` en cada archivo            | Llamar `session_start()` siempre  |

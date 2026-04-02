# Modulo 13: Fundamentos de PHP

## Tabla de Contenidos
1. [Que es PHP](#1-que-es-php)
2. [Variables, tipos y operadores](#2-variables-tipos-y-operadores)
3. [Cadenas de texto (strings)](#3-cadenas-de-texto-strings)
4. [Estructuras de control](#4-estructuras-de-control)
5. [Funciones](#5-funciones)
6. [Formularios y HTTP](#6-formularios-y-http)
7. [Sesiones](#7-sesiones)
8. [Expresiones regulares](#8-expresiones-regulares)
9. [Seguridad basica](#9-seguridad-basica)
10. [PHP vs Python](#10-php-vs-python---tabla-comparativa)
11. [Ejercicios de practica](#11-ejercicios-de-practica)

---

## 1. Que es PHP

PHP (PHP: Hypertext Preprocessor) es un lenguaje de programacion del **lado del servidor** disenado originalmente para el desarrollo web.

### Como funciona PHP en la web

```
   NAVEGADOR                    SERVIDOR WEB (Apache/Nginx)
   =========                    ===========================
       |                                |
       |  1. GET /pagina.php            |
       |  -----------------------------> |
       |                                |  2. Apache detecta .php
       |                                |     y llama al interprete PHP
       |                                |
       |                                |  3. PHP ejecuta el codigo
       |                                |     y genera HTML
       |                                |
       |  4. HTML puro                  |
       | <------------------------------ |
       |                                |
       |  5. El navegador renderiza     |
       |     el HTML. NUNCA ve el       |
       |     codigo PHP original.       |
```

### Sintaxis basica

```php
<?php
// Todo el codigo PHP va entre <?php y ?>
// Los comentarios de una linea usan // o #
/* Los comentarios de varias lineas usan esto */

echo "Hola mundo";  // echo envia texto al navegador
print "Hola mundo"; // print es similar a echo

// Las instrucciones terminan con punto y coma (;)
// Esto es OBLIGATORIO en PHP (a diferencia de Python)
?>
```

**IMPORTANTE:** Las etiquetas `<?php ... ?>` son obligatorias. Todo lo que este fuera de ellas se envia directamente al navegador como HTML.

---

## 2. Variables, tipos y operadores

### Variables

En PHP, todas las variables comienzan con `$` (signo de dolar). No es necesario declarar el tipo; PHP lo infiere automaticamente (**tipado dinamico**).

```php
<?php
$nombre = "Juan";      // string (cadena de texto)
$edad = 20;            // int (entero)
$promedio = 8.5;       // float (decimal)
$activo = true;        // bool (booleano)
$datos = null;         // null (sin valor)
$colores = ["rojo", "azul"];  // array (arreglo)
?>
```

### Tipos de datos

| Tipo     | Ejemplo            | Descripcion                    |
|----------|--------------------|--------------------------------|
| string   | `"Hola"`           | Cadena de texto                |
| int      | `42`               | Numero entero                  |
| float    | `3.14`             | Numero decimal                 |
| bool     | `true` / `false`   | Verdadero o falso              |
| array    | `[1, 2, 3]`        | Coleccion de valores           |
| null     | `null`             | Ausencia de valor              |
| object   | `new Clase()`      | Instancia de una clase         |

### Operadores

```
ARITMETICOS:
+   Suma            $a + $b
-   Resta           $a - $b
*   Multiplicacion  $a * $b
/   Division        $a / $b
%   Modulo          $a % $b     (residuo de la division)
**  Potencia        $a ** $b

ASIGNACION:
=   Asignar         $a = 5
+=  Sumar y asignar $a += 3     (equivale a $a = $a + 3)
.=  Concatenar      $a .= "!"  (equivale a $a = $a . "!")

COMPARACION:
==  Igual (valor)           $a == $b    (5 == "5" es TRUE)
=== Identico (valor+tipo)  $a === $b   (5 === "5" es FALSE)
!=  Diferente               $a != $b
<   Menor que               $a < $b
>   Mayor que               $a > $b
<=  Menor o igual           $a <= $b
>=  Mayor o igual           $a >= $b

LOGICOS:
&&  AND (y)         $a && $b
||  OR  (o)         $a || $b
!   NOT (no)        !$a
```

**CUIDADO:** `==` compara solo el valor (con conversion de tipos), pero `===` compara valor Y tipo. Siempre que puedas, usa `===` para evitar errores sutiles.

---

## 3. Cadenas de texto (strings)

### Comillas simples vs dobles

```php
<?php
$nombre = "Juan";

// Comillas dobles: INTERPOLAN variables (las reemplazan por su valor)
echo "Hola $nombre";     // Resultado: Hola Juan

// Comillas simples: NO interpolan (texto literal)
echo 'Hola $nombre';     // Resultado: Hola $nombre
?>
```

### Concatenacion

```php
<?php
// El PUNTO (.) une cadenas en PHP
$saludo = "Hola" . " " . "mundo";    // "Hola mundo"

// El PUNTO-IGUAL (.=) agrega al final
$texto = "Hola";
$texto .= " mundo";                  // "Hola mundo"
?>
```

### Funciones utiles para cadenas

| Funcion              | Descripcion                        | Ejemplo                              |
|---------------------|------------------------------------|--------------------------------------|
| `strlen($s)`        | Longitud de la cadena              | `strlen("Hola")` -> `4`             |
| `strtoupper($s)`    | Convertir a mayusculas             | `strtoupper("hola")` -> `"HOLA"`    |
| `strtolower($s)`    | Convertir a minusculas             | `strtolower("HOLA")` -> `"hola"`    |
| `str_repeat($s, n)` | Repetir n veces                    | `str_repeat("*", 3)` -> `"***"`     |
| `substr($s, i, n)`  | Subcadena desde posicion i         | `substr("Hola", 1, 2)` -> `"ol"`   |
| `trim($s)`          | Eliminar espacios al inicio y fin  | `trim(" Hola ")` -> `"Hola"`        |
| `str_replace(a,b,s)`| Reemplazar a por b en s            | `str_replace("a","o","Hala")` -> `"Holo"` |
| `explode(sep, $s)`  | Dividir cadena en array            | `explode(",", "a,b,c")` -> `["a","b","c"]` |
| `implode(sep, $a)`  | Unir array en cadena               | `implode("-", [1,2,3])` -> `"1-2-3"` |

---

## 4. Estructuras de control

### if / else / elseif

```php
<?php
$edad = 18;

if ($edad >= 18) {
    echo "Mayor de edad";
} elseif ($edad >= 13) {
    echo "Adolescente";
} else {
    echo "Menor de edad";
}

// Operador ternario (if en una linea):
$tipo = ($edad >= 18) ? "adulto" : "menor";
?>
```

### for

```php
<?php
// for (inicio; condicion; incremento)
for ($i = 0; $i < 5; $i++) {
    echo $i . " ";  // 0 1 2 3 4
}
?>
```

### while

```php
<?php
$i = 0;
while ($i < 5) {
    echo $i . " ";  // 0 1 2 3 4
    $i++;
}
?>
```

### foreach (para recorrer arrays)

```php
<?php
// Array simple
$frutas = ["manzana", "pera", "uva"];
foreach ($frutas as $fruta) {
    echo $fruta . " ";  // manzana pera uva
}

// Array asociativo
$alumno = ["nombre" => "Ana", "edad" => 20];
foreach ($alumno as $clave => $valor) {
    echo "$clave: $valor\n";  // nombre: Ana  edad: 20
}
?>
```

### switch

```php
<?php
$dia = "lunes";

switch ($dia) {
    case "lunes":
        echo "Inicio de semana";
        break;      // IMPORTANTE: sin break, sigue al siguiente case
    case "viernes":
        echo "Casi fin de semana";
        break;
    default:
        echo "Dia normal";
}
?>
```

---

## 5. Funciones

### Definicion y uso

```php
<?php
// Definicion: function nombre(parametros) { ... }
function saludar($nombre) {
    return "Hola, $nombre!";
}

// Llamada: nombre(argumentos)
$mensaje = saludar("Ana");
echo $mensaje;  // "Hola, Ana!"

// Parametros con valor por defecto
function potencia($base, $exponente = 2) {
    return $base ** $exponente;
}
echo potencia(3);      // 9 (usa exponente=2 por defecto)
echo potencia(3, 3);   // 27
?>
```

### Alcance de variables (scope)

```php
<?php
$global = "Soy global";

function ejemplo() {
    // Las variables de fuera NO son accesibles dentro
    // echo $global;  // ERROR: variable no definida

    $local = "Soy local";
    echo $local;  // OK

    // Para acceder a una variable global:
    global $global;
    echo $global;  // Ahora si funciona
}
?>
```

**NOTA:** En PHP, las funciones tienen su propio alcance. Esto es diferente a Python donde las funciones pueden leer (pero no modificar) variables externas.

---

## 6. Formularios y HTTP

### El ciclo peticion-respuesta (Request-Response)

```
  NAVEGADOR                                    SERVIDOR
  =========                                    ========
      |                                            |
      |  1. Usuario llena formulario y da clic     |
      |                                            |
      |  2. POST /formulario.php                   |
      |     Body: nombre=Ana&edad=20               |
      |  ----------------------------------------> |
      |                                            |
      |                           3. PHP ejecuta:  |
      |                           $_POST['nombre'] |
      |                           = "Ana"          |
      |                                            |
      |  4. HTML con la respuesta                  |
      | <----------------------------------------- |
      |                                            |
      |  5. Navegador muestra la pagina            |
```

### GET vs POST

| Caracteristica | GET                          | POST                          |
|---------------|------------------------------|-------------------------------|
| Datos en      | URL (`?nombre=Ana&edad=20`)  | Cuerpo de la peticion HTTP    |
| Visible en    | Barra del navegador, historial | No visible                  |
| Tamano maximo | ~2048 caracteres (URL)       | Sin limite practico           |
| Uso ideal     | Busquedas, filtros, compartir enlaces | Formularios, datos sensibles |
| Idempotente   | Si (repetir no cambia datos) | No (puede crear duplicados)   |
| PHP           | `$_GET['campo']`             | `$_POST['campo']`             |

### Formulario HTML + PHP

```html
<!-- HTML: El formulario -->
<form action="procesar.php" method="POST">
    <input type="text" name="nombre" required>
    <input type="email" name="email">
    <input type="submit" value="Enviar">
</form>
```

```php
<?php
// procesar.php: Recibe los datos
if (isset($_POST['nombre'])) {
    $nombre = $_POST['nombre'];
    echo "Recibido: $nombre";
}
?>
```

### Tipos de input y lo que envian

| HTML Input                          | $_POST recibe                  |
|------------------------------------|-------------------------------|
| `<input type="text" name="a">`     | `$_POST['a']` = texto escrito |
| `<input type="password" name="b">` | `$_POST['b']` = texto (sin cifrar) |
| `<input type="date" name="c">`     | `$_POST['c']` = "2024-12-25"  |
| `<select name="d"><option value="X">` | `$_POST['d']` = "X"       |
| `<input type="submit" name="e">`   | `$_POST['e']` = value del boton |

---

## 7. Sesiones

### El problema: HTTP es stateless (sin estado)

HTTP no recuerda nada entre peticiones. Cada vez que el navegador solicita una pagina, es como si fuera la primera vez. Las sesiones resuelven esto.

### Como funcionan las sesiones

```
  PRIMERA VISITA:
  ===============
  Navegador -> GET /pagina.php -> Servidor
                                   |
                                   v
                              session_start()
                              Genera ID: "abc123"
                              Crea archivo: /tmp/sess_abc123
                                   |
  Navegador <- HTML + Cookie: PHPSESSID=abc123 <- Servidor


  SIGUIENTES VISITAS:
  ===================
  Navegador -> GET /otra.php + Cookie: PHPSESSID=abc123 -> Servidor
                                                            |
                                                            v
                                                       session_start()
                                                       Lee /tmp/sess_abc123
                                                       Recupera $_SESSION
                                                            |
  Navegador <- HTML con datos personalizados <- Servidor
```

### Codigo de sesiones

```php
<?php
// PASO 1: Iniciar sesion (SIEMPRE al principio del archivo)
session_start();

// PASO 2: Guardar datos en la sesion
$_SESSION['usuario'] = "Ana";
$_SESSION['rol'] = "admin";

// PASO 3: Leer datos en OTRA pagina (que tambien tenga session_start())
echo $_SESSION['usuario'];  // "Ana"

// PASO 4: Cerrar sesion (logout)
session_start();
$_SESSION = [];      // Limpiar variables
session_unset();     // Liberar variables
session_destroy();   // Destruir la sesion
?>
```

### Diagrama del flujo de sesion completo

```
  Registro          Login              Info              Logout
  (formulario.php)  (login.php)        (info.php)        (logout.php)
       |                |                  |                  |
  session_start()  session_start()    session_start()    session_start()
       |                |                  |                  |
  $_SESSION =      Busca alumno       Lee $_SESSION      session_destroy()
  [alumno datos]   en $_SESSION       ['login']               |
       |                |                  |              Sesion eliminada
       |           Crea $_SESSION     Muestra datos
       |           ['login']               |
       |                |                  |
       |           header(Location)        |
       |           -> info.php             |
```

---

## 8. Expresiones regulares

### Sintaxis basica

Los patrones regex en PHP se encierran entre delimitadores: `/patron/`

| Simbolo   | Significado                    | Ejemplo           |
|-----------|-------------------------------|--------------------|
| `^`       | Inicio de cadena               | `/^Hola/`         |
| `$`       | Final de cadena                | `/mundo$/`        |
| `.`       | Cualquier caracter             | `/h.la/`          |
| `*`       | 0 o mas repeticiones           | `/ab*/`           |
| `+`       | 1 o mas repeticiones           | `/ab+/`           |
| `?`       | 0 o 1 repeticion (opcional)    | `/colou?r/`       |
| `[abc]`   | Cualquiera de a, b, c          | `/[aeiou]/`       |
| `[a-z]`   | Rango de la a a la z           | `/[a-z]+/`        |
| `[^abc]`  | Cualquiera EXCEPTO a, b, c     | `/[^0-9]/`        |
| `{n}`     | Exactamente n repeticiones     | `/[0-9]{4}/`      |
| `{n,m}`   | Entre n y m repeticiones       | `/[a-z]{2,6}/`    |
| `{n,}`    | n o mas repeticiones           | `/[a-z]{50,}/`    |
| `\d`      | Un digito (igual a [0-9])      | `/\d{3}/`         |
| `\w`      | Letra, digito o _              | `/\w+/`           |
| `\s`      | Espacio en blanco              | `/\s+/`           |
| `(grupo)` | Agrupa una sub-expresion       | `/(ab)+/`         |
| `\`       | Escapa un caracter especial    | `/\./` (punto literal) |

### Patrones comunes

```
EMAIL:    /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/
CURP:     /^[A-Z]{4}[0-9]{6}[A-Z]{6}[0-9]{2}$/
TELEFONO: /^[0-9]{10}$/
DECIMAL:  /^[0-9]+(\.[0-9]+)?$/
URL:      /^https?:\/\/[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(\/.*)?$/
```

### Funciones PHP para regex

```php
<?php
// preg_match: Busca UNA coincidencia (retorna 1 o 0)
$resultado = preg_match("/^[0-9]+$/", "12345");  // 1 (es un numero)

// preg_match_all: Busca TODAS las coincidencias
$cantidad = preg_match_all("/[0-9]+/", "hay 3 gatos y 5 perros", $matches);
// $matches[0] = ["3", "5"]

// preg_replace: Reemplaza coincidencias
$limpio = preg_replace("/[^a-zA-Z]/", "", "H0l@ Mund0");  // "HlMund"

// preg_split: Divide una cadena por un patron
$partes = preg_split("/[\s,]+/", "uno, dos,  tres");  // ["uno", "dos", "tres"]
?>
```

---

## 9. Seguridad basica

### XSS (Cross-Site Scripting)

Un atacante inyecta codigo JavaScript en tu pagina a traves de inputs de formularios.

```
ATAQUE:
1. Atacante escribe en un formulario: <script>alert('Hackeado!')</script>
2. Si PHP muestra ese dato sin limpiar: echo $_POST['nombre'];
3. El navegador ejecuta el JavaScript del atacante
4. Puede robar cookies, redirigir usuarios, modificar la pagina

DEFENSA:
Usar htmlspecialchars() SIEMPRE que muestres datos del usuario

echo htmlspecialchars($_POST['nombre'], ENT_QUOTES, 'UTF-8');
// Convierte < en &lt; y > en &gt;
// El navegador muestra el texto literal en vez de ejecutarlo
```

### Inyeccion SQL (SQL Injection)

```
ATAQUE:
Input del usuario: ' OR '1'='1
Query sin proteger: "SELECT * FROM users WHERE user='$input'"
Se convierte en:    "SELECT * FROM users WHERE user='' OR '1'='1'"
Resultado: Retorna TODOS los usuarios

DEFENSA:
Usar consultas preparadas (prepared statements) con PDO:
$stmt = $pdo->prepare("SELECT * FROM users WHERE user = ?");
$stmt->execute([$input]);
```

### Regla de oro

```
NUNCA confies en datos que vengan del usuario.
SIEMPRE valida en el servidor (PHP), no solo en el navegador (JavaScript/HTML).
SIEMPRE escapa datos antes de mostrarlos en HTML o usarlos en SQL.
```

---

## 10. PHP vs Python - Tabla comparativa

Para estudiantes que vienen del modulo 11 (Python):

| Concepto              | Python                        | PHP                              |
|-----------------------|-------------------------------|----------------------------------|
| Variables             | `nombre = "Juan"`             | `$nombre = "Juan";`             |
| Fin de instruccion    | Salto de linea                | Punto y coma `;`                |
| Bloques de codigo     | Indentacion                   | Llaves `{ }`                    |
| Imprimir              | `print("Hola")`              | `echo "Hola";`                  |
| Concatenar strings    | `"Hola" + " mundo"`          | `"Hola" . " mundo"`             |
| Comentarios           | `# comentario`               | `// comentario`                  |
| Arrays/Listas         | `lista = [1, 2, 3]`          | `$arr = [1, 2, 3];`             |
| Diccionarios          | `d = {"a": 1}`               | `$d = ["a" => 1];`              |
| Funciones             | `def nombre(param):`         | `function nombre($param) { }`   |
| For each              | `for x in lista:`            | `foreach ($arr as $x) { }`      |
| Tipo de variable      | `type(x)`                    | `gettype($x)`                   |
| Longitud string       | `len("hola")`                | `strlen("hola")`                |
| Mayusculas            | `"hola".upper()`             | `strtoupper("hola")`            |
| Comparacion estricta  | No aplica                     | `===` (valor Y tipo)            |
| Entorno               | Script / Servidor             | Servidor web (Apache/Nginx)      |
| Ejecucion             | `python script.py`           | Via servidor web + navegador     |

---

## 11. Ejercicios de practica

### Ejercicio 1: Variables y operadores
Crea un script PHP que calcule el area y perimetro de un rectangulo. Define las variables `$base` y `$altura`, muestra los resultados con `echo` formateados en HTML.

### Ejercicio 2: Estructuras de control
Escribe un programa que reciba un numero del 1 al 12 y muestre el nombre del mes correspondiente usando `switch`. Si el numero es invalido, muestra un mensaje de error.

### Ejercicio 3: Funciones y cadenas
Crea una funcion `invertirPalabra($palabra)` que invierta una cadena de texto SIN usar `strrev()`. Usa un bucle `for` que recorra la cadena de atras hacia adelante.

### Ejercicio 4: Formulario con validacion
Crea un formulario de contacto con campos nombre, email y mensaje. Valida en PHP que:
- El nombre tenga al menos 3 caracteres
- El email sea valido (usa una expresion regular)
- El mensaje no este vacio
Muestra los errores en rojo y los datos validos en verde.

### Ejercicio 5: Sesiones
Crea un sistema de carrito de compras simple con sesiones:
- Una pagina para agregar productos (nombre y precio)
- Otra pagina para ver el carrito con el total
- Un boton para vaciar el carrito (destruir sesion)

### Ejercicio 6: Expresiones regulares
Escribe expresiones regulares para validar:
- Un numero de telefono mexicano (10 digitos)
- Una contrasena segura (minimo 8 caracteres, al menos una mayuscula, una minuscula, un numero y un caracter especial)
- Un codigo postal mexicano (5 digitos)

---

## Recursos adicionales

- [Documentacion oficial de PHP](https://www.php.net/manual/es/)
- [PHP The Right Way](https://phptherightway.com/)
- [W3Schools PHP Tutorial](https://www.w3schools.com/php/)
- [RegExr - Probador de expresiones regulares](https://regexr.com/)

---

## Mapa de archivos del modulo

```
13-php-fundamentos/
|-- tarea1_NEMB.php              -> Funciones, bucles for, str_repeat(), piramides
|-- expReg_NEMB.php              -> Expresiones regulares: email, CURP, decimales
|-- TareaFormulario_NEMB/
|   |-- formulario.php           -> Formulario de registro + $_POST + $_SESSION
|   |-- login.php                -> Autenticacion + header(Location) + exit()
|   |-- info.php                 -> Lectura de sesion + foreach + tablas HTML
|   |-- usuario.php              -> Datos precargados (simula base de datos)
|   |-- logout.php               -> Cierre de sesion
|   |-- estilos.css              -> Estilos CSS: Flexbox, variables, box model
|-- CONCEPTOS.md                 -> Este archivo
```

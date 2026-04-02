<!-- Expresiones Regulares con PHP
INSTRUCCIONES
Realizar una expresión regular que detecte emails correctos.
Realizar una expresión regular que detecte Curps Correctos
es decir que permita usar únicamente estos caracteres: ABCD123456EFGHIJ78.
Realizar una expresión regular que detecte palabras de longitud mayor a 50 formadas solo por letras.
Crea una función para escapar los símbolos especiales.
Crear una expresión regular para detectar números decimales. -->

<!--
=============================================================================
EXPRESIONES REGULARES EN PHP
=============================================================================

CONCEPTOS CLAVE EN ESTE ARCHIVO:
---------------------------------

1. EXPRESIONES REGULARES (REGEX):
   Son patrones de texto que describen un conjunto de cadenas posibles.
   Se usan para VALIDAR, BUSCAR y REEMPLAZAR texto.

   En PHP, los patrones se encierran entre delimitadores (generalmente /.../)

   SINTAXIS BASICA DE REGEX:
   -------------------------
   ^        -> Inicio de la cadena
   $        -> Final de la cadena
   [a-z]    -> Cualquier letra minuscula de la 'a' a la 'z'
   [A-Z]    -> Cualquier letra mayuscula
   [0-9]    -> Cualquier digito
   [a-zA-Z] -> Cualquier letra (mayuscula o minuscula)
   .        -> Cualquier caracter (excepto salto de linea)
   +        -> Uno o mas del caracter/grupo anterior
   *        -> Cero o mas del caracter/grupo anterior
   ?        -> Cero o uno del caracter/grupo anterior (opcional)
   {n}      -> Exactamente n repeticiones
   {n,}     -> n o mas repeticiones
   {n,m}    -> Entre n y m repeticiones
   \.       -> Un punto literal (el backslash "escapa" el punto)
   ()       -> Agrupa una sub-expresion

2. preg_match($patron, $cadena):
   Funcion de PHP que evalua si una cadena coincide con un patron regex.
   Retorna 1 si hay coincidencia, 0 si no la hay, o FALSE si hay error.
   El prefijo "preg" viene de "Perl-compatible Regular Expressions" (PCRE).

3. htmlspecialchars($cadena):
   Funcion de seguridad que convierte caracteres especiales de HTML
   en sus entidades equivalentes para PREVENIR ataques XSS.
   Ejemplo: < se convierte en &lt;   > se convierte en &gt;

   SEGURIDAD - XSS (Cross-Site Scripting):
   Si un usuario ingresa <script>alert('hack')</script> en un formulario
   y lo mostramos sin escapar, el navegador ejecutaria ese JavaScript.
   htmlspecialchars() evita esto convirtiendo < y > en texto inofensivo.

ANALOGIA CON PYTHON:
---------------------
   PHP:    preg_match("/patron/", $cadena)
   Python: re.match(r"patron", cadena)

   Ambos usan la misma sintaxis de regex, pero PHP requiere delimitadores (/ /)
   y Python usa el prefijo r"" para raw strings.
-->

<?php

// ==========================================================================
// 1. EXPRESION REGULAR PARA VALIDAR EMAILS
// ==========================================================================
//
// Patron: /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/
//
// Desglose del patron:
// ^                    -> La cadena DEBE empezar aqui (no permite texto antes)
// [a-zA-Z0-9._-]+     -> Parte local del email (antes del @):
//                         Letras, numeros, puntos, guiones bajos, guiones
//                         El + significa "uno o mas caracteres"
// @                    -> El arroba literal (obligatorio en todo email)
// [a-zA-Z0-9.-]+      -> Dominio: letras, numeros, puntos, guiones
// \.                   -> Un punto literal (separa dominio de extension)
//                         Se usa \. porque el punto solo (.) significa "cualquier caracter"
// [a-zA-Z]{2,6}       -> Extension: solo letras, entre 2 y 6 caracteres
//                         Ejemplos validos: com, mx, org, museum
// $                    -> La cadena DEBE terminar aqui (no permite texto despues)
//
// EJEMPLOS:
//   "usuario@dominio.com"     -> VALIDO
//   "user.name@sub.dom.mx"   -> VALIDO
//   "@dominio.com"            -> INVALIDO (falta parte local)
//   "usuario@.com"            -> INVALIDO (dominio vacio)
//   "usuario@dominio"         -> INVALIDO (falta extension)

// Expresion regular para emails
$email = "      ";
$expRegEmail = "/^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/";

// preg_match() retorna 1 (verdadero) si el patron coincide con la cadena
// En este caso, $email son espacios en blanco, asi que NO coincidira
if (preg_match($expRegEmail, $email)) {
    echo "El email es correcto";
} else {
    echo "El email es incorrecto";
}
echo "<br>";

// ==========================================================================
// 2. EXPRESION REGULAR PARA VALIDAR CURP
// ==========================================================================
//
// CURP (Clave Unica de Registro de Poblacion) tiene el formato:
// 4 letras + 6 digitos + 6 letras + 2 digitos = 18 caracteres
//
// Patron: /^[A-Z]{4}[0-9]{6}[A-Z]{6}[0-9]{2}$/
//
// Desglose:
// ^             -> Inicio de cadena
// [A-Z]{4}      -> Exactamente 4 letras mayusculas (iniciales del nombre)
// [0-9]{6}      -> Exactamente 6 digitos (fecha de nacimiento: AAMMDD)
// [A-Z]{6}      -> Exactamente 6 letras mayusculas (datos adicionales)
// [0-9]{2}      -> Exactamente 2 digitos (homoclave)
// $             -> Final de cadena
//
// Ejemplo: ABCD123456EFGHIJ78
//          ^^^^              -> 4 letras
//              ^^^^^^        -> 6 numeros
//                    ^^^^^^  -> 6 letras
//                          ^^-> 2 numeros

// Expresion regular para Curps
$curp = "ABCD123456EFGHIJ78";
$expRegCurp = "/^[A-Z]{4}[0-9]{6}[A-Z]{6}[0-9]{2}$/";
if (preg_match($expRegCurp, $curp)) {
    echo "La curp es correcta";
} else {
    echo "La curp es incorrecta";
}
echo "<br>";

// ==========================================================================
// 3. EXPRESION REGULAR PARA PALABRAS LARGAS (>50 CARACTERES, SOLO LETRAS)
// ==========================================================================
//
// Patron: /^[a-zA-Z]{50,}$/
//
// Desglose:
// ^              -> Inicio de cadena
// [a-zA-Z]       -> Solo letras (mayusculas y minusculas)
// {50,}          -> MINIMO 50 caracteres (sin limite maximo)
//                   {50} seria exactamente 50
//                   {50,100} seria entre 50 y 100
// $              -> Final de cadena
//
// NOTA: Este patron rechaza espacios, numeros y caracteres especiales.
// Solo palabras formadas UNICAMENTE por letras alfabeticas.

// Expresion regular para palabras de longitud mayor a 50 formadas solo por letras
$palabra = "    ";
$expRegPalabra = "/^[a-zA-Z]{50,}$/";
if (preg_match($expRegPalabra, $palabra)) {
    echo "La palabra es correcta";
} else {
    echo "La palabra es incorrecta";
}
echo "<br>";

// ==========================================================================
// 4. FUNCION PARA ESCAPAR SIMBOLOS ESPECIALES (SEGURIDAD)
// ==========================================================================
//
// htmlspecialchars() convierte caracteres peligrosos en entidades HTML:
//   &  ->  &amp;     (ampersand)
//   "  ->  &quot;    (comillas dobles)
//   '  ->  &#039;   (comilla simple)
//   <  ->  &lt;      (menor que)
//   >  ->  &gt;      (mayor que)
//
// POR QUE ES IMPORTANTE:
// Sin esta funcion, un atacante podria inyectar codigo JavaScript:
//   Input malicioso: <script>document.cookie</script>
//   Sin escapar:     el navegador EJECUTA el script (robo de cookies!)
//   Con escapar:     se muestra como texto inofensivo: &lt;script&gt;...
//
// REGLA DE ORO: NUNCA confies en datos del usuario. SIEMPRE escapa
// cualquier dato que vayas a mostrar en HTML.

// Funcion para escapar los simbolos especiales
function escaparSimbolos($cadena)
{
    // htmlspecialchars() es la funcion mas basica de proteccion contra XSS
    // Para mayor seguridad, se puede agregar el segundo parametro:
    // htmlspecialchars($cadena, ENT_QUOTES, 'UTF-8')
    $cadena = htmlspecialchars($cadena);
    return $cadena;
}

// ==========================================================================
// 5. EXPRESION REGULAR PARA NUMEROS DECIMALES
// ==========================================================================
//
// Patron: /^[0-9]+(\.[0-9]+)?$/
//
// Desglose:
// ^              -> Inicio de cadena
// [0-9]+         -> Uno o mas digitos (parte entera obligatoria)
// (              -> Inicio de grupo
//   \.           -> Un punto literal (separador decimal)
//   [0-9]+       -> Uno o mas digitos (parte decimal)
// )              -> Fin de grupo
// ?              -> El grupo anterior es OPCIONAL (el ? hace que 0 o 1 vez)
//                   Esto permite tanto "123" como "123.456"
// $              -> Final de cadena
//
// EJEMPLOS:
//   "123"       -> VALIDO (entero sin decimales)
//   "123.456"   -> VALIDO (decimal)
//   "0.5"       -> VALIDO
//   ".5"        -> INVALIDO (falta parte entera)
//   "123."      -> INVALIDO (falta parte decimal despues del punto)
//   "12.34.56"  -> INVALIDO (mas de un punto)
//   "abc"       -> INVALIDO (no son numeros)

// Expresion regular para detectar numeros decimales
$numero = "123.456";
$expRegNumero = "/^[0-9]+(\.[0-9]+)?$/";
if (preg_match($expRegNumero, $numero)) {
    echo "El numero es correcto";
} else {
    echo "El numero es incorrecto";
}
?>

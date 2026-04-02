<!--
Natalia Edith Mejia Bautista
Tarea 1. Script que genere una piramide dado un simbolo y un número de filas -->

<!--
=============================================================================
TAREA 1: PIRAMIDE Y ROMBO CON PHP
=============================================================================

CONCEPTOS CLAVE EN ESTE ARCHIVO:
---------------------------------
1. ETIQUETAS PHP: <?php ... ?> delimitan el codigo PHP dentro de HTML.
   Todo lo que este fuera de estas etiquetas se envia al navegador como HTML puro.

2. FUNCIONES: Se definen con la palabra clave 'function'. Permiten reutilizar
   bloques de codigo. Reciben parametros entre parentesis y pueden retornar valores.
   Sintaxis: function nombre($param1, $param2) { ... }

3. VARIABLES: En PHP todas las variables comienzan con $ (signo de dolar).
   No se declara el tipo, PHP lo infiere automaticamente (tipado dinamico).

4. BUCLES FOR: Estructura de control que repite un bloque de codigo.
   Sintaxis: for (inicializacion; condicion; incremento) { ... }
   - $i = 1       -> se ejecuta UNA vez al inicio
   - $i <= $filas -> se evalua ANTES de cada iteracion
   - $i++         -> se ejecuta DESPUES de cada iteracion

5. str_repeat($cadena, $veces): Funcion nativa de PHP que repite una cadena
   de texto un numero determinado de veces.
   Ejemplo: str_repeat("*", 3) produce "***"

6. CONCATENACION: En PHP se usa el punto (.) para unir cadenas.
   Ejemplo: "Hola" . " " . "mundo" produce "Hola mundo"
   NOTA: Esto es diferente a Python (que usa +) y a JavaScript (que usa +).

7. echo: Sentencia de PHP para enviar texto al navegador. No es una funcion,
   es una construccion del lenguaje. Puede usarse con o sin parentesis.

8. MEZCLA PHP + HTML: PHP puede generar etiquetas HTML dinamicamente.
   El servidor ejecuta el PHP y envia el HTML resultante al navegador.
   El navegador NUNCA ve el codigo PHP, solo el HTML generado.

FLUJO DE EJECUCION:
-------------------
1. El servidor web (Apache) recibe la solicitud del navegador
2. Detecta que es un archivo .php y lo pasa al interprete PHP
3. PHP ejecuta el codigo y genera HTML
4. El HTML resultante se envia al navegador
5. El navegador renderiza el HTML (incluyendo los emojis y <center>)
-->

<?php

/**
 * ==========================================================================
 * FUNCION piramide()
 * ==========================================================================
 * Genera una piramide de texto centrada en HTML.
 *
 * COMO FUNCIONA:
 * - Recibe el numero de filas y un simbolo
 * - En cada iteracion, repite el simbolo un numero creciente de veces
 * - Usa la etiqueta HTML <center> para centrar cada fila
 *
 * Ejemplo con 4 filas y simbolo "*":
 *     *          (fila 1: 1 simbolo)
 *    **          (fila 2: 2 simbolos)
 *   ***          (fila 3: 3 simbolos)
 *  ****          (fila 4: 4 simbolos)
 *
 * @param int    $filas   - Numero de filas de la piramide
 * @param string $simbolo - Caracter o emoji a repetir
 *
 * NOTA SOBRE PARAMETROS:
 * En PHP, los parametros se pasan por valor por defecto.
 * Esto significa que la funcion trabaja con una COPIA del valor original.
 * Si quisieramos pasar por referencia, usariamos & : function piramide(&$filas, $simbolo)
 */
function piramide($filas, $simbolo){
    //recorrer las filas
    // El bucle for va de 1 hasta $filas (inclusive gracias a <=)
    // En la primera iteracion $i=1, en la ultima $i=$filas
    for ($i = 1; $i <= $filas; $i++) {
        //repetir el simbolo para la fila
        // str_repeat() es una funcion nativa (built-in) de PHP
        // Repite $simbolo exactamente $i veces
        // Cuando $i = 1, produce un simbolo; cuando $i = 5, produce cinco
        $piramide = str_repeat($simbolo, $i);

        //centrar la piramide
        // Aqui se concatena HTML con el contenido generado por PHP
        // El operador punto (.) une las cadenas:
        //   "<center>" . $piramide . "</center>"
        // Ejemplo: "<center>***</center>"
        $pirCentrada = "<center>" . $piramide . "</center>";

        // echo envia el HTML al navegador
        // El navegador recibira algo como: <center>***</center>
        echo $pirCentrada . " ";
    }
}

/**
 * ==========================================================================
 * FUNCION rombo()
 * ==========================================================================
 * Genera un rombo (diamante) de texto centrado en HTML.
 *
 * COMO FUNCIONA:
 * Un rombo es una piramide + una piramide invertida.
 * - Primera mitad: crece de 1 a $filas simbolos (igual que piramide)
 * - Segunda mitad: decrece de ($filas - 1) a 1 simbolo
 *
 * Ejemplo con 4 filas y simbolo "*":
 *     *          (fila 1: crece)
 *    **          (fila 2: crece)
 *   ***          (fila 3: crece)
 *  ****          (fila 4: crece - punto maximo)
 *   ***          (fila 3: decrece)
 *    **          (fila 2: decrece)
 *     *          (fila 1: decrece)
 *
 * NOTA SOBRE EL SEGUNDO BUCLE:
 * Inicia en ($filas - 1) para NO repetir la fila central del rombo.
 * Si empezara en $filas, la fila mas ancha apareceria dos veces.
 *
 * @param int    $filas   - Numero de filas (mitad superior del rombo)
 * @param string $simbolo - Caracter o emoji a repetir
 */
function rombo($filas, $simbolo){
    //Parte superior del rombo
    // Bucle ascendente: de 1 a $filas
    for ($i = 1; $i <= $filas; $i++) {
        //repetir el simbolo para la fila
        $piramide = str_repeat($simbolo, $i);
        //centrar la piramide
        $pirCentrada = "<center>" . $piramide . "</center>";
        echo $pirCentrada;
    }
    //Parte inferior del rombo
    // Bucle DESCENDENTE: de ($filas - 1) hasta 1
    // NOTA: Se usa $i-- para decrementar (restar 1 en cada iteracion)
    // Se empieza en $filas - 1 para no duplicar la fila central
    for ($i = $filas - 1; $i >= 1; $i--) {
        //repetir el simbolo para la fila
        $piramide = str_repeat($simbolo, $i);
        //centrar la piramide
        $pirCentrada = "<center>" . $piramide . "</center>";
        echo $pirCentrada;
    }
}

// ==========================================================================
// CODIGO PRINCIPAL - EJECUCION
// ==========================================================================
// Aqui es donde se "llama" o "invoca" a las funciones definidas arriba.
// PHP ejecuta este codigo de arriba hacia abajo (secuencialmente).

// Definimos las variables que usaremos como argumentos
// $filas es de tipo int (entero), $simbolo es de tipo string (cadena)
//llamada a las funciones
$filas = 10;
$simbolo = "🌟";

// echo puede enviar etiquetas HTML directamente al navegador
// Estas etiquetas se renderizan como titulos en la pagina
echo "<h2> Natalia Edith Mejia Bautista </h2>";
echo "<h1> Tarea 1 </h1>";
echo "<h3> Piramide </h3>";

// Llamada a la funcion piramide: se pasan $filas y $simbolo como argumentos
// Los argumentos se copian en los parametros de la funcion
piramide($filas, $simbolo);

echo "<h3> Rombo </h3>";

// Llamada a la funcion rombo con los mismos argumentos
rombo($filas, $simbolo);


?>

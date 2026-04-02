// =============================================================================
// MODULO 12 - JAVASCRIPT FUNDAMENTOS: EVENTOS DEL DOM
// =============================================================================
//
// NIVEL: Intermedio
// TEMA: DOMContentLoaded, onclick, onmouseover, getElementById
//
// CONCEPTOS CLAVE DE ESTE ARCHIVO:
// ---------------------------------
//
// 1. DOMContentLoaded:
//    Este evento se dispara cuando el HTML ha sido completamente cargado y
//    parseado, sin esperar a que las hojas de estilo, imagenes y subframes
//    terminen de cargar.
//
//    Es ESENCIAL cuando el <script> esta en el <head> o al inicio del <body>,
//    porque en ese momento los elementos HTML aun no existen en el DOM.
//    Sin DOMContentLoaded, document.getElementById("boton") retornaria null.
//
//    ALTERNATIVAS:
//    - window.onload: Espera a que TODO cargue (imagenes, CSS, etc.) -> mas lento
//    - DOMContentLoaded: Solo espera al HTML -> mas rapido, suficiente casi siempre
//    - defer en <script>: El script se ejecuta despues de parsear el HTML
//    - Poner <script> al final del body: Los elementos ya existen
//
// 2. document.getElementById():
//    Busca en TODO el documento un elemento con el ID especificado.
//    - Retorna el elemento si lo encuentra.
//    - Retorna null si no lo encuentra.
//    BUENA PRACTICA: Verificar que no sea null antes de usarlo:
//      const btn = document.getElementById("boton");
//      if (btn) { btn.onclick = hacerClick; }
//
// 3. EVENTOS (onclick, onmouseover):
//    Los eventos son acciones que ocurren en la pagina: clicks, movimientos
//    del mouse, teclas presionadas, carga de la pagina, etc.
//
//    FORMAS DE ASIGNAR EVENTOS:
//    a) Propiedad del elemento (usada aqui):
//       elemento.onclick = funcion;
//       - Simple y directa.
//       - Solo permite UN handler por evento.
//
//    b) addEventListener (recomendada):
//       elemento.addEventListener("click", funcion);
//       - Permite MULTIPLES handlers para el mismo evento.
//       - Permite remover handlers con removeEventListener.
//       - Soporta la fase de captura (tercer parametro).
//
//    c) Atributo HTML (NO recomendada):
//       <button onclick="hacerClick()">Click</button>
//       - Mezcla HTML con JavaScript.
//       - Dificil de mantener y depurar.
//       - Problema de seguridad: Content Security Policy puede bloquearlo.
//
// 4. alert():
//    Muestra un cuadro de dialogo modal con un mensaje.
//    "Modal" significa que BLOQUEA la interaccion con la pagina hasta que
//    el usuario cierra el dialogo.
//    EN LA PRACTICA: alert() casi nunca se usa en produccion.
//    Se prefieren modales de CSS/Bootstrap o notificaciones no intrusivas.
//
// TIPOS DE EVENTOS COMUNES:
// --------------------------
// | Evento         | Se dispara cuando...                        |
// |----------------|---------------------------------------------|
// | click          | El usuario hace click                       |
// | dblclick       | Doble click                                 |
// | mouseover      | El cursor entra al elemento                 |
// | mouseout       | El cursor sale del elemento                 |
// | mousedown      | Se presiona un boton del mouse               |
// | mouseup        | Se suelta un boton del mouse                 |
// | keydown        | Se presiona una tecla                       |
// | keyup          | Se suelta una tecla                         |
// | submit         | Se envia un formulario                      |
// | change         | Cambia el valor de un input/select           |
// | focus          | Un elemento recibe el foco                  |
// | blur           | Un elemento pierde el foco                  |
// | load           | Un recurso termina de cargar                |
// | scroll         | El usuario hace scroll                      |
//
// COMPARACION CON PYTHON (para quienes vienen del modulo 11):
// -----------------------------------------------------------
// Python no tiene manejo de eventos del DOM de forma nativa porque
// no es un lenguaje de navegador. Para interfaces graficas en Python
// se usa tkinter:
//   boton = Button(root, text="Click", command=mi_funcion)
// En JavaScript, los eventos son el CORAZON de la interactividad web.
// =============================================================================

//script que asigne un evento a un botón y a una imagen.

// DOMContentLoaded: Esperamos a que todo el HTML se haya cargado.
// La funcion anonima (function() { ... }) es un CALLBACK: una funcion
// que se pasara como argumento y se ejecutara DESPUES, cuando ocurra el evento.
//
// Este patron es fundamental en JavaScript: como el lenguaje es ASINCRONO,
// muchas operaciones usan callbacks para ejecutar codigo "cuando algo pase".
document.addEventListener("DOMContentLoaded", function() {

    // Definimos las funciones que se ejecutaran cuando ocurran los eventos.
    // Estas funciones se llaman "event handlers" (manejadores de eventos).

    // Handler para el evento click del boton.
    // Se define como funcion tradicional (function declaration) dentro
    // del callback de DOMContentLoaded.
    // NOTA: Esta funcion solo es accesible dentro de este bloque (scope local).
    function hacerClick(){
        alert("Has dado click al botón");
    }

    // Handler para el evento mouseover de la imagen.
    // onmouseover se dispara cuando el cursor ENTRA en el area del elemento.
    // CUIDADO: En la practica, usar alert() en mouseover es mala idea porque
    // se dispara constantemente y bloquea la pagina.
    function pasarMouse(){
        alert("Has pasado el cursor sobre la imagen");
    }

    // getElementById retorna una REFERENCIA al elemento HTML.
    // A partir de ahi, podemos modificar sus propiedades, estilos,
    // contenido y asignarle eventos.
    //
    // 'let' se usa aqui, aunque 'const' seria mas apropiado ya que
    // la referencia al elemento no cambiara despues de asignarse.
    let botoncito = document.getElementById("boton");

    // Asignacion de evento via propiedad:
    // botoncito.onclick recibe una REFERENCIA a la funcion (sin parentesis).
    // - hacerClick      -> Referencia a la funcion (CORRECTO)
    // - hacerClick()    -> EJECUTA la funcion inmediatamente (INCORRECTO aqui)
    //
    // Este es un error MUY comun en principiantes:
    //   botoncito.onclick = hacerClick();   // MAL: ejecuta la funcion YA
    //   botoncito.onclick = hacerClick;     // BIEN: pasa la referencia
    botoncito.onclick = hacerClick;

    // Lo mismo para la imagen con el evento onmouseover.
    let imagen = document.getElementById("imagen");
    imagen.onmouseover = pasarMouse;

    // NOTA: Estos eventos se podrian asignar tambien con addEventListener:
    //   botoncito.addEventListener("click", hacerClick);
    //   imagen.addEventListener("mouseover", pasarMouse);
    // La ventaja de addEventListener es que permite agregar multiples handlers.
});

// =============================================================================
// EVENT BUBBLING (BURBUJEO DE EVENTOS):
// Cuando haces click en el boton, el evento "sube" por el arbol del DOM:
//   button -> body -> html -> document
// Cada ancestro tiene la oportunidad de reaccionar al evento.
// Esto se llama "bubbling" y es la razon por la que funciona la "delegacion
// de eventos" (event delegation), un patron avanzado muy util.
//
// EJERCICIOS SUGERIDOS:
// 1. Cambia onclick por addEventListener y agrega DOS handlers al mismo boton.
// 2. En vez de alert, cambia el texto del boton con: botoncito.textContent = "Clickeado!"
// 3. Agrega un evento 'mouseout' a la imagen que cambie su borde.
// 4. Agrega un evento 'keydown' al documento que muestre la tecla presionada.
// 5. Usa el objeto 'event' para mostrar las coordenadas del click:
//    function hacerClick(event) { console.log(event.clientX, event.clientY); }
// =============================================================================

// =============================================================================
// MODULO 12 - PRACTICA FINAL: VALIDACION DE FORMULARIO
// =============================================================================
//
// NIVEL: Avanzado
// TEMA: Validacion de formularios con jQuery Form Validator, restrictLength
//
// CONCEPTOS CLAVE DE ESTE ARCHIVO:
// ---------------------------------
//
// 1. VALIDACION DE FORMULARIOS:
//    La validacion es el proceso de verificar que los datos del usuario
//    cumplan con ciertos criterios ANTES de enviarlos al servidor.
//
//    TIPOS DE VALIDACION:
//    a) Del lado del cliente (frontend) - Lo que hace este archivo:
//       - Se ejecuta en el navegador del usuario.
//       - Retroalimentacion inmediata (sin esperar al servidor).
//       - Se puede saltar facilmente (deshabilitando JS o modificando el HTML).
//       - NUNCA es suficiente por si sola.
//
//    b) Del lado del servidor (backend) - NO implementado aqui:
//       - Se ejecuta en el servidor.
//       - Es la validacion REAL y segura.
//       - No se puede saltar desde el navegador.
//       - SIEMPRE es necesaria, incluso si hay validacion frontend.
//
//    REGLA DE ORO: La validacion frontend mejora la UX (experiencia de usuario);
//    la validacion backend garantiza la seguridad.
//
// 2. $.validate() - JQUERY FORM VALIDATOR:
//    Es un plugin de jQuery que automatiza la validacion de formularios.
//    Se configura con un objeto de opciones:
//
//    - form: Selector CSS del formulario a validar.
//      '#form-registro' selecciona el formulario con id="form-registro".
//
//    - modules: Modulos adicionales de validacion.
//      'location': Validacion de ubicacion (pais, ciudad, etc.)
//      'date': Validacion de fechas
//      'security': Validacion de contrasenas fuertes
//      'file': Validacion de archivos (tipo, tamano)
//      NOTA: No todos los modulos se usan en este formulario, pero se cargan
//      por si se necesitan. En produccion, solo cargar los necesarios.
//
//    - lang: Idioma para los mensajes de error.
//      'es' = español. Los mensajes de error se mostraran en español:
//      "Este campo es obligatorio" en vez de "This field is required".
//
//    COMO FUNCIONA INTERNAMENTE:
//    a) El plugin intercepta el evento 'submit' del formulario.
//    b) Recorre todos los campos con atributos data-validation.
//    c) Ejecuta las reglas de validacion correspondientes.
//    d) Si algun campo falla:
//       - Muestra un mensaje de error debajo del campo.
//       - Agrega clases CSS de error al campo (borde rojo).
//       - IMPIDE el envio del formulario (preventDefault).
//    e) Si todos los campos pasan: Permite el envio normal.
//
// 3. .restrictLength() - LIMITE DE CARACTERES:
//    Este metodo (proporcionado por el plugin) limita la cantidad de
//    caracteres que se pueden escribir en un textarea/input y muestra
//    un contador en tiempo real.
//
//    $('#comentario').restrictLength($('#maxlength'));
//    - '#comentario': El textarea a limitar.
//    - '#maxlength': El <span> donde se muestra el conteo (restan X caracteres).
//
//    COMO FUNCIONA:
//    a) Lee el valor inicial del span (50 en este caso) como limite maximo.
//    b) Escucha los eventos 'keyup' e 'input' del textarea.
//    c) Al escribir, calcula: restantes = limite - textoActual.length
//    d) Actualiza el span con el numero restante.
//    e) Si se alcanza el limite, impide escribir mas.
//
//    ALTERNATIVA SIN PLUGIN (vanilla JS):
//    const textarea = document.getElementById('comentario');
//    const contador = document.getElementById('maxlength');
//    const maxLength = 50;
//    textarea.setAttribute('maxlength', maxLength);
//    textarea.addEventListener('input', function() {
//        contador.textContent = maxLength - this.value.length;
//    });
//
// 4. $(document).ready() VS ALTERNATIVAS:
//    $(document).ready(function() { ... });  // jQuery clasico
//    $(function() { ... });                  // jQuery abreviado
//    document.addEventListener('DOMContentLoaded', function() { ... }); // Nativo
//
// COMPARACION CON PYTHON (para quienes vienen del modulo 11):
// -----------------------------------------------------------
// En Python con Flask, la validacion se hace con WTForms:
//   class RegistroForm(FlaskForm):
//       nombre = StringField('Nombre', validators=[DataRequired()])
//       email = EmailField('Email', validators=[Email()])
//       password = PasswordField('Password', validators=[Length(min=8)])
//
// En Django, se usa la clase Form:
//   class RegistroForm(forms.Form):
//       nombre = forms.CharField(max_length=100)
//       email = forms.EmailField()
//
// La diferencia: en Python la validacion ocurre en el SERVIDOR.
// Aqui la validacion ocurre en el NAVEGADOR (cliente).
// =============================================================================

// $(document).ready(): Espera a que el DOM este cargado.
// Dentro se inicializa la validacion del formulario.
$( document ).ready(function() {

  // $.validate(): Inicializa la validacion para el formulario especificado.
  // Las reglas de validacion estan definidas en el HTML con atributos data-validation.
  // Este metodo solo necesita saber CUAL formulario validar y las opciones generales.
  //
  // REGLAS DEFINIDAS EN EL HTML (formulario.html):
  // - Nombre: required + alphanumeric (con espacios permitidos)
  // - Email: email
  // - Password: length min8
  // - Confirmacion: confirmation (debe coincidir con password)
  // - Genero: required (debe seleccionar una opcion)
  // - Comentario: alphanumeric + optional (no es obligatorio)
  $.validate({
  	form: '#form-registro',
    modules : 'location, date, security, file',
    lang: 'es'
  });

  // restrictLength: Limita los caracteres del textarea y actualiza el contador.
  // El argumento es el elemento jQuery donde se muestra el conteo restante.
  // En formulario.html: <span id="maxlength">50</span>
  // Al escribir en #comentario, el span se actualiza: 50, 49, 48...
  //
  // NOTA: El limite se toma del contenido inicial del span (50).
  // Si cambias el span a <span id="maxlength">100</span>, el limite seria 100.

  // Restrict presentation length
  $('#comentario').restrictLength($('#maxlength'));
});

// =============================================================================
// FLUJO COMPLETO DE VALIDACION:
//
// 1. La pagina carga -> $(document).ready() se ejecuta.
// 2. $.validate() intercepta el evento 'submit' del formulario.
// 3. restrictLength() comienza a escuchar cambios en el textarea.
// 4. El usuario llena los campos y hace click en "Submit".
// 5. El plugin recorre cada campo y verifica sus reglas:
//    - Nombre: tiene contenido? es alfanumerico?
//    - Email: tiene formato valido de email?
//    - Password: tiene al menos 8 caracteres?
//    - Confirmacion: coincide con el password?
//    - Genero: se selecciono una opcion?
//    - Comentario: si tiene contenido, es alfanumerico?
// 6. Si alguna regla falla:
//    - Se muestra un mensaje de error en español debajo del campo.
//    - El formulario NO se envia.
//    - El usuario puede corregir y volver a intentar.
// 7. Si todas las reglas pasan:
//    - El formulario se envia al servidor (action del form).
//    - Como action="" esta vacio, la pagina se recarga.
//
// EJERCICIOS SUGERIDOS:
// 1. Agrega un campo "telefono" con validacion de numeros (data-validation="number")
// 2. Cambia el formulario para que use AJAX ($.ajax()) en vez de submit tradicional
// 3. Agrega validacion de contrasena fuerte (mayusculas, numeros, simbolos)
// 4. Muestra un modal de "Registro exitoso" en vez de recargar la pagina
// 5. Implementa la misma validacion con JavaScript puro (sin plugin)
// =============================================================================

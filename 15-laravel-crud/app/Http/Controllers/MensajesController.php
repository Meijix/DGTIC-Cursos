<?php
/*
|==========================================================================
| MensajesController.php - Controlador para el Formulario de Contacto
|==========================================================================
|
| Este controlador maneja el envio de correos electronicos desde el
| formulario de contacto de la aplicacion.
|
| FLUJO DEL ENVIO DE CORREO:
|   1. Usuario llena el formulario en /contacto (vista contacto.blade.php)
|   2. El formulario envia los datos via POST a /contacto
|   3. Este controlador valida los datos
|   4. Se crea un objeto Mailable (MensajeRecibido)
|   5. Se envia el correo usando la fachada Mail
|   6. Se redirige al usuario a la pagina principal
|
| CONFIGURACION DE CORREO EN LARAVEL:
| - Se configura en el archivo .env con las variables:
|   MAIL_MAILER=smtp
|   MAIL_HOST=smtp.gmail.com (o el servidor que uses)
|   MAIL_PORT=587
|   MAIL_USERNAME=tu_correo@gmail.com
|   MAIL_PASSWORD=tu_contrasenya_de_aplicacion
|   MAIL_ENCRYPTION=tls
|   MAIL_FROM_ADDRESS=tu_correo@gmail.com
|   MAIL_FROM_NAME="Nombre de tu App"
|
| - Para desarrollo se puede usar Mailtrap (servicio gratuito) o
|   configurar MAIL_MAILER=log para ver los correos en storage/logs/
|
*/

namespace App\Http\Controllers;

use Illuminate\Http\Request;

// Fachada (Facade) Mail: proporciona una interfaz sencilla para enviar correos.
// Las fachadas en Laravel son "atajos" a servicios del contenedor de dependencias.
// En vez de inyectar el servicio completo, usamos Mail::to()->send()
USE Illuminate\Support\Facades\Mail;

// Importamos la clase Mailable personalizada que define el contenido del correo
use App\Mail\MensajeRecibido;

/*
|--------------------------------------------------------------------------
| Clase MensajesController
|--------------------------------------------------------------------------
| Controlador dedicado exclusivamente al procesamiento del formulario
| de contacto. Solo tiene un metodo (store) porque no necesitamos
| CRUD completo para mensajes de contacto.
|
| NOTA: Podriamos haber usado un "Single Action Controller" con __invoke():
|   class MensajesController extends Controller {
|       public function __invoke() { ... }
|   }
|   Y en la ruta: Route::post('/contacto', MensajesController::class);
*/
class MensajesController extends Controller
{
    /*
    |----------------------------------------------------------------------
    | STORE - Procesar y enviar el mensaje de contacto
    |----------------------------------------------------------------------
    |
    | VALIDACION CON MENSAJES PERSONALIZADOS:
    | - request()->validate() acepta dos arrays:
    |   1er array: las reglas de validacion
    |   2do array: mensajes personalizados (opcional)
    | - Formato de mensajes: 'campo.regla' => 'Mensaje personalizado'
    | - __() es el helper de traduccion de Laravel (localizacion/i18n)
    |
    | REGLAS DE VALIDACION USADAS:
    | - 'required': el campo no puede estar vacio
    | - 'email': debe ser un formato de correo valido
    | - 'min:3': minimo 3 caracteres
    | - Se pueden encadenar con | : 'required|email|max:255'
    |
    | ENVIO DEL CORREO:
    | - Mail::to('destino'): destinatario principal
    | - ->cc($email): copia al remitente (Carbon Copy)
    | - ->send(new MensajeRecibido($message)): crea y envia el Mailable
    | - Tambien existe ->bcc() para copia oculta y ->queue() para envio asincrono
    |
    */
    public function store(){

        // validate() retorna los datos validados como array asociativo
        // Si la validacion falla, redirige automaticamente con errores
        $message = request()->validate([
            'nombre' => 'required',
            'email' => 'required|email',       // Debe ser email valido
            'asunto' => 'required',
            'mensaje' => 'required|min:3'      // Minimo 3 caracteres
        ],[
            // MENSAJES PERSONALIZADOS:
            // Formato: 'campo.regla' => 'mensaje'
            // __() permite traducir los mensajes si se usa localizacion
            'nombre.required' => __('Se requiere el nombre'),
            'email.required' =>__('Se requiere el correo'),
            'asunto.required' =>__('Se requiere el asunto'),
            'mensaje.required' => __('Se requiere el mensaje a enviar'),
        ]);

        // ENVIAR EL CORREO:
        // Mail::to()  -> define el destinatario
        // ->cc()      -> envia copia al email del remitente
        // ->send()    -> crea la instancia de MensajeRecibido y envia
        // new MensajeRecibido($message) -> pasa los datos validados al Mailable
        Mail::to('natalia.mejbau@gmail.com')->cc($message['email'])->send(new MensajeRecibido($message));

        // Redirige a la ruta con nombre 'index' (pagina principal)
        // NOTA: se podria agregar ->with('info', 'Mensaje enviado') para mostrar confirmacion
        return redirect()->route('index');//->with('info', 'Mensaje enviado');
    }

}

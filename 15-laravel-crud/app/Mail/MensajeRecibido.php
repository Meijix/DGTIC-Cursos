<?php
/*
|==========================================================================
| MensajeRecibido.php - Clase Mailable para Correos de Contacto
|==========================================================================
|
| SISTEMA DE CORREOS EN LARAVEL:
| Laravel usa clases "Mailable" para representar correos electronicos.
| Cada Mailable es una clase PHP que define:
|   1. El sobre (Envelope): asunto, remitente, etc.
|   2. El contenido (Content): vista Blade que genera el cuerpo HTML
|   3. Los adjuntos (Attachments): archivos a enviar
|
| COMO SE GENERA:
|   php artisan make:mail MensajeRecibido
|
| COMO SE ENVIA (desde un controlador):
|   Mail::to('destino@email.com')->send(new MensajeRecibido($datos));
|
| FLUJO COMPLETO DEL CORREO:
|   +-----------+     +-----------+     +----------+     +----------+
|   | Formulario| --> | Controller| --> | Mailable | --> | Servidor |
|   | contacto  |     | store()   |     | (clase)  |     |  SMTP    |
|   +-----------+     +-----------+     +----------+     +----------+
|                                            |
|                                            v
|                                      Vista Blade
|                                      (email HTML)
|
| OPCIONES DE ENVIO:
| - Mail::to()->send()   : envio sincrono (el usuario espera)
| - Mail::to()->queue()  : envio asincrono (en segundo plano, mas rapido)
| - Mail::to()->later()  : envio programado para despues
|
| PARA PRUEBAS:
| - Mailtrap (https://mailtrap.io): atrapa correos sin enviarlos realmente
| - MAIL_MAILER=log en .env: escribe correos en storage/logs/laravel.log
| - php artisan make:mail MensajeRecibido --markdown para correos con formato
|
*/

namespace App\Mail;

// Queueable: permite enviar el correo de forma asincrona con ->queue()
use Illuminate\Bus\Queueable;
use Illuminate\Contracts\Queue\ShouldQueue;

// Mailable: clase base que todas las clases de correo deben extender
use Illuminate\Mail\Mailable;

// Content y Envelope: definen la estructura del correo en Laravel 10+
use Illuminate\Mail\Mailables\Content;
use Illuminate\Mail\Mailables\Envelope;

// SerializesModels: permite pasar modelos Eloquent al correo de forma segura
use Illuminate\Queue\SerializesModels;

/*
|--------------------------------------------------------------------------
| Clase MensajeRecibido
|--------------------------------------------------------------------------
| Representa un correo electronico que se envia cuando un usuario
| llena el formulario de contacto.
|
| TRAITS UTILIZADOS:
| - Queueable: agrega metodos para encolar el correo (envio asincrono)
| - SerializesModels: si pasamos un modelo Eloquent, lo serializa
|   correctamente para la cola de trabajos
|
| PROPIEDADES PUBLICAS:
| Las propiedades publicas del Mailable estan disponibles automaticamente
| en la vista del correo. Si $msg es publica, en la vista podemos usar
| {{ $msg['nombre'] }}, {{ $msg['email'] }}, etc.
*/
class MensajeRecibido extends Mailable
{
    use Queueable, SerializesModels;

    // Propiedad publica: automaticamente disponible en la vista del correo
    // Contiene los datos validados del formulario de contacto:
    // ['nombre' => '...', 'email' => '...', 'asunto' => '...', 'mensaje' => '...']
    public $msg;

    /*
    |----------------------------------------------------------------------
    | Constructor - Recibe los datos del mensaje
    |----------------------------------------------------------------------
    | Se ejecuta cuando hacemos: new MensajeRecibido($message)
    | El parametro $mensaje contiene el array de datos validados
    | del formulario de contacto.
    |
    | Al asignar a $this->msg (propiedad publica), los datos quedan
    | disponibles en la vista del correo como la variable $msg.
    */
    /**
     * Create a new message instance.
     */
    public function __construct($mensaje)
    {
        // Almacena los datos del formulario para usarlos en la vista del correo
        $this->msg = $mensaje;
    }

    /*
    |----------------------------------------------------------------------
    | Envelope - Define el "sobre" del correo
    |----------------------------------------------------------------------
    | El Envelope contiene metadatos del correo:
    | - subject: el asunto que vera el destinatario
    | - from: remitente (si no se especifica, usa el de .env)
    | - replyTo: direccion para respuestas
    | - cc/bcc: copias y copias ocultas
    |
    | EJEMPLO CON MAS OPCIONES:
    |   return new Envelope(
    |       from: new Address('no-reply@app.com', 'Mi App'),
    |       replyTo: [$this->msg['email']],
    |       subject: 'Contacto: ' . $this->msg['asunto'],
    |   );
    */
    /**
     * Get the message envelope.
     */
    public function envelope(): Envelope
    {
        return new Envelope(
            // El asunto del correo que aparecera en la bandeja de entrada
            subject: 'Mensaje de tu app Recibido',
        );
    }

    /*
    |----------------------------------------------------------------------
    | Content - Define el contenido HTML del correo
    |----------------------------------------------------------------------
    | Especifica que vista Blade se usa para generar el cuerpo del correo.
    | 'view' busca en resources/views/, asi que:
    |   'emails.mensaje-recibido' -> resources/views/emails/mensaje-recibido.blade.php
    |
    | La vista tiene acceso a todas las propiedades publicas del Mailable.
    | En este caso, $msg esta disponible automaticamente.
    |
    | TIPOS DE CONTENIDO:
    | - view: vista Blade con HTML completo
    | - markdown: vista con componentes Blade de correo predefinidos
    | - text: version de texto plano del correo
    |
    | EJEMPLO CON MARKDOWN:
    |   return new Content(
    |       markdown: 'emails.mensaje-recibido',
    |       with: ['url' => 'https://miapp.com'],
    |   );
    */
    /**
     * Get the message content definition.
     */
    public function content(): Content
    {
        return new Content(
            // Vista que genera el HTML del correo
            // Ruta: resources/views/emails/mensaje-recibido.blade.php
            view: 'emails.mensaje-recibido',
        );
    }

    /*
    |----------------------------------------------------------------------
    | Attachments - Archivos adjuntos del correo
    |----------------------------------------------------------------------
    | Retorna un array de objetos Attachment.
    |
    | EJEMPLO DE ADJUNTOS:
    |   use Illuminate\Mail\Mailables\Attachment;
    |
    |   return [
    |       Attachment::fromPath('/ruta/al/archivo.pdf')
    |           ->as('reporte.pdf')
    |           ->withMime('application/pdf'),
    |       Attachment::fromStorage('archivos/imagen.jpg'),
    |   ];
    */
    /**
     * Get the attachments for the message.
     *
     * @return array<int, \Illuminate\Mail\Mailables\Attachment>
     */
    public function attachments(): array
    {
        // Sin adjuntos en este correo
        return [];
    }
}

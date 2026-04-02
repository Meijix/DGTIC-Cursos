{{--
|==========================================================================
| contacto.blade.php - Formulario de Contacto para Enviar Correos
|==========================================================================
|
| Este formulario permite a los usuarios enviar mensajes que se
| convierten en correos electronicos via el sistema de Mail de Laravel.
|
| FLUJO COMPLETO:
|   1. GET /contacto -> Closure en web.php -> muestra esta vista
|   2. Usuario llena nombre, email, asunto y mensaje
|   3. POST /contacto -> MensajesController@store
|   4. Se validan los datos (con mensajes personalizados en espanol)
|   5. Se crea un Mailable (MensajeRecibido) con los datos
|   6. Se envia via Mail::to()->send()
|   7. Redirige a la pagina principal
|
| CAMPOS DEL FORMULARIO:
| - nombre: nombre del remitente
| - email: correo del remitente (se usa para enviar copia con ->cc())
| - asunto: asunto del mensaje
| - mensaje: cuerpo del mensaje (textarea, minimo 3 caracteres)
|
| VALIDACION:
| Si la validacion falla en el controlador, Laravel redirige aqui
| automaticamente. Los errores se pueden mostrar con:
|   @error('campo') {{ $message }} @enderror
|   o con $errors->first('campo')
|
--}}

{{-- Hereda la estructura de plantilla.blade.php --}}
@extends('plantilla')
@section('contenido')
<!-- Contenido principal -->
<section class="content">
    <h1>Contáctanos</h1>

    {{-- FORMULARIO DE CONTACTO:
         - method=POST: envia datos al servidor
         - action="{{ route('contacto') }}": la ruta POST /contacto
         - @csrf: token de proteccion contra CSRF (obligatorio)
         - style="width: 40rem;": limita el ancho del formulario
    --}}
    <form method=POST action="{{route('contacto')}}" style="width: 40rem;">
        @csrf

        {{-- CAMPO NOMBRE:
             name="nombre" es la clave para acceder en el controlador.
             Validacion en el controlador: 'required'
             Si falla: mensaje personalizado 'Se requiere el nombre'
        --}}
        <!-- Name input -->
        <div data-mdb-input-init class="form-outline mb-4">
            <input type="text" id="nombre" name="nombre" class="form-control" />
            <label class="form-label" for="nombre">Nombre</label>
        </div>

        {{-- CAMPO EMAIL:
             type="email": validacion HTML5 del navegador (primera capa)
             Validacion en el controlador: 'required|email' (segunda capa)
             Siempre validar en el servidor, no confiar solo en el navegador.
        --}}
        <!-- Email input -->
        <div data-mdb-input-init class="form-outline mb-4">
            <input type="email" id="email" name="email" class="form-control" />
            <label class="form-label" for="email">Correo electronico</label>
        </div>

        <!-- Asunto input -->
        <div data-mdb-input-init class="form-outline mb-4">
            <input type="text" id="asunto" name="asunto" class="form-control" />
            <label class="form-label" for="asunto">Asunto</label>
        </div>

        {{-- CAMPO MENSAJE:
             textarea: para texto largo multilínea
             rows="4": altura inicial del campo
             Validacion: 'required|min:3' (minimo 3 caracteres)
        --}}
        <!-- Message input -->
        <div data-mdb-input-init class="form-outline mb-4">
            <textarea class="form-control" id="mensaje" name="mensaje" rows="4"></textarea>
            <label class="form-label" for="mensaje">Mensaje</label>
        </div>

        <!-- Submit button -->
        {{-- Al enviar, los datos van a MensajesController@store --}}
        {{-- El controlador los valida, crea el Mailable y envia el correo --}}
        <button data-mdb-ripple-init type="submit" class="btn btn-primary btn-block mb-4">Enviar</button>
    </form>

</section>

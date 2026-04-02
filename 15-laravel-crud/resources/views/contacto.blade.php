@extends('plantilla')
@section('contenido')
<!-- Contenido principal -->
<section class="content">
    <h1>Contáctanos</h1>

    <form method=POST action="{{route('contacto')}}" style="width: 40rem;">
        @csrf
        <!-- Name input -->
        <div data-mdb-input-init class="form-outline mb-4">
            <input type="text" id="nombre" name="nombre" class="form-control" />
            <label class="form-label" for="nombre">Nombre</label>
        </div>
        
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
        
        <!-- Message input -->
        <div data-mdb-input-init class="form-outline mb-4">
            <textarea class="form-control" id="mensaje" name="mensaje" rows="4"></textarea>
            <label class="form-label" for="mensaje">Mensaje</label>
        </div>
        
        <!-- Submit button -->
        <button data-mdb-ripple-init type="submit" class="btn btn-primary btn-block mb-4">Enviar</button>
    </form>

</section>
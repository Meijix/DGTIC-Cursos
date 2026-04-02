{{--
|==========================================================================
| editar.blade.php - Formulario para Editar un Curso Existente
|==========================================================================
|
| DIFERENCIAS CON agregar.blade.php:
| 1. El formulario llega con datos precargados (value="{{ $curso->nombre }}")
| 2. La accion apunta a la ruta 'update' con el ID del curso
| 3. Se edita un registro existente en vez de crear uno nuevo
|
| FLUJO DE EDICION:
|   1. Usuario hace clic en "Editar" en la tabla (GET /editar/{id})
|   2. CursoController@edit busca el curso y lo pasa a esta vista
|   3. Los campos se precargan con los valores actuales del curso
|   4. Usuario modifica los datos y envia el formulario (POST)
|   5. CursoController@update valida y actualiza en la BD
|   6. Redirige a la pagina principal con mensaje de exito
|
| PRECARGA DE DATOS:
| La variable $curso viene del controlador:
|   $curso = Curso::find($id);
|   return view('editar', compact('curso'));
| En los inputs usamos value="{{ $curso->nombre }}" para mostrar
| el valor actual del campo.
|
| NOTA SOBRE EL METODO HTTP:
| Este formulario usa method=POST directamente. En una implementacion
| REST estricta, se usaria:
|   <form method="POST">
|       @csrf
|       @method('PUT')   <- Simula el verbo PUT
|   </form>
| Y la ruta seria: Route::put('/actualizar/{id}', ...)
|
--}}

{{-- Hereda la estructura HTML de plantilla.blade.php --}}
@extends('plantilla')

@section('contenido')
<!-- Contenido principal -->
<section class="content">
    <h1>Editar Curso</h1>
 {{--    <p>Por favor, llena el siguiente formulario para agregar un nuevo curso:</p> --}}

    {{-- FORMULARIO DE EDICION:
         - action: route('update', $curso->id) genera /actualizar/5
         - method=POST: envia los datos modificados
         - @csrf: token de seguridad obligatorio
         - Cada input tiene value="{{ $curso->campo }}" con el dato actual
    --}}
    <!-- Formulario para agregar un curso -->
    <form action="{{route('update', $curso->id)}}" method=POST>
        @csrf

        {{-- CAMPOS CON VALORES PRECARGADOS:
             value="{{ $curso->nombre }}" muestra el valor actual del curso.
             {{ }} usa escape HTML automatico para prevenir XSS.

             MEJORA SUGERIDA: usar old('nombre', $curso->nombre)
             Esto muestra el valor del intento anterior si hubo error de validacion,
             o el valor original del curso si es la primera vez que se carga.
             Ejemplo: value="{{ old('nombre', $curso->nombre) }}"
        --}}
        <!-- 1 column -->
        <div data-mdb-input-init class="form-outline mb-4">
            <input type="text" id="nombre" class="form-control" name="nombre" value="{{$curso->nombre}}" />
            <label class="form-label" for="nombre">Nombre:</label>
        </div>

        <div data-mdb-input-init class="form-outline mb-4">
            <input type="text" id="objetivo" class="form-control" name="objetivo" value="{{$curso->objetivo}}" />
            <label class="form-label" for="objetivo">Objetivo:</label>
        </div>

        <!-- 2 column grid layout with text inputs for the first and last names -->
        <div class="row mb-4">
            <div class="col">
            <div data-mdb-input-init class="form-outline">
                <input type="text" id="modalidad" class="form-control" name="modalidad" value="{{$curso->modalidad}}" />
                <label class="form-label" for="modalidad">Modalidad:</label>
            </div>
            </div>
            <div class="col">
            <div data-mdb-input-init class="form-outline">
                <input type="text" id="cupo" class="form-control" name="cupo" value="{{$curso->cupo}}" />
                <label class="form-label" for="cupo">Cupo:</label>
            </div>
            </div>
        </div>

        <div class="row mb-4">
            <div class="col">
            <div data-mdb-input-init class="form-outline">
                <input type="text" id="periodo" class="form-control" name="periodo" value="{{$curso->periodo}}" />
                <label class="form-label" for="periodo">Periodo:</label>
            </div>
            </div>
            <div class="col">
            <div data-mdb-input-init class="form-outline">
                <input type="text" id="horario" class="form-control" name="horario" value="{{$curso->horario}}"/>
                <label class="form-label" for="horario">Horario:</label>
            </div>
            </div>
        </div>

        <div class="row mb-4">
            <div class="col">
            <div data-mdb-input-init class="form-outline">
                <input type="text" id="dias" class="form-control" name="dias" value="{{$curso->dias}}" />
                <label class="form-label" for="dias">Dia:</label>
            </div>
            </div>
            <div class="col">
            <div data-mdb-input-init class="form-outline">
                <input type="text" id="salon" class="form-control" name="salon" value="{{$curso->salon}}" />
                <label class="form-label" for="salon">Salon:</label>
            </div>
            </div>
        </div>

        <!-- Submit button -->
        {{-- Al enviar, los datos van a CursoController@update con el $id del curso --}}
        <button data-mdb-ripple-init type="submit" class="btn btn-primary btn-block mb-4">Actualizar curso</button>
    </form>

</section>
@endsection

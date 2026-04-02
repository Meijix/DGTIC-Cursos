@extends('plantilla')

@section('contenido')
<!-- Contenido principal -->
<section class="content">
    <h1>Editar Curso</h1>
 {{--    <p>Por favor, llena el siguiente formulario para agregar un nuevo curso:</p> --}}
    <!-- Formulario para agregar un curso -->
    <form action="{{route('update', $curso->id)}}" method=POST>
        @csrf
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

        <button data-mdb-ripple-init type="submit" class="btn btn-primary btn-block mb-4">Actualizar curso</button>
    </form>

</section>
@endsection
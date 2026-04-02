@extends('plantilla')

@section('contenido')
<!-- Contenido principal -->
<section class="content">
    <h1>Agregar Nuevo Curso</h1>
 {{--    <p>Por favor, llena el siguiente formulario para agregar un nuevo curso:</p> --}}
    <!-- Formulario para agregar un curso -->
    <form action="{{route('store')}}" method=POST>
        @csrf
        <!-- 1 column -->
        <div data-mdb-input-init class="form-outline mb-4">
            <input type="text" id="nombre" name="nombre" class="form-control" />
            <label class="form-label" for="nombre">Nombre:</label>
        </div>

        <div data-mdb-input-init class="form-outline mb-4">
            <input type="text" id="objetivo" name="objetivo" class="form-control" />
            <label class="form-label" for="objetivo">Objetivo:</label>
        </div>

        <!-- 2 column grid layout with text inputs for the first and last names -->
        <div class="row mb-4">
            <div class="col">
            <div data-mdb-input-init class="form-outline">
                <input type="text" id="modalidad" name="modalidad" class="form-control" />
                <label class="form-label" for="modalidad">Modalidad:</label>
            </div>
            </div>
            <div class="col">
            <div data-mdb-input-init class="form-outline">
                <input type="text" id="cupo" name="cupo" class="form-control" />
                <label class="form-label" for="cupo">Cupo:</label>
            </div>
            </div>
        </div>

        <div class="row mb-4">
            <div class="col">
            <div data-mdb-input-init class="form-outline">
                <input type="text" id="periodo" name="periodo" class="form-control" />
                <label class="form-label" for="periodo">Periodo:</label>
            </div>
            </div>
            <div class="col">
            <div data-mdb-input-init class="form-outline">
                <input type="text" id="horario" name="horario" class="form-control" />
                <label class="form-label" for="horario">Horario:</label>
            </div>
            </div>
        </div>

        <div class="row mb-4">
            <div class="col">
            <div data-mdb-input-init class="form-outline">
                <input type="text" id="dias" name="dias" class="form-control" />
                <label class="form-label" for="dias">Dia:</label>
            </div>
            </div>
            <div class="col">
            <div data-mdb-input-init class="form-outline">
                <input type="text" id="salon" name="salon" class="form-control" />
                <label class="form-label" for="salon">Salon:</label>
            </div>
            </div>
        </div>

        <!-- Submit button -->

        <button data-mdb-ripple-init type="submit" class="btn btn-primary btn-block mb-4">Agregar curso</button>
    </form>

</section>
@endsection
{{--
|==========================================================================
| agregar.blade.php - Formulario para Crear un Nuevo Curso
|==========================================================================
|
| FORMULARIOS EN LARAVEL:
| Este archivo contiene el formulario HTML para agregar un nuevo curso.
|
| FLUJO COMPLETO DEL FORMULARIO:
|   1. Usuario visita /agregar (GET) -> CursoController@create -> esta vista
|   2. Usuario llena el formulario y hace clic en "Agregar curso"
|   3. El formulario envia datos via POST a la ruta 'store'
|   4. CursoController@store valida y guarda en la BD
|   5. Si hay errores, Laravel redirige aqui con los errores
|   6. Si todo sale bien, redirige a la pagina principal con mensaje
|
| PROTECCION CSRF (Cross-Site Request Forgery):
| @csrf genera un campo oculto con un token unico:
|   <input type="hidden" name="_token" value="abc123xyz...">
| Laravel verifica este token en cada peticion POST/PUT/DELETE.
| Sin @csrf, Laravel rechaza el formulario con error 419.
|
| QUE ES CSRF:
| Un ataque donde un sitio malicioso envia peticiones a tu app
| haciendose pasar por el usuario. El token CSRF lo previene
| porque el atacante no conoce el token unico de la sesion.
|
| HELPER old():
| Cuando la validacion falla, old('nombre') devuelve el valor que
| el usuario escribio antes del error, para no perder sus datos.
| Ejemplo: <input value="{{ old('nombre') }}" />
| NOTA: En este formulario no se usa old(), pero seria una mejora.
|
--}}

{{-- Hereda la estructura HTML de plantilla.blade.php --}}
@extends('plantilla')

{{-- Inserta este contenido en el @yield('contenido') de la plantilla --}}
@section('contenido')
<!-- Contenido principal -->
<section class="content">
    <h1>Agregar Nuevo Curso</h1>
 {{--    <p>Por favor, llena el siguiente formulario para agregar un nuevo curso:</p> --}}

    {{-- FORMULARIO DE CREACION:
         - action: URL a donde se envian los datos -> route('store') genera /agregar
         - method=POST: verbo HTTP para crear recursos
         - @csrf: OBLIGATORIO en todo formulario POST de Laravel
    --}}
    <!-- Formulario para agregar un curso -->
    <form action="{{route('store')}}" method=POST>
        @csrf

        {{-- CAMPOS DEL FORMULARIO:
             Cada input tiene:
             - type="text": tipo de campo
             - id="nombre": para el atributo for del label (accesibilidad)
             - name="nombre": CLAVE para que Laravel lo reciba en $request->nombre
             - class="form-control": estilos de Bootstrap

             El atributo 'name' es el mas importante: determina como se accede
             al valor en el controlador con $request->nombre
        --}}
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
        {{-- Grid de Bootstrap: row + col divide en columnas responsivas --}}
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
        {{-- Al hacer clic, el formulario envia todos los campos via POST --}}
        {{-- Laravel recibe los datos en CursoController@store como $request --}}
        <button data-mdb-ripple-init type="submit" class="btn btn-primary btn-block mb-4">Agregar curso</button>
    </form>

</section>
@endsection

{{--
|==========================================================================
| principal.blade.php - Vista Principal con Listado de Cursos
|==========================================================================
|
| BLADE TEMPLATING ENGINE:
| Blade es el motor de plantillas de Laravel. Permite escribir PHP
| de forma mas limpia y segura dentro de archivos HTML.
|
| HERENCIA DE PLANTILLAS:
| Blade usa un sistema de herencia similar a la POO:
|   - plantilla.blade.php define la estructura base con @yield('nombre')
|   - Las vistas hijas usan @extends('plantilla') y @section('nombre')
|
|   plantilla.blade.php          principal.blade.php
|   +-------------------+        +-------------------+
|   | <html>            |        | @extends          |
|   |   <header>        |        |                   |
|   |   @yield('conten') | <----  | @section('conten')|
|   |   <footer>        |        |   <tabla>         |
|   | </html>           |        | @endsection       |
|   +-------------------+        +-------------------+
|
| SINTAXIS BLADE IMPORTANTE:
| {{ $variable }}     -> Imprime con escape HTML (seguro contra XSS)
| {!! $variable !!}   -> Imprime sin escape (solo si confias en el dato)
| {{-- comentario --}} -> Comentario Blade (no aparece en HTML generado)
| @if / @else / @endif -> Condicionales
| @foreach / @endforeach -> Bucles
| @csrf               -> Token de proteccion contra CSRF
|
--}}

{{-- @extends: indica que esta vista hereda de 'plantilla.blade.php' --}}
{{-- Toda la estructura HTML (head, header, footer) viene de la plantilla --}}
@extends('plantilla')

{{-- @section('contenido'): define el contenido que se insertara --}}
{{-- en el lugar donde plantilla.blade.php tiene @yield('contenido') --}}
@section('contenido')
<!-- Contenido principal -->
<section class="content">
    <h1>Cursos</h1>
    <p>Esta es la página principal de la aplicación de cursos de la DGTIC.</p>

{{-- MENSAJES FLASH DE SESION:
     session('mensaje') recupera un dato "flash" almacenado con ->with()
     en el controlador. Los datos flash solo existen para UNA peticion.
     Flujo: Controller ->with('mensaje', 'texto') -> Vista session('mensaje')
--}}
{{-- no me sale la alerta de agregado y no se guarda en la base de datos --}}
    @if (session('mensaje'))
        {{-- Bootstrap alert: muestra el mensaje de exito/error --}}
        <div class="alert alert-success" role="alert">
            {{ (session('mensaje')) }}
        </div>
    @endif

    {{-- TABLA HTML CON DATOS DE ELOQUENT:
         La variable $cursos viene del controlador:
         $cursos = Curso::orderBy('id')->paginate(4);
         Es un objeto LengthAwarePaginator que se puede iterar como array --}}
    <table class="table">
        <thead>
            <tr>
                <th scope="col">#</th>
                <th scope="col">Nombre</th>
                <th scope="col">Objetivo</th>
                <th scope="col">Modalidad</th>
                <th scope="col">Cupo</th>
                <th scope="col">Periodo</th>
                <th scope="col">Horario</th>
                <th scope="col">Días</th>
                <th scope="col">Salon</th>
                <th scope="col">Opciones</th>
            </tr>
        </thead>
        <tbody>
            {{-- @foreach: itera sobre la coleccion de cursos --}}
            {{-- Cada $curso es una instancia del modelo Curso (un objeto Eloquent) --}}
            {{-- Se accede a las columnas como propiedades: $curso->nombre, $curso->id --}}
            @foreach ($cursos as $curso)
            <tr>
                {{-- {{ $curso->id }} usa doble llave para imprimir con escape HTML --}}
                {{-- El escape previene ataques XSS (Cross-Site Scripting) --}}
                <th scope="row">{{$curso->id}}</th>
                <td>{{$curso->nombre}}</td>
                <td>{{$curso->objetivo}}</td>
                <td>{{$curso->modalidad}}</td>
                <td>{{$curso->cupo}}</td>
                <td>{{$curso->periodo}}</td>
                <td>{{$curso->horario}}</td>
                <td>{{$curso->dias}}</td>
                <td>{{$curso->salon}}</td>
                <td>
                    {{-- BOTON EDITAR: enlace GET a la ruta 'edit' con el ID del curso --}}
                    {{-- route('edit', $curso->id) genera: /editar/5 (por ejemplo) --}}
                    <a class="btn btn-raised btn-primary btn-sm" href="{{route('edit', $curso->id)}}">Editar</a>
                    <br>

                    {{-- FORMULARIO ELIMINAR:
                         - Usa un formulario POST con @csrf y @method('DELETE')
                         - @csrf: genera un campo oculto con el token CSRF para proteccion
                         - method_field('delete'): genera <input type="hidden" name="_method" value="DELETE">
                           porque HTML solo soporta GET y POST, pero Laravel necesita DELETE
                         - onclick="return confirm(...)": confirmacion del navegador antes de eliminar
                    --}}
                    <form action="{{route('destroy', $curso->id)}}" method=POST>
                        @csrf
                        {{method_field('delete')}}
                        <button type="submit" class="btn btn-raised btn-danger btn-sm" onclick="return confirm('Quieres eliminar este curso?')">Eliminar</button>
                    </form>
                </td>
            </tr>
            @endforeach
        </tbody>
    </table>

    {{-- PAGINACION:
         $cursos->links() genera automaticamente los enlaces de paginacion.
         'pagination::bootstrap-4' usa el estilo de Bootstrap 4.
         Esto es posible porque usamos ->paginate(4) en el controlador.
         Laravel maneja automaticamente el parametro ?page=2, ?page=3, etc.
    --}}
    {{$cursos->links('pagination::bootstrap-4')}}

</section>
@endsection

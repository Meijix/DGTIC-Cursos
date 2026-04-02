{{--
|==========================================================================
| plantilla.blade.php - Layout Principal (Plantilla Base)
|==========================================================================
|
| HERENCIA DE PLANTILLAS EN BLADE:
| Este archivo es la "plantilla madre" que define la estructura HTML
| comun a todas las paginas: <head>, <header>, <footer>.
|
| Las vistas hijas (principal, agregar, editar, contacto, aviso) heredan
| de esta plantilla usando @extends('plantilla') y definen su contenido
| especifico con @section('contenido').
|
| DIAGRAMA DE HERENCIA:
|
|   plantilla.blade.php (Layout Base)
|   +------------------------------------------+
|   | <!DOCTYPE html>                          |
|   | <head>CSS, Bootstrap, titulo</head>      |
|   | <body>                                   |
|   |   <header>Logo + Menu de navegacion</header>|
|   |                                          |
|   |   @yield('contenido')  <-- Aqui se inserta el contenido de cada vista hija|
|   |                                          |
|   |   <footer>Pie de pagina</footer>         |
|   | </body>                                  |
|   +------------------------------------------+
|        ^           ^          ^          ^
|        |           |          |          |
|   principal   agregar    editar     contacto
|   .blade.php  .blade.php .blade.php .blade.php
|
| DIRECTIVAS CLAVE:
| @yield('nombre')   -> en la plantilla: "aqui va el contenido"
| @extends('plantilla') -> en la vista hija: "heredo de esta plantilla"
| @section('nombre') ... @endsection -> en la vista hija: "este es mi contenido"
|
| HELPERS DE LARAVEL EN BLADE:
| asset('css/style.css') -> genera la URL completa al archivo en /public
|   Ejemplo: http://localhost:8000/css/style.css
| route('index') -> genera la URL de una ruta por su nombre
|   Ejemplo: http://localhost:8000/
|
--}}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">

    {{-- asset() genera la URL al archivo en la carpeta /public --}}
    {{-- Los archivos estaticos (CSS, JS, imagenes) van en /public --}}
    <!-- Estilos css y bootstrap -->
    <link rel="stylesheet" href="{{ asset('css/style.css') }}">

    {{-- Bootstrap 5 via CDN: framework CSS para estilos responsivos --}}
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <title>Cursos DGTIC</title>
</head>
<body>
    <!-- Encabezado y menu de navegacion -->
    <header id="header_nav">
        <div class="container d-flex justify-content-between align-content-center" style="align-content: center;  height: 100%">
        <!-- Logo -->
        <a href="#" target="_blank" class="logo">
            {{-- asset('img/logo-dgtic.png') busca en /public/img/logo-dgtic.png --}}
            <img src="{{ asset('img/logo-dgtic.png') }}" alt="Logo UNAM">

            {{-- MENU DE NAVEGACION:
                 Cada enlace usa route('nombre') para generar la URL.
                 Esto es mejor que escribir URLs directas porque si
                 cambia la URL en web.php, los enlaces siguen funcionando.
            --}}
            <!-- Menú -->
            <div class="navbar">
                <ul class="mr-auto">
                    {{-- route('index') -> / (pagina principal) --}}
                    <li class="nav-item"><a  href="{{ route('index')}}">Principal</a></li>
                    {{-- route('create') -> /agregar (formulario nuevo curso) --}}
                    <li class="nav-item"><a  href="{{ route('create')}}">Agregar</a></li>
                    {{-- route('contacto') -> /contacto (formulario de contacto) --}}
                    <li class="nav-item"><a  href="{{ route('contacto')}}">Contáctanos</a></li>
                </ul>
            </div>

        </div>
    </header>

    {{-- @yield('contenido'):
         Punto de insercion donde las vistas hijas colocan su contenido.
         Cuando principal.blade.php hace @section('contenido'),
         todo ese bloque se inserta aqui.
    --}}
    <!-- Contenido -->
    @yield('contenido')


    <!-- Pie de pagina -->
    <footer>
        <div class="text-center p-3" >
            Hecho en México. Universidad Nacional Autónoma de México (UNAM). Todos los derechos reservados 2021. Esta página puede ser reproducida con fines no lucrativos, siempre y cuando se cite la fuente completa y su dirección electrónica, y no se mutile; de otra forma requiere permiso previo por escrito de la institución.
        </div>
    </footer>
</body>
</html>

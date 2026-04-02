<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <!-- Estilos css y bootstrap -->
    <link rel="stylesheet" href="{{ asset('css/style.css') }}">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <title>Cursos DGTIC</title>
</head>
<body>
    <!-- Encabezado y menú -->
    <header id="header_nav">
        <div class="container d-flex justify-content-between align-content-center" style="align-content: center;  height: 100%">
        <!-- Logo -->
        <a href="#" target="_blank" class="logo">
            <img src="{{ asset('img/logo-dgtic.png') }}" alt="Logo UNAM">
            <!-- Menú -->       
            <div class="navbar">
                <ul class="mr-auto">
                    <li class="nav-item"><a  href="{{ route('index')}}">Principal</a></li>
                    <li class="nav-item"><a  href="{{ route('create')}}">Agregar</a></li>
                    <li class="nav-item"><a  href="{{ route('contacto')}}">Contáctanos</a></li>
                </ul>
            </div>

        </div>          
    </header>

    <!-- Contenido -->
    @yield('contenido')


    <!-- Pie de página -->
    <footer>
        <div class="text-center p-3" >
            Hecho en México. Universidad Nacional Autónoma de México (UNAM). Todos los derechos reservados 2021. Esta página puede ser reproducida con fines no lucrativos, siempre y cuando se cite la fuente completa y su dirección electrónica, y no se mutile; de otra forma requiere permiso previo por escrito de la institución.  
        </div>
    </footer>
</body>
</html>
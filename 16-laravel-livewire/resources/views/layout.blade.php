{{--
|==========================================================================
| layout.blade.php - Plantilla Base para la Aplicacion Livewire
|==========================================================================
|
| Esta plantilla cumple el mismo rol que plantilla.blade.php del Modulo 15:
| define la estructura HTML comun (head, header, footer) y las vistas
| hijas insertan su contenido con @section('content').
|
| DIFERENCIAS CON LA PLANTILLA DEL MODULO 15:
| En Livewire es OBLIGATORIO incluir dos directivas adicionales:
|
|   1. @livewireStyles  -> en el <head>
|      Inyecta los estilos CSS que Livewire necesita para funcionar.
|
|   2. @livewireScripts -> antes de </body>
|      Inyecta el JavaScript de Livewire que maneja:
|      - La comunicacion AJAX con el servidor
|      - El DOM diffing (actualizar solo lo que cambio)
|      - La vinculacion de datos (wire:model)
|      - Los eventos (wire:click, wire:submit)
|
| SIN ESTAS DIRECTIVAS, LIVEWIRE NO FUNCIONA.
|
| COMPARACION DE LAYOUTS:
|
|   Modulo 15 (plantilla.blade.php):
|   <head>
|       <link css>
|   </head>
|   <body>
|       @yield('contenido')
|   </body>
|
|   Modulo 16 (layout.blade.php):
|   <head>
|       <link css>
|       @livewireStyles          <-- NUEVO: estilos de Livewire
|   </head>
|   <body>
|       @yield('content')
|       @livewireScripts         <-- NUEVO: JavaScript de Livewire
|   </body>
|
--}}
<!DOCTYPE html>
<html lang="{{ str_replace('_', '-', app()->getLocale()) }}">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">

        <!-- Estilos css y bootstrap -->
        {{-- asset() genera la URL completa al archivo en /public --}}
        <link rel="stylesheet" href="{{ asset('css/style.css') }}">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">

        <title>Cursos DGTIC Livewire</title>

        {{-- @livewireStyles: OBLIGATORIO para Livewire
             Inyecta las etiquetas <style> necesarias para que Livewire
             maneje correctamente la interfaz (estados de carga, etc.)
             En Livewire 3, se puede usar @livewireStyles o no (incluido automaticamente),
             pero es buena practica tenerlo explicitamente.
        --}}
        @livewireStyles
    </head>
    <body class="antialiased">
        <!-- Encabezado y menu de navegacion -->
    <header id="header_nav">
        <div class="container d-flex justify-content-between align-content-center" style="align-content: center;  height: 100%">
        <!-- Logo -->
        <a href="#" target="_blank" class="logo">
            <img src="{{ asset('img/logo-dgtic.png') }}" alt="Logo UNAM">
            <!-- Menu -->
            <div class="navbar">
                <ul class="mr-auto">
                    {{-- Los enlaces del menu estan vacios (href="")
                         En una app completa, apuntarian a rutas con nombre.
                         Con Livewire, la navegacion puede manejarse dentro
                         del componente cambiando $this->view sin nuevas rutas.
                    --}}
                    <li class="nav-item"><a  href="">Principal</a></li>
                    <li class="nav-item"><a  href="">Agregar</a></li>
                    <li class="nav-item"><a  href="">Contáctanos</a></li>
                </ul>
            </div>

        </div>
    </header>

    <!-- Contenido -->
    {{-- @yield('content'): punto de insercion para las vistas hijas.
         principal.blade.php usa @section('content') para insertar
         el componente Livewire aqui.
    --}}
    @yield('content')

    <!-- Pie de pagina -->
    <footer>
        <div class="text-center p-3" >
            Hecho en México. Universidad Nacional Autónoma de México (UNAM). Todos los derechos reservados 2021. Esta página puede ser reproducida con fines no lucrativos, siempre y cuando se cite la fuente completa y su dirección electrónica, y no se mutile; de otra forma requiere permiso previo por escrito de la institución.
        </div>
    </footer>

    {{-- @livewireScripts: OBLIGATORIO para Livewire
         Inyecta el JavaScript que hace funcionar todo Livewire:
         - Intercepta eventos del DOM (wire:click, wire:model, etc.)
         - Envia peticiones AJAX al servidor cuando hay cambios
         - Recibe el HTML actualizado del servidor
         - Aplica "DOM diffing" para actualizar solo lo necesario
         - Maneja la cola de peticiones y los estados de carga

         Va ANTES de </body> para que todo el HTML ya este cargado.
    --}}
    @livewireScripts
    </body>
</html>

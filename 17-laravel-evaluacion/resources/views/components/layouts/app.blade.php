{{--
==========================================================================
MODULO 17 - PROYECTO DE EVALUACION: Layout Principal de la Aplicacion
==========================================================================

PROPOSITO DE ESTE ARCHIVO:
Este es el LAYOUT (plantilla base) que envuelve TODAS las paginas de la aplicacion.
Contiene el HTML comun: <head>, estilos CSS, scripts de Livewire, etc.

UBICACION ESPECIAL:
resources/views/components/layouts/app.blade.php
Livewire busca este archivo AUTOMATICAMENTE como layout por defecto.
No necesitas especificarlo en cada componente.

QUE ES UN LAYOUT?
Un layout define la estructura HTML que se REPITE en todas las paginas:
- DOCTYPE, <html>, <head>, <body>
- Hojas de estilo CSS (Bootstrap, Tailwind, etc.)
- Scripts de JavaScript
- Barra de navegacion
- Footer
- etc.

EL CONCEPTO DE {{ $slot }}:
$slot es donde Livewire INYECTA el contenido del componente actual.
Si el usuario visita /customers, Livewire:
1. Renderiza Customers.php -> customers.blade.php
2. Toma ese HTML y lo pone en {{ $slot }}
3. El resultado es la pagina completa con layout + contenido

Es como un "hueco" que se llena con contenido diferente segun la pagina.
Similar a @yield('content') / @section('content') del Blade tradicional.

COMPARACION DE SISTEMAS DE LAYOUT EN LARAVEL:

  1. BLADE CLASICO (@extends / @yield):
     @extends('layouts.app')
     @section('content') ... @endsection

  2. COMPONENTES BLADE (<x-layout>):
     <x-app-layout> ... </x-app-layout>

  3. LIVEWIRE AUTOMATICO (este archivo):
     Livewire usa components/layouts/app.blade.php automaticamente.
     Cada componente renderiza su vista y Livewire la inyecta en $slot.
--}}

<!DOCTYPE html>
<html lang="{{ str_replace('_', '-', app()->getLocale()) }}">
    {{--
    app()->getLocale() devuelve el idioma configurado (ej: "es").
    str_replace('_', '-', ...) convierte "es_MX" a "es-MX" para el estandar HTML.
    El atributo lang="" es importante para:
    - Accesibilidad (lectores de pantalla)
    - SEO (motores de busqueda)
    - Correcta renderizacion de caracteres especiales
    --}}
    <head>
        <meta charset="utf-8">
        {{--
        viewport: ESENCIAL para que la pagina sea responsive (se adapte a moviles).
        Sin esto, la pagina se veria diminuta en telefonos.
        --}}
        <meta name="viewport" content="width=device-width, initial-scale=1.0">

        {{--
        @livewireStyles: Inyecta los estilos CSS que Livewire necesita.
        DEBE ir dentro de <head> para que los estilos se carguen antes del contenido.
        Sin esto, los componentes Livewire no se veran correctamente.
        --}}
        @livewireStyles

        {{--
        BOOTSTRAP 5 via CDN:
        CDN = Content Delivery Network (red de servidores para archivos estaticos).

        Ventajas de usar CDN:
        - No necesitas descargar Bootstrap (se carga desde internet)
        - Los navegadores pueden tener Bootstrap en cache de otros sitios
        - Se actualiza cambiando solo la URL

        Desventajas:
        - Requiere conexion a internet
        - Dependes de un servicio externo
        - No puedes personalizar facilmente

        ALTERNATIVA: Instalar con npm (npm install bootstrap)
        y compilar con Vite/Mix (mas control, funciona offline).

        integrity="sha384-..." verifica que el archivo no fue modificado (seguridad).
        crossorigin="anonymous" permite cargar desde otro dominio.
        --}}
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">

        {{--
        TITULO DINAMICO:
        {{ $title ?? 'Final-Natalia' }} usa el operador null coalescing (??):
        - Si $title esta definido, lo muestra
        - Si no, muestra 'Final-Natalia' como valor por defecto

        Los componentes pueden pasar un titulo personalizado:
        <x-slot name="title">Mi Pagina</x-slot>
        --}}
        <title>{{ $title ?? 'Final-Natalia' }}</title>
    </head>
    <body>
        {{--
        @livewireScripts: Inyecta el JavaScript que Livewire necesita.
        Este script es el "motor" de Livewire:
        - Intercepta eventos del DOM (clicks, submits, etc.)
        - Hace peticiones AJAX al servidor
        - Actualiza el DOM con los cambios (sin recargar la pagina)

        DEBE ir antes del cierre de </body> o dentro de <body>.
        --}}
        @livewireScripts

        {{--
        .container de Bootstrap: Centra el contenido con margenes laterales.

        {{ $slot }}: AQUI SE INYECTA EL CONTENIDO DEL COMPONENTE LIVEWIRE.
        Cada vez que visitas una ruta diferente, $slot contiene el HTML
        del componente correspondiente a esa ruta.
        --}}
        <div class="container">
            {{ $slot }}
        </div>
    </body>
</html>

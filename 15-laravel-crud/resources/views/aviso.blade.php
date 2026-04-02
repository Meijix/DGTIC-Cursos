{{--
|==========================================================================
| aviso.blade.php - Vista de Avisos con Logica Condicional Blade
|==========================================================================
|
| Esta vista demuestra el uso de directivas condicionales de Blade
| (@if / @else / @endif) y como mezclar PHP puro dentro de vistas.
|
| DIRECTIVAS CONDICIONALES EN BLADE:
| @if(condicion)       -> si se cumple
| @elseif(condicion)   -> alternativa
| @else                -> si nada se cumple
| @endif               -> cierra el bloque
|
| OTRAS DIRECTIVAS CONDICIONALES:
| @unless(condicion)   -> "a menos que" (lo opuesto a @if)
| @isset($variable)    -> si la variable existe y no es null
| @empty($variable)    -> si la variable esta vacia
| @auth                -> si el usuario esta autenticado
| @guest               -> si el usuario es invitado (no autenticado)
|
| PHP EN BLADE:
| Se puede usar <?php ?> dentro de Blade, pero se recomienda
| mover la logica al controlador y solo usar Blade para presentacion.
| La directiva @php ... @endphp es la forma Blade de escribir PHP.
|
--}}

{{-- Hereda la estructura de plantilla.blade.php --}}
@extends('plantilla')

@section('contenido')
<!-- Contenido principal -->
<section class="content">

    <h1>Aviso de curso de inducción</h1>

    <p>Se les convoca a asistir al curso de inducción, que se realizará durante la semana del  27 al 31 de enero de 2025 en el Auditorio Carlos Pérez del Toro a partir de las 9:00 am.</p>

    {{-- BLOQUE PHP PURO:
         Se puede usar <?php ?> en Blade, pero es mejor practica
         pasar las variables desde el controlador.
         Alternativa Blade: @php $estudiante_informatica = 4; @endphp
    --}}
    <?php
        $estudiante_informatica = 4;
    ?>

    {{-- CONDICIONAL @if:
         Evalua si $estudiante_informatica == 1
         Como vale 4, se ejecuta el bloque @else.

         Este ejemplo muestra como personalizar contenido segun
         una condicion. En la practica, la variable vendria del
         controlador o de la base de datos, no definida en la vista.
    --}}
    @if($estudiante_informatica == 1)
        <h2>Aviso conferencia</h2>
        <p>Se convoca a todos los estudiantes de informática de nuevo ingreso a participar en la conferencia</p>

        <p>-La informática como apoyo estratégico en las organizaciones- misma que se impartirá el 6 de febrero de 2025 en el Aula Magna de la Facultad a las 14:00 hrs</p>
    @else
        <h2>Aviso conferencia</h2>
        <p>Si les interesan otras conferencias ver el anuncio oficial. </p>

    @endif

</section>
@endsection



@extends('plantilla')

@section('contenido')
<!-- Contenido principal -->
<section class="content">

    <h1>Aviso de curso de inducción</h1>

    <p>Se les convoca a asistir al curso de inducción, que se realizará durante la semana del  27 al 31 de enero de 2025 en el Auditorio Carlos Pérez del Toro a partir de las 9:00 am.</p>

    <?php
        $estudiante_informatica = 4;
    ?>

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



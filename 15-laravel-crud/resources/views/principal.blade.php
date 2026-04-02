@extends('plantilla')

@section('contenido')
<!-- Contenido principal -->
<section class="content">
    <h1>Cursos</h1>
    <p>Esta es la página principal de la aplicación de cursos de la DGTIC.</p>

{{-- no me sale la alerta de agregado y no se guarda en la base de datos --}}
    @if (session('mensaje'))
        <div class="alert alert-success" role="alert">
            {{ (session('mensaje')) }}
        </div>
    @endif
    
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
            @foreach ($cursos as $curso)
            <tr>
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
                    <a class="btn btn-raised btn-primary btn-sm" href="{{route('edit', $curso->id)}}">Editar</a>  
                    <br>
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
    {{$cursos->links('pagination::bootstrap-4')}}

</section>
@endsection
{{--
|==========================================================================
| principal.blade.php - Pagina de Entrada que Carga el Componente Livewire
|==========================================================================
|
| Esta vista es el "puente" entre el sistema de rutas tradicional de Laravel
| y el mundo de los componentes Livewire.
|
| FLUJO:
|   1. Usuario visita / (ruta raiz)
|   2. web.php retorna esta vista: return view('principal')
|   3. Esta vista hereda del layout y usa @livewire() para cargar el componente
|   4. Livewire renderiza CursoComponent con su vista asociada
|   5. A partir de aqui, todo es reactivo (sin recargas de pagina)
|
| @livewire('curso-component'):
| Esta directiva le dice a Laravel que inserte el componente Livewire
| llamado 'curso-component' en este punto del HTML.
|
| COMO ENCUENTRA LARAVEL EL COMPONENTE:
| 'curso-component' (kebab-case) -> CursoComponent (PascalCase)
| Laravel busca: app/Livewire/CursoComponent.php
|
| ALTERNATIVAS PARA INCLUIR UN COMPONENTE:
| @livewire('curso-component')         -- directiva Blade
| <livewire:curso-component />         -- tag HTML (Livewire 3)
| @livewire('curso-component', ['param' => 'valor'])  -- con parametros
|
| DIFERENCIA CON EL MODULO 15:
|   Modulo 15: Cada accion tiene su propia vista y URL
|     GET /           -> principal.blade.php (lista)
|     GET /agregar    -> agregar.blade.php (formulario)
|     GET /editar/5   -> editar.blade.php (formulario)
|
|   Modulo 16: UNA sola pagina, el componente maneja todo
|     GET /           -> principal.blade.php -> @livewire('curso-component')
|     (todo el CRUD sucede dentro del componente sin cambiar de URL)
|
--}}

{{-- Hereda la estructura HTML del layout (con @livewireStyles y @livewireScripts) --}}
@extends('layout')

@section('content')
<div class="content">
    {{-- Aqui se inserta el componente Livewire CursoComponent
         Livewire automaticamente:
         1. Instancia la clase CursoComponent
         2. Ejecuta mount() (si existe)
         3. Ejecuta render() para obtener la vista
         4. Inserta el HTML generado aqui
         5. Activa el JavaScript para manejar interactividad
    --}}
    @livewire('curso-component')
</div>
@endsection

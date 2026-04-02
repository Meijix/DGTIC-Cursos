{{--
|==========================================================================
| curso-component.blade.php - Vista Principal del Componente Livewire
|==========================================================================
|
| Esta es la vista asociada al componente CursoComponent.php.
| En Livewire, cada componente tiene exactamente UNA vista Blade.
|
| REGLA FUNDAMENTAL DE LIVEWIRE:
| La vista de un componente debe tener UN SOLO elemento raiz.
| En este caso es <div>. Todo el contenido debe estar dentro.
|
|   CORRECTO:                   INCORRECTO:
|   <div>                       <h1>Titulo</h1>
|       <h1>Titulo</h1>        <p>Contenido</p>
|       <p>Contenido</p>       (dos elementos raiz)
|   </div>
|
| VISTAS DINAMICAS CON @include:
| Este componente usa la propiedad $view (del componente PHP)
| para decidir que sub-vista mostrar. @include("livewire.$view")
| inserta dinamicamente 'livewire/create.blade.php' o cualquier
| otra vista segun el valor de $view.
|
| ACCESO A PROPIEDADES:
| Todas las propiedades publicas del componente PHP estan disponibles
| automaticamente en esta vista:
|   - $view -> propiedad que controla que sub-vista mostrar
|   - $nombre, $objetivo, etc. -> propiedades del formulario
|
| COMPARACION CON MODULO 15:
|   Modulo 15: Cada pagina (principal, agregar, editar) es una vista
|              separada con su propia URL y ruta.
|   Modulo 16: Todo puede estar en UNA sola vista que cambia
|              dinamicamente segun el estado del componente.
|
--}}
<div>
    {{-- Comentario de Livewire: "Do your work, then step back"
         (Haz tu trabajo, luego da un paso atras) - Lao Tzu --}}
    {{-- Do your work, then step back. --}}
    <h1>Cursos Becarios DGTIC</h1>
    <div class="row">
        <div class="col-sm-10">
            {{-- @include DINAMICO:
                 "livewire.$view" se resuelve segun el valor de $view.
                 Si $view = 'create', incluye: livewire/create.blade.php
                 Si $view = 'edit', incluiria: livewire/edit.blade.php
                 Si $view = 'list', incluiria: livewire/list.blade.php

                 Esto permite cambiar entre vistas sin recargar la pagina.
                 Solo cambiamos $this->view = 'edit' en el componente PHP
                 y Livewire re-renderiza automaticamente con la nueva vista.
            --}}
            @include("livewire.$view")
        </div>
    </div>
</div>

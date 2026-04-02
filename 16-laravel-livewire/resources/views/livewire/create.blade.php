{{--
|==========================================================================
| create.blade.php - Sub-vista de Creacion (Livewire)
|==========================================================================
|
| Esta es una sub-vista que se incluye dentro de curso-component.blade.php
| mediante @include("livewire.$view") cuando $view = 'create'.
|
| DIFERENCIA CON EL FORMULARIO DEL MODULO 15:
|
|   Modulo 15 (Tradicional):
|   - El formulario usa <form action="{{ route('store') }}" method="POST">
|   - Necesita @csrf para proteccion CSRF
|   - El boton es <button type="submit">
|   - Los datos se envian como peticion HTTP completa
|   - La pagina se recarga completamente
|
|   Modulo 16 (Livewire):
|   - El boton usa wire:click="store" en vez de type="submit"
|   - NO necesita @csrf (Livewire lo maneja internamente)
|   - Los datos ya estan en el servidor (via wire:model)
|   - Solo se actualiza la parte necesaria de la pagina
|   - Sin recarga completa
|
| ESTRUCTURA DE TARJETA (CARD):
| Usa el componente Card de Bootstrap para organizar visualmente
| el formulario con un encabezado y un cuerpo.
|
--}}

<div class="card">
    <div class="card-header">
        <h5>Nuevo curso</h5>
    </div>
    <div class="card-body">
        {{-- Incluye el formulario compartido (form.blade.php)
             Este formulario puede reutilizarse tanto para crear como para editar.
             Los inputs usan wire:model para vincular con las propiedades PHP.
        --}}
        @include('livewire.form')

        {{-- BOTON CON wire:click:
             wire:click="store" le dice a Livewire:
             "Cuando el usuario haga clic, ejecuta el metodo store()
              del componente CursoComponent.php en el servidor"

             FLUJO:
             1. Clic en el boton
             2. Livewire.js envia una peticion AJAX al servidor
             3. El servidor ejecuta CursoComponent->store()
             4. store() valida datos y crea el curso
             5. El servidor re-renderiza la vista
             6. Livewire.js actualiza solo las partes que cambiaron

             type="button" (no "submit") porque Livewire maneja el evento,
             no el formulario HTML nativo.
        --}}
        <button wire:click="store" class="btn btn-primary" type="button" style="margin-top:10px">Agregar</button>
    </div>
</div>

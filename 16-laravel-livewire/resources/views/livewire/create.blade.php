
<div class="card">
    <div class="card-header">
        <h5>Nuevo curso</h5>
    </div>
    <div class="card-body">
        @include('livewire.form')

        <button wire:click="store" class="btn btn-primary" type="button" style="margin-top:10px">Agregar</button>
    </div>
</div>

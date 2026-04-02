<form action="">

    <div class="form-group">
        <label>Nombre</label>
        <input type="text" class="form-control" wire:model="nombre">
        @error('nombre') <span>{{ $message }}</span> @enderror
    </div>

    <div class="form-group">
        <label>Objetivo</label>
        <input type="text" class="form-control" wire:model="objetivo">
        @error('objetivo') <span>{{ $message }}</span> @enderror
    </div>

    <div class="form-group">
        <label>Modalidad</label>
        <input type="text" class="form-control" wire:model="modlidad">
        @error('modlidad') <span>{{ $message }}</span> @enderror
    </div>

    <div class="form-group">
        <label>Cupo</label>
        <input type="text" class="form-control" wire:model="cupo">
        @error('cupo') <span>{{ $message }}</span> @enderror
    </div>

    <div class="form-group">
        <label>Periodo</label>
        <input type="text" class="form-control" wire:model="periodo">
        @error('periodo') <span>{{ $message }}</span> @enderror
    </div>

    <div class="form-group">
        <label>Horario</label>
        <input type="text" class="form-control" wire:model="horario">
        @error('horario') <span>{{ $message }}</span> @enderror
    </div>

    <div class="form-group">
        <label>Dias</label>
        <input type="text" class="form-control" wire:model="dias">
        @error('dias') <span>{{ $message }}</span> @enderror
    </div>

    <div class="form-group">
        <label>Salon</label>
        <input type="text" class="form-control" wire:model="salon">
        @error('salon') <span>{{ $message }}</span> @enderror
    </div>

    <button type="submit" class="btn btn-primary"> Guardar </button>
</form>
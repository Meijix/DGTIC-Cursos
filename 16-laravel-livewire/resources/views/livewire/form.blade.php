{{--
|==========================================================================
| form.blade.php - Formulario Compartido (Parcial Livewire)
|==========================================================================
|
| Este formulario es una vista parcial ("partial") que se incluye desde
| create.blade.php (y potencialmente desde edit.blade.php).
| Contiene los inputs vinculados a las propiedades del componente Livewire.
|
| WIRE:MODEL - DATA BINDING (VINCULACION DE DATOS):
| wire:model="nombre" conecta BIDIRECCIONALMENTE el input con
| la propiedad $nombre del componente PHP.
|
|   +------------------+     wire:model     +------------------+
|   | INPUT HTML       | <================> | Propiedad PHP    |
|   | (Navegador)      |   bidireccional    | $this->nombre    |
|   +------------------+                    +------------------+
|
|   - El usuario escribe en el input -> se actualiza $this->nombre en PHP
|   - Si cambias $this->nombre en PHP -> se actualiza el input en el navegador
|
| VARIANTES DE wire:model:
| +------------------------+--------------------------------------------------+
| | Directiva              | Comportamiento                                   |
| +------------------------+--------------------------------------------------+
| | wire:model="nombre"    | Sincroniza cada vez que se pierde el foco         |
| |                        | (Livewire 3) o en cada tecla (Livewire 2)        |
| | wire:model.live="nombre"| Sincroniza en CADA tecla (tiempo real)          |
| | wire:model.blur="nombre"| Sincroniza al perder el foco (blur)             |
| | wire:model.lazy="nombre"| Sincroniza al perder el foco (Livewire 2)       |
| | wire:model.debounce.500ms| Espera 500ms despues de la ultima tecla        |
| +------------------------+--------------------------------------------------+
|
| MANEJO DE ERRORES (@error):
| Cuando $this->validate() falla en el componente PHP, Livewire
| automaticamente hace disponibles los errores en la vista.
| @error('campo') ... @enderror muestra el error si existe.
| {{ $message }} contiene el texto del error de validacion.
| Los errores aparecen INMEDIATAMENTE sin recargar la pagina.
|
| COMPARACION CON FORMULARIO TRADICIONAL (MODULO 15):
|
|   Modulo 15:                          Modulo 16:
|   <form method="POST"                <form>
|     action="{{ route('store') }}">     (sin action ni method)
|     @csrf                              (sin @csrf)
|     <input name="nombre"               <input wire:model="nombre">
|       value="{{ old('nombre') }}">     (sin old(), Livewire recuerda)
|   </form>                             </form>
|
| NOTA: Hay un typo en wire:model="modlidad" (falta una 'a').
| Deberia ser wire:model="modalidad" para coincidir con la propiedad PHP.
|
--}}
<form action="">

    {{-- CAMPO NOMBRE:
         wire:model="nombre" vincula este input con $this->nombre
         del componente CursoComponent.php.
         El atributo name="" no es necesario con Livewire (pero no estorba).
    --}}
    <div class="form-group">
        <label>Nombre</label>
        <input type="text" class="form-control" wire:model="nombre">
        {{-- @error muestra el mensaje de validacion si 'nombre' tiene error --}}
        {{-- El error aparece instantaneamente sin recargar la pagina --}}
        @error('nombre') <span>{{ $message }}</span> @enderror
    </div>

    <div class="form-group">
        <label>Objetivo</label>
        <input type="text" class="form-control" wire:model="objetivo">
        @error('objetivo') <span>{{ $message }}</span> @enderror
    </div>

    {{-- NOTA: Aqui hay un TYPO -> wire:model="modlidad" deberia ser "modalidad"
         Esto causaria que el valor no se vincule correctamente con la
         propiedad $modalidad del componente PHP. La validacion 'modalidad'
         fallaria siempre porque $this->modalidad estaria vacio.
    --}}
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

    {{-- NOTA: Este boton type="submit" NO deberia estar aqui si se usa
         wire:click="store" en create.blade.php. El submit causaria una
         peticion HTTP tradicional (recarga de pagina) en vez de usar
         Livewire. Se podria quitar o reemplazar por:
         <button type="button" wire:click="store">Guardar</button>

         Alternativa con wire:submit en el <form>:
         <form wire:submit="store">
             ... inputs ...
             <button type="submit">Guardar</button>
         </form>
    --}}
    <button type="submit" class="btn btn-primary"> Guardar </button>
</form>

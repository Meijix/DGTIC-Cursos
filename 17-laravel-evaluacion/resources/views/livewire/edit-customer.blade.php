{{--
==========================================================================
MODULO 17 - PROYECTO DE EVALUACION: Vista "edit-customer" (Formulario de Edicion)
==========================================================================

PROPOSITO DE ESTA VISTA:
Formulario para EDITAR un cliente existente. Similar a create-customer
pero con los campos PRE-LLENADOS con los datos actuales del cliente.

DIFERENCIA CLAVE CON CREATE:
- En CREATE, los inputs estan vacios (wire:model se enlaza a propiedades vacias)
- En EDIT, los inputs tienen valores iniciales cargados por mount()
  Las propiedades ya tienen valor cuando la vista se renderiza

SOBRE EL ATRIBUTO value="" EN LOS INPUTS:
NOTA IMPORTANTE: Cuando se usa wire:model, el atributo value="" de HTML es
IGNORADO por Livewire. El valor viene de la propiedad PHP, no del HTML.
Por lo tanto, value="{{old('name', $customer->name)}}" es redundante aqui.
Livewire ya maneja el valor a traves de wire:model="name", que toma
el valor de la propiedad $name del componente PHP.

La funcion old() es util en formularios TRADICIONALES (sin Livewire)
para recordar los valores despues de un error de validacion.
En Livewire, esto ya se maneja automaticamente.
--}}

<div>
    {{--
    LAYOUT CON BOOTSTRAP GRID:
    - .offset-1: Desplaza la card 1 columna a la derecha
    - .col-10: Ocupa 10 de 12 columnas
    - Resultado: Card centrada con margenes laterales
    --}}
    <div class="card offset-1 col-10">
        <div class="card-header">
          Editar Cliente
        </div>
        <div class="card-body">
            {{--
            wire:submit="save":
            NOTA: Aqui wire:submit llama a "save" pero en el componente PHP
            el metodo se llama "update()". Esto podria causar un error.
            Lo correcto seria wire:submit="update" para que coincida.

            Este tipo de inconsistencia es un error comun en desarrollo
            y se detecta durante las pruebas manuales o automatizadas.
            --}}
            <form wire:submit="save">

                <div class="mb-3">
                  <label for="name" class="form-label">Nombre</label>
                  {{--
                  wire:model="name": Se enlaza a la propiedad $name del componente.
                  Como mount() ya asigno $name = $customer->name, el input
                  aparecera con el nombre actual del cliente.
                  --}}
                  <input wire:model="name" id="name" type="text" class="form-control" aria-describedby="nameHelp" value="{{old('name', $customer->name)}}">
                  @error('name')<span class="text-danger" >{{$message}}</span>@enderror
                </div>
                <div class="mb-3">
                    <label for="email" class="form-label">Dirección de Correo Electrónico</label>
                    <input wire:model="email" id="email" type="text" class="form-control" aria-describedby="emailHelp" value="{{old('email', $customer->email)}}">
                    @error('email')<span class="text-danger" >{{$message}}</span>@enderror
                </div>
                <div class="mb-3">
                  <label for="phone" class="form-label">Teléfono</label>
                  <input wire:model="phone" id="phone" type="text" class="form-control" value="{{old('phone', $customer->phone)}}">
                  @error('phone')<span class="text-danger" >{{$message}}</span>@enderror
                </div>
                <div class="mb-3">
                  <label for="address" class="form-label">Dirección</label>
                  <input wire:model="address"  id="address" type="text" class="form-control" value="{{old('address', $customer->address)}}">
                  @error('address')<span class="text-danger" >{{$message}}</span>@enderror
                </div>
                <div class="mb-3">
                  <label for="birthday" class="form-label">Fecha de nacimiento</label>
                  <input wire:model="birthday" id="birthday" type="date" class="form-control" value="{{old('birthday', $customer->birthday)}}">
                  @error('birthday')<span class="text-danger" >{{$message}}</span>@enderror
                </div>
                <button type="submit" class="btn btn-primary">Guardar</button>
                {{--
                BOTON REGRESAR:
                href="./" navega al directorio padre de la URL actual.
                Si estamos en /customers/5/edit, "./" nos lleva a /customers/5
                (la vista de detalle del cliente).

                Alternativa mas explicita: href="{{ route('customers') }}"
                --}}
                <a href="./" class="btn btn-primary">Regresar</a>
              </form>

              <!-- Mensaje de éxito -->
              @if (session()->has('message'))
                <div class="alert alert-success mt-3">
                    {{ session('message') }}
                </div>
              @endif
        </div>
      </div>
  </div>

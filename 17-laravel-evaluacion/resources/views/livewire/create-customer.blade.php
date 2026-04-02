{{--
==========================================================================
MODULO 17 - PROYECTO DE EVALUACION: Vista "create-customer" (Formulario de Creacion)
==========================================================================

PROPOSITO DE ESTA VISTA:
Formulario para crear un nuevo cliente. Cada campo esta conectado
al componente CreateCustomer.php mediante wire:model.

CONCEPTOS CLAVE DE FORMULARIOS LIVEWIRE:
1. wire:submit="save"    -> Al enviar el form, ejecuta el metodo save() en PHP
2. wire:model="campo"    -> Binding bidireccional (input <-> propiedad PHP)
3. @error('campo')       -> Muestra errores de validacion del campo especifico

DIFERENCIA ENTRE wire:submit Y action="":
  HTML tradicional:  <form action="/customers" method="POST">
    -> Envia los datos y RECARGA toda la pagina

  Livewire:          <form wire:submit="save">
    -> Envia los datos por AJAX, ejecuta save() en PHP,
       y actualiza SOLO las partes que cambiaron (sin recarga)

VARIANTES DE wire:model:
  wire:model="name"          -> Sincroniza en cada tecleo (tiempo real)
  wire:model.lazy="name"     -> Sincroniza al salir del campo (on blur)
  wire:model.defer="name"    -> Sincroniza solo al enviar el form (mas eficiente)
  wire:model.debounce.300ms  -> Sincroniza 300ms despues del ultimo tecleo
--}}

<div>
  <h1>Nuevo Cliente</h1>

  {{--
  COMPONENTE CARD DE BOOTSTRAP:
  - .card: Contenedor con bordes y sombra
  - .card-header: Encabezado gris
  - .card-body: Contenido principal
  - .col-10: Ocupa 10 de 12 columnas del grid de Bootstrap
  --}}
  <div class="card col-10">
      <div class="card-header">
        Ingresar los datos del cliente a registrar
      </div>
      <div class="card-body">
          {{--
          FORMULARIO CON wire:submit="save":
          Cuando el usuario presiona "Guardar", Livewire:
          1. Recopila los valores de todos los wire:model
          2. Hace una peticion AJAX al servidor
          3. Ejecuta el metodo save() en CreateCustomer.php
          4. Si hay errores de validacion, los muestra sin recargar
          5. Si todo sale bien, redirige a la lista de clientes
          --}}
          <form wire:submit="save">

              {{--
              PATRON DE CAMPO CON VALIDACION:
              Cada campo sigue este patron:
                1. <label>     -> Texto descriptivo (accesibilidad)
                2. <input>     -> Campo de entrada con wire:model
                3. @error      -> Mensaje de error si la validacion falla

              Este patron se repite para TODOS los campos del formulario.
              En proyectos grandes, se crearia un componente Blade reutilizable:
                <x-input-field name="name" label="Nombre" type="text" />
              --}}
              <div class="mb-3">
                <label for="name" class="form-label">Nombre</label>
                <input wire:model="name" id="name" type="text" class="form-control" aria-describedby="nameHelp">
                {{--
                @error('name'): Si la validacion del campo 'name' fallo,
                muestra el mensaje de error definido en $messages del componente.
                $message contiene el texto del error especifico.
                --}}
                @error('name')<span class="text-danger">{{$message}}</span>@enderror
              </div>

              <div class="mb-3">
                  <label for="email" class="form-label">Dirección de Correo Electrónico</label>
                  <input wire:model="email" id="email" type="email" class="form-control" aria-describedby="emailHelp">
                  @error('email')<span class="text-danger">{{$message}}</span>@enderror
              </div>

              <div class="mb-3">
                <label for="phone" class="form-label">Teléfono</label>
                <input wire:model="phone" id="phone" type="text" class="form-control">
                @error('phone')<span class="text-danger">{{$message}}</span>@enderror
              </div>

              <div class="mb-3">
                <label for="address" class="form-label">Dirección</label>
                <input wire:model="address" id="address" type="text" class="form-control">
                @error('address')<span class="text-danger">{{$message}}</span>@enderror
              </div>

              <div class="mb-3">
                <label for="birthday" class="form-label">Fecha de nacimiento</label>
                {{--
                type="date": Muestra un selector de fecha nativo del navegador.
                Es mejor que un input de texto porque:
                - Garantiza formato correcto de fecha
                - Mas facil de usar en moviles
                - No necesita validacion de formato en el cliente
                --}}
                <input wire:model="birthday" id="birthday" type="date" class="form-control">
                @error('birthday')<span class="text-danger">{{$message}}</span>@enderror
              </div>

              {{--
              BOTONES DE ACCION:
              - "Guardar": type="submit" dispara wire:submit="save"
              - "Regresar": <a> con route('customers') navega de vuelta a la lista
                            No es un boton de submit, es un enlace estilizado como boton
              --}}
              <button type="submit" class="btn btn-primary">Guardar</button>
              <a href="{{ route('customers') }}" class="btn btn-secondary">Regresar</a>
            </form>

            {{--
            MENSAJE FLASH DE EXITO:
            session()->flash('message', '...') en el componente PHP
            crea un mensaje temporal que se muestra UNA VEZ.

            session()->has('message') verifica si existe el mensaje.
            session('message') obtiene el texto del mensaje.

            NOTA: En este caso, el mensaje flash probablemente NO se vera
            porque save() hace redirect() antes de que se muestre.
            El mensaje se vera en la pagina de DESTINO (customers).
            --}}
            @if (session()->has('message'))
              <div class="alert alert-success mt-3">
                  {{ session('message') }}
              </div>
            @endif
      </div>
    </div>
</div>

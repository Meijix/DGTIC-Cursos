{{--
==========================================================================
MODULO 17 - PROYECTO DE EVALUACION: Vista "customers" (Lista de Clientes)
==========================================================================

PROPOSITO DE ESTA VISTA:
Muestra la tabla con TODOS los clientes y botones de accion (Ver, Editar, Borrar).
Es la vista principal del CRUD, asociada al componente Customers.php.

ESTRUCTURA DE LA VISTA:
1. Encabezado con titulo y boton "Crear Cliente"
2. Tabla HTML con los datos de cada cliente
3. Botones de accion por cada fila

DIRECTIVAS BLADE USADAS:
- @foreach / @endforeach  -> Bucle para iterar sobre los clientes
- @error / @enderror      -> Mostrar errores de validacion
- {{ }}                   -> Mostrar datos (con escape HTML = seguro contra XSS)
- {{-- --}}               -> Comentarios Blade (NO se envian al navegador)
- route('nombre')         -> Generar URL a partir del nombre de la ruta

DIRECTIVAS LIVEWIRE:
- wire:click="metodo()"   -> Ejecutar metodo PHP al hacer click
  Equivale a: addEventListener('click', () => fetch('/livewire/...'))
  Livewire hace la peticion AJAX automaticamente, sin recargar la pagina.

COMPARACION CON HTML/PHP TRADICIONAL:
  Tradicional: <a href="/customers/delete/5">Borrar</a> (recarga la pagina)
  Livewire:    <button wire:click="delete(5)">Borrar</button> (AJAX, sin recarga)
--}}

<div>
    {{--
    NOTA IMPORTANTE: Todo componente Livewire DEBE tener UN SOLO elemento raiz.
    Por eso todo esta dentro de un <div>. Si pones dos elementos al mismo nivel,
    Livewire no puede rastrear los cambios correctamente.
    --}}

    <h1>Clientes</h1>
    <p>En esta pagina se pueden administrar los clientes con los que cuenta la empresa</p>

    {{--
    NAVEGACION ENTRE COMPONENTES:
    Este enlace usa route('create') que apunta a /customers/create
    donde esta montado el componente CreateCustomer.

    Es navegacion TRADICIONAL (recarga completa de pagina).
    En Livewire 3 se podria usar wire:navigate para navegacion SPA.
    --}}
    <a href="{{ route('create') }}" class="btn btn-success btn-sm">Crear Cliente</a>
    <br><br>

    {{--
    TABLA HTML CON BOOTSTRAP:
    - class="table" aplica estilos de Bootstrap para tablas
    - <thead> define los encabezados
    - <tbody> contiene los datos dinamicos
    - scope="col" y scope="row" mejoran la accesibilidad (lectores de pantalla)
    --}}
    <table class="table">
        <thead>
            <tr>
                <th scope="col">#</th>
                <th scope="col">Nombre</th>
                <th scope="col">Correo Electrónico</th>
                <th scope="col">Teléfono</th>
                <th scope="col">Dirección</th>
                <th scope="col">Fecha de Nacimiento</th>
                <th scope="col">Opciones</th>
            </tr>
        </thead>
        <tbody>
            {{--
            DIRECTIVA @foreach:
            Itera sobre $customers (la propiedad publica del componente PHP).
            Cada $customer es una instancia del modelo Customer con acceso
            a todas sus propiedades: ->id, ->name, ->email, etc.

            SEGURIDAD: {{ $customer->name }} usa "double curly braces"
            que ESCAPAN caracteres HTML automaticamente:
              Si name = "<script>alert('hack')</script>"
              Se muestra como texto, NO se ejecuta el script.

            Para HTML sin escapar se usa {!! $variable !!} (PELIGROSO, evitar).
            --}}
            @foreach ($customers as $customer)
                <tr>
                    <th scope="row">{{$customer->id}}</th>
                    <td>{{$customer->name}}</td>
                    <td>{{$customer->email}}</td>
                    <td>{{$customer->phone}}</td>
                    <td>{{$customer->address}}</td>
                    <td>{{$customer->birthday}}</td>
                    <td>
                        {{--
                        BOTONES DE ACCION - Tres patrones diferentes:

                        1. VER y EDITAR: Usan <a href=""> (navegacion tradicional)
                           - route('view', ['customer' => $customer->id])
                           - Genera: /customers/5 o /customers/5/edit
                           - El parametro 'customer' coincide con {customer} en la ruta

                        2. BORRAR: Usa wire:click (accion Livewire sin navegacion)
                           - wire:click="delete({{ $customer->id }})"
                           - Ejecuta el metodo delete() en Customers.php
                           - La tabla se actualiza SIN recargar la pagina

                        CRITERIO DE EVALUACION:
                        Mezclar navegacion HTML con acciones Livewire es valido.
                        Las acciones que NO requieren nueva pagina (como borrar)
                        se manejan mejor con wire:click.
                        --}}

                        {{-- Ver: Navega al componente ViewCustomer --}}
                        <a href="{{ route('view', ['customer' => $customer->id]) }}" class="btn btn-primary btn-sm">Ver</a>
                        {{-- Editar: Navega al componente EditCustomer --}}
                        <a href="{{ route('edit', ['customer' => $customer->id]) }}" class="btn btn-secondary btn-sm">Editar</a>
                        {{-- Borrar: Ejecuta metodo delete() via AJAX con Livewire --}}
                        <button class="btn btn-danger btn-sm" wire:click="delete({{ $customer->id }})" onclick="return confirm('¿Seguro que deseas eliminar este cliente?')" >Borrar</button>
                        {{-- <form wire:submit="save" action="delete" method="POST" style="display:inline;">
                            @csrf
                            @method('DELETE')
                            <button type="submit" class="btn btn-danger btn-sm" onclick="return confirm('¿Estás seguro de que quieres eliminar este cliente?')"> Borrar </button>
                        </form> --}}

                    </td>
                </tr>
            @endforeach
        </tbody>
    </table>
</div>

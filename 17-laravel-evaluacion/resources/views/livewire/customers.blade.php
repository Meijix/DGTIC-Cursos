<div>
    
    <h1>Clientes</h1>
    <p>En esta pagina se pueden administrar los clientes con los que cuenta la empresa</p>

    <a href="{{ route('create') }}" class="btn btn-success btn-sm">Crear Cliente</a>
    <br><br>
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
            @foreach ($customers as $customer)
                <tr>
                    <th scope="row">{{$customer->id}}</th>
                    <td>{{$customer->name}}</td>
                    <td>{{$customer->email}}</td>
                    <td>{{$customer->phone}}</td>
                    <td>{{$customer->address}}</td>
                    <td>{{$customer->birthday}}</td>
                    <td>
                        {{-- Ver --}}
                        <a href="{{ route('view', ['customer' => $customer->id]) }}" class="btn btn-primary btn-sm">Ver</a>
                        {{-- Editar --}}
                        <a href="{{ route('edit', ['customer' => $customer->id]) }}" class="btn btn-secondary btn-sm">Editar</a>
                        {{-- Borrar --}}
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

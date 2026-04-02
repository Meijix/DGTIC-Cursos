<div>
  <div class="card">
    <h5 class="card-header">Datos del Cliente</h5>
    <div class="card-body">
      <h5 class="card-title">{{$customer->name}}</h5>
      <p class="card-text">
      <table class="table">
        <thead>
          <tr>
            <th>Email</th>
            <th>Teléfono</th>
            <th>Direccion</th>
            <th>Fecha de nacimiento</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>{{$customer->email}}</td>
            <td>{{$customer->phone}}</td>
            <td>{{$customer->address}}</td>
            <td>{{$customer->birthday}}</td>
          </tr>
        </tbody>
      </table>
      </p>

      <a href="./" class="btn btn-primary">Volver</a>
      {{-- Editar --}}
      <a href="{{ route('edit', ['customer' => $customer->id]) }}" class="btn btn-secondary btn-sm">Editar</a>
    </div>
  </div>
</div>

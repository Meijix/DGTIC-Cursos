<div>
    <div class="card offset-1 col-10">
        <div class="card-header">
          Editar Cliente
        </div>
        <div class="card-body">
            <form wire:submit="save">
              
                <div class="mb-3">
                  <label for="name" class="form-label">Nombre</label>
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
  
  
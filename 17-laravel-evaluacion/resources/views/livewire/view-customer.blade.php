{{--
==========================================================================
MODULO 17 - PROYECTO DE EVALUACION: Vista "view-customer" (Detalle de Cliente)
==========================================================================

PROPOSITO DE ESTA VISTA:
Muestra los datos completos de UN cliente en formato de tarjeta (Card).
Es una vista de SOLO LECTURA — no tiene formularios ni inputs.

DIFERENCIA CON LA LISTA:
- La lista (customers.blade.php) muestra MUCHOS clientes en una tabla resumida
- Esta vista muestra UN cliente con TODOS sus detalles

EN PROYECTOS REALES, aqui se mostrarian:
- Datos completos del cliente
- Relaciones (pedidos, facturas, historial)
- Acciones rapidas (editar, enviar email, generar reporte)
- Notas y comentarios internos

PATRON DE VISTA DE DETALLE:
Es comun en aplicaciones CRUD tener una vista de detalle que sirve como
"hub" desde donde se puede navegar a otras acciones (editar, volver, etc.)
--}}

<div>
  {{--
  COMPONENTE CARD DE BOOTSTRAP:
  Estructura semantica para mostrar informacion agrupada:
  - .card: Contenedor principal con bordes
  - .card-header: Titulo de la seccion
  - .card-body: Contenido principal
  - .card-title: Titulo dentro del body
  - .card-text: Texto descriptivo
  --}}
  <div class="card">
    <h5 class="card-header">Datos del Cliente</h5>
    <div class="card-body">
      {{--
      $customer->name: Accede a la propiedad 'name' del modelo Customer.
      Recuerda que $customer es la propiedad publica del componente PHP,
      que fue cargada automaticamente por Route Model Binding en mount().
      --}}
      <h5 class="card-title">{{$customer->name}}</h5>
      <p class="card-text">
      {{--
      TABLA DE DATOS DEL CLIENTE:
      Se usa una tabla para mostrar los datos de forma organizada.
      Cada propiedad del modelo se accede con $customer->propiedad.

      Las propiedades disponibles corresponden a las columnas de la tabla
      definidas en la migracion: email, phone, address, birthday.
      --}}
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

      {{--
      BOTONES DE NAVEGACION:

      "Volver" (href="./"):
        Navega al directorio padre. Desde /customers/5, va a /customers/
        que es la lista de clientes.

      "Editar":
        route('edit', ['customer' => $customer->id]) genera la URL
        /customers/5/edit pasando el ID del cliente actual.

      CRITERIO DE EVALUACION: Navegacion entre componentes
      - Desde la vista de detalle se puede ir a editar directamente
      - Se puede volver a la lista facilmente
      - Esto crea un flujo de navegacion intuitivo para el usuario
      --}}
      <a href="./" class="btn btn-primary">Volver</a>
      {{-- Editar --}}
      <a href="{{ route('edit', ['customer' => $customer->id]) }}" class="btn btn-secondary btn-sm">Editar</a>
    </div>
  </div>
</div>

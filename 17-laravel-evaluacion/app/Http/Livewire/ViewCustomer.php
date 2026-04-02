<?php
/**
 * ==========================================================================
 * MODULO 17 - PROYECTO DE EVALUACION: Componente "ViewCustomer"
 * ==========================================================================
 *
 * PROPOSITO DE ESTE ARCHIVO:
 * Componente Livewire de SOLO LECTURA para ver el detalle de un cliente.
 * Es el componente mas simple de todo el CRUD.
 *
 * ESTE ES UN COMPONENTE DE "SOLO LECTURA":
 * - No tiene formularios
 * - No tiene metodos de modificacion (save, update, delete)
 * - Solo carga datos y los muestra
 *
 * ROUTE MODEL BINDING:
 * Al igual que EditCustomer, este componente usa Route Model Binding.
 * La ruta /customers/{customer} automaticamente busca el Customer por ID
 * y lo inyecta en mount(Customer $customer).
 *
 * POR QUE TENER UN COMPONENTE SOLO PARA VER?
 * 1. La lista muestra datos resumidos en una tabla (muchos clientes, pocos campos)
 * 2. La vista de detalle muestra TODA la informacion de UN cliente
 * 3. En proyectos reales, aqui se mostrarian relaciones:
 *    - Pedidos del cliente
 *    - Historial de compras
 *    - Notas internas
 *    - Documentos adjuntos
 *
 * CRITERIO DE EVALUACION: Separacion de vistas
 * - Tener una vista de detalle separada es buena practica
 * - Permite mostrar informacion que no cabe en la tabla de la lista
 */

namespace App\Http\Livewire;



use Livewire\Component;
use App\Models\Customer;

class ViewCustomer extends Component
{
    /**
     * El modelo Customer cargado desde la base de datos.
     *
     * Se inicializa como array vacio [] por seguridad, pero mount()
     * lo reemplaza con el objeto Customer completo.
     *
     * NOTA: En la vista se accede con $customer->name, $customer->email, etc.
     * Livewire pasa esta propiedad automaticamente a la vista por ser "public".
     */
    public $customer=[];

    /**
     * ROUTE MODEL BINDING: Carga automatica del cliente desde la URL.
     *
     * Ruta: Route::get('/customers/{customer}', ViewCustomer::class)
     *
     * Si el usuario visita /customers/3:
     *   - Laravel busca Customer::findOrFail(3)
     *   - Si existe: lo pasa como $customer
     *   - Si NO existe: responde automaticamente con error 404
     *
     * COMPARACION CON BUSQUEDA MANUAL:
     *   // Sin Route Model Binding (forma manual):
     *   public function mount($id) {
     *       $this->customer = Customer::find($id);
     *       if (!$this->customer) abort(404);
     *   }
     *
     *   // Con Route Model Binding (forma elegante):
     *   public function mount(Customer $customer) {
     *       $this->customer = $customer;  // Ya viene cargado
     *   }
     *
     * La segunda forma es mas limpia y es la forma "Laravel" de hacerlo.
     */
    public function mount(Customer $customer)
    {
        $this->customer=$customer;
    }

    public function render()
    {
        return view('livewire.view-customer');
    }
}

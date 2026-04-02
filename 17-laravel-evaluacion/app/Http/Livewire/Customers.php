<?php

namespace App\Http\Livewire;


use App\Models\Customer;
use Livewire\Component;

class Customers extends Component
{
    public $customers=[]; 

    public function mount()
    {
        $this->customers=Customer::all();
    }

    // método para eliminar un cliente

    public function delete($id) //busca al cliente por su id
    {
        $customer = Customer::find($id);
        if ($customer) {
            $customer->delete();  // Elimina el cliente
            $this->customers = Customer::all();  // Actualiza la lista de clientes
            session()->flash('message', 'Cliente eliminado correctamente.');  // Mensaje de éxito
        }
    }

    public function render()
    {
        return view('livewire.customers');
    }


}


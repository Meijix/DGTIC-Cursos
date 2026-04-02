<?php
/**
 * ==========================================================================
 * MODULO 17 - PROYECTO DE EVALUACION: Componente Livewire "Customers"
 * ==========================================================================
 *
 * PROPOSITO DE ESTE ARCHIVO:
 * Este es el componente Livewire principal que muestra la LISTA de todos
 * los clientes y permite ELIMINARLOS. Es la "pagina de inicio" del CRUD.
 *
 * PATRON DE COMPOSICION (Diferencia con el Modulo 16):
 * En el modulo 16, todo el CRUD estaba en UN SOLO componente Livewire.
 * Aqui se usa el patron de COMPOSICION: cada operacion CRUD tiene su
 * propio componente independiente:
 *
 *   Customers.php      -> Listar + Eliminar (este archivo)
 *   CreateCustomer.php -> Crear
 *   EditCustomer.php   -> Editar
 *   ViewCustomer.php   -> Ver detalle
 *
 * VENTAJAS DE SEPARAR EN MULTIPLES COMPONENTES:
 * 1. Cada componente tiene UNA SOLA responsabilidad (Principio SRP)
 * 2. El codigo es mas facil de leer y mantener
 * 3. Los componentes se pueden reutilizar en diferentes paginas
 * 4. Cada componente tiene sus propias reglas de validacion
 * 5. Mas facil de testear individualmente
 *
 * CRITERIO DE EVALUACION: Organizacion del codigo
 * - Separar responsabilidades demuestra madurez como desarrollador
 * - Es una BUENA PRACTICA en proyectos reales
 *
 * FLUJO DE NAVEGACION:
 *   [Lista] --click "Crear"--> CreateCustomer
 *   [Lista] --click "Ver"----> ViewCustomer
 *   [Lista] --click "Editar"--> EditCustomer
 *   [Lista] --click "Borrar"--> delete() (en este mismo componente)
 */

namespace App\Http\Livewire;


use App\Models\Customer;
use Livewire\Component;

/**
 * Componente Livewire para listar y eliminar clientes.
 *
 * CONCEPTOS CLAVE:
 * - Livewire\Component: Clase base de la que heredan TODOS los componentes Livewire
 * - Las propiedades "public" se sincronizan automaticamente con la vista Blade
 * - El metodo mount() es el "constructor" de Livewire (se ejecuta al cargar)
 * - El metodo render() devuelve la vista que se mostrara
 */
class Customers extends Component
{
    /**
     * Lista de todos los clientes.
     *
     * NOTA IMPORTANTE SOBRE PROPIEDADES PUBLICAS:
     * En Livewire, las propiedades "public" son REACTIVAS:
     * - Se pasan automaticamente a la vista Blade (no necesitas compact())
     * - Cuando cambian en PHP, la vista se actualiza automaticamente
     * - Es similar a "state" en React o "data" en Vue.js
     *
     * Se inicializa como array vacio [] para evitar errores si mount()
     * falla o se llama render() antes de mount().
     */
    public $customers=[];

    /**
     * Metodo mount(): El "constructor" de componentes Livewire.
     *
     * DIFERENCIA ENTRE mount() Y __construct():
     * - __construct() se ejecuta CADA VEZ que Livewire hace un request (no usar)
     * - mount() se ejecuta SOLO UNA VEZ cuando el componente se carga por primera vez
     *
     * Customer::all() - Metodo de Eloquent ORM que obtiene TODOS los registros
     * Equivale a: SELECT * FROM customers;
     *
     * CRITERIO DE EVALUACION: Uso correcto de Eloquent
     * - Usar Customer::all() es correcto para datasets pequenos
     * - Para grandes volumenes, seria mejor usar paginacion:
     *   Customer::paginate(15) con el trait WithPagination de Livewire
     */
    public function mount()
    {
        $this->customers=Customer::all();
    }

    /**
     * Metodo para eliminar un cliente por su ID.
     *
     * COMO FUNCIONA LA COMUNICACION VISTA -> COMPONENTE:
     * 1. En la vista Blade: wire:click="delete({{ $customer->id }})"
     * 2. Livewire intercepta el click y hace una peticion AJAX al servidor
     * 3. PHP ejecuta este metodo delete() con el ID recibido
     * 4. El componente se re-renderiza automaticamente
     *
     * PATRON DEFENSIVO con find() + if():
     * - Customer::find($id) devuelve null si no existe el registro
     * - El if() previene errores al intentar eliminar algo inexistente
     * - Esto es una BUENA PRACTICA de programacion defensiva
     *
     * ALTERNATIVA: Customer::findOrFail($id)
     * - Lanza una excepcion 404 si no encuentra el registro
     * - Util cuando SIEMPRE deberia existir el registro
     *
     * CRITERIO DE EVALUACION: Manejo de errores
     * - Verificar que el registro existe antes de operar es correcto
     * - El mensaje flash informa al usuario del resultado
     */
    public function delete($id) //busca al cliente por su id
    {
        $customer = Customer::find($id);
        if ($customer) {
            $customer->delete();  // Elimina el cliente
            $this->customers = Customer::all();  // Actualiza la lista de clientes
            session()->flash('message', 'Cliente eliminado correctamente.');  // Mensaje de éxito
        }
    }

    /**
     * Metodo render(): Devuelve la vista Blade asociada a este componente.
     *
     * CONVENCION DE NOMBRES EN LIVEWIRE:
     * - Componente: Customers (PascalCase)
     * - Vista: livewire/customers.blade.php (kebab-case)
     * - Livewire puede inferir la vista automaticamente, pero es
     *   mejor ser explicito para mayor claridad
     *
     * NOTA: La propiedad $customers se pasa AUTOMATICAMENTE a la vista
     * porque es "public". No necesitamos hacer:
     *   return view('livewire.customers', ['customers' => $this->customers]);
     */
    public function render()
    {
        return view('livewire.customers');
    }


}

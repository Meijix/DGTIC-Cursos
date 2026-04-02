<?php
/**
 * ==========================================================================
 * MODULO 17 - PROYECTO DE EVALUACION: Componente "EditCustomer"
 * ==========================================================================
 *
 * PROPOSITO DE ESTE ARCHIVO:
 * Componente Livewire dedicado a la EDICION de clientes existentes.
 * Carga los datos actuales del cliente y permite modificarlos.
 *
 * CONCEPTO CLAVE: ROUTE MODEL BINDING (Enlace Modelo-Ruta)
 * Este es uno de los conceptos MAS IMPORTANTES de Laravel.
 *
 * Cuando la ruta es: /customers/{customer}/edit
 * Y el metodo mount recibe: mount(Customer $customer)
 *
 * Laravel AUTOMATICAMENTE:
 * 1. Toma el valor {customer} de la URL (ejemplo: /customers/5/edit -> 5)
 * 2. Busca en la tabla customers el registro con id = 5
 * 3. Crea una instancia del modelo Customer con esos datos
 * 4. Lo inyecta como parametro $customer en mount()
 *
 * Es decir, Laravel hace Customer::findOrFail(5) POR TI.
 * Si el cliente no existe, Laravel automaticamente devuelve error 404.
 *
 * COMPARACION CREATE vs EDIT:
 *   CreateCustomer:
 *   - mount() no recibe parametros (formulario vacio)
 *   - save() usa Customer::create() (INSERT)
 *   - Reglas unique sin excepcion
 *
 *   EditCustomer:
 *   - mount(Customer $customer) recibe el modelo (Route Model Binding)
 *   - update() usa $this->customer->update() (UPDATE)
 *   - Reglas unique DEBERIAN excluir el registro actual (ver nota abajo)
 *
 * NOTA SOBRE VALIDACION UNIQUE EN EDICION:
 * Las reglas unique en este componente pueden causar problemas:
 *   'email' => 'required|email|unique:customers,email'
 * Si el usuario NO cambia el email, la validacion fallara porque
 * el email "ya existe" (es el mismo registro). La solucion correcta es:
 *   'email' => 'required|email|unique:customers,email,' . $this->customer->id
 * Esto le dice a Laravel: "es unico, EXCEPTO el registro con este ID"
 */
namespace App\Http\Livewire;

use Livewire\Component;
use App\Models\Customer;

class EditCustomer extends Component
{
    /**
     * El modelo Customer completo cargado desde la base de datos.
     *
     * IMPORTANTE: Esta propiedad almacena el OBJETO Customer completo,
     * no solo el ID. Esto permite hacer $this->customer->update() despues.
     *
     * Las siguientes propiedades ($name, $email, etc.) son COPIAS de los
     * valores del modelo. Se usan para el binding bidireccional con el
     * formulario (wire:model). Cuando el usuario edita un campo, solo
     * cambia la copia, NO el modelo original, hasta que se llame update().
     */
    public $customer;
    public $name, $email, $phone, $address, $birthday;

    /**
     * Reglas de validacion con expresiones regulares.
     *
     * EXPRESIONES REGULARES (regex) - Conceptos basicos:
     *   /^[\pL\s]+$/u  -> Solo letras Unicode (\pL) y espacios (\s)
     *                      ^ = inicio, $ = final, + = uno o mas
     *                      u = flag Unicode (para acentos, ene, etc.)
     *
     *   /^[0-9]+$/     -> Solo digitos del 0 al 9
     *                      + = uno o mas digitos
     *
     * CRITERIO DE EVALUACION: Validacion robusta
     * - regex previene inyeccion de caracteres especiales
     * - Combinar regex + min + max da validacion completa
     */
    protected $rules = [
        'name' => 'required|regex:/^[\pL\s]+$/u|max:50', // Solo letras y espacios
        'email' => 'required|email|unique:customers,email',
        'phone' => 'required|regex:/^[0-9]+$/|min:10|max:15|unique:customers,phone', // Solo números y mínimo 10 dígitos
        'address' => 'required|max:255',
        'birthday' => 'required|date|before:today',
    ];

    /**
     * Mensajes personalizados de validacion en espanol.
     * (Identicos a CreateCustomer para mantener consistencia de UX)
     */
    protected $messages = [
        'name.required' => 'El campo nombre es obligatorio.',
        'name.regex' => 'El nombre solo puede contener letras y espacios.',
        'email.required' => 'El correo electrónico es obligatorio.',
        'email.email' => 'Ingrese un correo válido.',
        'email.unique' => 'Este correo ya está registrado.',
        'phone.required' => 'El número de teléfono es obligatorio.',
        'phone.regex' => 'El teléfono solo puede contener números.',
        'phone.min' => 'El teléfono debe tener al menos 10 dígitos.',
        'phone.max' => 'El teléfono no puede tener más de 15 dígitos.',
        'phone.unique' => 'El número de teléfono ya está registrado.',
        'address.required' => 'La dirección es obligatoria.',
        'birthday.required' => 'La fecha de nacimiento es obligatoria.',
        'birthday.date' => 'Ingrese una fecha válida.',
        'birthday.before' => 'La fecha de nacimiento debe ser anterior a hoy.',
    ];

    /**
     * Metodo mount(): Carga los datos del cliente para edicion.
     *
     * ROUTE MODEL BINDING EN ACCION:
     * Cuando el usuario visita /customers/5/edit:
     *
     *   1. Laravel mira la ruta: Route::get('/customers/{customer}/edit', EditCustomer::class)
     *   2. El parametro {customer} tiene valor "5"
     *   3. Laravel ve que mount() pide "Customer $customer" (type hint)
     *   4. Ejecuta internamente: Customer::findOrFail(5)
     *   5. Pasa el resultado como $customer a mount()
     *
     * Luego, mount() copia cada campo del modelo a una propiedad publica.
     * Esto es necesario porque wire:model necesita propiedades independientes,
     * no puede hacer wire:model="customer.name" directamente en Livewire 2.
     *
     * CRITERIO DE EVALUACION: Route Model Binding
     * - Usar type hint (Customer $customer) es la forma CORRECTA
     * - Evita hacer Customer::find($id) manualmente
     * - Laravel maneja automaticamente el caso "no encontrado" (404)
     */
    // Laravel resuelve automáticamente el modelo basado en la URL (customers/{customer}/edit)
    public function mount(Customer $customer)
    {
        $this->customer = $customer;
        $this->name = $customer->name;
        $this->email = $customer->email;
        $this->phone = $customer->phone;
        $this->address = $customer->address;
        $this->birthday = $customer->birthday;
    }

    /**
     * Metodo update(): Actualiza el cliente en la base de datos.
     *
     * DIFERENCIA ENTRE create() Y update():
     *   Customer::create([...])         -> INSERT INTO customers ...
     *   $this->customer->update([...])  -> UPDATE customers SET ... WHERE id = X
     *
     * Como $this->customer ya es una instancia de Customer cargada desde la BD,
     * llamar ->update() sabe EXACTAMENTE que registro actualizar.
     *
     * FLUJO:
     * 1. validate() - Verifica las reglas (igual que en create)
     * 2. $this->customer->update() - Actualiza SOLO los campos especificados
     * 3. flash message + redirect - Informa al usuario y redirige
     *
     * CRITERIO DE EVALUACION: Actualizacion correcta
     * - Validar antes de actualizar (igual que al crear)
     * - Usar el modelo cargado, no buscar de nuevo por ID
     * - Redirigir despues de guardar (patron PRG)
     */
    public function update()
    {
        $this->validate();

        // Actualiza directamente usando el modelo cargado
        $this->customer->update([
            'name' => $this->name,
            'email' => $this->email,
            'phone' => $this->phone,
            'address' => $this->address,
            'birthday' => $this->birthday,
        ]);

        session()->flash('message', 'Cliente actualizado correctamente.');
        return redirect()->route('customers');
    }

    public function render()
    {
        return view('livewire.edit-customer');
    }
}

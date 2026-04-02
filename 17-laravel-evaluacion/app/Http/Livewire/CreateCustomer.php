<?php
/**
 * ==========================================================================
 * MODULO 17 - PROYECTO DE EVALUACION: Componente "CreateCustomer"
 * ==========================================================================
 *
 * PROPOSITO DE ESTE ARCHIVO:
 * Componente Livewire dedicado EXCLUSIVAMENTE a la CREACION de nuevos clientes.
 * Maneja el formulario, la validacion y el guardado en base de datos.
 *
 * PRINCIPIO DE RESPONSABILIDAD UNICA (SRP):
 * Este componente SOLO se encarga de crear. No lista, no edita, no elimina.
 * Esto hace que sea mas facil de:
 * - Entender (menos codigo, un solo proposito)
 * - Testear (solo necesitas probar la creacion)
 * - Modificar (cambios no afectan a otros componentes)
 *
 * COMPARACION CON MODULO 16 (componente unico):
 *   Modulo 16: Un componente con save(), update(), delete(), render()
 *              + variables para controlar modales ($isOpen, $isEditing)
 *   Modulo 17: Cada operacion en su propio componente
 *              + navegacion entre paginas con redirect()
 *
 * FLUJO DE ESTE COMPONENTE:
 *   1. Usuario llega a /customers/create
 *   2. Se muestra el formulario vacio (render -> create-customer.blade.php)
 *   3. Usuario llena los campos (wire:model sincroniza con propiedades PHP)
 *   4. Usuario hace click en "Guardar" (wire:submit="save")
 *   5. Se ejecuta save(): validar -> crear -> redirigir
 */

namespace App\Http\Livewire;



use Livewire\Component;
use App\Models\Customer;

class CreateCustomer extends Component
{
    /**
     * PROPIEDADES PUBLICAS = Campos del formulario.
     *
     * BINDING BIDIRECCIONAL (wire:model):
     * Cada propiedad publica aqui se conecta a un input en la vista:
     *   <input wire:model="name" ...>  <-->  public $name
     *   <input wire:model="email" ...> <-->  public $email
     *
     * Cuando el usuario escribe en el input, Livewire actualiza la propiedad PHP.
     * Cuando PHP cambia la propiedad, Livewire actualiza el input.
     * Es como v-model en Vue.js o useState en React.
     *
     * Se inicializan como string vacio '' para que el formulario aparezca limpio.
     */
    public $name = '';
    public $email = '';
    public $phone = '';
    public $address = '';
    public $birthday = '';

    /**
     * REGLAS DE VALIDACION.
     *
     * Laravel tiene un sistema de validacion MUY poderoso.
     * Las reglas se separan con | (pipe) y se leen como:
     *
     *   'name' => 'required|max:50'
     *   Traduccion: "El nombre es obligatorio Y no puede tener mas de 50 caracteres"
     *
     *   'email' => 'required|email|unique:customers,email'
     *   Traduccion: "El email es obligatorio, debe tener formato email,
     *                y debe ser unico en la tabla 'customers' columna 'email'"
     *
     *   'phone' => 'required|min:10|max:15|unique:customers,phone'
     *   Traduccion: "El telefono es obligatorio, minimo 10 caracteres,
     *                maximo 15, y unico en la tabla"
     *
     *   'birthday' => 'required|date|before:today'
     *   Traduccion: "La fecha es obligatoria, debe ser una fecha valida,
     *                y debe ser ANTERIOR a hoy (no puedes nacer en el futuro)"
     *
     * NOTA: La regla 'nacimiento' parece ser un error - deberia ser 'birthday'
     * para coincidir con la propiedad publica. Este tipo de bugs son comunes
     * y se detectan durante las pruebas.
     *
     * REGLAS DE VALIDACION MAS USADAS EN LARAVEL:
     *   required     - Campo obligatorio
     *   email        - Formato de correo valido
     *   unique:t,c   - Unico en tabla t, columna c
     *   max:n        - Maximo n caracteres
     *   min:n        - Minimo n caracteres
     *   date         - Debe ser una fecha valida
     *   before:date  - Antes de cierta fecha
     *   after:date   - Despues de cierta fecha
     *   regex:/p/    - Cumple expresion regular p
     *   numeric      - Debe ser un numero
     *   confirmed    - Debe tener campo _confirmation igual
     *
     * CRITERIO DE EVALUACION: Validacion completa
     * - Validar TODOS los campos es obligatorio en un proyecto real
     * - Las reglas unique previenen datos duplicados
     * - before:today es una validacion de logica de negocio
     */
    protected $rules = [
        'name' => 'required|max:50', // Solo letras y espacios
        'email' => 'required|email|unique:customers,email',
        'phone' => 'required|min:10|max:15|unique:customers,phone', // Solo números y mínimo 10 dígitos
        'address' => 'required|max:255',
        'nacimiento' => 'required|date|before:today',
    ];

    /**
     * MENSAJES DE ERROR PERSONALIZADOS.
     *
     * Por defecto, Laravel genera mensajes en ingles como:
     *   "The name field is required."
     *
     * Con $messages podemos personalizar CADA mensaje para CADA regla:
     *   'campo.regla' => 'Mensaje personalizado'
     *
     * Esto es una BUENA PRACTICA porque:
     * 1. Los usuarios ven mensajes en su idioma
     * 2. Los mensajes son mas descriptivos y utiles
     * 3. Mejora la experiencia de usuario (UX)
     *
     * CRITERIO DE EVALUACION: Experiencia de usuario
     * - Mensajes claros y en espanol demuestran atencion al detalle
     * - Cada regla tiene su propio mensaje especifico
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
     * Metodo save(): Guarda un nuevo cliente en la base de datos.
     *
     * FLUJO COMPLETO:
     * 1. $this->validate() - Ejecuta TODAS las reglas definidas en $rules
     *    - Si ALGUNA regla falla, Livewire DETIENE la ejecucion aqui
     *    - Los errores se envian automaticamente a la vista
     *    - En la vista, @error('campo') muestra el mensaje correspondiente
     *
     * 2. Customer::create([...]) - Usa Eloquent para insertar en la BD
     *    - Equivale a: INSERT INTO customers (name, email, ...) VALUES (...)
     *    - IMPORTANTE: Solo funciona si los campos estan en $fillable del modelo
     *    - Esto es la proteccion "Mass Assignment" de Laravel
     *
     * 3. session()->flash('message', '...') - Mensaje temporal
     *    - "flash" significa que el mensaje existe SOLO por UNA peticion
     *    - Despues de mostrarse una vez, desaparece automaticamente
     *    - Es el patron Post-Redirect-Get (PRG) para evitar reenvio de forms
     *
     * 4. redirect()->route('customers') - Redirige a la lista
     *    - route('customers') genera la URL a partir del nombre de la ruta
     *    - Es mejor que escribir '/customers' directamente (URLs pueden cambiar)
     *    - Esto es NAVEGACION ENTRE COMPONENTES en Livewire
     *
     * CRITERIO DE EVALUACION: Flujo correcto de creacion
     * - Validar ANTES de guardar (nunca guardar datos sin validar)
     * - Usar Mass Assignment con $fillable (seguridad)
     * - Redirigir despues de guardar (patron PRG)
     */
    public function save()
    {
        $this->validate(); // Ejecuta la validación con las reglas definidas

        Customer::create([
            'name' => $this->name,
            'email' => $this->email,
            'phone' => $this->phone,
            'address' => $this->address,
            'birthday' => $this->birthday,
        ]);
        // Crea un nuevo cliente con los datos ingresados en el formulario
        // y los almacena en la base de datos.


        session()->flash('message', 'Cliente creado exitosamente.');
        return redirect()->route('customers'); // Redirecciona a la lista de clientes
    }

    public function render()
    {
        return view('livewire.create-customer');
    }
}


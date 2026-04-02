<?php
/*
|==========================================================================
| CursoComponent.php - Componente Livewire para CRUD de Cursos
|==========================================================================
|
| QUE ES LIVEWIRE:
| Livewire es un framework de Laravel que permite crear interfaces
| reactivas (como las de React/Vue) sin escribir JavaScript.
| Cada componente Livewire tiene una clase PHP + una vista Blade.
|
| COMO FUNCIONA LIVEWIRE (bajo el capo):
|
|   +------------------+     +------------------+     +------------------+
|   | NAVEGADOR        |     | SERVIDOR Laravel |     | BASE DE DATOS   |
|   | (Blade + JS)     |     | (Componente PHP) |     |                 |
|   +------------------+     +------------------+     +------------------+
|   |                  |     |                  |     |                 |
|   | 1. Usuario       |     |                  |     |                 |
|   |    escribe en    |     |                  |     |                 |
|   |    un input      |     |                  |     |                 |
|   |                  |     |                  |     |                 |
|   | 2. Livewire.js   |     |                  |     |                 |
|   |    detecta el    |     |                  |     |                 |
|   |    cambio        |     |                  |     |                 |
|   |                  |     |                  |     |                 |
|   | 3. Envia AJAX -->|---->| 4. Actualiza la  |     |                 |
|   |    con el nuevo  |     |    propiedad PHP |     |                 |
|   |    valor         |     |    $this->nombre |     |                 |
|   |                  |     |                  |     |                 |
|   |                  |     | 5. Re-ejecuta    |     |                 |
|   |                  |     |    render()      |     |                 |
|   |                  |     |                  |     |                 |
|   | 6. Recibe HTML<--|<----| 7. Retorna HTML  |     |                 |
|   |    actualizado   |     |    nuevo         |     |                 |
|   |                  |     |                  |     |                 |
|   | 8. DOM diffing   |     |                  |     |                 |
|   |    (solo cambia  |     |                  |     |                 |
|   |    lo necesario) |     |                  |     |                 |
|   +------------------+     +------------------+     +------------------+
|
| COMPARACION: CRUD TRADICIONAL (Modulo 15) vs LIVEWIRE (Modulo 16):
|
|   TRADICIONAL:                    LIVEWIRE:
|   - Cada accion = recarga total   - Cada accion = AJAX parcial
|   - Formulario POST -> redirige   - wire:click -> actualiza en el mismo lugar
|   - Necesita rutas CRUD           - Una sola ruta, todo en el componente
|   - Controlador separado          - Logica en la clase del componente
|   - Paginas separadas             - Todo puede estar en una sola pagina
|
| CICLO DE VIDA DEL COMPONENTE:
|   1. mount()     -> Se ejecuta UNA sola vez al cargar el componente
|   2. render()    -> Se ejecuta cada vez que hay un cambio
|   3. hydrate()   -> Antes de procesar una accion (rehidratacion)
|   4. updated*()  -> Despues de que una propiedad cambia
|   5. dehydrate() -> Despues de render(), antes de enviar al navegador
|
| GENERAR UN COMPONENTE LIVEWIRE:
|   php artisan make:livewire CursoComponent
|   Esto crea:
|     - app/Livewire/CursoComponent.php (esta clase)
|     - resources/views/livewire/curso-component.blade.php (la vista)
|
*/

namespace App\Livewire;

// Clase base de Livewire: todos los componentes deben extender de Component
use Livewire\Component;

// Modelo Eloquent para interactuar con la tabla de cursos
use App\Models\Curso;

/*
|--------------------------------------------------------------------------
| Clase CursoComponent
|--------------------------------------------------------------------------
| Componente Livewire que maneja el CRUD de cursos.
| A diferencia del controlador tradicional (Modulo 15), toda la logica
| CRUD esta contenida en una sola clase.
|
| PROPIEDADES PUBLICAS:
| Las propiedades publicas del componente son REACTIVAS. Esto significa
| que cuando cambian (por ejemplo, desde un input con wire:model),
| Livewire automaticamente re-renderiza la vista.
|
| Es como tener "variables de estado" similares a React/Vue,
| pero escritas en PHP puro.
*/
class CursoComponent extends Component
{
    /*
    |----------------------------------------------------------------------
    | Propiedades publicas (reactivas)
    |----------------------------------------------------------------------
    | Cada propiedad publica es accesible desde la vista Blade y
    | se puede vincular a inputs con wire:model="propiedad".
    |
    | $view: controla que sub-vista se muestra (create, edit, list, etc.)
    | Las demas propiedades corresponden a los campos del formulario.
    |
    | IMPORTANTE: Las propiedades publicas se serializan en cada peticion
    | AJAX. Evita poner datos sensibles o muy grandes como propiedades
    | publicas. Usa propiedades protected o private para datos internos.
    */
    public $view = 'create';

    // Propiedades del formulario: cada una se vincula con wire:model="nombre"
    // en la vista. Cuando el usuario escribe, el valor se sincroniza
    // automaticamente con el servidor via AJAX.
    public $nombre, $objetivo, $modalidad, $cupo, $periodo, $horario, $dias, $salon;


    /*
    |----------------------------------------------------------------------
    | render() - Renderiza la vista del componente
    |----------------------------------------------------------------------
    | Se ejecuta automaticamente cada vez que:
    |   - El componente se carga por primera vez
    |   - Una propiedad publica cambia (via wire:model o asignacion)
    |   - Se llama a un metodo del componente (via wire:click, etc.)
    |
    | Retorna la vista Blade asociada al componente.
    | La vista tiene acceso a TODAS las propiedades publicas del componente
    | automaticamente (no necesita compact() ni paso explicito de datos).
    |
    | DIFERENCIA CON CONTROLADOR TRADICIONAL:
    |   Tradicional: return view('vista', compact('datos'));  // una sola vez
    |   Livewire:    return view('livewire.vista');           // se re-ejecuta constantemente
    */
    public function render()
    {
        // Retorna la vista principal del componente
        // Esta vista incluye sub-vistas segun el valor de $this->view
        return view('livewire.curso-component');
    }

    /*
    |----------------------------------------------------------------------
    | store() - Guardar un nuevo curso en la base de datos
    |----------------------------------------------------------------------
    | Este metodo se invoca desde la vista con: wire:click="store"
    | Es el equivalente a CursoController@store del Modulo 15,
    | pero sin necesidad de Request, ni rutas POST, ni redireccion.
    |
    | FLUJO:
    |   1. Usuario llena los inputs (vinculados con wire:model)
    |   2. Usuario hace clic en el boton "Agregar" (wire:click="store")
    |   3. Livewire envia los datos al servidor via AJAX
    |   4. Se ejecuta este metodo en el servidor
    |   5. Se validan los datos con $this->validate()
    |   6. Se crea el registro con Curso::create()
    |   7. Livewire re-renderiza el componente automaticamente
    |
    | VALIDACION EN LIVEWIRE:
    | $this->validate() funciona igual que en un controlador.
    | Si la validacion falla, Livewire muestra los errores
    | automaticamente en los @error('campo') de la vista.
    | No hay redireccion: los errores aparecen en tiempo real.
    |
    | COMPARACION CON MODULO 15:
    |   Modulo 15 (Tradicional):
    |     - $this->validate($request, [...]) en el controlador
    |     - Fallo -> redireccion al formulario con errores
    |     - Exito -> redirect(route('index'))->with('mensaje', '...')
    |
    |   Modulo 16 (Livewire):
    |     - $this->validate([...]) en el componente
    |     - Fallo -> errores aparecen inmediatamente (sin recargar)
    |     - Exito -> se queda en la misma pagina, se actualiza la lista
    |
    */
    public function store(){
        // Validar: las mismas reglas que en el controlador tradicional.
        // Si falla, Livewire maneja los errores automaticamente.
        // En la vista, @error('nombre') muestra el mensaje de error.
        $this->validate([
            'nombre' => 'required',
            'objetivo' => 'required',
            'modalidad' => 'required',
            'cupo' => 'required',
            'periodo' => 'required',
            'horario' => 'required',
            'dias' => 'required',
            'salon' => 'required',
        ]);

        // Crear el curso usando Mass Assignment (Eloquent)
        // Las propiedades del componente ($this->nombre, etc.)
        // ya tienen los valores del formulario gracias a wire:model
        Curso::create([
            'nombre' => $this->nombre,
            'objetivo' => $this->objetivo,
            'modalidad' => $this->modalidad,
            'cupo' => $this->cupo,
            'periodo' => $this->periodo,
            'horario' => $this->horario,
            'dias' => $this->dias,
            'salon' => $this->salon,
        ]);

        // NOTA: Despues de crear, podriamos:
        // - Limpiar el formulario: $this->reset(['nombre', 'objetivo', ...])
        // - Cambiar la vista: $this->view = 'list'
        // - Emitir un evento: $this->dispatch('cursoCreado')
        // - Mostrar un mensaje flash: session()->flash('mensaje', 'Curso creado')
    }

    /*
    |----------------------------------------------------------------------
    | METODOS ADICIONALES QUE SE PODRIAN AGREGAR
    |----------------------------------------------------------------------
    |
    | // Editar: cargar datos de un curso en las propiedades
    | public function edit($id) {
    |     $curso = Curso::find($id);
    |     $this->nombre = $curso->nombre;
    |     $this->objetivo = $curso->objetivo;
    |     // ... etc
    |     $this->view = 'edit';
    | }
    |
    | // Actualizar: guardar cambios
    | public function update() {
    |     $this->validate([...]);
    |     $curso = Curso::find($this->cursoId);
    |     $curso->update([...]);
    |     $this->view = 'list';
    | }
    |
    | // Eliminar: borrar un curso
    | public function destroy($id) {
    |     Curso::destroy($id);
    | }
    |
    | // Limpiar formulario
    | public function resetForm() {
    |     $this->reset(['nombre', 'objetivo', 'modalidad', ...]);
    | }
    |
    | // Hook: se ejecuta cuando la propiedad 'nombre' cambia
    | public function updatedNombre($value) {
    |     // Validacion en tiempo real solo para este campo
    |     $this->validateOnly('nombre');
    | }
    |
    */
}

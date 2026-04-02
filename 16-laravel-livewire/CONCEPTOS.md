# Modulo 16: Laravel Livewire - Conceptos Fundamentales

## Tabla de Contenidos
1. [Que es Livewire y por que existe](#1-que-es-livewire-y-por-que-existe)
2. [Como funciona Livewire internamente](#2-como-funciona-livewire-internamente)
3. [Anatomia de un componente](#3-anatomia-de-un-componente)
4. [Propiedades y Data Binding](#4-propiedades-y-data-binding)
5. [Acciones y eventos](#5-acciones-y-eventos)
6. [Ciclo de vida del componente](#6-ciclo-de-vida-del-componente)
7. [Validacion en tiempo real](#7-validacion-en-tiempo-real)
8. [CRUD Tradicional vs CRUD Livewire](#8-crud-tradicional-vs-crud-livewire)
9. [Cuando usar Livewire vs JavaScript](#9-cuando-usar-livewire-vs-javascript)
10. [Errores comunes](#10-errores-comunes)
11. [Ejercicios de practica](#11-ejercicios-de-practica)

---

## 1. Que es Livewire y por que existe

### El problema: "JavaScript fatigue" (fatiga de JavaScript)
Para crear interfaces web interactivas y reactivas, tradicionalmente se necesitan frameworks de JavaScript como React, Vue o Angular. Esto implica:

- Aprender un lenguaje/framework adicional (JavaScript + React/Vue)
- Mantener DOS aplicaciones: un API en Laravel + un frontend en React/Vue
- Manejar la comunicacion entre ambos (REST API, JSON, tokens)
- Configurar herramientas como Webpack, Vite, Node.js
- Duplicar logica de validacion (servidor + cliente)

### La solucion: Livewire
Livewire permite crear interfaces reactivas **usando solo PHP y Blade**. No necesitas escribir JavaScript.

```
SIN LIVEWIRE (Traditional SPA):
  Laravel (API)  +  React/Vue (Frontend)  +  REST API  +  Node.js

CON LIVEWIRE:
  Laravel + Blade + Livewire = Interfaz reactiva sin JavaScript
```

### Que NO es Livewire
- No es un reemplazo de React/Vue para aplicaciones complejas de tiempo real
- No es adecuado para interfaces con miles de actualizaciones por segundo
- No funciona sin conexion a internet (necesita AJAX constante)

### Que SI es Livewire
- Una herramienta para desarrolladores PHP que quieren interactividad sin JavaScript
- Ideal para CRUDs, formularios, tablas con filtros, paginacion en tiempo real
- Perfecto para aplicaciones internas, paneles de administracion, dashboards

---

## 2. Como funciona Livewire internamente

### El ciclo de comunicacion

```
COMO FUNCIONA LIVEWIRE BAJO EL CAPO

  NAVEGADOR (Cliente)                    SERVIDOR (Laravel)
  +------------------------+             +------------------------+
  |                        |             |                        |
  | 1. Carga inicial:      |   HTTP GET  |                        |
  |    El usuario visita   | ----------> | 2. Laravel renderiza   |
  |    la pagina           |             |    el componente       |
  |                        |             |    Livewire por        |
  |                        |   HTML      |    primera vez         |
  | 3. El navegador muestra| <---------- |                        |
  |    el HTML con el JS   |             |                        |
  |    de Livewire         |             |                        |
  |                        |             |                        |
  | 4. El usuario          |             |                        |
  |    interactua:         |             |                        |
  |    escribe en input    |             |                        |
  |    o hace clic         |             |                        |
  |                        |   AJAX      |                        |
  | 5. Livewire.js envia   | ----------> | 6. El servidor:        |
  |    los datos al        |   (JSON)    |    - Rehidrata el      |
  |    servidor via AJAX   |             |      componente        |
  |                        |             |    - Actualiza la      |
  |                        |             |      propiedad         |
  |                        |             |    - Ejecuta el metodo |
  |                        |             |    - Re-renderiza      |
  |                        |   HTML      |      la vista          |
  | 7. Livewire.js recibe  | <---------- |                        |
  |    el HTML nuevo       |   (diff)    |                        |
  |                        |             |                        |
  | 8. DOM Diffing:        |             |                        |
  |    Solo actualiza las  |             |                        |
  |    partes del HTML     |             |                        |
  |    que cambiaron       |             |                        |
  |    (como React)        |             |                        |
  +------------------------+             +------------------------+
```

### Conceptos clave

**Hidratacion (Hydration):** El proceso de reconstruir el estado del componente PHP a partir de los datos enviados desde el navegador. Cada peticion AJAX incluye el estado completo del componente.

**Deshidratacion (Dehydration):** El proceso inverso: convertir el estado del componente PHP en datos que el navegador puede almacenar.

**DOM Diffing:** Cuando el servidor retorna nuevo HTML, Livewire.js compara el HTML anterior con el nuevo y solo modifica los elementos que cambiaron. Similar a como funciona el Virtual DOM de React.

---

## 3. Anatomia de un componente

### Dos partes: Clase PHP + Vista Blade

```
COMPONENTE LIVEWIRE = CLASE PHP + VISTA BLADE

app/Livewire/CursoComponent.php              (Logica)
+------------------------------------------+
| class CursoComponent extends Component   |
| {                                        |
|     public $nombre;        // Estado     |
|     public $objetivo;      // (datos)    |
|                                          |
|     public function store() // Acciones  |
|     {                                    |
|         // crear curso...                |
|     }                                    |
|                                          |
|     public function render() // Vista    |
|     {                                    |
|         return view('livewire.curso');    |
|     }                                    |
| }                                        |
+------------------------------------------+
           |
           | Propiedades publicas disponibles automaticamente
           v
resources/views/livewire/curso-component.blade.php  (Presentacion)
+------------------------------------------+
| <div>                                    |
|     <input wire:model="nombre">          |
|     <input wire:model="objetivo">        |
|     <button wire:click="store">Guardar   |
| </div>                                   |
+------------------------------------------+
```

### Crear un componente

```bash
php artisan make:livewire CursoComponent
```

Esto crea:
- `app/Livewire/CursoComponent.php` - la clase del componente
- `resources/views/livewire/curso-component.blade.php` - la vista

### Convenciones de nombres

| Clase PHP | Vista Blade | Uso en plantilla |
|-----------|------------|------------------|
| `CursoComponent` | `curso-component.blade.php` | `@livewire('curso-component')` |
| `ContactForm` | `contact-form.blade.php` | `@livewire('contact-form')` |
| `Admin\UserList` | `admin/user-list.blade.php` | `@livewire('admin.user-list')` |

---

## 4. Propiedades y Data Binding

### Propiedades publicas = estado reactivo
Las propiedades publicas del componente son automaticamente accesibles en la vista y se sincronizan con el navegador.

```php
// En el componente PHP:
class CursoComponent extends Component
{
    public $nombre = '';      // Disponible como $nombre en la vista
    public $cupo = 30;        // Se puede inicializar con un valor
    public $cursos;           // Se puede asignar en mount()
}
```

```blade
{{-- En la vista Blade: --}}
<input wire:model="nombre">       {{-- Vinculado a $this->nombre --}}
<p>Cupo: {{ $cupo }}</p>           {{-- Muestra el valor --}}
```

### wire:model - Vinculacion bidireccional

```
wire:model="nombre"

   INPUT HTML                      PROPIEDAD PHP
   +------------+    escribe    +---------------+
   | [Laravel  ]| -----------> | $nombre =     |
   |            |               | "Laravel"     |
   +------------+    muestra    +---------------+
                  <-----------

Cuando el usuario escribe "Laravel" en el input,
$this->nombre se actualiza a "Laravel" en el servidor.
Si cambias $this->nombre en PHP, el input se actualiza.
```

### Variantes de wire:model

```blade
{{-- Livewire 3 --}}
<input wire:model="nombre">              {{-- Se sincroniza al enviar/perder foco --}}
<input wire:model.live="nombre">          {{-- Se sincroniza en CADA tecla --}}
<input wire:model.blur="nombre">          {{-- Se sincroniza al perder foco --}}
<input wire:model.live.debounce.300ms="nombre">  {{-- Espera 300ms despues de la ultima tecla --}}

{{-- Livewire 2 (diferente sintaxis) --}}
<input wire:model="nombre">              {{-- Se sincroniza en cada tecla --}}
<input wire:model.lazy="nombre">          {{-- Se sincroniza al perder foco --}}
<input wire:model.debounce.300ms="nombre"> {{-- Espera 300ms --}}
```

### Tipos de propiedades soportadas

```php
public string $nombre = '';          // Strings
public int $cupo = 0;               // Numeros
public bool $activo = true;          // Booleanos
public array $items = [];            // Arrays
public $curso;                       // Modelos Eloquent (con cuidado)
// NO soportado: objetos complejos, closures, resources
```

---

## 5. Acciones y eventos

### wire:click - Ejecutar metodos al hacer clic

```blade
{{-- En la vista: --}}
<button wire:click="store">Guardar</button>
<button wire:click="edit({{ $curso->id }})">Editar</button>
<button wire:click="destroy({{ $id }})">Eliminar</button>
```

```php
// En el componente PHP:
public function store() {
    // Se ejecuta cuando hacen clic en "Guardar"
    Curso::create([...]);
}

public function edit($id) {
    // Se ejecuta cuando hacen clic en "Editar"
    $curso = Curso::find($id);
    $this->nombre = $curso->nombre;
}

public function destroy($id) {
    // Se ejecuta cuando hacen clic en "Eliminar"
    Curso::destroy($id);
}
```

### wire:submit - Manejar envio de formularios

```blade
{{-- Mejor practica para formularios: --}}
<form wire:submit="store">
    <input wire:model="nombre">
    <input wire:model="objetivo">
    <button type="submit">Guardar</button>
</form>
```

### Otras directivas de eventos

```blade
wire:click="metodo"              {{-- Al hacer clic --}}
wire:submit="metodo"             {{-- Al enviar formulario --}}
wire:keydown="metodo"            {{-- Al presionar tecla --}}
wire:keydown.enter="metodo"      {{-- Al presionar Enter --}}
wire:mouseenter="metodo"         {{-- Al pasar el mouse --}}
wire:change="metodo"             {{-- Al cambiar un select/checkbox --}}

{{-- Prevenir comportamiento por defecto: --}}
wire:submit.prevent="metodo"     {{-- Previene el submit HTML nativo --}}

{{-- Confirmacion antes de ejecutar: --}}
wire:click="destroy({{ $id }})"
wire:confirm="Seguro que deseas eliminar?"
```

### Comunicacion entre componentes (Events)

```php
// Emitir evento desde un componente:
$this->dispatch('cursoCreado');

// Escuchar evento en otro componente:
#[On('cursoCreado')]
public function actualizarLista() {
    // Re-cargar datos...
}
```

---

## 6. Ciclo de vida del componente

### Hooks del ciclo de vida (en orden de ejecucion)

```
CICLO DE VIDA DE UN COMPONENTE LIVEWIRE

  CARGA INICIAL (primera vez):
  +--------------------------------------------------+
  | 1. boot()       Se ejecuta en CADA peticion       |
  |                 (antes de mount o hydrate)         |
  |                                                    |
  | 2. mount()      Solo la primera vez que se carga   |
  |                 Equivale al constructor             |
  |                 Ideal para inicializar datos        |
  |                                                    |
  | 3. render()     Genera el HTML del componente      |
  +--------------------------------------------------+

  PETICIONES SIGUIENTES (cada interaccion AJAX):
  +--------------------------------------------------+
  | 1. boot()       Se ejecuta en cada peticion        |
  |                                                    |
  | 2. hydrate()    Rehidrata el componente            |
  |                 (reconstruye el estado)             |
  |                                                    |
  | 3. updating*()  ANTES de actualizar una propiedad  |
  |    updatingNombre($value)                          |
  |                                                    |
  | 4. updated*()   DESPUES de actualizar una propiedad|
  |    updatedNombre($value)                           |
  |                                                    |
  | 5. [metodo]     Se ejecuta el metodo invocado      |
  |                 (store(), edit(), destroy()...)     |
  |                                                    |
  | 6. render()     Re-genera el HTML                  |
  |                                                    |
  | 7. dehydrate()  Prepara el estado para enviarlo    |
  |                 al navegador                       |
  +--------------------------------------------------+
```

### Ejemplos de hooks

```php
class CursoComponent extends Component
{
    public $nombre;
    public $cursos;

    // mount(): se ejecuta UNA sola vez al crear el componente
    // Ideal para cargar datos iniciales
    public function mount()
    {
        $this->cursos = Curso::all();
        $this->nombre = ''; // valor inicial
    }

    // updated{Propiedad}(): se ejecuta cuando la propiedad cambia
    // El nombre del metodo es: updated + NombrePropiedad (PascalCase)
    public function updatedNombre($value)
    {
        // Se ejecuta cada vez que $nombre cambia
        // Ideal para validacion en tiempo real
        $this->validateOnly('nombre');
    }

    // render(): se ejecuta en CADA peticion
    public function render()
    {
        return view('livewire.curso-component');
    }
}
```

---

## 7. Validacion en tiempo real

### Validacion basica (al enviar)

```php
class CursoComponent extends Component
{
    public $nombre, $email, $cupo;

    // Opcion 1: reglas como propiedad
    protected $rules = [
        'nombre' => 'required|min:3',
        'email' => 'required|email',
        'cupo' => 'required|numeric|min:1',
    ];

    // Mensajes personalizados (opcional)
    protected $messages = [
        'nombre.required' => 'El nombre es obligatorio',
        'nombre.min' => 'El nombre debe tener al menos 3 caracteres',
        'cupo.numeric' => 'El cupo debe ser un numero',
    ];

    public function store()
    {
        $this->validate(); // Valida todas las reglas
        Curso::create([...]);
    }
}
```

### Validacion en tiempo real (mientras escribe)

```php
class CursoComponent extends Component
{
    public $nombre, $email;

    protected $rules = [
        'nombre' => 'required|min:3',
        'email' => 'required|email',
    ];

    // Se ejecuta cada vez que $nombre cambia (cada tecla con wire:model.live)
    public function updatedNombre()
    {
        $this->validateOnly('nombre');
        // Solo valida el campo 'nombre', no todos los campos
    }

    public function updatedEmail()
    {
        $this->validateOnly('email');
    }
}
```

```blade
{{-- En la vista: --}}
<input wire:model.live="nombre" class="form-control @error('nombre') is-invalid @enderror">
@error('nombre')
    <span class="text-danger">{{ $message }}</span>
@enderror
{{-- El error aparece/desaparece mientras el usuario escribe! --}}
```

### Comparacion de validacion

| Aspecto | Modulo 15 (Tradicional) | Modulo 16 (Livewire) |
|---------|------------------------|---------------------|
| Cuando ocurre | Al enviar el formulario | En tiempo real o al enviar |
| Si falla | Recarga la pagina con errores | Muestra errores sin recargar |
| Experiencia | El usuario debe enviar para ver errores | El usuario ve errores mientras escribe |
| old() | Necesario para conservar datos | No necesario (Livewire conserva datos) |

---

## 8. CRUD Tradicional vs CRUD Livewire

### Comparacion lado a lado

#### Listado de cursos (READ)

```php
// MODULO 15 - Controlador tradicional
// CursoController.php
public function index()
{
    $cursos = Curso::orderBy('id')->paginate(4);
    return view('principal', compact('cursos'));
}

// Ruta:
Route::get('/', [CursoController::class, 'index']);
```

```php
// MODULO 16 - Componente Livewire
// CursoComponent.php
public function render()
{
    $cursos = Curso::orderBy('id')->paginate(4);
    return view('livewire.curso-component', compact('cursos'));
}

// Ruta:
Route::get('/', function () { return view('principal'); });
```

#### Crear un curso (CREATE)

```php
// MODULO 15 - Dos metodos + dos rutas
public function create()
{
    return view('agregar');              // GET /agregar
}

public function store(Request $request)  // POST /agregar
{
    $this->validate($request, [...]);
    $curso = new Curso;
    $curso->nombre = $request->nombre;
    $curso->save();
    return redirect(route('index'))->with('mensaje', 'Creado');
}
```

```php
// MODULO 16 - Un metodo, sin rutas adicionales
public function store()                  // wire:click="store" (AJAX)
{
    $this->validate([...]);
    Curso::create([
        'nombre' => $this->nombre,       // Datos ya estan en las propiedades
        'objetivo' => $this->objetivo,
    ]);
    // No hay redireccion, la pagina se actualiza sola
}
```

#### Vista del formulario

```blade
{{-- MODULO 15 - Formulario tradicional --}}
<form action="{{ route('store') }}" method="POST">
    @csrf
    <input type="text" name="nombre" value="{{ old('nombre') }}">
    @error('nombre') <span>{{ $message }}</span> @enderror
    <button type="submit">Guardar</button>
</form>
```

```blade
{{-- MODULO 16 - Formulario Livewire --}}
<form wire:submit="store">
    <input type="text" wire:model="nombre">
    @error('nombre') <span>{{ $message }}</span> @enderror
    <button type="submit">Guardar</button>
</form>
{{-- Sin action, sin method, sin @csrf, sin old() --}}
```

#### Eliminar un curso (DELETE)

```blade
{{-- MODULO 15 - Formulario con @method('DELETE') --}}
<form action="{{ route('destroy', $curso->id) }}" method="POST">
    @csrf
    {{ method_field('delete') }}
    <button type="submit" onclick="return confirm('Seguro?')">Eliminar</button>
</form>
```

```blade
{{-- MODULO 16 - Un simple boton --}}
<button wire:click="destroy({{ $curso->id }})"
        wire:confirm="Seguro que deseas eliminar?">
    Eliminar
</button>
```

### Resumen de diferencias

| Aspecto | Modulo 15 (Tradicional) | Modulo 16 (Livewire) |
|---------|------------------------|---------------------|
| **Rutas** | 7+ rutas en web.php | 1 ruta |
| **Archivos** | Controlador + vistas separadas | 1 componente + 1 vista |
| **Formularios** | action, method, @csrf | wire:model, wire:click |
| **Validacion** | Redireccion con errores | Errores en tiempo real |
| **Navegacion** | Recarga completa por accion | Sin recarga (AJAX) |
| **JavaScript** | Necesario para interactividad | No necesario |
| **Complejidad** | Mas archivos, mas explicito | Menos archivos, mas magico |
| **Rendimiento** | Una peticion HTTP por accion | Multiples AJAX pequenos |
| **Curva de aprendizaje** | Mas familiar (HTTP clasico) | Nuevos conceptos (reactivo) |

---

## 9. Cuando usar Livewire vs JavaScript

### Usa Livewire cuando:
- Tu equipo es principalmente de PHP/Laravel
- El proyecto es un CRUD, panel de administracion o dashboard
- Necesitas formularios interactivos con validacion en tiempo real
- Quieres tablas con filtros, busqueda y paginacion dinamica
- No quieres mantener un frontend separado (React/Vue)
- La latencia de red es aceptable (cada interaccion va al servidor)

### Usa JavaScript (React/Vue/Alpine.js) cuando:
- Necesitas interactividad instantanea sin latencia
- La aplicacion debe funcionar offline
- Tienes animaciones complejas o interacciones de arrastrar y soltar
- Necesitas actualizaciones en tiempo real (WebSockets, chat)
- El equipo tiene experiencia en JavaScript
- La interfaz es muy compleja (editor de imagenes, IDE web, juegos)

### La opcion intermedia: Alpine.js + Livewire
Alpine.js es un framework JavaScript minimalista que se integra perfectamente con Livewire para manejar interactividad del lado del cliente:

```blade
{{-- Alpine.js para cosas del cliente (sin servidor) --}}
<div x-data="{ open: false }">
    <button @click="open = !open">Toggle</button>
    <div x-show="open">Contenido</div>
</div>

{{-- Livewire para cosas del servidor (base de datos) --}}
<button wire:click="store">Guardar en BD</button>
```

### Tabla comparativa

| Herramienta | Donde se ejecuta | Mejor para |
|-------------|-------------------|-----------|
| **Livewire** | Servidor (PHP) | CRUD, formularios, tablas |
| **Alpine.js** | Cliente (JS) | Dropdowns, modales, tabs, toggles |
| **Vue/React** | Cliente (JS) | SPAs complejas, apps en tiempo real |
| **Livewire + Alpine** | Ambos | Lo mejor de ambos mundos |

---

## 10. Errores comunes

### Error: "Unable to find component"

```php
// PROBLEMA: el nombre del componente no coincide
@livewire('CursoComponent')  // MAL - PascalCase
@livewire('curso-component') // BIEN - kebab-case
```

### Error: La vista debe tener un solo elemento raiz

```blade
{{-- MAL: dos elementos raiz --}}
<h1>Titulo</h1>
<div>Contenido</div>

{{-- BIEN: un solo elemento raiz --}}
<div>
    <h1>Titulo</h1>
    <div>Contenido</div>
</div>
```

### Error: "Add [campo] to fillable property"

```php
// PROBLEMA: el modelo no tiene $fillable
// Curso::create([...]) falla

// SOLUCION: agregar en el modelo
protected $fillable = ['nombre', 'objetivo', 'modalidad', ...];
```

### Error: wire:model no actualiza la propiedad

```php
// PROBLEMA: la propiedad no es publica
private $nombre;    // MAL - Livewire no puede acceder
public $nombre;     // BIEN

// PROBLEMA: typo en wire:model
wire:model="modlidad"  // MAL - falta la 'a'
wire:model="modalidad"  // BIEN
```

### Error: @livewireStyles y @livewireScripts faltantes

```blade
{{-- Si el componente no responde a nada, verificar que el layout tenga: --}}
<head>
    @livewireStyles    {{-- En el head --}}
</head>
<body>
    ...
    @livewireScripts   {{-- Antes de </body> --}}
</body>
```

### Error: El componente no se actualiza despues de crear/eliminar

```php
// PROBLEMA: render() no re-consulta los datos
public $cursos;

public function mount() {
    $this->cursos = Curso::all(); // Solo se carga una vez
}

public function render() {
    return view('livewire.componente'); // Usa datos viejos
}

// SOLUCION: consultar en render()
public function render() {
    return view('livewire.componente', [
        'cursos' => Curso::all()  // Se consulta en cada render
    ]);
}
```

### Error: El formulario hace submit HTTP en vez de usar Livewire

```blade
{{-- PROBLEMA: el form tiene action y type="submit" pero no wire:submit --}}
<form action="/ruta" method="POST">
    <button type="submit">Enviar</button>  {{-- Esto recarga la pagina --}}
</form>

{{-- SOLUCION: usar wire:submit y quitar action --}}
<form wire:submit="store">
    <button type="submit">Enviar</button>  {{-- Ahora usa Livewire --}}
</form>

{{-- O usar wire:click con type="button" --}}
<button type="button" wire:click="store">Enviar</button>
```

---

## 11. Ejercicios de practica

### Ejercicio 1: Completar el CRUD
El componente actual solo tiene `store()`. Agrega los metodos faltantes:

1. Modificar `render()` para que liste los cursos:
```php
public function render()
{
    return view('livewire.curso-component', [
        'cursos' => Curso::orderBy('id')->get()
    ]);
}
```

2. Crear un metodo `edit($id)` que cargue los datos en las propiedades
3. Crear un metodo `update()` que actualice el registro
4. Crear un metodo `destroy($id)` que elimine el registro
5. Crear las sub-vistas correspondientes

### Ejercicio 2: Agregar validacion en tiempo real
Implementa validacion mientras el usuario escribe:

```php
protected $rules = [
    'nombre' => 'required|min:3',
    'cupo' => 'required|numeric|min:1|max:100',
    'email' => 'required|email',
];

public function updatedNombre() { $this->validateOnly('nombre'); }
public function updatedCupo() { $this->validateOnly('cupo'); }
```

Y usa `wire:model.live` en los inputs.

### Ejercicio 3: Agregar paginacion
Livewire tiene su propio trait de paginacion:

```php
use Livewire\WithPagination;

class CursoComponent extends Component
{
    use WithPagination;

    public function render()
    {
        return view('livewire.curso-component', [
            'cursos' => Curso::paginate(5)
        ]);
    }
}
```

### Ejercicio 4: Agregar busqueda en tiempo real
```php
public $buscar = '';

public function render()
{
    return view('livewire.curso-component', [
        'cursos' => Curso::where('nombre', 'like', "%{$this->buscar}%")
                        ->orderBy('id')
                        ->paginate(5)
    ]);
}
```

```blade
<input wire:model.live.debounce.300ms="buscar" placeholder="Buscar curso...">
```

### Ejercicio 5: Agregar mensajes flash
```php
public function store()
{
    $this->validate([...]);
    Curso::create([...]);
    $this->reset(['nombre', 'objetivo', ...]);  // Limpiar formulario
    session()->flash('mensaje', 'Curso creado exitosamente');
}
```

```blade
@if (session()->has('mensaje'))
    <div class="alert alert-success">{{ session('mensaje') }}</div>
@endif
```

### Ejercicio 6: Agregar confirmacion de eliminacion
```blade
{{-- Livewire 3: --}}
<button wire:click="destroy({{ $curso->id }})"
        wire:confirm="Estas seguro de eliminar este curso?">
    Eliminar
</button>
```

### Ejercicio 7: Comparar rendimiento
1. Abre las herramientas de desarrollo del navegador (F12 > Red/Network)
2. En el Modulo 15: navega entre paginas y observa las peticiones HTTP completas
3. En el Modulo 16: interactua con el componente y observa las peticiones AJAX
4. Compara: tamano de las respuestas, tiempo de carga, numero de peticiones

### Ejercicio 8: Convertir el formulario de contacto
Toma el formulario de contacto del Modulo 15 y convierte lo a un componente Livewire:
1. `php artisan make:livewire ContactoComponent`
2. Mover la logica de `MensajesController@store` al componente
3. Usar `wire:model` en los inputs
4. Agregar validacion en tiempo real
5. Mostrar un mensaje de exito sin recargar la pagina

### Ejercicio 9: Corregir el bug del typo
En `form.blade.php` hay un typo: `wire:model="modlidad"` deberia ser `wire:model="modalidad"`. Corrigelo y verifica que la validacion funcione para ese campo.

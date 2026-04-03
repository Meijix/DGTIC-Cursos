# Cheatsheet — Modulo 16: Laravel Livewire 3

## Crear componente

```bash
php artisan make:livewire CursoComponent
# Crea: app/Livewire/CursoComponent.php + resources/views/livewire/curso-component.blade.php
```

## Estructura basica

```php
class CursoComponent extends Component {
    public string $nombre = '';       // Propiedad reactiva (debe ser public)
    public function store() { ... }   // Accion invocable desde la vista
    public function render() { return view('livewire.curso-component'); }
}
```

## Referencia rapida — Directivas wire:

| Directiva | Efecto |
|-----------|--------|
| `wire:model="nombre"` | Binding al enviar/perder foco |
| `wire:model.live="nombre"` | Binding en cada tecla |
| `wire:model.blur="nombre"` | Binding al perder foco |
| `wire:model.live.debounce.300ms="nombre"` | Binding con retardo 300ms |
| `wire:click="store"` | Ejecutar metodo al clic |
| `wire:click="edit({{ $id }})"` | Clic con parametro |
| `wire:submit="store"` | Envio de formulario (reemplaza action+method+@csrf) |
| `wire:confirm="Seguro?"` | Confirmacion nativa antes de ejecutar |
| `wire:keydown.enter="buscar"` | Al presionar Enter |

## Ciclo de vida (hooks)

| Hook | Cuando | Uso tipico |
|------|--------|------------|
| `mount()` | Solo primera carga | Inicializar datos |
| `updatedNombre($v)` | Despues de que `$nombre` cambie | `$this->validateOnly('nombre')` |
| `render()` | Cada peticion | Devolver vista (consultar datos aqui, no en mount) |

## Validacion

```php
protected $rules = ['nombre' => 'required|min:3', 'email' => 'required|email'];
protected $messages = ['nombre.required' => 'El nombre es obligatorio'];

public function store() { $this->validate(); Curso::create([...]); }
public function updatedNombre() { $this->validateOnly('nombre'); } // Tiempo real
```

```blade
<input wire:model.live="nombre" class="@error('nombre') border-red-500 @enderror">
@error('nombre') <span class="text-red-500 text-sm">{{ $message }}</span> @enderror
```

## Formulario tipico

```blade
<form wire:submit="store">
    <input type="text" wire:model="nombre">
    @error('nombre') <span>{{ $message }}</span> @enderror
    <button type="submit">Guardar</button>
</form>
{{-- Sin action, sin method, sin @csrf, sin old() --}}
```

## Eventos entre componentes

```php
$this->dispatch('cursoCreado');                          // Emitir
#[On('cursoCreado')] public function actualizar() {}     // Escuchar
```

## Layout (obligatorio)

```blade
<head> @livewireStyles </head>
<body> ... @livewireScripts </body>
```

## Convenciones: `CursoComponent` -> vista `curso-component.blade.php` -> `@livewire('curso-component')`

## Tailwind CSS frecuente

`p-4` `px-6` `m-4` `mx-auto` `text-red-500` `text-sm` `bg-blue-500` `rounded-lg` `shadow-md` `flex` `grid` `gap-4` `border` `hover:bg-blue-600`

## Errores comunes

| Error | Solucion |
|-------|----------|
| "Unable to find component" | Usar kebab-case: `@livewire('curso-component')` |
| Vista con multiples raices | Envolver todo en un solo `<div>` |
| `wire:model` no actualiza | Propiedad debe ser `public`, sin typos |
| Formulario recarga la pagina | Quitar `action` y usar `wire:submit` |
| Datos viejos al crear/eliminar | Mover consulta BD a `render()`, no en `mount()` |
| "Add [campo] to fillable" | Agregar `protected $fillable = [...]` al modelo |

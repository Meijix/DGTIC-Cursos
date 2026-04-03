# Cheatsheet — Laravel CRUD

## Comandos Artisan esenciales

| Comando                                     | Descripcion                              |
|---------------------------------------------|------------------------------------------|
| `php artisan serve`                         | Iniciar servidor en localhost:8000       |
| `php artisan make:model Curso -mcr`        | Modelo + migracion + controlador resource|
| `php artisan make:controller NombreController --resource` | Controlador con 7 metodos CRUD |
| `php artisan make:migration create_cursos_table` | Crear migracion                    |
| `php artisan migrate`                       | Ejecutar migraciones pendientes          |
| `php artisan migrate:rollback`              | Revertir ultima migracion               |
| `php artisan migrate:fresh`                 | Borrar todo y re-ejecutar migraciones    |
| `php artisan route:list`                    | Ver todas las rutas registradas          |
| `php artisan make:mail NombreMail`          | Crear clase Mailable                     |
| `php artisan tinker`                        | Consola interactiva PHP/Eloquent         |
| `php artisan cache:clear`                   | Limpiar cache                            |
| `php artisan config:clear`                  | Limpiar cache de configuracion           |
| `composer dump-autoload`                    | Regenerar autoload (si "Class not found")|

## Rutas (routes/web.php)

```php
// Ruta simple con closure
Route::get('/about', function () {
    return view('about');
});

// Ruta con controlador (lo mas comun)
Route::get('/', [CursoController::class, 'index'])->name('index');

// Ruta con parametro
Route::get('/editar/{id}', [CursoController::class, 'edit'])->name('edit');

// RESOURCE: genera las 7 rutas CRUD de un solo golpe
Route::resource('cursos', CursoController::class);
```

## Las 7 rutas de Route::resource

| Verbo     | URI                  | Metodo    | Descripcion             |
|-----------|----------------------|-----------|-------------------------|
| GET       | `/cursos`            | index     | Listar todos            |
| GET       | `/cursos/create`     | create    | Formulario para crear   |
| POST      | `/cursos`            | store     | Guardar nuevo registro  |
| GET       | `/cursos/{id}`       | show      | Ver un registro         |
| GET       | `/cursos/{id}/edit`  | edit      | Formulario para editar  |
| PUT/PATCH | `/cursos/{id}`       | update    | Actualizar registro     |
| DELETE    | `/cursos/{id}`       | destroy   | Eliminar registro       |

## Controlador — estructura CRUD

```php
class CursoController extends Controller
{
    public function index() {
        $cursos = Curso::orderBy('id')->paginate(4);
        return view('principal', compact('cursos'));
    }

    public function create() {
        return view('agregar');
    }

    public function store(Request $request) {
        $this->validate($request, [
            'nombre' => 'required',
            'cupo'   => 'required|numeric|min:1',
        ]);
        $curso = new Curso;
        $curso->nombre = $request->nombre;
        $curso->save();
        return redirect(route('index'))->with('mensaje', 'Creado');
    }

    public function edit(string $id) {
        $curso = Curso::find($id);
        return view('editar', compact('curso'));
    }

    public function update(Request $request, string $id) {
        $this->validate($request, ['nombre' => 'required']);
        $curso = Curso::find($id);
        $curso->nombre = $request->nombre;
        $curso->save();
        return redirect(route('index'))->with('mensaje', 'Actualizado');
    }

    public function destroy(string $id) {
        Curso::destroy($id);
        return redirect(route('index'))->with('mensaje', 'Eliminado');
    }
}
```

## Eloquent ORM — referencia rapida

```php
Curso::all()                        // todos los registros
Curso::find(1)                      // buscar por ID
Curso::findOrFail(1)                // buscar o error 404
Curso::where('cupo', '>', 20)->get() // con condicion
Curso::orderBy('nombre')->get()     // ordenar
Curso::paginate(10)                 // paginacion
Curso::count()                      // contar registros
Curso::first()                      // primer registro

// Crear
$c = new Curso;
$c->nombre = "PHP";
$c->save();
// O con mass assignment:
Curso::create(['nombre' => 'PHP', 'cupo' => 30]);

// Actualizar
$c = Curso::find(1);
$c->nombre = "PHP Avanzado";
$c->save();

// Eliminar
Curso::destroy(1);
Curso::destroy([1, 2, 3]);
```

**Importante:** para usar `create()` masivo, definir `$fillable` en el modelo:

```php
protected $fillable = ['nombre', 'objetivo', 'cupo'];
```

## Validacion — reglas comunes

| Regla                     | Descripcion                        |
|---------------------------|------------------------------------|
| `required`                | Campo obligatorio                  |
| `email`                   | Formato de correo valido           |
| `numeric`                 | Debe ser un numero                 |
| `min:N`                   | Minimo N caracteres o valor        |
| `max:N`                   | Maximo N caracteres o valor        |
| `unique:tabla,columna`    | Unico en la tabla de BD            |
| `confirmed`               | Debe existir campo `_confirmation` |
| `date`                    | Fecha valida                       |
| `image`                   | Archivo de imagen                  |

## Plantillas Blade

```blade
{{-- Herencia de plantilla --}}
@extends('plantilla')
@section('contenido')
    {{-- contenido de la pagina --}}
@endsection

{{-- En la plantilla padre: --}}
@yield('contenido')

{{-- Imprimir variables --}}
{{ $variable }}                  {{-- con escape HTML (seguro) --}}
{!! $variable !!}                {{-- sin escape (cuidado XSS) --}}

{{-- Condicionales --}}
@if($condicion)  ...  @elseif($otra)  ...  @else  ...  @endif

{{-- Bucles --}}
@foreach($cursos as $curso)
    <p>{{ $curso->nombre }}</p>
@endforeach

@forelse($cursos as $curso)
    <p>{{ $curso->nombre }}</p>
@empty
    <p>No hay cursos.</p>
@endforelse

{{-- Errores de validacion --}}
@error('nombre')
    <span class="text-danger">{{ $message }}</span>
@enderror

{{-- Helpers --}}
{{ route('edit', $id) }}         {{-- URL por nombre de ruta --}}
{{ old('nombre') }}              {{-- valor anterior del form --}}
{{ old('nombre', $curso->nombre) }}  {{-- anterior o default --}}
{{ asset('css/style.css') }}     {{-- ruta a archivo en /public --}}
{{ session('mensaje') }}         {{-- dato flash de sesion --}}
```

## Formularios con seguridad

```html
<!-- Crear (POST) -->
<form action="{{ route('store') }}" method="POST">
    @csrf
    <input name="nombre" value="{{ old('nombre') }}">
    <button type="submit">Guardar</button>
</form>

<!-- Actualizar (PUT) -->
<form action="{{ route('update', $curso->id) }}" method="POST">
    @csrf
    @method('PUT')
    <input name="nombre" value="{{ old('nombre', $curso->nombre) }}">
    <button type="submit">Actualizar</button>
</form>

<!-- Eliminar (DELETE) -->
<form action="{{ route('destroy', $curso->id) }}" method="POST">
    @csrf
    @method('DELETE')
    <button onclick="return confirm('Seguro?')">Eliminar</button>
</form>
```

## Migraciones — tipos de columna

```php
$table->id();                  // BIGINT autoincremental (PK)
$table->string('nombre');      // VARCHAR(255)
$table->string('nombre', 100); // VARCHAR(100)
$table->text('descripcion');   // TEXT
$table->integer('cupo');       // INTEGER
$table->float('precio');       // FLOAT
$table->boolean('activo');     // BOOLEAN
$table->date('fecha');         // DATE
$table->timestamps();          // created_at + updated_at
```

## Paginacion

```php
// En el controlador:
$cursos = Curso::paginate(4);

// En la vista Blade:
{{ $cursos->links() }}
```

## Errores comunes

| Error                                   | Causa                                          | Solucion                                  |
|-----------------------------------------|------------------------------------------------|-------------------------------------------|
| Error 419 (Page Expired)               | Falta `@csrf` en el formulario                 | Agregar `@csrf` en todo form POST         |
| Error 405 (Method Not Allowed)         | Verbo HTTP no coincide con la ruta             | Agregar `@method('PUT')` o `@method('DELETE')` |
| "Add [campo] to fillable property"     | Campo no esta en `$fillable` del modelo        | Agregar el campo a `$fillable`            |
| Datos del form no llegan               | Falta `name` en el input HTML                  | Agregar `name="campo"` al input           |
| Validacion falla sin mostrar errores   | No se muestran `$errors` en la vista           | Agregar `@error('campo')` o `$errors->all()` |
| "Class not found"                      | Autoload no actualizado                        | Ejecutar `composer dump-autoload`         |
| Cambios en .env no se reflejan         | Cache de configuracion vieja                   | `php artisan config:clear && php artisan cache:clear` |

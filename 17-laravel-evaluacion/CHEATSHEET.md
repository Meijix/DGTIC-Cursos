# Cheatsheet — Modulo 17: Evaluacion Laravel — CRUD Livewire

## Composicion de componentes

```
Customers.php        -> Listar + Eliminar  -> /customers
CreateCustomer.php   -> Crear              -> /customers/create
EditCustomer.php     -> Editar             -> /customers/{customer}/edit
ViewCustomer.php     -> Ver detalle        -> /customers/{customer}
```

Cada componente = una sola responsabilidad.

## Route Model Binding

```php
// Ruta
Route::get('/customers/{customer}/edit', EditCustomer::class);

// Componente: Laravel resuelve Customer automaticamente (404 si no existe)
public function mount(Customer $customer) {
    $this->customer = $customer;
    $this->name = $customer->name;
}
```

Requisitos: parametro `{customer}` = nombre del modelo en minusculas + type hint en mount.

## Factories

```php
// database/factories/CustomerFactory.php
public function definition(): array {
    return [
        'name'  => $this->faker->name(),
        'email' => $this->faker->unique()->safeEmail(),
        'phone' => $this->faker->phoneNumber(),
    ];
}
```

| Metodo | Efecto |
|--------|--------|
| `Customer::factory()->create()` | Crea 1 en BD |
| `Customer::factory(50)->create()` | Crea 50 en BD |
| `Customer::factory()->make()` | Instancia sin guardar |
| `Customer::factory()->create(['name' => 'Ana'])` | Con dato especifico |

## Faker comun

`->name()` `->unique()->safeEmail()` `->phoneNumber()` `->address()` `->date()` `->numberBetween(1,100)` `->sentence()` `->boolean(70)`

## Seeders

```bash
php artisan db:seed                          # Ejecutar seeders
php artisan migrate:fresh --seed             # Recrear BD + seeders
```

## Testing

```php
use Illuminate\Foundation\Testing\RefreshDatabase;
use Livewire\Livewire;

class CustomerTest extends TestCase {
    use RefreshDatabase;  // BD limpia entre cada test

    public function test_puede_crear_cliente() {
        $datos = Customer::factory()->make()->toArray();
        Livewire::test(CreateCustomer::class)
            ->set('name', $datos['name'])
            ->set('email', $datos['email'])
            ->call('save');
        $this->assertDatabaseHas('customers', ['email' => $datos['email']]);
    }

    public function test_validacion_requiere_nombre() {
        Livewire::test(CreateCustomer::class)
            ->set('name', '')->call('save')
            ->assertHasErrors(['name' => 'required']);
    }
}
```

## Asserts de testing

| Assert | Verifica |
|--------|----------|
| `assertDatabaseHas('tabla', [...])` | Registro existe |
| `assertDatabaseMissing('tabla', [...])` | Registro no existe |
| `assertHasErrors(['campo'])` | Campo tiene error de validacion |
| `assertHasNoErrors()` | Sin errores |
| `assertSee('texto')` | Texto visible en la vista |
| `assertRedirect(route('...'))` | Redirige correctamente |

## Comandos artisan para testing

```bash
php artisan test                       # Todas las pruebas
php artisan test --filter=Customer     # Filtrar por nombre
php artisan test --testsuite=Feature   # Solo Feature tests
```

## Navegacion

```php
return redirect()->route('customers');                      // Despues de guardar
route('edit', ['customer' => $customer->id])                // Generar URL
```

```blade
<a href="{{ route('customers') }}" wire:navigate>Lista</a>  {{-- SPA nav --}}
<button wire:click="delete({{ $id }})" wire:confirm="Seguro?">Eliminar</button>
```

## Convenciones

| Elemento | Ejemplo |
|----------|---------|
| Modelo | `Customer` (singular, PascalCase) |
| Tabla | `customers` (plural, snake_case) |
| Factory | `CustomerFactory` |
| Componente | `CreateCustomer` (PascalCase) |
| Vista | `create-customer.blade.php` (kebab-case) |

## Errores comunes

| Error | Solucion |
|-------|----------|
| `unique` falla al editar sin cambiar email | `Rule::unique('customers','email')->ignore($this->customer->id)` |
| Mass assignment error | Definir `protected $fillable = [...]` en el modelo |
| Test falla por datos residuales | Agregar `use RefreshDatabase` al test |
| Route Model Binding no funciona | Verificar `{customer}` + `Customer $customer` en mount |

# Modulo 17: Proyecto de Evaluacion - CRUD Completo con Livewire

## Objetivo del Modulo

Este modulo es un **proyecto de evaluacion** donde se aplican todos los conocimientos
adquiridos en los modulos anteriores (13-16) para construir un CRUD completo de clientes
usando Laravel y Livewire con el patron de **composicion de componentes**.

---

## 1. Criterios de Evaluacion

### Que se evalua en este proyecto:

| Criterio | Descripcion | Peso |
|----------|-------------|------|
| **Funcionalidad completa** | CRUD funcional (Crear, Leer, Actualizar, Eliminar) | Alto |
| **Validacion de datos** | Reglas de validacion en todos los formularios | Alto |
| **Organizacion del codigo** | Separacion en componentes con responsabilidad unica | Alto |
| **Route Model Binding** | Uso correcto de inyeccion de modelos en rutas | Medio |
| **Modelo bien configurado** | $fillable, HasFactory, convenciones de nombres | Medio |
| **Migraciones correctas** | Tipos de datos apropiados, restricciones, reversibilidad | Medio |
| **Factory para testing** | Generacion de datos de prueba con Faker | Medio |
| **Experiencia de usuario** | Mensajes claros, navegacion intuitiva | Bajo |
| **Codigo limpio** | Nombres descriptivos, sin codigo muerto excesivo | Bajo |

### Que hace que el codigo sea "bueno":

```
BUENO:                              MALO:
- Nombres descriptivos              - Variables como $x, $data
- Un componente = una tarea          - Todo en un solo archivo
- Validacion completa                - Sin validacion
- $fillable definido                 - $guarded = [] (todo permitido)
- Mensajes en espanol               - Mensajes por defecto en ingles
- Route Model Binding               - Customer::find($id) manual
```

---

## 2. Composicion de Componentes: Dividir el CRUD

### Comparacion Modulo 16 vs Modulo 17

```
MODULO 16 - UN SOLO COMPONENTE:
================================
CustomerManager.php
├── $customers, $name, $email, ...
├── $isOpen, $isEditing, $selectedId
├── create()
├── edit($id)
├── save()
├── delete($id)
└── render()

Problemas:
- El archivo crece mucho (200+ lineas)
- Dificil de testear partes individuales
- Cambiar una funcion puede romper otra
- Variables de estado complejas ($isOpen, $isEditing)


MODULO 17 - MULTIPLES COMPONENTES:
====================================
Customers.php (Listar + Eliminar)
├── $customers
├── mount()
├── delete($id)
└── render()

CreateCustomer.php (Crear)
├── $name, $email, $phone, ...
├── $rules, $messages
├── save()
└── render()

EditCustomer.php (Editar)
├── $customer, $name, $email, ...
├── $rules, $messages
├── mount(Customer $customer)
├── update()
└── render()

ViewCustomer.php (Ver detalle)
├── $customer
├── mount(Customer $customer)
└── render()

Ventajas:
- Cada componente tiene UNA responsabilidad
- Archivos pequenos y faciles de leer
- Se pueden testear individualmente
- Cambios aislados (no afectan otros componentes)
```

### Flujo de Navegacion entre Componentes

```
                    ┌──────────────────────┐
                    │   /customers         │
                    │   Customers.php      │
                    │   (Lista de clientes)│
                    └──────┬───────────────┘
                           │
              ┌────────────┼────────────┐
              │            │            │
              ▼            ▼            ▼
   ┌──────────────┐ ┌───────────┐ ┌──────────────┐
   │ /customers/  │ │/customers/│ │ wire:click=   │
   │ create       │ │ {id}      │ │ "delete(id)" │
   │ CreateCustomer│ │ViewCustomer│ │ (AJAX, sin   │
   │ (Formulario) │ │ (Detalle) │ │  navegacion)  │
   └──────────────┘ └─────┬─────┘ └──────────────┘
                          │
                          ▼
                   ┌──────────────┐
                   │ /customers/  │
                   │ {id}/edit    │
                   │ EditCustomer │
                   │ (Formulario) │
                   └──────────────┘
```

---

## 3. Route Model Binding (Enlace Modelo-Ruta)

### Que es Route Model Binding?

Es la capacidad de Laravel de **resolver automaticamente** un modelo de Eloquent
a partir de un parametro en la URL.

### Como funciona paso a paso:

```
1. El usuario visita: /customers/5/edit

2. Laravel mira la ruta definida:
   Route::get('/customers/{customer}/edit', EditCustomer::class)

3. Laravel ve que el parametro se llama {customer}

4. Laravel busca un modelo llamado "Customer" (capitaliza el nombre)

5. Laravel ejecuta internamente: Customer::findOrFail(5)

6. El metodo mount() del componente recibe el resultado:
   public function mount(Customer $customer)
   {
       // $customer ya es el objeto Customer con id=5
       // con TODOS sus datos cargados desde la BD
   }

7. Si el ID no existe, Laravel automaticamente devuelve error 404
```

### Sin Route Model Binding vs Con Route Model Binding:

```php
// SIN Route Model Binding (forma manual):
Route::get('/customers/{id}/edit', EditCustomer::class);

public function mount($id)
{
    $customer = Customer::find($id);
    if (!$customer) {
        abort(404); // Hay que manejar el error manualmente
    }
    $this->customer = $customer;
}

// CON Route Model Binding (forma elegante):
Route::get('/customers/{customer}/edit', EditCustomer::class);

public function mount(Customer $customer)
{
    $this->customer = $customer; // Ya viene cargado y validado
}
```

### Requisitos para que funcione:

1. El parametro en la ruta (`{customer}`) debe coincidir con el nombre del modelo en minusculas
2. El parametro en mount() debe tener el **type hint** del modelo (`Customer $customer`)
3. El modelo debe existir en `app/Models/`
4. Por defecto busca por la columna `id`. Se puede cambiar con `getRouteKeyName()`

---

## 4. Factories y Seeders: Generando Datos de Prueba

### Que es un Factory?

Es un generador de datos falsos pero realistas para un modelo.

```php
// Crear 1 cliente con datos falsos:
Customer::factory()->create();
// Resultado: Customer { name: "Ana Garcia", email: "ana@example.com", ... }

// Crear 50 clientes:
Customer::factory(50)->create();

// Crear sin guardar en BD (solo instancia PHP):
$customer = Customer::factory()->make();

// Crear con datos especificos:
Customer::factory()->create(['name' => 'Mi Nombre']);
```

### Que es un Seeder?

Es un script que llena la BD con datos iniciales.

```php
// database/seeders/DatabaseSeeder.php
public function run(): void
{
    Customer::factory(10)->create(); // Crea 10 clientes falsos
}
```

### Comandos:

```bash
# Ejecutar seeders:
php artisan db:seed

# Recrear la BD y ejecutar seeders:
php artisan migrate:fresh --seed

# Ejecutar un seeder especifico:
php artisan db:seed --class=CustomerSeeder
```

### Faker: La libreria de datos falsos

```php
$this->faker->name()              // "Juan Perez Garcia"
$this->faker->unique()->safeEmail() // "juan.perez@example.com"
$this->faker->phoneNumber()       // "+52 55 1234 5678"
$this->faker->address()           // "Calle Reforma 123, Col. Centro"
$this->faker->date()              // "1990-05-15"
$this->faker->numberBetween(1,100) // 42
$this->faker->sentence()          // "Lorem ipsum dolor sit amet."
$this->faker->boolean(70)         // true (70% probabilidad)
```

---

## 5. Navegacion entre Componentes

### Formas de navegar en Livewire:

```php
// 1. REDIRECT desde PHP (despues de guardar):
return redirect()->route('customers');
// Redirige a la lista despues de crear/editar

// 2. ENLACES HTML (en las vistas Blade):
<a href="{{ route('view', ['customer' => $customer->id]) }}">Ver</a>
// Navegacion tradicional con recarga de pagina

// 3. WIRE:NAVIGATE (Livewire 3, navegacion SPA):
<a href="{{ route('customers') }}" wire:navigate>Lista</a>
// Navegacion sin recarga completa (como React Router)

// 4. WIRE:CLICK para acciones sin navegacion:
<button wire:click="delete({{ $id }})">Borrar</button>
// Ejecuta metodo PHP sin cambiar de pagina
```

### Generacion de URLs con route():

```php
// Ruta simple (sin parametros):
route('customers')     // -> /customers

// Ruta con parametro:
route('view', ['customer' => 5])   // -> /customers/5
route('edit', ['customer' => 5])   // -> /customers/5/edit

// Ruta con modelo (Laravel extrae el ID automaticamente):
route('view', $customer)           // -> /customers/5
```

---

## 6. Testing en Laravel

### Tipos de pruebas:

```
tests/
├── Unit/           -> Pruebas de funciones individuales (rapidas)
│   └── ExampleTest.php
└── Feature/        -> Pruebas de funcionalidades completas (mas lentas)
    └── ExampleTest.php
```

### Ejemplo de test para el CRUD de clientes:

```php
// tests/Feature/CustomerTest.php
use App\Models\Customer;

public function test_puede_crear_cliente()
{
    // 1. Preparar datos de prueba
    $datos = Customer::factory()->make()->toArray();

    // 2. Simular envio de formulario
    Livewire::test(CreateCustomer::class)
        ->set('name', $datos['name'])
        ->set('email', $datos['email'])
        ->set('phone', $datos['phone'])
        ->set('address', $datos['address'])
        ->set('birthday', $datos['birthday'])
        ->call('save');

    // 3. Verificar que se guardo en la BD
    $this->assertDatabaseHas('customers', [
        'email' => $datos['email']
    ]);
}

public function test_validacion_requiere_nombre()
{
    Livewire::test(CreateCustomer::class)
        ->set('name', '')  // Nombre vacio
        ->call('save')
        ->assertHasErrors(['name' => 'required']);
}
```

### Ejecutar pruebas:

```bash
php artisan test                    # Ejecutar todas las pruebas
php artisan test --filter=Customer  # Solo pruebas de Customer
php artisan test --testsuite=Unit   # Solo pruebas unitarias
```

---

## 7. Organizacion del Codigo - Buenas Practicas

### Estructura del proyecto:

```
app/
├── Http/
│   └── Livewire/                  # Componentes Livewire
│       ├── Customers.php          # Listar + Eliminar
│       ├── CreateCustomer.php     # Crear
│       ├── EditCustomer.php       # Editar
│       └── ViewCustomer.php       # Ver detalle
├── Models/
│   └── Customer.php               # Modelo Eloquent
database/
├── factories/
│   └── CustomerFactory.php        # Generador de datos falsos
├── migrations/
│   └── create_customers_table.php # Estructura de la tabla
├── seeders/
│   └── DatabaseSeeder.php         # Poblador de datos iniciales
resources/
└── views/
    ├── components/layouts/
    │   └── app.blade.php          # Layout principal
    └── livewire/
        ├── customers.blade.php        # Vista de lista
        ├── create-customer.blade.php  # Vista de creacion
        ├── edit-customer.blade.php    # Vista de edicion
        └── view-customer.blade.php    # Vista de detalle
routes/
└── web.php                        # Definicion de rutas
```

### Convenciones de nombres:

| Elemento | Convencion | Ejemplo |
|----------|-----------|---------|
| Modelo | Singular, PascalCase | `Customer` |
| Tabla BD | Plural, snake_case | `customers` |
| Migracion | snake_case con accion | `create_customers_table` |
| Factory | Modelo + Factory | `CustomerFactory` |
| Componente | PascalCase descriptivo | `CreateCustomer` |
| Vista | kebab-case | `create-customer.blade.php` |
| Ruta | plural, kebab-case | `/customers/{customer}/edit` |

---

## 8. Ejercicios Practicos

### Ejercicio 1: Agregar paginacion
Modifica `Customers.php` para usar paginacion en vez de `Customer::all()`:
```php
use Livewire\WithPagination;

class Customers extends Component
{
    use WithPagination;

    public function render()
    {
        return view('livewire.customers', [
            'customers' => Customer::paginate(10)
        ]);
    }
}
```

### Ejercicio 2: Corregir la validacion unique en EditCustomer
La validacion `unique:customers,email` falla al editar sin cambiar el email.
Investiga como excluir el registro actual de la validacion unique.

### Ejercicio 3: Agregar busqueda
Agrega un campo de busqueda en la lista de clientes que filtre por nombre o email.
Pista: usa `Customer::where('name', 'like', '%'.$busqueda.'%')->get()`.

### Ejercicio 4: Agregar confirmacion con SweetAlert
Reemplaza el `confirm()` nativo del navegador con SweetAlert2 para confirmaciones
mas bonitas al eliminar un cliente.

### Ejercicio 5: Crear tests automatizados
Crea al menos 3 pruebas en `tests/Feature/CustomerTest.php`:
1. Que se puede crear un cliente con datos validos
2. Que la validacion rechaza un email duplicado
3. Que se puede eliminar un cliente existente

### Ejercicio 6: Agregar un campo "notas"
1. Crea una nueva migracion para agregar la columna `notes` (TEXT, nullable)
2. Actualiza el modelo ($fillable)
3. Actualiza el factory
4. Actualiza los formularios de crear y editar
5. Muestra las notas en la vista de detalle

---

## Resumen de Conceptos Clave

```
MODULO 17 - PROYECTO DE EVALUACION
====================================

1. COMPOSICION: Dividir el CRUD en componentes independientes
   - Cada componente = una responsabilidad
   - Mas facil de mantener y testear

2. ROUTE MODEL BINDING: Laravel resuelve modelos desde la URL
   - {customer} + Customer $customer = resolucion automatica
   - Manejo automatico de errores 404

3. FACTORIES + SEEDERS: Datos de prueba
   - Faker genera datos realistas
   - Esencial para testing y desarrollo

4. NAVEGACION: redirect(), route(), wire:click
   - redirect() para despues de guardar
   - route() para generar URLs con nombres
   - wire:click para acciones sin navegacion

5. VALIDACION: $rules + $messages + $this->validate()
   - Siempre validar antes de guardar
   - Mensajes personalizados en espanol

6. TESTING: Verificar que todo funciona
   - Factories generan datos de prueba
   - Tests automatizados previenen regresiones
```

# Setup — Laravel Evaluación (Módulo 17)

## Requisitos previos

- **PHP** >= 8.1 (`php -v`)
- **Composer** >= 2.x (`composer -V`)

## Instalación paso a paso

```bash
# 1. Entrar a la carpeta del proyecto
cd 17-laravel-evaluacion

# 2. Instalar dependencias de PHP
composer install

# 3. Crear archivo de configuración
#    (este proyecto no tiene .env.example, hay que crearlo manualmente)
cat > .env << 'EOF'
APP_NAME=Laravel
APP_ENV=local
APP_KEY=
APP_DEBUG=true
APP_URL=http://localhost

DB_CONNECTION=sqlite

SESSION_DRIVER=file
CACHE_STORE=file
EOF

# 4. Generar clave de la aplicación
php artisan key:generate

# 5. Crear la base de datos SQLite
touch database/database.sqlite

# 6. Ejecutar migraciones (crea tabla customers)
php artisan migrate

# 7. (Opcional) Poblar con datos de prueba
php artisan tinker
# Dentro de tinker:
# \App\Models\Customer::factory(10)->create();
# exit

# 8. Levantar el servidor
php artisan serve
```

Abre **http://localhost:8000** en tu navegador.

## Qué vas a ver

- **`/customers`**: Lista de todos los clientes con botón de eliminar
- **`/customers/create`**: Formulario para crear un nuevo cliente
- **`/customers/{id}`**: Ver detalle de un cliente
- **`/customers/{id}/edit`**: Editar un cliente existente

## Diferencia con los Módulos 15 y 16

Este es un **proyecto evaluado** que demuestra un uso más avanzado de Livewire:

| Aspecto | Mod 15 | Mod 16 | Mod 17 |
|---------|--------|--------|--------|
| Componentes | 0 (controllers) | 1 componente | 4 componentes |
| CRUD | 1 controller | 1 componente | Separado por acción |
| Route Model Binding | No | No | Sí |
| Factories | No | No | Sí |
| Laravel version | 11 | 11 | 10 |

## Estructura de archivos clave

```
app/
├── Http/Livewire/
│   ├── Customers.php          ← Lista + eliminar
│   ├── CreateCustomer.php     ← Crear cliente
│   ├── EditCustomer.php       ← Editar cliente
│   └── ViewCustomer.php       ← Ver detalle
├── Models/
│   └── Customer.php           ← Modelo con $fillable

database/
├── migrations/
│   └── ..._create_customers_table.php
└── factories/
    └── CustomerFactory.php    ← Genera datos de prueba con Faker

resources/views/
├── components/layouts/app.blade.php  ← Layout principal
└── livewire/
    ├── customers.blade.php
    ├── create-customer.blade.php
    ├── edit-customer.blade.php
    └── view-customer.blade.php

routes/web.php                 ← Rutas con Route Model Binding
```

## Generar datos de prueba

```bash
# Opción 1: Tinker (interactivo)
php artisan tinker
>>> \App\Models\Customer::factory(20)->create();

# Opción 2: Crear un seeder
php artisan make:seeder CustomerSeeder
# Editar database/seeders/CustomerSeeder.php y agregar:
#   Customer::factory(20)->create();
php artisan db:seed --class=CustomerSeeder
```

## Solución de problemas

| Error | Solución |
|-------|----------|
| `Class Livewire not found` | `composer dump-autoload` |
| `.env not found` | Crear manualmente (ver paso 3) |
| `SQLSTATE: no such table` | `php artisan migrate` |
| Sin datos en la lista | Crear con factory (ver arriba) |
| `Target class does not exist` | Verificar namespace en `app/Http/Livewire/` |

## Conceptos demostrados

Revisa [CONCEPTOS.md](CONCEPTOS.md) para la teoría sobre composición de componentes, Route Model Binding y factories.

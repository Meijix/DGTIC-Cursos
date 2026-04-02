# Setup — Laravel + Livewire (Módulo 16)

## Requisitos previos

- **PHP** >= 8.2 (`php -v`)
- **Composer** >= 2.x (`composer -V`)
- **Node.js** >= 18 y npm (`node -v`) — para compilar assets con Vite

## Instalación paso a paso

```bash
# 1. Entrar a la carpeta del proyecto
cd 16-laravel-livewire

# 2. Instalar dependencias de PHP
composer install

# 3. Crear archivo de configuración local
cp .env.example .env

# 4. Generar clave de la aplicación
php artisan key:generate

# 5. Crear la base de datos SQLite
touch database/database.sqlite

# 6. Ejecutar migraciones
php artisan migrate

# 7. Instalar dependencias de frontend (Tailwind + Vite)
npm install

# 8. Compilar assets (en otra terminal, o usar --build)
npm run build
# O para desarrollo con hot-reload:
# npm run dev

# 9. Levantar el servidor
php artisan serve
```

Abre **http://localhost:8000** en tu navegador.

## Diferencia con el Módulo 15

Este proyecto hace lo MISMO que el 15 (CRUD de cursos), pero usando **Livewire** en vez de controladores tradicionales:

| Aspecto | Módulo 15 (tradicional) | Módulo 16 (Livewire) |
|---------|------------------------|---------------------|
| Rutas | 7+ rutas en web.php | 1 ruta |
| Controlador | CursoController.php | CursoComponent.php |
| Recarga | Página completa | Solo el componente (AJAX) |
| JavaScript | No necesario | No necesario (Livewire lo maneja) |
| Formularios | Envío POST clásico | wire:model + wire:click |

## Estructura de archivos clave

```
app/
├── Livewire/
│   └── CursoComponent.php       ← Lógica del componente (CRUD)
└── Models/
    └── Curso.php                 ← Modelo Eloquent

resources/views/
├── layout.blade.php              ← Layout con @livewireStyles/@livewireScripts
├── principal.blade.php           ← Página de entrada
└── livewire/
    ├── curso-component.blade.php ← Vista principal del componente
    ├── create.blade.php          ← Partial: formulario de creación
    └── form.blade.php            ← Partial: campos del formulario

routes/web.php                    ← Solo 1 ruta
```

## Nota importante sobre $fillable

El modelo `Curso.php` de este proyecto **no tiene `$fillable` definido**. Esto es un bug intencional para aprender. Si ves el error:

```
Add [nombre] to fillable property to allow mass assignment
```

Agrega esto en `app/Models/Curso.php`:

```php
protected $fillable = ['nombre', 'objetivo', 'modalidad', 'cupo', 'periodo', 'horario', 'dias', 'salon'];
```

## Solución de problemas

| Error | Solución |
|-------|----------|
| `Livewire component not found` | `composer dump-autoload` |
| `Vite manifest not found` | Ejecutar `npm run build` |
| `SQLSTATE: no such table` | Ejecutar `php artisan migrate` |
| Componente no se actualiza | Verificar `@livewireScripts` en layout |

## Conceptos demostrados

Revisa [CONCEPTOS.md](CONCEPTOS.md) para la teoría sobre Livewire, data binding y componentes reactivos.

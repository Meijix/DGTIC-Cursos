# Setup — Laravel CRUD (Módulo 15)

## Requisitos previos

- **PHP** >= 8.2 (`php -v`)
- **Composer** >= 2.x (`composer -V`)

Si no los tienes instalados:
```bash
# macOS (con Homebrew)
brew install php composer

# Ubuntu/Debian
sudo apt install php php-mbstring php-xml php-sqlite3 composer

# Windows: descargar de https://windows.php.net y https://getcomposer.org
```

## Instalación paso a paso

```bash
# 1. Entrar a la carpeta del proyecto
cd 15-laravel-crud

# 2. Instalar dependencias de PHP
composer install

# 3. Crear archivo de configuración local
cp .env.example .env

# 4. Generar clave de la aplicación
php artisan key:generate

# 5. Crear la base de datos SQLite (archivo vacío)
touch database/database.sqlite

# 6. Ejecutar migraciones (crea las tablas)
php artisan migrate

# 7. Levantar el servidor de desarrollo
php artisan serve
```

Abre **http://localhost:8000** en tu navegador.

## Qué vas a ver

- **Página principal** (`/`): lista de cursos con paginación
- **Agregar** (`/agregar`): formulario para crear un nuevo curso
- **Editar** (`/editar/{id}`): formulario para modificar un curso existente
- **Eliminar**: botón en la lista que borra el curso
- **Contacto** (`/contacto`): formulario de contacto (requiere configurar email)

## Estructura de archivos clave

```
app/
├── Http/Controllers/
│   ├── CursoController.php    ← CRUD (index, create, store, edit, update, destroy)
│   └── MensajesController.php ← Formulario de contacto + email
├── Models/
│   └── Curso.php              ← Modelo Eloquent
└── Mail/
    └── MensajeRecibido.php    ← Clase Mailable

resources/views/
├── plantilla.blade.php        ← Layout base (@yield/@section)
├── principal.blade.php        ← Lista de cursos
├── agregar.blade.php          ← Formulario de creación
├── editar.blade.php           ← Formulario de edición
├── contacto.blade.php         ← Formulario de contacto
└── aviso.blade.php            ← Página de aviso

routes/web.php                 ← Todas las rutas
database/migrations/           ← Definición de tablas
```

## Solución de problemas

| Error | Solución |
|-------|----------|
| `Could not find driver` | Instalar extensión SQLite: `sudo apt install php-sqlite3` |
| `SQLSTATE: no such table` | Ejecutar `php artisan migrate` |
| `No application key` | Ejecutar `php artisan key:generate` |
| `Permission denied` en storage | `chmod -R 775 storage bootstrap/cache` |
| Warning de `PDO::MYSQL_ATTR_SSL_CA` | Normal en PHP 8.5, ignorar |

## Conceptos demostrados

Revisa el archivo [CONCEPTOS.md](CONCEPTOS.md) para la teoría completa sobre MVC, Eloquent, Blade y rutas.

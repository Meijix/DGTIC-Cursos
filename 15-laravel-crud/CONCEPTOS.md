# Modulo 15: Laravel CRUD - Conceptos Fundamentales

## Tabla de Contenidos
1. [Que es Laravel y MVC](#1-que-es-laravel-y-mvc)
2. [Ciclo de vida de una peticion](#2-ciclo-de-vida-de-una-peticion)
3. [Artisan CLI](#3-artisan-cli)
4. [Enrutamiento (Routing)](#4-enrutamiento-routing)
5. [Controladores](#5-controladores)
6. [Eloquent ORM](#6-eloquent-orm)
7. [Plantillas Blade](#7-plantillas-blade)
8. [Formularios y seguridad](#8-formularios-y-seguridad)
9. [Sistema de correos (Mail)](#9-sistema-de-correos-mail)
10. [Migraciones de base de datos](#10-migraciones-de-base-de-datos)
11. [Errores comunes](#11-errores-comunes)
12. [Ejercicios de practica](#12-ejercicios-de-practica)

---

## 1. Que es Laravel y MVC

### Laravel
Laravel es un framework de PHP de codigo abierto que sigue el patron de diseno **MVC** (Modelo-Vista-Controlador). Fue creado por Taylor Otwell en 2011 y es uno de los frameworks mas populares para desarrollo web con PHP.

### Por que usar un framework
- **No reinventar la rueda**: enrutamiento, autenticacion, correos, base de datos ya estan resueltos
- **Seguridad**: proteccion contra CSRF, XSS, SQL Injection incluida
- **Convencion sobre configuracion**: si sigues las convenciones, todo funciona con minima configuracion
- **Comunidad enorme**: documentacion, tutoriales, paquetes de terceros

### Patron MVC (Modelo-Vista-Controlador)

```
+------------------------------------------------------------------+
|                    PATRON MVC EN LARAVEL                         |
+------------------------------------------------------------------+
|                                                                  |
|  MODELO (Model)         La logica de datos y negocio             |
|  app/Models/            Interactua con la base de datos          |
|  Curso.php              via Eloquent ORM                         |
|                                                                  |
|  VISTA (View)           La presentacion / interfaz de usuario    |
|  resources/views/       Archivos Blade (.blade.php)              |
|  principal.blade.php    Solo se encarga de MOSTRAR datos         |
|                                                                  |
|  CONTROLADOR (Controller)  La logica de la aplicacion            |
|  app/Http/Controllers/     Recibe peticiones, procesa datos,     |
|  CursoController.php       coordina Modelo y Vista               |
|                                                                  |
+------------------------------------------------------------------+
```

### Analogia del restaurante
| MVC | Restaurante | Funcion |
|-----|-------------|---------|
| **Vista** | El menu y los platos servidos | Lo que ve el cliente |
| **Controlador** | El mesero | Recibe pedido, lo lleva a la cocina, trae la comida |
| **Modelo** | La cocina y los ingredientes | Donde se preparan y almacenan los datos |

---

## 2. Ciclo de vida de una peticion

Cuando un usuario visita una URL en una aplicacion Laravel, esto es lo que sucede internamente:

```
CICLO DE VIDA DE UNA PETICION HTTP EN LARAVEL

  +------------------+
  |   NAVEGADOR      |     1. El usuario escribe una URL o
  |   (Cliente)      |        hace clic en un enlace
  +--------+---------+
           |
           | HTTP Request (GET /editar/5)
           v
  +------------------+
  |   public/        |     2. index.php es el punto de entrada.
  |   index.php      |        Carga el framework completo.
  +--------+---------+
           |
           v
  +------------------+
  |   MIDDLEWARE      |     3. Filtros que procesan la peticion ANTES
  |   (CSRF, Auth,   |        de llegar al controlador.
  |    Session)       |        Ejemplo: verificar token CSRF.
  +--------+---------+
           |
           v
  +------------------+
  |   ROUTER          |    4. routes/web.php busca la ruta que
  |   (web.php)       |       coincide con la URL y el verbo HTTP.
  +--------+---------+
           |
           | Route::get('/editar/{id}', [CursoController::class, 'edit'])
           v
  +------------------+
  |   CONTROLADOR     |    5. Se ejecuta el metodo del controlador.
  |   CursoController |       Valida datos, consulta el modelo.
  |   ->edit($id)     |
  +--------+---------+
           |
           | $curso = Curso::find($id);
           v
  +------------------+
  |   MODELO          |    6. Eloquent traduce la peticion a SQL
  |   Curso::find(5)  |       y consulta la base de datos.
  |   (Eloquent ORM)  |       SELECT * FROM cursos WHERE id = 5
  +--------+---------+
           |
           | Objeto $curso con los datos
           v
  +------------------+
  |   VISTA           |    7. El controlador pasa datos a la vista Blade.
  |   editar.blade.php|       Blade genera el HTML final.
  +--------+---------+
           |
           | HTML generado
           v
  +------------------+
  |   NAVEGADOR       |    8. El HTML se envia de vuelta al navegador.
  |   (Respuesta)     |       El usuario ve la pagina.
  +------------------+
```

---

## 3. Artisan CLI

Artisan es la herramienta de linea de comandos de Laravel. Se ejecuta desde la raiz del proyecto.

### Comandos mas usados

| Comando | Descripcion |
|---------|-------------|
| `php artisan serve` | Inicia el servidor de desarrollo en localhost:8000 |
| `php artisan make:controller NombreController` | Crea un nuevo controlador |
| `php artisan make:controller NombreController --resource` | Controlador con los 7 metodos CRUD |
| `php artisan make:model Nombre` | Crea un nuevo modelo Eloquent |
| `php artisan make:model Nombre -m` | Modelo + migracion |
| `php artisan make:model Nombre -mcr` | Modelo + migracion + controlador resource |
| `php artisan make:migration create_tabla_table` | Crea una migracion |
| `php artisan migrate` | Ejecuta migraciones pendientes |
| `php artisan migrate:rollback` | Revierte la ultima migracion |
| `php artisan migrate:fresh` | Borra todas las tablas y re-ejecuta migraciones |
| `php artisan make:mail NombreMail` | Crea una clase Mailable |
| `php artisan make:request NombreRequest` | Crea una clase Form Request (validacion) |
| `php artisan route:list` | Muestra todas las rutas registradas |
| `php artisan tinker` | Consola interactiva para probar codigo PHP/Eloquent |
| `php artisan cache:clear` | Limpia la cache de la aplicacion |
| `php artisan config:clear` | Limpia la cache de configuracion |

### Ejemplo de flujo con Artisan

```bash
# Crear modelo, migracion y controlador de un solo comando
php artisan make:model Curso -mcr

# Editar la migracion en database/migrations/
# Editar el modelo en app/Models/Curso.php
# Editar el controlador en app/Http/Controllers/CursoController.php

# Ejecutar la migracion para crear la tabla
php artisan migrate

# Iniciar el servidor
php artisan serve
```

---

## 4. Enrutamiento (Routing)

### Archivo de rutas: `routes/web.php`
Todas las rutas web se definen aqui. Laravel las carga automaticamente con el middleware `web` (sesiones, CSRF, cookies).

### Tipos de rutas

```php
// 1. RUTA CON CLOSURE (funcion anonima)
// Para paginas simples sin logica compleja
Route::get('/about', function () {
    return view('about');
});

// 2. RUTA CON CONTROLADOR (lo mas comun)
// Conecta una URL con un metodo de un controlador
Route::get('/', [CursoController::class, 'index'])->name('index');

// 3. RUTA CON PARAMETROS
// {id} captura un valor de la URL y lo pasa al metodo
Route::get('/editar/{id}', [CursoController::class, 'edit'])->name('edit');
// /editar/5 -> $id = 5
// /editar/12 -> $id = 12

// 4. RUTA RESOURCE (genera 7 rutas CRUD automaticamente)
Route::resource('cursos', CursoController::class);
// Equivale a definir: index, create, store, show, edit, update, destroy
```

### Verbos HTTP y su uso en CRUD

| Verbo HTTP | Ruta | Accion | Descripcion |
|------------|------|--------|-------------|
| GET | `/cursos` | index | Listar todos |
| GET | `/cursos/create` | create | Mostrar formulario nuevo |
| POST | `/cursos` | store | Guardar nuevo |
| GET | `/cursos/{id}` | show | Ver uno |
| GET | `/cursos/{id}/edit` | edit | Mostrar formulario editar |
| PUT/PATCH | `/cursos/{id}` | update | Actualizar existente |
| DELETE | `/cursos/{id}` | destroy | Eliminar |

### Rutas con nombre (Named Routes)

```php
// Definir:
Route::get('/agregar', [CursoController::class, 'create'])->name('create');

// Usar en vistas:
<a href="{{ route('create') }}">Agregar</a>
// Genera: <a href="/agregar">Agregar</a>

// Con parametros:
<a href="{{ route('edit', $curso->id) }}">Editar</a>
// Genera: <a href="/editar/5">Editar</a>

// En controladores:
return redirect()->route('index');
```

### Por que usar rutas con nombre
Si cambias la URL de `/agregar` a `/nuevo-curso`, solo necesitas cambiar la ruta en web.php. Todos los `route('create')` en las vistas siguen funcionando sin cambios.

---

## 5. Controladores

### Que es un controlador
Es una clase PHP que agrupa la logica relacionada con un recurso. En este proyecto, `CursoController` maneja todo lo relacionado con cursos.

### Los 7 metodos CRUD de un Resource Controller

```php
class CursoController extends Controller
{
    // 1. INDEX - Listar todos (GET /)
    public function index()
    {
        $cursos = Curso::orderBy('id')->paginate(4);
        return view('principal', compact('cursos'));
    }

    // 2. CREATE - Mostrar formulario nuevo (GET /agregar)
    public function create()
    {
        return view('agregar');
    }

    // 3. STORE - Guardar nuevo registro (POST /agregar)
    public function store(Request $request)
    {
        $this->validate($request, ['nombre' => 'required', ...]);
        $curso = new Curso;
        $curso->nombre = $request->nombre;
        $curso->save();
        return redirect(route('index'))->with('mensaje', 'Creado');
    }

    // 4. SHOW - Ver un registro (GET /cursos/{id})
    public function show(string $id) { }

    // 5. EDIT - Mostrar formulario edicion (GET /editar/{id})
    public function edit(string $id)
    {
        $curso = Curso::find($id);
        return view('editar', compact('curso'));
    }

    // 6. UPDATE - Actualizar registro (POST /actualizar/{id})
    public function update(Request $request, string $id)
    {
        $this->validate($request, [...]);
        $curso = Curso::find($id);
        $curso->nombre = $request->nombre;
        $curso->save();
        return redirect(route('index'))->with('mensaje', 'Actualizado');
    }

    // 7. DESTROY - Eliminar registro (DELETE /eliminar/{id})
    public function destroy(string $id)
    {
        Curso::destroy($id);
        return redirect(route('index'))->with('mensaje', 'Eliminado');
    }
}
```

### Validacion en el controlador

```php
// Validacion basica
$this->validate($request, [
    'nombre' => 'required',              // obligatorio
    'email' => 'required|email',         // obligatorio + formato email
    'cupo' => 'required|numeric|min:1',  // obligatorio + numero + minimo 1
    'descripcion' => 'required|min:10',  // obligatorio + minimo 10 caracteres
]);

// Si falla la validacion:
// 1. Laravel redirige automaticamente al formulario anterior
// 2. Los errores estan disponibles en $errors en la vista
// 3. Los valores anteriores estan disponibles con old('campo')
```

### Reglas de validacion comunes

| Regla | Descripcion |
|-------|-------------|
| `required` | Campo obligatorio |
| `email` | Formato de correo valido |
| `numeric` | Debe ser un numero |
| `min:N` | Minimo N caracteres (string) o valor minimo (numero) |
| `max:N` | Maximo N caracteres o valor maximo |
| `unique:tabla,columna` | Debe ser unico en la tabla |
| `confirmed` | Debe existir un campo `campo_confirmation` igual |
| `date` | Debe ser una fecha valida |
| `image` | Debe ser un archivo de imagen |
| `mimes:jpg,png` | Solo tipos de archivo especificos |

### Redireccion con mensajes flash

```php
// En el controlador:
return redirect(route('index'))->with('mensaje', 'Curso creado');

// En la vista:
@if (session('mensaje'))
    <div class="alert alert-success">{{ session('mensaje') }}</div>
@endif
```

---

## 6. Eloquent ORM

### Que es un ORM
ORM (Object-Relational Mapping) es una tecnica que mapea tablas de base de datos a clases PHP. Eloquent es el ORM de Laravel.

### Mapeo Modelo-Tabla

```
Clase PHP (Modelo)          Tabla en la BD
+------------------+        +------------------+
| class Curso      | <----> | tabla: cursos    |
|   ->nombre       |        |   nombre VARCHAR |
|   ->objetivo     |        |   objetivo TEXT  |
|   ->save()       |        |   INSERT/UPDATE  |
+------------------+        +------------------+
```

### Convenciones de nombres

| Modelo (PHP) | Tabla (BD) |
|-------------|------------|
| `Curso` | `cursos` |
| `User` | `users` |
| `CategoriaProducto` | `categoria_productos` |

Si tu tabla no sigue la convencion:
```php
protected $table = 'mi_tabla_personalizada';
```

### Consultas con Eloquent

```php
// OBTENER REGISTROS
Curso::all();                    // Todos los cursos
Curso::find(1);                  // Por ID
Curso::findOrFail(1);            // Por ID (404 si no existe)
Curso::where('cupo', '>', 20)->get();  // Con condicion
Curso::orderBy('nombre')->get(); // Ordenados
Curso::first();                  // Solo el primero
Curso::count();                  // Contar registros
Curso::paginate(10);             // Paginados (10 por pagina)

// CREAR
$curso = new Curso;
$curso->nombre = "PHP";
$curso->save();                  // INSERT INTO cursos...

// O con Mass Assignment:
Curso::create(['nombre' => 'PHP', 'cupo' => 30]);

// ACTUALIZAR
$curso = Curso::find(1);
$curso->nombre = "PHP Avanzado";
$curso->save();                  // UPDATE cursos SET...

// O:
Curso::where('id', 1)->update(['nombre' => 'PHP Avanzado']);

// ELIMINAR
$curso = Curso::find(1);
$curso->delete();                // DELETE FROM cursos...

// O directamente por ID:
Curso::destroy(1);
Curso::destroy([1, 2, 3]);      // Eliminar varios
```

### $fillable vs $guarded

```php
// LISTA BLANCA: solo estos campos pueden asignarse masivamente
protected $fillable = ['nombre', 'objetivo', 'cupo'];
// Curso::create(['nombre' => 'PHP', 'cupo' => 30]); // OK
// Curso::create(['is_admin' => true]);               // Ignorado!

// LISTA NEGRA: todos excepto estos pueden asignarse
protected $guarded = ['id', 'is_admin'];
// Todos los demas campos si pueden asignarse masivamente

// PELIGRO: nunca dejes $guarded vacio sin $fillable
protected $guarded = []; // Permite TODO -> riesgo de seguridad
```

### Relaciones (concepto avanzado)

```php
// Un curso tiene muchos alumnos
class Curso extends Model {
    public function alumnos() {
        return $this->hasMany(Alumno::class);
    }
}

// Un alumno pertenece a un curso
class Alumno extends Model {
    public function curso() {
        return $this->belongsTo(Curso::class);
    }
}

// Uso:
$curso->alumnos;        // Coleccion de alumnos del curso
$alumno->curso->nombre; // Nombre del curso del alumno
```

---

## 7. Plantillas Blade

### Sistema de herencia

```
plantilla.blade.php (Layout)
├── @yield('contenido')  <-- Punto de insercion
│
├── principal.blade.php
│   ├── @extends('plantilla')
│   └── @section('contenido') ... @endsection
│
├── agregar.blade.php
│   ├── @extends('plantilla')
│   └── @section('contenido') ... @endsection
│
├── editar.blade.php
│   ├── @extends('plantilla')
│   └── @section('contenido') ... @endsection
│
└── contacto.blade.php
    ├── @extends('plantilla')
    └── @section('contenido') ... @endsection
```

### Directivas Blade principales

```blade
{{-- IMPRIMIR VALORES --}}
{{ $variable }}              {{-- Con escape HTML (seguro) --}}
{!! $variable !!}            {{-- Sin escape (cuidado con XSS!) --}}

{{-- CONDICIONALES --}}
@if($condicion)
    ...
@elseif($otra)
    ...
@else
    ...
@endif

{{-- BUCLES --}}
@foreach($cursos as $curso)
    <p>{{ $curso->nombre }}</p>
@endforeach

@forelse($cursos as $curso)
    <p>{{ $curso->nombre }}</p>
@empty
    <p>No hay cursos.</p>
@endforelse

{{-- HERENCIA DE PLANTILLAS --}}
@extends('plantilla')           {{-- Hereda del layout --}}
@section('contenido')           {{-- Define seccion --}}
@endsection
@yield('contenido')             {{-- Punto de insercion en el layout --}}

{{-- INCLUIR PARCIALES --}}
@include('partials.header')     {{-- Incluye otra vista --}}

{{-- FORMULARIOS --}}
@csrf                           {{-- Token de proteccion CSRF --}}
@method('PUT')                  {{-- Simular verbo PUT/PATCH/DELETE --}}

{{-- ERRORES DE VALIDACION --}}
@error('nombre')
    <span class="error">{{ $message }}</span>
@enderror

{{-- COMENTARIOS --}}
{{-- Este comentario NO aparece en el HTML generado --}}
<!-- Este comentario SI aparece en el HTML -->
```

### Helpers utiles en Blade

```blade
{{ asset('css/style.css') }}       {{-- URL a archivo en /public --}}
{{ route('index') }}               {{-- URL de ruta por nombre --}}
{{ route('edit', $id) }}           {{-- URL con parametro --}}
{{ old('nombre') }}                {{-- Valor anterior del formulario --}}
{{ old('nombre', $curso->nombre) }} {{-- Anterior o valor por defecto --}}
{{ session('mensaje') }}           {{-- Dato flash de sesion --}}
{{ url('/about') }}                {{-- URL absoluta --}}
```

---

## 8. Formularios y seguridad

### Proteccion CSRF

```
QUE ES CSRF (Cross-Site Request Forgery):
Un atacante puede crear un formulario en su sitio que haga POST
a tu aplicacion. Si el usuario esta logueado, el ataque funciona.

Sitio malicioso                    Tu App Laravel
+------------------+               +------------------+
| <form action=    | -- POST -->   | /eliminar/5      |
|   "tu-app.com/   |               | Sin CSRF: EXITO! |
|   eliminar/5">   |               | Con CSRF: FALLA  |
+------------------+               +------------------+

SOLUCION: @csrf genera un token unico por sesion.
El middleware VerifyCsrfToken rechaza peticiones sin token valido.
```

### Formulario completo con seguridad

```html
<form action="{{ route('store') }}" method="POST">
    @csrf  {{-- Obligatorio: genera <input type="hidden" name="_token" value="..."> --}}

    <input type="text" name="nombre" value="{{ old('nombre') }}">
    @error('nombre')
        <span class="text-danger">{{ $message }}</span>
    @enderror

    <button type="submit">Guardar</button>
</form>
```

### Formulario para actualizar (PUT)

```html
<form action="{{ route('update', $curso->id) }}" method="POST">
    @csrf
    @method('PUT')  {{-- Simula PUT porque HTML solo soporta GET/POST --}}

    <input name="nombre" value="{{ old('nombre', $curso->nombre) }}">
    <button type="submit">Actualizar</button>
</form>
```

### Formulario para eliminar (DELETE)

```html
<form action="{{ route('destroy', $curso->id) }}" method="POST">
    @csrf
    @method('DELETE')

    <button type="submit" onclick="return confirm('Seguro?')">Eliminar</button>
</form>
```

---

## 9. Sistema de correos (Mail)

### Componentes del sistema de correo

```
+------------------+     +------------------+     +------------------+
| Controlador      | --> | Clase Mailable   | --> | Vista Blade      |
| Mail::to()->send |     | MensajeRecibido  |     | (HTML del email) |
| (quien envia)    |     | (que contiene)   |     | (como se ve)     |
+------------------+     +------------------+     +------------------+
                                                          |
                                                          v
                                                  +------------------+
                                                  | Servidor SMTP    |
                                                  | (como se envia)  |
                                                  +------------------+
```

### Estructura de un Mailable

```php
class MensajeRecibido extends Mailable
{
    public $msg; // Propiedades publicas = disponibles en la vista

    public function __construct($mensaje)
    {
        $this->msg = $mensaje;
    }

    public function envelope(): Envelope  // El "sobre": asunto, remitente
    {
        return new Envelope(subject: 'Mensaje Recibido');
    }

    public function content(): Content    // El "contenido": vista Blade
    {
        return new Content(view: 'emails.mensaje-recibido');
    }

    public function attachments(): array  // Archivos adjuntos
    {
        return [];
    }
}
```

### Enviar desde un controlador

```php
// Envio basico
Mail::to('destino@email.com')->send(new MensajeRecibido($datos));

// Con copia
Mail::to('destino@email.com')
    ->cc('copia@email.com')
    ->bcc('copia-oculta@email.com')
    ->send(new MensajeRecibido($datos));

// Envio asincrono (en segundo plano, mas rapido)
Mail::to('destino@email.com')->queue(new MensajeRecibido($datos));
```

### Configuracion en .env

```env
MAIL_MAILER=smtp
MAIL_HOST=smtp.gmail.com
MAIL_PORT=587
MAIL_USERNAME=tu_correo@gmail.com
MAIL_PASSWORD=tu_contrasenya_de_aplicacion
MAIL_ENCRYPTION=tls
MAIL_FROM_ADDRESS=tu_correo@gmail.com
MAIL_FROM_NAME="Cursos DGTIC"

# Para desarrollo (escribe correos en el log en vez de enviarlos):
MAIL_MAILER=log
```

---

## 10. Migraciones de base de datos

### Que son las migraciones
Las migraciones son como **control de versiones para la base de datos**. Permiten crear, modificar y compartir el esquema de la BD de forma reproducible.

### Crear una migracion

```bash
php artisan make:migration create_cursos_table
```

### Estructura de una migracion

```php
class CreateCursosTable extends Migration
{
    // UP: lo que se ejecuta al correr la migracion
    public function up(): void
    {
        Schema::create('cursos', function (Blueprint $table) {
            $table->id();                    // Columna 'id' autoincremental
            $table->string('nombre');         // VARCHAR(255)
            $table->text('objetivo');         // TEXT
            $table->string('modalidad');
            $table->integer('cupo');          // INTEGER
            $table->string('periodo');
            $table->string('horario');
            $table->string('dias');
            $table->string('salon');
            $table->timestamps();             // created_at y updated_at
        });
    }

    // DOWN: lo que se ejecuta al revertir la migracion
    public function down(): void
    {
        Schema::dropIfExists('cursos');
    }
}
```

### Tipos de columnas comunes

| Metodo | Tipo SQL | Descripcion |
|--------|----------|-------------|
| `$table->id()` | BIGINT UNSIGNED AUTO_INCREMENT | Clave primaria |
| `$table->string('nombre')` | VARCHAR(255) | Texto corto |
| `$table->string('nombre', 100)` | VARCHAR(100) | Texto con longitud |
| `$table->text('descripcion')` | TEXT | Texto largo |
| `$table->integer('cupo')` | INTEGER | Numero entero |
| `$table->float('precio')` | FLOAT | Numero decimal |
| `$table->boolean('activo')` | BOOLEAN | Verdadero/Falso |
| `$table->date('fecha')` | DATE | Fecha |
| `$table->dateTime('publicado')` | DATETIME | Fecha y hora |
| `$table->timestamps()` | DATETIME x2 | created_at + updated_at |

### Comandos de migracion

```bash
php artisan migrate              # Ejecutar migraciones pendientes
php artisan migrate:rollback     # Revertir ultima tanda de migraciones
php artisan migrate:reset        # Revertir TODAS las migraciones
php artisan migrate:fresh        # Borrar todo y re-ejecutar migraciones
php artisan migrate:status       # Ver estado de migraciones
```

---

## 11. Errores comunes

### Error 419: Token CSRF expirado o faltante
```blade
{{-- SOLUCION: agregar @csrf en TODOS los formularios POST/PUT/DELETE --}}
<form method="POST">
    @csrf   {{-- <-- No olvidar esto! --}}
    ...
</form>
```

### Error 405: Method Not Allowed
```php
// El verbo HTTP no coincide con la ruta definida
// ERROR: el formulario hace POST pero la ruta espera PUT
Route::put('/actualizar/{id}', ...);

// SOLUCION: usar @method('PUT') en el formulario
```

### Error "Add [campo] to fillable property"
```php
// SOLUCION: agregar el campo a $fillable en el modelo
protected $fillable = ['nombre', 'objetivo', 'campo_faltante'];
```

### Los datos del formulario no llegan al controlador
```html
<!-- PROBLEMA: falta el atributo name en el input -->
<input type="text" id="nombre">              <!-- MAL -->
<input type="text" id="nombre" name="nombre"> <!-- BIEN -->
```

### La validacion falla pero no se ven los errores
```blade
{{-- SOLUCION: mostrar errores en la vista --}}
@if ($errors->any())
    <ul>
        @foreach ($errors->all() as $error)
            <li>{{ $error }}</li>
        @endforeach
    </ul>
@endif

{{-- O por campo individual: --}}
@error('nombre')
    <span class="text-danger">{{ $message }}</span>
@enderror
```

### "Class not found" despues de crear un archivo
```bash
# SOLUCION: regenerar el autoload de Composer
composer dump-autoload
```

### Cambios en .env no se reflejan
```bash
# SOLUCION: limpiar la cache de configuracion
php artisan config:clear
php artisan cache:clear
```

---

## 12. Ejercicios de practica

### Ejercicio 1: Agregar validacion visual
Modifica `agregar.blade.php` para mostrar errores de validacion debajo de cada campo:
```blade
<input type="text" name="nombre" value="{{ old('nombre') }}"
       class="form-control @error('nombre') is-invalid @enderror">
@error('nombre')
    <div class="invalid-feedback">{{ $message }}</div>
@enderror
```

### Ejercicio 2: Agregar campo "descripcion"
1. Crear una migracion para agregar la columna
2. Agregar el campo a `$fillable` en el modelo
3. Agregar el input en los formularios de crear y editar
4. Mostrar la columna en la tabla de la vista principal
5. Agregar validacion en el controlador

### Ejercicio 3: Implementar el metodo show()
1. Crear una vista `detalle.blade.php` que muestre toda la informacion de un curso
2. Implementar el metodo `show()` en el controlador
3. Agregar la ruta `Route::get('/curso/{id}', ...)->name('show')`
4. Agregar un enlace "Ver" en la tabla de la vista principal

### Ejercicio 4: Usar Route::resource
Reemplaza todas las rutas CRUD individuales por una sola linea:
```php
Route::resource('cursos', CursoController::class);
```
Y ajusta los nombres de las rutas en las vistas.

### Ejercicio 5: Refactorizar con Mass Assignment
Reemplaza la asignacion campo por campo en `store()` y `update()` por:
```php
// store():
Curso::create($request->validated());

// update():
$curso = Curso::findOrFail($id);
$curso->update($request->validated());
```

### Ejercicio 6: Agregar busqueda
1. Agregar un campo de busqueda en la vista principal
2. En el controlador, filtrar cursos por nombre:
```php
$cursos = Curso::where('nombre', 'LIKE', "%{$request->buscar}%")->paginate(4);
```

### Ejercicio 7: Soft Deletes
En vez de eliminar permanentemente, implementar "borrado suave":
1. Agregar `use SoftDeletes;` en el modelo
2. Crear migracion para agregar columna `deleted_at`
3. Los registros "eliminados" no aparecen en consultas normales
4. Crear una vista para ver registros eliminados con `Curso::onlyTrashed()->get()`

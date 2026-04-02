<?php
/*
|==========================================================================
| web.php - Definicion de Rutas Web de la Aplicacion
|==========================================================================
|
| QUE ES EL ENRUTAMIENTO (ROUTING):
| Las rutas conectan las URLs con la logica de la aplicacion.
| Cuando un usuario visita una URL, Laravel busca la ruta que coincide
| y ejecuta el codigo asociado (controlador o closure).
|
| CICLO DE VIDA DE UNA PETICION:
|   +----------+     +------------+     +----------+     +---------+
|   | Navegador| --> | Middleware  | --> | Router   | --> | Control-|
|   | (URL)    |     | (CSRF,Auth)| --> | (web.php)| --> | ador    |
|   +----------+     +------------+     +----------+     +---------+
|
| TIPOS DE RUTAS POR VERBO HTTP:
| +---------------------------+------------------------------------------+
| | Metodo                    | Proposito                                |
| +---------------------------+------------------------------------------+
| | Route::get($uri, $accion) | Obtener/mostrar datos (lectura)         |
| | Route::post($uri, $accion)| Enviar datos (crear recurso)            |
| | Route::put($uri, $accion) | Actualizar recurso completo             |
| | Route::patch($uri, $accion)| Actualizar parcialmente                |
| | Route::delete($uri, $accion)| Eliminar recurso                     |
| +---------------------------+------------------------------------------+
|
| RUTAS CON NOMBRE (Named Routes):
| ->name('nombre') permite referenciar la ruta por nombre en vez de URL.
| Ventaja: si cambia la URL, el nombre sigue funcionando.
|   route('index')   genera: /
|   route('edit', 5) genera: /editar/5
|
| PARAMETROS DE RUTA:
| {id} captura un segmento de la URL y lo pasa como parametro:
|   Route::get('/editar/{id}', ...) -> /editar/5 -> $id = 5
|
| RUTAS RESOURCE (alternativa mas elegante a definir cada ruta):
|   Route::resource('cursos', CursoController::class);
|   Esto genera automaticamente las 7 rutas CRUD (index, create, store,
|   show, edit, update, destroy) con nombres y verbos correctos.
|
| ARCHIVOS DE RUTAS EN LARAVEL:
| - routes/web.php   -> rutas web (con sesion, CSRF, cookies)
| - routes/api.php   -> rutas API (sin estado, prefix /api)
| - routes/console.php -> comandos Artisan personalizados
|
*/

// Importa el orden de las rutas

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\CursoController;
use App\Http\Controllers\MensajesController;

/*
|--------------------------------------------------------------------------
| RUTA PRINCIPAL - Listado de cursos
|--------------------------------------------------------------------------
| Verbo: GET | URL: / | Controlador: CursoController@index
| Nombre: 'index' (para referenciar con route('index'))
|
| Esta es la pagina de inicio. Muestra la tabla con todos los cursos.
| El metodo index() del controlador obtiene los cursos paginados
| y retorna la vista 'principal'.
*/
Route::get('/', [CursoController::class,'index'])-> name('index');

/*
|--------------------------------------------------------------------------
| RUTA DE AVISOS - Vista estatica con Closure
|--------------------------------------------------------------------------
| Verbo: GET | URL: /avisos
|
| Ejemplo de ruta que usa un Closure (funcion anonima) en vez de controlador.
| Es util para paginas simples que no necesitan logica compleja.
| NOTA: no tiene nombre asignado, se accede solo por URL directa.
*/
Route::get('avisos', function () {
    return view('aviso');
});

/*
|--------------------------------------------------------------------------
| RUTAS CRUD PARA CURSOS
|--------------------------------------------------------------------------
|
| CREATE (mostrar formulario):
| Verbo: GET | URL: /agregar | Nombre: 'create'
| Muestra el formulario vacio para agregar un nuevo curso.
*/
//Para mostrar formulario de agregar un curso
Route::get('/agregar', [CursoController::class, 'create']) -> name('create');

/*
| STORE (guardar en BD):
| Verbo: POST | URL: /agregar | Nombre: 'store'
| Procesa los datos del formulario y crea el registro en la BD.
| NOTA: create y store comparten la misma URL (/agregar) pero
| difieren en el verbo HTTP (GET vs POST).
*/
//Para guardar un curso
Route::post('/agregar', [CursoController::class, 'store']) -> name('store');

/*
| EDIT (mostrar formulario de edicion):
| Verbo: GET | URL: /editar/{id} | Nombre: 'edit'
| {id} es un parametro de ruta que captura el ID del curso.
| Ejemplo: /editar/3 -> CursoController@edit con $id = 3
*/
//Para editar un curso
Route::get('/editar/{id}', [CursoController::class, 'edit']) -> name('edit');

/*
| UPDATE (actualizar en BD):
| Verbo: POST | URL: /actualizar/{id} | Nombre: 'update'
| Recibe los datos editados y actualiza el registro.
| NOTA: Idealmente deberia ser PUT o PATCH (convencion REST).
| Con Route::put() se usaria @method('PUT') en el formulario.
*/
//Para actualizar un curso
Route::post('/actualizar/{id}', [CursoController::class, 'update']) -> name('update');

/*
| DESTROY (eliminar):
| Verbo: DELETE | URL: /eliminar/{id} | Nombre: 'destroy'
| Elimina permanentemente el curso de la base de datos.
| Como HTML no soporta DELETE, el formulario usa @method('DELETE')
| para simular el verbo correcto.
*/
//Para eliminar un curso
Route::delete('/eliminar/{id}', [CursoController::class, 'destroy']) -> name('destroy');

/*
|--------------------------------------------------------------------------
| RUTAS DE CONTACTO
|--------------------------------------------------------------------------
|
| GET /contacto: Muestra el formulario de contacto (usa Closure)
| POST /contacto: Procesa el envio del correo (usa MensajesController)
|
| Mismo patron que create/store: GET muestra formulario, POST procesa datos.
*/
//Contacto
Route::get('/contacto', function () {
    return view('contacto');})->name('contacto');

//Para enviar un correo
Route::post('/contacto', [MensajesController::class, 'store']);

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider and all of them will
| be assigned to the "web" middleware group. Make something great!
|
 */

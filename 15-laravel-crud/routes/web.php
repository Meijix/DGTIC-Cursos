<?php
// Importa el orden de las rutas

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\CursoController;
use App\Http\Controllers\MensajesController;

Route::get('/', [CursoController::class,'index'])-> name('index');

Route::get('avisos', function () {
    return view('aviso');
});
//Para mostrar formulario de agregar un curso
Route::get('/agregar', [CursoController::class, 'create']) -> name('create');
//Para guardar un curso
Route::post('/agregar', [CursoController::class, 'store']) -> name('store');

//Para editar un curso
Route::get('/editar/{id}', [CursoController::class, 'edit']) -> name('edit');
//Para actualizar un curso
Route::post('/actualizar/{id}', [CursoController::class, 'update']) -> name('update');
//Para eliminar un curso
Route::delete('/eliminar/{id}', [CursoController::class, 'destroy']) -> name('destroy');


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

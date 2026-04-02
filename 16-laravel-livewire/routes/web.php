<?php
/*
|==========================================================================
| web.php - Rutas de la Aplicacion Livewire
|==========================================================================
|
| MINIMALISMO EN LAS RUTAS CON LIVEWIRE:
| A diferencia del Modulo 15 que necesitaba 7+ rutas para el CRUD,
| con Livewire solo necesitamos UNA ruta. Toda la logica CRUD se
| maneja dentro del componente Livewire sin cambiar de URL.
|
| COMPARACION DE RUTAS:
|
|   MODULO 15 (Tradicional) - 7+ rutas:
|   Route::get('/', [CursoController::class, 'index'])->name('index');
|   Route::get('/agregar', [CursoController::class, 'create'])->name('create');
|   Route::post('/agregar', [CursoController::class, 'store'])->name('store');
|   Route::get('/editar/{id}', [CursoController::class, 'edit'])->name('edit');
|   Route::post('/actualizar/{id}', [CursoController::class, 'update'])->name('update');
|   Route::delete('/eliminar/{id}', [CursoController::class, 'destroy'])->name('destroy');
|   Route::get('/contacto', function () { return view('contacto'); });
|   Route::post('/contacto', [MensajesController::class, 'store']);
|
|   MODULO 16 (Livewire) - 1 ruta:
|   Route::get('/', function () { return view('principal'); });
|
| POR QUE SOLO UNA RUTA:
| Livewire maneja la interactividad via AJAX. El usuario nunca
| "navega" a otra URL. Todo sucede en la misma pagina:
| - Crear un curso -> AJAX al servidor -> se actualiza la vista
| - Editar un curso -> AJAX -> se muestra el formulario de edicion
| - Eliminar -> AJAX -> desaparece de la lista
|
| Livewire registra automaticamente sus propias rutas internas
| (como /livewire/message/{component}) para manejar la comunicacion.
|
| ALTERNATIVA: Ruta directa a componente (Livewire 3):
|   Route::get('/', CursoComponent::class);
|   Esto renderiza el componente directamente sin necesidad de
|   una vista intermedia (principal.blade.php).
|
*/

use Illuminate\Support\Facades\Route;

/*
|--------------------------------------------------------------------------
| RUTA UNICA - Carga la vista que contiene el componente Livewire
|--------------------------------------------------------------------------
| Esta unica ruta carga 'principal.blade.php', que a su vez incluye
| el componente Livewire con @livewire('curso-component').
| Todo el CRUD se maneja dentro del componente sin rutas adicionales.
*/
Route::get('/', function () {
    return view('principal');
});

<?php
/**
 * ==========================================================================
 * MODULO 17 - PROYECTO DE EVALUACION: Archivo de Rutas Web
 * ==========================================================================
 *
 * PROPOSITO DE ESTE ARCHIVO:
 * Define TODAS las URLs (rutas) de la aplicacion web y que componente
 * o controlador responde a cada una.
 *
 * QUE ES UNA RUTA?
 * Una ruta conecta una URL con una accion:
 *   URL: /customers         ->  Accion: Mostrar componente Customers
 *   URL: /customers/create  ->  Accion: Mostrar componente CreateCustomer
 *   URL: /customers/5       ->  Accion: Mostrar componente ViewCustomer (cliente #5)
 *
 * VERBOS HTTP (Metodos):
 *   Route::get()    -> Para OBTENER/MOSTRAR informacion (leer)
 *   Route::post()   -> Para ENVIAR/CREAR informacion (escribir)
 *   Route::put()    -> Para ACTUALIZAR informacion completa
 *   Route::patch()  -> Para ACTUALIZAR informacion parcial
 *   Route::delete() -> Para ELIMINAR informacion
 *
 * NOTA: En este proyecto, TODAS las rutas son GET porque Livewire
 * maneja las operaciones POST/DELETE internamente via AJAX.
 * No necesitamos Route::post() ni Route::delete() cuando usamos Livewire.
 *
 * RUTAS CON LIVEWIRE vs RUTAS CON CONTROLADORES:
 *
 *   Con Livewire (este proyecto):
 *   Route::get('/customers', Customers::class);
 *   -> La URL apunta DIRECTAMENTE al componente Livewire
 *   -> El componente actua como pagina completa (full-page component)
 *
 *   Con Controladores (enfoque tradicional - comentado abajo):
 *   Route::get('/customers', [CustomerController::class, 'index']);
 *   -> La URL apunta a un metodo del controlador
 *   -> El controlador decide que vista mostrar
 *
 * CRITERIO DE EVALUACION: Rutas bien organizadas
 * - Rutas RESTful con nombres claros
 * - Rutas con nombre (->name()) para facilitar la generacion de URLs
 * - Route Model Binding en las rutas con parametros
 */

//use App\Http\Controllers\CustomerController;

use App\Http\Livewire\Customers;
use App\Http\Livewire\CreateCustomer;
use App\Http\Livewire\EditCustomer;
use App\Http\Livewire\ViewCustomer;
use Illuminate\Support\Facades\Route;


/**
 * RUTA PRINCIPAL: Pagina de bienvenida.
 *
 * Route::get('/', function() { ... })
 * - '/' es la URL raiz (ej: http://localhost:8000/)
 * - function() { return view('welcome'); } es un CLOSURE (funcion anonima)
 * - view('welcome') busca resources/views/welcome.blade.php
 * - ->name('principal') le da un nombre a la ruta para referencia
 */
Route::get('/', function () {
    return view('welcome');})->name('principal');

/**
 * RUTAS DEL CRUD DE CLIENTES:
 * Cada ruta apunta a un componente Livewire como pagina completa.
 *
 * ORDEN IMPORTANTE DE LAS RUTAS:
 * /customers/create DEBE ir ANTES de /customers/{customer}
 * porque si fuera al reves, Laravel interpretaria "create" como un {customer} ID.
 *
 * ANATOMIA DE UNA RUTA:
 *   Route::get('/customers', Customers::class)->name('customers');
 *   |          |              |                      |
 *   |          |              |                      +-- Nombre para route()
 *   |          |              +-- Componente que responde
 *   |          +-- URL que el usuario visita
 *   +-- Metodo HTTP (GET = mostrar/leer)
 */

// LISTAR todos los clientes
Route::get('/customers', Customers::class)->name('customers');

// CREAR un nuevo cliente (formulario)
Route::get('/customers/create', CreateCustomer::class)->name('create');

/**
 * VER detalle de un cliente.
 *
 * ROUTE MODEL BINDING:
 * {customer} es un parametro dinamico. Si la URL es /customers/5:
 * - Laravel toma el valor "5"
 * - Busca Customer::findOrFail(5)
 * - Lo pasa al metodo mount() del componente ViewCustomer
 *
 * El nombre del parametro {customer} DEBE coincidir con:
 * 1. El nombre del modelo en minusculas (Customer -> customer)
 * 2. El nombre del parametro en mount(Customer $customer)
 *
 * Si no coinciden, Laravel no hara la resolucion automatica.
 */
Route::get('/customers/{customer}', ViewCustomer::class)->name('view');

/**
 * EDITAR un cliente existente.
 *
 * La URL /customers/{customer}/edit sigue la convencion RESTful:
 *   /recurso/{id}       -> Ver detalle
 *   /recurso/{id}/edit  -> Formulario de edicion
 *   /recurso/create     -> Formulario de creacion
 *
 * Laravel resuelve {customer} igual que en la ruta de ver.
 */
Route::get('/customers/{customer}/edit', EditCustomer::class)->name('edit');

/*
//Crear un cliente
Route::get('/customers/create', CreateCustomer::class)->name('create')
//Registar un cliente
//Route::post('/customers', [CustomerController::class, 'store'])->name('customers.store');
//Listar clientes
Route::get('/customers', Customers::class);
//Ver un cliente
Route::get('/customers/{customer}', ViewCustomer::class);
//Tengo que crear el controlador de Customers
Route::get('/customers/{id}', [CustomerController::class, 'show'])->name('customers.show');

//Borrar un cliente
Route::delete('/customers/{id}', [CustomerController::class, 'destroy'])->name('customers.destroy');

//Editar un cliente
Route::get('/customers/{id}', [CustomerController::class, 'edit'])->name('customers.edit');
//Actualizar un cliente
Route::post('/customers/{id}', [CustomerController::class, 'update'])->name('customers.update');


 */
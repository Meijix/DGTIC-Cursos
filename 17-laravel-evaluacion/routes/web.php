<?php

//use App\Http\Controllers\CustomerController;

use App\Http\Livewire\Customers;
use App\Http\Livewire\CreateCustomer;
use App\Http\Livewire\EditCustomer;
use App\Http\Livewire\ViewCustomer;
use Illuminate\Support\Facades\Route;


Route::get('/', function () {
    return view('welcome');})->name('principal');

Route::get('/customers', Customers::class)->name('customers');
Route::get('/customers/create', CreateCustomer::class)->name('create');
Route::get('/customers/{customer}', ViewCustomer::class)->name('view');
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
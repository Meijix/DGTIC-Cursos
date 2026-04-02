<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Customer;

class CustomerController extends Controller
{
    /* public function edit($id)
    {
        $customer = Customer::find($id);
        return view('customers.edit', compact('customer'));
    }
    
    public function destroy($id)
    {
        $customer = Customer::find($id);
        $customer->delete();


        return redirect(route('principal'))->with('success', 'Cliente eliminado correctamente.');
    } */

}

<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
USE Illuminate\Support\Facades\Mail;
use App\Mail\MensajeRecibido;

class MensajesController extends Controller
{
    public function store(){

        $message = request()->validate([
            'nombre' => 'required',
            'email' => 'required|email',
            'asunto' => 'required',
            'mensaje' => 'required|min:3'
        ],[
            'nombre.required' => __('Se requiere el nombre'),
            'email.required' =>__('Se requiere el correo'),
            'asunto.required' =>__('Se requiere el asunto'),
            'mensaje.required' => __('Se requiere el mensaje a enviar'),
        ]);
        Mail::to('natalia.mejbau@gmail.com')->cc($message['email'])->send(new MensajeRecibido($message));

        return redirect()->route('index');//->with('info', 'Mensaje enviado');
    }

}

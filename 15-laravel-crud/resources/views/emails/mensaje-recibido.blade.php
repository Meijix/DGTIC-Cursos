@extends('plantilla')
@section('contenido')
<p>Recibiste un mensaje de: {{$msg['nombre']}} - {{$msg['email']}}</p>
<p><strong>Asunto:</strong> {{$msg['asunto']}}</p>
<p>El mensaje es: {{$msg['mensaje']}}</p>
@endsection
<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Curso;

class CursoController extends Controller
{
    /**
     * Display a listing of the resource.
     */
    public function index()
    {
        $cursos = Curso::orderBy('id')-> paginate(4);
        return view('principal', compact('cursos'));
    }

    /**
     * Show the form for creating a new resource.
     */
    public function create()
    {
        return view('agregar');
    }

    /**
     * Store a newly created resource in storage.
     */
    public function store(Request $request)
    {
        $this->validate($request, [
            'nombre' => 'required',
            'objetivo' => 'required',
            'modalidad' => 'required',
            'cupo' => 'required',
            'periodo' => 'required',
            'horario' => 'required',
            'dias' => 'required',
            'salon' => 'required'
        ]);

        $curso = new Curso;
        $curso->nombre = $request->nombre;
        $curso->objetivo = $request->objetivo;
        $curso->modalidad = $request->modalidad;
        $curso->cupo = $request->cupo;
        $curso->periodo = $request->periodo;
        $curso->horario = $request->horario;
        $curso->dias = $request->dias;
        $curso->salon = $request->salon;
        $curso->save();

        return redirect(route('index'))->with('mensaje', 'El curso fue agregado con éxito');
    }

    /**
     * Display the specified resource.
     */
    public function show(string $id)
    {
        //
    }

    /**
     * Show the form for editing the specified resource.
     */
    public function edit(string $id)
    {
        $curso = Curso::find($id);
        return view('editar', compact('curso'));        
    }

    /**
     * Update the specified resource in storage.
     */
    public function update(Request $request, string $id)
    {
        $this->validate($request, [
            'nombre' => 'required',
            'objetivo' => 'required',
            'modalidad' => 'required',
            'cupo' => 'required',
            'periodo' => 'required',
            'horario' => 'required',
            'dias' => 'required',
            'salon' => 'required'
        ]);

        $curso = Curso::find($id);
        $curso->nombre = $request->nombre;
        $curso->objetivo = $request->objetivo;
        $curso->modalidad = $request->modalidad;
        $curso->cupo = $request->cupo;
        $curso->periodo = $request->periodo;
        $curso->horario = $request->horario;
        $curso->dias = $request->dias;
        $curso->salon = $request->salon;
        $curso->save();

        return redirect(route('index'))->with('mensaje', 'El curso fue actualizado con éxito');
    }


    /**
     * Remove the specified resource from storage.
     */
    public function destroy(string $id)
    {
        Curso::destroy($id);
        return redirect(route('index'))->with('mensaje', 'El curso fue eliminado con éxito');
    }
}

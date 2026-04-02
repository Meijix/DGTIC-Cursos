<?php

namespace App\Livewire;

use Livewire\Component;
use App\Models\Curso;

class CursoComponent extends Component
{
    public $view = 'create';
    public $nombre, $objetivo, $modalidad, $cupo, $periodo, $horario, $dias, $salon;


    public function render()
    {
        return view('livewire.curso-component');
    }

    public function store(){
        $this->validate([
            'nombre' => 'required',
            'objetivo' => 'required',
            'modalidad' => 'required',
            'cupo' => 'required',
            'periodo' => 'required',
            'horario' => 'required',
            'dias' => 'required',
            'salon' => 'required',
        ]);
        Curso::create([
            'nombre' => $this->nombre,
            'objetivo' => $this->objetivo,
            'modalidad' => $this->modalidad,
            'cupo' => $this->cupo,
            'periodo' => $this->periodo,
            'horario' => $this->horario,
            'dias' => $this->dias,
            'salon' => $this->salon,
        ]);
    }
}

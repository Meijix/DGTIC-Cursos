<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class Curso extends Model
{
    protected $table = 'cursos';
    //protected $primaryKey = 'id';
    protected $fillable = ['nombre', 'objetivo', 'modalidad', 'cupo', 'periodo', 'horario', 'dias', 'salon'];
    //public $timestamps = false;
}

<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    public function up(): void
    {
        Schema::create('cursos', function (Blueprint $table) {
            $table->id();
            $table->string('nombre');
            $table->text('objetivo')->nullable();
            $table->string('modalidad')->nullable();
            $table->integer('cupo')->nullable();
            $table->string('periodo')->nullable();
            $table->string('horario')->nullable();
            $table->string('dias')->nullable();
            $table->string('salon')->nullable();
            $table->timestamps();
        });
    }

    public function down(): void
    {
        Schema::dropIfExists('cursos');
    }
};

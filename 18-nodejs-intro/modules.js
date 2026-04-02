/**
 * ==========================================================================
 * MODULO 18 - INTRODUCCION A NODE.JS: Ejemplo de Modulos
 * ==========================================================================
 *
 * PROPOSITO DE ESTE ARCHIVO:
 * Demostrar como funcionan los MODULOS en Node.js.
 * Un modulo es un archivo JavaScript que exporta funcionalidad
 * para ser usada en otros archivos.
 *
 * SISTEMAS DE MODULOS EN NODE.JS:
 *
 * 1. COMMONJS (el sistema por defecto en Node.js):
 *    - Usa require() para importar
 *    - Usa module.exports para exportar
 *    - Carga SINCRONA (bloqueante)
 *    - Ejemplo:
 *        const fs = require('fs');           // Importar modulo nativo
 *        const express = require('express'); // Importar paquete npm
 *        const utils = require('./utils');   // Importar archivo local
 *
 * 2. ES MODULES (estandar moderno de JavaScript):
 *    - Usa import/export
 *    - Carga ASINCRONA
 *    - Requiere "type": "module" en package.json o extension .mjs
 *    - Ejemplo:
 *        import fs from 'fs';
 *        import express from 'express';
 *        import { miFuncion } from './utils.js';
 *
 * TIPOS DE MODULOS QUE PUEDES IMPORTAR:
 *
 *   1. MODULOS NATIVOS (built-in): Vienen con Node.js, no necesitan instalacion
 *      - 'os'      -> Informacion del sistema operativo
 *      - 'fs'      -> Sistema de archivos (leer/escribir archivos)
 *      - 'path'    -> Manipulacion de rutas de archivos
 *      - 'http'    -> Crear servidores HTTP basicos
 *      - 'crypto'  -> Funciones criptograficas
 *      - 'readline' -> Leer input del usuario en la terminal
 *
 *   2. PAQUETES NPM: Se instalan con npm install
 *      - 'express'  -> Framework web
 *      - 'axios'    -> Cliente HTTP
 *      - 'dotenv'   -> Variables de entorno
 *      - 'openai'   -> API de OpenAI
 *
 *   3. MODULOS LOCALES: Archivos de tu proyecto
 *      - './utils'  -> Importar utils.js del mismo directorio
 *      - '../config' -> Importar del directorio padre
 *
 * NOTA SOBRE ESTE ARCHIVO:
 * Tiene un error de sintaxis en la linea de require.
 * La forma correcta seria:
 *   const os = require('node:os');
 *
 * El prefijo 'node:' es una convencion moderna (Node.js 14+) para
 * distinguir modulos nativos de paquetes npm:
 *   require('node:os')  -> SIEMPRE el modulo nativo 'os'
 *   require('os')       -> Podria ser un paquete npm llamado 'os'
 */

const require = ('node:os')
/**
 * ERROR DE SINTAXIS:
 * Esta linea tiene un error. 'require' es una funcion global de Node.js
 * y NO deberia reasignarse con const.
 *
 * Lo correcto seria:
 *   const os = require('node:os');
 *
 * Esto importaria el modulo 'os' que proporciona informacion del sistema:
 *   os.platform()    -> 'darwin' (macOS), 'linux', 'win32'
 *   os.cpus()        -> Informacion de los procesadores
 *   os.totalmem()    -> Memoria RAM total en bytes
 *   os.freemem()     -> Memoria RAM disponible
 *   os.hostname()    -> Nombre del equipo
 *   os.homedir()     -> Directorio home del usuario
 *   os.tmpdir()      -> Directorio temporal
 *   os.uptime()      -> Tiempo encendido en segundos
 *
 * EJEMPLO CORRECTO:
 *   const os = require('node:os');
 *   console.log('Plataforma:', os.platform());
 *   console.log('Memoria total:', os.totalmem() / 1024 / 1024 / 1024, 'GB');
 *   console.log('CPUs:', os.cpus().length, 'nucleos');
 *   console.log('Usuario:', os.userInfo().username);
 */

console.log('Información del sistema:');
/**
 * console.log(): La forma basica de mostrar informacion en Node.js.
 *
 * METODOS DE CONSOLE:
 *   console.log()    -> Informacion general (stdout)
 *   console.error()  -> Errores (stderr)
 *   console.warn()   -> Advertencias
 *   console.table()  -> Muestra datos en formato tabla
 *   console.time()   -> Inicia un cronometro
 *   console.timeEnd() -> Detiene el cronometro y muestra el tiempo
 *
 * EJEMPLO COMPLETO (si el require estuviera correcto):
 *   const os = require('node:os');
 *   console.log('Plataforma:', os.platform());
 *   console.log('Arquitectura:', os.arch());
 *   console.log('Hostname:', os.hostname());
 *   console.table({
 *     'Memoria Total': (os.totalmem() / 1e9).toFixed(2) + ' GB',
 *     'Memoria Libre': (os.freemem() / 1e9).toFixed(2) + ' GB',
 *     'Nucleos CPU': os.cpus().length,
 *     'Uptime': (os.uptime() / 3600).toFixed(1) + ' horas'
 *   });
 */

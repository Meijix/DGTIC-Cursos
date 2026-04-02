# Modulo 18: Introduccion a Node.js

## Objetivo del Modulo

Aprender los fundamentos de **Node.js** para crear servidores web y APIs REST.
Este modulo marca la transicion de PHP/Laravel (modulos 13-17) a JavaScript
en el lado del servidor.

---

## 1. Que es Node.js y Por Que Importa

### Definicion

Node.js es un **entorno de ejecucion** para JavaScript fuera del navegador.
Usa el motor V8 de Google Chrome para ejecutar JavaScript en el servidor.

### Antes y despues de Node.js

```
ANTES (hasta 2009):
  Navegador: JavaScript (frontend)
  Servidor:  PHP, Java, Python, Ruby (backend)
  Resultado: Los desarrolladores web necesitaban DOS lenguajes

DESPUES (con Node.js, 2009+):
  Navegador: JavaScript (frontend)
  Servidor:  JavaScript con Node.js (backend)
  Resultado: UN SOLO lenguaje para todo (Full Stack JavaScript)
```

### El ecosistema npm

npm (Node Package Manager) es el **mayor registro de paquetes** del mundo:
- Mas de 2 millones de paquetes disponibles
- Se instalan con: `npm install nombre-paquete`
- Se definen en `package.json`
- Se guardan en la carpeta `node_modules/`

```bash
# Comandos npm esenciales:
npm init -y              # Crear proyecto nuevo
npm install express      # Instalar un paquete
npm install -D nodemon   # Instalar solo para desarrollo
npm start                # Ejecutar script "start"
npm test                 # Ejecutar script "test"
npm run dev              # Ejecutar script personalizado
```

---

## 2. El Event Loop (Bucle de Eventos)

### El secreto de Node.js: Non-Blocking I/O

Node.js es **single-threaded** (un solo hilo) pero maneja miles de conexiones
simultaneas gracias al Event Loop.

### Diagrama del Event Loop

```
  ┌───────────────────────────────────────────────┐
  │                  CALL STACK                    │
  │            (Pila de ejecucion)                 │
  │                                                │
  │  Aqui se ejecuta el codigo SINCRONICO:         │
  │  - console.log()                               │
  │  - operaciones matematicas                     │
  │  - asignacion de variables                     │
  └────────────────────┬──────────────────────────┘
                       │
                       ▼  Si hay operacion async (fetch, fs, setTimeout...)
  ┌───────────────────────────────────────────────┐
  │              NODE.JS APIs                      │
  │         (Delegacion al S.O.)                   │
  │                                                │
  │  Node.js delega operaciones al sistema:        │
  │  - Leer archivos (libuv)                       │
  │  - Peticiones HTTP (libuv)                     │
  │  - Timers (setTimeout, setInterval)            │
  │  - DNS lookup                                  │
  └────────────────────┬──────────────────────────┘
                       │
                       ▼  Cuando la operacion termina...
  ┌──────────────────────────┬────────────────────┐
  │    MICROTASK QUEUE       │  CALLBACK QUEUE    │
  │   (Alta prioridad)      │  (Baja prioridad)  │
  │                          │                    │
  │  - Promise.then()        │  - setTimeout()    │
  │  - async/await           │  - setInterval()   │
  │  - process.nextTick()    │  - I/O completado  │
  │                          │  - eventos         │
  └──────────┬───────────────┴───────┬────────────┘
             │                       │
             └───────────┬───────────┘
                         │
                         ▼
  ┌───────────────────────────────────────────────┐
  │                EVENT LOOP                      │
  │         (Bucle infinito)                       │
  │                                                │
  │  1. Esta vacio el Call Stack? ────── No ──┐    │
  │     │                                     │    │
  │    Si                                     │    │
  │     │                                     │    │
  │  2. Hay microtasks? ──── Si ──> Ejecutar  │    │
  │     │                                     │    │
  │    No                                     │    │
  │     │                                     │    │
  │  3. Hay callbacks? ──── Si ──> Ejecutar   │    │
  │     │                                     │    │
  │  4. Volver al paso 1 <───────────────────┘    │
  └───────────────────────────────────────────────┘
```

### Ejemplo practico

```javascript
console.log('1. Inicio');

setTimeout(() => {
  console.log('2. Timeout (callback queue)');
}, 0);

Promise.resolve().then(() => {
  console.log('3. Promise (microtask queue)');
});

console.log('4. Fin');

// Salida:
// 1. Inicio
// 4. Fin
// 3. Promise (microtask queue)     <-- Microtasks primero
// 2. Timeout (callback queue)      <-- Callbacks despues
```

---

## 3. Modulos en Node.js

### CommonJS (require / module.exports)

```javascript
// ===== EXPORTAR (archivo: utils.js) =====
function sumar(a, b) {
  return a + b;
}

function restar(a, b) {
  return a - b;
}

// Exportar funciones individuales:
module.exports = { sumar, restar };

// O exportar una sola cosa:
// module.exports = sumar;


// ===== IMPORTAR (archivo: app.js) =====
const { sumar, restar } = require('./utils');  // Archivo local (con ./)
const express = require('express');            // Paquete npm (sin ./)
const fs = require('fs');                      // Modulo nativo (sin ./)
const os = require('node:os');                 // Modulo nativo (con prefijo node:)
```

### ES Modules (import / export)

```javascript
// ===== EXPORTAR (archivo: utils.mjs o con "type":"module") =====
export function sumar(a, b) {
  return a + b;
}

export default function restar(a, b) {
  return a - b;
}


// ===== IMPORTAR =====
import restar, { sumar } from './utils.js';  // NOTA: extension .js obligatoria
import express from 'express';
```

### Modulos nativos mas importantes

| Modulo | Proposito | Ejemplo |
|--------|-----------|---------|
| `fs` | Sistema de archivos | `fs.readFileSync('archivo.txt')` |
| `path` | Rutas de archivos | `path.join(__dirname, 'data')` |
| `http` | Servidor HTTP basico | `http.createServer(...)` |
| `os` | Info del sistema | `os.platform()`, `os.cpus()` |
| `crypto` | Criptografia | `crypto.randomUUID()` |
| `readline` | Input del usuario | `rl.question('Nombre:', ...)` |
| `child_process` | Ejecutar comandos | `exec('ls -la')` |
| `events` | Emisor de eventos | `emitter.on('data', ...)` |

---

## 4. Express.js: Creando Servidores Web

### Estructura basica de un servidor Express

```javascript
const express = require('express');
const app = express();

// Middleware (se ejecuta en TODAS las peticiones)
app.use(express.json());       // Parsear JSON
app.use(express.static('public')); // Servir archivos estaticos

// Rutas
app.get('/', (req, res) => {
  res.send('Hola Mundo');
});

app.get('/api/users', (req, res) => {
  res.json([{ id: 1, name: 'Ana' }]);
});

app.post('/api/users', (req, res) => {
  const newUser = req.body;
  res.status(201).json(newUser);
});

// Iniciar servidor
app.listen(3000, () => {
  console.log('Servidor en http://localhost:3000');
});
```

### Pipeline de Middleware

```
Peticion HTTP
    │
    ▼
┌─────────────────┐
│  express.json() │  <-- Parsea el body JSON
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   cors()        │  <-- Permite peticiones cross-origin
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  morgan()       │  <-- Log de la peticion
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Tu ruta        │  <-- Tu codigo (req, res)
│  app.get(...)   │
└────────┬────────┘
         │
         ▼
  Respuesta HTTP
```

### Metodos HTTP y su uso

```
GET     /api/customers          -> Listar todos los clientes
GET     /api/customers/5        -> Obtener cliente con ID 5
POST    /api/customers          -> Crear nuevo cliente
PUT     /api/customers/5        -> Actualizar cliente completo
PATCH   /api/customers/5        -> Actualizar campos parciales
DELETE  /api/customers/5        -> Eliminar cliente

ANALOGIA CON LARAVEL:
  Express:  app.get('/customers', (req, res) => {...})
  Laravel:  Route::get('/customers', [Controller::class, 'index'])
```

---

## 5. Programacion Asincrona: La Evolucion

### De Callbacks a Async/Await

```javascript
// ═══════════════════════════════════════════
// NIVEL 1: CALLBACKS (2009-2015)
// Problema: "Callback Hell" (piramide de la muerte)
// ═══════════════════════════════════════════
fs.readFile('archivo1.txt', (err, data1) => {
  if (err) return console.error(err);
  fs.readFile('archivo2.txt', (err, data2) => {
    if (err) return console.error(err);
    fs.readFile('archivo3.txt', (err, data3) => {
      if (err) return console.error(err);
      console.log(data1, data2, data3);
      // ... y asi sucesivamente (ilegible!)
    });
  });
});

// ═══════════════════════════════════════════
// NIVEL 2: PROMISES (2015+)
// Mejor: encadenamiento con .then()
// ═══════════════════════════════════════════
fetch('https://api.example.com/users')
  .then(response => response.json())
  .then(users => {
    console.log(users);
    return fetch(`/api/users/${users[0].id}`);
  })
  .then(response => response.json())
  .then(user => console.log(user))
  .catch(error => console.error(error));

// ═══════════════════════════════════════════
// NIVEL 3: ASYNC/AWAIT (2017+)
// El mejor: se lee como codigo sincronico
// ═══════════════════════════════════════════
async function obtenerUsuarios() {
  try {
    const response = await fetch('https://api.example.com/users');
    const users = await response.json();
    console.log(users);

    const detailResponse = await fetch(`/api/users/${users[0].id}`);
    const user = await detailResponse.json();
    console.log(user);
  } catch (error) {
    console.error(error);
  }
}
```

---

## 6. AWS: Servicios en la Nube

### Servicios AWS mencionados en este modulo

```
┌─────────────────────────────────────────────────────────────┐
│                    AMAZON WEB SERVICES                      │
├─────────────────────┬───────────────────────────────────────┤
│  DynamoDB           │  Base de datos NoSQL                  │
│                     │  - Sin esquema fijo                   │
│                     │  - Escala automaticamente             │
│                     │  - Respuesta en milisegundos          │
│                     │  - Modelo de pago por uso             │
├─────────────────────┼───────────────────────────────────────┤
│  Lambda             │  Funciones serverless                 │
│                     │  - Ejecuta codigo sin servidores      │
│                     │  - Se activa por eventos              │
│                     │  - Paga solo por el tiempo de uso     │
├─────────────────────┼───────────────────────────────────────┤
│  API Gateway        │  Puerta de entrada para APIs          │
│                     │  - Enruta peticiones HTTP             │
│                     │  - Autenticacion y autorizacion       │
│                     │  - Rate limiting                      │
├─────────────────────┼───────────────────────────────────────┤
│  S3                 │  Almacenamiento de archivos           │
│                     │  - Imagenes, videos, PDFs             │
│                     │  - Hosting de sitios estaticos        │
├─────────────────────┼───────────────────────────────────────┤
│  EC2                │  Servidores virtuales                 │
│                     │  - Como tu propia computadora en nube │
│                     │  - Tu controlas el SO, software, etc. │
└─────────────────────┴───────────────────────────────────────┘
```

### DynamoDB vs MySQL

```
MySQL (SQL Relacional):          DynamoDB (NoSQL):
┌────┬───────┬────────┐          {
│ id │ name  │ email  │            "id": "abc123",
├────┼───────┼────────┤            "name": "Ana",
│ 1  │ Ana   │ a@...  │            "email": "a@...",
│ 2  │ Bob   │ b@...  │            "pedidos": [1, 2, 3],  <-- Flexible!
└────┴───────┴────────┘            "metadata": { ... }     <-- Anidado!
Esquema FIJO                     }
Tablas y relaciones              Sin esquema fijo
JOIN entre tablas                Documentos auto-contenidos
Mejor para datos estructurados   Mejor para datos variables
```

---

## 7. Variables de Entorno y Seguridad

### El archivo .env

```bash
# .env - NUNCA subir a Git!
AWS_REGION=us-east-1
AWS_ACCESS_KEY_ID=AKIA...
AWS_SECRET_ACCESS_KEY=wJalr...
DYNAMO_TABLE=MiTabla
OPENAI_API_KEY=sk-proj-...
PORT=3000
DATABASE_URL=postgres://user:pass@host:5432/db
```

### Configuracion de .gitignore

```
# .gitignore
node_modules/
.env
.env.local
.env.production
*.log
```

### Reglas de seguridad

```
NUNCA:
  ✗ Poner claves API directamente en el codigo
  ✗ Hacer commit del archivo .env
  ✗ Compartir claves por chat o email
  ✗ Usar la misma clave en desarrollo y produccion

SIEMPRE:
  ✓ Usar variables de entorno (.env + dotenv)
  ✓ Agregar .env a .gitignore
  ✓ Crear un .env.example con las variables (sin valores)
  ✓ Rotar claves si se exponen accidentalmente
  ✓ Usar secretos del CI/CD para produccion (GitHub Secrets, etc.)
```

---

## 8. REST API: Diseno de APIs

### Principios REST

```
REST = Representational State Transfer

Principios:
1. RECURSOS: Todo es un recurso (users, products, orders)
2. URLs DESCRIPTIVAS: /api/users, /api/products/5
3. VERBOS HTTP: GET (leer), POST (crear), PUT (actualizar), DELETE (eliminar)
4. RESPUESTAS JSON: Formato estandar para intercambiar datos
5. SIN ESTADO: Cada peticion contiene toda la informacion necesaria
```

### Diseno de endpoints

```
Verbo    Endpoint                Accion             Status Code
───────  ──────────────────────  ─────────────────  ───────────
GET      /api/customers          Listar todos       200
GET      /api/customers/5        Obtener uno        200 / 404
POST     /api/customers          Crear nuevo        201 / 400
PUT      /api/customers/5        Actualizar         200 / 404
DELETE   /api/customers/5        Eliminar           200 / 404

Respuesta JSON tipica:
{
  "success": true,
  "data": { "id": 5, "name": "Ana", "email": "ana@mail.com" },
  "message": "Cliente creado exitosamente"
}

Respuesta de error:
{
  "success": false,
  "error": "Datos invalidos",
  "details": { "email": "El email es obligatorio" }
}
```

---

## 9. Node.js vs PHP: Tabla Comparativa

Para estudiantes que vienen de los modulos 13-17 (Laravel/PHP):

| Aspecto | PHP / Laravel | Node.js / Express |
|---------|---------------|-------------------|
| **Lenguaje** | PHP | JavaScript |
| **Gestor de paquetes** | Composer | npm |
| **Framework web** | Laravel (full-stack) | Express (minimalista) |
| **ORM** | Eloquent | Sequelize, Prisma, Mongoose |
| **Plantillas** | Blade | EJS, Pug, Handlebars |
| **Base de datos** | MySQL/PostgreSQL | MongoDB, DynamoDB, MySQL |
| **Servidor** | Apache/Nginx + PHP-FPM | Node.js ES el servidor |
| **Modelo de ejecucion** | Multi-thread | Single-thread + Event Loop |
| **Tiempo real** | Requiere extensiones | Nativo (Socket.io) |
| **Curva de aprendizaje** | Moderada | Baja (ya sabes JS) |
| **Ecosistema** | Maduro, estable | Enorme, muy activo |
| **Ideal para** | Apps web tradicionales | APIs, tiempo real, microservicios |
| **Hosting** | Cualquier hosting PHP | Heroku, Vercel, AWS Lambda |
| **Archivo de config** | composer.json | package.json |
| **Instalacion deps** | composer install | npm install |
| **Ejecutar** | php artisan serve | node index.js / npm start |

---

## 10. Ejercicios Practicos

### Ejercicio 1: Mi primer servidor Express
Crea un servidor que responda a:
- `GET /` -> "Bienvenido a mi API"
- `GET /hora` -> La hora actual
- `GET /random` -> Un numero aleatorio entre 1 y 100

### Ejercicio 2: API CRUD en memoria
Crea una API para manejar una lista de tareas (to-do) en un array:
- `GET /api/todos` -> Lista todas las tareas
- `POST /api/todos` -> Agrega una tarea nueva
- `DELETE /api/todos/:id` -> Elimina una tarea

### Ejercicio 3: Cliente HTTP
Usa `axios` o `fetch` para consumir una API publica:
```javascript
const response = await fetch('https://jsonplaceholder.typicode.com/users');
const users = await response.json();
console.log(users);
```

### Ejercicio 4: Variables de entorno
1. Crea un archivo `.env` con `NOMBRE=TuNombre` y `PUERTO=4000`
2. Usa `dotenv` para leerlas
3. Muestra un saludo personalizado en `GET /`
4. Agrega `.env` a `.gitignore`

### Ejercicio 5: Middleware personalizado
Crea un middleware que registre cada peticion:
```javascript
app.use((req, res, next) => {
  console.log(`${new Date().toISOString()} ${req.method} ${req.url}`);
  next(); // IMPORTANTE: sin next(), la peticion se queda "colgada"
});
```

### Ejercicio 6: Event Loop
Predice el orden de ejecucion de este codigo (sin ejecutarlo):
```javascript
console.log('A');
setTimeout(() => console.log('B'), 0);
Promise.resolve().then(() => console.log('C'));
console.log('D');
// Respuesta: A, D, C, B
```

---

## Resumen de Conceptos Clave

```
MODULO 18 - INTRODUCCION A NODE.JS
=====================================

1. NODE.JS: JavaScript fuera del navegador (motor V8)
   - Single-threaded con Event Loop
   - Non-blocking I/O (no bloquea)
   - npm = mayor ecosistema de paquetes del mundo

2. MODULOS: require() (CommonJS) o import (ES Modules)
   - Nativos: fs, path, http, os, readline
   - npm: express, axios, dotenv, openai
   - Locales: ./miArchivo

3. EXPRESS: Framework web minimalista
   - app.get(), app.post() para rutas
   - app.use() para middleware
   - app.listen() para iniciar servidor

4. ASYNC/AWAIT: Codigo asincrono legible
   - await pausa la funcion, NO el servidor
   - try/catch para manejar errores
   - Evolucion: callbacks -> promises -> async/await

5. AWS: Servicios en la nube
   - DynamoDB: Base de datos NoSQL
   - Lambda: Funciones serverless
   - API Gateway: Puerta de entrada

6. SEGURIDAD: Variables de entorno
   - .env + dotenv
   - NUNCA hacer commit de secretos
   - .gitignore para excluir .env

7. REST: Diseno de APIs
   - Recursos + Verbos HTTP + JSON
   - Codigos de estado significativos
   - URLs descriptivas y consistentes
```

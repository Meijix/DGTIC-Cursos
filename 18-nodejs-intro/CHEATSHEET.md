# Cheatsheet — Modulo 18: Introduccion a Node.js

## Modulos

```javascript
// CommonJS
const express = require('express');         // npm
const fs = require('fs');                   // nativo
const { sumar } = require('./utils');       // local
module.exports = { sumar };                 // exportar

// ES Modules (requiere "type":"module" en package.json)
import express from 'express';
import { sumar } from './utils.js';         // extension obligatoria
export function sumar(a, b) { return a + b; }
```

## npm esencial

| Comando | Descripcion |
|---------|-------------|
| `npm init -y` | Crear proyecto |
| `npm install express` | Instalar dependencia |
| `npm install -D nodemon` | Solo desarrollo |
| `npm ci` | Instalar desde lock (para CI) |
| `npm start` / `npm run dev` | Ejecutar scripts |

## Express — Servidor basico

```javascript
const express = require('express');
const app = express();
app.use(express.json());                    // Parsear body JSON

app.get('/', (req, res) => res.send('Hola'));
app.get('/api/users', (req, res) => res.json([{ id: 1, name: 'Ana' }]));
app.post('/api/users', (req, res) => res.status(201).json(req.body));

app.listen(3000, () => console.log('Servidor en :3000'));
```

## Verbos HTTP

| Metodo | Ruta | Accion | Status |
|--------|------|--------|--------|
| `app.get('/api/items')` | Listar | 200 |
| `app.get('/api/items/:id')` | Obtener uno | 200/404 |
| `app.post('/api/items')` | Crear | 201/400 |
| `app.put('/api/items/:id')` | Actualizar | 200/404 |
| `app.delete('/api/items/:id')` | Eliminar | 200/404 |

## Middleware

```javascript
app.use((req, res, next) => {
    console.log(`${req.method} ${req.url}`);
    next();  // Sin next() la peticion se queda colgada
});
```

## Async/Await

```javascript
async function obtenerDatos() {
    try {
        const response = await fetch('https://api.example.com/data');
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error:', error.message);
    }
}
```

## Variables de entorno

```bash
# .env (agregar a .gitignore)
PORT=3000
API_KEY=sk-proj-...
```

```javascript
require('dotenv').config();
const port = process.env.PORT || 3000;
```

## AWS DynamoDB

```javascript
const dynamo = new AWS.DynamoDB.DocumentClient();
// PUT (insertar)
await dynamo.put({ TableName: 'T', Item: { id: '1', name: 'Ana' } }).promise();
// GET (por clave)
await dynamo.get({ TableName: 'T', Key: { id: '1' } }).promise();
// SCAN (todos — costoso)
await dynamo.scan({ TableName: 'T' }).promise();
```

## AWS Lambda

```javascript
exports.handler = async (event) => {
    const body = JSON.parse(event.body);
    return { statusCode: 200, body: JSON.stringify({ data: body }) };
};
```

## Servicios AWS

| Servicio | Funcion |
|----------|---------|
| API Gateway | Enruta HTTP, auth, rate limiting |
| Lambda | Codigo sin servidor (pago por uso) |
| DynamoDB | BD NoSQL sin esquema fijo |
| S3 | Almacenamiento de archivos |

## Modulos nativos

`fs` (archivos) `path` (rutas) `http` (servidor) `os` (sistema) `readline` (input) `crypto` (UUID, hash)

## Errores comunes

| Error | Solucion |
|-------|----------|
| `require is not defined` | Usar `import` o quitar `"type":"module"` |
| `Cannot find module` | `npm install` o verificar ruta con `./` |
| Peticion colgada | Agregar `next()` o enviar `res.json()` |
| `await` fuera de `async` | Envolver en `async function` |
| Clave API expuesta | Usar `.env` + `dotenv` + `.gitignore` |
| `EADDRINUSE` | Cambiar puerto o cerrar proceso anterior |

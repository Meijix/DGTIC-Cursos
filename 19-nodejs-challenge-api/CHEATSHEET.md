# Cheatsheet — Modulo 19: Node.js Challenge API (CLI + Servidor)

## Arquitectura del proyecto

```
index.js    -> CLI (terminal interactiva)     server.js -> Servidor Express (POST /ask)
.env        -> OPENAI_API_KEY                 package.json -> dependencias
```

Separar logica de negocio de la interfaz para reusar entre CLI y servidor.

## Servidor Express — Endpoint POST

```javascript
const express = require('express');
require('dotenv').config();
const app = express();
app.use(express.json());

app.post('/ask', async (req, res) => {
    const { question } = req.body;
    if (!question) return res.status(400).json({ error: 'Falta la pregunta' });
    try {
        const answer = await callOpenAI(question);
        res.json({ answer });
    } catch (error) {
        res.status(500).json({ error: 'Error interno' });
    }
});
app.listen(3000);
```

## CLI con readline

```javascript
const readline = require('readline');
const rl = readline.createInterface({ input: process.stdin, output: process.stdout });

rl.question('Tu pregunta: ', async (pregunta) => {
    const respuesta = await callOpenAI(pregunta);
    console.log(respuesta);
    rl.close();  // Cerrar para que termine el programa
});
```

## fetch vs axios

| Aspecto | axios | fetch (Node 18+) |
|---------|-------|-------------------|
| JSON auto | `response.data` | `response.json()` (manual) |
| Error en 4xx/5xx | Lanza error | No (verificar `response.ok`) |
| Body | Objeto directo | `JSON.stringify(...)` |
| Instalar | `npm install axios` | Incluido |

## Llamada a OpenAI con axios

```javascript
const response = await axios.post('https://api.openai.com/v1/chat/completions', {
    model: 'gpt-3.5-turbo',
    messages: [
        { role: 'system', content: 'Responde en espanol.' },
        { role: 'user', content: pregunta }
    ],
    max_tokens: 500, temperature: 0.7
}, { headers: { 'Authorization': `Bearer ${process.env.OPENAI_API_KEY}` } });

const answer = response.data.choices[0].message.content.trim();
```

## OpenAI — Roles y parametros

| Rol | Proposito |
|-----|-----------|
| `system` | Instrucciones para el modelo (no visible al usuario) |
| `user` | Pregunta del usuario |
| `assistant` | Respuestas previas (memoria de conversacion) |

| Parametro | Descripcion | Tipico |
|-----------|-------------|--------|
| `model` | Modelo a usar | `gpt-3.5-turbo`, `gpt-4o-mini` |
| `max_tokens` | Longitud maxima respuesta | 500 |
| `temperature` | 0=preciso, 2=creativo | 0.7 |

## Manejo de errores

```javascript
try {
    const response = await axios.post(url, data);
    return response.data;
} catch (error) {
    if (error.response) console.error('API error:', error.response.status);
    else if (error.request) console.error('Sin respuesta:', error.message);
    else console.error('Error config:', error.message);
}
```

| Codigo | Causa | Solucion |
|--------|-------|----------|
| 401 | Clave invalida | Verificar `OPENAI_API_KEY` en `.env` |
| 429 | Limite excedido | Esperar o rate limiting |
| 400 | Parametros invalidos | Verificar model, messages |

## Seguridad con .env

```bash
npm install dotenv && echo "OPENAI_API_KEY=sk-tu-clave" > .env && echo ".env" >> .gitignore
```

```javascript
require('dotenv').config();
if (!process.env.OPENAI_API_KEY) { console.error('Falta OPENAI_API_KEY'); process.exit(1); }
```

## Probar con curl

```bash
curl -X POST http://localhost:3000/ask \
  -H "Content-Type: application/json" \
  -d '{"question": "Que es JavaScript?"}'
```

## CLI vs API Server

| CLI | API Server |
|-----|------------|
| 1 usuario, interactivo | Multiples simultaneos |
| Se ejecuta y termina | Corre continuamente |
| Scripts, uso personal | Backend, integraciones |

## Errores comunes

| Error | Solucion |
|-------|----------|
| CLI no termina | Agregar `rl.close()` |
| `req.body` undefined | Agregar `app.use(express.json())` antes de rutas |
| Clave hardcodeada | Mover a `.env` + `.gitignore` |
| `Cannot read 'data'` | Verificar `response.ok` (fetch) o usar try/catch (axios) |

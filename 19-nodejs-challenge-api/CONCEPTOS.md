# Modulo 19: Challenge API - CLI y Servidor con OpenAI

## Objetivo del Modulo

Construir dos formas de acceder a la API de OpenAI:
1. **Herramienta CLI** (index.js): Pregunta desde la terminal
2. **Servidor API** (server.js): Endpoint POST /ask para integraciones

Este modulo es un **reto practico** que aplica los conceptos del modulo 18.

---

## 1. Herramientas CLI con Node.js

### Que es una CLI?

CLI (Command Line Interface) es una aplicacion que se ejecuta en la terminal.
Ejemplos que ya usas: `git`, `npm`, `node`, `curl`, `docker`.

### El modulo readline

```javascript
const readline = require('readline');

// Crear interfaz de lectura
const rl = readline.createInterface({
  input: process.stdin,   // Leer del teclado
  output: process.stdout  // Escribir en pantalla
});

// Hacer una pregunta
rl.question('Como te llamas? ', (nombre) => {
  console.log(`Hola, ${nombre}!`);
  rl.close();  // IMPORTANTE: cerrar para que el programa termine
});
```

### Streams de entrada/salida

```
┌─────────────────────────────────────────────────┐
│  SISTEMA DE STREAMS EN NODE.JS                  │
│                                                  │
│  process.stdin    (Readable Stream)              │
│  ├── Fuente: teclado, pipe, archivo              │
│  └── Uso: leer input del usuario                 │
│                                                  │
│  process.stdout   (Writable Stream)              │
│  ├── Destino: pantalla, pipe, archivo            │
│  └── Uso: console.log() escribe aqui             │
│                                                  │
│  process.stderr   (Writable Stream)              │
│  ├── Destino: pantalla de errores                │
│  └── Uso: console.error() escribe aqui           │
│                                                  │
│  EJEMPLO CON PIPES:                              │
│  echo "pregunta" | node index.js > respuesta.txt │
│       stdin ────┘                └── stdout       │
└─────────────────────────────────────────────────┘
```

### CLI mas avanzados

```javascript
// Multiples preguntas con readline
function preguntar(rl, pregunta) {
  return new Promise((resolve) => {
    rl.question(pregunta, resolve);
  });
}

async function main() {
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
  });

  const nombre = await preguntar(rl, 'Nombre: ');
  const edad = await preguntar(rl, 'Edad: ');
  console.log(`${nombre} tiene ${edad} anos`);
  rl.close();
}

main();
```

### Librerias para CLIs profesionales

```
inquirer  -> Menus interactivos, checkboxes, seleccion
commander -> Parsing de argumentos (--flag valor)
chalk     -> Texto con colores en la terminal
ora       -> Spinners de carga
figlet    -> ASCII art para banners
boxen     -> Cajas con bordes en la terminal
```

---

## 2. Clientes HTTP: axios vs fetch

### Comparacion detallada

```
                    AXIOS                   FETCH (nativo)
                    ─────                   ──────────────
Instalacion:        npm install axios       Incluido en Node 18+
JSON automatico:    Si (response.data)      No (response.json())
Error en 4xx/5xx:   Si (lanza error)        No (hay que verificar)
Interceptores:      Si                      No (necesita wrapper)
Timeout:            Si (config)             Si (AbortController)
Progreso upload:    Si                      No
Node.js antiguo:    Si (cualquier version)  No (solo 18+)
Tamano:             ~13KB                   0KB (nativo)
```

### Ejemplo: La misma peticion con ambos

```javascript
// ═══════════════════════════════════════
// CON AXIOS:
// ═══════════════════════════════════════
const axios = require('axios');

try {
  const response = await axios.post('https://api.example.com/data', {
    name: 'Ana'
  });
  console.log(response.data);        // Ya es un objeto JS
  console.log(response.status);      // 200
} catch (error) {
  // Axios LANZA error en status 4xx y 5xx
  console.error(error.response.status);  // 404, 500, etc.
  console.error(error.response.data);    // Cuerpo del error
}


// ═══════════════════════════════════════
// CON FETCH:
// ═══════════════════════════════════════
const response = await fetch('https://api.example.com/data', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ name: 'Ana' })     // Hay que serializar manualmente
});

if (!response.ok) {
  // Fetch NO lanza error en 4xx/5xx (hay que verificar manualmente)
  throw new Error(`HTTP ${response.status}`);
}

const data = await response.json();         // Hay que parsear manualmente
console.log(data);
```

---

## 3. API de OpenAI: Chat Completions

### Estructura de una peticion

```javascript
const response = await axios.post(
  'https://api.openai.com/v1/chat/completions',  // Endpoint
  {
    // BODY:
    model: 'gpt-3.5-turbo',     // Modelo a usar
    messages: [                   // Historial de conversacion
      {
        role: 'system',           // Instrucciones para el modelo
        content: 'Eres un experto en programacion. Responde en espanol.'
      },
      {
        role: 'user',             // Pregunta del usuario
        content: 'Que es una API?'
      }
    ],
    max_tokens: 500,              // Longitud maxima de respuesta
    temperature: 0.7              // Creatividad (0=preciso, 2=creativo)
  },
  {
    // HEADERS:
    headers: {
      'Content-Type': 'application/json',
      'Authorization': 'Bearer sk-...'  // Clave API
    }
  }
);
```

### Roles de mensajes

```
┌──────────────────────────────────────────────────────┐
│  ROLES EN CHAT COMPLETIONS                           │
├───────────┬──────────────────────────────────────────┤
│ 'system'  │ Define el COMPORTAMIENTO del modelo.     │
│           │ Es como las "instrucciones" que le das.  │
│           │ El usuario final NO ve este mensaje.     │
│           │                                          │
│           │ Ejemplo: "Eres un tutor de matematicas.  │
│           │ Explica paso a paso. Usa ejemplos."      │
├───────────┼──────────────────────────────────────────┤
│ 'user'    │ Los mensajes del USUARIO.                │
│           │ Son las preguntas o instrucciones.       │
│           │                                          │
│           │ Ejemplo: "Resuelve 2x + 5 = 15"         │
├───────────┼──────────────────────────────────────────┤
│ 'assistant'│ Respuestas PREVIAS del modelo.          │
│           │ Se usan para dar CONTEXTO.               │
│           │ El modelo "recuerda" la conversacion.    │
│           │                                          │
│           │ Ejemplo: "x = 5. Primero reste 5..."     │
└───────────┴──────────────────────────────────────────┘
```

### Parametros importantes

```
model:          Cual modelo usar
                'gpt-3.5-turbo'  (rapido, economico)
                'gpt-4o-mini'    (bueno, asequible)
                'gpt-4o'         (el mas capaz)

max_tokens:     Limite de tokens en la respuesta
                1 token ≈ 3/4 de una palabra en espanol
                100 tokens ≈ 75 palabras

temperature:    Nivel de "creatividad" (0.0 a 2.0)
                0.0 = Muy determinista (siempre la misma respuesta)
                0.7 = Balance (por defecto, recomendado)
                2.0 = Muy creativo (puede ser incoherente)

top_p:          Alternativa a temperature
                0.1 = Solo las palabras mas probables
                1.0 = Todas las palabras posibles

n:              Numero de respuestas a generar (por defecto 1)
                Util para comparar diferentes respuestas

stop:           Secuencias que detienen la generacion
                ["\\n", "FIN"] -> Para si encuentra salto de linea o "FIN"
```

### Limites de tokens por modelo

```
Modelo              Contexto (input+output)    Costo input    Costo output
──────────────────  ─────────────────────────  ────────────── ──────────────
gpt-3.5-turbo       4,096 tokens               $0.50/1M       $1.50/1M
gpt-4o-mini         128,000 tokens              $0.15/1M       $0.60/1M
gpt-4o              128,000 tokens              $2.50/1M       $10.00/1M

1M tokens ≈ 750,000 palabras ≈ 3,000 paginas de texto
```

---

## 4. Servidor REST con Express: Endpoint POST

### Anatomia de un endpoint POST

```javascript
app.post('/ask', async (req, res) => {
  //      ────   ─────  ───  ───
  //       │       │     │    │
  //       │       │     │    └── Response: para enviar respuesta
  //       │       │     └── Request: contiene los datos de la peticion
  //       │       └── async: la funcion hace operaciones asincronas
  //       └── POST /ask: la URL y el metodo HTTP

  // PASO 1: Extraer datos del body
  const { question } = req.body;

  // PASO 2: Validar entrada
  if (!question) {
    return res.status(400).json({ error: 'Falta la pregunta' });
  }

  // PASO 3: Procesar (llamar a OpenAI)
  try {
    const answer = await callOpenAI(question);
    res.json({ answer });           // PASO 4: Enviar respuesta exitosa
  } catch (error) {
    res.status(500).json({ error: 'Error interno' }); // PASO 5: Manejar error
  }
});
```

### Probar el endpoint

```bash
# Con curl (terminal):
curl -X POST http://localhost:3000/ask \
  -H "Content-Type: application/json" \
  -d '{"question": "Que es JavaScript?"}'

# Con httpie (terminal, mas legible):
http POST localhost:3000/ask question="Que es JavaScript?"

# Con JavaScript (desde otro archivo):
const response = await fetch('http://localhost:3000/ask', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ question: 'Que es JavaScript?' })
});
const data = await response.json();
console.log(data.answer);
```

---

## 5. Arquitectura: CLI vs API Server

### Cuando usar cada patron

```
HERRAMIENTA CLI                         API SERVER
───────────                             ──────────
1 usuario a la vez                      Multiples usuarios simultaneos
Interactiva (terminal)                  Programatica (HTTP)
Se ejecuta y termina                    Corre continuamente
Facil de prototipar                     Escalable y distribuible
Uso personal/interno                    Uso publico/integrable

EJEMPLOS:
- Script para generar reportes          - Backend de una app web
- Herramienta de deploy                 - Microservicio
- Automatizacion de tareas              - Webhook handler
- Utilidades de desarrollo              - API publica

DIAGRAMA DE DECISION:
  Un solo usuario lo usa?
    Si  -> CLI
    No  -> Necesita interfaz web?
             Si  -> API + Frontend
             No  -> API sola (para integraciones)
```

### Patron de arquitectura compartida

```javascript
// ═══ Logica de negocio separada (openai-service.js) ═══
async function askOpenAI(question) {
  const response = await axios.post('https://api.openai.com/v1/chat/completions', {
    model: 'gpt-3.5-turbo',
    messages: [{ role: 'user', content: question }]
  }, {
    headers: { Authorization: `Bearer ${process.env.OPENAI_API_KEY}` }
  });
  return response.data.choices[0].message.content.trim();
}

module.exports = { askOpenAI };


// ═══ CLI (index.js) ═══
const { askOpenAI } = require('./openai-service');
rl.question('> ', async (q) => {
  const answer = await askOpenAI(q);
  console.log(answer);
  rl.close();
});


// ═══ API Server (server.js) ═══
const { askOpenAI } = require('./openai-service');
app.post('/ask', async (req, res) => {
  const answer = await askOpenAI(req.body.question);
  res.json({ answer });
});
```

Esta separacion permite:
- Reusar la logica de negocio
- Testear independientemente
- Agregar nuevas interfaces (Discord bot, Slack bot, etc.)

---

## 6. Claves API y Seguridad

### El problema

```
FORMA INCORRECTA (presente en este proyecto):
const API_KEY = 'sk-proj-abc123...';  // HARDCODEADA EN EL CODIGO

Riesgos:
- Cualquiera con acceso al repo ve la clave
- Bots escanean GitHub buscando claves expuestas
- OpenAI puede desactivar tu cuenta
- Alguien puede generar cargos en tu tarjeta
```

### La solucion

```bash
# Paso 1: Instalar dotenv
npm install dotenv

# Paso 2: Crear .env
echo "OPENAI_API_KEY=sk-proj-tu-clave-real" > .env

# Paso 3: Agregar a .gitignore
echo ".env" >> .gitignore

# Paso 4: Crear .env.example (para documentar)
echo "OPENAI_API_KEY=tu-clave-aqui" > .env.example
```

```javascript
// Paso 5: Usar en el codigo
require('dotenv').config();
const API_KEY = process.env.OPENAI_API_KEY;

if (!API_KEY) {
  console.error('Error: OPENAI_API_KEY no esta configurada');
  console.error('Crea un archivo .env con tu clave API');
  process.exit(1);
}
```

### Checklist de seguridad

```
[ ] .env esta en .gitignore
[ ] No hay claves hardcodeadas en el codigo
[ ] Existe un .env.example con las variables (sin valores reales)
[ ] Las claves son diferentes en desarrollo y produccion
[ ] Si una clave se expuso, fue rotada inmediatamente
[ ] El servidor valida la existencia de las variables al iniciar
```

---

## 7. Manejo de Errores en APIs

### Patron try/catch con async/await

```javascript
async function llamarAPI() {
  try {
    // Codigo que puede fallar
    const response = await axios.post(url, data);
    return response.data;

  } catch (error) {
    // Clasificar el error
    if (error.response) {
      // La API respondio con un error (4xx, 5xx)
      console.error('Error de API:', error.response.status);
      console.error('Detalles:', error.response.data);
    } else if (error.request) {
      // La peticion se envio pero no hubo respuesta (timeout, sin internet)
      console.error('Sin respuesta:', error.message);
    } else {
      // Error al configurar la peticion
      console.error('Error de config:', error.message);
    }

  } finally {
    // Se ejecuta SIEMPRE (con o sin error)
    // Ideal para limpiar recursos
    console.log('Peticion completada');
  }
}
```

### Errores comunes de la API de OpenAI

```
401 Unauthorized     -> Clave API invalida o expirada
                        Solucion: Verificar la clave en .env

429 Too Many Requests -> Limite de peticiones excedido
                        Solucion: Esperar o implementar rate limiting

400 Bad Request      -> Parametros invalidos
                        Solucion: Verificar model, messages, etc.

500 Server Error     -> Error interno de OpenAI
                        Solucion: Reintentar despues de unos segundos

ENOTFOUND            -> Sin conexion a internet
                        Solucion: Verificar conexion de red

ECONNREFUSED         -> Servidor no disponible
                        Solucion: Verificar URL y estado del servicio
```

---

## 8. Consideraciones de Deployment

### Opciones para desplegar

```
PLATAFORMA       TIPO              COSTO          IDEAL PARA
────────────     ──────            ────────       ──────────
Vercel           Serverless        Gratis*        APIs simples
Railway          PaaS              Gratis*        Node.js servers
Render           PaaS              Gratis*        APIs y web apps
Heroku           PaaS              $7/mes+        Apps completas
AWS Lambda       Serverless        Pago por uso   APIs escalables
AWS EC2          Servidor          $10/mes+       Control total
DigitalOcean     VPS               $4/mes+        Servidores propios

* Con limitaciones en el tier gratuito
```

### Checklist para produccion

```
[ ] Variables de entorno configuradas (no hardcodeadas)
[ ] .gitignore incluye: .env, node_modules/, *.log
[ ] package.json tiene script "start": "node server.js"
[ ] Manejo de errores en todas las rutas
[ ] Logging apropiado (no console.log con datos sensibles)
[ ] CORS configurado si el frontend es diferente dominio
[ ] Rate limiting para prevenir abuso
[ ] HTTPS habilitado (la plataforma suele proporcionarlo)
```

---

## 9. Ejercicios Practicos

### Ejercicio 1: Arreglar la seguridad
1. Instala `dotenv` en el proyecto
2. Mueve la clave API a un archivo `.env`
3. Agrega `.env` a `.gitignore`
4. Modifica index.js y server.js para usar `process.env.OPENAI_API_KEY`
5. Crea un `.env.example`

### Ejercicio 2: CLI conversacional
Modifica index.js para que:
- Permita hacer MULTIPLES preguntas (bucle)
- Mantenga el historial de la conversacion
- El usuario pueda escribir "salir" para terminar

```javascript
// Pista: Usa un array para guardar el historial
const messages = [
  { role: 'system', content: 'Eres un asistente amigable.' }
];

// En cada pregunta, agrega al historial:
messages.push({ role: 'user', content: pregunta });
// ... llamar a OpenAI con todos los messages ...
messages.push({ role: 'assistant', content: respuesta });
```

### Ejercicio 3: Agregar endpoint GET /health
Agrega a server.js un endpoint que confirme que el servidor funciona:
```javascript
app.get('/health', (req, res) => {
  res.json({
    status: 'ok',
    timestamp: new Date().toISOString(),
    uptime: process.uptime()
  });
});
```

### Ejercicio 4: Agregar system prompt al servidor
Modifica server.js para aceptar un prompt de sistema opcional:
```json
{
  "question": "Que es JavaScript?",
  "system": "Responde como si fueras un pirata"
}
```

### Ejercicio 5: Conectar CLI con servidor
Modifica index.js para que en vez de llamar directamente a OpenAI,
llame a tu servidor local (server.js en el puerto 3000):
```javascript
const response = await axios.post('http://localhost:3000/ask', {
  question: userQuestion
});
```

### Ejercicio 6: Agregar cache simple
Implementa un cache en memoria para no repetir llamadas a OpenAI:
```javascript
const cache = {};

app.post('/ask', async (req, res) => {
  const { question } = req.body;

  // Verificar cache
  if (cache[question]) {
    return res.json({ answer: cache[question], cached: true });
  }

  // Llamar a OpenAI
  const answer = await callOpenAI(question);

  // Guardar en cache
  cache[question] = answer;

  res.json({ answer, cached: false });
});
```

---

## Resumen de Conceptos Clave

```
MODULO 19 - CHALLENGE API
===========================

1. CLI: Herramientas de terminal con readline
   - process.stdin / process.stdout (streams)
   - rl.question() para input del usuario
   - rl.close() para terminar

2. HTTP CLIENTS: axios vs fetch
   - axios: automatico, errores en 4xx/5xx, interceptores
   - fetch: nativo (Node 18+), manual, sin errores auto

3. OPENAI API: Chat Completions
   - Roles: system (instrucciones), user (pregunta), assistant (contexto)
   - Parametros: model, max_tokens, temperature
   - Endpoint: POST /v1/chat/completions

4. EXPRESS POST: Recibir y responder JSON
   - express.json() para parsear body
   - req.body para acceder a datos
   - res.json() para enviar respuesta
   - Validar entrada SIEMPRE

5. ARQUITECTURA: CLI vs API
   - CLI: personal, interactivo, una ejecucion
   - API: escalable, programatico, continuo
   - Separar logica de negocio de la interfaz

6. SEGURIDAD: .env y dotenv
   - NUNCA hardcodear claves API
   - .env en .gitignore
   - Rotar claves expuestas

7. ERRORES: try/catch/finally
   - error.response (error de API)
   - error.request (error de red)
   - error.message (error general)
   - finally para limpiar recursos
```

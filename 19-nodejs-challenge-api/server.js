/**
 * ==========================================================================
 * MODULO 19 - CHALLENGE API: Servidor Express con endpoint /ask
 * ==========================================================================
 *
 * PROPOSITO DE ESTE ARCHIVO:
 * Crear un servidor HTTP que expone la funcionalidad de OpenAI como API REST.
 * Mientras que index.js es una herramienta CLI (terminal), este archivo
 * es un SERVIDOR que responde a peticiones HTTP.
 *
 * COMPARACION CLI vs API SERVER:
 *
 *   index.js (CLI):                    server.js (API):
 *   ┌─────────────────────┐            ┌─────────────────────┐
 *   │  Terminal            │            │  Cualquier cliente   │
 *   │  > Ask me something: │            │  - Navegador         │
 *   │  > Que es Node.js?  │            │  - Postman           │
 *   │                      │            │  - Frontend React    │
 *   │  (1 usuario,         │            │  - Otra API          │
 *   │   1 pregunta,        │            │  - App movil         │
 *   │   y se cierra)       │            │  (multiples clientes │
 *   └─────────────────────┘            │   simultaneos)       │
 *                                       └─────────────────────┘
 *
 * CUANDO USAR CADA UNO:
 *   CLI:
 *   - Scripts personales de automatizacion
 *   - Herramientas de desarrollo (como git, npm, docker)
 *   - Prototipos rapidos
 *   - Tareas de administracion de servidores
 *
 *   API Server:
 *   - Cuando un frontend necesita datos (React, Vue, Angular)
 *   - Cuando otros servicios necesitan acceder a la funcionalidad
 *   - Para integrar con webhooks (Slack, Discord, GitHub)
 *   - Cuando multiples usuarios acceden simultaneamente
 *
 * FLUJO DE ESTE SERVIDOR:
 *   1. Cliente envia: POST /ask con { "question": "Que es Node.js?" }
 *   2. Servidor recibe la peticion y extrae la pregunta
 *   3. Servidor llama a la API de OpenAI con la pregunta
 *   4. Servidor recibe la respuesta de OpenAI
 *   5. Servidor envia: { "answer": "Node.js es..." } al cliente
 *
 * COMO PROBAR:
 *   1. Iniciar: node server.js
 *   2. Con curl:
 *      curl -X POST http://localhost:3000/ask \
 *        -H "Content-Type: application/json" \
 *        -d '{"question": "Que es JavaScript?"}'
 *
 *   3. Con Postman:
 *      - Metodo: POST
 *      - URL: http://localhost:3000/ask
 *      - Body: raw JSON -> { "question": "Que es JavaScript?" }
 */

const express = require('express');
/**
 * EXPRESS: Framework minimalista para crear servidores HTTP en Node.js.
 *
 * Express proporciona:
 * - Routing (definir endpoints como GET /users, POST /ask)
 * - Middleware (funciones intermedias: parsear JSON, logging, auth)
 * - Manejo de errores
 * - Servir archivos estaticos
 *
 * ALTERNATIVAS A EXPRESS:
 *   Fastify  -> Mas rapido que Express, API moderna
 *   Koa      -> Del mismo equipo de Express, usa async/await nativo
 *   Hapi     -> Mas orientado a configuracion, ideal para enterprise
 *   NestJS   -> Framework completo como Laravel (usa Express internamente)
 */

const axios = require('axios');
/**
 * AXIOS: Se usa aqui para hacer peticiones HTTP a la API de OpenAI.
 *
 * En este archivo, axios actua como CLIENTE HTTP:
 *   Nuestro servidor (Express) -> peticion HTTP -> API de OpenAI
 *
 * Es comun que un servidor sea a su vez CLIENTE de otros servicios.
 * Este patron se llama "Backend for Frontend" (BFF) o "API Gateway".
 *
 * BENEFICIO DE ESTE PATRON:
 * - La clave API de OpenAI esta en el servidor (segura)
 * - El frontend nunca ve la clave API
 * - El servidor puede agregar cache, rate limiting, logging
 * - Se pueden combinar multiples APIs en un solo endpoint
 */

const app = express();
const PORT = 3000;
/**
 * PUERTO DEL SERVIDOR:
 *
 * MEJORA SUGERIDA: Usar variable de entorno para el puerto:
 *   const PORT = process.env.PORT || 3000;
 *
 * Esto permite que servicios de hosting (Heroku, Railway, Render)
 * asignen el puerto dinamicamente.
 */

//leer JSON
app.use(express.json());
/**
 * MIDDLEWARE express.json():
 * Convierte el cuerpo de peticiones JSON en un objeto JavaScript.
 *
 * Sin este middleware:
 *   POST { "question": "hola" }
 *   req.body -> undefined
 *
 * Con este middleware:
 *   POST { "question": "hola" }
 *   req.body -> { question: "hola" }
 *
 * ANTES de Express 4.16, se necesitaba instalar 'body-parser':
 *   const bodyParser = require('body-parser');
 *   app.use(bodyParser.json());
 *
 * Ahora express.json() lo incluye integrado.
 */

//clave API de OpenAI
const API_KEY = 'TU_API_KEY_AQUI'; // Reemplázala si es necesario
/**
 * !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
 * ADVERTENCIA CRITICA DE SEGURIDAD
 * !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
 *
 * La clave API esta HARDCODEADA en el codigo fuente.
 * Esto es un PROBLEMA SERIO de seguridad:
 *
 * 1. Cualquiera con acceso al repositorio puede ver la clave
 * 2. Si se sube a GitHub, bots automatizados la detectan en segundos
 * 3. Un atacante puede usar tu clave y generar cargos en tu cuenta
 * 4. OpenAI puede desactivar tu cuenta por exposicion de clave
 *
 * SOLUCION CORRECTA:
 *
 *   Paso 1: Instalar dotenv
 *     npm install dotenv
 *
 *   Paso 2: Crear archivo .env
 *     OPENAI_API_KEY=sk-proj-...
 *
 *   Paso 3: Agregar .env a .gitignore
 *     echo ".env" >> .gitignore
 *
 *   Paso 4: Usar en el codigo
 *     require('dotenv').config();
 *     const API_KEY = process.env.OPENAI_API_KEY;
 *
 *   Paso 5: Crear .env.example (para documentar las variables)
 *     OPENAI_API_KEY=tu-clave-aqui
 */

// Ruta POST /ask
app.post('/ask', async (req, res) => {
  /**
   * ENDPOINT POST /ask:
   * Recibe una pregunta en JSON y devuelve la respuesta de OpenAI.
   *
   * METODO POST (no GET) porque:
   * - Estamos ENVIANDO datos al servidor (la pregunta)
   * - GET no deberia tener body (aunque tecnicamente puede)
   * - POST es semanticamente correcto para "enviar algo para procesar"
   *
   * PARAMETROS:
   *   req (Request):  Contiene toda la informacion de la peticion
   *     - req.body:    Cuerpo JSON parseado
   *     - req.params:  Parametros de URL (/users/:id -> req.params.id)
   *     - req.query:   Query strings (?page=1 -> req.query.page)
   *     - req.headers: Headers HTTP
   *
   *   res (Response): Objeto para enviar la respuesta
   *     - res.json():  Envia respuesta JSON
   *     - res.status(): Establece codigo de estado
   *     - res.send():  Envia texto
   *     - res.redirect(): Redirige a otra URL
   *
   * async: La funcion es async porque hace await de la llamada a OpenAI.
   */

  const userQuestion = req.body.question;
  /**
   * EXTRAER LA PREGUNTA:
   * req.body es el JSON que el cliente envio.
   *
   * Si el cliente envio: { "question": "Que es JavaScript?" }
   * Entonces: req.body.question = "Que es JavaScript?"
   *
   * VALIDACION MAS ROBUSTA (sugerencia):
   *   const { question } = req.body;  // Desestructuracion
   *   if (!question || typeof question !== 'string' || question.trim() === '') {
   *     return res.status(400).json({ error: 'Question must be a non-empty string' });
   *   }
   */

  if (!userQuestion) {
    return res.status(400).json({ error: 'Missing question in body.' });
  }
  /**
   * VALIDACION DE ENTRADA:
   * Status 400 = Bad Request (error del cliente).
   *
   * El "return" es CRITICO: sin el, la funcion continuaria ejecutandose
   * y podria enviar DOS respuestas (lo que causa un error en Express:
   * "Cannot set headers after they are sent to the client").
   *
   * REGLA: Siempre usar "return" antes de res.json()/res.send() en
   * bloques condicionales para evitar respuestas multiples.
   */

  try {
    const response = await axios.post(
      'https://api.openai.com/v1/chat/completions',
      {
        model: 'gpt-3.5-turbo',
        messages: [{ role: 'user', content: userQuestion }]
        /**
         * MENSAJES SIMPLES:
         * Solo enviamos un mensaje con role 'user'.
         *
         * MEJORA: Agregar un mensaje 'system' para definir el comportamiento:
         *   messages: [
         *     { role: 'system', content: 'Responde siempre en espanol y de forma concisa.' },
         *     { role: 'user', content: userQuestion }
         *   ]
         *
         * MEJORA AVANZADA: Mantener historial de conversacion
         * Para esto necesitarias almacenar mensajes previos (en memoria o BD)
         * y enviarlos todos en cada peticion.
         */
      },
      {
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${API_KEY}`
          /**
           * HEADER DE AUTENTICACION:
           * Authorization: Bearer <token>
           *
           * Este es el estandar OAuth 2.0 para autenticacion con tokens.
           * "Bearer" indica que el token "porta" (bears) la identidad.
           */
        }
      }
    );

    const answer = response.data.choices[0].message.content.trim();
    /**
     * EXTRAER Y LIMPIAR LA RESPUESTA:
     * Navegar la estructura de respuesta de OpenAI:
     *   response.data           -> Cuerpo de la respuesta HTTP (por axios)
     *     .choices[0]           -> Primera opcion de respuesta
     *       .message.content    -> Texto de la respuesta
     *         .trim()           -> Eliminar espacios en blanco
     */

    res.json({ answer });
    /**
     * ENVIAR RESPUESTA:
     * res.json({ answer }) es equivalente a:
     *   res.json({ answer: answer })
     *
     * El shorthand de ES6 { answer } crea { answer: "..." }
     * cuando la variable y la propiedad tienen el mismo nombre.
     *
     * Express automaticamente:
     * - Establece Content-Type: application/json
     * - Convierte el objeto a string JSON
     * - Establece status 200 (por defecto)
     */

  } catch (error) {
    console.error('Error:', error.response?.data || error.message);
    res.status(500).json({ error: 'Error fetching from OpenAI' });
    /**
     * MANEJO DE ERRORES:
     *
     * console.error(): Registra el error completo en la consola del servidor
     *   (para debugging - solo el desarrollador ve esto)
     *
     * res.status(500).json(): Envia una respuesta generica al cliente
     *   (no revelar detalles internos del error)
     *
     * Status 500 = Internal Server Error
     *   El error NO fue culpa del cliente, fue del servidor.
     *
     * BUENAS PRACTICAS DE ERRORES:
     *   - Registrar el error completo en el servidor (logs)
     *   - Enviar mensaje generico al cliente (seguridad)
     *   - Nunca enviar stack traces al cliente en produccion
     *   - Usar codigos de estado HTTP apropiados
     */
  }
});

// Iniciar servidor
app.listen(PORT, () => {
  console.log(`Server running at http://localhost:${PORT}`);
});
/**
 * INICIAR EL SERVIDOR:
 *
 * app.listen() hace que Express empiece a escuchar peticiones HTTP
 * en el puerto especificado (3000).
 *
 * El callback se ejecuta cuando el servidor esta listo.
 * Si el puerto esta ocupado, se lanza un error EADDRINUSE.
 *
 * PARA PROBAR:
 *   Terminal 1: node server.js
 *   Terminal 2: curl -X POST http://localhost:3000/ask \
 *               -H "Content-Type: application/json" \
 *               -d '{"question": "Que es JavaScript?"}'
 *
 * O usando el CLI del mismo modulo:
 *   Modifica index.js para que en vez de llamar directamente a OpenAI,
 *   llame a tu servidor: axios.post('http://localhost:3000/ask', ...)
 */

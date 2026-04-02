/**
 * ==========================================================================
 * MODULO 19 - CHALLENGE API: Herramienta CLI con OpenAI
 * ==========================================================================
 *
 * PROPOSITO DE ESTE ARCHIVO:
 * Crear una herramienta de LINEA DE COMANDOS (CLI) interactiva que
 * permite hacerle preguntas a la API de OpenAI desde la terminal.
 *
 * QUE ES UNA HERRAMIENTA CLI?
 * CLI = Command Line Interface (Interfaz de Linea de Comandos)
 * Es un programa que se ejecuta en la terminal, sin interfaz grafica.
 * Ejemplos de CLIs famosos: git, npm, node, curl, docker
 *
 * ARQUITECTURA DEL MODULO 19:
 * Este modulo tiene DOS formas de acceder a la misma funcionalidad:
 *
 *   ┌──────────────────────┐     ┌──────────────────────┐
 *   │   index.js (CLI)     │     │  server.js (API)     │
 *   │                      │     │                      │
 *   │  Terminal/Consola     │     │  HTTP POST /ask      │
 *   │  > Ask me something: │     │  { "question": "?" } │
 *   │  > ...respuesta...   │     │  { "answer": "..." } │
 *   └──────────┬───────────┘     └──────────┬───────────┘
 *              │                            │
 *              └────────────┬───────────────┘
 *                           │
 *                           ▼
 *              ┌────────────────────────┐
 *              │   OpenAI API           │
 *              │   Chat Completions     │
 *              │   gpt-3.5-turbo        │
 *              └────────────────────────┘
 *
 * CUANDO USAR CLI vs API SERVER:
 *   CLI:  Herramientas personales, scripts de automatizacion,
 *         tareas administrativas, prototipado rapido
 *   API:  Cuando otros servicios/apps necesitan acceder,
 *         integraciones, frontend separado, microservicios
 *
 * FLUJO DE ESTE ARCHIVO:
 *   1. Importar dependencias (axios, readline)
 *   2. Configurar readline para leer input del usuario
 *   3. Mostrar un prompt ("> Ask me something: ")
 *   4. Enviar la pregunta a OpenAI via axios
 *   5. Mostrar la respuesta
 *   6. Cerrar readline
 */

const axios = require('axios');
/**
 * AXIOS: Cliente HTTP para Node.js y navegadores.
 *
 * Axios facilita hacer peticiones HTTP:
 *   axios.get(url)          -> Peticion GET
 *   axios.post(url, data)   -> Peticion POST con datos
 *   axios.put(url, data)    -> Peticion PUT
 *   axios.delete(url)       -> Peticion DELETE
 *
 * AXIOS vs FETCH vs NODE-FETCH:
 *
 *   AXIOS (usado aqui):
 *   + Funciona en Node.js Y navegadores
 *   + Parsea JSON automaticamente
 *   + Interceptores (middleware para requests)
 *   + Manejo de errores mas detallado
 *   + Timeout integrado
 *   - Dependencia externa (npm install axios)
 *
 *   FETCH (nativo en Node.js 18+):
 *   + No requiere instalacion (nativo)
 *   + API estandar del navegador
 *   - Necesitas hacer response.json() manualmente
 *   - No lanza error en status 4xx/5xx
 *   - No disponible en Node.js < 18
 *
 *   NODE-FETCH (paquete npm):
 *   + Polyfill de fetch para Node.js antiguo
 *   + Misma API que el fetch del navegador
 *   - Dependencia externa
 *   - Innecesario en Node.js 18+
 *
 * EJEMPLO COMPARATIVO:
 *   // Con axios:
 *   const { data } = await axios.post(url, { question: 'hola' });
 *   console.log(data.answer);
 *
 *   // Con fetch:
 *   const response = await fetch(url, {
 *     method: 'POST',
 *     headers: { 'Content-Type': 'application/json' },
 *     body: JSON.stringify({ question: 'hola' })
 *   });
 *   const data = await response.json();
 *   console.log(data.answer);
 */

const readline = require('readline');
/**
 * READLINE: Modulo NATIVO de Node.js para leer input del usuario.
 *
 * Es un modulo built-in (no necesita npm install).
 * Permite crear interfaces interactivas en la terminal.
 *
 * CONCEPTOS:
 * - process.stdin:  Flujo de ENTRADA (lo que el usuario escribe)
 * - process.stdout: Flujo de SALIDA (lo que se muestra en pantalla)
 * - readline.createInterface(): Crea una interfaz de lectura
 * - rl.question(): Muestra un prompt y espera respuesta
 * - rl.close(): Cierra la interfaz (termina el programa)
 *
 * ALTERNATIVAS PARA CLI MAS COMPLEJOS:
 *   - inquirer:  Menus, checkboxes, seleccion multiple
 *   - commander: Parsing de argumentos (--flag, subcomandos)
 *   - chalk:     Texto con colores en la terminal
 *   - ora:       Spinners de carga
 *   - figlet:    ASCII art para titulos
 */

//Clave Api
const API_KEY = 'TU_API_KEY_AQUI'; // Clave API
/**
 * !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
 * PROBLEMA DE SEGURIDAD: CLAVE API HARDCODEADA
 * !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
 *
 * NUNCA poner claves API directamente en el codigo fuente.
 * Esta clave es visible para cualquiera que tenga acceso al repositorio.
 *
 * FORMA INCORRECTA (como esta aqui):
 *   const API_KEY = 'sk-proj-...';
 *
 * FORMA CORRECTA:
 *   1. Crear archivo .env:
 *      OPENAI_API_KEY=sk-proj-...
 *
 *   2. Agregar .env a .gitignore
 *
 *   3. En el codigo:
 *      require('dotenv').config();
 *      const API_KEY = process.env.OPENAI_API_KEY;
 *
 * Si esta clave se subio a GitHub, ya esta COMPROMETIDA y debe:
 * 1. Revocarse inmediatamente en https://platform.openai.com/api-keys
 * 2. Generar una nueva clave
 * 3. Guardarla en .env (NO en el codigo)
 *
 * NOTA PARA ESTUDIANTES: Este es un ejemplo de lo que NO se debe hacer.
 * En un proyecto real, esto seria una vulnerabilidad de seguridad critica.
 */

// Preparar la consola para leer al usuario
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});
/**
 * CREAR INTERFAZ READLINE:
 *
 * readline.createInterface() crea un objeto que permite:
 * - Leer lineas de texto del usuario
 * - Mostrar prompts
 * - Manejar eventos de linea completada
 *
 * PARAMETROS:
 *   input: process.stdin   -> Lee del teclado
 *   output: process.stdout -> Escribe en la pantalla
 *
 * process.stdin y process.stdout son "streams" (flujos de datos):
 * - stdin:  Datos que ENTRAN al programa (teclado, pipe, archivo)
 * - stdout: Datos que SALEN del programa (pantalla, pipe, archivo)
 *
 * Esto permite que el programa funcione con pipes:
 *   echo "Mi pregunta" | node index.js
 *   node index.js < preguntas.txt
 */

// Preguntar
rl.question('> Ask me something: ', async (question) => {
  /**
   * rl.question(prompt, callback):
   *
   * 1. Muestra el texto "> Ask me something: " en la terminal
   * 2. Espera a que el usuario escriba algo y presione Enter
   * 3. Ejecuta el callback con el texto escrito como argumento
   *
   * El callback es async porque necesitamos hacer await dentro:
   * - await axios.post() es una operacion asincrona (red)
   *
   * FLUJO DETALLADO:
   *   Terminal: > Ask me something: |        (cursor parpadeando)
   *   Usuario:  > Ask me something: Que es Node.js?
   *   Enter:    question = "Que es Node.js?"
   *   Axios:    Envia peticion a OpenAI...
   *   Respuesta: { answer: "Node.js es un entorno de..." }
   *   Terminal:  { answer: 'Node.js es un entorno de...' }
   */

  try {
    /**
     * TRY/CATCH en funciones async:
     * Captura errores de:
     * - Problemas de red (sin internet, timeout)
     * - Errores de la API (clave invalida, limite excedido)
     * - Errores de parseo (respuesta inesperada)
     */

    const response = await axios.post(
      'https://api.openai.com/v1/chat/completions',
      /**
       * ENDPOINT DE OPENAI:
       * URL: https://api.openai.com/v1/chat/completions
       *
       * Este es el endpoint de "Chat Completions" de OpenAI.
       * Es la forma principal de interactuar con modelos GPT.
       *
       * ESTRUCTURA DE LA URL:
       *   https://api.openai.com  -> Servidor de OpenAI
       *   /v1                     -> Version 1 de la API
       *   /chat/completions       -> Recurso: completar conversaciones
       */
      {
        model: 'gpt-3.5-turbo',
        /**
         * MODELO: gpt-3.5-turbo
         *
         * MODELOS DISPONIBLES (a la fecha):
         *   gpt-4o          -> Mas capaz, mas costoso
         *   gpt-4o-mini     -> Buen balance costo/calidad
         *   gpt-3.5-turbo   -> Rapido y economico (usado aqui)
         *   gpt-4-turbo     -> Modelo anterior, muy capaz
         *
         * LIMITES DE TOKENS:
         * Cada modelo tiene un limite de "contexto" (input + output):
         *   gpt-3.5-turbo: 4,096 tokens (~3,000 palabras)
         *   gpt-4o:        128,000 tokens (~96,000 palabras)
         *
         * Un TOKEN es aproximadamente 3/4 de una palabra en espanol.
         */
        messages: [{ role: 'user', content: question }]
        /**
         * MENSAJES (Chat Completions):
         * La API espera un array de mensajes con roles:
         *
         *   role: 'system'    -> Instrucciones para el modelo
         *                        Ejemplo: "Eres un experto en Python"
         *
         *   role: 'user'      -> Mensaje del usuario (la pregunta)
         *
         *   role: 'assistant' -> Respuesta previa del modelo
         *                        Se usa para mantener contexto
         *
         * Aqui solo enviamos UN mensaje con role 'user'.
         *
         * Para una conversacion con contexto, enviarias:
         *   messages: [
         *     { role: 'system', content: 'Eres un tutor de programacion' },
         *     { role: 'user', content: 'Que es una variable?' },
         *     { role: 'assistant', content: 'Una variable es...' },
         *     { role: 'user', content: 'Dame un ejemplo en JS' }
         *   ]
         */
      },
      {
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${API_KEY}`
        }
        /**
         * HEADERS HTTP:
         *
         * Content-Type: 'application/json'
         *   Le dice al servidor que el body es JSON.
         *
         * Authorization: 'Bearer sk-...'
         *   Autenticacion con token Bearer.
         *   "Bearer" es un esquema de autenticacion HTTP estandar.
         *   El token va despues de "Bearer " (con espacio).
         *
         * OTROS ESQUEMAS DE AUTENTICACION:
         *   Bearer token  -> APIs modernas (OpenAI, GitHub, etc.)
         *   Basic         -> Usuario:contrasena en base64
         *   API Key       -> Clave en header o query parameter
         *   OAuth 2.0     -> Flujo de autorizacion complejo
         */
      }
    );

    const answer = response.data.choices[0].message.content;
    /**
     * EXTRAER LA RESPUESTA:
     *
     * La estructura completa de la respuesta de OpenAI:
     * {
     *   data: {
     *     id: "chatcmpl-abc123",
     *     object: "chat.completion",
     *     created: 1677858242,
     *     model: "gpt-3.5-turbo",
     *     usage: {
     *       prompt_tokens: 13,      <- Tokens del input
     *       completion_tokens: 50,  <- Tokens del output
     *       total_tokens: 63        <- Total (se cobra por esto)
     *     },
     *     choices: [
     *       {
     *         message: {
     *           role: "assistant",
     *           content: "La respuesta del modelo..."
     *         },
     *         finish_reason: "stop"  <- "stop" = respuesta completa
     *       }
     *     ]
     *   }
     * }
     *
     * response.data: Axios pone la respuesta JSON en .data
     * .choices[0]: Primera (y usualmente unica) opcion de respuesta
     * .message.content: El texto de la respuesta
     */

    console.log({ answer: answer.trim() });
    /**
     * MOSTRAR LA RESPUESTA:
     * console.log() con un objeto lo muestra en formato:
     *   { answer: 'La respuesta del modelo...' }
     *
     * .trim(): Elimina espacios y saltos de linea al inicio/final
     *
     * ALTERNATIVA mas bonita:
     *   console.log('\nRespuesta:', answer.trim());
     */

  } catch (error) {
    console.error('Error:', error.response?.data || error.message);
    /**
     * MANEJO DE ERRORES:
     *
     * error.response?.data:
     *   El ?. es "optional chaining" (encadenamiento opcional).
     *   Si error.response es undefined, no lanza error sino que
     *   devuelve undefined (en vez de "Cannot read property 'data'").
     *
     * Posibles errores:
     *   - 401 Unauthorized: Clave API invalida o expirada
     *   - 429 Too Many Requests: Limite de peticiones excedido
     *   - 500 Server Error: Error interno de OpenAI
     *   - ENOTFOUND: Sin conexion a internet
     *   - ECONNREFUSED: Servidor no disponible
     *
     * error.response?.data: Error de la API (con detalles)
     * error.message: Error de red o JavaScript (sin detalles de API)
     */
  } finally {
    rl.close();
    /**
     * BLOQUE FINALLY:
     * Se ejecuta SIEMPRE, sin importar si hubo error o no.
     *
     * rl.close(): Cierra la interfaz readline.
     * Esto es NECESARIO porque:
     * - Sin close(), el programa no termina (readline sigue escuchando)
     * - Es buena practica liberar recursos cuando ya no se necesitan
     *
     * PATRON TRY/CATCH/FINALLY:
     *   try {
     *     // Codigo que puede fallar
     *   } catch (error) {
     *     // Manejar el error
     *   } finally {
     *     // Limpiar recursos (SIEMPRE se ejecuta)
     *   }
     */
  }
});

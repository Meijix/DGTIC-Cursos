/**
 * ==========================================================================
 * MODULO 18 - INTRODUCCION A NODE.JS: Servidor Express + AWS DynamoDB + OpenAI
 * ==========================================================================
 *
 * PROPOSITO DE ESTE ARCHIVO:
 * Crear un servidor web con Node.js que:
 * 1. Lee datos de AWS DynamoDB (base de datos NoSQL en la nube)
 * 2. Envia esos datos a OpenAI para generar un resumen
 * 3. Devuelve el resumen como respuesta JSON
 *
 * QUE ES NODE.JS?
 * Node.js es un ENTORNO DE EJECUCION para JavaScript fuera del navegador.
 * Antes de Node.js, JavaScript SOLO podia correr dentro del navegador web.
 * Ahora puede correr en servidores, terminales, robots, IoT, etc.
 *
 * MOTOR V8:
 * Node.js usa el motor V8 de Google Chrome para ejecutar JavaScript.
 * V8 compila JavaScript a codigo maquina (muy rapido).
 *
 * EVENT LOOP (Bucle de Eventos):
 * Node.js es SINGLE-THREADED pero maneja miles de conexiones simultaneas
 * gracias al Event Loop:
 *
 *   ┌─────────────────────────────────┐
 *   │         CALL STACK              │  <-- Ejecuta codigo sincronico
 *   │  (Pila de llamadas)             │
 *   └──────────┬──────────────────────┘
 *              │
 *              ▼
 *   ┌─────────────────────────────────┐
 *   │       EVENT LOOP                │  <-- Revisa si hay tareas pendientes
 *   │  (Bucle de eventos)             │
 *   └──────────┬──────────────────────┘
 *              │
 *       ┌──────┴──────┐
 *       ▼             ▼
 *   ┌────────┐  ┌───────────┐
 *   │Microtask│  │ Callback  │  <-- Tareas asincronicas completadas
 *   │ Queue  │  │  Queue    │
 *   │(Promise)│  │(setTimeout│
 *   │        │  │ I/O, etc) │
 *   └────────┘  └───────────┘
 *
 * Esto significa que operaciones lentas (leer BD, llamar APIs, leer archivos)
 * NO bloquean el servidor. Mientras espera una respuesta de DynamoDB,
 * Node.js puede atender otras peticiones HTTP.
 *
 * COMPARACION NODE.JS vs PHP (para estudiantes del modulo 13-17):
 *
 *   Caracteristica     | PHP (Laravel)          | Node.js (Express)
 *   -------------------|------------------------|--------------------------
 *   Lenguaje           | PHP                    | JavaScript
 *   Modelo             | Multi-thread           | Single-thread + Event Loop
 *   Paquetes           | Composer               | npm
 *   Framework web      | Laravel                | Express.js
 *   Base de datos      | MySQL/PostgreSQL       | MongoDB/DynamoDB/MySQL
 *   Plantillas         | Blade                  | EJS/Pug/Handlebars
 *   Tiempo real        | Requiere WebSockets    | Nativo con Socket.io
 *   Servidor           | Apache/Nginx           | El propio Node.js
 *
 * COMANDOS PARA EMPEZAR:
 *   npm init -y                        // Inicializa un proyecto Node.js
 *   npm install express dotenv openai @aws-sdk/client-dynamodb @aws-sdk/lib-dynamodb
 *
 * ARCHIVO .env NECESARIO:
 *   AWS_REGION=us-east-1
 *   DYNAMO_TABLE=YourDynamoTable
 *   OPENAI_API_KEY=sk-...
 *   PORT=3000
 */

// =====================================================================
// SECCION 1: IMPORTACION DE MODULOS
// =====================================================================
//
// require() es la forma de importar modulos en Node.js (sistema CommonJS).
//
// COMMONJS vs ES MODULES:
//   CommonJS (antiguo, por defecto en Node.js):
//     const express = require('express');
//     module.exports = { miFuncion };
//
//   ES Modules (moderno, nativo en navegadores):
//     import express from 'express';
//     export { miFuncion };
//
// Para usar ES Modules en Node.js, necesitas:
//   - Agregar "type": "module" en package.json, O
//   - Usar extension .mjs en vez de .js
//
// En este archivo usamos CommonJS (require) que es lo mas comun en tutoriales.
// =====================================================================

require('dotenv').config();                      // Cargar variables del archivo .env
/**
 * dotenv: Lee el archivo .env y pone sus variables en process.env
 *
 * ANTES de dotenv:
 *   process.env.OPENAI_API_KEY  ->  undefined
 *
 * DESPUES de require('dotenv').config():
 *   process.env.OPENAI_API_KEY  ->  "sk-..."
 *
 * POR QUE USAR .env?
 * - Las claves API son SECRETAS (nunca deben ir en el codigo fuente)
 * - Cada entorno (desarrollo, produccion) tiene claves diferentes
 * - El archivo .env se agrega a .gitignore (nunca se sube a Git)
 *
 * REGLA DE ORO: NUNCA hacer commit de claves API, contrasenas o secretos.
 * Si una clave se sube a GitHub, se considera COMPROMETIDA y debe rotarse.
 */

const express = require('express');              // Framework para crear servidores HTTP
/**
 * EXPRESS.JS: El framework web mas popular de Node.js.
 *
 * Express simplifica la creacion de servidores HTTP:
 * - Sin Express: usar el modulo 'http' nativo (muy verboso)
 * - Con Express: API limpia y middleware pipeline
 *
 * Express es MINIMALISTA: solo hace routing y middleware.
 * Para todo lo demas, instalas paquetes adicionales.
 *
 * ANALOGIA CON LARAVEL:
 *   Laravel = framework "con baterias incluidas" (ORM, auth, mail, etc.)
 *   Express = framework minimalista (tu eliges que agregar)
 */

const { Configuration, OpenAIApi } = require('openai');
/**
 * OPENAI SDK: Cliente oficial para la API de OpenAI.
 *
 * DESESTRUCTURACION { Configuration, OpenAIApi }:
 * El paquete 'openai' exporta un objeto con muchas clases.
 * Solo importamos las que necesitamos:
 *   Configuration -> Para configurar la clave API
 *   OpenAIApi    -> Para hacer peticiones a la API
 *
 * NOTA: Esta es la version 3.x del SDK de OpenAI.
 * La version 4.x usa una API diferente:
 *   const OpenAI = require('openai');
 *   const openai = new OpenAI({ apiKey: process.env.OPENAI_API_KEY });
 */

const { DynamoDBClient } = require('@aws-sdk/client-dynamodb');
const { DynamoDBDocumentClient, GetCommand } = require('@aws-sdk/lib-dynamodb');
/**
 * AWS SDK v3: Cliente para servicios de Amazon Web Services.
 *
 * AWS SDK v3 es MODULAR (importas solo lo que necesitas):
 *   @aws-sdk/client-dynamodb  -> Cliente base de DynamoDB
 *   @aws-sdk/lib-dynamodb     -> Capa de alto nivel (DocumentClient)
 *
 * QUE ES DYNAMODB?
 * DynamoDB es una base de datos NoSQL de AWS:
 * - No tiene esquema fijo (cada item puede tener campos diferentes)
 * - Escala automaticamente (de 1 a millones de peticiones por segundo)
 * - Baja latencia (respuestas en milisegundos)
 * - Servicio completamente administrado (no necesitas instalar nada)
 *
 * COMPARACION SQL vs NoSQL:
 *   MySQL (SQL):     Tablas con filas y columnas fijas
 *   DynamoDB (NoSQL): Colecciones con documentos flexibles (JSON)
 *
 * DynamoDBDocumentClient: Capa de ALTO NIVEL que simplifica operaciones.
 * Convierte automaticamente tipos de JavaScript a tipos de DynamoDB.
 *
 * GetCommand: Comando para obtener UN item por su clave primaria.
 * Otros comandos: PutCommand, DeleteCommand, ScanCommand, QueryCommand.
 */

// =====================================================================
// SECCION 2: CONFIGURACION DE LA APLICACION
// =====================================================================

// Crear una aplicación Express
const app = express();
/**
 * express() crea una INSTANCIA de la aplicacion Express.
 * Esta instancia 'app' es el objeto central de tu servidor:
 * - Configura middleware con app.use()
 * - Define rutas con app.get(), app.post(), etc.
 * - Inicia el servidor con app.listen()
 *
 * ANALOGIA: 'app' es como el archivo routes/web.php de Laravel,
 * pero tambien incluye la configuracion del servidor.
 */

app.use(express.json());                         // Permite recibir JSON en las solicitudes
/**
 * MIDDLEWARE express.json():
 * Parsea (analiza) el cuerpo de peticiones con Content-Type: application/json
 *
 * SIN este middleware:
 *   req.body -> undefined (Express no sabe leer JSON)
 *
 * CON este middleware:
 *   POST { "id": "123" }  ->  req.body -> { id: "123" }
 *
 * QUE ES UN MIDDLEWARE?
 * Es una funcion que se ejecuta ENTRE la peticion y la respuesta:
 *
 *   Peticion HTTP -> [Middleware 1] -> [Middleware 2] -> [Ruta] -> Respuesta
 *
 * Ejemplos de middleware comunes:
 *   express.json()    -> Parsear JSON
 *   cors()            -> Permitir peticiones cross-origin
 *   morgan()          -> Logging de peticiones
 *   helmet()          -> Seguridad HTTP
 *   authMiddleware()  -> Verificar autenticacion
 *
 * ANALOGIA CON LARAVEL:
 *   En Laravel, los middleware estan en app/Http/Middleware/
 *   y se registran en app/Http/Kernel.php
 *   En Express, se registran con app.use()
 */

// =====================================================================
// SECCION 3: CONFIGURACION DE AWS
// =====================================================================

// Configurar AWS
const awsRegion = process.env.AWS_REGION || 'us-east-1';
/**
 * process.env.AWS_REGION: Lee la region de AWS desde variables de entorno.
 * El operador || proporciona un valor por defecto si la variable no existe.
 *
 * REGIONES DE AWS: Son centros de datos distribuidos globalmente.
 *   us-east-1     -> Virginia (la mas comun)
 *   us-west-2     -> Oregon
 *   eu-west-1     -> Irlanda
 *   sa-east-1     -> Sao Paulo (la mas cercana a Mexico)
 *
 * La region determina DONDE estan tus datos fisicamente.
 * Elegir una region cercana a tus usuarios reduce la latencia.
 */

const dynamoClient = new DynamoDBClient({ region: awsRegion });
/**
 * DynamoDBClient: Cliente de BAJO NIVEL para DynamoDB.
 * Solo necesita la region para saber a que servidor de AWS conectarse.
 *
 * La autenticacion con AWS se maneja automaticamente:
 * 1. Variables de entorno: AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY
 * 2. Archivo de credenciales: ~/.aws/credentials
 * 3. IAM Role (si corres en EC2, Lambda, etc.)
 */

const ddbDocClient = DynamoDBDocumentClient.from(dynamoClient);
/**
 * DocumentClient: Capa de ALTO NIVEL sobre DynamoDBClient.
 *
 * DIFERENCIA:
 *   Bajo nivel: { id: { S: "123" }, name: { S: "Ana" } }  (tipos DynamoDB)
 *   Alto nivel: { id: "123", name: "Ana" }  (JavaScript normal)
 *
 * DocumentClient convierte automaticamente entre los dos formatos.
 */

// =====================================================================
// SECCION 4: CONFIGURACION DE OPENAI
// =====================================================================

// Configurar OpenAI
if (!process.env.OPENAI_API_KEY) {
  console.error('Falta la clave OPENAI_API_KEY');
  process.exit(1);
}
/**
 * VALIDACION TEMPRANA de configuracion:
 * Si falta la clave API, el servidor se detiene INMEDIATAMENTE.
 *
 * process.exit(1):
 *   0 = salida exitosa
 *   1 = salida con error
 *
 * Es mejor fallar RAPIDO al iniciar que fallar DESPUES cuando un
 * usuario intenta usar la funcionalidad.
 * Este patron se llama "fail fast" (fallar temprano).
 */

const openai = new OpenAIApi(
  new Configuration({ apiKey: process.env.OPENAI_API_KEY })
);
/**
 * Configuracion del cliente OpenAI (v3):
 *
 * 1. Configuration: Objeto que contiene la clave API
 * 2. OpenAIApi: Cliente que hace las peticiones a la API
 *
 * NOTA SOBRE VERSIONES:
 * Este codigo usa openai SDK v3. En v4 (mas reciente), la sintaxis es:
 *   const OpenAI = require('openai');
 *   const openai = new OpenAI({ apiKey: process.env.OPENAI_API_KEY });
 *   const completion = await openai.chat.completions.create({...});
 */

// =====================================================================
// SECCION 5: DEFINICION DE RUTAS (ENDPOINTS)
// =====================================================================

// Ruta básica para probar si el servidor funciona
app.get('/health', (_req, res) => {
  res.status(200).json({ status: 'ok', timestamp: Date.now() });
});
/**
 * ENDPOINT DE HEALTH CHECK:
 * Es una ruta simple que confirma que el servidor esta funcionando.
 *
 * USOS:
 * - Monitoreo automatizado (AWS, Datadog, etc.)
 * - Load balancers necesitan saber si el servidor esta vivo
 * - Desarrollo: verificar que el servidor inicio correctamente
 *
 * ANATOMIA DE UNA RUTA EXPRESS:
 *   app.get('/health', (_req, res) => { ... })
 *   |   |      |        |     |
 *   |   |      |        |     +-- res: objeto Response (para enviar respuesta)
 *   |   |      |        +-- _req: objeto Request (con _ porque no se usa)
 *   |   |      +-- Path: la URL relativa
 *   |   +-- Metodo HTTP (GET, POST, PUT, DELETE)
 *   +-- La aplicacion Express
 *
 * res.status(200): Establece el codigo de estado HTTP
 * .json({...}): Envia la respuesta como JSON
 *
 * CODIGOS DE ESTADO HTTP:
 *   200 OK              -> Todo bien
 *   201 Created         -> Recurso creado exitosamente
 *   400 Bad Request     -> Error del cliente (datos invalidos)
 *   401 Unauthorized    -> No autenticado
 *   403 Forbidden       -> Sin permisos
 *   404 Not Found       -> Recurso no encontrado
 *   500 Internal Error  -> Error del servidor
 */

// Ruta principal para procesar texto desde DynamoDB usando OpenAI
app.post('/process', async (req, res) => {
  /**
   * ENDPOINT POST /process:
   * Esta es la ruta principal de la API. Recibe un ID, busca el item
   * en DynamoDB, y usa OpenAI para generar un resumen.
   *
   * FLUJO:
   *   1. Cliente envia: POST /process { "id": "abc123" }
   *   2. Servidor busca el item en DynamoDB
   *   3. Servidor envia el texto a OpenAI para resumir
   *   4. Servidor devuelve: { "id": "abc123", "summary": "..." }
   *
   * ASYNC/AWAIT:
   * La funcion es async porque hace operaciones ASINCRONICAS:
   *   - Leer de DynamoDB (I/O de red)
   *   - Llamar a OpenAI (I/O de red)
   *
   * await PAUSA la funcion hasta que la operacion termine,
   * PERO no bloquea el Event Loop (otras peticiones se siguen procesando).
   *
   * EVOLUCION DEL CODIGO ASINCRONO EN NODE.JS:
   *   1. CALLBACKS (antiguo, dificil de leer):
   *      dynamoDB.get(params, function(err, data) {
   *        if (err) { ... }
   *        openai.create(params2, function(err2, result) { ... })
   *      });
   *
   *   2. PROMISES (mejor, pero encadenamientos largos):
   *      dynamoDB.get(params)
   *        .then(data => openai.create(params2))
   *        .then(result => res.json(result))
   *        .catch(err => res.status(500).json(err));
   *
   *   3. ASYNC/AWAIT (moderno, se lee como codigo sincronico):
   *      const data = await dynamoDB.get(params);
   *      const result = await openai.create(params2);
   *      res.json(result);
   */

  const { id } = req.body;  // Leer "id" desde el cuerpo JSON de la petición
  /**
   * DESESTRUCTURACION de req.body:
   * const { id } = req.body es equivalente a: const id = req.body.id
   *
   * req.body contiene el cuerpo JSON de la peticion HTTP.
   * Solo funciona si express.json() esta configurado como middleware.
   */

  const tableName = process.env.DYNAMO_TABLE;

  if (!id || !tableName) {
    return res.status(400).json({ error: 'id y DYNAMO_TABLE son requeridos' });
  }
  /**
   * VALIDACION DE ENTRADA:
   * Siempre validar los datos ANTES de usarlos:
   * - !id: El cliente no envio un ID
   * - !tableName: No se configuro la variable de entorno
   *
   * Status 400 = Bad Request (error del cliente, no del servidor)
   *
   * El "return" es importante: detiene la ejecucion de la funcion.
   * Sin return, el codigo seguiria ejecutandose despues del error.
   */

  try {
    /**
     * TRY/CATCH: Manejo de errores en codigo asincrono.
     *
     * Si CUALQUIER await dentro del try lanza un error,
     * la ejecucion salta inmediatamente al catch.
     *
     * Esto es CRITICO en aplicaciones de servidor porque:
     * - Una excepcion no capturada puede MATAR todo el proceso de Node.js
     * - El cliente quedaria sin respuesta
     * - Otros usuarios se verian afectados
     */

    // 1. Leer item desde DynamoDB
    const getResult = await ddbDocClient.send(
      new GetCommand({ TableName: tableName, Key: { id } })
    );
    /**
     * OPERACION GET EN DYNAMODB:
     * Busca UN item por su clave primaria (partition key).
     *
     * ANALOGIA CON SQL:
     *   SQL:      SELECT * FROM customers WHERE id = 'abc123'
     *   DynamoDB: GetCommand({ TableName: 'customers', Key: { id: 'abc123' } })
     *
     * ddbDocClient.send(): Envia el comando a AWS.
     * await: Espera la respuesta (sin bloquear el Event Loop).
     * getResult.Item: El item encontrado (o undefined si no existe).
     */

    const item = getResult.Item;
    if (!item) {
      return res.status(404).json({ error: 'Item no encontrado' });
    }

    // 2. Enviar el texto a OpenAI para resumir
    const textToSummarise = item.text || JSON.stringify(item);
    /**
     * PREPARACION DEL TEXTO:
     * - Si el item tiene un campo 'text', lo usa directamente
     * - Si no, convierte TODO el item a texto JSON
     * - JSON.stringify() convierte un objeto JS a string JSON
     *
     * Esto es FLEXIBLE: funciona sin importar la estructura del item.
     */

    const completion = await openai.createChatCompletion({
      model: 'gpt-4o-mini',
      messages: [
        {
          role: 'system',
          content: 'Eres un asistente útil que escribe resúmenes en español.'
        },
        {
          role: 'user',
          content: `Resume este texto en 3 oraciones:\n\n${textToSummarise}`
        }
      ],
      max_tokens: 200
    });
    /**
     * LLAMADA A LA API DE OPENAI:
     *
     * MODELO: 'gpt-4o-mini' (rapido y economico)
     * Otros modelos: 'gpt-4o' (potente), 'gpt-3.5-turbo' (clasico)
     *
     * MENSAJES (Chat Completions API):
     * La API usa un formato de CONVERSACION con roles:
     *
     *   'system': Define el COMPORTAMIENTO del asistente
     *             Es como las "instrucciones" que le das.
     *             El usuario final NO ve este mensaje.
     *
     *   'user':   El mensaje del usuario (la pregunta/instruccion)
     *
     *   'assistant': Respuestas previas del modelo (para contexto)
     *                No se usa aqui porque es una sola pregunta.
     *
     * PROMPT ENGINEERING:
     * La forma en que redactas el prompt IMPORTA MUCHO:
     *   Malo:  "Resume esto"
     *   Bueno: "Resume este texto en 3 oraciones"
     *   Mejor: "Eres un asistente util. Resume en 3 oraciones en espanol."
     *
     * max_tokens: Limita la longitud de la respuesta.
     * Un token es aproximadamente 3/4 de una palabra en espanol.
     * 200 tokens = aproximadamente 150 palabras.
     */

    const summary = completion.data.choices[0].message.content.trim();
    /**
     * EXTRAER LA RESPUESTA:
     * La API de OpenAI devuelve un objeto complejo:
     *   completion.data.choices[0].message.content
     *
     * Estructura de la respuesta:
     *   {
     *     data: {
     *       choices: [
     *         {
     *           message: {
     *             role: "assistant",
     *             content: "El resumen del texto..."
     *           }
     *         }
     *       ]
     *     }
     *   }
     *
     * .trim(): Elimina espacios en blanco al inicio y final.
     */

    // 3. Enviar respuesta con el resumen generado
    return res.status(200).json({ id, summary });
    /**
     * RESPUESTA EXITOSA:
     * Status 200 = OK
     * { id, summary } es shorthand para { id: id, summary: summary }
     *
     * El cliente recibe algo como:
     * {
     *   "id": "abc123",
     *   "summary": "El texto trata sobre... En resumen..."
     * }
     */

  } catch (err) {
    console.error('Error en /process', err);
    return res.status(500).json({ error: 'Error interno', detalles: err.message });
    /**
     * MANEJO DE ERRORES:
     * Si DynamoDB o OpenAI fallan, capturamos el error y:
     * 1. Lo registramos en el servidor (console.error) para debugging
     * 2. Enviamos una respuesta generica al cliente (status 500)
     *
     * IMPORTANTE: No enviar detalles internos al cliente en produccion.
     * err.message podria contener informacion sensible (claves, rutas, etc.)
     * En produccion, solo enviar: { error: 'Error interno del servidor' }
     */
  }
});

// =====================================================================
// SECCION 6: INICIAR EL SERVIDOR
// =====================================================================

// Iniciar el servidor en el puerto especificado
const port = process.env.PORT || 3000;
/**
 * PUERTO DEL SERVIDOR:
 * El puerto es como una "puerta" en tu computadora.
 * Cada aplicacion usa un puerto diferente:
 *   Puerto 80:   HTTP (web)
 *   Puerto 443:  HTTPS (web segura)
 *   Puerto 3000: Desarrollo Node.js (convencion)
 *   Puerto 3306: MySQL
 *   Puerto 5432: PostgreSQL
 *   Puerto 8000: Desarrollo Laravel (php artisan serve)
 *
 * process.env.PORT || 3000:
 * - En desarrollo: usa 3000
 * - En produccion (AWS, Heroku): el servicio asigna el puerto via env
 */

app.listen(port, () => {
  console.log(`🚀 Servidor escuchando en http://localhost:${port}`);
});
/**
 * app.listen(): Inicia el servidor HTTP.
 *
 * DIFERENCIA CON PHP:
 * - PHP necesita Apache/Nginx como servidor (php artisan serve es solo dev)
 * - Node.js ES el servidor (no necesita Apache ni Nginx)
 *
 * El callback se ejecuta DESPUES de que el servidor este listo.
 * Si hay un error (puerto ocupado, permisos), se lanza una excepcion.
 *
 * PARA PROBAR ESTE SERVIDOR:
 *   1. Crear archivo .env con las variables necesarias
 *   2. npm install
 *   3. node index.js
 *   4. Abrir http://localhost:3000/health en el navegador
 *   5. Usar curl o Postman para POST /process:
 *      curl -X POST http://localhost:3000/process \
 *        -H "Content-Type: application/json" \
 *        -d '{"id": "mi-item"}'
 */

/*
 * index.js – Starter Node.js server for AWS + DynamoDB + OpenAI
 * ------------------------------------------------------------
 * Este archivo contiene lo esencial para comenzar a trabajar con Node.js,
 * especialmente si estás empezando. Incluye ejemplos básicos de cómo:
 *   - Crear un servidor usando Express
 *   - Leer variables de entorno con dotenv
 *   - Hacer llamadas HTTP a APIs
 *   - Conectarse a DynamoDB y OpenAI
 *
 * Comandos básicos para empezar:
 *   npm init -y                        // Inicializa un proyecto Node.js
 *   npm install express dotenv openai @aws-sdk/client-dynamodb @aws-sdk/lib-dynamodb
 *
 * Crea un archivo .env con:
 *   AWS_REGION=us-east-1
 *   DYNAMO_TABLE=YourDynamoTable
 *   OPENAI_API_KEY=sk-...
 *   PORT=3000
 */

// Importación de módulos
require('dotenv').config();                      // Cargar variables del archivo .env
const express = require('express');              // Framework para crear servidores HTTP
const { Configuration, OpenAIApi } = require('openai');
const { DynamoDBClient } = require('@aws-sdk/client-dynamodb');
const { DynamoDBDocumentClient, GetCommand } = require('@aws-sdk/lib-dynamodb');

// Crear una aplicación Express
const app = express();
app.use(express.json());                         // Permite recibir JSON en las solicitudes

// Configurar AWS
const awsRegion = process.env.AWS_REGION || 'us-east-1';
const dynamoClient = new DynamoDBClient({ region: awsRegion });
const ddbDocClient = DynamoDBDocumentClient.from(dynamoClient);

// Configurar OpenAI
if (!process.env.OPENAI_API_KEY) {
  console.error('Falta la clave OPENAI_API_KEY');
  process.exit(1);
}
const openai = new OpenAIApi(
  new Configuration({ apiKey: process.env.OPENAI_API_KEY })
);

// Ruta básica para probar si el servidor funciona
app.get('/health', (_req, res) => {
  res.status(200).json({ status: 'ok', timestamp: Date.now() });
});

// Ruta principal para procesar texto desde DynamoDB usando OpenAI
app.post('/process', async (req, res) => {
  const { id } = req.body;  // Leer "id" desde el cuerpo JSON de la petición
  const tableName = process.env.DYNAMO_TABLE;

  if (!id || !tableName) {
    return res.status(400).json({ error: 'id y DYNAMO_TABLE son requeridos' });
  }

  try {
    // 1. Leer item desde DynamoDB
    const getResult = await ddbDocClient.send(
      new GetCommand({ TableName: tableName, Key: { id } })
    );
    const item = getResult.Item;
    if (!item) {
      return res.status(404).json({ error: 'Item no encontrado' });
    }

    // 2. Enviar el texto a OpenAI para resumir
    const textToSummarise = item.text || JSON.stringify(item);

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

    const summary = completion.data.choices[0].message.content.trim();

    // 3. Enviar respuesta con el resumen generado
    return res.status(200).json({ id, summary });
  } catch (err) {
    console.error('Error en /process', err);
    return res.status(500).json({ error: 'Error interno', detalles: err.message });
  }
});

// Iniciar el servidor en el puerto especificado
const port = process.env.PORT || 3000;
app.listen(port, () => {
  console.log(`🚀 Servidor escuchando en http://localhost:${port}`);
});

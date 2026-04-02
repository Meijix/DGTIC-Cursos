# 🧠 Aprendiendo Node.js con AWS, DynamoDB y OpenAI

¡Bienvenida/o a mi viaje de aprendizaje de Node.js! 🚀  
Este repositorio contiene ejemplos, apuntes y prácticas enfocadas en construir aplicaciones backend modernas usando **Node.js**, con especial énfasis en integraciones con **AWS (DynamoDB, Lambda, API Gateway)** y **OpenAI**.

---

## 🎯 Objetivo general


- Entender cómo funciona Node.js desde cero.
- Aprender a crear servidores HTTP básicos.
- Usar Express.js para construir APIs RESTful.
- Conectar con bases de datos (como MongoDB).
- Manejar rutas, middlewares y errores.
- Desplegar una aplicación real en la nube.


Dominar Node.js lo suficiente para:

- Leer datos desde **DynamoDB**
- Procesarlos con **funciones Lambda**
- Aplicar inteligencia artificial usando **OpenAI**
- Enviar los resultados a un **sistema ERP**
- Exponer todo esto vía **API Gateway** con endpoints HTTP

---

## 📚 Ruta de aprendizaje personalizada

A continuación, los módulos y temas que estoy abordando. Cada carpeta del repo representa un paso práctico en esta ruta:

### ✅ Fundamentos de Node.js
- [ ] Estructura básica de un proyecto (`package.json`, `npm`)
- [ ] Uso de `require`, `import/export`
- [ ] Manejo de `async/await` y `promises`
- [ ] Llamadas HTTP con `axios` o `fetch`
- [ ] JSON, estructuras de datos y errores

📁 Carpeta: `01-node-fundamentos/`

---

### ✅ Node.js + AWS SDK
- [ ] Conexión con DynamoDB
- [ ] Lectura y escritura usando el cliente `DocumentClient`
- [ ] Configuración con variables de entorno

📁 Carpeta: `02-dynamodb-node/`

---

### ✅ Funciones AWS Lambda con Node.js
- [ ] Estructura de una función Lambda
- [ ] Lectura de eventos y cuerpos HTTP
- [ ] Integración con DynamoDB y OpenAI
- [ ] Manejo de errores y respuestas HTTP

📁 Carpeta: `03-lambdas-aws/`

---

### ✅ API Gateway
- [ ] Crear endpoints que invoquen Lambdas
- [ ] Configurar rutas como `/api/procesar`
- [ ] Probar desde Postman o curl
- [ ] Deploy de APIs seguras

📁 Carpeta: `04-api-gateway/`

---

### ✅ OpenAI con Node.js
- [ ] Uso del SDK oficial (`openai`)
- [ ] Autenticación con API Key
- [ ] Enviar texto para resumen, clasificación, transformación
- [ ] Usar la respuesta de OpenAI dentro de un flujo

📁 Carpeta: `05-openai-integration/`

---

### ✅ Integración con ERP
- [ ] Formatear y transformar datos para un ERP
- [ ] Enviar datos a un webhook o endpoint externo
- [ ] Autenticación con token u OAuth (pendiente)

📁 Carpeta: `06-enviar-a-erp/`

---

## 🛠 Tecnologías que estoy usando

- **Node.js**
- **Express.js** (para probar localmente algunas rutas)
- **AWS Lambda**
- **Amazon DynamoDB**
- **API Gateway**
- **OpenAI SDK**
- **axios**
- **dotenv**

---

## 💡 Ideas de práctica futura

- [ ] Crear panel de control con React que consuma estas APIs
- [ ] Agregar autenticación con tokens JWT
- [ ] Desplegar con Serverless Framework o SAM
- [ ] Testing automatizado con Jest

---

## 📌 Recursos útiles

- [Node.js Docs](https://nodejs.org/en/docs)
- [AWS Lambda + Node.js](https://docs.aws.amazon.com/lambda/latest/dg/nodejs-handler.html)
- [DynamoDB SDK v3](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/clients/client-dynamodb/)
- [OpenAI API Docs](https://platform.openai.com/docs)
- [Serverless Framework](https://www.serverless.com/)

---

## 👩‍💻 Autora

**Natalia Mejia**  
Aprendiendo a construir soluciones serverless, escalables e inteligentes con JavaScript y AWS ☁️  
Contacto: `natalia.mejbau@gmail.com`

---

## 📝 Licencia

MIT – Libre para usar y modificar.




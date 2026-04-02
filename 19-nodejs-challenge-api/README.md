# Challenge Node.js
Mini Challenge with NodeJS
No frontend or database is required. You can build everything locally.

## Console task using NodeJS
Create a script index.js that does the following:

When run with node index.js, it prompts the user:
> Ask me something:

It captures the user's question via the terminal.

It sends that question to the OpenAI API using the provided API key.

It prints the result as a JSON object like this:

{ "answer": "Your response from OpenAI goes here." }
Para usar este proyecto necesitas una API key de OpenAI. Configúrala en un archivo .env:
OPENAI_API_KEY=tu-api-key-aqui
We recommend using axios to make the request.

## Bonus, with Express:
If you finish early, try extending it with a simple API server:

Create a server.js file using Express.

Add a POST endpoint /ask.

It should accept a JSON body like:

{ "question": "What is the speed of light?" }
It should return a response like:

{ "answer": "The speed of light is approximately 299,792,458 meters per second." }

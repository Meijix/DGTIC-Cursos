const express = require('express');
const axios = require('axios');

const app = express();
const PORT = 3000;

//leer JSON
app.use(express.json());

//clave API de OpenAI
const API_KEY = 'TU_API_KEY_AQUI'; // Reemplázala si es necesario

// Ruta POST /ask
app.post('/ask', async (req, res) => {
  const userQuestion = req.body.question;

  if (!userQuestion) {
    return res.status(400).json({ error: 'Missing question in body.' });
  }

  try {
    const response = await axios.post(
      'https://api.openai.com/v1/chat/completions',
      {
        model: 'gpt-3.5-turbo',
        messages: [{ role: 'user', content: userQuestion }]
      },
      {
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${API_KEY}`
        }
      }
    );

    const answer = response.data.choices[0].message.content.trim();
    res.json({ answer });

  } catch (error) {
    console.error('Error:', error.response?.data || error.message);
    res.status(500).json({ error: 'Error fetching from OpenAI' });
  }
});

// Iniciar servidor
app.listen(PORT, () => {
  console.log(`Server running at http://localhost:${PORT}`);
});

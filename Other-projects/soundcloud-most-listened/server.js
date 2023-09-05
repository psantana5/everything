const express = require('express');
const fetch = require('node-fetch');
const app = express();
const PORT = process.env.PORT || 3000;

app.use(express.json());

app.post('/getDocumentation', async (req, res) => {
    const query = req.body.prompt;
    try {
        const response = await fetch('https://api.openai.com/v1/chat/completions', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${process.env.OPENAI_API_KEY}`
            },
            body: JSON.stringify({
                prompt: query
            })
        });

        const data = await response.json();
        res.json({ documentation: data.choices[0].text });
    } catch (error) {
        console.error("An error occurred:", error);
        res.status(500).json({ error: 'An error occurred while fetching documentation.' });
    }
});


app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});

// integrate_with_ai.js
const fetch = require('node-fetch');

async function getSecurityInsight(processedData) {
  const prompt = `Given the following context: "${processedData}", provide cybersecurity insights and recommendations.`;
  const response = await fetch('https://api.openai.com/v1/chat/completions', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${process.env.OPENAI_API_KEY}`
    },
    body: JSON.stringify({
      model: 'gpt-4',
      messages: [
        { role: 'system', content: 'You are a cybersecurity AI assistant.' },
        { role: 'user', content: prompt }
      ],
      max_tokens: 150,
      temperature: 0.7
    })
  });
  const data = await response.json();
  return data.choices[0].message.content.trim();
}

(async () => {
  const processedData = "Anomalous network traffic detected from IP 10.0.0.5.";
  const insight = await getSecurityInsight(processedData);
  console.log("Cybersecurity Insight:", insight);
})();

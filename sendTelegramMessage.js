// Importação das bibliotecas
const fetch = require('node-fetch');
require('dotenv').config();

// Configurações
const botToken = process.env.TELEGRAM_BOT_TOKEN;
const chatId = process.env.TELEGRAM_CHAT_ID;
const message = "Olá, mundo! Esta é uma mensagem de teste.";

// URL da API do Telegram
const apiUrl = `https://api.telegram.org/bot${botToken}/sendMessage`;

// Objeto de requisição
const requestOptions = {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ chat_id: chatId, text: message })
};

// Função para enviar a mensagem
async function sendTelegramMessage() {
    try {
        const response = await fetch(apiUrl, requestOptions);
        const data = await response.json();
        console.log('Mensagem enviada:', data);
    } catch (error) {
        console.error('Erro ao enviar mensagem:', error);
    }
}

// Chamada da função para enviar a mensagem
sendTelegramMessage();
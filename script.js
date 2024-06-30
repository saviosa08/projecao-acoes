const fetch = require('node-fetch');

// Token do seu bot do Telegram
const BOT_TOKEN = 'COLOQUE_AQUI_O_SEU_TOKEN_DO_BOT';

// ID do chat onde você deseja enviar a mensagem (pode ser um chat privado com o bot)
const CHAT_ID = 'COLOQUE_AQUI_O_CHAT_ID';

// Texto da mensagem que você deseja enviar
const message = 'Olá! Esta é uma mensagem de teste enviada pelo meu bot do Telegram.';

// URL da API do Telegram para enviar mensagem
const telegramUrl = `https://api.telegram.org/bot${BOT_TOKEN}/sendMessage`;

// Parâmetros da requisição
const params = {
    chat_id: CHAT_ID,
    text: message,
};

// Configurações da requisição
const requestOptions = {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify(params),
};

// Enviar a mensagem via API do Telegram
fetch(telegramUrl, requestOptions)
    .then(response => response.json())
    .then(result => {
        console.log('Mensagem enviada com sucesso:', result);
    })
    .catch(error => {
        console.error('Erro ao enviar mensagem:', error);
    });

import requests
import datetime
import time
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.key_management import get_api_key
from telegram.ext import Updater, CommandHandler
import pandas as pd
import numpy as np
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt

# Chave da API do Alpha Vantage (substitua pela sua chave)
ALPHA_VANTAGE_API_KEY = 'sua_chave_aqui'

# Token do bot do Telegram (substitua pelo seu token)
TELEGRAM_BOT_TOKEN = 'seu_token_aqui'

# Lista de ações para verificar
acoes = ['AAPL', 'GOOGL', 'MSFT']  # Exemplo de lista de ações

# Função para calcular a projeção do valor da ação para a próxima semana usando ARIMA
def calcular_projecao_valor_acao(symbol):
    ts = TimeSeries(key=ALPHA_VANTAGE_API_KEY, output_format='pandas')
    data, meta_data = ts.get_daily(symbol=symbol, outputsize='compact')

    # Ajuste o modelo ARIMA
    model = ARIMA(data['4. close'], order=(5,1,0))  # Exemplo de ordem (p, d, q)
    model_fit = model.fit()

    # Fazendo a projeção para a próxima semana (5 dias úteis)
    forecast = model_fit.forecast(steps=5)

    # Valor projetado para a próxima semana (média dos valores projetados)
    valor_projecao = np.mean(forecast)

    return valor_projecao

# Função para enviar mensagem formatada para o Telegram
def enviar_mensagem_telegram(chat_id, text):
    updater = Updater(token=TELEGRAM_BOT_TOKEN, use_context=True)
    updater.bot.send_message(chat_id=chat_id, text=text)

# Função principal para executar o script
def main():
    for acao in acoes:
        valor_projecao = calcular_projecao_valor_acao(acao)
        mensagem = f'{acao}: {valor_projecao:.2f}'  # Formato para duas casas decimais
        enviar_mensagem_telegram(chat_id='seu_chat_id_telegram', text=mensagem)
        time.sleep(2)  # Aguarda 2 segundos entre cada mensagem (evitar limites de API)

if __name__ == '__main__':
    main()
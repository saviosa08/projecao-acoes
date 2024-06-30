import requests
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
from telegram import Bot

# Configurações
API_KEY = 'LM9RP358619S046Q'
SYMBOL = 'PETR4.SA'
TELEGRAM_TOKEN = '7486305961:AAHNaYir4Cf4Vq6TFhdMhpULX64OiUHXQpc'
CHAT_IDS = ['447938340', '6452451093']  # Lista com os IDs dos chats

# Passo 1: Requisição à API do Alpha Vantage
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={SYMBOL}&apikey={API_KEY}'
response = requests.get(url)
data = response.json()

# Converter os dados para um DataFrame
df = pd.DataFrame(data['Time Series (Daily)']).T
df.columns = ['open', 'high', 'low', 'close', 'volume']
df = df.apply(pd.to_numeric)
df.index = pd.to_datetime(df.index)

# Usar apenas a coluna de fechamento para o modelo ARIMA
df_close = df['close']

# Passo 2: Análise dos Dados e Projeção com ARIMA
model = ARIMA(df_close, order=(5, 1, 0))
model_fit = model.fit()
forecast = model_fit.forecast(steps=7)
forecast_dates = pd.date_range(start=df.index[-1], periods=8, inclusive='right')

# Passo 3: Envio da Mensagem via Bot do Telegram
message = "Projeção dos valores da ação PETR4.SA para os próximos 7 dias:\n"
for date, value in zip(forecast_dates, forecast):
    message += f"{date.date()}: {value:.2f}\n"

bot = Bot(token=TELEGRAM_TOKEN)
for chat_id in CHAT_IDS:
    bot.send_message(chat_id=chat_id, text=message)

print("Mensagens enviadas com sucesso!")
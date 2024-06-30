import requests
import datetime
import time

# Token do seu bot no Telegram
TOKEN = '7486305961:AAHNaYir4Cf4Vq6TFhdMhpULX64OiUHXQpc'

# Chat ID onde a mensagem será enviada
CHAT_ID = '447938340'

def send_telegram_message(message):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    data = {'chat_id': CHAT_ID, 'text': message}
    response = requests.post(url, data=data)
    return response.json()

def main():
    message = "Esta é uma mensagem de teste para o Telegram!"
    send_telegram_message(message)

if __name__ == "__main__":
    main()

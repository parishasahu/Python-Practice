import requests

def send_telegram_message(message, chat_id):
    bot_token = "8478469633:AAEovsFIOVfA1oI9t6MqEmi2wZeaJyFbWIE" # message botfather for api key
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    params = {"chat_id": 7297809796, "text": message}

    
    response = requests.get(url, params=params, timeout=10)
    return response.json()

print(send_telegram_message("Hello world", 7297809796))
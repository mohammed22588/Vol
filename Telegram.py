import requests

def send_message_volume(message):
    bot_token = "8173508973:AAFBIrMcdpweiaE1a9L4IVqolynCmz_lMw8"
    bot_chatID = "-2493334574"
    send_text = "https://api.telegram.org/bot"+bot_token+"/sendMessage?chat_id="+bot_chatID+"&parse_mode=Markdown&text="+message
    response = requests.get(send_text)
    return response.json()
    
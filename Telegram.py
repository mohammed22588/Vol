import requests

def send_message_volume(message):
    bot_token = "8009228884:AAEB1BT0TkVrz5xKltI1WXCZ7aHje4cVkB8"  # توكن البوت
    bot_chatID = "-1002289303666"  # معرف القناة
    send_text = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={bot_chatID}&parse_mode=Markdown&text={message}"
    # إرسال الطلب عبر API
    response = requests.get(send_text)
    return response.json()  # إرجاع استجابة الخادم

def send_message_down(message):
    bot_tok = "8198786045:AAHHqcvH1Gmi9bTvDbNAB5nHSeFg0bcmIV4"  # توكن البوت
    bot_ch = "-1002434525520"  # معرف القناة
    send_text = f"https://api.telegram.org/bot{bot_tok}/sendMessage?chat_id={bot_ch}&parse_mode=Markdown&text={message}"
    # إرسال الطلب عبر API
    response = requests.get(send_text)
    return response.json()  # إرجاع استجابة الخادم
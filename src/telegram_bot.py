import requests

TOKEN = "8684691424:AAFyRnh0_yBy6298VKthXoAoR1iCZEG3mmE"
CHAT_ID = "1331660741"

def send_message(message):

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    requests.post(
        url,
        json={
            "chat_id": CHAT_ID,
            "text": message
        }
    )
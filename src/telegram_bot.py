import os
import requests

TOKEN = os.getenv("8684691424:AAFyRnh0_yBy6298VKthXoAoR1iCZEG3mmE")
CHAT_ID = os.getenv("1331660741")

def send_message(message):

    url = f"https://api.telegram.org/bot8684691424:AAFyRnh0_yBy6298VKthXoAoR1iCZEG3mmE/sendMessage"

    requests.post(
        url,
        data={
            "chat_id": CHAT_ID,
            "text": message
        }
    )

if __name__ == "__main__":

    send_message(
        "Pipeline ejecutado correctamente"
    )
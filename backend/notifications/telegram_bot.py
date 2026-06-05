import os
import requests

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv(
    "TELEGRAM_TOKEN"
)

CHAT_ID = os.getenv(
    "TELEGRAM_CHAT_ID"
)


def send_message(message):

    try:

        url = (
            f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        )

        response = requests.post(
            url,
            json={
                "chat_id": CHAT_ID,
                "text": message
            },
            timeout=10
        )

        return response

    except Exception as e:

        print(
            f"Error Telegram: {e}"
        )
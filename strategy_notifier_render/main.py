import requests
import datetime
import os

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send_message(text):
    if TOKEN and CHAT_ID:
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        data = {"chat_id": CHAT_ID, "text": text}
        requests.post(url, data=data)

def run():
    now = datetime.datetime.now()
    message = f"Strategy check at {now.strftime('%Y-%m-%d %H:%M:%S')} — No signal today"
    send_message(message)

if __name__ == "__main__":
    run()

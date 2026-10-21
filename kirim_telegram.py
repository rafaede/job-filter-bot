import os
import requests
from dotenv import load_dotenv
load_dotenv()
def kirim_telegram(pesan):
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = {"chat_id":chat_id,
            "text":pesan}

    
    try:
        response = requests.post(url,data=data,timeout=10)
        print(response.status_code)
    except Exception: 
        print("gagal kirim telegram")

kirim_telegram("tes job bot")
from telegram import Bot
from binance_scraper import check_new_projects
from dotenv import load_dotenv
import os
import time
import threading
from bot import run_telegram_bot

load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
bot = Bot(token=TOKEN)

def send_notification(projects):
    message = "🆕 *New Binance Learn & Earn Projects!*\n\n"
    message += "\n".join(f"• {p}" for p in projects)
    message += "\n\n👉 https://www.binance.com/en/learn-and-earn"
    bot.send_message(chat_id=CHAT_ID, text=message, parse_mode='Markdown')

def background_checker():
    while True:
        try:
            new_projects = check_new_projects()
            if new_projects:
                send_notification(new_projects)
        except Exception as e:
            print("Error checking Learn & Earn:", e)
        time.sleep(90)  # check every 90 seconds

if __name__ == "__main__":
    threading.Thread(target=background_checker, daemon=True).start()
    run_telegram_bot()

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from binance_scraper import fetch_learn_earn_projects
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome! Use /learn to view current Binance Learn & Earn projects.")

async def learn(update: Update, context: ContextTypes.DEFAULT_TYPE):
    projects = fetch_learn_earn_projects()
    if projects:
        msg = "📚 *Current Binance Learn & Earn Projects:*\n\n"
        msg += "\n".join(f"• {p}" for p in projects)
        msg += "\n\n👉 https://www.binance.com/en/learn-and-earn"
        await update.message.reply_text(msg, parse_mode='Markdown')
    else:
        await update.message.reply_text("No Learn & Earn projects found right now.")

def run_telegram_bot():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("learn", learn))
    app.run_polling()

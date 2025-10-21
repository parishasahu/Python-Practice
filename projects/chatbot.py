from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello Aashi! 🍀 Your bot is alive!")

app = ApplicationBuilder.token("8039378407:AAEctH_4bxy8rplxeRMJfAZN9X58BkSqlZs")

app.add_handler(CommandHandler("start", start))

print("Bot is running...")
app.run_polling()

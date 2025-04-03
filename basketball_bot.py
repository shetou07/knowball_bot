import logging
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    CallbackContext,
)

# Enable logging for debugging purposes
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# Handler for the /start command
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text(
        "Welcome to the Basketball News Bot! "
        "Type /news to get the latest basketball headlines or ask me any question about basketball."
    )

# Handler for the /news command
async def news(update: Update, context: CallbackContext):
    # Dummy news headlines. Replace this with an actual API call if needed.
    news_list = [
        "Lakers win against Celtics in a thrilling game!",
        "Warriors' new strategy leading to more wins this season.",
        "NBA announces schedule changes for upcoming playoffs.",
    ]
    message = "\n".join(news_list)
    await update.message.reply_text(message)

# Handler for the /help command
async def help_command(update: Update, context: CallbackContext):
    await update.message.reply_text(
        "Commands available:\n"
        "/start - Welcome message\n"
        "/news - Latest basketball news\n"
        "You can also ask me any basketball-related question!"
    )

# General message handler for interactions
async def handle_message(update: Update, context: CallbackContext):
    user_text = update.message.text.lower()
    if "nba" in user_text:
        await update.message.reply_text("The NBA season is really exciting this year! What would you like to know?")
    elif "player" in user_text:
        await update.message.reply_text("Basketball is full of talented players. Who is your favorite?")
    else:
        await update.message.reply_text("I'm here to talk basketball! Ask me anything or type /news for the latest headlines.")

# Error handler to log errors
async def error(update: Update, context: CallbackContext):
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    # Replace 'YOUR_TELEGRAM_BOT_TOKEN' with your actual token
    token = "7614255401:AAFIH5qIRSXPpYQg1QCXmCW_5lO7-k3FZeo"
    
    app = Application.builder().token(token).build()
    
    # Register handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("news", news))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    # Log all errors
    app.add_error_handler(error)
    
    # Start the Bot
    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()

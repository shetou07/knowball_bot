import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Enable logging for debugging purposes
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Handler for the /start command
def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Welcome to the Basketball News Bot! "
        "Type /news to get the latest basketball headlines or ask me any question about basketball."
    )

# Handler for the /news command
def news(update: Update, context: CallbackContext):
    # Dummy news headlines. You can integrate a live news API here.
    news_list = [
        "Lakers win against Celtics in a thrilling game!",
        "Warriors' new strategy leading to more wins this season.",
        "NBA announces schedule changes for upcoming playoffs."
    ]
    message = "\n".join(news_list)
    update.message.reply_text(message)

# Handler for the /help command
def help_command(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Commands available:\n"
        "/start - Welcome message\n"
        "/news - Latest basketball news\n"
        "You can also ask me any basketball-related question!"
    )

# General message handler for interactions
def handle_message(update: Update, context: CallbackContext):
    user_text = update.message.text.lower()
    if "nba" in user_text:
        update.message.reply_text("The NBA season is really exciting this year! What would you like to know?")
    elif "player" in user_text:
        update.message.reply_text("Basketball is full of talented players. Who is your favorite?")
    else:
        update.message.reply_text("I'm here to talk basketball! Ask me anything or type /news for the latest headlines.")

# Error handler to log errors
def error(update: Update, context: CallbackContext):
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    # Replace 'YOUR_TELEGRAM_BOT_TOKEN' with the token you received from BotFather
    token = "7614255401:AAFIH5qIRSXPpYQg1QCXmCW_5lO7-k3FZeo"
    updater = Updater(token, use_context=True)
    
    # Get the dispatcher to register handlers
    dp = updater.dispatcher
    
    # Register command handlers
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("news", news))
    dp.add_handler(CommandHandler("help", help_command))
    
    # Register a message handler for non-command messages
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
    
    # Log all errors
    dp.add_error_handler(error)
    
    # Start the Bot using polling
    updater.start_polling()
    
    # Run the bot until you press Ctrl-C or the process is stopped
    updater.idle()

if __name__ == '__main__':
    main()

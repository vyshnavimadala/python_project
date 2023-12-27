import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Your Telegram Bot token obtained from BotFather
TOKEN = "6954313797:AAH3DqZou80UPbCrEAVFSgPS-dGXYRsQwkw"

# Create an updater object
updater = Updater(token="6954313797:AAH3DqZou80UPbCrEAVFSgPS-dGXYRsQwkw" , use_context=True)

# Get the dispatcher to register handlers
dp = updater.dispatcher

# Define a command handler
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Hello! Welcome to Code Easy by AI")

# Define an echo handler
def echo(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(update.message.text)

# Register the handlers
dp.add_handler(CommandHandler("start", start))
dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

# Start the Bot
updater.start_polling()

# Run the bot until you send a signal to stop it
updater.idle()
import telegram
from telegram.ext import Updater, CommandHandler

def start(bot, update):
    update.message.reply_text("Welcome to the code generator! Send me a message to encode.")

def encode(bot, update):
    text = update.message.text
    encoded_text = ""
    for char in text:
        encoded_text += chr(ord(char) + 1)
    update.message.reply_text(encoded_text)

def main():
    # Insert your bot's token
    updater = Updater("YOUR_BOT_TOKEN")

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("encode", encode))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()

from telegram.ext import Updater, CommandHandler
import os


def printreply(update, context) -> None:
    update.message.reply_text("привет привет")


def main():
    updater = Updater(os.environ["MYFIRSTTGBOT"])
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("hello", printreply))
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()

from telegram import Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    CallbackContext,
)
import pytesseract
import os
from PIL import Image
import logging
import traceback

pytesseract.pytesseract.tesseract_cmd = "/usr/bin/tesseract"  # ваш путь до tesseract


def get_text_from_image(path):
    logging.info("getting image")
    img = Image.open(path)
    logging.info("image opened")
    return pytesseract.image_to_string(img, lang="rus+eng", timeout=30)

def echo_photo(update: Update, context: CallbackContext) -> None:
    print(update.message.photo)
    lst = update.message.photo
    logging.info("photo_size : " + str(len(lst)))
    result = "Что-то пошло не так, попробуйте позже"
    try:
        path = "images/photo.jpg"
        lst[-1].get_file().download(path, timeout=5)
        logging.info("download ok")
        result = get_text_from_image(path)
        logging.info("getting text ok")
    except Exception as e:
        logging.error(traceback.format_exc())
    try:
        update.message.reply_text(result)
    except Exception as e:
        update.message.reply_text("Текст не определен")


def echo_no_photo(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Это не фото")


def help(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Пришлите изображение с которого Вам нужен текст")


def main():
    updater = Updater(os.environ["MYFIRSTTGBOT"])
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", help))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(MessageHandler(Filters.photo & ~Filters.command, echo_photo))
    dp.add_handler(MessageHandler(~Filters.photo & ~Filters.command, echo_no_photo))
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()

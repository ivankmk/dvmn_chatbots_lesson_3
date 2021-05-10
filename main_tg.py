from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from dflow import detect_intent_texts
import os
from dotenv import load_dotenv
import logging

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

load_dotenv()


def start(bot, update):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')


def help(bot, update):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def echo(bot, update):
    """Echo the user message."""
    dialogflow_response = detect_intent_texts(
        os.environ.get('DF_PROJECT'),
        os.environ.get('DG_SESSION'),
        [update.message.text], 'ru')
    if dialogflow_response:
        update.message.reply_text(dialogflow_response)


def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def main():
    updater = Updater(os.environ.get('TG_DVMN_LESSONS'))
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(MessageHandler(Filters.text, echo))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()

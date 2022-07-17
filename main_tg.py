from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from dflow import detect_intent_texts
import os
from dotenv import load_dotenv, find_dotenv
import logging
from log_handler import MyLogsHandler


logger = logging.getLogger(__name__)


def start(bot, update):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')


def help(bot, update):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def respont_to_user(bot, update):
    session_id = f'tg-{update.message.from_user.id}'

    dialogflow_response = detect_intent_texts(
        os.getenv('gcp_project_name'),
        session_id,
        [update.message.text], 'ru')

    if dialogflow_response:
        update.message.reply_text(dialogflow_response)


def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def main():
    logger.setLevel(logging.INFO)
    logger.addHandler(MyLogsHandler())
    logger.info('TG Bot is running.')
    updater = Updater(os.environ.get('TG_DVMN_LESSONS'))
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(MessageHandler(Filters.text, respont_to_user))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    load_dotenv(find_dotenv())
    main()

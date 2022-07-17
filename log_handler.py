import logging
import telegram
import os


class MyLogsHandler(logging.Handler):
 
    def emit(self, record):
        tg_token = os.environ.get('TG_TOKEN')
        tg_chat_id = os.environ.get('TG_CHAT_ID')
        bot_logger = telegram.Bot(token=tg_token)
        log_entry = self.format(record)
        bot_logger.send_message(
            chat_id=tg_chat_id, text=log_entry)

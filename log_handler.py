import logging
import telegram


class LogsHandler(logging.Handler):

    def __init__(self, tg_token, tg_chat_id):
        self.bot = telegram.Bot(token=tg_token)
        self.chat_id = tg_chat_id

    def emit(self, record):
        log_entry = self.format(record)
        self.bot.send_message(
            chat_id=self.tg_chat_id, text=log_entry)

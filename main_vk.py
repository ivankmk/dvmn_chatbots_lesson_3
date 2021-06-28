import random
import os
import vk_api as vk
from dflow import detect_intent_texts
from vk_api.longpoll import VkLongPoll, VkEventType
from dotenv import load_dotenv

import logging
from log_handler import MyLogsHandler

logger = logging.getLogger(__name__)


def echo(event, vk_api):
    dialogflow_response = detect_intent_texts(
        os.environ.get('DF_PROJECT'),
        os.environ.get('DG_SESSION'),
        [event.text], 'ru')
    if dialogflow_response:
        vk_api.messages.send(
            user_id=event.user_id,
            message=dialogflow_response,
            random_id=random.randint(1, 1000)
        )


def main():
    logger.setLevel(logging.INFO)
    logger.addHandler(MyLogsHandler())
    logger.info('VK bot is running.')

    vk_session = vk.VkApi(token=os.environ.get('VK_TOKEN'))
    vk_api = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            echo(event, vk_api)


if __name__ == "__main__":
    load_dotenv()
    main()

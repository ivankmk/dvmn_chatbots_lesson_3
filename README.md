# Technical support chatbots

This project implements two technical support chatbots for vk.com and telegram for the fictional company "Game of Verbs". Bots answer typical user questions, presented in free form. The bots were trained with a neural network using the [DialogFlow] service (https://dialogflow.cloud.google.com/). The logs of each bot are sent to the established telegram chat.

## How to use

Send a question ([available questions] (https://github.com/ivankmk/dvmn_chatbots_lesson_3/blob/main/train_phrases.txt)) [telegram bot] (@dvmn_chatbot_lesson2_ivankmk_bot) or [vk group] ( https://vk.com/im?media=&sel=-205407374)

## Usage example

Telegram

![](https://im4.ezgif.com/tmp/ezgif-4-ef1c7e6199d0.gif)


VK

![](https://im4.ezgif.com/tmp/ezgif-4-85ed8ea56cc9.gif)

## How to install

### On local machine

Create an .env file in the root of the directory with the following variables
python
DF_PROJECT = "Your dialogflow project id"
DG_SESSION = "Your dialoglow session id"
GOOGLE_APPLICATION_CREDENTIALS = "path to google credentials json"
TG_CHAT_ID = 'your chat_id for errors'
TG_TOKEN = "Telegram bot token"
VK_TOKEN = "Your vk group token"
``,

Create [DialogFlow project] (https://cloud.google.com/dialogflow/es/docs/quick/setup) then create [agent] (https://cloud.google.com/dialogflow/es/docs/quick / build-agent) Record intents and responses for future bots. Intents can also be created by the `new_intents_loader.py` script, it will train the network using examples from` train_phrases.txt`

Create [google credentials json file] (https://cloud.google.com/docs/authentication/getting-started)

Create a vk group, in your group, click Manage -> Working with API -> Create key (allow sending messages)

Create a telegram bot using [@BotFather] (https://telegram.me/botfather). Get your bot token

Python3 must already be installed. Then use pip (or pip3, there is a conflict with Python2) to install the dependencies:

python
pip install -r requirements.txt
``,
Run the scripts with the following commands:
python
python main_vk.py
``,
python
python main_tg.py
``,

### Deploy to Heroku

Clone the repository, login or register on [Heroku] (https://dashboard.heroku.com)

Create a new Heroku application, connect your github account in the Deploy tab and select the required repository.

In the Settings tab, set the environment variables as Config Vars, [add google credentials] (https://stackoverflow.com/questions/47446480/how-to-use-google-api-credentials-json-on-heroku), use [this buildpack] (https://github.com/gerywahyunugraha/heroku-google-application-credentials-buildpack)

Activate the bot in the Resourses tab
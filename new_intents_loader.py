from ast import arg
import json
import time
from dotenv import load_dotenv
import os
import argparse
from google.cloud import dialogflow


def read_intents(filename):
    with open(filename, 'r') as my_file:
        file_contents = my_file.read()
        return json.loads(file_contents)


def create_intent(creds, display_name, training_phrases_parts, message_texts):
    """Create an intent of the given intent type."""
    intents_client = dialogflow.IntentsClient()

    parent = dialogflow.AgentsClient.agent_path(creds)

    training_phrases = []
    for training_phrases_part in training_phrases_parts:
        part = dialogflow.Intent.TrainingPhrase.Part(
            text=training_phrases_part)
        # Here we create a new training phrase for each provided part.
        training_phrase = dialogflow.Intent.TrainingPhrase(parts=[part])
        training_phrases.append(training_phrase)

    text = dialogflow.Intent.Message.Text(text=message_texts)
    message = dialogflow.Intent.Message(text=text)

    intent = dialogflow.Intent(
        display_name=display_name,
        training_phrases=training_phrases,
        messages=[message]
    )

    response = intents_client.create_intent(
        request={"parent": parent, "intent": intent}
    )

    print("Intent created: {}".format(response))


if __name__ == '__main__':
    load_dotenv()
    parser = argparse.ArgumentParser(
        description='Script will load new intents.'
    )
    parser.add_argument(
        '-f',
        '--file_with_intents',
        help='File with intents',
        default=os.getenv('train_phrases')
    )
    args = parser.parse_args()
    creds = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
    intents_to_load = read_intents(args.file_with_intents)
    for subject, questions_answers in intents_to_load.items():
        create_intent(
            creds,
            display_name=subject,
            training_phrases_parts=questions_answers['questions'],
            message_texts=[questions_answers['answer']]
        )
        time.sleep(15)

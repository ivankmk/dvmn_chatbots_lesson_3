import json
import time


def read_intents(filename):
    with open(filename, 'r') as my_file:
        file_contents = my_file.read()
        return json.loads(file_contents)


def create_intent(project_id, display_name, training_phrases_parts, message_texts):
    """Create an intent of the given intent type."""
    from google.cloud import dialogflow

    intents_client = dialogflow.IntentsClient()

    parent = dialogflow.AgentsClient.agent_path(project_id)
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
        display_name=display_name, training_phrases=training_phrases, messages=[
            message]
    )

    response = intents_client.create_intent(
        request={"parent": parent, "intent": intent}
    )

    print("Intent created: {}".format(response))


if __name__ == '__main__':
    project = 'dvmn-tg-lesson-2-vwlv'
    intents_to_load = read_intents('train_phrases.txt')
    for k, v in intents_to_load.items():
        time.sleep(15)
        create_intent(
            project,
            display_name=k,
            training_phrases_parts=v['questions'],
            message_texts=[v['answer']]
        )

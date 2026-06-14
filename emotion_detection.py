import requests


def emotion_detector(text_to_analyze):
    """Run emotion detection on the given text using the Watson NLP EmotionPredict function.

    The text to be analysed is passed in via ``text_to_analyze``. The raw ``text``
    attribute of the response returned by the Emotion Detection function is returned.
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": {"text": text_to_analyze}}

    response = requests.post(url, json=input_json, headers=headers)

    return response.text

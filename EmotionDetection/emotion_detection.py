import requests

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    data = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, headers=headers, json=data)
    answer_dict = response.json().get('emotionPredictions')[0].get('emotion')
    max_value = 0
    for key in answer_dict.keys():
        if answer_dict[key] > max_value:
            dominant_emotion = key
            max_value = answer_dict[key]
    answer_dict['dominant_emotion'] = dominant_emotion
    return(answer_dict)

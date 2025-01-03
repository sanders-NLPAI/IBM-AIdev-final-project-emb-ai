"""API module for Watson NLP Libraries
"""
import json
import requests

def emotion_detector(text_to_analyze):
    '''returns the emotion analysis result for given input text
    '''
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url,json=input_json,headers=headers, timeout=3)
    # convers response to json format
    res_json = json.loads(response.text)

    # extract the set of emotions with corresponding scores
    emotion_scores = res_json["emotionPredictions"][0]["emotion"] #NOTE: unnecessary nested json structure: list with one dictionary

    #find dominant emotion
    scores_sorted = sorted(emotion_scores.items(), key=lambda x:x[1], reverse=True)
    dominant_emotion = scores_sorted[0][0]
    
    formatted_output ={
        'anger': emotion_scores["anger"],
        'disgust': emotion_scores["disgust"],
        'fear': emotion_scores["fear"],
        'joy': emotion_scores["joy"],
        'sadness': emotion_scores["sadness"],
        "dominant_emotion" : dominant_emotion
    }
    return formatted_output

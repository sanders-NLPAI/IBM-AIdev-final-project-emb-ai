"""API module for Watson NLP Libraries
"""
import requests

def emotion_detector(text_to_analyze):
    '''returns the emotion analysis result for given input text
    '''
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url,json=input_json,headers=headers, timeout=3)
    return response.text

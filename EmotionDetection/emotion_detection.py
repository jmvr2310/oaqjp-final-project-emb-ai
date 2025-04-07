import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json_obj = { "raw_document": { "text": text_to_analyse } }

    response = requests.post(url, json=input_json_obj, headers=headers)
    formatted_response = json.loads(response.text)

    predictions = formatted_response.get("emotionPredictions", [])

    emotions = predictions[0].get("emotion", {})
   
    anger_score = emotions.get("anger", 0)
    disgust_score = emotions.get("disgust", 0)
    fear_score = emotions.get("fear", 0)
    joy_score = emotions.get("joy", 0)
    sadness_score = emotions.get("sadness", 0)

    emotion_scores = [anger_score, disgust_score, fear_score, joy_score, sadness_score]
    emotion_keys = ["anger", "disgust", "fear", "joy", "sadness"]
  
    dominant_emotion_index = emotion_scores.index(max(emotion_scores))
    dominant_emotion_key = emotion_keys[dominant_emotion_index]

    if response.status_code == 400:
        anger_score = None
        disgust_score = None
        fear_score = None
        joy_score = None
        sadness_score = None
        dominant_emotion_key = None
    
    result = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion_key
    }
    
    return result
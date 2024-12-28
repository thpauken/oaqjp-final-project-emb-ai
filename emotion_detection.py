import requests
#importing requests to handle HTTP requests

def emotion_detector(text_to_analyze):
    #defining the function that takes text_to_analyze variable
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    #url of the Watson emotion detection service
    
    myobj = { "raw_document": { "text": text_to_analyze } }
    #creating nested dictionary with text to be analyzed. "Raw document" is the key of the key : value pair"
    
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    #setting the headers required for the API request

    response = requests.post(url, json=myobj, headers=headers)
    formatted_response = response.json()
    #return text from the API
    emotion = formatted_response['emotionPredictions'][0]['emotion']
    dominant_emotion = max(emotion, key=emotion.get)
    #finding the dominant emotion by the value
    emotion['dominant_emotion'] = dominant_emotion
    #adding the dominant emotion to the emotion dictionary
    return emotion



from flask import Flask, request, render_template
from emotion_detection import emotion_detector
import json
app = Flask("Emotion Detector")
app.debug = True


@app.route("/emotionDetector", methods=['GET'])
def sent_emotion():
    #this is going go to receive the text from the HTML interface and run the emotional analysis on it using emotion_detector() funcion. 
    text_to_analyze = request.args.get('textToAnalyze')
    print("Text to analyze:", text_to_analyze)     
    response = emotion_detector(text_to_analyze)
    print("Response from emotion_detector:", response)
    emotion = response
    #return text from the API
    dominant_emotion = response['dominant_emotion']
    #finding the dominant emotion by the value
    response_text = (f"For the given statement, the system response is 'anger': {emotion['anger']}, " f"'disgust': {emotion['disgust']}, 'fear': {emotion['fear']}, 'joy': {emotion['joy']} " f"and 'sadness': {emotion['sadness']}. The dominant emotion is {dominant_emotion}.")
    return(response_text)    

        
@app.route("/")
def render_index_page():
    #This function initiates the rendering of the main application over the flask channel
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)



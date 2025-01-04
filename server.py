''' Executing this function initiates the application Emotion Detector
    to be executed over the Flask channel and deployed on
    localhost:5000.
'''
# Imports from the flask framework package
from flask import Flask, render_template, request
# Imports function from the package
from emotiondetection.emotion_detection import emotion_detector

#Initiate the flask app
app = Flask("Emotion Detector")

@app.route("/emotionDetector", methods=['GET'])
def run_analyzer():
    ''' This code receives the user's input from the HTML form and 
        runs emotion detection over it using emotion_detector()
        function. The output returned shows the labels and their confidence 
        score for the provided text plus the predicted dominant emotion.
    '''
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)
    dominant = response.pop('dominant_emotion')
    #scores = {}

    if dominant is None:
        message = "Invalid text! Please try again!"
    else:
        conf_scores = ""
        for key,value in response.items():
            if list(response.keys()).index(key) == len(list(response.keys())) -1:
                conf_scores = conf_scores + f"and '{key}': {value}"
            else:
                conf_scores = conf_scores + f"'{key}': {value}, "
        predicted = "The dominant emotion is "+ dominant
        message = f"For the given statement, the system response is {conf_scores}. {predicted}."
    return message

@app.route("/")
def render_index_page():
    ''' initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)
    
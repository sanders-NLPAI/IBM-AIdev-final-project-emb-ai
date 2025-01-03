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
    scores = response[0]
    dominant = response[1]
    for key,value in scores.items():
        if type(scores[key]) is float:
            scores[key] = str(value)
    res_items = list(scores.items())
    separator = '\': '
    formatted_output = f"'{separator.join(res_items[0])}, '{separator.join(res_items[1])}, '{separator.join(res_items[2])}, '{separator.join(res_items[3])} and '{separator.join(res_items[4])}."
    return ("For the given statement, the system response is "+ formatted_output + "The dominant emotion is " + dominant +".")


@app.route("/")
def render_index_page():
    ''' initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)
    
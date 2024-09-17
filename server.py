# Import necessary libraries from Flask
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

# Instantiate Flask application
app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/emotionDetector")
def get_sentiment():
    input = str(request.args.get('textToAnalyze'))
    result = emotion_detector(input)
    answer = (
    f"""For the given statement, the system response is 'anger': {result.get('anger')},
    'disgust': {result.get('disgust')}, 'fear': {result.get('fear')}, 
    'joy': {result.get('joy')} and 'sadness': {result.get('sadness')}. 
    The dominant emotion is <b>{result.get('dominant_emotion')}</b>.
    """
    )

    return answer

# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)
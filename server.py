"""
This module contains a Flask web application that provides an interface
for emotion detection. It receives text input from a user, processes it
using an emotion detection model, and displays the results.
"""

# Import the Flask, render_template, and request classes from the Flask framework
from flask import Flask, render_template, request

# Import the emotion_detector function from your EmotionDetection package,
# matching the import style in your test file.
from EmotionDetection.emotion_detection import emotion_detector

# Initialize the Flask application
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_detector():
    """
    Receives text from the HTML interface, runs emotion detection,
    and returns the formatted results. It also handles potential errors
    from the emotion_detector function if the input is invalid.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    # Format the response string as per the project requirements
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    return (
        f"For the given statement, the system response is 'anger': {anger}, "
        f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and "
        f"'sadness': {sadness}. The dominant emotion is {dominant_emotion}."
    )


@app.route("/")
def render_index_page():
    """
    This function renders the main application page (index.html).
    """
    return render_template('index.html')


if __name__ == "__main__":
    # This function executes the flask app and deploys it on localhost:5000
    app.run(host="0.0.0.0", port=5000)
    
"""Flask server for the emotion detection application."""

from flask import Flask, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/emotionDetector")
def sent_detector():
    """Analyze text and return the detected emotions."""

    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function
    response = emotion_detector(text_to_analyze)

    # Check if the input is invalid
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    # Extract the emotion scores
    anger_score = response['anger']
    disgust_score = response['disgust']
    fear_score = response['fear']
    joy_score = response['joy']
    sadness_score = response['sadness']

    # Extract the dominant emotion
    dominant_emotion = response['dominant_emotion']

    # Return the formatted response
    return (
        f"For the given statement, the system response is "
        f"'anger': {anger_score}, 'disgust': {disgust_score}, "
        f"'fear': {fear_score}, 'joy': {joy_score} "
        f"and 'sadness': {sadness_score}. "
        f"The dominant emotion is {dominant_emotion}."
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    
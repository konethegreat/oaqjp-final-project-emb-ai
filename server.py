"""Flask web server for the Emotion Detection application.

Serves the front-end page and exposes the ``/emotionDetector`` route, which runs
the ``emotion_detector`` function on the supplied text and returns a
human-readable summary of the detected emotions and the dominant emotion.
"""
import requests
from flask import Flask, render_template, request

from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def emotion_detector_route():
    """Analyze the text given via the ``textToAnalyze`` query argument."""
    text_to_analyze = request.args.get('textToAnalyze')

    try:
        response = emotion_detector(text_to_analyze)
    except requests.exceptions.RequestException:
        # The Watson endpoint is only reachable from inside the IBM Skills
        # Network lab; surface a clear message instead of a raw 500 error.
        return ("The emotion analysis service could not be reached. "
                "It is only available from within the IBM Skills Network lab environment.")

    # Blank / invalid input -> emotion_detector returns None values.
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    return (
        "For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )


@app.route("/")
def render_index_page():
    """Render the main application page."""
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

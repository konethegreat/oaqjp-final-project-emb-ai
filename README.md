# Emotion Detection — IBM AI Engineering Final Project

A small Flask web app that runs text through IBM Watson NLP's `EmotionPredict` model and reports the five emotion scores plus the dominant emotion.

This is the final project for the **Building AI Powered Applications with Python** course on Coursera (IBM Skills Network).

## What it does

Give it a sentence, get back something like:

> For the given statement, the system response is `'anger': 0.006`, `'disgust': 0.002`, `'fear': 0.030`, `'joy': 0.968` and `'sadness': 0.049`. The dominant emotion is **joy**.

Blank or nonsensical input returns `Invalid text! Please try again!` instead of a crash.

## Project layout

```
.
├── EmotionDetection/            # Reusable package
│   ├── __init__.py
│   └── emotion_detection.py     # emotion_detector() — calls Watson NLP
├── server.py                    # Flask app, exposes /emotionDetector
├── templates/index.html         # Front-end page
├── static/mywebscript.js        # Front-end JS
├── test_emotion_detection.py    # Unit tests (5 dominant-emotion cases)
└── requirements.txt
```

## Important: where it runs

The Watson NLP endpoint (`sn-watson-emotion.labs.skills.network`) is **only reachable from inside the IBM Skills Network lab environment**. Running locally, the request will time out and the route will respond with a polite "service unreachable" message instead of a 500.

If you want to use it for real, clone the repo inside the Cloud IDE lab and run it from there.

## Running it (inside the lab)

```bash
git clone https://github.com/konethegreat/oaqjp-final-project-emb-ai.git
cd oaqjp-final-project-emb-ai
pip3 install -r requirements.txt
python3 server.py
```

Then click **Launch Application** in the lab toolbar and enter port `5000`.

## Running the tests

```bash
python3 test_emotion_detection.py
```

Five assertions cover joy / anger / disgust / sadness / fear dominant-emotion cases.

## Code quality

`server.py` scores **10.00/10** under pylint:

```bash
pylint server.py
```

## Course deliverables

Task-by-task transcripts (screenshots / terminal captures) live in the repo as `<task>_<name>.txt` files — e.g. `5b_unit_testing_result.txt`, `8b_static_code_analysis.txt`.

## License

See [LICENSE](LICENSE).

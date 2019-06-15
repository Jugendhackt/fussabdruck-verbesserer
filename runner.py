from flask import Flask
from flask import jsonify
import fragen

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '''Hello, JugendHackt!
    
    Den Senf kriegst du <a href="/senf/">hier</a>.'''

@app.route('/senf/')
def json_ausgabe():
    d = get_data()
    return jsonify(d)

def get_data():
    questions = fragen.getQuestions()
    result = []
    for question in questions:
        result.append(question.toJSON())

    return {
        'data':result
    }
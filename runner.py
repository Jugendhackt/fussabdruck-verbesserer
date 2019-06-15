from flask import Flask
from flask import jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '''Hello, JugendHackt!
    
    Den Senf kriegst du <a href="/senf">hier</a>.'''

@app.route('/senf')
def json_ausgabe():
    d = get_data()
    return jsonify(d)

def get_data():
    return {
        'data':[
            {
                'frage':'Treiben Sie Sport?',
                'antworten':[
                    'Ja',
                    'Nein'
                ]
            },
            {
                'frage':'Wie oft essen Sie Fleisch?',
                'antworten':[
                    'täglich',
                    'mehrmals wöchentlich',
                    'einmal die Woche',
                    'nie'
                ]
            },

        ]
    }
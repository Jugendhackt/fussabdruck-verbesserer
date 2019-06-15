from flask import Flask, request, send_from_directory, jsonify
import fragen

app = Flask(__name__)

@app.route('/')
def hello_world():
    return open('website/index.html').read().replace('"style.css', '"/website/style.css').replace('"javascript.js', '"/website/javascript.js')

@app.route('/OLD')
def hello_old_world():
    return '''<h2>Willkommen bei der Datenverarbeitung von FußabdruckVerbesserer!</h2> 
    Wir helfen ihnen  konkret und innovativ ihren Ressourcenverbrauch zu reduzieren 
    und zum Wohle aller, vor allem künftiger Generationen nachhaltiger zu leben.'''

@app.route('/website/<path:path>')
def send_resource(path):
    return send_from_directory('website', path)


def fragebogen_generieren():
    fragebogen = []
    frage = fragen.Question("Treiben Sie Sport?")
    frage.add_answer('ja')
    frage.add_answer('nein')
    fragebogen.append(frage)

    frage = fragen.Question('Wie oft essen Sie Fleisch?')
    frage.add_answer('täglich')
    frage.add_answer('mehrmals wöchentlich')
    frage.add_answer('einmal die Woche')
    frage.add_answer('nie')
    fragebogen.append(frage)

    frage = fragen.Question('Worauf achten sie bei der Anschaffung neuer Konsumgüter?')
    frage.add_answer('Langlebigkeit')
    frage.add_answer('Funktionalität')
    frage.add_answer('günstige Preise')
    fragebogen.append(frage)

    frage = fragen.Question('Wie schätzen sie ihr Kaufverhalten ein?')
    frage.add_answer('sparsam')
    frage.add_answer('durchschnittlich')
    frage.add_answer('großzügig')
    fragebogen.append(frage)

    frage = fragen.Question('Sind Sie Halter*In eines Haustieres?')
    frage.add_answer('Hund')
    frage.add_answer('Katze')
    frage.add_answer('Nagetier')
    frage.add_answer('Nein')
    fragebogen.append(frage)
    return fragebogen

#def antwort_generieren():
#    antworten[]

@app.route('/fragebogen/')
def fragebogen_senden():
    d = get_data()
    return jsonify(d)

def get_data():
    questions = fragebogen_generieren()
    result = []
    for question in questions:
        result.append(question.toJSON())

    return {
        'data':result
    }
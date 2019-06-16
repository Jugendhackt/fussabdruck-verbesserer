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
    frage = fragen.Question("Treiben Sie Sport?", 0.35)
    frage.add_answer('ja', faktor = 1.1)
    frage.add_answer('nein')
    fragebogen.append(frage)

    frage = fragen.Question('Wie oft essen Sie Fleisch?', 0.78)
    frage.add_answer('täglich', faktor = 1.3)
    frage.add_answer('mehrmals wöchentlich')
    frage.add_answer('einmal die Woche', faktor = 0.8)
    frage.add_answer('nie', faktor = 0.7)
    fragebogen.append(frage)

    frage = fragen.Question('Worauf achten sie bei der Anschaffung neuer Konsumgüter?', 1)
    frage.add_answer('Langlebigkeit', faktor = 0.95)
    frage.add_answer('Funktionalität')
    frage.add_answer('günstige Preise', faktor = 1.05)
    fragebogen.append(frage)

    frage = fragen.Question('Wie schätzen sie ihr Kaufverhalten ein?', 1)
    frage.add_answer('sparsam', faktor = 0.95)
    frage.add_answer('durchschnittlich')
    frage.add_answer('großzügig', faktor = 1.05)
    fragebogen.append(frage)

    frage = fragen.Question('Sind Sie Halter*In eines Haustieres?', 1)
    frage.add_answer('kleiner Hund', faktor = 1.8)
    frage.add_answer('großer Hund', faktor = 3)
    frage.add_answer('Katze', faktor=2)
    frage.add_answer('Alpaka', faktor = 6)
    frage.add_answer('Nein', faktor = 0)
    fragebogen.append(frage)

    frage = fragen.Question('Auf wievielen Quadratmetern Wohnfläche leben Sie?', 1)
    frage.add_answer('bis 40', faktor = 5.8)
    frage.add_answer('40 - 60', faktor = 6.2)
    frage.add_answer('60 - 90', faktor = 6.6)
    frage.add_answer('90 - 120', faktor = 7.1)
    frage.add_answer('ab 120', faktor = 8)
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
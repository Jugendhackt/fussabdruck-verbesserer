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
    frage.add_hint("Auch wenn Sport den CO2 ausstos steigert ist es trotzdem gesund und sollet mind. 1mal pro Woche betriben werden.")
    frage.add_answer('ja', faktor = 1.1,hint="Totz CO2 ausstos, treiben ie weiter Sport.")
    frage.add_answer('nein')
    fragebogen.append(frage)

    frage = fragen.Question('Wie oft essen Sie Fleisch?', 0.78)
    frage.add_answer('täglich', faktor = 1.3,hint="Sie könnten versuchen einen Fleisch freien Tag einzuführen.")
    frage.add_answer('mehrmals wöchentlich', faktor = 1)
    frage.add_answer('einmal die Woche', faktor = 0.8)
    frage.add_answer('nie', faktor = 0.7)
    frage.add_hint("Ihr Fleisch kommt von Tieren die CO2 produzieren.")
    fragebogen.append(frage)

    frage = fragen.Question('Worauf achten Sie bei der Anschaffung neuer Konsumgüter?', 1)
    frage.add_answer('Langlebigkeit', faktor = 0.95)
    frage.add_answer('Funktionalität',hint= "Trotz Funktionalität können sie noch auf Langlebigkeit achten.")
    frage.add_answer('günstige Preise', faktor = 1.05, hint="Meistens halten günstige Produkte nicht sehr lange.")
    frage.add_hint("Durch wegwerfen entsteht Müll.")
    fragebogen.append(frage)

    frage = fragen.Question('Wie schätzen sie ihr Kaufverhalten ein?', 1)
    frage.add_answer('sparsam', faktor = 0.95)
    frage.add_answer('durchschnittlich')
    frage.add_answer('großzügig', faktor = 1.05, hint="Durch vieles kaufen werden auch viele Ressourcen verbraucht.Durch weniger kaufen könnten sie Ressourcen sparen.")
    frage.add_hint("Je mehr man verbraucht desto mehr CO2 entsteht durch Produktion.")
    fragebogen.append(frage)

    frage = fragen.Question('Sind Sie Halter*In eines Haustieres?', 1)
    frage.add_answer('kleiner Hund', faktor = 1.8)
    frage.add_answer('großer Hund', faktor = 3)
    frage.add_answer('Katze', faktor=2)
    frage.add_answer('Alpaka', faktor = 0,hint="Alpaka ist immer die richtige antwort!")
    frage.add_answer('Nein', faktor = 0, hint="Tiere verbrauchen genauso wie Menschen CO2 und diese können wir auch nicht abschaffen, also legen sie sich ein Tier zu.")
    frage.add_hint("Auch wenn Tiere CO2 prodozieren ist es kein Grund sie abzuschaffen.")
    fragebogen.append(frage)

    frage = fragen.Question('Auf wievielen Quadratmetern Wohnfläche leben Sie?', 1)
    frage.add_answer('bis 40', faktor = 5.8)
    frage.add_answer('40 - 60', faktor = 6.2)
    frage.add_answer('60 - 90', faktor = 6.6)
    frage.add_answer('90 - 120', faktor = 7.1)
    frage.add_answer('ab 120', faktor = 8)
    frage.add_hint("Große Grundstücke versiegeln mehr Fläche.")
    fragebogen.append(frage)

    return fragebogen

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

def get_results(answers):
    position = 0
    abdruck = 0
    hinweise = []
    questions = fragebogen_generieren()
    for Element in answers:
        if type(Element) is list:
            for senf in Element:
                abdruck += questions[position].getAbdruck(senf)
                hinweise.append(questions[position].gethints(senf))
        else:
            abdruck += questions[position].getAbdruck(Element)
            hinweise.append(questions[position].gethints(Element))
        position += 1
    text = 'Ihr Abdruck beträgt ' + abdruck + ' Tonnen CO2 pro Jahr\n' 
    text += 'Tipps zum verkleinern Ihres Fußabdrucks:\n'
    for tipp in hinweise:
        text += tipp +'\n'
    return text

@app.route('/antworten/', methods=['GET','POST'])
def antworten_verarbeiten():
    print(request.get_json())
    return 'ok', 200
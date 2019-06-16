# fussabdruck-verbesserer
Hier entsteht ein Quiz, bei dem man den eigenen Resourcen-Verbrauch berechnen kann.

## Benutzung 

Zum Betrieb der Website wird Python 3 benötigt und muss auf dem Rechner installiert sein.
Zudem muss Flask installiert sein.

    pip install Flask 

### laufen lassen unter Windows 

    set FLASK_APP=runner.py
    set FLASK_ENV=development
    flask run

### laufen lassen unter Linux

    export FLASK_APP=runner.py
    export FLASK_ENV=development
    flask run

#### website aufrufen :
http://127.0.0.1:5000

from flask import Flask

#   Applikation wird erstellt ...
def create_app():
    app=Flask(__name__)
#   ...und konfiguriert
    app.config.from_pyfile('config.py')
    return app

#   Funktion wird auf app gelegt
app=create_app()

#   Importierung der anderen PY_Dateien
from lucky.routes import *
from lucky.database import *


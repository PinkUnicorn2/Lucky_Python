from flask import Flask
from flask_login import LoginManager
from flask_moment import Moment
from flask_admin import Admin

#   Applikation wird erstellt ...
def create_app():
    app=Flask(__name__)
#   ...und konfiguriert
    app.config.from_pyfile('config.py')
    return app

#   Funktion wird auf app gelegt
app=create_app()
login_manager = LoginManager()
login_manager.init_app(app)
admin = Admin(app)
moment= Moment(app)

#   Importierung der anderen PY_Dateien
from lucky.routes import *
from lucky.database import *
from lucky.form import *
from lucky.functions import *

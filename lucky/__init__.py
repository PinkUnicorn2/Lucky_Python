from flask import Flask
from flask_login import LoginManager
from flask_moment import Moment
from flask_admin import Admin
from flask_socketio import SocketIO, send
import datetime


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
socketio = SocketIO(app)


#   Websocket broadcastet alle Nachrichten
@socketio.on('message')
def handleMessage(msg):
#   Keine Speicherung der aktuellen Zeit in Variablen, weil Timestamp dann nicht Aktuell
    print(datetime.datetime.strftime(datetime.datetime.now(), '%H%M:%S')+ ':' +msg)
#   chat.Nachricht, chat.Zeit, chat.Datum und chat.Benutzername werden in message Objekt gepackt
    message = chat(message=msg,timestamp=datetime.datetime.strftime(datetime.datetime.now(), '%H:%M:%S'),
                   datestamp=datetime.datetime.strftime(datetime.datetime.now(), '%Y:%m:%d'),user_id=current_user.id)
#   message objekt wird an Datenbank uebergeben
    db.session.add(message)
#   und gespeichert
    db.session.commit()
    msg=current_user.username+' ['+datetime.datetime.strftime(datetime.datetime.now(), '%H:%M:%S')+']: '+msg
    send(msg, broadcast=True)

#   Importierung der anderen PY_Dateien
from lucky.routes import *
from lucky.database import *
from lucky.form import *
from lucky.functions import *
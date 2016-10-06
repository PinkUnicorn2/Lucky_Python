from flask_socketio import SocketIO, send
from lucky.__init__ import app

socketio = SocketIO(app)

@socketio.on('message')
def handleMessage(msg):
    print('Message: ' +msg)
    send(msg, broadcast=True)

if __name__ == '__main__':
    socketio.run(app)
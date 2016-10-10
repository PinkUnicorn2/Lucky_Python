from lucky import app
from lucky.__init__ import socketio
#   create_app() wird aufgerufen -> __init__.py
socketio.run(app)
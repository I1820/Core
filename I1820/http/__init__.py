from flask import Flask
from flask_cors import CORS
import socketio

sio = socketio.Server(async_mode='gevent')

app = Flask("I1820")
app.wsgi_app = socketio.Middleware(sio, app.wsgi_app)

CORS(app)

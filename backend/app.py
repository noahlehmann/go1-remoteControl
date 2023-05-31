from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@socketio.on('connect')
def test_connect():
    print("socket connected")


if __name__ == '__main__':
    socketio.run(app)

from flask import Flask
from flask_socketio import SocketIO
from flask_mqtt import Mqtt
import struct

app = Flask(__name__)
app.config['MQTT_BROKER_URL'] = "rocky.hof-university.de"
app.config['MQTT_BROKER_PORT'] = 1883
mqtt_client = Mqtt(app, connect_async=True)
mqtt_client.publish("controller/action", "walk", qos=2)
socketio = SocketIO(app, cors_allowed_origins='*')

stick_values = {
    'lx': 0, 'rx': 0, 'ry': 0, 'ly': 0
}
preset_speed = 0.6


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@socketio.on('connect')
def test_connect():
    print("socket connected")


@socketio.on('keydown')
def set_key(key):
    print(key + " down")
    translation = translate_key_to_stick_value(key)
    stick_values[translation["key"]] = translation["value"]
    change_stick_values(
        stick_values["lx"],
        stick_values["rx"],
        stick_values["ry"],
        stick_values["ly"]
    )


@socketio.on('keyup')
def reset_key(key):
    print(key + " up")
    translation = translate_key_to_stick_value(key)
    stick_values[translation["key"]] = 0
    change_stick_values(
        stick_values["lx"],
        stick_values["rx"],
        stick_values["ry"],
        stick_values["ly"]
    )


@socketio.on('color')
def change_color(info):
    change_led_color(info.r, info.g, info.b)


@mqtt_client.on_log()
def log_mqtt(msg):
    print(msg)


def change_stick_values(lx, rx, ry, ly):
    # lx, rx, ry, ly
    data = struct.pack("ffff", lx, rx, ry, ly)
    mqtt_client.publish("controller/stick", data, qos=2)


def change_led_color(r, g, b):
    mqtt_client.publish("face_light/color", struct.pack('iii', r, g, b), qos=2)


def translate_key_to_stick_value(key):
    if key == "l_up":
        return {"key": "ly", "value": preset_speed}
    if key == "l_down":
        return {"key": "ly", "value": -preset_speed}
    if key == "l_left":
        return {"key": "lx", "value": -preset_speed}
    if key == "l_right":
        return {"key": "lx", "value": preset_speed}
    if key == "r_up":
        return {"key": "ry", "value": preset_speed}
    if key == "r_down":
        return {"key": "ry", "value": -preset_speed}
    if key == "r_left":
        return {"key": "rx", "value": -preset_speed}
    if key == "r_right":
        return {"key": "rx", "value": preset_speed}


if __name__ == '__main__':
    socketio.run(app)

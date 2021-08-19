from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
import json

# import logging

# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)

async_mode = None

app = Flask(__name__, static_url_path="", static_folder="public/static", template_folder="public/templates")
app.config["SECRET_KEY"] = "secret!"

# sio = SocketIO(app)
# sio = SocketIO(app, async_mode=async_mode)
sio = SocketIO(app, logger=True, engineio_logger=True)


@app.route("/")
def index():
    # logger.info('serving root')
    return render_template("index.html")
    # return render_template(
    #     'index.html', async_mode=socketio.async_mode)


@sio.event
def connect():
    print(f"{request.sid} connected")
    with open("text.json", "r") as file:
        data = file.read()
        if data:
            data = json.loads(data)
            emit("UpdateText", data["files"][-1]["Data"], broadcast=True)


@sio.on("TextUpdated")
def update_text(message):
    with open("text.json", "r") as file:
        versions = file.read()
    if versions:
        versions = json.loads(versions)
        version_number = len(versions.get("files")) + 1
        data = {"Version": version_number, "Data": message}
        if "files" in versions and versions["files"]:
            versions["files"].append(data)
    else:
        versions = {}
        versions["files"] = [{"Version": 1, "Data": message}]
    with open("text.json", "w+") as file:
        file.write(json.dumps(versions, indent=4))
        emit("UpdateText", message, broadcast=True)


@sio.on("UpdateAll")
def update_all(message):
    emit("UpdateText", message, broadcast=True)


@sio.on("disconnect")
def test_disconnect():
    print(f"{request.sid} disconnected")


if __name__ == "__main__":
    # sio.run(app)
    sio.run(app, host="localhost", port=8000, debug=True)
    # sio.run(app, host='0.0.0.0', port=5000) # production

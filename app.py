from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
# import logging

# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)

async_mode = None

app = Flask(__name__,
            static_url_path='',
            static_folder='public/static',
            template_folder='public/templates')
app.config['SECRET_KEY'] = 'secret!'

# sio = SocketIO(app)
# sio = SocketIO(app, async_mode=async_mode)
sio = SocketIO(app, logger=True, engineio_logger=True)


@app.route('/')
def index():
    # logger.info('serving root')
    return render_template('index.html')
    # return render_template(
    #     'index.html', async_mode=socketio.async_mode)


@sio.event
def connect():
    print(f"{request.sid} connected")


@sio.on('disconnect')
def test_disconnect():
    print(f"{request.sid} disconnected")


if __name__ == '__main__':
    # sio.run(app)
    sio.run(app, host="localhost", port=8000, debug=True)
    # sio.run(app, host='0.0.0.0', port=5000) # production

from flask import Flask, render_template
from flask_socketio import SocketIO


# import logging
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)


app = Flask(__name__,
            static_url_path='',
            static_folder='public/static',
            template_folder='public/templates')
app.config['SECRET_KEY'] = 'secret!'

# sio = SocketIO(app)
sio = SocketIO(app, logger=True, engineio_logger=True)


@app.route('/')
def index():
    # logger.info('serving root')
    return render_template('index.html')


if __name__ == '__main__':
    sio.run(app, host="localhost", port=8000, debug=True)

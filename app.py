from flask import Flask, render_template
from flask_socketio import SocketIO


app = Flask(__name__,
            static_url_path='',
            static_folder='public/static',
            template_folder='public/templates')
app.config['SECRET_KEY'] = 'secret!'

sio = SocketIO(app)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    sio.run(app)

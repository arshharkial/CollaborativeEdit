import socketio

sio = socketio.Server()

# wrap socket io app into a WSGI app
app = socketio.WSGIApp(sio)

@sio.event
def connect(sid, environ):
    print(sid, 'connected')


@sio.event
def disconnect(sid):
    print(sid, 'disconnected')

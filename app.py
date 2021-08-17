import socketio

sio = socketio.Server()

# wrap socketio app into a WSGI app
app = socketio.WSGIApp(sio)

app = socketio.WSGIApp(sio, static_files={
    '/': './static/'
})


@sio.event
def connect(sid, environ):
    print(sid, 'connected')


@sio.event
def disconnect(sid):
    print(sid, 'disconnected')

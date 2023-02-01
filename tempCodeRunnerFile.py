import socketio
sio=socketio.Server()
@sio.event
def connect(sid,environ):
    print('connect',sid)
@sio.event
def on_message(sid,data):
    pass
@sio.event
def disconnect(sid,envion):
    print('disconnect',sid)
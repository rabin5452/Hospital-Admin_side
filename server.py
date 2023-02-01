from flask import Flask, render_template
from flask_socketio import SocketIO
from main import calculate_token
from datetime import datetime
app = Flask(__name__)
sio = SocketIO(app)
tokenqueue=[]
@sio.on('connect')
def handle_connect():
    print('Connected')

@sio.on('message')
def handle_message(data):
        data_time=datetime.now().strftime("%H-%M-%S")
        email=data['msg']
        tokenqueue.append(email)
        queue_length=len(tokenqueue)
        calculate_token(email,data_time,queue_length)
        # print('Received message:', data['msg'])
        # print(data_time)

@sio.on('disconnect')
def handle_disconnect():
    print('Disconnected')

# def runserver():
if __name__ == '__main__':
    sio.run(app, host='localhost', port=5000)
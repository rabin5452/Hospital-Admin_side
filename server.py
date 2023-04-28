from flask import Flask, render_template
from flask_socketio import SocketIO
from main import calculate_token
from datetime import datetime
from databaseconnect import check_email_exists,cursor,delete_table
app = Flask(__name__)
sio = SocketIO(app)
tokenqueue=[]
start_time = datetime.now().strftime("%H-%M-%S")
@sio.on('connect')
def handle_connect():
    print('Connected')

@sio.on('message')
def handle_message(data):
        data_time=datetime.now().strftime("%H-%M-%S")
        email=data['msg']
        if check_email_exists(email)==0:
            tokenqueue.append(email)
            queue_length=len(tokenqueue)
            calculate_token(email,data_time,queue_length,start_time)
            print(start_time)
            print('Received message:', data['msg'])
            print(data_time)
        else:
             pass
            

@sio.on('disconnect')
def handle_disconnect():
    print('Disconnected')

# def runserver():
if __name__ == '__main__':
    delete_table()
    sio.run(app, host='localhost', port=5000)
from flask_socketio import SocketIO, emit, send
from flask import render_template, Flask, session, request, copy_current_request_context
from threading import Lock

async_mode = None

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode=async_mode)

thread = None
thread_lock = Lock


# flask 打开页面 socketio.run debug=True 会启动不起来

@app.route('/')
def index():
    return render_template('second.html', async_mode=socketio.async_mode)


@socketio.on('message')
def handle_message(data):
    print('received message: ' + data)


@socketio.on('json')
def handle_json(json):
    print('received json first: ' + str(json))


# 前后端建立连接 按照事件名称进行建立连接。my event 就是事件名称

@socketio.on('my event')
def handle_my_custom_event(json):
    print('received json second: ' + str(json))


@socketio.on('my_event')
def handle_my_custom_event(arg1, arg2, arg3):
    print('received args: ' + arg1 + arg2 + arg3)


@socketio.event
def my_custom_event(arg1, arg2, arg3):
    print('received args: ' + arg1 + arg2 + arg3)


if __name__ == '__main__':
    socketio.run(app, port=8020)

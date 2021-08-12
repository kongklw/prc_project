from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit, send
from flask_socketio import join_room, leave_room

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@socketio.on('connect', namespace='/test')
def test_connect():
    emit('my response', {'data': 'Connected'})


@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')


@socketio.on('message')
def handle_message(message):
    print('received message: ' + message)


@socketio.on('json')
def handle_json(json):
    print('received json: ' + str(json))


@socketio.on('my event')
def handle_my_custom_event(json):
    print('received json: ' + str(json))


@socketio.on('my event')
def handle_my_custom_event(arg1, arg2, arg3):
    print('received args: ' + arg1 + arg2 + arg3)


@socketio.on('my event', namespace='/test')
def handle_my_custom_namespace_event(json):
    print('received json: ' + str(json))


@socketio.on('my event')
def handle_my_custom_event(json):
    print('received json: ' + str(json))
    return 'one', 2


@socketio.on('message')
def handle_message(message):
    send(message)


@socketio.on('json')
def handle_json(json):
    send(json, json=True)


@socketio.on('my event')
def handle_my_custom_event(json):
    emit('my response', json)


@socketio.on('message')
def handle_message(message):
    send(message, namespace='/chat')


@socketio.on('my event')
def handle_my_custom_event(json):
    emit('my response', json, namespace='/chat')


@socketio.on('my event')
def handle_my_custom_event(json):
    emit('my response', ('foo', 'bar', json), namespace='/chat')


def ack():
    print('message was received!')


@socketio.on('my event')
def handle_my_custom_event(json):
    emit('my response', json, callback=ack)





@socketio.on('join')
def on_join(data):
    username = data['username']
    room = data['room']
    join_room(room)
    send(username + ' has entered the room.', room=room)


@socketio.on('leave')
def on_leave(data):
    username = data['username']
    room = data['room']
    leave_room(room)
    send(username + ' has left the room.', room=room)


@socketio.on_error()  # Handles the default namespace
def error_handler(e):
    pass


@socketio.on_error('/chat')  # handles the '/chat' namespace
def error_handler_chat(e):
    pass


@socketio.on_error_default  # handles all namespaces without an explicit error handler
def default_error_handler(e):
    pass


@socketio.on("my error event")
def on_my_event(data):
    raise RuntimeError()


@socketio.on_error_default
def default_error_handler(e):
    print(request.event["message"])  # "my error event"
    print(request.event["args"])  # (data,)


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', debug=True)

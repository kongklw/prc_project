from flask import Flask
from flask_sockets import Sockets
import datetime
import time
import random

app = Flask(__name__)
sockets = Sockets(app)


@sockets.route('/echo')
def echo_socket(ws):
    while not ws.closed:
        now = datetime.datetime.now().isoformat() + 'Z'
        ws.send(now)  # 发送数据
        time.sleep(1)


@app.route('/')
def hello():
    return 'Hello World!'


if __name__ == "__main__":
    from gevent import pywsgi
    from geventwebsocket.handler import WebSocketHandler

    server = pywsgi.WSGIServer(('', 8000), app, handler_class=WebSocketHandler)
    print('server start')
    server.serve_forever()

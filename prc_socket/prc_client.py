# Echo client program
import socket
import time
import random

HOST = '10.1.94.167'  # The remote host
PORT = 50007  # The same port as used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello, world')
    data = s.recv(1024)
print('Received', repr(data))

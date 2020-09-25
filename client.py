import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
try:
    s.connect((host, 5555))
    print('Connected to server')

#    print('Input:')
    while True:
        msg = input()
        s.sendall(str.encode(msg))
        data = s.recv(1024)
        if msg == 'disconnect':
            break
        print('Received: ' + data.decode('utf-8'))
    s.close()
except socket.error as e:
    print('Error code : ' + str(e))
    sys.exit()
import socket
import sys
from _thread import *

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = ''
port = 5555

try:
    s.bind((host, port))
except socket.error as e:
    print('Error code : ' + str(e))
    sys.exit()

s.listen(5)
print('Waiting for connections\n')

def thread_client(conn):


    while True:
        data = conn.recv(1024)
        reply = 'Server Reply: ' + data.decode('utf-8')
        if not data:
            print(addr[0] + ' Disconnected at port: ' + str(addr[1]))
            break
        conn.sendall(str.encode(reply))


    conn.close()

while True:
    conn, addr = s.accept()
    print('connected to: ' + addr[0] + ': ' + str(addr[1]))
    conn.sendall(str.encode('Connection established.Input: '))
    start_new_thread(thread_client, (conn,))

s.close()





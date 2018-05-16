from array import array

import socket

import time

 
HOST = '127.0.0.1'
PORT = 42001

 
print("connecting...")
scratchSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
scratchSock.connect((HOST, PORT))
print("connected! waiting for data...")

 
# print incoming data forever
while 1:

    time.sleep(0.01)
    data = scratchSock.recv(1024)
    if not data: break
    print(data)

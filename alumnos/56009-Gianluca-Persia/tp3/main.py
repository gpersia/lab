#!/usr/bin/python3

import socket, threading

server = socket.socket()
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(("localhost", 8888))
server.listen(1)
while True:
    clientSocket, clientAddress = server.accept()
    clientThread = threading.Thread(target = client, args = (clientSocket, clientAddress))
    clientThread.start()
    exit()
#!/usr/bin/python3

import socket, threading
import main

def rcvespuesta(clientSocket):
    clientSocket.settimeout(3)
    data = b""
    try:
        while True:
            rcv = clientSocket.recv(1024) #se ahce un timeout cuando termina el rcv y ya no hay nada que recibir
            data = data + rcv
    except socket.timeout as exception:
        return data

def soliparse(requestBytes): 
    solistring = str(requestBytes)
    solistring = requestString.split("\\r\\n")
    requestDictionary = {}
    for field in solistring[1:-2]:
        values = field.split(":")
        requestDictionary[values[0].lower()] = values[1]
    print(requestDictionary)
    return requestDictionary

def cliente(clientSocket, clientAddress):
    rawRequest = receiveRequest(clientSocket) #recibo la llamada del cliente
    parsedRequest = parseRequest(rawRequest) #solicitud del parse
    nuevosock = socket.socket() #creo un socket para conectar al servidor
    host = parsedRequest["host"][1:]
    nuevosock.connect((host, 80))
    nuevosock.send(rawRequest) #mando solicitud al servidor
    # Receive response from destination server
    nuevares = nuevosock.recv(10000000) #recibo respuesta del servidor
    print(nuevares)
    clientSocket.send(nuevares)
    clientSocket.close() #cierro conexion
    

# ---------------------------------- MAIN ---------------------------------------------------------------- 
"""
server = socket.socket()
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(("localhost", 8888))
server.listen(1)
#loopCalls = 0
while True:
    #loopCalls = loopCalls + 1
    #threadname = "ClientThread" + str(loopCalls)
    #print("Loop ", str(loopCalls))
    clientSocket, clientAddress = server.accept()
    clientThread = threading.Thread(target = client, args = (clientSocket, clientAddress))
    clientThread.start()
    #exit() # for testing purposes only """
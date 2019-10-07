#!/usr/bin/python

import multiprocessing

msjs = ["Hola", "Que tal?", "Chau"]

def enviar(conn, msjs):
    for msj in msjs:
        conn.send(msj)
    conn.close()

def recibir(conn):
    while 1:
        msj = conn.recv()
        if msj == "Chau":
            break
        print(msj)

padre_conn, hijo_conn = multiprocessing.Pipe()

p1 = multiprocessing.Process(target=enviar, args=(padre_conn, msjs))
p2 = multiprocessing.Process(target=recibir, args=(hijo_conn,))

p1.start()
p2.start()

p1.join()
p2.join()

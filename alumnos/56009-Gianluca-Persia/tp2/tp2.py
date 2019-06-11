#!/usr/bin/python3

""" TP2 para ejercitar sincronizacion y sus problemas"""

import threading
import time

listab = []
listah = []
cond = threading.Condition()

def seguridad():
        while listab.count("R") == 4 or listab.count("B") == 4:
                listah.append(listab.pop(0))
                listab.append(listah.pop(0))
        else:
                print("Bote: ", listab)

def a_bordo():
        subeh = listah.pop()
        if subeh == 'R':
                print("Sube hincha RIVER")
        else:
                print("Sube hincha BOCA")
        #time.sleep(1)
        listab.append(subeh)
        if len(listab) == 4:
                seguridad()
                print("Lleno")
                #time.sleep(1)
                a_remar()
                #time.sleep(1)
        cond.release()

def a_remar():
        print("-")
        print("Remando")
        print(listab)
        while True:
                for people in range(4):
                        print("Baja:", listab.pop())
                        #time.sleep(1)
                if len(listab) == 0:
                        print("Vacio")
                        print("-")
                        break

def hincha_river():
        hincha = "R"
        listah.append(hincha)
        cond.acquire()
        a_bordo()
        #if len(listab) == 4:
        #        cond.wait()

def hincha_boca():
        hincha = "B"
        listah.append(hincha)
        cond.acquire()
        a_bordo()
        #if len(listab) == 4:
        #        cond.wait()

def barra_brava_river(numeroh):
        """Generacion de hinchas de River"""
        for numero in range(numeroh):
                river = threading.Thread(target=hincha_river)
                river.start()

def barra_brava_boca(numeroh):
        """Generacion de hinchas de Boca"""
        for numero in range(numeroh):
                boca = threading.Thread(target=hincha_boca)
                boca.start()

if __name__ == "__main__":
        hinchariver = threading.Thread(target=barra_brava_river, args=(20,))
        hinchaboca = threading.Thread(target=barra_brava_boca, args=(20,))

        hinchariver.start()
        hinchaboca.start()

        hinchariver.join()
        hinchaboca.join()
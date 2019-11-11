#!/usr/bin/python
import multiprocessing
import os
resultado = []
mq = multiprocessing.Queue()

#Defino la funcion en la cual declaro una lista y un bucle para recorrerla e ir multiplicando
def cuadrado(elemento,subindice):
    print "subindice", subindice, "valor" ,elemento * elemento
    mq.put([subindice,elemento*elemento])
    #print os.getpid()
    return

#Completo el arreglo de mi lista
lista = [1,2,3,4,8,12,4,5]
p = []
nro_hijos = len (lista)
for i in range(nro_hijos):
    p.append( multiprocessing.Process(target=cuadrado, args=(lista[i],i)))
    p[i].start()

for i in range(nro_hijos):
    p[i].join()

print "terminaron todos"
lista2 = []
for i in range(nro_hijos):
    lista2.append ( mq.get())
print lista, lista2

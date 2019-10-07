#!/usr/bin/python

import multiprocessing

resultado = []

#Defino la funcion en la cual declaro una lista y un bucle para recorrerla e ir multiplicando
def cuadrado(lista):
    global resultado

    for num in lista:
        resultado.append(num * num)
    print("Resultado: {}".format(resultado))

#Completo el arreglo de mi lista
lista = [1,2,3,4]

p1 = multiprocessing.Process(target=cuadrado, args=(lista,))
p1.start()
p1.join()

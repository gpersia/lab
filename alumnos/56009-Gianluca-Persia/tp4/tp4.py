#!/usr/bin/python3

import os, sys
import getopt
import array
import argparse
import requests
import urllib.request, urllib.parse, urllib.error #con las librerias urllib me facilita el trabajo con URLS y contienen funciones que permiten la descarga de archivos
from PIL import Image #con la libreria PIL puedo manipular imagenes 
from bs4 import BeautifulSoup #con esta libreria puedo hacer pulling de datos de html o de archivos xml
#import urllib.error
from urllib.request import urlopen #la función recibe una URL, ya sea como cadena de texto o como un objeto Request y su objeto de retorno depende del tipo de URL que se le pase como argumento
import mkred, mkgreen, mkblue

opc, args = getopt.getopt(sys.argv[1:], "u:h")

URLs_images = ""

for o in opc:
    if o[0] == "-h":
        OpcAyuda()
    if o[0] == "-u":
        URLs_images = o[1]
        print(o[1])

urls = URLs_images

hosts = urls.split(",")

contents = {}
imageSources = []

for host in hosts:
    contents[host] = BeautifulSoup(requests.get(host).text, "html.parser")

for host in hosts:
    images = contents[host].findAll("img")
    for img in images:
        imgUrl = img.get("src")
        if imgUrl[0] == "/":
            imgUrl = host + imgUrl
        imageSources.append(imgUrl)

for i in range(len(imageSources)):
    src = imageSources[i]
    parsedUrl = urllib.parse.urlparse(src)
    newUrl = parsedUrl.scheme + "://" + parsedUrl.netloc + parsedUrl.path #devuelve los elementos de la estructura de la url
    imageSources[i] = newUrl

path = 'images/'
cantimages = []

for i in range(len(imageSources)):
    cantimages.append(i)

for url in imageSources:
    cantidad = len(url)
    if (url[cantidad-3::] == "jpg"):
        try:
            nameimg= cantimages.pop()
            urllib.request.urlretrieve(url, ruta+str(nameimg)+".jpg")
            pathimg = 'images/'+str(nameimg)
            img = Image.open(pathimg+".jpg").convert('RGB').save(pathimg+".ppm") #me ayuda a convertir la imagen
            os.remove(pathimg+".jpg")
            mkred.red(pathimg)
            mkgreen.green(pathimg)
            mkblue.blue(pathimg)
        except urllib.error.HTTPError as e:
            print('status', e.code)
            print('reason', e.reason)
    if (url[cantidad-3::] == "png"):
        try:
            nameimg= cantimages.pop()
            urllib.request.urlretrieve(url, ruta+str(nameimg)+'.png')
            pathimg = 'images/'+str(nameimg)
            img = Image.open(pathimg+".png").convert('RGB').save(pathimg+".ppm") #me ayuda a convertir la imagen
            os.remove(pathimg+".png")
            mkred.red(pathimg)
            mkgreen.green(pathimg)
            mkblue.blue(pathimg)
        except urllib.error.HTTPError as e:
            print('status', e.code)
            print('reason', e.reason)
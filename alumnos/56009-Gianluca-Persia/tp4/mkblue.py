#!/usr/bin/python3

import os, array

def blue(path):
    fd = os.open(path+".ppm", os.O_RDONLY)

    head = os.read(fd,15) #leo 15 bytes
    splithead = str(head).split("\\n")

    p_image = splithead[0][2] + splithead[0][3]
    width = int(splithead[1].split()[0])
    height = int(splithead[1].split()[1])
    max_value = int(splithead[2])

    ppm_header = p_image + ' ' + str(width) + ' ' + str(height) + ' ' + str(max_value) + "\n"
    firstimg = os.read(fd, width*height*3)

    img = array.array('B', [0, 0, 0] * width * height)

    for x in range(0, height):
        for y in range(0, width):
            index = 3 * (x * width + y)
            img[index + 2] = firstimg[index + 2]

    #imagen azul guardado
    f =  open(ruta+'blue.ppm', 'wb')
    f.write(bytearray(ppm_header, 'ascii'))
    image.tofile(f)
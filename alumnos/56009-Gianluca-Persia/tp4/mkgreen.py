#!/usr/bin/python3

import os, array

def green(path):
    fd = os.open(path+".ppm", os.O_RDONLY)

    head = os.read(fd,16)
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
            img[index + 1] = firstimg[index + 0]

    #imagen verde guardado
    f = open(path+'green.ppm', 'wb')
    f.write(bytearray(ppm_header, 'ascii'))
    img.tofile(f)
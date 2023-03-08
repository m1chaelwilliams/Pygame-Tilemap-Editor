import pygame as py

def open_file(filename):
    layer = []
    with open(filename, 'r') as f:
        count = 0
        i = 0
        while i < 1:
            if f.readline() != "":
                count += 1
            else:
                i += 1

        f.seek(0)
        global test
        for x in range(count):
            line = f.readline().rstrip("\n")
            rect_line = line[:-2].split(",")
            int_line = map(int, rect_line)
            newline= tuple(int_line)
            value = int(line[-1:])
            sprite = (py.Rect(newline), value)
            layer.append(sprite)
    return layer
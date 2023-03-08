import pygame as py
import blocks

py.init()
screen = py.display.set_mode((1000,1000))
surface = py.Surface((2000,2000))
clock = py.time.Clock()

def open_file(filename, layer):
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
            sprite = (newline, value)
            layer.append(sprite)


            
def draw_rects(tilemap):
    for j in tilemap:
        
        surface.blit(blocks.blocks[j[1]], j[0])     



layer0 = [

]
layer1 = [

]
open_file("layer0.txt", layer0)
open_file("layer1.txt", layer1)

up = False
down = False
right = False
left = False



movement = [0,0]

while True:
    screen.fill('black')
    surface.fill(py.Color("#9aad55"))
    if right:
        movement[0] -= 10
    if left:
        movement[0] += 10
    if up:
        movement[1] += 10
    if down:
        movement[1] -= 10
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            exit()
        if event.type == py.KEYDOWN:
            if event.key == py.K_d:
                right = True
            if event.key == py.K_a:
                left = True
            if event.key == py.K_w:
                up = True
            if event.key == py.K_s:
                down = True
        if event.type == py.KEYUP:
            if event.key == py.K_d:
                right = False
            if event.key == py.K_a:
                left = False
            if event.key == py.K_w:
                up = False
            if event.key == py.K_s:
                down = False
        

    draw_rects(layer1)
    draw_rects(layer0)

    screen.blit(surface, movement)

    py.display.update()
    clock.tick(60)
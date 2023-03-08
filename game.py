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
            sprite = (py.Rect(newline), value)
            layer.append(sprite)


            
def draw_rects(tilemap):
    for j in tilemap:
        
        surface.blit(blocks.blocks[j[1]], j[0])     

def collision_test(rect, tiles):
    hit_list = []
    for tile in tiles:
        if rect.colliderect(tile[0]):
            hit_list.append(tile[0])
    return hit_list

def move(rect, player_movement, tiles):
    collision_types = {'top': False, 'bottom': False, 'right': False, 'left': False}
    rect.x += player_movement[0]
    hit_list = collision_test(rect, tiles)
    for tile in hit_list:
        if player_movement[0] > 0:
            rect.right = tile.left
            collision_types['right'] = True
        elif player_movement[0] < 0:
            rect.left = tile.right
            collision_types['left'] = True
    rect.y += player_movement[1]
    hit_list = collision_test(rect, tiles)
    for tile in hit_list:
        if player_movement[1] > 0:
            rect.bottom = tile.top
            collision_types['bottom'] = True
        elif player_movement[1] < 0:
            rect.top = tile.bottom
            collision_types['top'] = True
    return rect, collision_types

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

player_movement = [0,0]

movement = [0,0]

player = py.transform.scale(py.image.load('square.png').convert(), (50,50))
p_rect = player.get_rect(center = (500,500))

map_pos = [0,0]

while True:
    screen.fill('black')
    surface.fill(py.Color("#9aad55"))
    if right:
        movement[0] = -10
        player_movement[0] = 10
    elif left:
        movement[0] = +10
        player_movement[0] = -10
    else:
        movement[0] = 0
        player_movement[0] = 0
    if up:
        movement[1] = +10
        player_movement[1] = -10
    elif down:
        movement[1] = -10
        player_movement[1] = 10
    else:
        movement[1] = 0
        player_movement[1] = 0
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
    p_rect, collisions = move(p_rect, player_movement, layer0)


    if collisions['right']:
        movement[0] = 0
    if collisions['left']:
        movement[0] = 0
    if collisions['top']:
        movement[1] = 0
    if collisions['bottom']:
        movement[1] = 0

    draw_rects(layer1)
    draw_rects(layer0)
    
    surface.blit(player, p_rect)

    map_pos[0] += movement[0]
    map_pos[1] += movement[1]
    screen.blit(surface, tuple(map_pos))

    py.display.update()
    clock.tick(60)
import pygame as py
import blocks
import tilemapfileopen


py.init()
screen = py.display.set_mode((1000,1000))
surface = py.Surface((2000,2000))
clock = py.time.Clock()




            
def draw_rects(tilemap):
    for j in tilemap:
        if type(blocks.blocks[j[1]]) == list:
            pass     
        else:
            surface.blit(blocks.blocks[j[1]], j[0])     

def draw_animated_rects(tilemap):
    for i in tilemap:
        if i[1] == 4:
            surface.blit(blocks.blocks[i[1]][coin_anim.frame_count], i[0])     
        elif i[1] == 5:
            surface.blit(blocks.blocks[i[1]][flower_anim.frame_count], i[0])     


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

# BLOCK LISTS WITH INDEXES

# 0 - TREE
# 1 - ROCK
# 2 - PATH
# 3 - WATER
# 4 - COIN

layer0 = [

]
layer1 = [

]
layer2 = [

]

layer0 = tilemapfileopen.open_file("layer0.txt")
layer1 = tilemapfileopen.open_file("layer1.txt")
layer2 = tilemapfileopen.open_file("layer2.txt")

up = False
down = False
right = False
left = False

player_movement = [0,0]

movement = [0,0]

player = py.transform.scale(py.image.load('square2.jpeg').convert(), (50,50))
p_rect = player.get_rect(center = (500,500))

map_pos = [0,0]

# ---ANIMATIONS---

class animation:
    amt_frames = 0
    frame_speed = 0
    frame_count = 0
    count = 0
    def __init__(self, frame_speed, frame_count, amt_frames) -> None:
        self.frame_speed = frame_speed
        self.frame_count = frame_count
        self.amt_frames = amt_frames-1
    
    def update(self):
        self.count += 1
        if self.count == self.frame_speed:
            self.count = 0
            if self.frame_count < self.amt_frames:
                self.frame_count += 1
            else:
                self.frame_count = 0
        print(self.frame_count)

coin_anim = animation(10,0,4)
flower_anim = animation(20,0,2)

while True:


    

    screen.fill('black')
    surface.fill(py.Color("#9aad55"))
    if right:
        movement[0] = -5
        player_movement[0] = 5
    elif left:
        movement[0] = +5
        player_movement[0] = -5
    else:
        movement[0] = 0
        player_movement[0] = 0
    if up:
        movement[1] = +5
        player_movement[1] = -5
    elif down:
        movement[1] = -5
        player_movement[1] = 5
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

    draw_rects(layer2)
    draw_rects(layer1)
    draw_rects(layer0)
    draw_animated_rects(layer2)
    draw_animated_rects(layer1)
    draw_animated_rects(layer0)

    for x in layer1:
        if p_rect.colliderect(x[0]) and x[1] == 4:
            layer1.remove(x)
    
    surface.blit(player, p_rect)

    map_pos[0] += movement[0]
    map_pos[1] += movement[1]
    screen.blit(surface, tuple(map_pos))

    coin_anim.update()
    flower_anim.update()

    py.display.update()
    clock.tick(60)

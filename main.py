import pygame as py
import blocks
import math

width = int(input('Enter width of frame in blocks: '))
height = int(input('Enter height of frame in blocks: '))

py.init()
screen = py.display.set_mode((1000,1000))
clock = py.time.Clock()

canvas = py.Surface((800,800))
surface = py.Surface((width*100,height*100))

canvas_layout = py.image.load('canvasLayout.png').convert_alpha()

up = False
down = False
right = False
left = False

movement = [0,0]

def draw_bg(movement):
    canvas.blit(surface, movement)
    screen.blit(canvas, (0,0))

def draw_bg_scaled():
    py.draw.rect(canvas, (100,100,100), (25,25,750,750))
    new_map = py.transform.scale(surface, (700,700))
    canvas.blit(new_map, (50,50))
    screen.blit(canvas, (0,0))

def draw_rects(layout_blocks):
    for i in layout_blocks:
        surface.blit(blocks.blocks[i[1]], i[0])

def get_mouse_cell_pos(mouse_pos, movement):
    cell_x = int(math.floor((mouse_pos[0]-movement[0])/100)*100)
    cell_y = int(math.floor((mouse_pos[1]-movement[1])/100)*100)
    return (cell_x, cell_y)
def compare_rects(rect, mouse_rect):
    if rect == mouse_rect:
        return True
    
def load_map():
    layout_blocks.clear()
    bg_blocks.clear()
    open_file("layer0.txt", layout_blocks)
    open_file("layer1.txt", bg_blocks)

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
        for x in range(count):
            line = f.readline().rstrip("\n")
            rect_line = line[:-2].split(",")
            int_line = map(int, rect_line)
            newline= tuple(int_line)
            value = int(line[-1:])
            sprite = (py.Rect(newline), value)
            
            layer.append(sprite)

        
    
def export_tilemap(tilemap, name):
    with open(name, 'w') as f:
        for x in tilemap:
            
            f.write(str(x[0][0]))
            f.write(',')
            f.write(str(x[0][1]))
            f.write(',')
            f.write(str(x[0][2]))
            f.write(',')
            f.write(str(x[0][3]))
            f.write(',')
            f.write(str(x[1]))
            f.write("\n")



sand_color = py.Color(194,178,128)
grass_green = py.Color("#9aad55")

layout_blocks = [

]

bg_blocks = [

]

# --- ON STARTUP ---



# ------------------


selected_block = 0

selected_layer = 0

# UI VARIABLES

font = py.font.Font('ARCADECLASSIC.ttf', 30)

palette_selection = 0

current_palette = [] # the 6 sprites that are currently on the screen

layers = ['layer 0', 'layer 1']
selected_layer_UI = 0

# map

minimap = False

if(len(blocks.blocks)/6) == 0:
    palette_list = 1

else:
    palette_list = int(len(blocks.blocks)/6)

while True:
    screen.fill('lightblue')
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
        if event.type == py.MOUSEWHEEL:
            if event.y == -1:
                
                if selected_block < len(current_palette)-1:
                    selected_block += 1
                else:
                    selected_block = 0

            if event.y == 1:
                if selected_block > 0:
                    selected_block -= 1
                else:
                    selected_block = len(current_palette)-1
        if event.type == py.KEYDOWN:
            if event.key == py.K_d:
                right = True
            if event.key == py.K_a:
                left = True
            if event.key == py.K_w:
                up = True
            if event.key == py.K_s:
                down = True
            if event.key == py.K_UP:
                selected_layer = 0
                selected_layer_UI = 0
            if event.key == py.K_m:
                minimap = not minimap
            if event.key == py.K_l:
                load_map()
            if event.key == py.K_DOWN:
                selected_layer = 1
                selected_layer_UI = 1

            if event.key == py.K_LEFT:
                if palette_selection > 0:
                    palette_selection -= 6
                    selected_block = 0
  
                
            if event.key == py.K_RIGHT:
                if palette_selection < palette_list:
                    palette_selection += 6
                    selected_block = 0

            if event.key == py.K_RETURN:
                export_tilemap(layout_blocks, "layer0.txt")
                export_tilemap(bg_blocks, "layer1.txt")
     

        if event.type == py.KEYUP:
            if event.key == py.K_d:
                right = False
            if event.key == py.K_a:
                left = False
            if event.key == py.K_w:
                up = False
            if event.key == py.K_s:
                down = False
    mouse_pressed = py.mouse.get_pressed()
    if mouse_pressed[0]:
        if get_mouse_cell_pos(py.mouse.get_pos(), (0,0))[0] > 700 or get_mouse_cell_pos(py.mouse.get_pos(), (0,0))[1] > 700:
            pass
        else:
            mouse_cell_pos = get_mouse_cell_pos(py.mouse.get_pos(), movement)
            count = 0
            if selected_layer == 0:
                for x in layout_blocks:
                    if compare_rects(x[0], py.Rect(mouse_cell_pos[0], mouse_cell_pos[1], 100,100)):
                        count += 1
                if count < 1:
                    layout_blocks.append((py.Rect(mouse_cell_pos[0], mouse_cell_pos[1], 100,100), selected_block+palette_selection))
                    
            else:
                for x in bg_blocks:
                    if compare_rects(x[0], py.Rect(mouse_cell_pos[0], mouse_cell_pos[1], 100,100)):
                        count += 1
                if count < 1:
                    bg_blocks.append((py.Rect(mouse_cell_pos[0], mouse_cell_pos[1], 100,100), selected_block+palette_selection))
                
    if mouse_pressed[2]:
        if get_mouse_cell_pos(py.mouse.get_pos(), (0,0))[0] > 700 or get_mouse_cell_pos(py.mouse.get_pos(), (0,0))[1] > 700:
            pass
        else:
            mouse_cell_pos = get_mouse_cell_pos(py.mouse.get_pos(), movement)
            if selected_layer == 0:
                for x in layout_blocks:
                    if compare_rects(x[0], py.Rect(mouse_cell_pos[0], mouse_cell_pos[1], 100,100)):
                        layout_blocks.remove(x)
            else:
                for x in bg_blocks:
                    if compare_rects(x[0], py.Rect(mouse_cell_pos[0], mouse_cell_pos[1], 100,100)):
                        bg_blocks.remove(x)
                        
    # SCREEN UI ELEMENTS
    screen.blit(canvas_layout, (0,0))

    block_x_pos = 50
    current_palette.clear()
    for i in range(6):
        if i+palette_selection < len(blocks.blocks):
            if selected_block == i:
                py.draw.rect(screen, (255,255,255), py.Rect(block_x_pos-5, 845, 110,110))
            screen.blit(blocks.blocks[i+palette_selection], (block_x_pos, 850))
            current_palette.append(blocks.blocks[i+palette_selection])
            block_x_pos += 125

    layerSpacingy = 100
    for i, x in enumerate(layers):
        layerText = font.render(layers[i], True, (255,255,255))
        if selected_layer_UI == i:
            py.draw.rect(screen, (255,128,128), py.Rect(850, layerSpacingy, 100,50))
        screen.blit(layerText, (850, layerSpacingy))
        layerSpacingy += 100

    surface.fill(grass_green)
    for x in range(width):
        py.draw.line(surface, (255,255,255), (x*100, 0), (x*100, height*100), 1)
    for x in range(height):
        py.draw.line(surface, (255,255,255), (0,x*100), (width*100,x*100), 1)

    draw_rects(bg_blocks)
    draw_rects(layout_blocks)
    
    canvas.fill('darkblue')
    draw_bg(movement)

    if minimap:
        draw_bg_scaled()
        

    py.display.update()
    clock.tick(60)
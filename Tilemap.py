import pygame as py
import blocks
import tilemapfileopen as openfile
import math



py.init()
screen = py.display.set_mode((1000,1000))
clock = py.time.Clock()

canvas = py.Surface((800,800))
surface = py.Surface((100,100))

canvas_layout = py.image.load('canvasLayout.png').convert_alpha()

up = False
down = False
right = False
left = False

movement = [0,0]

dimensions = True

canvas_width = 0
canvas_height = 0

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
        if type(blocks.blocks[i[1]]) == list:
            surface.blit(blocks.blocks[i[1]][0], i[0])
        else:
            surface.blit(blocks.blocks[i[1]], i[0])

def get_mouse_cell_pos(mouse_pos, movement):
    cell_x = int(math.floor((mouse_pos[0]-movement[0])/100)*100)
    cell_y = int(math.floor((mouse_pos[1]-movement[1])/100)*100)
    return (cell_x, cell_y)
def compare_rects(rect, mouse_rect):
    if rect == mouse_rect:
        return True
    
def load_map(layer, filename):
    layer.clear()
    layer = openfile.open_file(filename)
    return layer




        
    
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

def set_canvas(canvas_surface, canvas_width, canvas_height):
    canvas_surface = py.Surface((canvas_width*100, canvas_height*100))
    return canvas_surface


sand_color = py.Color(194,178,128)
grass_green = py.Color("#9aad55")

layout_blocks = [

]

bg_blocks = [

]
bg_blocks2 = [

]

# --- ON STARTUP ---



# ------------------


selected_block = 0

selected_layer = 0

# UI VARIABLES

font = py.font.Font('ARCADECLASSIC.ttf', 30)

palette_selection = 0

current_palette = [] # the 6 sprites that are currently on the screen

layers = ['layer 0', 'layer 1', 'layer2']
selected_layer_UI = 0

# map

minimap = False

if(len(blocks.blocks)/6) == 0:
    palette_list = 1

else:
    palette_list = int(len(blocks.blocks)/6)

while dimensions:
    screen.fill('darkblue')

    dimensions_text_width = font.render(f'Width in blocks   {str(canvas_width)}   Left/Right', True, (255,255,255), None)
    dimensions_text_rect = dimensions_text_width.get_rect(center = (500,500))
    dimensions_text_height = font.render(f'Width in blocks   {str(canvas_height)}   Up/Down', True, (255,255,255), None)
    dimensions_height_rect = dimensions_text_height.get_rect(center = (500,700))

    screen.blit(dimensions_text_width, dimensions_text_rect)
    screen.blit(dimensions_text_height, dimensions_height_rect)
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            exit()
        if event.type == py.KEYDOWN:
            if event.key == py.K_LEFT:
                canvas_width -= 1
            if event.key == py.K_RIGHT:
                canvas_width += 1
            if event.key == py.K_UP:
                canvas_height += 1
            if event.key == py.K_DOWN:
                canvas_height -= 1
            if event.key == py.K_RETURN:
                surface = set_canvas(surface, canvas_width, canvas_width)
                dimensions = not dimensions
    
    py.display.update()
    clock.tick(60)

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
                if selected_layer > 0:
                    selected_layer -= 1
                    selected_layer_UI -= 1
                else:
                    selected_layer = 2
                    selected_layer_UI = 2
            if event.key == py.K_m:
                minimap = not minimap
            if event.key == py.K_l:
                layout_blocks = load_map(layout_blocks, "layer0.txt")
                bg_blocks = load_map(bg_blocks, "layer1.txt")
                bg_blocks2 = load_map(bg_blocks2, "layer2.txt")
            if event.key == py.K_DOWN:
                if selected_layer < 2:
                    selected_layer += 1
                    selected_layer_UI += 1
                else:
                    selected_layer = 0
                    selected_layer_UI = 0
                

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
                export_tilemap(bg_blocks2, "layer2.txt")
     

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
                    
            elif selected_layer == 1:
                for x in bg_blocks:
                    if compare_rects(x[0], py.Rect(mouse_cell_pos[0], mouse_cell_pos[1], 100,100)):
                        count += 1
                if count < 1:
                    bg_blocks.append((py.Rect(mouse_cell_pos[0], mouse_cell_pos[1], 100,100), selected_block+palette_selection))
            elif selected_layer == 2:
                for x in bg_blocks2:
                    if compare_rects(x[0], py.Rect(mouse_cell_pos[0], mouse_cell_pos[1], 100,100)):
                        count += 1
                if count < 1:
                    bg_blocks2.append((py.Rect(mouse_cell_pos[0], mouse_cell_pos[1], 100,100), selected_block+palette_selection))
                
    if mouse_pressed[2]:
        if get_mouse_cell_pos(py.mouse.get_pos(), (0,0))[0] > 700 or get_mouse_cell_pos(py.mouse.get_pos(), (0,0))[1] > 700:
            pass
        else:
            mouse_cell_pos = get_mouse_cell_pos(py.mouse.get_pos(), movement)
            if selected_layer == 0:
                for x in layout_blocks:
                    if compare_rects(x[0], py.Rect(mouse_cell_pos[0], mouse_cell_pos[1], 100,100)):
                        layout_blocks.remove(x)
            elif selected_layer == 1:
                for x in bg_blocks:
                    if compare_rects(x[0], py.Rect(mouse_cell_pos[0], mouse_cell_pos[1], 100,100)):
                        bg_blocks.remove(x)
            elif selected_layer == 2:
                for x in bg_blocks2:
                    if compare_rects(x[0], py.Rect(mouse_cell_pos[0], mouse_cell_pos[1], 100,100)):
                        bg_blocks2.remove(x)
                        
    # SCREEN UI ELEMENTS
    screen.blit(canvas_layout, (0,0))

    block_x_pos = 50
    current_palette.clear()
    for i in range(6):
        if i+palette_selection < len(blocks.blocks):
            if selected_block == i:
                py.draw.rect(screen, (255,255,255), py.Rect(block_x_pos-5, 845, 110,110))
            
            if type(blocks.blocks[i+palette_selection]) == list:
                current_palette.append(blocks.blocks[i+palette_selection][0])
                screen.blit(blocks.blocks[i+palette_selection][0], (block_x_pos, 850))
            else:
                current_palette.append(blocks.blocks[i+palette_selection])
                screen.blit(blocks.blocks[i+palette_selection], (block_x_pos, 850))
            block_x_pos += 125

    layerSpacingy = 100
    for i, x in enumerate(layers):
        layerText = font.render(layers[i], True, (255,255,255))
        if selected_layer_UI == i:
            py.draw.rect(screen, (255,128,128), py.Rect(850, layerSpacingy, 100,50))
        screen.blit(layerText, (850, layerSpacingy))
        layerSpacingy += 100

    surface.fill(grass_green)
    for x in range(canvas_width):
        py.draw.line(surface, (255,255,255), (x*100, 0), (x*100, canvas_height*100), 1)
    for x in range(canvas_height):
        py.draw.line(surface, (255,255,255), (0,x*100), (canvas_width*100,x*100), 1)

    draw_rects(bg_blocks2)
    draw_rects(bg_blocks)
    draw_rects(layout_blocks)
    
    canvas.fill('darkblue')
    draw_bg(movement)

    if minimap:
        draw_bg_scaled()
        

    py.display.update()
    clock.tick(60)
import pygame as py

py.init()

py.display.set_mode((1000,1000))

bush = py.transform.scale(py.image.load('bush.png').convert_alpha(), (100,100))
rock = py.transform.scale(py.image.load('rock.png').convert_alpha(), (100,100))
path = py.transform.scale(py.image.load('ground.png').convert_alpha(), (100,100))

blocks = [
    bush,
    rock,
    path,
    path,
    path,
    path,
    bush,
    path,
    rock,
    path,
]
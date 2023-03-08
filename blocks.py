import pygame as py
import os

py.init()

py.display.set_mode((1000,1000))

bush = py.transform.scale(py.image.load(os.path.join('sprites', 'bush.png')).convert_alpha(), (100,100))
rock = py.transform.scale(py.image.load(os.path.join('sprites', 'rock.png')).convert_alpha(), (100,100))
path = py.transform.scale(py.image.load(os.path.join('sprites', 'ground.png')).convert_alpha(), (100,100))
water = py.transform.scale(py.image.load(os.path.join('sprites', 'water.png')).convert_alpha(), (100,100))

coin0 = py.transform.scale(py.image.load(os.path.join('sprites', 'coin', 'coin_0.png')).convert_alpha(), (100,100))
coin1 = py.transform.scale(py.image.load(os.path.join('sprites', 'coin', 'coin_1.png')).convert_alpha(), (100,100))
coin2 = py.transform.scale(py.image.load(os.path.join('sprites', 'coin', 'coin_2.png')).convert_alpha(), (100,100))
coin3 = py.transform.scale(py.image.load(os.path.join('sprites', 'coin', 'coin_3.png')).convert_alpha(), (100,100))

coin = [coin0, coin1, coin2, coin3]

flower0 = py.transform.scale(py.image.load(os.path.join('sprites', 'flower', 'flower_0.png')).convert_alpha(), (100,100))
flower1 = py.transform.scale(py.image.load(os.path.join('sprites', 'flower', 'flower_1.png')).convert_alpha(), (100,100))

flower = [flower0, flower1]


blocks = [
    bush,
    rock,
    path,
    water,
    coin,
    flower,
    bush,
    path,
    rock,
    path,
]
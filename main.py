from pygame import *
from random import randint
import json

win_height = 500
win_width = 700

img_back = "road.png"

window = display.set_mode((win_width,win_height))

background =transform.scale(image.load(img_back), (win_width,win_height))
window.blit(background,(0,0))

run = True
finish = False

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        display.update()
    
    time.delay(55)
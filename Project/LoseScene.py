import Game_Framework
from pico2d import *

def init():
    global lose_image, cur_time

    lose_image = load_image("../Sprite/You_Lose.png")
    cur_time = 0

def update():
    global cur_time
    cur_time += Game_Framework.frame_time
    if cur_time >= 3.0:
        Game_Framework.pop_scene()

def draw():
    lose_image.clip_draw(0, 0, 1600, 900, 800, 450)
    update_canvas()

def pause(): pass
def resume(): pass

def finish():
    global lose_image
    del lose_image

def Input_Event():
    pass
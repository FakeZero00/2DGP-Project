import Game_Framework
from pico2d import *

def init():
    global image, sfx, cur_time

    sfx = load_wav('../Sound/Newtype_Flash.wav')
    sfx.set_volume(50)
    sfx.play()

    image = load_image("../Sprite/Newtype.png")

    cur_time = 0

def update():
    global cur_time
    cur_time += Game_Framework.frame_time



def draw():
    global image, cur_time

    if cur_time <= 1.5:
        image.clip_draw(0, 0, 400, 300, 800, 450, 800, 600)
    elif cur_time > 1.5:
        Game_Framework.pop_scene()
    update_canvas()

def pause(): pass
def resume(): pass
def finish():
    global image, sfx
    del image, sfx

def Input_Event():
    event_list = get_events()
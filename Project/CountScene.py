import Game_Framework, Global_Object, PlayScene_world
from pico2d import *

def init():
    global numbers, cur_time

    numbers = load_image("Sprite/Numbers.png")
    cur_time = 4.0

def update():
    global cur_time
    cur_time -= Game_Framework.frame_time
    if cur_time <= 0.0:
        Game_Framework.pop_scene()

def draw():
    clear_canvas()
    PlayScene_world.render()
    if cur_time >= 0.0:
        numbers.clip_draw(int(cur_time) * 512, 0, 512, 512, 800, 450)
    update_canvas()

def pause(): pass
def resume(): pass

def finish():
    global numbers
    del numbers

    Global_Object.Global_Start = False

def Input_Event():
    event_list = get_events()
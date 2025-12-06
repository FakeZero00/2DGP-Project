import Game_Framework, Global_Object
from pico2d import *

def init():
    global win_image, cur_time

    win_image = load_image("../Sprite/You_Win.png")
    cur_time = 0

def update():
    global cur_time
    cur_time += Game_Framework.frame_time
    if cur_time >= 3.0:
        Game_Framework.pop_scene()

def draw():
    win_image.clip_draw(0, 0, 1600, 900, 800, 450)
    update_canvas()

def pause(): pass
def resume(): pass

def finish():
    global win_image
    del win_image

    Global_Object.p1hp.current_point = 100
    Global_Object.p2hp.current_point = 100

    Global_Object.p1.x = 300
    Global_Object.p1.y = 250
    Global_Object.p1.statemachine.handle_state_event(('IDLE', Global_Object.p1.IDLE), Global_Object.p1.object_state)

    Global_Object.p2.x = 1300
    Global_Object.p2.y = 250
    Global_Object.p2.statemachine.handle_state_event(('IDLE', Global_Object.p2.IDLE), Global_Object.p2.object_state)

def Input_Event():
    event_list = get_events()
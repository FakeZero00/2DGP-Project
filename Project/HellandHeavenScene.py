import Game_Framework, Global_Object
from Project.Gundam import Gundam
from pico2d import *

MOVE_SPEED_PPS = 200
MOVE_SPEED_PPS2 = 2000

def init():
    global background_image, Gaogaigar_image, Gaogaigar_sprite, Gundam_image, GS_Ride_image, cur_time, frame, sfx, position, position2

    sfx = load_wav('../Sound/Hell&Heaven.wav')
    sfx.set_volume(50)
    sfx.play()

    background_image = load_image("../Sprite/Hell_and_Heaven_Background.png")
    Gaogaigar_image = load_image("../Sprite/Hell&Heaven.png")
    Gaogaigar_sprite = load_image("../Sprite/Gaogaigar_Sprite.png")
    Gundam_image = load_image("../Sprite/Gundam_Sprite.png")
    GS_Ride_image = load_image("../Sprite/GS_Ride.jpg")
    cur_time = 0
    frame = 0
    position = 1000
    position2 = 1200

def update():
    global cur_time, frame, position, position2
    cur_time += Game_Framework.frame_time
    if cur_time > 4.2 and cur_time <= 8.2:
        frame = (frame + 1) % 2
    elif cur_time > 14.0 and cur_time <= 16.0:
        position -= MOVE_SPEED_PPS * Game_Framework.frame_time
    elif cur_time > 16.0 and cur_time <= 17.0:
        position2 -= MOVE_SPEED_PPS * Game_Framework.frame_time
    elif cur_time > 18.0 and cur_time <= 24.2:
        position2 -= MOVE_SPEED_PPS2 * Game_Framework.frame_time

def draw():
    global background_image, Gaogaigar_image, Gaogaigar_sprite, Gundam_image, GS_Ride_image, cur_time, frame, position, position2

    clear_canvas()
    background_image.draw(800, 450)
    if cur_time <= 4.2:
        Gaogaigar_sprite.clip_draw(0, 0, 800, 800, 800, 450, 800, 800)
    elif cur_time > 4.2 and cur_time <= 6.0:
        GS_Ride_image.clip_draw(frame * 960, 0, 960, 720, 800, 450, 960, 720)
    elif cur_time > 6.0 and cur_time <= 8.2:
        Gaogaigar_image.clip_draw(frame * 800, 0, 800, 800, 800, 450, 800, 800)
    elif cur_time > 8.2 and cur_time <= 10.1:
        Gaogaigar_image.clip_draw(2 * 800, 0, 800, 800, 800, 450, 800, 800)
    elif cur_time > 10.1 and cur_time <= 12.0:
        Gaogaigar_image.clip_draw(3 * 800, 0, 800, 800, 800, 450, 800, 800)
    elif cur_time > 12.0 and cur_time <= 14.0:
        Gundam_image.clip_draw(5 * 800, 0, 880, 790, 800, 450, 800, 800)
    elif cur_time > 14.0 and cur_time <= 16.0:
        Gaogaigar_image.clip_draw(4 * 800, 0, 800, 800, position, 450, 800, 800)
    elif cur_time > 16.0 and cur_time <= 24.2:
        Gundam_image.clip_draw(5 * 800, 0, 880, 790, 300, 450, 550, 500)
        Gaogaigar_image.clip_draw(5 * 800, 0, 800, 800, position2, 450, 500, 500)
    elif cur_time > 24.2:
        Game_Framework.pop_scene()
    update_canvas()

def pause(): pass
def resume(): pass
def finish():
    global background_image, Gaogaigar_image, Gaogaigar_sprite, Gundam_image, GS_Ride_image, sfx
    del background_image, Gaogaigar_image, Gaogaigar_sprite, Gundam_image, GS_Ride_image
    del sfx

    if type(Global_Object.p1) is Gundam:
        Global_Object.p1hp.current_point = 0
    elif type(Global_Object.p2) is Gundam:
        Global_Object.p2hp.current_point = 0

def Input_Event():
    event_list = get_events()
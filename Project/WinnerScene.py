import Game_Framework, Global_Object, PlayScene_world, TitleScene
from Gaogaigar import Gaogaigar
from Gundam import Gundam
from pico2d import *

def init():
    global background_image, Gaogaigar_image, Gundam_image, win_text, cur_time

    background_image = load_image("Sprite/Title_Background.png")
    Gaogaigar_image = load_image("Sprite/Gaogaigar.jpg")
    Gundam_image = load_image("Sprite/Gundam.jpg")
    win_text = load_image("Sprite/Winner.png")
    cur_time = 0

def update():
    global cur_time
    cur_time += Game_Framework.frame_time
    if cur_time >= 3.0:
        Game_Framework.change_scene(TitleScene)

def draw():
    global background_image, Gaogaigar_image, Gundam_image, win_text, cur_time

    clear_canvas()
    background_image.clip_draw(0, 0, 1600, 900, 800, 450)
    if Global_Object.p1wp.current_point == 2:
        if type(Global_Object.p1) == Gaogaigar:
            Gaogaigar_image.clip_draw(0, 0, 853, 1200, 800, 450, 568, 800)
        elif type(Global_Object.p1) == Gundam:
            Gundam_image.clip_draw(0, 0, 423, 600, 800, 450, 550, 800)
    elif Global_Object.p2wp.current_point == 2:
        if type(Global_Object.p2) == Gaogaigar:
            Gaogaigar_image.clip_draw(0, 0, 853, 1200, 800, 450, 568, 800)
        elif type(Global_Object.p2) == Gundam:
            Gundam_image.clip_draw(0, 0, 423, 600, 800, 450, 550, 800)
    win_text.clip_draw(0, 0, 1600, 900, 800, 450)
    update_canvas()

def pause(): pass
def resume(): pass
def finish():
    global background_image, Gaogaigar_image, Gundam_image, win_text
    del background_image, Gaogaigar_image, Gundam_image, win_text

    PlayScene_world.remove_object(Global_Object.p1)
    PlayScene_world.remove_object(Global_Object.p2)

    PlayScene_world.remove_object(Global_Object.p1hp)
    PlayScene_world.remove_object(Global_Object.p2hp)

    PlayScene_world.remove_object(Global_Object.p1pp)
    PlayScene_world.remove_object(Global_Object.p2pp)

    PlayScene_world.remove_object(Global_Object.p1wp)
    PlayScene_world.remove_object(Global_Object.p2wp)

    del Global_Object.p1, Global_Object.p2
    del Global_Object.p1hp, Global_Object.p2hp
    del Global_Object.p1pp, Global_Object.p2pp
    del Global_Object.p1wp, Global_Object.p2wp

def Input_Event():
    event_list = get_events()
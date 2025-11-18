import Game_Framework
from pico2d import *

def init():
    global image, logo_start_time

    image = load_image("../Sprite/Title_Background.png")

def update():
    pass

def draw():
    clear_canvas()
    image.draw(800, 450)
    update_canvas()

def resume(): pass

def finish():
    global image
    del image

def Input_Event():
    event_list = get_events()
    for event in event_list:
        if event.type == SDL_QUIT:  # 창 닫기 버튼
            Game_Framework.quit()
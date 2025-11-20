import Game_Framework
from pico2d import *

TIME_PER_VIDEO = 5.0
VIDEO_PER_TIME = 1.0 / TIME_PER_VIDEO

def init():
    global background_image, title_image, title_animation, framex, framey, frame

    background_image = load_image("../Sprite/Title_Background.png")
    title_image = load_image("../Sprite/Title.png")

    
    frame = 0.0

def update():
    global frame
    frame += frame * VIDEO_PER_TIME * Game_Framework.frame_time

def draw():
    clear_canvas()
    background_image.draw(800, 450)
    title_image.clip_draw(0, 0, 1600, 900, 800, 450, 1600, 900)
    update_canvas()

def pause(): pass
def resume(): pass

def finish():
    global background_image, letter_image, title_image
    del background_image, letter_image, title_image

def Input_Event():
    event_list = get_events()
    for event in event_list:
        if event.type == SDL_QUIT:  # 창 닫기 버튼
            Game_Framework.quit()
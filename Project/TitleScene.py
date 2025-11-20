import Game_Framework, TitleScene_world, PlayScene
from pico2d import *
from Button import Button

TIME_PER_VIDEO = 5.0
VIDEO_PER_TIME = 1.0 / TIME_PER_VIDEO

def init():
    global background_image, title_image, start_button, exit_button

    background_image = load_image("../Sprite/Title_Background.png")
    title_image = load_image("../Sprite/Title.png")

    start_button = Button('Start_Button.png', 300, 100, 500, 200, 1)
    TitleScene_world.add_object(start_button)
    exit_button = Button('Exit_Button.png', 300, 100, 1100, 200, 0)
    TitleScene_world.add_object(exit_button)

def update():
    TitleScene_world.update()
    TitleScene_world.handle_collisions()

def draw():
    clear_canvas()
    background_image.draw(800, 450)
    title_image.clip_draw(0, 0, 1600, 900, 800, 450, 1600, 900)
    TitleScene_world.render()
    update_canvas()

def pause(): pass
def resume(): pass

def finish():
    global background_image, title_image, start_button, exit_button
    del background_image, title_image, start_button, exit_button

def Input_Event():
    event_list = get_events()
    for event in event_list:
        if event.type == SDL_QUIT:  # 창 닫기 버튼
            Game_Framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RETURN:
                if start_button.state == 1: Game_Framework.change_scene(PlayScene)
                elif exit_button.state == 1: Game_Framework.quit()
            else:
                start_button.handle_event(event)
                exit_button.handle_event(event)
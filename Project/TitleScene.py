import Game_Framework, TitleScene_world, SelectScene, Global_Object
from pico2d import *
from Button import Button

TIME_PER_VIDEO = 5.0
VIDEO_PER_TIME = 1.0 / TIME_PER_VIDEO

def init():
    global background_image, title_image, start_button, training_button, exit_button

    if Global_Object.Button_Enter_sfx is None:
        Global_Object.Button_Enter_sfx = load_wav('../Sound/Button_Enter.wav')
        Global_Object.Button_Enter_sfx.set_volume(10)

    Global_Object.Background_Music = load_music('../Sound/Gong.wav')
    Global_Object.Background_Music.set_volume(10)
    Global_Object.Background_Music.repeat_play()

    background_image = load_image("../Sprite/Title_Background.png")
    title_image = load_image("../Sprite/Title.png")

    start_button = Button('Start_Button.png', 300, 100, 400, 200, 1)
    TitleScene_world.add_object(start_button)
    training_button = Button('Training_Button.png', 300, 100, 800, 200, 0)
    TitleScene_world.add_object(training_button)
    exit_button = Button('Exit_Button.png', 300, 100, 1200, 200, 0)
    TitleScene_world.add_object(exit_button)

def update():
    Global_Object.Current_mode_number = clamp(0, Global_Object.Current_mode_number, 2)
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
    global background_image, title_image, start_button, training_button, exit_button
    del background_image, title_image, start_button, training_button, exit_button

def Input_Event():
    event_list = get_events()
    for event in event_list:
        if event.type == SDL_QUIT:  # 창 닫기 버튼
            Game_Framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RETURN:
                Global_Object.Button_Enter_sfx.play()
                if start_button.state == 1:
                    Game_Framework.change_scene(SelectScene)
                    Global_Object.Current_mode = 'Play'
                elif training_button.state == 1:
                    Game_Framework.change_scene(SelectScene)
                    Global_Object.Current_mode = 'Training'
                elif exit_button.state == 1: Game_Framework.quit()
            elif event.key == SDLK_LEFT:
                Global_Object.Current_mode_number -= 1
                Global_Object.Current_mode_number = clamp(0, Global_Object.Current_mode_number, 2)
                start_button.handle_event(event)
                training_button.handle_event(event)
                exit_button.handle_event(event)
            elif event.key == SDLK_RIGHT:
                Global_Object.Current_mode_number += 1
                Global_Object.Current_mode_number = clamp(0, Global_Object.Current_mode_number, 2)
                start_button.handle_event(event)
                training_button.handle_event(event)
                exit_button.handle_event(event)

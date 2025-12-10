import Game_Framework, SelectScene_world, PlayScene, TrainingScene, Global_Object
from pico2d import *
from Button import Button
from Project.Gaogaigar import Gaogaigar
from Project.Gundam import Gundam

TIME_PER_VIDEO = 5.0
VIDEO_PER_TIME = 1.0 / TIME_PER_VIDEO

def init():
    global background_image, banner_image, gaogaigar_button, gundam_button

    Global_Object.Background_Music = load_music('../Sound/Select_Background_Music.wav')
    Global_Object.Background_Music.set_volume(10)
    Global_Object.Background_Music.repeat_play()

    background_image = load_image("../Sprite/Title_Background.png")
    banner_image = load_image("../Sprite/Select_Your_Character.png")

    gaogaigar_button = Button('Gaogaigar.jpg', 853, 1200, 500, 400, 0)
    SelectScene_world.add_object(gaogaigar_button)
    gundam_button = Button('Gundam.jpg', 423, 600, 1100, 400, 1)
    SelectScene_world.add_object(gundam_button)

def update():
    SelectScene_world.update()
    SelectScene_world.handle_collisions()

def draw():
    clear_canvas()
    background_image.draw(800, 450)
    banner_image.clip_draw(0, 0, 600, 100, 800, 800, 600, 100)
    SelectScene_world.render()
    update_canvas()

def pause(): pass
def resume(): pass

def finish():
    global background_image, banner_image, gaogaigar_button, gundam_button
    del background_image, banner_image, gaogaigar_button, gundam_button

def Input_Event():
    event_list = get_events()
    for event in event_list:
        if event.type == SDL_QUIT:  # 창 닫기 버튼
            Game_Framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RETURN:
                if gaogaigar_button.state == 0:
                    Global_Object.p1 = Gaogaigar('p1')
                    Global_Object.p2 = Gundam('p2')
                elif gundam_button.state == 0:
                    Global_Object.p1 = Gundam('p1', 300, 250)
                    Global_Object.p2 = Gaogaigar('p2', 1300, 250)
                Global_Object.Button_Enter_sfx.play()
                if Global_Object.Current_mode == 'Play':
                    Game_Framework.change_scene(PlayScene)
                elif Global_Object.Current_mode == 'Training':
                    Game_Framework.change_scene(TrainingScene)
            else:
                gaogaigar_button.handle_event(event)
                gundam_button.handle_event(event)
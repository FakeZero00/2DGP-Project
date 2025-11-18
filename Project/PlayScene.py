from pico2d import *
from Project.Gaogaigar import Gaogaigar, command_buffer
from Project.Background import Background
from Project.Ground import Ground
import PlayScene_world, Game_Framework

#========= 씬 함수 ==========
def init():
    global gaogaigar

    background = Background(0)
    PlayScene_world.add_object(background, 0)

    ground = Ground(0)
    PlayScene_world.add_object(ground, 0)

    gaogaigar = Gaogaigar()
    PlayScene_world.add_object(gaogaigar)

    PlayScene_world.add_collision_pairs('gaogaigar:ground', gaogaigar, ground)

def update():
    PlayScene_world.update()
    PlayScene_world.handle_collisions()
    print(command_buffer.tokens())

def draw():
    clear_canvas()
    PlayScene_world.render()
    update_canvas()

def finish(): pass
def resume(): pass
def pause(): pass
def resume(): pass

#====== Input 이벤트 처리 함수 =====
def Input_Event():
    event_list = get_events()
    for event in event_list:
        if event.type == SDL_QUIT: # 창 닫기 버튼
            Game_Framework.quit()
        else:
            gaogaigar.handle_event(event)
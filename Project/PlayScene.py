from pico2d import *
from Project.Gaogaigar import Gaogaigar
import PlayScene_world
from Project.Gaogaigar import command_buffer

#========= 씬 함수 ==========
def init():
    global gaogaigar

    gaogaigar = Gaogaigar()
    PlayScene_world.add_object(gaogaigar)

def update():
    PlayScene_world.update()
    print(command_buffer.tokens())

def draw():
    clear_canvas()
    PlayScene_world.render()
    update_canvas()

def finish(): pass
def resume(): pass

#====== Input 이벤트 처리 함수 =====
def Input_Event():
    global Window_Running

    event_list = get_events()
    for event in event_list:
        if event.type == SDL_QUIT: # 창 닫기 버튼
            Window_Running = False
        else:
            gaogaigar.handle_event(event)

#========= 전역 변수 ==========
Running = True
from pico2d import *
from Project.Gaogaigar import Gaogaigar, command_buffer
import PlayScene_world

open_canvas(1600, 900)

#========= 월드 함수 ==========
def reset_world():
    global gaogaigar

    gaogaigar = Gaogaigar()
    PlayScene_world.add_object(gaogaigar)

def update_world():
    PlayScene_world.update()

def render_world():
    clear_canvas()
    PlayScene_world.render()
    update_canvas()

#Input 이벤트 처리 함수
def Input_Event():
    global Window_Running

    event_list = get_events()
    for event in event_list:
        if event.type == SDL_QUIT: # 창 닫기 버튼
            Window_Running = False
        else:
            gaogaigar.handle_event(event)

#========= 전역 변수 ==========
Window_Running = True

#========= 메인 루프 ==========
reset_world()

while Window_Running:
    Input_Event()
    update_world()
    render_world()
    print(command_buffer.tokens())
    delay(1 / 20)

close_canvas()
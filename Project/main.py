from pico2d import *
from Project.Gaogaigar import Gaogaigar

open_canvas(1600, 900)

#========= 월드 함수 ==========
def reset_world():
    global world
    global gaogaigar

    world = []

    gaogaigar = Gaogaigar()
    world.append(gaogaigar)

def update_world():
    for o in world:
        o.update()

def render_world():
    clear_canvas()
    for o in world:
        o.draw()
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
    delay(1 / 20)

close_canvas()
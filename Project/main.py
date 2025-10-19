from pico2d import *

open_canvas(1600, 900)




#Input 이벤트 처리 함수
def Input_Event():
    global Window_Running

    event_list = get_events()
    for event in event_list:
        if event.type == SDL_QUIT: # 창 닫기 버튼
            Window_Running = False

#========= 전역 변수 ==========
Window_Running = True

#========= 메인 루프 ==========
while Window_Running:
    Input_Event()

close_canvas()
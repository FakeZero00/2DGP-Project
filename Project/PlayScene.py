from pico2d import *
from Project.Gaogaigar import Gaogaigar
from Project.Gundam import Gundam
from Project.Background import Background
from Project.Ground import Ground
from Project.Hpbar import Hpbar
from Project.Timer import Timer
import PlayScene_world, Game_Framework, Global_Object

#========= 씬 함수 ==========
def init():
    global gaogaigar, gundam

    background = Background(0)
    PlayScene_world.add_object(background, 0)

    ground = Ground(0)
    PlayScene_world.add_object(ground, 0)

    p1hp = Hpbar(1)
    PlayScene_world.add_object(p1hp, 0)
    p2hp = Hpbar(2)
    PlayScene_world.add_object(p2hp, 0)

    timer = Timer(60)
    PlayScene_world.add_object(timer, 0)

    Global_Object.p1 = Gaogaigar('p1')
    PlayScene_world.add_object(Global_Object.p1)

    Global_Object.p2 = Gundam('p2')
    PlayScene_world.add_object(Global_Object.p2)

    PlayScene_world.add_collision_pairs('p1_body:p2_body', Global_Object.p1.get_collider('body'), Global_Object.p2.get_collider('body'))

def update():
    PlayScene_world.update()
    PlayScene_world.handle_collisions()
    print(Global_Object.p1.command_buffer.tokens())

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
            Global_Object.p1.handle_event(event)
            Global_Object.p2.handle_event(event)
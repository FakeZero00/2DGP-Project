from pico2d import *
from Project.Gaogaigar import Gaogaigar
from Project.Gundam import Gundam
from Project.Background import Background
from Project.Ground import Ground
from Project.Bar import Bar
from Project.Timer import Timer
from Project.WinPoint import WinPoint
import PlayScene_world, Game_Framework, Global_Object, WinScene, LoseScene, DrawScene, WinnerScene

#========= 씬 함수 ==========
def init():
    global gaogaigar, gundam, timer

    background = Background(0)
    PlayScene_world.add_object(background, 0)

    ground = Ground(0)
    PlayScene_world.add_object(ground, 0)

    Global_Object.p1hp = Bar(1, 'HP', 100)
    PlayScene_world.add_object(Global_Object.p1hp, 0)
    Global_Object.p2hp = Bar(2, 'HP', 100)
    PlayScene_world.add_object(Global_Object.p2hp, 0)

    Global_Object.p1pp = Bar(1, 'PP', 0)
    PlayScene_world.add_object(Global_Object.p1pp, 0)
    Global_Object.p2pp = Bar(2, 'PP', 0)
    PlayScene_world.add_object(Global_Object.p2pp, 0)

    Global_Object.p1wp = WinPoint(1)
    PlayScene_world.add_object(Global_Object.p1wp, 0)
    Global_Object.p2wp = WinPoint(2)
    PlayScene_world.add_object(Global_Object.p2wp, 0)

    timer = Timer(60)
    PlayScene_world.add_object(timer, 0)

    Global_Object.p1 = Gaogaigar('p1')
    PlayScene_world.add_object(Global_Object.p1)

    Global_Object.p2 = Gundam('p2')
    PlayScene_world.add_object(Global_Object.p2)

    PlayScene_world.add_collision_pairs('p1_body:p2_body', Global_Object.p1.get_collider('body'), Global_Object.p2.get_collider('body'))
    PlayScene_world.add_collision_pairs('p1_body:p2_attack', Global_Object.p1.get_collider('body'), Global_Object.p2.get_collider('attack'))
    PlayScene_world.add_collision_pairs('p2_body:p1_attack', Global_Object.p2.get_collider('body'), Global_Object.p1.get_collider('attack'))

    if type(Global_Object.p1) == Gaogaigar:
        pass
    elif type(Global_Object.p1) == Gundam:
        PlayScene_world.add_collision_pairs('p1_body:broken_magnum', Global_Object.p1.get_collider('body'), None)

    if type(Global_Object.p2) == Gaogaigar:
        pass
    elif type(Global_Object.p2) == Gundam:
        PlayScene_world.add_collision_pairs('p2_body:broken_magnum', Global_Object.p2.get_collider('body'), None)

def update():
    PlayScene_world.update()
    PlayScene_world.handle_collisions()
    print(Global_Object.p1.command_buffer.tokens())

def draw():
    clear_canvas()
    PlayScene_world.render()
    update_canvas()

    if Global_Object.p1hp.current_point <= 0 and Global_Object.p2.behavior_state == Global_Object.p2.IDLE:
        Global_Object.p2wp.current_point += 1
        Game_Framework.push_scene(LoseScene)
    elif Global_Object.p2hp.current_point <= 0 and Global_Object.p1.behavior_state == Global_Object.p1.IDLE:
        Global_Object.p1wp.current_point += 1
        Game_Framework.push_scene(WinScene)
    elif timer.time <= 0 and Global_Object.p2.behavior_state == Global_Object.p2.IDLE and Global_Object.p2.behavior_state == Global_Object.p2.IDLE:
        if Global_Object.p1hp.current_point > Global_Object.p2hp.current_point:
            Global_Object.p1wp.current_point += 1
            Game_Framework.push_scene(WinScene)
        elif Global_Object.p1hp.current_point < Global_Object.p2hp.current_point:
            Global_Object.p2wp.current_point += 1
            Game_Framework.push_scene(LoseScene)
        else:
            Game_Framework.push_scene(DrawScene)

def finish(): pass

def resume():
    global timer
    timer.time = 60

    if Global_Object.p1wp.current_point == 2 or Global_Object.p2wp.current_point == 2:
        Game_Framework.change_scene(WinnerScene)

def pause(): pass

#====== Input 이벤트 처리 함수 =====
def Input_Event():
    event_list = get_events()
    for event in event_list:
        if event.type == SDL_QUIT: # 창 닫기 버튼
            Game_Framework.quit()
        else:
            if Global_Object.p1hp.current_point > 0 and Global_Object.p2hp.current_point > 0:
                Global_Object.p1.handle_event(event)
                Global_Object.p2.handle_event(event)
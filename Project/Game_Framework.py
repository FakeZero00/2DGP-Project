import time
frame_time = 0.0
GRAVITY = 9.8

running = None
stack = None

def change_scene(scene):
    global stack
    if (len(stack) > 0):
        # 스택의 가장 마지막, 즉, 가장 최근의 씬의 종료 함수 실행
        stack[-1].finish()
        # 스택에서 가장 최근의 씬 제거
        stack.pop()
    stack.append(scene)
    scene.init()

def push_scene(scene):
    global stack
    if (len(stack) > 0):
        stack[-1].pause()
    stack.append(scene)
    scene.init()

def pop_mode():
    global stack
    if (len(stack) > 0):
        # 스택의 가장 마지막, 즉, 가장 최근의 씬의 종료 함수 실행
        stack[-1].finish()
        # 스택에서 가장 최근의 씬 제거
        stack.pop()

    # 이전 씬의 재개 함수 실행
    if (len(stack) > 0):
        stack[-1].resume()

def quit():
    global running
    running = False

def run(start_scene):
    global running, stack
    running = True
    stack = [start_scene]
    start_scene.init()

    global frame_time
    frame_time = 0.0
    current_time = time.time()
    while running:
        stack[-1].Input_Event()
        stack[-1].update()
        stack[-1].draw()

        frame_time = time.time() - current_time
        current_time += frame_time
        # 프레임 표시 변수
        #frame_rate = 1.0 / frame_time

    #running이 False가 되면 종료 시퀸스 작동
    while (len(stack) > 0):
        stack[-1].finish()
        stack.pop()
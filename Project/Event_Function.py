from sdl2 import *


def anim_end(behavior):
    if behavior == 'RUN': return anim_end_to_run
    elif behavior == 'BACK': return anim_end_to_back
    elif behavior == 'CROUCH': return anim_end_to_crouch
    elif behavior == 'IDLE': return anim_end_to_idle

def anim_end_to_run(e, command_buffer, input_booleans, cooltime_bool):
    return e[0] == 'ANIM_END' and input_booleans['d'] == True
def anim_end_to_back(e, command_buffer, input_booleans, cooltime_bool):
    return e[0] == 'ANIM_END' and input_booleans['a'] == True
def anim_end_to_crouch(e, command_buffer, input_booleans, cooltime_bool):
    return e[0] == 'ANIM_END' and input_booleans['s'] == True
def anim_end_to_idle(e, command_buffer, input_booleans, cooltime_bool):
    return e[0] == 'ANIM_END' and input_booleans['a'] == False and input_booleans['d'] == False and input_booleans['s'] == False

def input_check(e, input_booleans):
    if(e[0] == 'INPUT'):
        if(e[1].type == SDL_KEYDOWN):
            if e[1].key == SDLK_w:
                input_booleans['w'] = True
            elif e[1].key == SDLK_a:
                input_booleans['a'] = True
            elif e[1].key == SDLK_s:
                input_booleans['s'] = True
            elif e[1].key == SDLK_d:
                input_booleans['d'] = True
        elif(e[1].type == SDL_KEYUP):
            if e[1].key == SDLK_w:
                input_booleans['w'] = False
            elif e[1].key == SDLK_a:
                input_booleans['a'] = False
            elif e[1].key == SDLK_s:
                input_booleans['s'] = False
            elif e[1].key == SDLK_d:
                input_booleans['d'] = False

def left_down(e, command_buffer, input_booleans, cooltime_bool):
    if(e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_a and input_booleans['a'] == False):
        if (command_buffer.last_token() == 'DOWN'):
            command_buffer.add('LEFTDOWN')
        else:
            command_buffer.add('LEFT')
        input_booleans['a'] = True
        return True
def left_up(e, command_buffer, input_booleans, cooltime_bool):
    if(e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_a and input_booleans['a'] == True):
        if (command_buffer.last_token() == 'LEFTDOWN'):
            command_buffer.add('DOWN')
        else:
            command_buffer.add('IDLE')
        input_booleans['a'] = False
        return True

def right_down(e, command_buffer, input_booleans, cooltime_bool):
    if(e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_d and input_booleans['d'] == False):
        if (command_buffer.last_token() == 'DOWN'):
            command_buffer.add('RIGHTDOWN')
        else:
            command_buffer.add('RIGHT')
        input_booleans['d'] = True
        return True
def right_up(e, command_buffer, input_booleans, cooltime_bool):
    if(e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_d and input_booleans['d'] == True):
        if(command_buffer.last_token() == 'RIGHTDOWN'):
            command_buffer.add('DOWN')
        else:
            command_buffer.add('IDLE')
        input_booleans['d'] = False
        return True

def down_down(e, command_buffer, input_booleans, cooltime_bool):
    if(e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_s and input_booleans['s'] == False):
        if (command_buffer.last_token() == 'RIGHT'):
            command_buffer.add('RIGHTDOWN')
        elif (command_buffer.last_token() == 'LEFT'):
            command_buffer.add('LEFTDOWN')
        else:
            command_buffer.add('DOWN')
        input_booleans['s'] = True
        return True
def down_up(e, command_buffer, input_booleans, cooltime_bool):
    if(e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_s and input_booleans['s'] == True):
        if(command_buffer.last_token() == 'RIGHTDOWN'):
            command_buffer.add('RIGHT')
        elif(command_buffer.last_token() == 'LEFTDOWN'):
            command_buffer.add('LEFT')
        else:
            command_buffer.add('IDLE')
        input_booleans['s'] = False
        return True

def attack_down(e, command_buffer, input_booleans = None, cooltime_bool = None):
    if(e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_j):
        if cooltime_bool:
            command_buffer.add('ATTACK')
            return True
def attack_up(e, command_buffer = None, input_booleans = None, cooltime_bool = None):
    if(e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_j):
        return True
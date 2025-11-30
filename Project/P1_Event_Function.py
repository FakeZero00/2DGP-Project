from sdl2 import *


def anim_end(behavior):
    if behavior == 'RUN': return anim_end_to_run
    elif behavior == 'BACK': return anim_end_to_back
    elif behavior == 'CROUCH': return anim_end_to_crouch
    elif behavior == 'IDLE': return anim_end_to_idle

#object_state = (command_buffer, input_booleans, self.cooltime_bool, self.jump_bool)

def anim_end_to_run(e, object_state):
    return e[0] == 'ANIM_END' and object_state[1]['d'] == True
def anim_end_to_back(e, object_state):
    return e[0] == 'ANIM_END' and object_state[1]['a'] == True
def anim_end_to_crouch(e, object_state):
    return e[0] == 'ANIM_END' and object_state[1]['s'] == True
def anim_end_to_idle(e, object_state):
    return e[0] == 'ANIM_END' and object_state[1]['a'] == False and object_state[1]['d'] == False and object_state[1]['s'] == False

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

def left_down(e, object_state):
    if(e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_a and object_state[1]['a'] == False):
        if (object_state[0].last_token() == 'DOWN'):
            object_state[0].add('LEFTDOWN')
        else:
            object_state[0].add('LEFT')
        object_state[1]['a'] = True
        return True
def left_up(e, object_state):
    if(e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_a and object_state[1]['a'] == True):
        if (object_state[0].last_token() == 'LEFTDOWN'):
            object_state[0].add('DOWN')
        else:
            object_state[0].add('IDLE')
        object_state[1]['a'] = False
        return True

def right_down(e, object_state):
    if(e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_d and object_state[1]['d'] == False):
        if (object_state[0].last_token() == 'DOWN'):
            object_state[0].add('RIGHTDOWN')
        elif (object_state[0].last_token() == 'UP'):
            object_state[0].add('RIGHTUP')
        else:
            object_state[0].add('RIGHT')
        object_state[1]['d'] = True
        return True
def right_up(e, object_state):
    if(e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_d and object_state[1]['d'] == True):
        if(object_state[0].last_token() == 'RIGHTDOWN'):
            object_state[0].add('DOWN')
        elif (object_state[0].last_token() == 'RIGHTUP'):
            object_state[0].add('UP')
        else:
            object_state[0].add('IDLE')
        object_state[1]['d'] = False
        return True

def up_down(e, object_state):
    if(e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_w and object_state[1]['w'] == False and object_state[3] == False):
        if (object_state[0].last_token() == 'RIGHT'):
            object_state[0].add('RIGHTUP')
        elif (object_state[0].last_token() == 'LEFT'):
            object_state[0].add('LEFTUP')
        else:
            object_state[0].add('UP')
        object_state[1]['w'] = True
        return True

def up_up(e, object_state):
    if(e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_w and object_state[1]['w'] == True):
        if(object_state[0].last_token() == 'RIGHTUP'):
            object_state[0].add('RIGHT')
        elif(object_state[0].last_token() == 'LEFTUP'):
            object_state[0].add('LEFT')
        else:
            object_state[0].add('IDLE')
        object_state[1]['w'] = False
        return True

def down_down(e, object_state):
    if(e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_s and object_state[1]['s'] == False and object_state[3] == False):
        if (object_state[0].last_token() == 'RIGHT'):
            object_state[0].add('RIGHTDOWN')
        elif (object_state[0].last_token() == 'LEFT'):
            object_state[0].add('LEFTDOWN')
        else:
            object_state[0].add('DOWN')
        object_state[1]['s'] = True
        return True

def down_up(e, object_state):
    if(e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_s and object_state[1]['s'] == True):
        if(object_state[0].last_token() == 'RIGHTDOWN'):
            object_state[0].add('RIGHT')
        elif(object_state[0].last_token() == 'LEFTDOWN'):
            object_state[0].add('LEFT')
        else:
            object_state[0].add('IDLE')
        object_state[1]['s'] = False
        return True

def attack_down(e, object_state):
    if(e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_j):
        if object_state[2]:
            object_state[0].add('ATTACK')
            return True
def attack_up(e, object_state):
    if(e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_j):
        return True
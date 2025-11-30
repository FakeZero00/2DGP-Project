from sdl2 import *


def anim_end(behavior):
    if behavior == 'RUN': return anim_end_to_run
    elif behavior == 'BACK': return anim_end_to_back
    elif behavior == 'CROUCH': return anim_end_to_crouch
    elif behavior == 'IDLE': return anim_end_to_idle

#object_state = (command_buffer, input_booleans, self.cooltime_bool, self.jump_bool)

def anim_end_to_run(e, object_state):
    return e[0] == 'ANIM_END' and object_state[1]['RIGHT'] == True
def anim_end_to_back(e, object_state):
    return e[0] == 'ANIM_END' and object_state[1]['LEFT'] == True
def anim_end_to_crouch(e, object_state):
    return e[0] == 'ANIM_END' and object_state[1]['DOWN'] == True
def anim_end_to_idle(e, object_state):
    return e[0] == 'ANIM_END' and object_state[1]['LEFT'] == False and object_state[1]['RIGHT'] == False and object_state[1]['DOWN'] == False

def input_check(e, input_booleans):
    if(e[0] == 'INPUT'):
        if(e[1].type == SDL_KEYDOWN):
            if e[1].key == SDLK_UP:
                input_booleans['UP'] = True
            elif e[1].key == SDLK_LEFT:
                input_booleans['LEFT'] = True
            elif e[1].key == SDLK_DOWN:
                input_booleans['DOWN'] = True
            elif e[1].key == SDLK_RIGHT:
                input_booleans['RIGHT'] = True
        elif(e[1].type == SDL_KEYUP):
            if e[1].key == SDLK_UP:
                input_booleans['UP'] = False
            elif e[1].key == SDLK_LEFT:
                input_booleans['LEFT'] = False
            elif e[1].key == SDLK_DOWN:
                input_booleans['DOWN'] = False
            elif e[1].key == SDLK_RIGHT:
                input_booleans['RIGHT'] = False

def left_down(e, object_state):
    if(e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_LEFT and object_state[1]['LEFT'] == False):
        if (object_state[0].last_token() == 'DOWN'):
            object_state[0].add('LEFTDOWN')
        else:
            object_state[0].add('LEFT')
        object_state[1]['LEFT'] = True
        return True
def left_up(e, object_state):
    if(e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_LEFT and object_state[1]['LEFT'] == True):
        if (object_state[0].last_token() == 'LEFTDOWN'):
            object_state[0].add('DOWN')
        else:
            object_state[0].add('IDLE')
        object_state[1]['LEFT'] = False
        return True

def right_down(e, object_state):
    if(e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_RIGHT and object_state[1]['RIGHT'] == False):
        if (object_state[0].last_token() == 'DOWN'):
            object_state[0].add('RIGHTDOWN')
        elif (object_state[0].last_token() == 'UP'):
            object_state[0].add('RIGHTUP')
        else:
            object_state[0].add('RIGHT')
        object_state[1]['RIGHT'] = True
        return True
def right_up(e, object_state):
    if(e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_RIGHT and object_state[1]['RIGHT'] == True):
        if(object_state[0].last_token() == 'RIGHTDOWN'):
            object_state[0].add('DOWN')
        elif (object_state[0].last_token() == 'RIGHTUP'):
            object_state[0].add('UP')
        else:
            object_state[0].add('IDLE')
        object_state[1]['RIGHT'] = False
        return True

def up_down(e, object_state):
    if(e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_UP and object_state[1]['UP'] == False and object_state[3] == False):
        if (object_state[0].last_token() == 'RIGHT'):
            object_state[0].add('RIGHTUP')
        elif (object_state[0].last_token() == 'LEFT'):
            object_state[0].add('LEFTUP')
        else:
            object_state[0].add('UP')
        object_state[1]['UP'] = True
        return True

def up_up(e, object_state):
    if(e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_UP and object_state[1]['UP'] == True):
        if(object_state[0].last_token() == 'RIGHTUP'):
            object_state[0].add('RIGHT')
        elif(object_state[0].last_token() == 'LEFTUP'):
            object_state[0].add('LEFT')
        else:
            object_state[0].add('IDLE')
        object_state[1]['UP'] = False
        return True

def down_down(e, object_state):
    if(e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_DOWN and object_state[1]['DOWN'] == False and object_state[3] == False):
        if (object_state[0].last_token() == 'RIGHT'):
            object_state[0].add('RIGHTDOWN')
        elif (object_state[0].last_token() == 'LEFT'):
            object_state[0].add('LEFTDOWN')
        else:
            object_state[0].add('DOWN')
        object_state[1]['DOWN'] = True
        return True

def down_up(e, object_state):
    if(e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_DOWN and object_state[1]['DOWN'] == True):
        if(object_state[0].last_token() == 'RIGHTDOWN'):
            object_state[0].add('RIGHT')
        elif(object_state[0].last_token() == 'LEFTDOWN'):
            object_state[0].add('LEFT')
        else:
            object_state[0].add('IDLE')
        object_state[1]['DOWN'] = False
        return True

def attack_down(e, object_state):
    if(e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_KP_4):
        if object_state[2]:
            object_state[0].add('ATTACK')
            return True
def attack_up(e, object_state):
    if(e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_KP_4):
        return True
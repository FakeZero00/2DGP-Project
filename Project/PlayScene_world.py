# 0번 레이어: 배경 레이어, 1번 레이어: 기본 레이어
world = [[], []]

def add_object(o, depth = 1):
    world[depth].append(o)

def add_objects(ol, depth = 1):
    world[depth] += ol

def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o)
            return
    raise ValueError('Cannot find object in world')

def update():
    for layer in world:
        for o in layer:
            o.update()

def render():
    for layer in world:
        for o in layer:
            o.draw()
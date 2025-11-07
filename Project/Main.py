from pico2d import *
import PlayScene
from Project.Gaogaigar import command_buffer

open_canvas(1600, 900)

PlayScene.init()

while PlayScene.Running:
    PlayScene.Input_Event()
    PlayScene.update()
    PlayScene.draw()
    print(command_buffer.tokens())
    delay(1 / 20)

close_canvas()
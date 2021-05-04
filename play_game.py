import time
from color_lib import Color_Lib
import keyboard
import mouse
from game_state import GameState
from action_system import ActionSystem
from actions import Actions
import random


def Play_Game():
    gs = GameState()
    while True:
        gs.update()
        time.sleep(1)
        if gs.get_fountain_coords() is not None:
            Actions.retreat(gs.get_fountain_coords())
               
Play_Game()

    
    
    

    
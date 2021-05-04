import time
from color_lib import Color_Lib
import keyboard
import mouse
from game_state import GameState
from action_system import ActionSystem
import random


def Play_Game():
    gs = GameState()

    while True:
        gs.update()
        gs.debug_print()
        time.sleep(1)
        
Play_Game()
    
    
    

    
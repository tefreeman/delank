from client import Client
from game.play_game import PlayGame
from input import Mouse
import keyboard
import time



stop_flag = {'val': False}

def set_stop_flag():
    stop_flag['val'] = not stop_flag['val']
    
    
keyboard.add_hotkey('ctrl+s', set_stop_flag, suppress=bool)

Mouse()
Client()




while True:
    Client.get_into_game("sup", "mid", "yuumi", 20)
    PlayGame(stop_flag)
    time.sleep(5)
    Client.force_close_league()
    time.sleep(30)
 
from client import Client
from game.play_game import PlayGame
from input import Mouse
import keyboard
import time
from configs import Configs


stop_flag = {'val': False}
attach_target = {'val': 'f4'}

def set_stop_flag():
    stop_flag['val'] = not stop_flag['val']

def set_attach_target(key):
    attach_target['val'] = key
    
keyboard.add_hotkey('ctrl+s', set_stop_flag, suppress=bool)
keyboard.add_hotkey('ctrl+f1',set_attach_target, args=('f1'))
keyboard.add_hotkey('ctrl+f1',set_attach_target, args=('f2'))
keyboard.add_hotkey('ctrl+f1',set_attach_target, args=('f3'))
keyboard.add_hotkey('ctrl+f1',set_attach_target, args=('f4'))

Mouse()
Client()



while True:
    Client.get_into_game("sup", "mid", "yuumi", 20)
    time.sleep(5)
    PlayGame(stop_flag, attach_target)
    time.sleep(5)
    Client.force_close_league()
    time.sleep(10)
    #Configs.restore_configs()
    time.sleep(15)
 
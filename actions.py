from game_coords import GameCoords
from coords import Coords
from utility import Utility
import keyboard
import time
import mouse

class Actions:
    def __init__(self):
        pass
    
    @staticmethod
    def yummi_attach(key='f4'):
        keyboard.press(key)
        mouse.move(GameCoords.ally_focus_center.x, GameCoords.ally_focus_center.y)
        time.sleep(0.05)
        
        keyboard.press_and_release('w')
        
        time.sleep(0.5)
        
        keyboard.press_and_release('w')
        
        time.sleep(0.25)
        
        keyboard.release(key)
    
    @staticmethod   
    def cast_spell(key):
        keyboard.press_and_release(key)
    @staticmethod
    def camera_lock():
        keyboard.press_and_release('y')
    @staticmethod    
    def purchase_recommend():
        keyboard.press_and_release('p')
        mouse.move(GameCoords.shop_select_recommend.x, GameCoords.shop_select_recommend.y)
        time.sleep(0.25)
        Utility.left_click()
        time.sleep(0.25)
        mouse.move(GameCoords.shop_purchase_selected.x, GameCoords.shop_purchase_selected.y)
        time.sleep(0.25)
        Utility.left_click()
        time.sleep(0.25)
        keyboard.press_and_release('p')
        time.sleep(0.25)
    
    @staticmethod   
    def type_in_chat(msg: str):
        keyboard.press_and_release('enter')
        time.sleep(0.25)
        keyboard.write(msg, 0.01)
        keyboard.press_and_release('enter')
        time.sleep(0.1)
        
    
    @staticmethod
    def retreat(coord: Coords):
        mouse.move(coord.x, coord.y)
        time.sleep(0.1)
        Utility.left_click()
        time.sleep(0.05)
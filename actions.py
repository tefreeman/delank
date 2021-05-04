from game_coords import GameCoords
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
        
    def cast_spell(key):
        keyboard.press_and_release(key)
    
    def camera_lock():
        keyboard.press_and_release('y')
        
    def purchase_recommend():
        keyboard.press_and_release('p')
        mouse.move(GameCoords.shop_select_recommend.x, GameCoords.shop_select_recommend.y)
        time.sleep(0.25)
        Utility.click()
        time.sleep(0.25)
        mouse.move(GameCoords.shop_purchase_selected.x, GameCoords.shop_purchase_selected.y)
        time.sleep(0.25)
        Utility.click()
        time.sleep(0.25)
        keyboard.press_and_release('p')
        time.sleep(0.25)
        
    def type_in_chat(msg: str):
        keyboard.press_and_release('enter')
        time.sleep(0.25)
        keyboard.write(msg, 0.01)
        keyboard.press_and_release('enter')
        time.sleep(0.1)
        
        
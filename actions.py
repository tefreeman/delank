from game_coords import GameCoords
from coords import Coords
from utility import Utility
import keyboard
import time
import mouse
import random

class Actions:
    def __init__(self):
        pass
    
    _rand_messages = ["...", "D:","shit", "my b", "i suck", "come on now", "yummi sucks so much sometimes", "sorry im kinda new", "god damn", "we got wrecked", "jesus", "yeah prob gg", "im not toxic, but i feel toxic rn", "ugh, plz come on", "I can't do this anymore", "I need to find a new game", "lmao", "come on ur gotta be the adc", "I can't carry this!", "lordy", "gg", "this is no fun", "/all get good", "/all ez gg", "i don't like to get off, soz", "dang I gotta do better", "u gotta play safer", "plz play safer", "don't play aggro", "play passive", "u having fun?", "this sucks", "yummi always gets wrecked in lane", "i need to find a new game", "we aren't carrying bot lane that's for sure", "maybe i need to learn a new champ", "ughhhhhhh", "plz no", "I don't think we can win this lane", "yummi is a strong LATE game champ", "zzzz"]
    last_attach = 0
    
    @staticmethod
    def yummi_attach(key='f4'):
        
        if Actions.last_attach + 8 < time.time():
            keyboard.press(key)
            mouse.move(GameCoords.ally_focus_center.x, GameCoords.ally_focus_center.y)
            time.sleep(0.05)
            
            keyboard.press_and_release('w')
            
            time.sleep(0.5)
            
            keyboard.press_and_release('w')
            
            time.sleep(0.25)
            
            keyboard.release(key)
            
            Actions.last_attach = time.time()
    
    @staticmethod   
    def cast_spell(key):
        keyboard.press_and_release(key)
        
    @staticmethod
    def level_all_spells(s1, s2, s3, s4):
        keyboard.press_and_release('ctrl+' + s1)
        time.sleep(0.01)
        keyboard.press_and_release('ctrl+' + s2)
        time.sleep(0.01)
        keyboard.press_and_release('ctrl+' + s3)
        time.sleep(0.01)
        keyboard.press_and_release('ctrl+' + s4)
        time.sleep(0.01)
        
    @staticmethod
    def camera_lock():
        keyboard.press_and_release('y')
    
    @staticmethod    
    def purchase_recommend():
        keyboard.press_and_release('p')
        mouse.move(GameCoords.shop_tab_recommend.x, GameCoords.shop_tab_recommend.y)
        time.sleep(0.25)
        Utility.left_click()
        time.sleep(0.25)
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
    def type_shit_in_chat():
        num = random.randint(0, len(Actions._rand_messages)-1)
        Actions.type_in_chat(Actions._rand_messages[num])
        
    @staticmethod
    def retreat(coord: Coords):
        mouse.move(coord.x, coord.y)
        time.sleep(0.1)
        Utility.left_click()
        time.sleep(0.05)
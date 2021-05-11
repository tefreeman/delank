from game.game_coords import GameCoords
from coords import Coords
from utility import Utility
from input import Mouse
from game.game_elements import GameElements
import keyboard
import time
import mouse
import random

class Actions:
    def __init__(self):
        pass
    
    _rand_messages = ["...", "D:","shit", "my b", "i suck", "come on now", "yummi sucks so much sometimes", "sorry im kinda new", "god damn", "we got wrecked", "jesus", "yeah prob gg", "im not toxic, but i feel toxic rn", "ugh, plz come on", "I can't do this anymore", "I need to find a new game", "lmao", "come on ur gotta be the adc", "I can't carry this!", "lordy", "gg", "this is no fun", "/all get good", "/all ez gg", "i don't like to get off, soz", "dang I gotta do better", "u gotta play safer", "plz play safer", "don't play aggro", "play passive", "u having fun?", "this sucks", "yummi always gets wrecked in lane", "i need to find a new game", "we aren't carrying bot lane that's for sure", "maybe i need to learn a new champ", "ughhhhhhh", "plz no", "I don't think we can win this lane", "yummi is a strong LATE game champ", "zzzz"]
    _cast_cds = {
        'q': {'wait_time': 0, 'cd': 2},
        'e': {'wait_time': 0, 'cd': 2},
        'r': {'wait_time': 0, 'cd': 10}
    }
    last_attach = 0
    
    @staticmethod
    def yummi_attach(key='f4'):
        
        if Actions.last_attach + 8 < time.time():
            keyboard.press(key)
            Mouse.move((GameCoords.ally_focus_center.x, GameCoords.ally_focus_center.y), 0.05)
            time.sleep(0.160)
            
            keyboard.press_and_release('w')
            
            time.sleep(0.5)
            
            keyboard.press_and_release('w')
            
            time.sleep(0.25)
            
            keyboard.release(key)
            
            Actions.last_attach = time.time()
    
    @staticmethod   
    def cast_spell(key):
        if key in Actions._cast_cds:
            if time.time() > Actions._cast_cds[key]['wait_time']:
                keyboard.press_and_release(key)
                Actions._cast_cds[key]['wait_time'] = time.time() + Actions._cast_cds[key]['cd']
        else:
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
        Mouse.move((GameCoords.shop_tab_recommend.x, GameCoords.shop_tab_recommend.y))
        time.sleep(1)
        Mouse.click()
        time.sleep(0.5)
        Mouse.move((GameCoords.shop_select_recommend.x, GameCoords.shop_select_recommend.y))
        time.sleep(1)
        Mouse.click()
        time.sleep(0.5)
        Mouse.move((GameCoords.shop_purchase_selected.x, GameCoords.shop_purchase_selected.y))
        time.sleep(1.5)
        Mouse.click()
        time.sleep(1)
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
    def random_mouse_movement():
        x = random.randint(200, 1000)
        y = random.randint(100, 620)
        
        Mouse.move((x,y), duration=0.1, resolution= 10.0)
        
    
    @staticmethod
    def try_buy_item(item_str: str):
        keyboard.press_and_release('p')
        time.sleep(0.50)
        keyboard.press_and_release('ctrl+l')
        time.sleep(0.50)
        keyboard.write(item_str, 0.01)
        time.sleep(0.30)
        GameElements.item_result_pos.click()
        time.sleep(0.30)
        
        result = GameElements.item_buy_button_pos.is_detected()
        
        if result == True:
            GameElements.item_buy_button_pos.click()
            time.sleep(0.30)
        
        keyboard.press_and_release('p')
        return result
            
        
        
        
        
    @staticmethod
    def retreat(coord: Coords):
        Mouse.move((coord.x, coord.y), 0.15, 8.0)
        time.sleep(0.40)
        Mouse.click()
        Actions.cast_spell('e')
        time.sleep(0.60)
        Utility.right_click()
        count = 0
        
        while count < 10:
            Actions.cast_spell('e')
            time.sleep(1)
            count += 1
        
        Actions.cast_spell('b')
        
        time.sleep(11)
        
        Actions.purchase_recommend()
        
        
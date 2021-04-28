import time
from color_lib import Color_Lib
import keyboard
import mouse

class GameReader():
    is_game_started_coord = {'coords': (451, 692), 'img': 'game_started.png'}
    shop_buy_reccommend_coord = {'coords': (245, 305), "img": "shop_open.png"}
    champ_loc_screen_coord = {'coords': (640, 340), "img": ""}
    troll_start_coord = {'coords': (140, 631), "img": ""}
    yummi_is_attached_coord = {'coords': (590, 200), "height": 40, "color": (99, 93, 222)}
    def __init__(self, img_path):
        self.img_path = img_path
        
    def wait_for_game_start(self):
        while True:
            
            if Color_Lib.match_color_screen_img(GameReader.is_game_started_coord["coords"], self.img_path + GameReader.is_game_started_coord["img"] ):
                print("game_started!")
                break
            
            time.sleep(1)

    def buy_items(self): 
        keyboard.press_and_release('p')
        mouse.move(GameReader.shop_buy_reccommend_coord["coords"][0], GameReader.shop_buy_reccommend_coord["coords"][1])
        time.sleep(1)
        mouse.click()
        time.sleep(0.05)
        mouse.click()
        time.sleep(1)
        keyboard.press_and_release('p')
        time.sleep(1)
    
    def is_yummi_attached(self):
        return Color_Lib.is_color_in_vline_on_screen(GameReader.yummi_is_attached_coord["coords"], GameReader.yummi_is_attached_coord["height"], GameReader.yummi_is_attached_coord["color"], 10, -10)
    
    def start_game_troll(self):
        mouse.move(GameReader.troll_start_coord["coords"][0], GameReader.troll_start_coord["coords"][1])
        time.sleep(0.5)
        mouse.click()
        
        time.sleep(20)
        mouse.move(GameReader.champ_loc_screen_coord["coords"][0],GameReader.champ_loc_screen_coord["coords"][1])
        time.sleep(0.5)
        keyboard.press_and_release('4')
        
        time.sleep(0.5)
        keyboard.press_and_release('b')
        
        
    def attach(self, target: str):
        tar_key = ""
        if target == "top":
            tar_key = "f1"
        elif target == "jg":
            tar_key = "f2"
        elif target == "mid":
            tar_key = "f3"
        elif target == "adc":
            tar_key = "f4"
        
        keyboard.press(tar_key)
        mouse.move(GameReader.champ_loc_screen_coord["coords"][0],GameReader.champ_loc_screen_coord["coords"][1])
        time.sleep(0.5)
        keyboard.press_and_release('w')
        time.sleep(0.5)
        keyboard.release(tar_key)

def Play_Game(gameReader: GameReader):
    
    while True:
        print(gameReader.is_yummi_attached())
        time.sleep(1)
    gameReader.wait_for_game_start()
    
    gameReader.buy_items()
    
    gameReader.start_game_troll()

gr = GameReader("C:\\Users\\Trevor\\Documents\\delank\\images\\")

Play_Game(gr)
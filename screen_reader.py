  
from mss import mss
from PIL import Image
from threading import Thread
from color_lib import Color_Lib
from game_state import GameState
import time

class ScreenReader(Thread):
    def __init__(self, game_state, fps):
        Thread.__init__(self)
        self.game_state = game_state
        self.sleep_time = 1.0/fps
        self.running = True
        
    def run(self):
        # Capture entire screen
        with mss() as sct:
            monitor = sct.monitors[1]
            # mon = {"top": 800, "left": 0, "width": 280, "height": 280}
            while self.running is True:
                sct_img = sct.grab(monitor)
                img = Image.frombytes('RGB', sct_img.size, sct_img.bgra, 'raw', 'BGRX')
                self.game_state.update(img)
                print('fire')
                time.sleep(self.sleep_time)


        
    def stop(self):
        self.running = False
  
from mss import mss
from PIL import Image
from threading import Thread
from color_lib import Color_Lib
import time

class ScreenReader(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.running = True
        
    def run(self):
        # Capture entire screen
        with mss() as sct:
            monitor = sct.monitors[1]
            # mon = {"top": 800, "left": 0, "width": 280, "height": 280}
            while self.running:
                sct_img = sct.grab(monitor)
                img = Image.frombytes('RGB', sct_img.size, sct_img.bgra, 'raw', 'BGRX')
                Color_Lib.update_screen()
                time.sleep(0.05)


        
    def stop(self):
        self.running = False
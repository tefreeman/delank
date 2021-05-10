import random
from input import Mouse
from color_lib import ColorLib
from utility import Utility
import time
import os
from win32api import GetSystemMetrics
class Detection:
    main_dir = os.path.dirname(__file__)
    img_path = os.path.join(main_dir, "images\\")
    
    def __init__(self, x, y, img: str):
        self.pt = (x,y)
        self.img = Detection.img_path + img
    
    
    def is_detected(self):
        raise NotImplementedError("Must override methodB")
    
    def wait_for_detection(self, fps = 1, max_wait=0):
        sleep_time = 1/fps
        if max_wait != 0:
            count = 0
            while count < max_wait:
                if self.is_detected():
                    break
                count += 1
                time.sleep(sleep_time)
        else:
            while True:
                if self.is_detected():
                    break
                time.sleep(sleep_time)
    
    
class PointDetection(Detection):
    def __init__(self, x, y, img):
        Detection.__init__(self, x, y, img)

    def is_detected(self):
        return ColorLib.match_color_screen_img(self.pt, self.img)
    
        
class Element:
    margin = 2
    
    def __init__(self, pt: tuple, detection: Detection = None):
        self.pt = pt
        
        if detection is not None:
            self._detection = detection
        else:
            self._detection = Detection(0,0, "")
        
    
    def get_random_pt_on(self):
        raise NotImplementedError("Must override get_random_pt")
    
    def get_random_pt_off(self):
        raise NotImplementedError("Must override get_random_pt")
    
    def is_mouse_over(self):
        raise NotImplementedError("Must override get_random_pt")
    
    def move_mouse_off(self):
        raise NotImplementedError("Must override get_random_pt")
    def click(self, timeout=10):
        
        result = False
        
        while not result:
            
            pt = self.get_random_pt_on()
        
            Mouse.move(pt)
        
            result = self.wait_till_reached(pt, timeout)

        
        Mouse.click()

    
    def wait_till_reached(self, pt, timeout):
        pos = Mouse.get_cursor_pos()
        
        max_time = Utility.TimestampMillisec64() + timeout * 1000
        
        in_accuracy = abs(pos[0] - pt[0]) + abs(pos[1] - pt[1])
        
        while in_accuracy > 4:
            time.sleep(0.05)
            pos = Mouse.get_cursor_pos()
            
            if Utility.TimestampMillisec64() > max_time:
                return False
            
            in_accuracy = abs(pos[0] - pt[0]) + abs(pos[1] - pt[1])
            

        return True
    
    
    def wait_till_detected(self, fps, max_wait):
        return self._detection.wait_for_detection(fps, max_wait)
    
    
    def is_detected(self):
        if self.is_mouse_over():
            self.move_mouse_off()
            time.sleep(0.25)
        return self._detection.is_detected()
    

class Box(Element):

    def __init__(self, pt, w, h, detection=None):
        Element.__init__(self, pt, detection)
        self.w = w
        self.h = h
        
    def get_random_pt_on(self):
        x = random.randint(self.pt[0] + Element.margin, self.pt[0] + self.w - Element.margin)
        y = random.randint(self.pt[1] + Element.margin, self.pt[1] + self.h - Element.margin)   
        return x,y

    def get_random_pt_off(self):
        mid_x = self.pt[0] + int(self.w/2)
        mid_y = self.pt[1] + int(self.h/2)
        
        screen_w = GetSystemMetrics(0)
        screen_h = GetSystemMetrics(1)
        
        #left side
        x = 0
        y = 0
        
        if screen_w - mid_x > screen_w/2:
            x = random.randint(self.pt[0] + self.w + self.margin, screen_w)
        else: 
            x = random.randint(0, self.pt[0] - self.margin)

        
        if screen_h - mid_y > screen_h/2:
            y = random.randint(self.pt[1] + self.margin, screen_h)
        else:
            y = random.randint(0, self.pt[1] - self.margin)
            
        return x,y
        
    
    def move_mouse_off(self, timeout=10):
        result = False
        
        while not result:
            
            pt = self.get_random_pt_off()
        
            Mouse.move(pt)
        
            result = self.wait_till_reached(pt, timeout)
        

    def is_mouse_over(self):
        c_pos = Mouse.get_cursor_pos()
        
        return c_pos[0] >= self.pt[0] - self.margin and c_pos[0] < self.pt[0] + self.w + self.margin\
        and c_pos[1] >= self.pt[1] - self.margin and c_pos[1] < self.pt[1] + self.h + self.margin

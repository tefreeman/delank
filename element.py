import random
from input import Mouse
import time

class Detection:
    def __init__(self, pt: tuple, img: str):
        self.pt = pt,
        self.img = img
    
    
    def is_detected():
        pass
    
class Point_Detection(Detection):
    def __init__(self, pt, img):
        Detection.__init__(self, pt, img)

    def is_detected():
        return  None#Color_Lib.match_color_screen_img(Detection.pt, Detection.img)
        
class Element:
    margin = 2
    
    def __init__(self, pt: tuple):
        self.pt = pt
        
    
    def get_random_pt(self):
        pass
    
    def click(self):
        pt = self.get_random_pt()
        Mouse.move(self.pt, 0.5, 4.0)
        Mouse.click()
    
    

class Box(Element):

    def __init__(self, pt, w, h):
        Element.__init__(self, pt)
        self.w = w
        self.h = h
        
    def get_random_pt(self):
        x = random.randint(self.pt[0] + Element.margin, self.pt[0] + self.w - Element.margin)
        y = random.randint(self.pt[1] + Element.margin, self.pt[1] + self.h - Element.margin)   
        return x,y
    
Mouse()
time.sleep(1)
test = Box((100, 100), 50, 50)
test.click()

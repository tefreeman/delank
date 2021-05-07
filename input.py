import win32api, win32con
import win32gui
from random import randint, choice
import threading, queue
from time import sleep
import pyautogui
import random
import numpy as np
import time
from scipy import interpolate
import math


class Mouse:
    _q = queue.LifoQueue()
    
    SCREEN_WIDTH = win32api.GetSystemMetrics(0)
    SCREEN_HEIGHT = win32api.GetSystemMetrics(1)
    
    t = None
    
    def __init__(self):
        Mouse.t = threading.Thread(target=Mouse._worker, daemon=False)
        Mouse.t.start()
        
    
    @staticmethod
    def _worker():
        while True:
            item = Mouse._q.get()
            if item is not None:
                if item[0] is "move":
                    ms = time.time_ns() // 1_000_000 
                    print(time.time())
                    Mouse._curved_move(item[1], item[2], item[3])
                    print((time.time_ns() // 1_000_000) - ms)
            Mouse._q.task_done()
            time.sleep(0.01)
    
    @staticmethod
    def _left_click(wait = 0):
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        sleep(wait)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    
    @staticmethod
    def _right_click(wait = 0):
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
        sleep(wait)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)

    @staticmethod
    def _click(button):
        
        wait_time = randint(43, 113) / 1000
        
        if button == "left":
            Mouse._left_click(wait_time)
        elif button == "right":
            Mouse._right_click(wait_time)
    

    @staticmethod
    def click(button="left"):
        Mouse._q.put(Mouse._click(button))

    @staticmethod
    def _move(pt):
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE | win32con.MOUSEEVENTF_ABSOLUTE, int(pt[0]/Mouse.SCREEN_WIDTH*65535.0), int(pt[1]/Mouse.SCREEN_HEIGHT*65535.0))
    
    @staticmethod
    def move(pt, duration = 0.5, resolution = 8.0):
        Mouse._q.put(("move", pt, duration, resolution))
         
    @staticmethod
    def _point_dist(x1,y1,x2,y2):
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    
    @staticmethod
    def _curved_move(pt, duration, resolution):
        
            # Any duration less than this is rounded to 0.0 to instantly move the mouse.
        pyautogui.MINIMUM_DURATION = 0  # Default: 0.1
        # Minimal number of seconds to sleep between mouse moves.
        pyautogui.MINIMUM_SLEEP = 0  # Default: 0.05
        # The number of seconds to pause after EVERY public function call.
        pyautogui.PAUSE = 0  # Default: 0.1
        cp = random.randint(3, 5)  # Number of control points. Must be at least 2.
        flags, hcursor, (x1,y1) = win32gui.GetCursorInfo()
        x2, y2 = pt
        
        # Distribute control points between start and destination evenly.
        x = np.linspace(x1, x2, num=cp, dtype='int')
        y = np.linspace(y1, y2, num=cp, dtype='int')

        # Randomise inner points a bit (+-RND at most).
        RND = 10
        xr = [random.randint(-RND, RND) for k in range(cp)]
        yr = [random.randint(-RND, RND) for k in range(cp)]
        xr[0] = yr[0] = xr[-1] = yr[-1] = 0
        x += xr
        y += yr

        # Approximate using Bezier spline.
        degree = 3 if cp > 3 else cp - 1  # Degree of b-spline. 3 is recommended.
                                        # Must be less than number of control points.
        tck, u = interpolate.splprep([x, y], k=degree)
        
        # Move upto a certain number of points
        u = np.linspace(0, 1, num=2+int(Mouse._point_dist(x1,y1,x2,y2)/ resolution))
        
        points = interpolate.splev(u, tck)

        # Move mouse.
        timeout = duration / len(points[0])
        point_list=zip(*(i.astype(int) for i in points))
        
        for point in point_list:
            Mouse._move(point)
            time.sleep(timeout)
          




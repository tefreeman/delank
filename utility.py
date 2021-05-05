import win32api, win32con
import time

class Utility:
    _arrays = {'Yummi_set_attached': [False, False, False], 'Player_set_is_dead': [False, False, False, False, False, False, False, False, False, False]}
    
    @staticmethod
    def denoised_bool(status, arr_name):
        Utility._arrays[arr_name].append(status)
        Utility._arrays[arr_name].pop(0)
        
        f_count = 0
        t_count = 0
        
        for i in Utility._arrays[arr_name]:
            if i is True:
                t_count += 1
            else:
                f_count += 1
        
        return t_count > f_count
        
        
    @staticmethod
    def left_click():
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        time.sleep(.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

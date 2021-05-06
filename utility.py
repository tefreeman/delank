import win32api, win32con
from client import Client
import time
import shutil
import os

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
        
    @staticmethod
    def right_click():
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
        time.sleep(.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)

    @staticmethod
    def save_replace_configs():
        new_config_dir = Client.main_dir + '\\league_configs\\new\\'
        saved_config_dir = Client.main_dir + '\\league_configs\\saved\\'
        l_config_dir = "C:\\Riot Games\\League of Legends\\Config\\"


        new_game_cfg = new_config_dir + "game.cfg"
        new_input_ini = new_config_dir + "input.ini"

        l_game_cfg = l_config_dir + "game.cfg"
        l_input_ini = l_config_dir + "input.ini"
        
        if os.path.exists(l_game_cfg):
            shutil.copy2(l_game_cfg, saved_config_dir)
            os.remove(l_game_cfg)
        
        if os.path.exists(l_input_ini):
            shutil.copy2(l_input_ini, saved_config_dir)
            os.remove(l_input_ini)
        

Utility.save_replace_configs()



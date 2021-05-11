from color_lib import ColorLib
from coords import Coords
import psutil
import subprocess
import time
import mouse
import keyboard
import os
from win32.win32gui import GetForegroundWindow, GetWindowRect, MoveWindow, IsWindowVisible ,GetWindowText, EnumWindows, FindWindow, SetForegroundWindow
from win32.win32process import GetWindowThreadProcessId
from element import Box, PointDetection
from configs import Configs


class Client():
    main_dir = os.path.dirname(__file__)
    img_path = os.path.join(main_dir, "images\\")

    role_pos = {
        "top": Coords(x=300, y=384),
        "jg": Coords(x=323, y=327),
        "mid": Coords(x=379, y=303),
        "adc": Coords(x=435, y=327),
        "sup": Coords(x=460, y=384)
    }
    
    
    ele_role_pos_1 = {
        "top": Box((300, 384), w=8, h=8),
        "jg": Box((323, 327), w=8, h=8),
        "mid": Box((379, 303), w=8, h=8),
        "adc": Box((435, 327), w=8, h=8),
        "sup": Box((460, 384), w=8, h=8)
    }
    
    ele_role_pos_2 = {
        "top": Box((300 + 74, 384),w=8, h=8),
        "jg": Box((323 + 74, 327),w=8, h=8),
        "mid": Box((379 + 74, 303),w=8, h=8),
        "adc": Box((435 + 74, 327),w=8, h=8),
        "sup": Box((460 + 74, 384),w=8, h=8)
    }
    role_2_x_offset = 74
    
    pos_messages_dismiss = {
        "verify_email_exit_1": Coords(x=706, y=72),
    }
    
    ele_play_button = Box((52, 20), w=79, h=25, detection=PointDetection(x=90, y=20, img="v2/client_play.png"))
    ele_game_mode_pvp = Box((20, 8), w=20, h=8)
    ele_soloq_mode = Box((127,457),w=134, h=8)
    ele_confirm_play_button = Box((370, 538), w=112, h=25)
    
    ele_role_1 = Box((369,373), w=18, h=19)
    ele_role_2 = Box((443,373), w=18, h=19)
    
    ele_find_match = Box((368,535), w=115, h=26)
    
    ele_accept_match_button = Box((438,428), w=135, h=28, detection=PointDetection(x=506,y=428, img="v2/client_accept_match.png"))
    
    detection_my_pick = PointDetection(x=384,y=2, img="v2/client_choose_champ.png")
    
    ele_lobby_champ_search = Box((580, 74), w=157, h=19)
    ele_lobby_first_champ = Box((276,106), w=52, h=52)
    
    ele_lobby_lock_in = Box((450, 471), w=111, h=26)
    
    
    

    play_button_rdy = Coords(x=90, y=20, img="v2/client_play.png")
    play_button  = Coords(x=90, y=33)
    game_mode_pvp = Coords(x=42, y=80)
    ranked_soloq = Coords(x=175, y=461)
    confirm_play_button = Coords(x=422, y=550)
    
    role_1_pos = Coords(x=378, y=383)
    role_2_pos = Coords(x=452, y=383)
    
    find_match_rdy_button = Coords (x=420, y=535, img="v2/client_find_match_ready.png")
    find_match_button = Coords(x=430, y=538)
    accept_match_button = Coords(x=507, y=429, img="v2/client_accept_match.png")
    
    pick_champ_detect = Coords(x=384, y=2, img="v2/client_choose_champ.png")
    pick_champ = Coords(x=304, y=134)
    champ_search_bar = Coords(x=702, y=82, img="v2/client_choose_champ.png")
    
    lock_in_button = Coords(x=504, y=486)
    

    league_client_name = "League of Legends"
    
    @staticmethod
    def set_league_client_active():
        handle = Client.get_league_client_handle()
        SetForegroundWindow(handle)
    
    @staticmethod
    def get_league_client_handle():
        return FindWindow(0, Client.league_client_name) 
    
    @staticmethod
    def force_close_league():
        leagueProcessNames = {"LeagueCrashHandler.exe", "RiotClientCrashHandler.exe", "LeagueClient.exe", "LeagueClientUxRender.exe", "LeagueClientUx.exe", "RiotClientServices.exe", "League of Legends.exe"}
        for proc in psutil.process_iter():
            
            try:
                if proc.name() in leagueProcessNames:
                    proc.kill()
                    
            except:
                pass
    
    @staticmethod
    def is_league_game_running():
        for proc in psutil.process_iter():
            try:
                if proc.name().lower() == "League of Legends.exe".lower():
                    return True
            except:
                pass
        return False
    
    @staticmethod
    def open_league_client():
        subprocess.Popen(r'"C:\\Riot Games\\Riot Client\\RiotClientServices.exe" --launch-product=league_of_legends --launch-patchline=live')
        
    
    @staticmethod
    def _is_client_play_button_ready():
        return ColorLib.match_color_screen_img((Client.play_button_rdy.x, Client.play_button_rdy.y), Client.img_path + Client.play_button_rdy.img)
            
    
    @staticmethod
    def move_client():
        MoveWindow(Client.get_league_client_handle(), -7,0, 1024, 576, True)
        
    @staticmethod
    def wait_for_league_client(wait_time):
        while Client.get_league_client_handle() != 0:
            time.sleep(1)
        time.sleep(wait_time)
            
    @staticmethod
    def open_ready_client(wait_time):
        
        Client.open_league_client()
        Client.wait_for_league_client(wait_time)
        
        Client.set_league_client_active()
        time.sleep(2)
        Client.move_client()
        time.sleep(5)
        
        if Client.ele_play_button.is_detected() is False:
            for key, val in Client.pos_messages_dismiss.items():
                mouse.move(val.x, val.y)
                time.sleep(0.5)
                mouse.click()
                time.sleep(1.5)
                if Client.ele_play_button.is_detected() is True:
                    break
            
    @staticmethod
    def accept_match(max_time_mins, champ_name):
        count = 0
        while not Client.is_league_game_running() and count < max_time_mins * 60:
            #pick_champ_phase
            if Client.detection_my_pick.is_detected():
                Client.select_champ(champ_name)
                time.sleep(10)
            #accept_match_phase
            if Client.ele_accept_match_button.is_detected():
                Client.ele_accept_match_button.click()
                time.sleep(10)
            #dodged restart find match
            if count > max_time_mins * 60:
                break
            
            count += 1
            time.sleep(1)
    
    @staticmethod
    def select_champ(champ_name):
        Client.ele_lobby_champ_search.click()
        time.sleep(3)
        
        keyboard.write(champ_name, 0.1)
        time.sleep(3)
        
        Client.ele_lobby_first_champ.click()
        time.sleep(3)
        
        Client.ele_lobby_lock_in.click()
        time.sleep(3)
        
    @staticmethod
    def start_match_search(pos1, pos2):
        
        Client.ele_play_button.click()
        time.sleep(2)
        Client.ele_game_mode_pvp.click()
        time.sleep(2)
        Client.ele_soloq_mode.click()
        time.sleep(2)
        Client.ele_confirm_play_button.click()
        time.sleep(2)
        Client.ele_role_1.click()
        time.sleep(2)   
        Client.ele_role_pos_1[pos1].click()
        time.sleep(2)  
           
        Client.ele_role_2.click()
        time.sleep(2)
        
        Client.ele_role_pos_2[pos2].click()
        time.sleep(2)
        
        Client.ele_find_match.click()

        time.sleep(5)

    @staticmethod
    def get_into_game(role1, role2, champ, max_time_mins):
        if not Client.is_league_game_running():
            Client.open_ready_client(32)
            time.sleep(1)
            #Configs.replace_configs()
            Client.start_match_search(role1, role2)
            Client.accept_match(max_time_mins, champ)


from coords import Coords
import psutil
import subprocess
import time
import mouse
import keyboard
from color_lib import Color_Lib
from win32.win32gui import GetForegroundWindow, GetWindowRect, MoveWindow



class Client():
    #C:/Users/trevo/Documents/delank/delank/images/
    #C:/Users/Trevor/Documents/delank/images/
    img_path = "C:/Users/trevo/Documents/delank/delank/images/"
    role_pos = {
        "top": Coords(x=300, y=384),
        "jg": Coords(x=323, y=327),
        "mid": Coords(x=379, y=303),
        "adc": Coords(x=435, y=327),
        "sup": Coords(x=460, y=384)
    }
    
    role_2_x_offset = 74
    
    pos_messages_dismiss = {
        "verify_email_exit_1": Coords(x=706, y=72),
    }
    play_button_rdy = Coords(x=90, y=20, img="v2/client_play.png")
    play_button  = Coords(x=90, y=33)
    game_mode_pvp = Coords(x=42, y=80)
    ranked_soloq = Coords(x=175, y=461)
    confirm_play_button = Coords(x=422, y=550)
    
    role_1_pos = Coords(x=378, y=383)
    role_2_pos = Coords(x=452, y=383)
    
    find_match_button = Coords(x=430, y=538)
    accept_match_button = Coords(x=507, y=429, img="v2/client_accept_match.png")
    
    pick_champ_detect = Coords(x=384, y=2, img="v2/client_choose_champ.png")
    pick_champ = Coords(x=304, y=134)
    champ_search_bar = Coords(x=702, y=82, img="v2/client_choose_champ.png")
    
    lock_in_button = Coords(x=504, y=486)
    
    
    @staticmethod
    def force_close_league():
        leagueProcessNames = {"LeagueCrashHandler.exe", "RiotClientCrashHandler.exe", "LeagueClient.exe", "LeagueClientUxRender.exe", "LeagueClientUx.exe", "RiotClientServices.exe", "League of Legends.exe"}
        for proc in psutil.process_iter():
            
            try:
                if proc.name() in leagueProcessNames:
                    proc.kill()
                    
            except psutil.AccessDenied:
                pass
    
    @staticmethod
    def is_league_game_running():
        for proc in psutil.process_iter():
            try:
                if proc.name().lower() == "League of Legends.exe".lower():
                    return True
            except psutil.AccessDenied:
                pass
        return False
    
    @staticmethod
    def open_league_client():
        subprocess.Popen(r'"C:\\Riot Games\\Riot Client\\RiotClientServices.exe" --launch-product=league_of_legends --launch-patchline=live')
        
    
    @staticmethod
    def _is_client_play_button_ready():
        print(Color_Lib.match_color_screen_img((Client.play_button_rdy.x, Client.play_button_rdy.y), Client.img_path + Client.play_button_rdy.img))
        return Color_Lib.match_color_screen_img((Client.play_button_rdy.x, Client.play_button_rdy.y), Client.img_path + Client.play_button_rdy.img)
            
    
    @staticmethod
    def move_client():
        mouse.move(560,90)
        time.sleep(.1)
        mouse.click()
        time.sleep(.5)
        MoveWindow(GetForegroundWindow(), -7,0, 1024, 576, True)
        
    @staticmethod
    def open_ready_client(wait_time):
        Client.open_league_client()
        time.sleep(wait_time)
        Client.move_client()
        time.sleep(2)
        
        if not Client._is_client_play_button_ready():
            for key, val in Client.pos_messages_dismiss.items():
                mouse.move(val.x, val.y)
                time.sleep(0.5)
                mouse.click()
                time.sleep(1.5)
                if Client._is_client_play_button_ready() is True:
                    break
            
    @staticmethod
    def accept_match(max_time_mins, champ_name):
        count = 0
        while not Client.is_league_game_running() and count < max_time_mins * 60:
            if Color_Lib.match_color_screen_img((Client.pick_champ_detect.x, Client.pick_champ_detect.y), Client.img_path + Client.pick_champ_detect.img):
                Client.select_champ(champ_name)
                time.sleep(10)
            if Color_Lib.match_color_screen_img((Client.accept_match_button.x, Client.accept_match_button.y), Client.img_path + Client.accept_match_button.img):
                mouse.move(Client.accept_match_button.x, Client.accept_match_button.y)
                time.sleep(0.5)
                mouse.click()
                time.sleep(10)
            count += 1
            time.sleep(1)
    
    @staticmethod
    def select_champ(champ_name):
        mouse.move(Client.champ_search_bar.x, Client.champ_search_bar.y)
        time.sleep(0.5)
        mouse.click()
        time.sleep(1)
        
        keyboard.write(champ_name)
        time.sleep(2)
        
        mouse.move(Client.pick_champ.x, Client.pick_champ.y)
        time.sleep(0.5)
        mouse.click()
        time.sleep(1)
        
        mouse.move(Client.lock_in_button.x, Client.lock_in_button.y)
        time.sleep(0.5)
        mouse.click()
        time.sleep(0.5)
        
    @staticmethod
    def start_match_search(pos1, pos2):
        mouse.move(Client.play_button.x, Client.play_button.y)
        time.sleep(0.5)
        mouse.click()
        time.sleep(2)
        
        mouse.move(Client.game_mode_pvp.x, Client.game_mode_pvp.y)
        time.sleep(0.5)
        mouse.click()
        time.sleep(2)
        
        mouse.move(Client.ranked_soloq.x, Client.ranked_soloq.y)
        time.sleep(0.5)
        mouse.click()
        time.sleep(2)
        
        mouse.move(Client.confirm_play_button.x, Client.confirm_play_button.y)
        time.sleep(0.5)
        mouse.click()
        time.sleep(2)
       
        time.sleep(3)
        
        mouse.move(Client.role_1_pos.x, Client.role_1_pos.y)
        time.sleep(0.5)
        mouse.click()
        time.sleep(1)
        
        mouse.move(Client.role_pos[pos1].x, Client.role_pos[pos1].y)
        time.sleep(0.5)
        mouse.click()
        time.sleep(1)
      
        
        mouse.move(Client.role_2_pos.x, Client.role_2_pos.y)
        time.sleep(0.5)
        mouse.click()
        time.sleep(1)
        
        mouse.move(Client.role_pos[pos2].x + Client.role_2_x_offset, Client.role_pos[pos2].y)
        time.sleep(0.5)
        mouse.click()
        time.sleep(1)
        
        mouse.move(Client.find_match_button.x, Client.find_match_button.y)
        time.sleep(0.5)
        mouse.click()
        time.sleep(1)

    @staticmethod
    def get_into_game(role1, role2, champ, max_time_mins):
        if not Client.is_league_game_running():
            Client.open_ready_client(35)
            time.sleep(1)
            Client.start_match_search(role1, role2)
            Client.accept_match(max_time_mins, champ)

            
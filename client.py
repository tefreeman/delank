from coords import Coords
import psutil
import subprocess
import time
import mouse
import keyboard
from color_lib import Color_Lib
from win32.win32gui import GetForegroundWindow, GetWindowRect, MoveWindow

class Client():
    
    img_path = "C:/Users/trevo/Documents/delank/delank/images/"
    role_pos = {
        "top": Coords(x=432, y=441),
        "jg": Coords(x=457, y=386),
        "mid": Coords(x=513, y=362),
        "adc": Coords(x=564, y=386),
        "sup": Coords(x=593, y=441)
        
    }
    
    pos_messages_dismiss = {
        "verify_email_exit_2": Coords(x=841, y=132),
        "leave_buster_warning_button": Coords(x=640, y=402),
        "demoted_message_button": Coords(x=654, y=371),
        "verify_email_exit": Coords(x=840, y=89),
    }
    play_button_rdy = Coords(x=225, y=72, img="v2/client_play.png")
    play_button  = Coords(x=225, y=89)
    game_mode_pvp = Coords(x=178, y=137)
    ranked_soloq = Coords(x=263, y=519)
    confirm_play_button = Coords(x=560, y=610)
    
    role_1_pos = Coords(x=510, y=442)
    role_2_pos = Coords(x=585, y=442)
    
    find_match_button = Coords(x=555, y=605)
    accept_match_button = Coords(x=640, y=524, img="match_found.png")
    
    pick_champ_search = Coords(x=736, y=140, img="pick_champ.png")
    
    champ_search_bar = Coords(x=434,y=192, img="pick_champ")
    
    lock_in_button = Coords(x=640, y=543)
    
    
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
        MoveWindow(GetForegroundWindow(), -7,0, 1115, 632, True)
        
    @staticmethod
    def open_ready_client():
        Client.open_league_client()
        time.sleep(20)
        
        if Client._is_client_play_button_ready():
            mouse.move(Client.play_button.x, Client.play_button.y)
            time.sleep(0.5)
            mouse.click()
            time.sleep(0.5)
        else:
            for key, val in Client.pos_messages_dismiss.items():
                mouse.move(val.x, val.y)
                time.sleep(0.5)
                mouse.click()
                time.sleep(1.5)
                if Client._is_client_play_button_ready() is True:
                    break
            
            mouse.move(Client.play_button.x, Client.play_button.y)
            time.sleep(0.5)
            mouse.click()
            time.sleep(0.5)
            
Client.open_ready_client()
            
            
    
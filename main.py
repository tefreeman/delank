import subprocess
import time
import mouse
import keyboard

from porofessor_live import is_game_over
from PIL import Image
from PIL import ImageGrab
import psutil


champion_ban = "trundle"
champion_pick_1 = "master"
champion_pick_2 = "warwick"
img_path = "C:\\Users\\trevo\\Documents\\delank\\delank\\images\\"

color_pixels = {
    "accept_match": {
        'x': 644,
        'y': 485,
        'img': 'match_found.png'
    },
    
    "ban": {
        'x': 549,
        'y': 64,
        'img': 'ban_champ.png'
    },
    "pick": {
        'x': 549,
        'y': 64,
        'img': 'pick_champ.png'
    }
}

role_pos = {
     "top": {
        "x": 432,
        "y": 441,
        "img": "roles_selected_ready.png"
    },
    "jg": {
        "x": 445,
        "y": 386,
        "img": "roles_selected_ready.png"
    },
    "mid": {
        "x": 511,
        "y": 360,
        "img": "roles_selected_ready.png"
    },
     "adc": {
        "x": 567,
        "y": 384,
        "img": "roles_selected_ready.png"
    },
    "sup": {
        "x": 591,
        "y": 360,
        "img": "roles_selected_ready.png"
    },
}
pos = {
    "leave_buster_warning_button": {
        'x': 640,
        'y': 402,
        'img': "leave_buster_warnings.png"
    },
    
    "demoted_message_button": {
        'x': 654,
        'y': 371,
        'img': "leave_buster_warings.png"
    },
    "verify_email_exit": {
        'x': 840,
        'y': 125,
        'img': "leave_buster_warings.png"
    },
    'play_button': {
        'x': 276, 
        'y': 89, 
        'img': "client.png"
        },
    
    "ranked_solo_q_checkbox": {
        "x": 164,
        'y': 517,
        'img': "play.png",
    },
    "confirm_play_button": {
        "x": 560,
        "y": 606,   
    },
    "accept_match": {
        "x": 640,
        "y": 524,
        "img": "match_found.png"
    },
    "role_1_pos": {
        "x": 510,
        "y": 442,
        "img": "roles_selected_ready.png"
    },
    "role_2_pos": {
        "x": 585,
        "y": 442,
        "img": "roles_selected_ready.png"
    },
    
    
    "roles_select_1_jg_pos": {'x': 454, 'y': 387, "img": "first_role_select.png"},
    "roles_select_2_top_pos": {'x': 504, 'y': 438, "img": "second_roles_select.png"},
    "find_match_button": {"x": 555, "y": 605, "img": "roles_selected_ready.png"},
    "match_found_button": {"x": 637, "y": 517, "img": "match_found.png"},
    "pick_champ_search": {"x": 736, "y": 140, "img": "pick_champ.png"},
    "champ_search_1": {"x": 434, "y": 192, "img": "pick_champ.png"},
    "lock_in": {"x": 640, "y": 543, "img": "pick_champ.png"},

}

def img_screen_pixel_compare(img_path, x, y, max_diff):   
    screenshot = ImageGrab.grab()
    screenshot_rgb: Image = screenshot.convert("RGB")
    screenshot_pixel = screenshot_rgb.getpixel((x,y))
    
    im = Image.open(img_path, 'r')
    img_rgb = im.convert("RGB")
    image_pixel = img_rgb.getpixel((x, y))
    
    total_pixel_diff = abs(screenshot_pixel[0] - image_pixel[0]) + abs(screenshot_pixel[1] - image_pixel[1]) + abs(screenshot_pixel[2] - image_pixel[2])
    print(total_pixel_diff)
    if total_pixel_diff < max_diff:
        return True
    
    else:
        return False
        

    

    
def force_close_league():
    leagueProcessNames = {"LeagueCrashHandler.exe", "RiotClientCrashHandler.exe", "LeagueClient.exe", "LeagueClientUxRender.exe", "LeagueClientUx.exe", "RiotClientServices.exe", "League of Legends.exe"}
    for proc in psutil.process_iter():
        
        try:
            if proc.name() in leagueProcessNames:
                print(proc.name())
                proc.kill()
                
        except psutil.AccessDenied:
            print("access denied")
    
def is_league_game_running():
    for proc in psutil.process_iter():
        try:
            if proc.name().lower() == "League of Legends.exe".lower():
                return True
        except psutil.AccessDenied:
            pass
    return False
        
        
def open_league_client():
    subprocess.Popen(r'"C:\\Riot Games\\Riot Client\\RiotClientServices.exe" --launch-product=league_of_legends --launch-patchline=live')


def Start_Accept_League_client():
    open_league_client()
    time.sleep(25)
    
    mouse.move(pos["verify_email_exit"]["x"], pos["verify_email_exit"]["y"])
    time.sleep(1)
    mouse.click()
    time.sleep(4)
    
    mouse.move(pos["leave_buster_warning_button"]["x"], pos["leave_buster_warning_button"]["y"])
    time.sleep(1)
    mouse.click()
    time.sleep(6)

    mouse.move(pos["demoted_message_button"]["x"], pos["demoted_message_button"]["y"])
    time.sleep(1)
    mouse.click()
    time.sleep(6)

def Start_Matchmaking(role_1: str, role_2: str):
    
    mouse.move(pos["play_button"]["x"], pos["play_button"]["y"])
    time.sleep(1)
    mouse.click()
    time.sleep(3)
    
    mouse.move(pos["ranked_solo_q_checkbox"]["x"], pos["ranked_solo_q_checkbox"]["y"])
    time.sleep(1)
    mouse.click()
    time.sleep(1)
    
    mouse.move(pos["confirm_play_button"]["x"], pos["confirm_play_button"]["y"])
    time.sleep(1)
    mouse.click()
    time.sleep(5)
    
    
    mouse.move(pos["role_1_pos"]["x"], pos["role_1_pos"]["y"])
    time.sleep(1)
    mouse.click()
    time.sleep(2)
    
    mouse.move(pos["roles_select_1_jg_pos"]["x"], pos["roles_select_1_jg_pos"]["y"])
    time.sleep(1)
    mouse.click()
    time.sleep(2)
    
    
    mouse.move(pos["role_2_pos"]["x"], pos["role_2_pos"]["y"])
    time.sleep(1)
    mouse.click()
    time.sleep(2)
    
    mouse.move(pos["roles_select_2_top_pos"]["x"], pos["roles_select_2_top_pos"]["y"])
    time.sleep(1)
    mouse.click()
    time.sleep(2)
    
    mouse.move(pos["find_match_button"]["x"], pos["find_match_button"]["y"])
    time.sleep(1)
    mouse.click()

def accept_matches_until_ban_phase():
    cur_time = 0
    while not img_screen_pixel_compare(img_path + color_pixels["ban"]["img"], color_pixels["ban"]["x"], color_pixels["ban"]["y"], 10):
        print("waiting for ban phase")
        
        if cur_time > 60*30:
            break
        else:
            cur_time += 1
            
    print("ban phase DETECTED")

def accept_match():
    if img_screen_pixel_compare(img_path + color_pixels["accept_match"]["img"], color_pixels["accept_match"]["x"], color_pixels["accept_match"]["y"], 20):
        mouse.move(pos["accept_match"]["x"], pos["accept_match"]["y"])
        time.sleep(1)
        mouse.click()
        time.sleep(1)
        mouse.move(0,0)

def detect_pick_phase():
    cur_time = 0
    while not img_screen_pixel_compare(img_path + color_pixels["pick"]["img"], color_pixels["pick"]["x"], color_pixels["pick"]["y"], 10):
        time.sleep(1)
        print("waiting for pick phase")
        
        if cur_time > 60*3:
            break
        else:
            cur_time += 1
    
    print("pick phase DETECTED")

def select_champ(option_1, option_2):
    
    if img_screen_pixel_compare(img_path + color_pixels["pick"]["img"], color_pixels["pick"]["x"], color_pixels["pick"]["y"], 10):
        
        time.sleep(2)
        mouse.move(pos["pick_champ_search"]["x"], pos["pick_champ_search"]["y"])
        time.sleep(1)
        mouse.click()
        time.sleep(2)
        
        keyboard.write(option_1)
        time.sleep(2)
        mouse.move(pos["champ_search_1"]["x"], pos["champ_search_1"]["y"])
        time.sleep(1)
        mouse.click()
        
        
        time.sleep(2)
        mouse.move(pos["lock_in"]["x"], pos["lock_in"]["y"])
        time.sleep(1)
        mouse.click()


        # second option
        time.sleep(2)
        mouse.move(pos["pick_champ_search"]["x"], pos["pick_champ_search"]["y"])
        time.sleep(1)
        mouse.click()
        time.sleep(2)
        
        keyboard.write(option_2)
        time.sleep(2)
        mouse.move(pos["champ_search_1"]["x"], pos["champ_search_1"]["y"])
        time.sleep(1)
        mouse.click()
        
        
        time.sleep(2)
        mouse.move(pos["lock_in"]["x"], pos["lock_in"]["y"])
        time.sleep(1)
        mouse.click()
        
        

def detect_league_game_start():
    
    cur_time = 0
    while not is_league_game_running():
        time.sleep(1)
    
        if cur_time > 60*3:
            break
        else:
            cur_time += 1
    print("league game exe started")

print("starting in 3 seconds...")

time.sleep(3)


while True:
    force_close_league()
    time.sleep(10)
    
    Start_Accept_League_client()
 
    if not is_league_game_running():
        Start_Matchmaking("jg", "top")
    #time.sleep(60*20)
    
    time.sleep(3)

    
    while not is_league_game_running():
        accept_match()
        select_champ("master", "warwick")
        time.sleep(1)
    
    
    force_close_league()
    
    
    time.sleep(60*6)
    
    max_times = 30
    count = 0
    while not is_game_over():
        time.sleep(60)
        count += 1
        
        if count > max_times:
            break
    
    count = 0
        
        
    #detect when match has ended by pooling opgg    
    
    
    
    
        
    
    
    
    
    
    
    
    
    

import time
from color_lib import ColorLib
import keyboard
import mouse
from game_state import GameState
from action_system import ActionSystem
from actions import Actions
import random
from client import Client

def PlayGame(stop_flag):
    gs = GameState()
    loop_count = 0
    ff_time = 0
    first_run = True
    while Client.is_league_game_running():
        gs.update()
        
        if gs.has_game_started() and not stop_flag['val']:
            if first_run is True:
                time.sleep(10)
                Actions.cast_spell('ctrl+4')
                time.sleep(10)
                Actions.cast_spell('y')
                time.sleep(1)
                Actions.purchase_recommend()
                first_run = False
                ff_time = time.time() + 60*15
            
            if time.time() > ff_time: 
                Actions.type_in_chat("/ff")
                ff_time += 60
                
            if not gs.is_adc_dead() and not gs.is_i_dead():
                if gs.is_yummi_attached() is True:
                    if gs.is_adc_hp_low() is True:
                        Actions.cast_spell('e')
                    
                    if gs.is_adc_hp_critical() is True:
                        coord = gs.get_general_enemy_dir_coords()
                        Actions.cast_spell('d')
                        mouse.move(coord.x, coord.y)
                        time.sleep(0.01)
                        Actions.cast_spell('r')
                        time.sleep(0.01)
                        Actions.cast_spell('q')
                else:
                    Actions.yummi_attach('f4')
                    
            if gs.is_i_dead():
                Actions.purchase_recommend()
                
                if random.randint(0, 15) == 10:
                    Actions.type_shit_in_chat()
                             
            if gs.is_adc_dead() and not gs.is_i_dead():
                if gs.get_fountain_coords() is not None:
                    Actions.retreat(gs.get_fountain_coords())
            
            if loop_count % 10 == 0:
                Actions.random_mouse_movement()
                time.sleep(0.20)
                
            if loop_count % 20 == 0:
                Actions.level_all_spells('r', 'q', 'w', 'e')
            
            if loop_count == 40:
                Actions.cast_spell('4')
                Actions.cast_spell('1')
                loop_count = 0
            
            if random.randint(0, 50):
                Actions.cast_spell('ctrl+4')
            loop_count += 1
            time.sleep(0.04)

    
    
    

    
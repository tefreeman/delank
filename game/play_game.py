import time
from color_lib import ColorLib
import keyboard
import mouse
from game.game_state import GameState
from action_system import ActionSystem
from actions import Actions
import random
from client import Client
from action import Action



def PlayGame(stop_flag, attach_target):
    gs = GameState()
    items = ["spellthief's edge", "Tear of the Goddess",  "kindlegem", "amplifying Tome", "amplifying Tome", "Blasting Wand", "EverFrost"]
    loop_count = 1
    ff_time = 0
    first_run = True
    
    s_time = time.time()
    increase_loop_dur = random.randint(3,7)
    
    while Client.is_league_game_running():
        gs.update()
        
        if gs.has_game_started() and not stop_flag['val']:
            if first_run is True:
                time.sleep(1)
                Actions.cast_spell('ctrl+4')
                Actions.cast_spell('y')
                time.sleep(1)
                Actions.purchase_recommend()
                first_run = False
                ff_time = time.time() + 60*15
                Actions.action_troll_ward(gs.get_my_team_side())
            
            
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
                    Actions.yummi_attach(attach_target['val'])
                    
            if gs.is_i_dead():
                Actions.purchase_recommend()
                
                if random.randint(0, 15) == 10:
                    Actions.type_shit_in_chat()
                             
            if gs.is_adc_dead() and not gs.is_i_dead():
                if gs.get_fountain_coords() is not None:
                    Actions.retreat(gs.get_fountain_coords())
            
            if time.time() - s_time > increase_loop_dur:
                loop_count = loop_count + 1
                
                increase_loop_dur = random.randint(3,7)
                s_time = time.time()
                
            
            if loop_count % 3 == 0:
                if random.randint(0, 1) == 1:
                    pass
                    Actions.random_mouse_movement()
                    time.sleep(0.15)
                
            if loop_count % 4 == 0:
                if random.randint(0, 1) == 1:
                    Actions.level_all_spells('r', 'q', 'w', 'e')
            
            if loop_count % 15 == 0:
                if random.randint(0, 1) == 1:
                    if gs.is_yummi_attached():
                        Actions.cast_spell('4')
                        Actions.cast_spell('1')
            
            if loop_count % 15 == 0:
                if random.randint(0, 1) == 1:
                    if gs.is_yummi_attached():
                        Actions.cast_spell('ctrl+4')
            
            time.sleep(0.04)

    
    
    

    
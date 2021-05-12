from game.player import Player
from game.yummi import Yummi
from coords import Coords
from game.team import Team
from game.game_coords import GameCoords
from color_lib import ColorLib
from PIL import Image
from mss import mss

class GameState():
    def __init__(self):
        self.img = None
        
        self.ally_low_hp = 0.75
        self.ally_critical_hp = 0.25
        
        self._my_fountain_coords = None
        self._my_team_side = None
        self._general_enemy_dir_coords = None
        self._has_game_started = False
        self._is_in_fountain = True
        self._is_adc_hp_low = False
        self._is_adc_hp_critical = False
        self._is_adc_dead = False
        #self._is_in_fountain = False
        #self_is_camera_locked = False
        
        
        self.yummi = Yummi()
        self.team = Team()
    
    def debug(self):
        print("has game started: ", self._has_game_started)
        print("is adc low: ", self._is_adc_hp_low)
        print("is adc critcally low: ", self._is_adc_hp_critical)
        print("is yummi attached: ", self.is_yummi_attached())
        
    def _update_all(self):
        
        if self._has_game_started == False:
            self.__u_has_game_started()

            if self._has_game_started is True:
                self._set_ally_fountain_loc()
        else:
             self.__u_yummi_attached()
             self.__u_is_adc_hp_low()
             self.__u_is_adc_hp_critical()
             self.__u_player_is_alive()
             self.__u_is_adc_dead()
    
    def _set_ally_fountain_loc(self):
        if ColorLib.match_color_screen(self.img, (GameCoords.bottom_left_base.x, GameCoords.bottom_left_base.y), GameCoords.bottom_left_base.colors[0], 15, -15):
            self._my_fountain_coords = GameCoords.bottom_fountain
            self._my_team_side = 'bot'
            self._general_enemy_dir_coords = Coords(x=870, y=180)
        else:
            self._my_fountain_coords = GameCoords.top_fountain
            self._my_team_side = 'top'
            self._general_enemy_dir_coords = Coords(x=380, y=470)
            
    def __u_yummi_attached(self):
        self.yummi.set_attached(ColorLib.fuzzy_color_match_test(self.img, GameCoords.yummi_attached, 10, -10))
    
    def __u_is_adc_hp_low(self):
        x = GameCoords.health_bars['adc'].x + round( GameCoords.health_bars['adc'].w * self.ally_low_hp)
        y = GameCoords.health_bars['adc'].y+1
        
        self._is_adc_hp_low = ColorLib.match_color_screen(self.img, (x, y), GameCoords.health_bars['adc'].colors[0])
    
    def __u_is_adc_hp_critical(self):
        x = GameCoords.health_bars['adc'].x + round( GameCoords.health_bars['adc'].w * self.ally_critical_hp)
        y = GameCoords.health_bars['adc'].y+1
        
        self._is_adc_hp_critical = ColorLib.match_color_screen(self.img, (x, y), GameCoords.health_bars['adc'].colors[0])
    
    def __u_is_adc_dead(self):
        self._is_adc_dead = ColorLib.fuzzy_color_match_test(self.img, GameCoords.my_adc_dead_hp_bar, 15, -15)
        
    def __u_has_game_started(self):
        self._has_game_started = ColorLib.match_color_screen(self.img, (GameCoords.has_game_started.x, GameCoords.has_game_started.y), GameCoords.has_game_started.colors[0])

    def __u_player_is_alive(self):
         self.yummi.set_is_dead(ColorLib.fuzzy_color_match_test(self.img, GameCoords.my_champ_dead_team_bar, 15, -15))
    
    def __u_am_i_in_fountain(self):
        pass
    
    def has_game_started(self):
        return self._has_game_started
    
    def is_adc_hp_low(self):
        return self._is_adc_hp_low
    
    def is_adc_hp_critical(self):
        return self._is_adc_hp_critical
    
    def is_adc_dead(self):
        return self._is_adc_dead
    
    def is_i_dead(self):
        return self.yummi.is_dead()
    
    def is_yummi_attached(self):
        return self.yummi.is_attached()
    
    def get_general_enemy_dir_coords(self):
        return self._general_enemy_dir_coords
        
    def get_fountain_coords(self):
        return self._my_fountain_coords

    def get_my_team_side(self):
        return self._my_team_side
    
    def update(self):
        with mss() as sct:
            monitor = sct.monitors[1]
            sct_img = sct.grab(monitor)
            self.img = Image.frombytes('RGB', sct_img.size, sct_img.bgra, 'raw', 'BGRX')
        
        self._update_all()
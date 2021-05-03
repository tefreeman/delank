from player import Player
from yummi import Yummi
from team import Team
from game_coords import GameCoords
from color_lib import Color_Lib
from PIL import Image


class GameState():
    def __init__(self):
        self.img = None
        self._is_game_started = False
        self.yummi = Yummi()
        self.team = Team()
    
    def _update_all(self):
        self.__u_yummi_attached()
    
    def __u_yummi_attached(self):
        self.yummi.set_attached(Color_Lib.fuzzy_color_match_test(self.img, GameCoords.yummi_attached), 10, -10)
    
    def __u_team_hp(self):
        pass
    
    def has_game_started(self):
        return self._is_game_started
    
    def update(self, img):
        self.img =img
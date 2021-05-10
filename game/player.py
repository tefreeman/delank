from utility import Utility

class Player:
    def __init__(self, spell_lvl_order=()):
        self._is_dead = False
        self.hp = 1.0


    def set_hp(self, hp: float):
        self.hp = hp
    
    def set_is_dead(self, status: bool):
        self._is_dead = Utility.denoised_bool(status, "Player_set_is_dead")
        
    def is_dead(self):
        return self._is_dead
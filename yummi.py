from player import Player
from utility import Utility

class Yummi(Player):
    def __init__(self, spell_lvl_order):
        Player.__init__(self)
        self._is_attached = False

        if len(spell_lvl_order) is 0:
                self.spell_lvl_order = ('q', 'e', 'q', 'e', 'q', 'r', 'q', 'e', 'q', 'e', 'r', 'q', 'w', 'w', 'r', 'w', 'w')
        elif len(spell_lvl_order) is not 18:
            raise Exception("spell lvl order must be 18")
        else:
            self.spell_lvl_order = spell_lvl_order
    
    def set_attached(self, status: bool):
        self._is_attached = Utility.denoised_bool(status, "Yummi_set_attached")

    def is_attached(self):
        return self._is_attached
    
    def auto_level(self):
        pass

        

    
test = Yummi()


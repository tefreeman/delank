from player import Player
from utility import Utility

class Yummi(Player):
    def __init__(self):
        Player.__init__(self)
        self._is_attached = False
    
    def set_attached(self, status: bool):
        self._is_attached = Utility.denoised_bool(status, "Yummi_set_attached")

    def is_attached(self):
        return self._is_attached

    
test = Yummi()


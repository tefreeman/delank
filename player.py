class Player:
    def __init__(self):
        self.is_dead = False
        self.hp = 1.0
    
    def set_hp(self, hp: float):
        self.hp = hp
    
    def set_is_dead(self, status: bool):
        self.is_dead = status
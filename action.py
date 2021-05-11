import time
from utility import Utility

class Action:
    
    def __init__(self,func, cd=-1, is_blocking=True):
        
        self._next_fire_time = 0
        self.cd = cd
        
        self.is_enabled = True
        self.enable_at = 0
        
        self.func = func
        self.is_blocking = True
    
    def fire(self):
        if not self.is_enabled:
            now = time.time()
            if now >= self.enable_at:
                self.is_enabled = True
        
        if self.is_enabled:
            if self._is_on_cd():
                self.func()
                
    def enable(self):
        self.is_enabled = True

    def disable(self, disable_for=-1):
        self.is_enabled = False
        if disable_for != -1:
            self.enable_at = time.time() + disable_for

            
    def _is_on_cd(self):
        if self.cd != -1:
            now = time.time() 
            if now >= self._next_fire_time:
                self._next_fire_time = now + self.cd        
                return True
            else:
                return False
        else:
            return True
    
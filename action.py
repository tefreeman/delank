import time

class Action:
    
    def __init__(self,func, cd=-1, is_blocking=True):
        
        self._next_call = 0
        self.cd = cd
        self.func = func
        self.is_blocking = True
    
    def fire(self):
        if self._is_on_cd():
            self.func()
    
    def _is_on_cd(self):
        if self.cd != -1:
            now = time.time() 
            if now >= self._next_call:
                self._next_call = now + self.cd        
                return True
            else:
                return False
        else:
            return True
    
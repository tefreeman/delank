import time
import threading

class ActionSystem:
    
    _actions = []
    _clear_flag = False
    start_time = 0
    
    # str: fast, slow
    @staticmethod
    def add_action(func, is_blocking = True, add_to_front = False):
        if add_to_front is False:
            ActionSystem._actions.append((is_blocking, func))
        else:
            ActionSystem._actions.insert(0, (is_blocking, func))
    
    @staticmethod
    def clear_actions():
        ActionSystem._actions = []
    
    @staticmethod
    # return True if more left return False if actions done
    def do_action():
        if len(ActionSystem._actions) > 0:
            if ActionSystem._actions[0][0] is True:
                ActionSystem._actions[0][1]()
            
            ActionSystem._actions.pop(0)
            return True
        else:
            return False

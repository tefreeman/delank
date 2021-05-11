import time
from action import Action


def test_print():
    print('trevor')
    
test = Action(test_print, 3)

test.disable(10)
while True:
    test.fire()
    time.sleep(1)
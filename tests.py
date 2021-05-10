from element import Box
from input import Mouse
import random
import time

time.sleep(1)

Mouse()
tries = 10

for x in range(0, tries):
    pt = (random.randint(400,1280), random.randint(400,720))
    w = random.randint(0, 400)
    h = random.randint(0, 400)
    new_box = Box(pt, w, h)

    new_box.click()
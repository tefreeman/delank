from client import Client
from play_game import PlayGame
import time
while True:
    
    Client.get_into_game("sup", "mid", "yuumi", 30)
    PlayGame()
    time.sleep(5)
    Client.force_close_league()
    time.sleep(30)

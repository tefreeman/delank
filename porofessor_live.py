import requests


def is_game_over(summoner_tag: str):
    try:
        not_in_game_msg = "The summoner is not in-game, please retry later."
        
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        x = requests.get('https://porofessor.gg/live/na/' + summoner_tag, headers=headers)

        print(x.status_code)
        if x.status_code == 200:
            if x.text.find(not_in_game_msg) > -1:
                return True
            else:
                return False
    except:
        return False
    
print(is_game_over("diaperdáddy"))
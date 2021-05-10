from element import Box, PointDetection

class GameElements:
    item_result_pos = Box((234,184), w=137, h=35)
    item_buy_button_pos = Box((657,551), w=247, h=20, detection=PointDetection(783, 551, img="/v2/game_shop_item_search.png"))
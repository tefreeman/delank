from coords import Coords
# 246 -> 270
# 215 -> 239
class GameCoords:
    yummi_attached = Coords(x=583, y=245, h=50, w=5, colors=[(99,93,222),(115,109,255), (82,78,189)], img="", shape="vline")  
    my_champ_potrait_dead = Coords(x=452, y=684, h=1, w=18, colors=[(245,1,1)], img="", shape="hline")
    my_champ_dead_team_bar = Coords(x=210, y=495, h=2,w=15, colors=[(245,1,1)], img="", shape="hline")
    my_adc_dead_hp_bar = Coords(x=152, y=496, h=4, w=34, colors=[(245,1,1)], img="", shape="hline")
    ally_focus_center = Coords(x=640, y=330, h=1, w=1)
    has_game_started = Coords(x=218, y=709, h=1, w=1, colors=[(171,144,98)], img="")
    bottom_left_base = Coords(x=55, y=660, h=1, w=1, colors= [(52, 144, 174), (160, 44, 43)]) #blue, red
    upper_right_base = Coords(x=152, y=563, h=1, w=1, colors= [(160, 44, 43), (52, 144, 174)]) #red, blue
    
    bottom_fountain = Coords(x=14, y=702)
    top_fountain = Coords(x=190, y=530)
    
    
    shop_select_recommend = Coords(x=270, y=320)
    shop_purchase_selected = Coords(x=708, y=576)
    shop_tab_recommend = Coords(x=230, y=132)
    bl_fountain_minimap_camera_box = Coords(x=33, y=686, h=8, w=2, colors = [(255,255,255)], shape="vline")
    health_bars = {
        'top': Coords(),
        'jg': Coords(),
        'mid': Coords(),
        'adc': Coords(x=152, y=496, h=4, w=34, colors=[(19,19,19)], img="", shape="hline") # color is unfilled hp bar
    }
    
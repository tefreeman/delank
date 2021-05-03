from mss import mss
from PIL import Image
from coords import Coords

class Color_Lib():
    cached_images = {}
    
    @staticmethod  
    def get_img(img_path: str):
        if img_path in Color_Lib.cached_images:
            return Color_Lib.cached_images[img_path]
        else:
            img = Image.open(img_path, 'r')
            Color_Lib.cached_images[img_path] = img
            return img
    
    @staticmethod
    def fuzzy_color_match(input_c, output_c, max_color_dif = 5, min_color_diff = -5):
        if (input_c[0] - output_c[0]) > max_color_dif or (input_c[0] - output_c[0]) < min_color_diff:
            return False
        if (input_c[1] - output_c[1]) > max_color_dif or (input_c[1] - output_c[1]) < min_color_diff:
            return False
        if (input_c[2] - output_c[2]) > max_color_dif or (input_c[2] - output_c[2]) < min_color_diff:
            return False
    
        return True

    
    @staticmethod
    def color_compare(color, colors_match):
        scores = []
        for color_match in colors_match:
            scores.append(abs(color_match[0] - color[0]) + abs(color_match[1] - color[1]) + abs(color_match[2] - color[2]))
            
        lowest_val = 10000
        id = -1
        for i in range(0, len(scores)):
            if scores[i] < lowest_val:
                lowest_val = scores[i]
                id = i
        return id
                
            
    @staticmethod
    def fuzzy_color_match_test(screen: Image, coord: Coords, max_color_dif = 5, min_color_diff = -5):
        detections = {'top': False, 'bottom': False, }
        for color in coord.colors:
            if coord.shape == "vline":
                for i in range(coord.y,  round(coord.y + coord.h/2)):
                    if Color_Lib.fuzzy_color_match(Color_Lib.get_pixel_color((coord.x, i), screen),color, max_color_dif, min_color_diff):
                        detections['bottom'] = True           
                    
                for j in range(coord.y - round(coord.h/2), coord.y):
                    if Color_Lib.fuzzy_color_match(Color_Lib.get_pixel_color((coord.x, j), screen), color, max_color_dif, min_color_diff):
                        detections['top'] = True
                        
        return detections['top'] or detections['bottom']
    
    @staticmethod
    def get_pixel_color(coords, img: Image):
        return img.getpixel(coords)
    
    @staticmethod
    def get_vline_color(coords, height, img: Image):
        color_arr = []
        for i in range(0, height):
            color_arr.append(Color_Lib.get_pixel_color((coords[0], coords[1] + i), img))
        return color_arr

    
    @staticmethod
    def match_color_screen_img(screen, coords, img_path, max_color_diff=5, min_color_diff = -5):
        img = Color_Lib.get_img(img_path)
        img_color = Color_Lib.get_pixel_color(coords, img)
        screen_color = Color_Lib.get_pixel_color(coords, screen)
        
        return Color_Lib.fuzzy_color_match(img_color, screen_color)

    @staticmethod
    def match_color_screen(screen, coords, color, max_color_diff=5, min_color_diff = -5):
        screen_color = Color_Lib.get_pixel_color(coords, screen)
        
        return Color_Lib.fuzzy_color_match(color, screen_color)

    @staticmethod
    def is_color_in_vline_on_screen(screen, coords, height, color, max_color_diff=5, min_color_diff=-5):
        screen = Color_Lib.get_screen()
        vline_colors = Color_Lib.get_vline_color(coords, height, screen)
       
        for vline_color in vline_colors:
           if Color_Lib.fuzzy_color_match(vline_color, color, max_color_diff, min_color_diff):
               return True
    
        return False
            
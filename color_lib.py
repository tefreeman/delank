from mss import mss
from PIL import Image
from coords import Coords

class ColorLib:
    cached_images = {}

    
    @staticmethod  
    def get_img(img_path: str):
        if img_path in ColorLib.cached_images:
            return ColorLib.cached_images[img_path]
        else:
            img = Image.open(img_path, 'r')
            ColorLib.cached_images[img_path] = img
            return img
    
    @staticmethod
    def get_screen():
          with mss() as sct:
            monitor = sct.monitors[1]
            sct_img = sct.grab(monitor)
            return Image.frombytes('RGB', sct_img.size, sct_img.bgra, 'raw', 'BGRX')
        
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
        detections = {'top': False, 'bottom': False, 'left': False, 'right': False}
        for color in coord.colors:
            if coord.shape == "vline":
                for i in range(coord.y,  round(coord.y + coord.h/2)):
                    if ColorLib.fuzzy_color_match(ColorLib.get_pixel_color((coord.x, i), screen),color, max_color_dif, min_color_diff):
                        detections['bottom'] = True           
                    
                for j in range(coord.y - round(coord.h/2), coord.y):
                    if ColorLib.fuzzy_color_match(ColorLib.get_pixel_color((coord.x, j), screen), color, max_color_dif, min_color_diff):
                        detections['top'] = True
            
            elif coord.shape == "hline":
                for i in range(coord.x, round(coord.x + coord.w)):
                    if ColorLib.fuzzy_color_match(ColorLib.get_pixel_color((i, coord.y), screen), color, max_color_dif, min_color_diff):
                        detections['left'] = True     
        
        if coord.shape == "vline":      
            return detections['top'] or detections['bottom']
        
        elif coord.shape == "hline":
            return detections['left'] or detections['right']
    
    @staticmethod
    def get_pixel_color(coords, img: Image):
        return img.getpixel(coords)
    
    @staticmethod
    def get_vline_color(coords, height, img: Image):
        color_arr = []
        for i in range(0, height):
            color_arr.append(ColorLib.get_pixel_color((coords[0], coords[1] + i), img))
        return color_arr

    
    @staticmethod
    def match_color_screen_img(coords, img_path, max_color_diff=5, min_color_diff = -5):
        screen = ColorLib.get_screen()
        
        img = ColorLib.get_img(img_path)
        img_color = ColorLib.get_pixel_color(coords, img)
        
        screen_color = ColorLib.get_pixel_color(coords, screen)
        
        return ColorLib.fuzzy_color_match(img_color, screen_color)

    @staticmethod
    def match_color_screen(screen, coords, color, max_color_diff=5, min_color_diff = -5):
        screen_color = ColorLib.get_pixel_color(coords, screen)
        
        return ColorLib.fuzzy_color_match(color, screen_color)

    @staticmethod
    def is_color_in_vline_on_screen(screen, coords, height, color, max_color_diff=5, min_color_diff=-5):
        screen = ColorLib.get_screen()
        vline_colors = ColorLib.get_vline_color(coords, height, screen)
       
        for vline_color in vline_colors:
           if ColorLib.fuzzy_color_match(vline_color, color, max_color_diff, min_color_diff):
               return True
    
        return False
            
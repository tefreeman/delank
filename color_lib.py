from mss import mss
from PIL import Image


class Color_Lib():
    @staticmethod
    def get_screen():
          with mss() as sct:
            monitor = sct.monitors[1]
            sct_img = sct.grab(monitor)
            return Image.frombytes('RGB', sct_img.size, sct_img.bgra, 'raw', 'BGRX')
    
    @staticmethod  
    def get_img(img_path: str):
        img = Image.open(img_path, 'r')
        return Image.frombytes('RGB', img.size, img.bgra, 'raw', 'BGRX')
    
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
    def get_pixel_color(coords, img: Image):
        return img.getpixel(coords)
    
    @staticmethod
    def match_color_screen_img(coords, img_path, max_color_diff=5, min_color_diff = -5):
        img = Color_Lib.get_img(img_path)
        screen = Color_Lib.get_screen()
        
        img_color = Color_Lib.get_pixel_color(coords, img)
        screen_color = Color_Lib.get_pixel_color(coords, screen)
        
        return Color_Lib.fuzzy_color_match(img_color, screen_color)


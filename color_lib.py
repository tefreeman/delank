from mss import mss
from PIL import Image
from coords import Coords
import time
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
    def minimap_to_coord(screen, prev_cord):
        
        minimap_pos = (9, 520)
        minimap_size = 190
        
        minimap_mid_x = minimap_pos[0] + round(minimap_size / 2)
        minimap_mid_y = minimap_pos[1] + round(minimap_size / 2)
        
        box_width = 52
        box_height = 28
        
        
        
        
        x = minimap_pos [0]+ int(box_width/3)
        
        found_points = []
        while x < minimap_pos[0] + minimap_size:
            for y in range(minimap_pos[1], minimap_size + minimap_pos[1]):
                c = ColorLib.get_pixel_color((x, y), screen )
                
                if c[0] == 255 and c[1] == 255 and c[2] == 255:
                    found_points.append((x,y))
                
            
            x += box_width - 5
        
        length_found_points = len(found_points)
        #print(length_found_points)
        x_dir = -1
        y_dir = -1
        
       
        if length_found_points > 0:
            if found_points[0][0] > minimap_mid_x:
                # on right side use left corner
               x_dir = -1
            else:
                # on left side use right corner
               x_dir = 1
            
            if found_points[0][1] > minimap_mid_y:
                # on bottom side use top corner
                y_dir = -1
            else:
                #on top side use bottom corner
                y_dir = 1
        
        
            if length_found_points < 5:
                t_x = found_points[1][0]
                t_y = found_points[1][1]
            else:
                t_x = found_points[0][0]
                t_y = found_points[0][1]
              
        
            p_color = ColorLib.get_pixel_color((t_x, t_y), screen )
            
            while p_color[0] == 255 and p_color[1] == 255 and p_color[2] == 255:
                t_x += x_dir
                
                p_color = ColorLib.get_pixel_color((t_x, t_y), screen )
            
            t_x -= x_dir
           
            
            
            p_color = ColorLib.get_pixel_color((t_x, t_y), screen )
            while p_color[0] == 255 and p_color[1] == 255 and p_color[2] == 255:
                t_y += y_dir
                
                p_color = ColorLib.get_pixel_color((t_x, t_y), screen )
            t_y -= y_dir
            
            tt_x = t_x + x_dir*2
            tt_y = t_y + y_dir*2
            count = 0
            
            p_color = ColorLib.get_pixel_color((tt_x, tt_y), screen )
            
            while p_color[0] == 255 and p_color[1] == 255 and p_color[2] == 255:
                tt_y += y_dir
                
                p_color = ColorLib.get_pixel_color((tt_x, tt_y), screen )
                count += 1
            
            tt_y -= y_dir
            
            if count > 0:
                t_y = tt_y
            
            
            offset_coords =[(0,1), (1,0), (1,1), (1,2), (2,1), (2,0), (0,2), (2,2)]
            for c in offset_coords:
                lx = t_x - x_dir * c[0]
                ly = t_y - y_dir * c[1]
                
                m_color = ColorLib.get_pixel_color((lx, ly), screen )
                x_color = ColorLib.get_pixel_color((lx + x_dir, ly), screen )
                y_color = ColorLib.get_pixel_color((lx, ly + y_dir), screen )

                if m_color[0] != 255 and m_color[1] != 255 and m_color[2] != 255\
                    and x_color[0] == 255  and x_color[1] == 255  and x_color[2] == 255\
                    and y_color[0] == 255 and y_color[1] == 255 and y_color[2] == 255:
                        t_x = lx
                        t_y = ly
                else:
                    print('exact corner not foudn')
                
                    
            
            
            #print('xdir: ', x_dir, " ydir: " , y_dir)
            #print('tx: ', t_x, " ty: " , t_y)
            #print(t_y)
            if x_dir == -1:
                loc_x = t_x + (box_width / 2)
            else:
                loc_x = t_x - (box_width / 2)
            
            if y_dir == -1:
                loc_y = t_y + (box_height / 2)
            else:
                loc_y = t_y - (box_height / 2)

            #print('loc_x: ', loc_x, ", loc_y: ", loc_y)
            return loc_x, loc_y
        else:
            return (-1,-1)
            
        
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


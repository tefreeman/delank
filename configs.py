from client import Client
import os, shutil

class Configs:
    new_config_dir = Client.main_dir + '\\league_configs\\new\\'
    saved_config_dir = Client.main_dir + '\\league_configs\\saved\\'
    l_config_dir = "C:\\Riot Games\\League of Legends\\Config\\"
    
    @staticmethod
    def replace_configs():


        new_game_cfg = Configs.new_config_dir + "game.cfg"
        new_input_ini = Configs.new_config_dir + "input.ini"
        new_p_settings = Configs.new_config_dir + "PersistedSettings.json"
        
        l_game_cfg = Configs.l_config_dir + "game.cfg"
        l_input_ini = Configs.l_config_dir + "input.ini"
        l_p_settings = Configs.l_config_dir + "PersistedSettings.json"
        
        if os.path.exists(l_game_cfg):
            shutil.copy2(l_game_cfg, Configs.saved_config_dir)
            os.remove(l_game_cfg)
            shutil.copy2(new_game_cfg, Configs.l_config_dir)
        
        if os.path.exists(l_input_ini):
            shutil.copy2(l_input_ini, Configs.saved_config_dir)
            os.remove(l_input_ini)
            shutil.copy2(new_input_ini, Configs.l_config_dir)
        
        if os.path.exists(l_p_settings):
            shutil.copy2(l_p_settings, Configs.saved_config_dir)
            os.remove(l_p_settings)
            shutil.copy2(new_p_settings, Configs.l_config_dir)
    
    def restore_configs():
        saved_game_cfg = Configs.saved_config_dir + "game.cfg"
        saved_input_ini = Configs.saved_config_dir + "input.ini"
        saved_p_settings = Configs.saved_config_dir + "PersistedSettings.json"
        
        if os.path.exists(saved_game_cfg):
            shutil.copy2(saved_game_cfg, Configs.l_config_dir)
        else:
            raise Exception("no saved game_cfg")
        
        if os.path.exists(saved_input_ini):
            shutil.copy2(saved_input_ini, Configs.l_config_dir)
        else:
            raise Exception("no saved input_ini")
        
        if os.path.exists(saved_p_settings):
            shutil.copy2(saved_p_settings, Configs.l_config_dir)
        else:
            raise Exception("no saved input_ini")
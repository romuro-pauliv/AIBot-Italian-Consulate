# +--------------------------------------------------------------------------------------------------------------------|
# |                                                                                        APP.Services.Login.email.py |
# |                                                                                             Author: Pauliv, Rômulo |
# |                                                                                          email: romulopauliv@bk.ru |
# |                                                                                                    encoding: UTF-8 |
# +--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
import pyautogui as GUI
from Tools.AI.img2text_coord import ImageTools
from Tools.json.read_json import read_json
from Tools.page.up_down import updown_page
from log.AISearchText import Log

from typing import Any
from time import sleep
# |--------------------------------------------------------------------------------------------------------------------|
class AISearch(object):
    def __init__(self) -> None:
        config: dict[str, Any] = read_json("Tools/json/data.json")
        self.resolution: list[int] = config['screen']['resolution']
        self.AI_loop_try: int = config['config']['tesseract-recognition-try']
    
    def search2write(self, page: str, search_text: str, write_in_box: str,
                     increment_x: int = 20, increment_y: int = 20) -> None | bool:
        
        # + Variables and Objects +
        count: int = 0
        log = Log()
        function_name: str = "AI-S2W"
        
        # + Sweep Text Search +
        while count < self.AI_loop_try:
            
            # + ImageTools Object __init__ +
            ImageObj = ImageTools(0, 0, self.resolution[0], self.resolution[1])
            
            # | Preprocessing Image Alternator |-----------------------------------------------------------------------|
            alternator = lambda num: num % 2 == 0
            if alternator(count):
                coord: dict[str, int] | bool = ImageObj.search_data2img_hard(search_text)
            else:
                coord: dict[str, int] | bool = ImageObj.search_data2img(search_text)
            # |--------------------------------------------------------------------------------------------------------|
            
            # + Loading Log +
            log.AISearch_loading(count, function_name, page, search_text)
            
            if coord != False:  # + Successfully Complete Process +
                
                # | Click and Write Function |-------------------------------------------------------------------------|
                GUI.click((coord[0]+increment_x), (coord[1]+increment_y)), GUI.write(write_in_box, 0.1)
                GUI.click(0, (self.resolution[1] - 20))
                # |----------------------------------------------------------------------------------------------------|
                
                # + Complete Log +
                log.AISearch_complete(function_name, page, search_text)
                break
            else:
                # + Iterator +
                updown_page(count)
                count += 1
        
        # + Failed Process +
        if count >= self.AI_loop_try:
            log.AISearch_failed(function_name, page, search_text)
        
        return False
    
    def search2click(self, page: str, search_text: str, increment_x: int = 20, increment_y: int = 20) -> None | bool:
        
        # + Variables and Objects +
        count: int = 0
        log = Log()
        function_name: str = "AI-S2C"
        
        # + Sweep Text Search +
        while count < self.AI_loop_try:
            
            # + ImageTools Object __init__ +
            imageObj = ImageTools(0, 0, self.resolution[0], self.resolution[1])
            
            # | Preprocessing Image Alternator |-----------------------------------------------------------------------|
            alternator = lambda num: num % 2 == 0
            if alternator(count):
                coord: dict[str, int] | bool = imageObj.search_data2img_hard(search_text)
            else:
                coord: dict[str, int] | bool = imageObj.search_data2img(search_text)
            # |--------------------------------------------------------------------------------------------------------|
            
            # + Loading Log +
            log.AISearch_loading(count, function_name, page, search_text)
            
            if coord != False:  # + Successfully Complete Process +
                # | Click and Write Function |-------------------------------------------------------------------------|
                GUI.click((coord[0]+increment_x), (coord[1]+increment_y))
                GUI.click(0, (self.resolution[1] - 20))
                # |----------------------------------------------------------------------------------------------------|
                
                # + Complete Log +
                log.AISearch_complete(function_name, page, search_text)
                break
            else:
                # + Iterator +
                updown_page(count)
                count += 1
        
        # + Failed Process +
        if count >= self.AI_loop_try:
            log.AISearch_failed(function_name, page, search_text)
        
        return False
    
    def search2true(self, page: str, search_text: str, sweep: bool = False) -> bool:
        
        # + Variables and Objects +
        count: int = 0
        log = Log()
        function_name: str = "AI-S2T"
        
        # + Sweep Text Search +
        while count < self.AI_loop_try:
            
            # + ImageTools Object __init__ +
            imageObj = ImageTools(0, 0, self.resolution[0], self.resolution[1])
            
            # | Preprocessing Image Alternator |-----------------------------------------------------------------------|
            alternator = lambda num: num % 2 == 0
            if alternator(count):
                coord: dict[str, int] | bool = imageObj.search_data2img_hard(search_text)
            else:
                coord: dict[str, int] | bool = imageObj.search_data2img(search_text)
            # |--------------------------------------------------------------------------------------------------------|
            
            # + Loading Log +
            log.AISearch_loading(count, function_name, page, search_text)
            
            if coord != False: # + Successfully Complete Process +
                
                # + Complete Log +
                log.AISearch_complete(function_name, page, search_text)
                return True
            else:
                
                # + Iterator and Sweeper+
                updown_page(count) if sweep == True else sleep(0.5)
                count += 1
        
        # + Failed Process +
        if count >= self.AI_loop_try:
            log.AISearch_failed(function_name, page, search_text)
        
        return False
    
    def search2coord(self, page: str, search_text: str) -> dict[str, int] | bool:
        
        # + Variables and Objects +
        count: int = 0
        log = Log()
        function_name: str = "AI-S2CC"
        
        # + Sweep Text Search +
        while count < self.AI_loop_try:
            
            # + ImageTools Object __init__ +
            imageObj = ImageTools(0, 0, self.resolution[0], self.resolution[1])
            
            # | Preprocessing Image Alternator |-----------------------------------------------------------------------|
            alternator = lambda num: num % 2 == 0
            if alternator(count):
                coord: dict[str, int] | bool = imageObj.search_data2img_hard(search_text)
            else:
                coord: dict[str, int] | bool = imageObj.search_data2img(search_text)
            # |--------------------------------------------------------------------------------------------------------|
            
            # + Loading Log +
            log.AISearch_loading(count, function_name, page, search_text)
            
            if coord != False: # + Successfully Complete Process +
                
                # + Complete Log +
                log.AISearch_complete(function_name, page, search_text)
                return coord
            else:
                
                # + Iterator and Sweeper +
                updown_page(count)
                count += 1
        
        # + Failed Process +
        if count >= self.AI_loop_try:
            log.AISearch_failed(function_name, page, search_text)
        
        return False
    
    def PERsearch2click(self, page: str, search_text: str, resolution: tuple[int],
                        increment_x: int = 20, increment_y: int = 20) -> None:
        
        # + Variables and Objects +
        count: int = 0
        log = Log()
        function_name: str = "AI-S2C-RES"
        
        # + Sweep Text Search +
        while count < self.AI_loop_try:
            
            # + ImageTools Object __init__ +
            imageObj = ImageTools(resolution[0], resolution[1], resolution[2], resolution[3])
            
            # | Preprocessing Image Alternator |-----------------------------------------------------------------------|
            alternator = lambda num: num % 2 == 0
            if alternator(count):
                coord: dict[str, int] | bool = imageObj.search_data2img_hard(search_text)
            else:
                coord: dict[str, int] | bool = imageObj.search_data2img(search_text)
            # |--------------------------------------------------------------------------------------------------------|
            
            # + Loading Log +
            log.AISearch_loading(count, function_name, page, search_text)
            
            if coord != False: # + Successfully Complete Process +
                
                # | Click Function |-----------------------------------------------------------------------------------|
                Cx: int = coord[0]
                Cy: int = coord[1] + resolution[0]
                GUI.click((Cx + increment_x), (Cy + increment_y))
                # |----------------------------------------------------------------------------------------------------|
                
                # + Complete Log +
                log.AISearch_complete(function_name, page, search_text)
                break
            else:
                
                # + Iterator +
                sleep(0.1)
                count += 1
        
        # + Failed Process +
        if count >= self.AI_loop_try:
            log.AISearch_failed(function_name, page, search_text)
        
        return False
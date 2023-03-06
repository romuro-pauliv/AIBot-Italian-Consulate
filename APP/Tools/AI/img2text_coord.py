# +--------------------------------------------------------------------------------------------------------------------|
# |                                                                                              APP.Tools.img2text.py |
# |                                                                                             Author: Pauliv, Rômulo |
# |                                                                                          email: romulopauliv@bk.ru |
# |                                                                                                    encoding: UTF-8 |
# +--------------------------------------------------------------------------------------------------------------------|


# | Imports |----------------------------------------------------------------------------------------------------------+
from Tools.Image.preprocessing import Preprocessing
import mss
import numpy as np
import pytesseract
import cv2
# |--------------------------------------------------------------------------------------------------------------------+

class ImageTools(object):
    def __init__(self, top: int, left: int, width: int, height: int) -> None:
        self.monitor: dict[str, int] = {
            "top": top, "left": left, "width": width, "height": height
        }
        self.image: np.ndarray = []
    
    def screenshot(self) -> np.ndarray:
        with mss.mss() as sct:
            self.image: np.ndarray = np.array(sct.grab(self.monitor))
            return np.array(sct.grab(self.monitor))
    
    def search_data2img(self, search_text: str) -> dict[str, int] | bool:
        self.screenshot()
        self.image = Preprocessing.high_contrast(self.image)
        
        data: dict[str] = pytesseract.image_to_data(self.image, output_type=pytesseract.Output.DICT)
                
        for i, word in enumerate(data['text']):
            if word.strip() == search_text:
                return data['left'][i], data['top'][i], data['width'][i], data['height'][i]
        return False
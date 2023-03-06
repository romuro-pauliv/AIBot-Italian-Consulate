# +--------------------------------------------------------------------------------------------------------------------|
# |                                                                                   APP.Tools.Image.preprocessing.py |
# |                                                                                             Author: Pauliv, Rômulo |
# |                                                                                          email: romulopauliv@bk.ru |
# |                                                                                                    encoding: UTF-8 |
# +--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
import cv2
import numpy as np
# |--------------------------------------------------------------------------------------------------------------------|

class Preprocessing(object):
    @staticmethod
    def high_contrast(image: np.ndarray) -> np.ndarray:
        image: np.ndarray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)                                 # Grayscale
        # image: np.ndarray = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]    # Thresholding
        
        return image
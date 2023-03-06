# +--------------------------------------------------------------------------------------------------------------------|
# |                                                                                                  APP.Tools.page.py |
# |                                                                                             Author: Pauliv, Rômulo |
# |                                                                                          email: romulopauliv@bk.ru |
# |                                                                                                    encoding: UTF-8 |
# +--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
from Tools.json.read_json import read_json
from time import sleep
import pyautogui as GUI
# |--------------------------------------------------------------------------------------------------------------------|

def updown_page(count: int) -> None:
    loops: int = read_json("Tools/json/data.json")['config']['tesseract-recognition-try']
    cycle: int = round(loops / 4, 0)
    
    if (0 <= count < cycle):
        GUI.press("down")
    elif (cycle <= count < 2*cycle):
        GUI.press("up")
    elif (2*cycle <= count < 3*cycle):
        GUI.press("down")
    elif (3*cycle <= count <= 4*cycle):
        GUI.press("up")
    
    sleep(0.1)
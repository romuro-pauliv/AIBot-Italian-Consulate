# +--------------------------------------------------------------------------------------------------------------------|
# |                                                                                                  APP.Tools.zoom.py |
# |                                                                                             Author: Pauliv, Rômulo |
# |                                                                                          email: romulopauliv@bk.ru |
# |                                                                                                    encoding: UTF-8 |
# +--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
import pyautogui as GUI
# |--------------------------------------------------------------------------------------------------------------------|

def zoom_in(times: int) -> None:
    for _ in range(0, times):
        GUI.hotkey("ctrl", "+")


def zoom_out(times: int) -> None:
    for _ in range(0, times):
        GUI.hotkey("ctrl", "-")
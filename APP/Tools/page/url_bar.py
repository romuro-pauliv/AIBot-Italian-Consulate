# +--------------------------------------------------------------------------------------------------------------------|
# |                                                                                          APP.Tools.page.url_bar.py |
# |                                                                                             Author: Pauliv, Rômulo |
# |                                                                                          email: romulopauliv@bk.ru |
# |                                                                                                    encoding: UTF-8 |
# +--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
import pyautogui as GUI
from Tools.json.read_json import read_json
from time import sleep
from log.pages.page_log import RequestTime
# |--------------------------------------------------------------------------------------------------------------------|

config_screen: dict[str] = read_json("Tools/json/data.json")["screen"]

url_bar_coord: list[int] = config_screen['url_coord']
resolution: list[str] = config_screen["resolution"]

def write_url_bar(url: str) -> None:
    GUI.click(url_bar_coord[0], url_bar_coord[1]), sleep(0.1)
    GUI.write(url), sleep(0.1)
    GUI.press("enter"), sleep(0.1)
    GUI.click(0, (resolution[1] - 20)), sleep(0.1)  # Return to HTML page
    
    count: int = 0
    total_count: int = 10
    while count < total_count:
        RequestTime.loadingRequest(count, total_count)
        sleep(1)
        count += 1
    
    RequestTime.completeRequest()


def request_time(total_secs: int = 10) -> None:
    count: int = 0
    total_count: int = total_secs
    while count < total_count:
        RequestTime.loadingRequest(count, total_count)
        sleep(1)
        count += 1
    
    RequestTime.completeRequest()
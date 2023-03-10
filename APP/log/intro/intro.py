# +--------------------------------------------------------------------------------------------------------------------|
# |                                                                                             APP.log.intro.intro.py |
# |                                                                                             Author: Pauliv, Rômulo |
# |                                                                                          email: romulopauliv@bk.ru |
# |                                                                                                    encoding: UTF-8 |
# +--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
from colorama import Fore, Style
from Tools.json.read_json import read_json
from time import sleep
from Tools.sound.play_beep import play_beep, play_alert
# |--------------------------------------------------------------------------------------------------------------------|

url: str = read_json("Tools/json/data.json")["urls"]["home-page"]

line: str = f"|{'-'*88}|"
text: dict[str] = {
    "header": f"AI OCR Tesseract {Fore.CYAN}{url}{Style.RESET_ALL}",
    "body": f"|> Bot Activate {Fore.YELLOW} [Y/N]: {Style.RESET_ALL}",
    "input_n": f"{Fore.RED} || DEVICE TERMINATED || {Style.RESET_ALL}",
    "invalid_input": f"{Fore.YELLOW} || INVALID INPUT [Y/N] || {Style.RESET_ALL}",
    "input_y": f"{Fore.GREEN} |> START DEVICE IN: {Style.RESET_ALL}"
}


def timer() -> None:
    seconds: int = 20
    
    while seconds > -1:
        real_time: int = 20 - seconds
        
        if real_time == 0:
            time_line: str = "|"*seconds
        else:
            time_line: str = "|"*(seconds)
            ster_line: str = "*"*(real_time)
        
        if real_time == 0:
            LINE: str = f"{Fore.GREEN}{time_line}{Style.RESET_ALL}"
        else:
            LINE: str = f"{Fore.GREEN}{time_line}{Fore.RED}{ster_line}{Style.RESET_ALL}"
        
        if seconds != 0:
            print(f"{text['input_y']}<{LINE}>", end="\r")
            play_beep()
        else:
            print(f"{text['input_y']}<{LINE}>")
            play_alert()
        sleep(1)
        seconds -= 1
        

def intro() -> None:
    print(f"{Fore.MAGENTA}{line}{Style.RESET_ALL}")
    print(f"{Fore.MAGENTA}| {text['header']}{' '*(len(line) - len(text['header']) + 6)}{Fore.MAGENTA}|")
    print(f"{line}{Style.RESET_ALL}")

def body() -> None:
    while True:
        input_yn: str = input(text["body"])
        
        if input_yn.lower() == "y":
            timer()
            break
        elif input_yn.lower() == "n":
            print(text["input_n"])
            exit()
        else:
            print(text["invalid_input"])


def _log_exec() -> None:
    intro(), body()
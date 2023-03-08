# +--------------------------------------------------------------------------------------------------------------------|
# |                                                                                         APP.log.pages.pages_log.py |
# |                                                                                             Author: Pauliv, Rômulo |
# |                                                                                          email: romulopauliv@bk.ru |
# |                                                                                                    encoding: UTF-8 |
# +--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
from colorama import Fore, Style
# |--------------------------------------------------------------------------------------------------------------------|

class PagesLogs(object):
    def __init__(self) -> None:
        self.line: str = f"|{'-'*88}|"
        
    def log(self, page_name: str) -> None:
        print(f"{Fore.CYAN}{self.line}")
        print(f"|{Fore.LIGHTYELLOW_EX}@{page_name}{' '*((len(self.line) - len(page_name))-3)}{Fore.CYAN}|")
        print(f"{Fore.CYAN}{self.line}")
    

class RequestTime(object):
    @staticmethod
    def loadingRequest(time: int, total_time: int) -> None:
        print(f"{Fore.LIGHTGREEN_EX}<#> {Fore.LIGHTMAGENTA_EX}Request time | {Fore.CYAN}SSC: {total_time - time}", end="\r")
    
    def completeRequest() -> None:
        print(f"{Fore.LIGHTGREEN_EX}<#> {Fore.LIGHTMAGENTA_EX}Request time | {Fore.CYAN}SSC: 0")
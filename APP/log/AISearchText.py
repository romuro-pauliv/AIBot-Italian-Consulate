# +--------------------------------------------------------------------------------------------------------------------|
# |                                                                                            APP.log.AISearchText.py |
# |                                                                                             Author: Pauliv, Rômulo |
# |                                                                                          email: romulopauliv@bk.ru |
# |                                                                                                    encoding: UTF-8 |
# +--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
from colorama import Fore, Style
from Tools.json.read_json import read_json
# |--------------------------------------------------------------------------------------------------------------------|

class Log:
    def __init__(self):
        self.AI_loop = read_json("Tools/json/data.json")["config"]["tesseract-recognition-try"]
        self.info_space = 27
        self.searchtext_space = 15
        self.percent_space = 3
        
    def _get_loading_line(self, count: int) -> str:
        off_line = "_" * (self.AI_loop - count)
        on_line = "|" * count if count != 0 else ""
        return f"{Fore.GREEN}|{Fore.GREEN}{on_line}{Fore.CYAN}{off_line}{Fore.GREEN}|{Style.RESET_ALL}"
    
    def _get_info_text(self, info: str, page: str, searchtext: str) -> str:
        return f"{Fore.GREEN}{page}{Fore.MAGENTA}@{info}{' ' * (self.info_space - (len(info)+len(page)))}-> " \
               f"{' ' * (self.searchtext_space - len(searchtext))}{Fore.YELLOW}[{searchtext}]"
    
    def AISearch_loading(self, count: int, info: str, page: str,searchtext: str) -> None:
        percent_int = int((count / self.AI_loop) * 100) if count != 0 else 0
        percent_text = f"{Fore.CYAN}{' ' * (self.percent_space - len(str(percent_int)))}{percent_int}%"
        info_text = self._get_info_text(info, page, searchtext)
        loading_line = self._get_loading_line(count)
        print(f"{info_text} {percent_text} {loading_line}", end="\r")
        
    def AISearch_complete(self, info: str, page: str, searchtext: str) -> None:
        info_text = self._get_info_text(info, page, searchtext)
        percent_text = f"{Fore.GREEN}100%"
        loading_line = f"{Fore.GREEN}{'|' * self.AI_loop}||"
        complete_text = f"{Fore.LIGHTGREEN_EX}COMPLETE"
        print(f"{info_text} {percent_text} {loading_line} {complete_text}{Style.RESET_ALL}")
    
    def AISearch_failed(self, info: str, page: str, searchtext: str) -> None:
        info_text = self._get_info_text(info, page, searchtext)
        percent_text = f"{Fore.RED}100%"
        loading_line = f"{Fore.RED}{'|' * self.AI_loop}||"
        complete_text = f"{Fore.LIGHTRED_EX}FAILED"
        print(f"{info_text} {percent_text} {loading_line} {complete_text}{Style.RESET_ALL}")
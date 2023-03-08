# +--------------------------------------------------------------------------------------------------------------------|
# |                                                                                         APP.Services.core.exec_.py |
# |                                                                                             Author: Pauliv, Rômulo |
# |                                                                                          email: romulopauliv@bk.ru |
# |                                                                                                    encoding: UTF-8 |
# +--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
from Services.AISearch.AISearch import AISearch
from Tools.json.read_json import read_json
from Tools.page.url_bar import write_url_bar, request_time
from Tools.sound.play_beep import play_alert
from log.pages.page_log import PagesLogs

from Services.Process.coord_calculation import flotation_resolution
# |--------------------------------------------------------------------------------------------------------------------|

pages_logs = PagesLogs()

search_text: dict[str] = read_json("Services/search_text.json")
credentials: dict[str] = read_json("Services/credentials.json")
config_data: dict[str] = read_json("Tools/json/data.json")

pg: dict[str] = {
    "root": "root",
    "login": "LoginITA",
    "home": ["HomeNA", "HomeITA"],
    "book": "PrenotaITA",
    "popup": "PopupITA"
}

def login_page_exec() -> bool:
    AIOBJ = AISearch()
    
    # | Data |---------------------------------------------------------------------------------------------------------|
    ConfirmHomePage: str = search_text["HomePage"]["confirmation"]["header-page-NA"]
    ConfirmLoginPage: str = search_text["Login"]["confirmation"]["header-page-ITA"]
    
    ST_email: str = search_text["Login"]["search-text"]["email-box"]
    ST_paswd: str = search_text["Login"]["search-text"]["password-box"]
    ST_submt: str = search_text["Login"]["search-text"]["submit-box"]
    
    URL_HomePage: str = config_data['urls']['home-page']
    # |----------------------------------------------------------------------------------------------------------------|
    
    # if in HomePage
    if AIOBJ.search2true(pg["root"], ConfirmHomePage):
        return True
    
    # if in Login Page
    elif AIOBJ.search2true(pg["root"], ConfirmLoginPage):
        pages_logs.log(pg["login"])
        # Input Crendentials and Log-In    
        AIOBJ.search2write(pg["login"], ST_email, credentials['email'])
        AIOBJ.search2write(pg["login"], ST_paswd, credentials['password'])
        AIOBJ.search2click(pg["login"], ST_submt)
        
        # if in HomePage 
        return True if AIOBJ.search2true(pg["root"], ConfirmHomePage) else False
    
    # if page not found
    else:
        write_url_bar(URL_HomePage)
        return False

def home_page_exec() -> bool:
    AIOBJ = AISearch()
    
    # | Data |---------------------------------------------------------------------------------------------------------|
    ConfirmHomePageITA: str = search_text["HomePage"]["confirmation"]["function-page-ITA"]
    ConfirmBookPageITA: str = search_text["PrenotaPage"]["confirmation"]["header-page-ITA"]
    
    ST_language: str = search_text["config"]["language"]
    ST_prenota: str = search_text["HomePage"]["search-text"]["prenota-box"]
    
    URL_HomePage: str = config_data['urls']['home-page']
    # |----------------------------------------------------------------------------------------------------------------|
    
    # | Reboot Function |----------------------------------------------------------------------------------------------|
    def reboot() -> None:
        write_url_bar(URL_HomePage)
        response_login: bool = login_page_exec()
        while response_login == False:
            response_login: bool = login_page_exec()
    # |----------------------------------------------------------------------------------------------------------------|
    
    # Change to ITALIAN language
    pages_logs.log(pg["home"][0])
    AIOBJ.search2click(pg["home"][0], ST_language, 10, 10), request_time(13)
    
    # if in ITA HomePage
    if AIOBJ.search2true(pg["root"], ConfirmHomePageITA, False):
        pages_logs.log(pg["home"][1])
        AIOBJ.search2click(pg["home"][1], ST_prenota)
        
        # if in ITA Prenota Page
        if AIOBJ.search2true(pg["book"], ConfirmBookPageITA):
            pages_logs.log(pg["book"])
            return True
        else:
            reboot()
            return False
        
    # if not found ITA HomePage
    else:
        reboot()
        return False

def prenota_page_exec() -> bool:
    AIOBJ = AISearch()
    
    # | Data |---------------------------------------------------------------------------------------------------------|
    URL_HomePage: str = config_data['urls']['home-page']
    
    ConfirmPopup: str = search_text['ErrorPopup']['confirmation']['in-text-popup']
    ConfirmRichiesta: str = search_text["RichiestaPage"]["confirmation"]["header-page-ITA"]
    
    ST_prenota: str = search_text['PrenotaPage']['search-text']['prenota-item-box']
    ST_popup: str = search_text['ErrorPopup']['confirmation']['in-text-popup']
    
    SCC_itemlist: str = search_text["PrenotaPage"]['search-cood']['itemlist-ITA']
    
    CONF_popupButton_x: int = config_data['config']['popup-button']['x']
    CONF_popupButton_y: int = config_data['config']['popup-button']['y']
    # |----------------------------------------------------------------------------------------------------------------|
    
    # | Reboot Function |----------------------------------------------------------------------------------------------|
    def reboot() -> None:
        write_url_bar(URL_HomePage)
        response_login: bool = login_page_exec()
        while response_login == False:
            response_login: bool = login_page_exec()

        response_home: bool = home_page_exec()
        while response_home == False:
            response_home: bool = home_page_exec()
    # |----------------------------------------------------------------------------------------------------------------|
    
    item_coord: bool | tuple[int] = AIOBJ.search2coord(pg["book"], SCC_itemlist)
    
    if item_coord != False:
        # | Personalized Item Resolution 
        data: tuple[int] = flotation_resolution(item_coord)
    
        # Click in Prenota
        AIOBJ.PERsearch2click(pg["book"], ST_prenota, data, 10, 10)
        
        # If PopUp Alert
        if AIOBJ.search2true(pg["book"], ConfirmPopup):
            pages_logs.log(pg["popup"])
            play_alert()
            AIOBJ.search2click(pg["book"], ST_popup, CONF_popupButton_x, CONF_popupButton_y)
            return False
        
        # If Richiesta Page Enter
        elif AIOBJ.search2true(pg["book"], ConfirmRichiesta):
            play_alert()
            return True
        else:
            reboot()
            return False
    else:
        reboot()
        return False
        
def execution() -> None:
    response_login: bool = login_page_exec()
    while response_login == False:
        response_login: bool = login_page_exec()
    
    response_home: bool = home_page_exec()
    while response_home == False:
        response_home: bool = home_page_exec()
    
    response_prenota: bool = prenota_page_exec()
    while response_prenota == False:
        response_prenota: bool = prenota_page_exec()
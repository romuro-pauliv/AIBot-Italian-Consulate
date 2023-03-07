# +--------------------------------------------------------------------------------------------------------------------|
# |                                                                                         APP.Services.core.exec_.py |
# |                                                                                             Author: Pauliv, Rômulo |
# |                                                                                          email: romulopauliv@bk.ru |
# |                                                                                                    encoding: UTF-8 |
# +--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
from Services.AISearch.AISearch import AISearch
from Tools.json.read_json import read_json
from Tools.page.zoom import zoom_in, zoom_out
from Tools.page.url_bar import write_url_bar
from time import sleep
# |--------------------------------------------------------------------------------------------------------------------|

search_text: dict[str] = read_json("Services/search_text.json")
credentials: dict[str] = read_json("Services/credentials.json")
config_data: dict[str] = read_json("Tools/json/data.json")

def login_page_exec() -> bool:
    AIOBJ = AISearch()
    
    # if in HomePage
    if AIOBJ.search2true("root", search_text["HomePage"]["confirmation"]["header-page-NA"]):
        return True
    
    # if in Login Page
    elif AIOBJ.search2true("root", search_text["Login"]["confirmation"]["header-page-ITA"]):
        # Input Crendentials and Log-In    
        AIOBJ.search2write("LoginPageITA", search_text["Login"]["search-text"]["email-box"], credentials['email'])
        AIOBJ.search2write("LoginPageITA", search_text["Login"]["search-text"]["password-box"], credentials['password'])
        AIOBJ.search2click("LoginPageITA", search_text["Login"]["search-text"]["submit-box"])
        
        # if in HomePage 
        return True if AIOBJ.search2true("root", search_text["HomePage"]["confirmation"]["header-page-NA"]) else False
    
    # if page not found
    else:
        write_url_bar(config_data['urls']['home-page'])
        return False

def home_page_exec() -> bool:
    AIOBJ = AISearch()
    
    # Change to ITALIAN language
    AIOBJ.search2click("HomePageNA", search_text["config"]["language"], 10, 10), sleep(10)
    
    # if in ITA HomePage
    if AIOBJ.search2true("root", search_text["HomePage"]["confirmation"]["function-page-ITA"], False):
        AIOBJ.search2click("HomePageITA", search_text["HomePage"]["search-text"]["prenota-box"])
        
        # if in ITA Prenota Page
        if AIOBJ.search2true("BookPageITA", search_text["PrenotaPage"]["confirmation"]["header-page-ITA"]):
            return True
        else:
            write_url_bar(config_data['urls']['home-page']), sleep(10)
            # Verify if in LoginPage or HomePage and adjust bot
            login_page_exec()
            return False
    
    # if not found ITA HomePage
    else:
        write_url_bar(config_data['urls']['home-page'])
        # Verify if in LoginPage or HomePage and adjust bot
        login_page_exec()
        return False


def prenota_page_exec() -> bool:
    AIOBJ = AISearch()
    
    item_coord: bool | tuple[int] = AIOBJ.search2coord("PrenotaPage", search_text["PrenotaPage"]['search-cood']['itemlist-ITA'])
    
    if item_coord != False:
        # | Personalized Item Resolution 
        xy: dict[str, int] = {"x": 0, 'y': (item_coord[1]-50)}
        len_xy: dict[str, int] = {"x": config_data['screen']['resolution'][0], "y": 150}
        data: tuple[int] = (xy['y'], xy['x'], len_xy['x'], len_xy["y"])
    
        # Click in Prenota
        AIOBJ.PERsearch2click("PrenotaPage", search_text['PrenotaPage']['search-text']['prenota-item-box'], data, 10, 10)
        if AIOBJ.search2true("PrenotaPage", search_text['ErrorPopup']['confirmation']['in-text-popup']):
            AIOBJ.search2click("PrenotaPage", search_text['ErrorPopup']['confirmation']['in-text-popup'], 160, 100)
            return False
    
    else:
        write_url_bar(config_data['urls']['home-page'])
        # Verify if in LoginPage or HomePage and adjust bot
        response_login: bool = login_page_exec()
        while response_login == False:
            response_login: bool = login_page_exec()
    
        response_home: bool = home_page_exec()
        while response_home == False:
            response_home: bool = home_page_exec()
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
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
# |--------------------------------------------------------------------------------------------------------------------|

search_text: dict[str] = read_json("Services/search_text.json")
credentials: dict[str] = read_json("Services/credentials.json")
config_data: dict[str] = read_json("Tools/json/data.json")

def login_page_exec() -> bool:
    AIOBJ = AISearch()
    if AIOBJ.search2true("root", search_text['home-page-confirmation']['header-page-NA'], False):
        return True
    
    elif AIOBJ.search2true("root", search_text['login-page-confirmation']["header-page-ITA"], False):
        AIOBJ.search2write("LoginPageITA", search_text["login-page"]['email-box'], credentials['email'])
        AIOBJ.search2write("LoginPageITA", search_text["login-page"]['password-box'], credentials['password'])
        AIOBJ.search2click("LoginPageITA", search_text["login-page"]['submit'])    
        return True if AIOBJ.search2true("root", search_text['home-page-confirmation']['header-page-NA'], False) else False
    
    else:
        write_url_bar(config_data['urls']['home-page'])
        return False

def home_page_exec() -> bool:
    AIOBJ = AISearch()
    AIOBJ.search2click("HomePageNA", search_text['page-config']['language'], 10, 10)
    if AIOBJ.search2true("root", search_text['home-page-confirmation']['function-page-ITA'], False):
        AIOBJ.search2click("HomePageITA", search_text['home-page-confirmation']['function-page-ITA'])
        return True
    else:
        write_url_bar(config_data['urls']['home-page'])
        return False
    
    
    
def execution() -> None:
    response_login: bool = login_page_exec()
    while response_login == False:
        response_login: bool = login_page_exec()
    
    response_home: bool = home_page_exec()
    while response_home == False:
        response_home: bool = home_page_exec()
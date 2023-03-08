# +--------------------------------------------------------------------------------------------------------------------|
# |                                                                                  APP.Services.coord_calculation.py |
# |                                                                                             Author: Pauliv, Rômulo |
# |                                                                                          email: romulopauliv@bk.ru |
# |                                                                                                    encoding: UTF-8 |
# +--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
from Tools.json.read_json import read_json
# |--------------------------------------------------------------------------------------------------------------------|

resolution: dict[str] = read_json("Tools/json/data.json")["screen"]["resolution"]
config: dict[str, dict[str]] = read_json("Tools/json/data.json")["config"]

def flotation_resolution(coord: tuple[int]) -> tuple[int]:
    xy: dict[str, int] = {"x": 0, "y": (coord[1]-config['prenota-function']["top"])}
    len_xy: dict[str, int] = {"x": resolution[0], "y": config['prenota-function']["area"]}
    
    return (xy['y'], xy['x'], len_xy['x'], len_xy['y'])

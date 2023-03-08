# +--------------------------------------------------------------------------------------------------------------------|
# |                                                                                       APP.Tools.Sound.play_beep.py |
# |                                                                                             Author: Pauliv, Rômulo |
# |                                                                                          email: romulopauliv@bk.ru |
# |                                                                                                    encoding: UTF-8 |
# +--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
from pydub import AudioSegment
from pydub.playback import play

from Tools.json.read_json import read_json
# |--------------------------------------------------------------------------------------------------------------------|

dir: str = read_json("Tools/json/data.json")["Audio"]["dir"]

def play_alert() -> None:
    song = AudioSegment.from_wav(dir)
    play(song)

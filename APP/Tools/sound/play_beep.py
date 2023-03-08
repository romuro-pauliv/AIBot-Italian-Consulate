# +--------------------------------------------------------------------------------------------------------------------|
# |                                                                                       APP.Tools.Sound.play_beep.py |
# |                                                                                             Author: Pauliv, Rômulo |
# |                                                                                          email: romulopauliv@bk.ru |
# |                                                                                                    encoding: UTF-8 |
# +--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
import os
import subprocess
from pydub import AudioSegment
from pydub.playback import play

from Tools.json.read_json import read_json
# |--------------------------------------------------------------------------------------------------------------------|

dir: str = read_json("Tools/json/data.json")["Audio"]["dir"]

def play_alert() -> None:
    song = AudioSegment.from_wav(dir)
    with open(os.devnull, 'w') as devnull:
        subprocess.Popen(['ffplay', '-nodisp', '-autoexit', '-loglevel', 'quiet', '-i', dir], stdout=devnull, stderr=devnull)
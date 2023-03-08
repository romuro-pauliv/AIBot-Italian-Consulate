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
from time import sleep

from Tools.json.read_json import read_json
# |--------------------------------------------------------------------------------------------------------------------|


def play_alert() -> None:
    dir: str = read_json("Tools/json/data.json")["Audio"]["dir"]
    song = AudioSegment.from_wav(dir)
    with open(os.devnull, 'w') as devnull:
        subprocess.Popen(['ffplay', '-nodisp', '-autoexit', '-loglevel', 'quiet', '-i', dir], stdout=devnull, stderr=devnull)
        

def play_danger() -> None:
    dir: str = read_json("Tools/json/data.json")["Audio"]["dirX"]
    song = AudioSegment.from_mp3(dir)
    with open(os.devnull, 'w') as devnull:
        subprocess.Popen(['ffplay', '-nodisp', '-autoexit', '-loglevel', 'quiet', '-i', dir], stdout=devnull, stderr=devnull)
        

def play_danger_loop() -> None:
    while True:
        play_danger(), sleep(15)
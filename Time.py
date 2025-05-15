"""Time.py"""

from initializer_functions import *
from datetime import datetime

def getTime():
    time = datetime.now().strftime("%H:%M")
    print_and_speak(f"At the current moment, the time is {time}")

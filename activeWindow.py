"""activeWindow.py"""

from pygetwindow import *
import time
from initializer_functions import *

def is_vscode_active():
    active_window = getActiveWindow()
    if active_window:
        return 'Visual Studio Code' in active_window.title
    return False

def ActiveWindowCheck():
    # Pause if VS Code is not active
    if not is_vscode_active():
        while not is_vscode_active():
            time.sleep(1)  #Check every second
        speak("Welcome back Master!")


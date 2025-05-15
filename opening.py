import os
import psutil
import webbrowser
from time import sleep
import pyautogui
from initializer_functions import *

words = ["Jarvis","open","launch"," ","the", "close","please","kindly","do","what", "who","can","you","is", "will"]
def cleanQuery(query):
    for word in words:
        query = query.replace(word,"")
    return query

dictapp = {"commandprompt":"cmd", "vscode":"code", "chrome":"chrome", "wps office":"wps", "notepad":"notepad", "paint":"mspaint", "fileexplorer":"explorer" }

def openApp(query):
    speak("Opening Master, Please wait...")
    query = cleanQuery(query)
    if ".com" in query or ".org" in query or ".in" in query or ".net" in query or ".org" in query or ".gov" in query:
        webbrowser.open(f"https://www.{query}")
        sleepStateHandler()
    elif query in dictapp:
        os.system(f"start {dictapp[query]}")
        sleepStateHandler()
    else:
        speak("I am not able to open this application, Master!")

def closeApp(query):
    query = cleanQuery(query)
    if "tab" in query:
        speak("Closing current tab...")
        pyautogui.hotkey("ctrl", "w")
    elif query in dictapp:
        app_name = dictapp[query]
        speak(f"Closing {query}, Master. Please wait...")
        closed = False
        
        for proc in psutil.process_iter(['name']):
            if app_name.lower() in proc.info['name'].lower():
                proc.terminate()  # Gracefully terminate
                closed = True
                break

        if not closed:
            speak(f"Couldn't find {query} running, Master.")
    else:
        speak("I am not able to close this application, Master!")
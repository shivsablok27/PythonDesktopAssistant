"""main.py"""

from initializer_functions import *
from searchQuery import *
from openweatherapi import *
from Time import *
#from activeWindow import *
from opening import *

def wakeStateHandling():
    while True:
        #ActiveWindowCheck()

        #____________General Queries____________
        query = takeCommand()
        if "go to sleep" in query:
            sleepStateHandler()
        elif "hello" in query:
            speak("Hello Master, How are you?")
        elif "i am fine" in query:
            speak("Glad to know this Master!")
        elif "how are you" in query:
            speak("I am perfect Master, Thankyou!")
        elif "thank you" in query:
            speak("You are always welcome Master!")
        elif "exit" in query:
            speak("Sure Master, Exiting the Desktop Assistant...")
            exit()

        #_____________Opening & Closing Queries_______________
        elif "open" in query or "launch" in query:
            openApp(query)
        elif "close" in query:
            closeApp(query)
            
        #_____________Online Queries_______________
        elif "google" in query:
            searchGoogle(query)
        elif "youtube" in query:
            searchYoutube(query)
        elif "wikipedia" in query:
            searchWikipedia(query)
        elif "temperature" in query:
            getTemperature("Agra")
        elif "weather" in query:
            getWeather("Agra") 
        elif "time" in query:
            getTime() 
        
   
if __name__ == "__main__":
    while True:
        initializer()
        wakeStateHandling()
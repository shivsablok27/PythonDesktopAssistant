"""initializer_functions.py"""

import pyttsx3
import speech_recognition as sr
import datetime

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 150)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def print_and_speak(text):
    print(text)
    speak(text)

def takeCommand():
    r = sr.Recognizer() 
    with sr.Microphone() as source:
        print("Listening in active mode...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,7)
        
    try:
        print("Understanding...")
        query = r.recognize_google(audio, language = "en-in")
        print(f"You said: {query}\n")
    except Exception as e:
        speak("I am not able to listen Master, Could you please repeat?")
        return "None"
    
    return query.lower()

def greetMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Master!")
    elif hour>=12 and hour<16:
        speak("Good Afternoon Master!")
    else:
        speak("Good Evening Master!")

def initializer():
    print("Listening in sleep mode...")
    while True:
        r = sr.Recognizer() 
        with sr.Microphone() as source:
            r.pause_threshold = 1
            r.energy_threshold = 300
            audio = r.listen(source,0,7)
            try:
                query = r.recognize_google(audio, language = "en-in")
                if "wake up" in query:
                    greetMe()
                    speak("How can i assist you?")
                    break
                elif "exit" in query:
                    speak("Sure Master, Exiting the Desktop Assistant...")
                    exit()
            except Exception as e:
                pass

def sleepStateHandler():
    speak("I am gonna sleep master, wake me when needed!")
    print("Listening in sleep mode...")
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.pause_threshold = 1
            r.energy_threshold = 300
            audio = r.listen(source,0,7)
            try:
                query = r.recognize_google(audio, language = "en-in")
                if "wake up" in query:
                    speak("I am here master, how can i assist you?")
                    break
                elif "exit" in query:
                    speak("Sure Master, Exiting the Desktop Assistant...")
                    exit()
            except Exception as e:
                pass

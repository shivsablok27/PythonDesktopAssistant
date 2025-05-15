"""searchQuery.py"""

from initializer_functions import *
import wikipedia as wiki
import pywhatkit
import webbrowser

words = ["Jarvis","on","search","wikipedia","google","youtube",
         "please","kindly","do","what", "who","can","you","is", "will"]

def cleanQuery(query):
    for word in words:
        query = query.replace(word,"")
    return query

def searchGoogle(query):
    speak("Ok Master!!")
    query = cleanQuery(query)
    speak("This is what I found on google !!!")

    try:
        pywhatkit.search(query)
        result = wiki.summary(query, sentences = 1)
        speak(result)
        sleepStateHandler()
    except:
        speak("No speakable output available!!!")

def searchYoutube(query):
    speak("Ok Master!!")
    query = cleanQuery(query)
    speak("Here's what i found for your search!!!")

    web = "https://www.youtube.com/results?search_query=" + query
    #webbrowser.open(web)
    pywhatkit.playonyt(query)  #play first video of youtube search in different tab
    sleepStateHandler()

def searchWikipedia(query):
    speak("Ok Master!!")
    query = cleanQuery(query)
    speak("Searching on Wikipedia !!!")
    try:
        result = wiki.summary(query, sentences = 2)
        speak("According to wikipedia...")
        print_and_speak(result)
    except Exception as e:
        print_and_speak("Nothing available Master!!")
    

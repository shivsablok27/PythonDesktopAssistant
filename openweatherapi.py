"""openweatherapi.py"""

from initializer_functions import *
import requests

def getTemperature(city):
    api_key = "dd03bc2c48416e05bbda57abe989d42c"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "q=" + city + "&appid=" + api_key + "&units=metric"
    response = requests.get(complete_url)
    data = response.json()

    if data.get("cod") == 200:  # Check if request was successful
        main = data.get("main")
        if main is not None:  # Ensure 'main' is not None
            temp = main.get("temp")
            if temp is not None:  # Ensure 'temp' is not None
                print_and_speak(f"Temperature of {city} is {temp} degrees Celsius")
            else:
                print_and_speak("Temperature data not found in response")
        else:
            print_and_speak("Main data not found in response")
    else:
        print_and_speak("City Not Found Master")

def getWeather(city):
    api_key = "dd03bc2c48416e05bbda57abe989d42c"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "q=" + city + "&appid=" + api_key + "&units=metric" 
    response = requests.get(complete_url)
    data = response.json()

    if data.get("cod") == 200: 
        weather_list = data.get("weather")
        if weather_list: 
            weather = weather_list[0]
            main_weather = weather.get("main")
            description_weather = weather.get("description")
            if main_weather is not None and description_weather is not None: 
                print_and_speak(f"Weather of {city} is like : {main_weather}, {description_weather}")
            else:
                print_and_speak("Weather Description data not found in response")
        else:
            print_and_speak("Weather list not found in response")
    else:
        print_and_speak("City Not Found Master")

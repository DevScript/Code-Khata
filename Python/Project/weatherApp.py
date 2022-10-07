import requests
from termcolor import colored
import json
import os
import time

def getWeather(city):
    url = "https://weatherapi-com.p.rapidapi.com/current.json"

    querystring = {"q":city}

    headers = {
        "X-RapidAPI-Key": "37620eccc1msha8766c22b64e086p1c29fdjsn89264391a5cc",
        "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.text
    else:
        print(colored("\nSomething went wrong!\n", 'white', 'on_red'))
        time.sleep(2)
        welcome()
    return response.text

def welcome():
    os.system('cls')
    print(colored('\n~ Hacktoberfest 2022!\n', 'magenta'))
    print(colored(" Welcome to the Weather App \n", 'green', attrs=['reverse', 'blink']))
    print(colored("1. Get Weather", 'green'))
    print(colored("2. Exit", 'yellow'))
    choice = input("\nEnter your choice: ")
    if choice == "1":
        cityName = input("Enter city name: ")
        weather = getWeather(cityName)
        temp_c = colored(' ' + str(json.loads(weather)['current']['temp_c']) + '\N{DEGREE SIGN}C ', 'white', 'on_blue')
        temp_f = colored(' ' + str(json.loads(weather)['current']['temp_f']) + ' F ', 'white', 'on_cyan')
        temprature =  str(temp_c) + ' | ' + str(temp_f)
        condition = colored(' ' + str(json.loads(weather)['current']['condition']['text']) + ' ', 'grey', 'on_white')
        print('\n'+temprature + ' | ' + condition+'\n')
        newChoice = input("Search again? ("+colored('y', 'green')+'/'+colored('n','red') + "): ")
        if newChoice == 'y':
            welcome()
        else:
            exit()
    elif choice == "2":
        print(colored("\nBye!", 'cyan'))
        exit()
    else:
        print(colored('\nInvalid Input!', 'red'))
        time.sleep(1)
        welcome()

welcome()


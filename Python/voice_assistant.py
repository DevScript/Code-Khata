import pyttsx3                          # pip install pyttsx3
import speech_recognition as sr         # pip install SpeechRecognition
import datetime
import wikipedia
import webbrowser
import os
import random

engine = pyttsx3.init('sapi5')      # sapi5 for windows, nsss for mac and espeak for other platforms
voices = engine.getProperty('voices')  # returns list of voices

# print(voices[1].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if (hour >= 0 and hour < 12):
        speak('Good Morning!')
    elif (hour >= 12 and hour < 18):
        speak('Good Afternoon!')
    else:
        speak('Good Evening!')

    speak('I am Jarvis Sir, I am working for Waqar bhai. Please tell me how may I help you')


def takeCommand():
    # It takes microphone input from the user and returns string output, microphone input requires PyAudio
    # pip install pyaudio

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1  # Means it can have a 1 second gap while speaking
        r.energy_threshold = 300  # minimum audio energy to consider for recording
        r.adjust_for_ambient_noise(source, duration = 1)
        audio = r.listen(source)                               #instance of AudioData

        try:
            print('Recognizing...')
            query = r.recognize_google(audio, language='en-US')
            print(f'User Said: {query}\n')
        except Exception as e:
            print(e)
            print('Say that again please...')
            query = takeCommand().lower()
            return query;
        return query;


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'your name' in query:
            speak('My name is Jarvis')
        elif 'how are you' in query:
            speak('I am fine')
        elif 'who are you' in query:
            speak('I am Jarvis working for my friend Waqar Bhai')
        elif 'waqar' in query:
            speak('Waqar bhai is a good person. He was born on 23rd february 2000. He is studying ' +
                  'software engineering at mehran university of engineering and technology. He loves ' +
                  'coding and pubg. He is such a nice person. He is my friend and I am working for him.')
        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=2)
            speak('According to wikipedia')
            print(results)
            speak(results)
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\ND.COM\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'play song' in query:
            music_dir = 'D:\\MLSA Event\\songs'
            songs = os.listdir(music_dir)  # returns the list of files inside that directory
            # print(songs)
            os.startfile(
                os.path.join(music_dir, songs[random.randrange(0, 3)]))  # generating random index to play random song
        elif ('add' or 'addition') in query:
            speak("enter first number")
            num1 = float(input("Enter First No: "))
            speak("enter second number")
            num2 = float(input("Enter Second No: "))
            print(f"Ans = {num1+num2}")
            speak(f"The addition of {num1} and {num2} is {num1+num2}")
        elif ('subtract' or 'subtraction') in query:
            speak("enter first number")
            num1 = float(input("Enter First No: "))
            speak("enter second number")
            num2 = float(input("Enter Second No: "))
            print(f"Ans = {num1-num2}")
            speak(f"The subtraction of {num1} and {num2} is {num1-num2}")
        elif ('multiply' or 'multiplication') in query:
            speak("enter first number")
            num1 = float(input("Enter First No: "))
            speak("enter second number")
            num2 = float(input("Enter Second No: "))
            print(f"Ans = {num1*num2}")
            speak(f"The multiplication of {num1} and {num2} is {num1*num2}")
        elif ('divide' or 'division') in query:
            speak("enter first number")
            num1 = float(input("Enter First No: "))
            speak("enter second number")
            num2 = float(input("Enter Second No: "))
            print(f"Ans = {num1/num2}")
            speak(f"The division of {num1} and {num2} is {num1/num2}")

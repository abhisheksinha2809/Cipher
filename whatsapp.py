import pywhatkit
import pyttsx3
import datetime
import speech_recognition
import webbrowser
from bs4 import BeautifulSoup
from time import sleep
import os
from datetime import timedelta
from datetime import datetime

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate", 170)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0, 4)

    try:
        print("Understanding..")
        query = r.recognize_google(audio, language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query


strTime = int(datetime.now().strftime("%H"))
update = int((datetime.now() + timedelta(minutes=1)).strftime("%M"))


def sendMessage():
    speak("Who do you want to message")
    a = takeCommand().lower()
    if a == "abhishek":
        speak("Whats the message")
        message = takeCommand().lower()
        pywhatkit.sendwhatmsg("+919057079613", message, time_hour=strTime, time_min=update)
    elif a == 2:
        pass

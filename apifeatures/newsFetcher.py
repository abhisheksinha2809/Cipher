import pyttsx3
import requests
import speech_recognition as sr
import json
import time


#
# url = ('https://newsapi.org/v2/top-headlines?'
#        'country = in&'
#        'apiKey = 8969ef45f64047d1a83d74eb19504c9d')
#
# url += '8969ef45f64047d1a83d74eb19504c9d'
#
# engine = pyttsx3.init()
#
# rate = engine.getProperty('rate')
# engine.setProperty('rate', rate + 10)
#
# volume = engine.getProperty('volume')
# engine.setProperty('volume', volume - 0.60)
#
# sound = engine.getProperty('voices')
# engine.setProperty('voice', 'sound[1].id')
#
# response = ''
#
# try:
#     response = requests.get(url)
# except:
#     engine.say("Sorry sir, cannot access the link right now, please check your internet")
#
# news = json.loads(response.text)
#
# for new in news['articles']:
#     print(str(new['title']), "\n\n")
#     engine.say(str(new['title']))
#     engine.runAndWait()
#     print(str(new['description']), "\n\n")
#     engine.say(str(new['description']))
#     engine.runAndWait()
#     time.sleep(2)
#

def NewsFromBBC():

    # r = sr.Recognizer()
    #
    # with sr.Microphone() as source:
    #     print("Listening...")
    #     r.pause_threshold = 1
    #     audio = r.listen(source)
    #
    # try:
    #     print("Recognizing...")
    #     query = r.recognize_google(audio, language='en-us')
    #     print(f"User said: {query}\n")
    # except Exception as e:
    #     print("Sorry, say that again please")

    query_params = {
        "source": "bbc-news",
        "sortBy": "top",
        "apiKey": "8969ef45f64047d1a83d74eb19504c9d"
    }
    main_url = "https://newsapi.org/v1/articles"
    res = requests.get(main_url, params=query_params)
    open_bbc_page = res.json()
    article = open_bbc_page["articles"]
    results = []
    for ar in article:
        results.append(ar["title"])
    for i in range(len(results) - 5):
        # if "stop reading" in query:
        #     break
        print(i + 1, results[i])
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.Spvoice")
    speak.Speak(results)


if __name__ == "__main__":
    NewsFromBBC()

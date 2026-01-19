import speech_recognition as sr
import os 
import webbrowser
import pyttsx3
import music_library
import requests

engine=pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()
def processcommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")

    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1]
        link = music_library.music[song]
        webbrowser.open(link)
    elif any(word in c.lower() for word in ["news", "new", "headlines"]):
        speak("Opening news")
        webbrowser.open("https://news.google.com")

        speak("Here are the top headlines")

        response = requests.get(
            "https://newsapi.org/v2/top-headlines?country=in&apiKey=YOUR_API_KEY"
        )

        if response.status_code == 200:
            articles = response.json().get("articles", [])
            for article in articles[:5]:
                title = article.get("title")
                if title:
                    speak(title)
        else:
            speak("Sorry, I could not fetch the news")


if __name__=="__main__":
    speak("Initialising Jarvis ")
    while True:
        # Litsen for the wake word Jarvis 
        # obtain audio from the microphone
        r = sr.Recognizer()
            
        print("Recognising....")
        # recognize speech using Sphinx
        try:
            with sr.Microphone() as source:
                print("Litsening....")
                audio = r.listen(source,timeout=5,phrase_time_limit=3)
            word= r.recognize_google(audio)
            if(word.lower() in ["jarvis","jarviss","jarves","jar-vis","jarv-is","jervis","jarvas"]):
                speak("Ya")
                #litsen for command 
                with sr.Microphone() as source:
                    print("Jarvis Active")
                    audio = r.listen(source,)
                    command= r.recognize_google(audio)

                    print(command)
                    processcommand(command)


        except Exception as e:
            print(f"Error; {e}")
import speech_recognition as sr
import webbrowser
import pyttsx3
import requests
import music_library

engine = pyttsx3.init()
r = sr.Recognizer()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processcommand(c):
    c = c.lower()

    if "open google" in c:
        webbrowser.open("https://google.com")

    elif "open youtube" in c:
        webbrowser.open("https://youtube.com")

    elif "open linkedin" in c:
        webbrowser.open("https://linkedin.com")

    elif "open facebook" in c:
        webbrowser.open("https://facebook.com")

    elif c.startswith("play"):
        song = c.replace("play", "").strip()
        if song in music_library.music:
            webbrowser.open(music_library.music[song])
        else:
            speak("Song not found")

    elif any(word in c for word in ["news", "headlines"]):
        speak("Opening news")
        webbrowser.open("https://news.google.com")

    else:
        # Open ANY website using Google search
        search_url = f"https://www.google.com/search?q={c}"
        webbrowser.open(search_url)


if __name__ == "__main__":
    speak("Initializing Jarvis")

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for wake word...")
                r.adjust_for_ambient_noise(source, duration=0.5)
                audio = r.listen(source)

            word = r.recognize_google(audio).lower()
            print("Heard:", word)

            if word in ["jarvis", "jarviss", "jarves", "jervis", "jarvas"]:
                speak("Yes")
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    r.adjust_for_ambient_noise(source, duration=0.5)
                    audio = r.listen(source)

                command = r.recognize_google(audio)
                print("Command:", command)
                processcommand(command)

        except sr.UnknownValueError:
            pass  # ignore unrecognized speech

        except Exception as e:
            print("Error:", e)

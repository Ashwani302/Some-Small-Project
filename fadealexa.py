import webbrowser
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import os




engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices') #details of current voice
#print(voices[1].id)
"""There are three voice available in my pc i.e.0,1,2"""
engine.setProperty('voice', voices[2].id) #change voice[] to set different voice


def speak(audio):
    engine.say(audio)
    engine.runAndWait() #speech audible because of this command


def wishme():
    hr = int(datetime.datetime.now().hour)
    if hr>= 0 and hr>=12:
        speak("Good Morning")
    elif hr >= 12 and hr >=18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    
    speak("I am Fade. Please tell me how may i help you")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        take = r.recognize_google(audio, language='en-in')#using google to recognize
        print(f"Said by user: {take}")
    except Exception as e:
        print("Please say it again...")
        return "None"   #none string will be returned
    return take



if __name__ == "__main__":
    wishme()
    takecommand()
    while True:
        take = takecommand().lower()  #this convert taken command into lower case
        if 'wikipedia' in take:
            speak("Searching Wikipedia...")
            result = wikipedia.summary(take, sentences=2)
            speak("Wikipedia says")
            print(result)
            speak(result)
        elif 'open youtube' in take:
            webbrowser.open("youtube.com")
        elif 'open google' in take:
            webbrowser.open("google.com")
        elif 'play music' in take:
            speak("Play top 50 global music")
            webbrowser.open("https://open.spotify.com/playlist/37i9dQZEVXbMDoHDwVN2tF?si=24db68d4d9e94d49")
        elif 'the time' in take:
            a_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The Time is{a_time}")
        elif 'open visual studio ' in take:
            visualPath = "C:\\Users\\ashwa\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(visualPath)
        elif 'open code' in take:
            visualPath = "C:\\Users\\ashwa\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(visualPath)
        elif 'pycharm' in take:
            charmPath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2022.1.3\\bin\pycharm64.exe"
            os.startfile(charmPath)
        elif 'exit' in take:
            break
        elif 'quit' in take:
            break
        elif 'close' in take:
            break
        elif 'anime' in take:
            webbrowser.open("https://yugen.to/")
        elif 'valorant' in take:
            valorantPath = "E:\\Riot Games\\Riot Client\\RiotClientServices.exe"
            os.startfile(valorantPath)
        elif 'open spotify' in take:
            webbrowser.open("https://open.spotify.com/")
        elif 'open brave' in take:
            bravePath = "C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
            os.startfile(bravePath)
        

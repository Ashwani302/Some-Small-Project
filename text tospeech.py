import requests

def speak(str):
    from win32com.client import Dispatch

    speak = Dispatch("SAPI.SpVoice")

    speak.Speak(str)
while(True):
    choice = 0
    print("1.URL\n""2.Type anything\n")
    choice = int(input("Enter 1 or 2 and 3 to stop: "))
    if choice ==1:
        if __name__ == '__main__':
            url = input('Enter News API link: ')
            speak("Lets begin")
            response = requests.get(url)
            a = response.json()
            speak(a)
            speak("Thanks for listening")
    elif choice ==2:
        b = input("Enter anything you want to SAPI to speak: ")
        speak(b)
    else:
        speak("Exiting")
        break

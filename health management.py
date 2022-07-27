from pygame import mixer
from datetime import datetime
from time import time


def audio(start, stopper):
    mixer.init()
    mixer.music.load(start)
    mixer.music.play()
    while True:
        a = input()
        if a == stopper:
            mixer.music.stop()
            break


def log(text):
    with open("music.txt", "a") as f:
        f.write(f"{text} {datetime.now()}\n")


if __name__ == '__main__':
    a_water = time()
    a_eye = time()
    a_excersie = time()
    watertime = 50*60
    eyetime = 30*60
    execrisetime =45*60

    while True:
        if time() - a_water > watertime:
            print("Its time to drink water. To stop Enter 'drank'. ")
            audio('water.mp3.mp3', 'drank')
            a_water = time()
            log("Drink water at ")
        if time() - a_eye > eyetime:
            print("Its time to rub your eye. To stop Enter 'doneeye'. ")
            audio('Eyes.mp3.mp3', 'doneeye')
            a_eye = time()
            log("Rub eye at ")
        if time() - a_excersie > execrisetime:
            print("Its time to do some workout. To stop Enter 'doneworkout'. ")
            audio('gym.mp3.mp3', 'doneworkout')
            a_excersie= time()
            log("workout at ")

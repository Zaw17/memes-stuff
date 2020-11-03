import webbrowser 
import os  
from gtts import gTTS
import random
import time 

def talkToMe(audio):
    "speaks audio passed as argument"

    print(audio)
    for line in audio.splitlines():
        os.system("say " + audio)

greetings = ["Hi","Hello", "What's up"]
ran = random.choice(greetings)
talkToMe(ran)
talkToMe("What is your name?")
name1 = input()

talkToMe("I ain\t never seen two pretty best friends, it\’s always one of them gotta be ugly")

webbrowser.open("https://www.youtube.com/watch?v=CBCpjJufWME")
time.sleep(1)
talkToMe("Enjoy " + name1)
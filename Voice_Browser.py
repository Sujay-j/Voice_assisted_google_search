import numpy as np
import pandas as pd
import speech_recognition as sr
from time import ctime
import webbrowser
import time
import os
import random
import playsound
from gtts import gTTS
r = sr.Recognizer()
def Record_audio(ask=False):
    with sr.Microphone() as source:
        #print("say something")
        if ask:
            honey_speak(ask)
        audio = r.listen(source)
        voice_data=''
        try:
            voice_data = r.recognize_google(audio)
            #honey_speak(voice_data)
        except sr.UnknownValueError:
            honey_speak("Sorry , i did not get that")
        except sr.RequestError:
            honey_speak("Sorry my speech service is down")
        return voice_data
def honey_speak(audio_string):
    tts=gTTS(text=audio_string,lang='en')
    r = random.randint(1,10000000)
    audio_file = 'audio-'+str(r)+'.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)
def respond(voice_data):
    if 'what is your name' in voice_data:
        honey_speak("my name is honey")
    if ' what is the time ' in voice_data:
        honey_speak(ctime())
    if 'search' in voice_data:
        search = Record_audio('what do you whant to search for')
        url='https://google.com/search?q='+search
        webbrowser.get().open(url)
        honey_speak("here is what i found for"+search)
    if 'find location' in voice_data:
        location = Record_audio('what is the location')
        url='https://google.nl/maps/place/'+location+'/&amp;'
        webbrowser.get().open(url)
        honey_speak("here is the location "+location+"  i found")
    if 'exit' in voice_data:
        honey_speak("Thank You Master")
        exit()

time.sleep(1)
while 1:
    honey_speak("How can i help you")
    voice_data = Record_audio()
    respond(voice_data)
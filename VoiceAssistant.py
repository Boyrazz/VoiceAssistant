import time

import pywhatkit

import webbrowser

import speech_recognition as sr

import pyautogui

import os

import getpass

from playsound import playsound

from gtts import gTTS

from datetime import date, datetime

import random

from ctypes import cast,POINTER

from comtypes import CLSCTX_ALL

from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))



r = sr.Recognizer()

opening_sound_chose = random.randint(0,1)

kullanici_adi = (getpass.getuser())


def speak(sening):
    tts = gTTS(text=sening, lang="en", slow=False)
    file = "answer.mp3"
    tts.save(file)
    # speeding()
    playsound(file)
    os.remove(file)
    # os.remove("speed.mp3")


def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = r.listen(source)
        voice_data = ""
        try:
            voice_data = r.recognize_google(audio, language="EN-en")
        except sr.UnknownValueError:
            print("I dont get it")
            pass
        except sr.RequestError:
            print("System Failure")
            pass
        print(voice_data)
        return voice_data


def respond(voice_data):
    if "Hello" in voice_data:
        print("Hello Sir")

    if "Search in web" in voice_data:
        word = voice_data.split("search in web", maxsplit=1)
        component = word[1]
        url = "https://www.google.com/?hl=en" + component
        webbrowser.get().open(url)

    if "who is" in voice_data:
        word = voice_data.split("who is", maxsplit =1)
        component = word[0]
        url = "https://www.google.com/?hl=en" + component
        webbrowser.get().open(url)

    if "where is" in voice_data:
        word = voice_data.split("where is", maxsplit=1)
        component = word[0]
        url = "https://www.google.com.en/maps/place/" + component
        webbrowser.get().open(url)

    if "play" in voice_data:
        word = voice_data.split("play", maxsplit=1)
        component = word[0]
        pywhatkit.playonyt(component)

    if "take a screenshot" in voice_data:
        take_ss = pyautogui.screenshot()
        f = open("screen_record.txt", "r")
        num = f.read()
        f.close()
        file_name = "ss" + num + ".jpg"
        file_path1 = 'C:\\Users\ '
        file_path1 = file_path1.rstrip()
        file_path2 = '\Desktop'
        file_path = os.path.join(file_path1 + kullanici_adi + file_path2, file_name)
        f = open("screen_record.txt", "w")
        con_num = int(num)
        con_num = con_num + 1
        con_num1 = str(con_num)
        f.write(con_num1)
        f.close()
        take_ss.save(file_path)

    if "what day is today" in voice_data:
        today = time.strftime("%A")
        today.capitalize()
        speak(today)

    if "what time is it" in voice_data:
        selection = ["The time is: ", "Let me look: "]
        clock = datetime.now().strftime("%H:%M")
        selection = random.choice(selection)
        speak(selection + clock)

    if "adjut sound" in voice_data:
        word = voice_data.split("adjut sound",maxsplit=1)
        component = word[1]
        component = component.rstrip()
        print (component)
        if component == " one":
            volume.SetMasterVolumeLevel(-50.0, None)
        if component == ' 2':
            volume.SetMasterVolumeLevel(-20.0, None)
        if component == ' 3':
            volume.SetMasterVolumeLevel(-10, None)
        if component == ' 4':
            volume.SetMasterVolumeLevel(-0, None)

    if "shutdown the computer" in voice_data:
        os.system("shutdown /s /t 1")
        
    if "close the window" in voice_data:
        pyautogui.hotkey('altleft','f4')
        pyautogui.press('enter')

    if "close program" in voice_data:
        playsound("shuttingdown.mp3")
        exit()

def test(wake):
    if"jarvis" in wake:
        playsound("DING.mp3")
        wake = record_audio()
        if wake != '':
            voice_data = wake.lower()
            respond(voice_data)

if opening_sound_chose == 1:
    playsound("activate_sound.mp3")
else:
    playsound("geridonus.mp3")

while True:
    wake = record_audio()
    if wake != '':
        wake = wake.lower()
        test(wake)

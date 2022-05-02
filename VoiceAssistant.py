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

acilis = random.randint(0,1)

kullanici_adi = (getpass.getuser())


def speak(string):
    tts = gTTS(text=string, lang="tr", slow=False)
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
            voice_data = r.recognize_google(audio, language="TR-tr")
        except sr.UnknownValueError:
            print("Anlayamadım")
            pass
        except sr.RequestError:
            print("Sistem Hatası")
            pass
        print(voice_data)
        return voice_data


def respond(voice_data):
    if "merhaba" in voice_data:
        print("Merhaba Efendim")

    if "internette ara" in voice_data:
        kelime = voice_data.split("internette ara", maxsplit=1)
        oge = kelime[1]
        url = "https://www.google.com.tr/search?q=" + oge
        webbrowser.get().open(url)

    if "kimdir" in voice_data:
        kelime = voice_data.split("kimdir", maxsplit =1)
        oge = kelime[0]
        url = "https://www.google.com.tr/search?q=" + oge
        webbrowser.get().open(url)

    if "nerede" in voice_data:
        kelime = voice_data.split("nerede", maxsplit=1)
        oge = kelime[0]
        url = "https://www.google.com.tr/maps/place/" + oge
        webbrowser.get().open(url)

    if "oynat" in voice_data:
        kelime = voice_data.split("oynat", maxsplit=1)
        oge = kelime[0]
        pywhatkit.playonyt(oge)

    if "ekran görüntüsü al" in voice_data:
        ekran_goruntusu = pyautogui.screenshot()
        f = open("ekran_goruntusu_kayit.txt", "r")
        num = f.read()
        f.close()
        dosya_adi = "ekran_gorüntüsü" + num + ".jpg"
        dosya_yolu1 = 'C:\\Users\ '
        dosya_yolu1 = dosya_yolu1.rstrip()
        dosya_yolu2 = '\Desktop'
        dosya_yolu = os.path.join(dosya_yolu1 + kullanici_adi + dosya_yolu2, dosya_adi)
        f = open("ekran_goruntusu_kayit.txt", "w")
        con_num = int(num)
        con_num = con_num + 1
        con_num1 = str(con_num)
        f.write(con_num1)
        f.close()
        ekran_goruntusu.save(dosya_yolu)

    if "hangi gündeyiz" in voice_data or "bugün günlerden ne" in voice_data:
        today = time.strftime("%A")
        today.capitalize()
        if today == "Monday":
            today = "Pazartesi"

        elif today == "Tuesday":
            today = "Salı"

        elif today == "Wednesday":
            today = "Çarşamba"

        elif today == "Thursday":
            today = "Perşembe"

        elif today == "Friday":
            today = "Cuma"

        elif today == "Saturday":
            today = "Cumartesi"

        elif today == "Sunday":
            today = "Pazar"

        speak(today)

    if "saat kaç" in voice_data:
        selection = ["Saat şu an: ", "Hemen bakıyorum: "]
        clock = datetime.now().strftime("%H:%M")
        selection = random.choice(selection)
        speak(selection + clock)

    if "sesi ayarla" in voice_data:
        kelime = voice_data.split("sesi ayarla",maxsplit=1)
        oge = kelime[1]
        oge = oge.rstrip()
        print (oge)
        if oge == " bir":
            volume.SetMasterVolumeLevel(-50.0, None)
        if oge == ' 2':
            volume.SetMasterVolumeLevel(-20.0, None)
        if oge == ' 3':
            volume.SetMasterVolumeLevel(-10, None)
        if oge == ' 4':
            volume.SetMasterVolumeLevel(-0, None)

    if "bilgisayarı kapat" in voice_data:
        os.system("shutdown /s /t 1")
        
    if "pencereyi kapat" in voice_data:
        pyautogui.hotkey('altleft','f4')
        pyautogui.press('enter')

    if "programı kapat" in voice_data:
        playsound("shuttingdown.mp3")
        exit()

def test(wake):
    if"ceviz" in wake:
        playsound("DING.mp3")
        wake = record_audio()
        if wake != '':
            voice_data = wake.lower()
            respond(voice_data)

if acilis == 1:
    playsound("aktive.mp3")
else:
    playsound("geridonus.mp3")

while True:
    wake = record_audio()
    if wake != '':
        wake = wake.lower()
        test(wake)

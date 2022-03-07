import time

import webbrowser

import speech_recognition as sr

import pyautogui

import os

import getpass


r = sr.Recognizer()



kullanici_adi = (getpass.getuser())



def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = r.listen(source)
        try:
            voice_data = r.recognize_google(audio, language="TR-tr")
            print(voice_data)
        except sr.UnknownValueError:
            print("Ses Algılanmadı")
        except sr.RequestError:
            print("Sistem Hatası")
        return voice_data


def respond(voice_data):
    if "merhaba" in voice_data:
        print("Merhaba Efendim")


    if "internette ara" in voice_data:
        kelime = record_audio("Ne aramak istiyorsunuz")
        url = "https://www.google.com.tr/search?q=" + kelime
        webbrowser.get().open(url)


    if "kimdir" in voice_data:
        kelime = voice_data.split("kimdir", maxsplit = 1)
        oge = kelime[0]
        url = "https://www.google.com.tr/search?q=" + oge
        webbrowser.get().open(url)


    if "nerede" in voice_data:
        kelime = voice_data.split("nerede", maxsplit=1)
        oge = kelime[0]
        url = "https://www.google.com.tr/maps/place/" + oge
        webbrowser.get().open(url)


    if "YouTube" in voice_data:
        kelime = voice_data.split("YouTube", maxsplit=1)
        oge = kelime[1]
        url = "https://www.youtube.com/results?search_query=" + oge
        webbrowser.get().open(url)
        time.sleep(5)
        pyautogui.press('tab')
        pyautogui.press('enter')


    if "Ekran görüntüsü al" in voice_data:
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

time.sleep(1)
while 1:
    voice_data = record_audio()
    respond(voice_data)
